# Layout Patterns

Use these patterns according to the user's task and information density.

## Application Shell

For an operational workspace:

- Keep global identity and workspace switching in the top-level shell.
- Group navigation by user task, not by database entity.
- Keep the current workspace or project visible.
- Allow independent navigation scrolling when the menu is long.
- Put account, notifications, help, and status in predictable locations.
- On mobile, replace fixed side navigation with a drawer.

Avoid a marketing hero as the first view of an authenticated product.

## Standard Analysis Page

Use this order unless the analytical task demands otherwise:

1. Page title, context, freshness, and clear actions
2. Global filters and active-filter summary
3. KPI strip
4. Primary trend or comparison
5. Diagnostic, ranking, or explanatory panel
6. Detailed table
7. Methodology or data-quality notes

Keep sections unframed or separated by simple borders. Do not turn every section into a floating card.

## List And Detail

Use a list-detail pattern for diagnosis, tasks, entities, quality issues, and approvals:

- Keep search, filters, status, and counts with the list.
- Preserve selected-item context.
- Show evidence before recommendations.
- Provide next actions near the detail outcome.
- Use a drawer only when the detail is secondary and can be dismissed safely.
- Use a full page when the detail has deep navigation or multiple workflows.

## Forms And Settings

- Group fields by user intent rather than data model.
- Put stable identity before optional configuration.
- Mark required fields explicitly.
- Show validation near the field and a page summary when necessary.
- Preserve dirty state and warn before losing changes.
- Keep security and destructive actions in a clearly separated final section.
- Use staged setup for complex connectors or imports.

## Tables

- Keep the table as the source-of-truth surface.
- Use a sticky header for long tables.
- Freeze identifying columns only when horizontal comparison requires it.
- Set column width and alignment by data type.
- Right-align numeric values; keep units in headers or formatted values.
- Provide sorting on fields users compare.
- Use pagination or virtualization for large datasets.
- On mobile, prioritize columns, offer a detail view, or constrain horizontal scrolling to the table.

## Responsive Composition

At wide desktop, use multiple columns only when simultaneous comparison matters. At compact desktop, collapse secondary content before shrinking core content. At tablet and mobile:

- Stack filters and forms.
- Move secondary insight panels below the primary data.
- Use drawers for navigation and optional details.
- Replace wide KPI rows with a stable two-column or one-column grid.
- Keep important actions visible without making a permanent floating obstruction.

Do not hide an active control solely because the viewport narrows.
