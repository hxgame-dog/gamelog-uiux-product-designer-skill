# README Effect Images Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add three polished, fictional `1600×900` UI/UX showcase images to the public README.

**Architecture:** Build one deterministic temporary HTML document with three query-selected scenes. Render each scene with a real Chromium browser, commit only the PNG outputs, then reference them from the README with explicit fictional-data captions.

**Tech Stack:** HTML, CSS, inline SVG, Playwright CLI, Markdown, Python standard library, Git

---

### Task 1: Build The Deterministic Showcase

**Files:**
- Create temporarily: `/tmp/gamelog-uiux-readme-showcase.html`

- [ ] **Step 1: Create one fixed-size render document**

Implement a `1600×900` canvas selected by `?scene=audit`, `?scene=dashboard`, or `?scene=responsive`. Define shared CSS variables for neutral surfaces, borders, type, blue actions, teal analytics, and semantic states. Use only system fonts, HTML, CSS, and inline SVG.

- [ ] **Step 2: Implement the audit scene**

Render a repository audit header, four category scores, a severity summary, an evidence-backed findings table, and one selected-finding detail panel. Use generic paths such as `src/components/Filters.tsx`.

- [ ] **Step 3: Implement the dashboard scene**

Render project context, freshness, four global filters, five KPI cells, a trend chart, diagnostics, and a date-and-region table. Use fictional values and generic source labels.

- [ ] **Step 4: Implement the responsive scene**

Render desktop, tablet, and mobile frames together with a validation checklist. Demonstrate structural adaptation rather than proportional shrinking.

- [ ] **Step 5: Open each scene in Chromium**

Run:

```bash
command -v npx
npx playwright screenshot --viewport-size="1600,900" \
  "file:///tmp/gamelog-uiux-readme-showcase.html?scene=audit" \
  /tmp/audit-preview.png
```

Expected: Chromium renders a nonblank `1600×900` preview without console-visible load errors.

### Task 2: Render And Verify PNG Assets

**Files:**
- Create: `docs/images/uiux-audit-overview.png`
- Create: `docs/images/dashboard-optimization.png`
- Create: `docs/images/responsive-validation.png`

- [ ] **Step 1: Render all three assets**

Run Playwright screenshot commands for the three query-selected scenes and write directly to the three target paths.

- [ ] **Step 2: Verify dimensions**

Run:

```bash
python3 -c 'from PIL import Image; import pathlib; [print(p.name, Image.open(p).size) for p in pathlib.Path("docs/images").glob("*.png")]'
```

Expected: every output reports `(1600, 900)`. If Pillow is unavailable, use macOS `sips -g pixelWidth -g pixelHeight`.

- [ ] **Step 3: Inspect every image at original resolution**

Use the image inspection tool and check text fit, overlap, blank charts, consistent colors, and fictional content. Correct the render document and rerender any failed scene.

### Task 3: Integrate The README

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add the showcase section**

Insert an "效果示例" section after the repository introduction. Explain that all interfaces and values are fictional.

- [ ] **Step 2: Add the three images**

Use relative Markdown paths:

```markdown
![UI/UX 审计效果示例](docs/images/uiux-audit-overview.png)
![数据后台优化效果示例](docs/images/dashboard-optimization.png)
![响应式与验收效果示例](docs/images/responsive-validation.png)
```

Add one concise caption below each image explaining the capability demonstrated.

- [ ] **Step 3: Check README links**

Verify every referenced image exists and uses the exact case-sensitive path.

### Task 4: Validate And Publish

**Files:**
- Verify: `uiux-product-designer/`
- Verify: `README.md`
- Verify: `docs/images/*.png`

- [ ] **Step 1: Validate the Skill**

Run:

```bash
PYTHONPATH=/tmp/codex-skill-creator-pydeps \
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  uiux-product-designer
```

Expected: `Skill is valid!`

- [ ] **Step 2: Scan privacy and repository hygiene**

Run:

```bash
rg -n -i 'Nicety|Nexus|Cooking Legacy|Puzzle Workshop|Screw Fun|Merge Bistro|hxgames@gmail' .
git status --short
git diff --check
```

Expected: no private project matches and no temporary render document is tracked.

- [ ] **Step 3: Commit**

```bash
git add README.md docs/images docs/superpowers/plans/2026-07-27-readme-effect-images.md
git commit -m "docs: add uiux showcase images"
```

- [ ] **Step 4: Push and verify**

```bash
git push origin main
git rev-parse HEAD
git ls-remote origin refs/heads/main
```

Expected: local and remote `main` SHA values match.
