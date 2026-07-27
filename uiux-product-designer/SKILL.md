---
name: uiux-product-designer
description: Analyze, design, implement, and QA practical UI/UX for Chinese-first web products, data dashboards, operational consoles, interactive prototypes, and reporting tools. Use for interface audits, information architecture, user flows, design systems, frontend implementation, responsive behavior, accessibility, workflow states, and browser-based acceptance testing.
---

# UI/UX Product Designer

Design usable product workflows, not decorative screenshots. Start from user goals, data truth, permissions, states, and repeated actions before choosing visual styling.

## Scope

Apply this skill to SaaS workspaces, admin consoles, analytics dashboards, operational tools, reports, and interactive prototypes. Cover UI design, UX flow, frontend implementation, and verification as one connected process.

Do not use it as the primary skill for brand identity, advertising creative, illustration, native mobile conventions, gameplay, 3D scenes, or backend-only work. Combine it with a specialist skill when those concerns dominate.

## Choose The Workflow

- **Audit only**: inspect and report; do not edit until the user confirms.
- **Design specification**: define journeys, screens, states, tokens, components, and acceptance criteria.
- **Implementation**: inspect the repository first, follow its stack and patterns, implement the real workflow, and verify it in a browser.
- **End-to-end redesign**: audit before changing structure; identify migration risks and preserve working behavior.

Load only the references needed:

- Read [design-system.md](references/design-system.md) when defining or reviewing visual tokens.
- Read [layout-patterns.md](references/layout-patterns.md) for shells, forms, detail pages, and responsive composition.
- Read [interaction-patterns.md](references/interaction-patterns.md) for filters, dialogs, feedback, permissions, and destructive actions.
- Read [dashboard-patterns.md](references/dashboard-patterns.md) for KPI, chart, table, diagnostic, and data-trust patterns.
- Read [uiux-checklist.md](references/uiux-checklist.md) before final acceptance or during a comprehensive audit.

## Inspect Inputs

1. Read repository instructions, package files, routes, styles, components, tests, screenshots, PRD, and design documentation.
2. Identify users, roles, primary tasks, data sources, permissions, and destructive actions.
3. Record target devices, viewports, languages, browsers, and accessibility expectations.
4. Separate verified requirements from assumptions.
5. Preserve existing changes and avoid unrelated refactors.
6. Ask before changing auth, billing, deletion behavior, privacy boundaries, production data, migrations, or deployment.

## Analyze The Product

1. Map routes, navigation levels, page inventory, and entry points.
2. Map critical journeys from entry to a verifiable successful outcome.
3. Inventory shells, forms, filters, tables, charts, dialogs, status, and feedback components.
4. Extract typography, spacing, radius, border, shadow, color, breakpoint, and motion tokens.
5. Inspect loading, empty, error, partial, stale, permission, success, and destructive states.
6. Test keyboard navigation, focus visibility, semantics, contrast, zoom, overflow, and text wrapping.
7. Compare documented behavior with implemented behavior.
8. Rank findings by severity, affected workflow, evidence, and corrective action.

## Design Pages

For each workflow:

1. State the user goal and success condition.
2. Place the page in the information architecture.
3. Identify required data, controls, decisions, roles, and dependencies.
4. Define the state matrix before visual polish.
5. Design the primary path, then recovery and exception paths.
6. Preserve relevant context between screens.
7. Use URL state for shareable filters, tabs, search, and selected entities when appropriate.
8. Expose active filters, pending changes, saved state, and reset behavior.
9. Separate destructive actions and require impact-aware confirmation.
10. Remove marketing copy and visible usage tutorials from operational screens.

## Generate A Design System

Define semantic tokens before styling screens:

- Background, surface, border, text, action, success, warning, danger, and information colors.
- Chinese-friendly typography with explicit size, weight, and line height.
- A 4px-based spacing scale with a deliberately small vocabulary.
- Compact desktop controls and mobile touch targets of at least 44px.
- Restrained 4–8px radii for operational interfaces.
- Shadows only when elevation communicates interaction or layering.
- Stable chart colors with sufficient distinction and non-color indicators.

Use at least 14px for normal main-content text unless density is tested and justified. Keep table text normally at 12–14px. Do not scale font size directly with viewport width. Derive the palette from the product context; never force a reference project's brand colors.

## Implement The Frontend

- Follow the repository's framework, component system, tokens, and routing conventions.
- Build the usable workflow as the first screen, not a marketing page.
- Separate page composition, domain logic, data access, and low-level UI primitives.
- Avoid giant client components and accumulating global CSS overrides.
- Use typed props and structured data models.
- Keep secrets and privileged actions server-only.
- Use familiar icons with accessible names or tooltips.
- Keep controls, tables, boards, and charts dimensionally stable.
- Make controls functional; never ship visual-only filters or buttons.
- Never present demo values as live data.
- Expose source, freshness, unit, timezone, and completeness for analytical data.
- Implement loading, empty, error, partial, stale, permission, success, and retry behavior.

## Make It Responsive

Design desktop-first without locking the document to a desktop width. Verify at least:

- 1440×1024 standard desktop
- 1280×720 compact desktop
- 768×1024 tablet
- 390×844 mobile

Use content-driven breakpoints. Collapse secondary panels, move navigation into a drawer, stack forms, prioritize table columns, and keep horizontal scrolling inside data surfaces. Do not set a large `min-width` on `body`, hide active filters without a summary, or shrink text to solve overflow.

## Meet Accessibility Requirements

- Use semantic headings, landmarks, forms, labels, tables, and buttons.
- Support keyboard interaction and visible `focus-visible` states.
- Give icon-only controls accessible names.
- Do not encode status with color alone.
- Provide chart summaries and textual access to critical values.
- Announce asynchronous success and failure with live regions.
- Preserve useful behavior at 200% zoom.
- Respect reduced motion.
- Validate contrast for text, controls, charts, and disabled states.

Treat automated checks as supporting evidence, not accessibility certification.

## Verify Before Completion

1. Complete the primary journeys without hidden instructions.
2. Check navigation and workspace or project context.
3. Validate form errors and preservation of recoverable input.
4. Confirm filters update data consistently and can be reset.
5. Check required table sorting, filtering, pagination, and date context.
6. Match each chart to its analytical question and show units, legends, tooltips, and empty states.
7. Exercise loading, empty, error, partial, stale, permission, success, and destructive states.
8. Inspect all target viewport screenshots for overlap, clipping, and unreadable text.
9. Run targeted tests, typecheck, lint, and build when available.
10. Check relevant browser console and network errors.

Run `python3 scripts/validate-uiux.py <project-path>` for advisory static checks, then perform browser verification.

## Format Outputs

For an audit, report:

1. Context and assumptions.
2. Information architecture and journey map.
3. Findings ordered by severity.
4. Evidence with file, route, or screenshot references.
5. Reusable patterns and project-specific constraints.
6. Recommended implementation phases.
7. Acceptance criteria and unresolved risks.

For a design specification, report the user goal, page hierarchy, component inventory, interaction/state matrix, tokens, responsive behavior, accessibility requirements, and implementation notes.

For implementation, report changed files, verified workflows, test results, and residual risks.

Use the templates in `assets/templates/` when a structured deliverable is useful.

## Avoid These Errors

- Do not create decorative landing pages for operational product requests.
- Do not use decorative gradients, blobs, oversized heroes, excessive cards, or nested cards without a functional reason.
- Do not use tiny typography to simulate information density.
- Do not hide controls or filters without preserving active state.
- Do not create charts that fail to answer a user question.
- Do not hand-roll complex chart, table, date, or accessibility behavior when a proven existing library fits.
- Do not enable destructive actions without impact explanation and confirmation.
- Do not depend on hover for essential information.
- Do not claim mobile support based on horizontal page scrolling.
- Do not claim completion without browser and viewport evidence.
- Do not copy private brands, accounts, datasets, screenshots, credentials, or business terminology into reusable assets.
