# Interaction Patterns

## Filters

Separate draft selection from applied state when queries are expensive. Otherwise update immediately and show loading without shifting layout.

Always provide:

- Visible active state
- Reset behavior
- Dependency handling
- Empty-result feedback
- URL persistence when sharing or restoration matters
- A compact summary when secondary filters collapse

For date ranges, provide presets, explicit start/end inputs, timezone, unavailable dates, comparison range, cancel, and apply. Do not close the picker before a valid range is complete.

## Forms

- Validate on blur for field errors and on submit for completeness.
- Do not erase user input after a failed request.
- Disable repeated submission while pending.
- Show success near the changed object.
- Explain disabled actions where the reason is not obvious.
- Use selects, toggles, checkboxes, sliders, and segmented controls according to the data type.

## Dialogs And Drawers

Use dialogs for focused decisions and drawers for secondary detail that benefits from retained page context.

Support:

- A clear title and consequence
- Predictable close behavior
- Escape and focus trapping
- Initial focus on the safest useful control
- Return focus to the trigger
- Scroll containment
- Loading and error states inside the layer

Do not stack multiple dialogs.

## Destructive Actions

Before deletion or irreversible change:

1. State what will change.
2. State affected objects and downstream impact.
3. State recoverability and retention.
4. Require explicit confirmation proportional to risk.
5. Re-authorize highly sensitive actions when necessary.
6. Record an audit event where the product requires accountability.

Never rely on a red button alone as protection.

## Feedback And Status

Use:

- Inline feedback for field or local errors.
- Toasts for completed background-safe actions.
- Banners for page-wide partial, stale, or blocking conditions.
- Progress and timelines for long-running tasks.
- Persistent status for synchronization and data freshness.

Announce asynchronous feedback through an appropriate live region. Avoid success messages that disappear before users can understand the result.

## Permissions

Hide actions users should never know about only when product policy requires it. Otherwise show disabled actions with a concise reason and escalation path. Confirm authorization server-side; UI permission checks are not security boundaries.

## Loading And Recovery

- Preserve geometry with skeletons for known layouts.
- Use progress when the work has measurable stages.
- Allow retry for recoverable failures.
- Preserve last-known data when safe, label it stale, and avoid replacing the whole page with a spinner.
- Distinguish no permission, no data, no result, and system failure.

## Keyboard And Focus

Use native elements first. Ensure predictable tab order, visible focus, keyboard activation, escape behavior, and focus restoration. Never make essential information hover-only.
