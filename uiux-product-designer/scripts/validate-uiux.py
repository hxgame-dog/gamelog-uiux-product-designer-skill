#!/usr/bin/env python3
"""Advisory static UI/UX checks for common web source files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


SOURCE_SUFFIXES = {".css", ".scss", ".sass", ".less", ".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"}
IGNORED_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".output",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "vendor",
}
SEVERITY_RANK = {"info": 0, "warning": 1, "critical": 2}


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    file: str
    line: int
    message: str
    suggestion: str


@dataclass(frozen=True)
class Rule:
    code: str
    severity: str
    suffixes: frozenset[str]
    pattern: re.Pattern[str]
    message: str
    suggestion: str


RULES = (
    Rule(
        "UX001",
        "warning",
        frozenset({".css", ".scss", ".sass", ".less"}),
        re.compile(r"font-size\s*:\s*(?:[0-9]|1[01])(?:\.[0-9]+)?px\b", re.I),
        "发现小于 12px 的固定字号，可能影响后台主内容可读性。",
        "确认是否仅用于非关键元数据；正文和表格通常保持 12–14px 以上。",
    ),
    Rule(
        "UX002",
        "critical",
        frozenset({".css", ".scss", ".sass", ".less"}),
        re.compile(r"\bbody\b[^{]*\{[^}]*min-width\s*:\s*(?:[89]\d{2}|[1-9]\d{3,})px", re.I | re.S),
        "页面 body 被锁定为较大的最小宽度，移动端将产生整页横向滚动。",
        "移除页面级最小宽度，并在组件或数据表内部控制溢出。",
    ),
    Rule(
        "UX003",
        "warning",
        frozenset({".css", ".scss", ".sass", ".less"}),
        re.compile(r"transition(?:-property)?\s*:\s*all\b", re.I),
        "使用 transition: all 可能产生意外动画和性能问题。",
        "只声明需要动画的 opacity、transform、color 等属性。",
    ),
    Rule(
        "UX004",
        "warning",
        frozenset({".css", ".scss", ".sass", ".less"}),
        re.compile(r"outline\s*:\s*(?:0|none)\b", re.I),
        "发现移除焦点轮廓的样式。",
        "确保同一组件提供清晰的 :focus-visible 替代样式。",
    ),
    Rule(
        "UX005",
        "warning",
        frozenset({".jsx", ".tsx", ".vue", ".svelte", ".html", ".htm"}),
        re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*>", re.I | re.S),
        "图片元素缺少 alt 属性。",
        "为信息图片提供替代文本，为装饰图片使用空 alt。",
    ),
    Rule(
        "UX006",
        "warning",
        frozenset({".jsx", ".tsx", ".vue", ".svelte", ".html", ".htm"}),
        re.compile(r"<(?:div|span)\b(?=[^>]*\bonClick\s*=)(?![^>]*\brole\s*=)[^>]*>", re.I | re.S),
        "非交互元素绑定点击事件但缺少交互语义。",
        "优先改用 button/link；否则补充角色、键盘处理和焦点能力。",
    ),
    Rule(
        "UX007",
        "warning",
        frozenset({".jsx", ".tsx", ".vue", ".svelte", ".html", ".htm"}),
        re.compile(r"<button\b(?![^>]*(?:aria-label|title)\s*=)[^>]*>\s*<(?:[A-Z][A-Za-z0-9]*|svg)\b[^>]*>\s*</button>", re.S),
        "疑似只有图标的按钮缺少可访问名称。",
        "添加 aria-label，并为不熟悉的图标提供 tooltip。",
    ),
    Rule(
        "UX008",
        "warning",
        frozenset({".jsx", ".tsx", ".vue", ".svelte", ".html", ".htm"}),
        re.compile(r"(?:min-w-\[(?:[89]\d{2}|[1-9]\d{3,})px\]|minWidth\s*:\s*[\"']?(?:[89]\d{2}|[1-9]\d{3,}))"),
        "发现较大的组件最小宽度。",
        "确认它只作用于可横向滚动的数据表或画布，而不是页面容器。",
    ),
)


def source_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        if root.suffix.lower() in SOURCE_SUFFIXES:
            yield root
        return

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SOURCE_SUFFIXES:
            continue
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        yield path


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def inspect_file(path: Path, root: Path) -> list[Finding]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    relative = str(path.relative_to(root)) if root.is_dir() else path.name
    findings: list[Finding] = []
    suffix = path.suffix.lower()

    for rule in RULES:
        if suffix not in rule.suffixes:
            continue
        for match in rule.pattern.finditer(text):
            findings.append(
                Finding(
                    severity=rule.severity,
                    code=rule.code,
                    file=relative,
                    line=line_number(text, match.start()),
                    message=rule.message,
                    suggestion=rule.suggestion,
                )
            )
    return findings


def project_level_findings(root: Path, files: list[Path]) -> list[Finding]:
    combined_names = " ".join(path.name.lower() for path in files)
    results: list[Finding] = []

    if root.is_dir() and not any(name in combined_names for name in ("loading", "skeleton", "spinner")):
        results.append(
            Finding(
                "info",
                "UX101",
                ".",
                1,
                "未从文件名发现明确的加载状态实现。",
                "人工确认关键页面是否具有稳定的加载反馈。",
            )
        )
    if root.is_dir() and not any(name in combined_names for name in ("error", "empty", "not-found")):
        results.append(
            Finding(
                "info",
                "UX102",
                ".",
                1,
                "未从文件名发现明确的空状态或错误状态实现。",
                "人工确认无数据、无结果、无权限和系统失败是否被区分。",
            )
        )
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="要检查的项目目录或源文件")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument(
        "--fail-on",
        choices=("none", "warning", "critical"),
        default="none",
        help="达到指定严重级别时返回非零状态；默认仅报告。",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.path.expanduser().resolve()
    if not root.exists():
        print(f"路径不存在: {root}", file=sys.stderr)
        return 2

    files = list(source_files(root))
    findings = [finding for path in files for finding in inspect_file(path, root)]
    findings.extend(project_level_findings(root, files))
    findings.sort(key=lambda item: (-SEVERITY_RANK[item.severity], item.file, item.line, item.code))

    counts = {severity: sum(item.severity == severity for item in findings) for severity in SEVERITY_RANK}
    summary = {"files_scanned": len(files), "counts": counts, "findings": [asdict(item) for item in findings]}

    if args.format == "json":
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(
            f"扫描 {len(files)} 个文件："
            f"{counts['critical']} critical，{counts['warning']} warning，{counts['info']} info"
        )
        for item in findings:
            print(f"[{item.severity.upper()}] {item.code} {item.file}:{item.line}")
            print(f"  {item.message}")
            print(f"  建议：{item.suggestion}")

    if args.fail_on == "none":
        return 0
    threshold = SEVERITY_RANK[args.fail_on]
    return 1 if any(SEVERITY_RANK[item.severity] >= threshold for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
