# README Effect Images Design

## Goal

Add three public, reusable screenshots to the repository README that demonstrate what the Skill can produce for an existing Web product. Use only fictional products and data. Do not include private project names, screenshots, accounts, credentials, or business-specific fields.

## Deliverables

Create three `1600×900` PNG files under `docs/images/`:

1. `uiux-audit-overview.png`
2. `dashboard-optimization.png`
3. `responsive-validation.png`

Add an "效果示例 / Examples" section near the beginning of `README.md`. Display each image at full README width with a short caption. Label all screenshots as illustrative interfaces using fictional data.

## Visual Direction

Use a compact operational-console style:

- White surfaces on a light neutral page background
- Light borders instead of decorative shadows
- Blue for primary actions and teal for analytical highlights
- Restrained green, amber, and red semantic states
- Chinese-first labels with short English metadata where useful
- Readable typography and stable panel dimensions
- Radius between 4px and 8px except status pills
- No gradients, decorative blobs, marketing hero, or nested card stacks

## Image 1: UI/UX Audit Overview

Show a browser-like audit workspace containing:

- Repository and audit-scope header
- Four category scores: information architecture, readability, interaction, responsive/accessibility
- Severity summary
- Findings table with severity, area, evidence, impact, and recommendation
- A narrow detail panel for one selected finding

The image must communicate that the Skill produces evidence-backed analysis rather than a visual opinion.

## Image 2: Dashboard Optimization

Show a generic analytics workspace containing:

- Visible project context and data freshness
- Date, region, platform, and channel filters
- KPI strip with units and comparison context
- A primary trend chart
- Diagnostic findings
- A date-and-region detail table
- Source and completeness indicators

Use fictional values and generic sources such as "Attribution", "Ad Network", and "Revenue Platform". Do not reference real vendors.

## Image 3: Responsive Validation

Show desktop, tablet, and mobile frames together:

- Desktop retains sidebar, filters, KPI, chart, and table
- Tablet collapses secondary navigation and stacks the insight panel
- Mobile uses a navigation trigger, compact filters, stacked KPI, and prioritized table columns
- Include a validation checklist for overflow, text fit, keyboard focus, states, and contrast

The image must make clear that responsive support is structural, not a scaled-down desktop canvas.

## Production Method

Build a temporary deterministic HTML/CSS showcase and render each scene with a real browser at `1600×900`. Use system fonts and inline SVG only for charts and icons. Commit the PNG files, not the temporary rendering page.

Inspect every PNG at original resolution. Verify:

- Text is readable and not clipped
- No UI element overlaps another
- Charts are nonblank
- No private or real business information appears
- The three images share one visual system
- README relative paths resolve on GitHub

## Acceptance Criteria

- All three PNG files are exactly `1600×900`
- Each image remains legible when displayed at README width
- Images use fictional data and generic terminology
- README explains what each image demonstrates
- The repository Skill still passes `quick_validate.py`
- Working tree contains no temporary browser or rendering artifacts
