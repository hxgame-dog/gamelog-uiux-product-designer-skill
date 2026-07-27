# Design System Rules

Use this reference when generating, auditing, or normalizing a product design system.

## Token Order

Define tokens in this order:

1. Semantic color roles
2. Typography
3. Spacing
4. Size and density
5. Radius
6. Borders and elevation
7. Motion
8. Data visualization

Do not begin with individual component colors. Components must consume semantic roles.

## Color

Create roles for:

- `page`, `surface`, `surface-subtle`, `overlay`
- `border`, `border-strong`
- `text`, `text-muted`, `text-disabled`, `text-inverse`
- `action`, `action-hover`, `action-active`
- `success`, `warning`, `danger`, `info` and their subtle surfaces

Use neutral surfaces for most of an operational interface. Reserve saturated color for selection, action, status, and data encoding. Avoid a one-note palette dominated by one hue family.

Validate:

- Normal text contrast at least 4.5:1.
- Large text and meaningful UI boundaries at least 3:1.
- Status remains understandable without color.
- Disabled controls remain legible but clearly unavailable.

## Typography

Prefer a system or locally available font stack that supports Chinese and Latin text. Define roles rather than arbitrary values:

| Role | Typical desktop size | Guidance |
|---|---:|---|
| Page title | 24–32px | Reserve for page-level hierarchy |
| Section title | 18–22px | Use for full sections |
| Panel title | 14–16px | Keep compact in tools |
| Body | 14–16px | Default readable content |
| Table/control | 12–14px | Test at target density |
| Metadata | 12px | Never carry critical information alone |
| KPI value | 22–32px | Match available panel height |

Use explicit line heights. Keep letter spacing at `0` for Chinese product UI. Do not use viewport-width font scaling. Ensure the longest translated label fits or wraps predictably.

## Spacing And Density

Use a 4px base and a limited scale such as `4, 8, 12, 16, 20, 24, 32, 40`.

- Use 8–12px inside compact controls and table cells.
- Use 16–24px between related page groups.
- Use 24–40px between major sections.
- Keep desktop control heights around 32–40px.
- Use at least 44px touch targets on mobile.

Do not solve density by shrinking type. Reduce redundant containers, labels, and whitespace first.

## Radius, Borders, And Elevation

- Use 4–8px radii for controls, panels, and operational cards.
- Use pills only for status, compact tags, or segmented choices.
- Prefer a light 1px border over large shadows.
- Use shadows for menus, popovers, drawers, and modals where elevation matters.
- Do not place cards inside cards unless both boundaries represent real independent objects.

## Motion

Keep product motion short and functional:

- 100–160ms for hover and control feedback.
- 160–240ms for menus and panels.
- Avoid `transition: all`.
- Animate opacity and transform where possible.
- Respect `prefers-reduced-motion`.

## Chart Tokens

Define a stable categorical palette, positive/negative colors, comparison colors, grid, axis, tooltip, and selection states. Reuse metric colors across pages. Pair colors with labels, shapes, or line styles.

## Deliverable

Output tokens as a framework-neutral table first. Translate them into CSS variables, Tailwind theme values, or the repository's token format only after approval.
