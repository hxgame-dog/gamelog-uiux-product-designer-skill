# GameLog UI/UX Product Designer Skill

一个面向中文 Web 产品、数据后台、运营工作台、交互原型和运营报告的 Codex Skill。

它不只生成视觉稿，而是从信息架构、用户流程、数据可信度、交互状态和权限边界出发，覆盖 UI/UX 分析、页面设计、前端落地、响应式、可访问性和浏览器验收。

## 适用场景

- 审查现有 Web 产品的 UI/UX 与前端实现
- 设计数据后台、SaaS 工作台和运营控制台
- 规划页面结构、路由、导航与关键用户流程
- 建立或整理设计系统与组件规范
- 优化筛选器、表格、图表、弹窗、侧边栏和顶部导航
- 补齐加载、空状态、错误、权限、部分数据和操作反馈
- 检查桌面端、平板和移动端适配
- 为实施方案提供可验证的验收清单

## 核心原则

- 先解决真实产品流程，再处理视觉装饰
- 桌面端优先，但不通过页面锁宽伪装成响应式
- 强调中文界面的可读性、信息层级和操作反馈
- 数据看板必须披露来源、日期、时区、完整性和刷新状态
- 不把演示数据伪装成真实数据
- 不复制具体项目、品牌、账号、密钥或私有业务数据

## 安装

### 方式一：复制安装

```bash
git clone https://github.com/hxgame-dog/gamelog-uiux-product-designer-skill.git
mkdir -p ~/.codex/skills
cp -R gamelog-uiux-product-designer-skill/uiux-product-designer ~/.codex/skills/
```

重新打开 Codex 会话后，即可通过 `$uiux-product-designer` 显式调用。

### 方式二：符号链接

适合需要拉取仓库更新或参与开发的用户：

```bash
git clone https://github.com/hxgame-dog/gamelog-uiux-product-designer-skill.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/gamelog-uiux-product-designer-skill/uiux-product-designer" \
  ~/.codex/skills/uiux-product-designer
```

如果目标目录已存在，请先备份已有版本，不要直接覆盖个人修改。

## 使用示例

### UI/UX 审计

```text
$uiux-product-designer
请对当前项目进行只读 UI/UX 审计，重点检查信息架构、字体可读性、
筛选器、表格、响应式和可访问性。先不要修改代码。
```

### 页面设计

```text
$uiux-product-designer
请为一个中文数据后台设计项目管理和项目设置流程，
输出页面层级、状态矩阵、组件清单和响应式规则。
```

### 前端落地

```text
$uiux-product-designer
请基于当前仓库的技术栈实现这个工作台页面，
补齐 loading、empty、error、permission 和 mobile 状态，
并使用浏览器截图完成验收。
```

### 数据看板优化

```text
$uiux-product-designer
请检查当前看板的 KPI、图表、表格、筛选器和数据来源表达，
判断它们是否支持真实分析决策，并实施已确认的优化。
```

## 工作方式

Skill 会根据任务选择不同流程：

1. **只读审计**：分析并输出证据，不修改文件。
2. **设计规格**：定义用户目标、页面结构、状态矩阵、设计系统和验收条件。
3. **前端实现**：遵循现有技术栈实现真实流程，并完成类型、测试和浏览器验证。
4. **完整重构**：先审计再拆分阶段，避免破坏现有可用功能。

详细规则按需存放在：

- `references/design-system.md`
- `references/layout-patterns.md`
- `references/interaction-patterns.md`
- `references/dashboard-patterns.md`
- `references/uiux-checklist.md`

## 静态检查工具

Skill 包含一个无第三方依赖的辅助检查脚本：

```bash
python3 uiux-product-designer/scripts/validate-uiux.py /path/to/web-project
```

输出 JSON：

```bash
python3 uiux-product-designer/scripts/validate-uiux.py \
  /path/to/web-project \
  --format json
```

在发现严重问题时返回非零退出码：

```bash
python3 uiux-product-designer/scripts/validate-uiux.py \
  /path/to/web-project \
  --fail-on critical
```

脚本用于发现小字号、页面锁宽、焦点样式、图片替代文本、图标按钮标签等常见风险。它只是辅助工具，不能替代真实浏览器、键盘、响应式和可访问性验收。

## 输出模板

`assets/templates/` 提供：

- `design-brief.md`：产品与设计输入简报
- `screen-spec.md`：页面设计和状态规格
- `ui-audit-report.md`：按严重程度组织的审计报告

## 目录结构

```text
uiux-product-designer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── design-system.md
│   ├── layout-patterns.md
│   ├── interaction-patterns.md
│   ├── dashboard-patterns.md
│   └── uiux-checklist.md
├── assets/
│   └── templates/
└── scripts/
    └── validate-uiux.py
```

## 隐私与安全

该仓库是通用方法库，不应提交：

- 产品密钥、Token、Cookie 或登录信息
- 真实用户数据、业务日志或数据库导出
- 私有项目截图、品牌素材或未公开 PRD
- 特定客户、项目或账号配置

提交改动前建议运行：

```bash
rg -n -i 'api[_-]?key|secret|token|password|cookie|authorization' .
```

## 限制

- 静态检查不能证明页面已经可用。
- 自动化可访问性工具不能替代键盘和辅助技术测试。
- Skill 不强制某个前端框架或组件库。
- 设计规则应服从具体产品受众、任务密度和现有设计系统。

## Contributing

欢迎通过 Issue 或 Pull Request 提交通用规则、检查项、模板和真实但已脱敏的使用案例。请保持 Skill 与具体产品、品牌和私有数据解耦。

## English Quick Start

This Codex Skill audits, designs, implements, and validates practical UI/UX for web products, analytics dashboards, operational consoles, prototypes, and reports.

```bash
git clone https://github.com/hxgame-dog/gamelog-uiux-product-designer-skill.git
mkdir -p ~/.codex/skills
cp -R gamelog-uiux-product-designer-skill/uiux-product-designer ~/.codex/skills/
```

Invoke it explicitly:

```text
$uiux-product-designer Audit this dashboard for information architecture,
workflow completeness, readability, responsiveness, and accessibility.
```

The bundled validator is advisory and must be followed by browser and accessibility verification.

## License

[MIT](LICENSE)
