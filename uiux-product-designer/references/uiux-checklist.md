# UI/UX Acceptance Checklist

Use this checklist for audits and before claiming implementation complete.

## Product And Flow

- [ ] Primary users, roles, goals, and success conditions are explicit.
- [ ] Entry, primary path, recovery path, and completion state exist.
- [ ] Navigation reflects the user's mental model.
- [ ] Workspace, project, or account context remains visible.
- [ ] Permission boundaries are understandable and enforced server-side.
- [ ] Destructive actions explain impact and recoverability.

## Information Hierarchy

- [ ] Each page has one clear purpose and primary heading.
- [ ] Primary actions are distinguishable from secondary actions.
- [ ] Repeated sections follow a consistent order.
- [ ] Critical status and freshness are visible without opening details.
- [ ] Operational screens contain task-oriented copy rather than feature promotion.

## Visual System

- [ ] Semantic color tokens replace arbitrary component colors.
- [ ] Main content and tables remain readable at target density.
- [ ] Spacing, radius, borders, shadows, and control heights are consistent.
- [ ] No decorative palette dominates the product.
- [ ] Long Chinese and English labels wrap or truncate with recovery.

## Components And Interaction

- [ ] Buttons, links, selects, toggles, and icon actions use appropriate controls.
- [ ] Filters show draft/applied state, reset, and active summary.
- [ ] Forms preserve input and explain errors.
- [ ] Menus, dialogs, and drawers manage focus and scrolling.
- [ ] Disabled controls explain non-obvious reasons.
- [ ] Feedback matches local, page-wide, or background task scope.

## Data And Dashboards

- [ ] KPI definitions, units, scope, period, and comparison are clear.
- [ ] Charts answer named questions and expose exact values.
- [ ] Tables support required dimensions, sorting, filtering, and pagination.
- [ ] Zero, unavailable, delayed, partial, and failed data are distinct.
- [ ] Source, freshness, timezone, currency, and coverage are visible.
- [ ] Exports retain applied filter and date metadata.

## States

- [ ] Loading preserves layout.
- [ ] Empty states distinguish no setup from no result.
- [ ] Errors offer a useful retry or recovery path.
- [ ] Partial and stale data remain visible but clearly labeled.
- [ ] Success is confirmed without interrupting continued work.
- [ ] Permission and destructive states are explicitly tested.

## Responsive

- [ ] 1440×1024 and 1280×720 desktop views are verified.
- [ ] 768×1024 tablet view is verified.
- [ ] 390×844 mobile view is verified.
- [ ] The document has no desktop-only minimum width.
- [ ] Navigation, filters, tables, dialogs, and charts remain usable.
- [ ] Text and controls do not overlap or clip.

## Accessibility

- [ ] Landmarks, headings, labels, and tables are semantic.
- [ ] Keyboard order and activation work.
- [ ] Focus is visible and restored after overlays.
- [ ] Icon-only controls have accessible names.
- [ ] Color is not the sole status signal.
- [ ] Async feedback uses live regions.
- [ ] Charts provide textual access to critical information.
- [ ] Contrast, zoom, and reduced motion are checked.

## Engineering Verification

- [ ] Existing repository patterns are respected.
- [ ] No giant component or duplicated CSS patch was introduced.
- [ ] Controls are functional and connected to real state.
- [ ] No private or demo data appears as live data.
- [ ] Targeted tests, typecheck, lint, and build pass.
- [ ] Browser console and relevant network errors are clean.
- [ ] Screenshots or equivalent visual evidence were inspected.
