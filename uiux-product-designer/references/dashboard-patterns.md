# Dashboard Patterns

## Start With The Decision

Define the question each surface answers:

- Trend: line or area chart
- Category comparison: bar chart
- Composition: stacked bar; use pie only for a few stable categories
- Distribution and relationship: scatter or quadrant chart
- Funnel: staged bars with denominator and drop-off
- Cohort or matrix: heatmap with readable legend
- Exact comparison: table

Do not choose a chart because it looks varied.

## KPI Strip

For each KPI show:

- Name
- Value and unit
- Comparison or target
- Scope and date context
- Data availability or quality state
- Optional definition tooltip

Avoid mixing incompatible periods or units in one strip. Keep KPI placement stable during loading.

## Global Filters

Use consistent dimensions across pages but disable unsupported dimensions with a reason. Show date, timezone, and applied scope. Keep project or workspace context outside metric filters.

When filters affect data from multiple sources, disclose coverage differences and prevent false comparisons.

## Charts

Every chart needs:

- A question-oriented title
- Unit and grain
- Legend when more than one series exists
- Tooltip or accessible detail
- Empty, partial, and loading states
- A textual summary for the critical conclusion

Use stable dimensions and avoid auto-resizing caused by labels or loading text. Do not truncate the only identifying label.

## Tables

Operational analytical tables should support the user's actual comparison task:

- Date grain
- One or two selected dimensions
- Sort direction
- Filter/search where useful
- Column visibility
- Pagination or virtualization
- Export with applied-filter metadata
- Totals only when mathematically meaningful

Label unavailable values as unavailable, not zero. Distinguish missing joins, source delays, and genuine zero activity.

## Diagnostics

Express a finding as:

1. Severity and status
2. Observed metric change
3. Scope and period
4. Evidence
5. Likely causes with confidence
6. Recommended next action
7. Destination for verification

Do not produce recommendations unsupported by visible evidence.

## Data Trust

Expose:

- Source
- Last successful update
- Latest complete date
- Timezone and currency
- Coverage and partial-data state
- Quality issue count
- Join or attribution limitations

Never blend sources silently. Define source precedence and metric ownership. Keep raw, normalized, and published states distinguishable where users operate the pipeline.

## Empty And Partial Data

Differentiate:

- No source connected
- Connected but not synchronized
- Synchronization pending
- Filters returned no rows
- Source returned no activity
- Data is incomplete
- Data failed validation

Give the next useful action for each state.
