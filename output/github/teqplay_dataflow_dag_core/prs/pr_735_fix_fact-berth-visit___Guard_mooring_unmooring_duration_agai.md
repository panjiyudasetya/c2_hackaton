---
id: github:teqplay/dataflow_dag_core:pr:735
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 735
title: 'fix(fact-berth-visit): Guard mooring/unmooring duration against inverted terminal
  visit timestamps'
author: panjiyudasetya
state: closed
date: '2026-08-10'
merged_at: '2026-08-10'
base_branch: develop
head_branch: PTO-2873
url: https://github.com/teqplay/dataflow_dag_core/pull/735
labels: []
linked_issues: []
explicit_links: []
---
# PR #735: fix(fact-berth-visit): Guard mooring/unmooring duration against inverted terminal visit timestamps

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/735  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2873`  
**Created:** 2026-08-10  
**Merged:** 2026-08-10  

## Description

### Problem

`fact_port_visit.total_mooring_duration` and `total_unmooring_duration` contained large negative values for ARA ports (`BEANR`, `NLRTM`, `NLAMS`), propagating to `silver.enriched_portcall_duration_monthly` and `gold.kpi_portcall_duration_monthly` across all months from 2023 to present.


### Root cause
In Amsterdam and Rotterdam, a single `ods_terminal_visit` record is routinely linked to multiple `ods_berth_visit` records within the same port call through `ods_terminal_visit_berth_visits`. This occurs when a vessel shifts berths within the same terminal. The terminal records one service event for the entire stay, while the ODS produces a separate berth visit for each berth position.

The mooring and unmooring durations are defined as:

```text
mooring_duration   = berth.start_timestamp − terminal.mooring_start_timestamp
unmooring_duration = terminal.mooring_end_timestamp − berth.end_timestamp
```

The CASE expressions previously only checked for `IS NOT NULL`. This resulted in two distinct failure modes:

1. **Negative values**: When a stale terminal visit with timestamps from a completely different time period is linked to a berth visit, one or both subtractions can produce a negative interval. These values accumulate through `SUM` in `add_berths_summary.sql` and are eventually written to `fact_port_visit`, producing totals as large as −16,000 hours.

2. **Overcounting**: When the terminal visit window chronologically contains multiple berth visits, all of them pass the `IS NOT NULL` check. As a result, every berth receives the full mooring and unmooring operation duration instead of only the duration belonging to the corresponding berth visit.

### Fix

Two layered guards added to `payload_fact_berth_visit` in both affected files:

- **Ordering guard**; Used to compute `mooring_duration` only when `mooring_start_timestamp < berth.start_timestamp`; And compute `unmooring_duration` only when `mooring_end_timestamp > berth.end_timestamp`. Prevents negatives.

- **Rank guard**; A new `ranked_berth_visit` CTE ranks berth visits within each terminal group by `start_timestamp` (ascending) and `end_timestamp` (descending). `mooring_duration` is attributed only to `mooring_rank = 1` (first berth); `unmooring_duration` only to `unmooring_rank = 1` (last berth). Prevents overcounting.

- **`NULL` safety for BARGE**; `ORDER BY end_timestamp DESC` defaults to `NULLS FIRST` in PostgreSQL. BARGE vessel type permits null `end_timestamp`. A null-end BARGE berth was claiming `unmooring_rank=1`, failing the timestamp comparison, and excluding all completed berths in that terminal group. Fixed by explicit `NULLS LAST` on both window `ORDER BY` clauses.
 
- **Deterministic tiebreaker**; Equal timestamps within a partition made `ROW_NUMBER` non-deterministic. The fact load and QC check could pick different peers, producing false accuracy failures. Fixed by appending `id ASC` as a stable tiebreaker.

- **Guard-aware ranking**; `ROW_NUMBER` is evaluated before the timestamp guard. A stale berth link with an earlier `start_timestamp` could claim `mooring_rank=1`, fail the guard, and force a valid berth to rank 2 where the rank guard silences it. Fixed by joining `ods_terminal_visit` into `ranked_berth_visit` and using a `CASE` expression in the window `ORDER BY`: non-qualifying berths receive `NULL` and sort last via `NULLS LAST;` only chronologically valid berths compete for rank 1. The redundant `LEFT JOIN ods_terminal_visit` in `payload_fact_berth_visit` is removed.

### Files changed

- `teqplay/templates/sql/dml/fact/berth_visit/prepare_mooring_unmooring.sql`
- `teqplay/templates/sql/quality_control/accuracy/berth_visit/mooring_components.sql`

### Required follow-up

This fix prevents new incorrect values but does not self-heal existing data. A full backfill is required after merge:

1. Re-run `fact_berth_visit` + `fact_port_visit` pipeline for `BEANR`, `NLRTM`, `NLAMS` from 2023-01-01
2. `REFRESH MATERIALIZED VIEW silver.enriched_portcall_duration_monthly`
3. Re-run `gold__kpi_monthly_refresh` for the affected port/month combinations

## Commits

- `ac22dbae` **Panji Y. Wiwaha** (2026-08-10): fix(fact-berth-visit): guard mooring/unmooring duration against inverted terminal visit timestamps
  A single terminal visit in ods_terminal_visit_berth_visits is often linked
  to multiple berth visits within the same port call (e.g. when a vessel shifts
  berths within a terminal). The mooring/unmooring duration formulas previously
  only checked for IS NOT NULL, so every berth visit that did not own the mooring
  operation received a negative interval — mooring_end predated berth_end, or
  mooring_start postdated berth_start. These negatives accumulated via SUM in
  add_berths_summary.sql into fact_port_visit, reaching values as large as
  −16,000 hours, and propagated into the Silver and Gold KPI layers.
  
  Fix: add temporal ordering guards to both affected files so each CASE returns
  interval '0 seconds' when the terminal visit timestamps do not enclose the
  berth visit window. Only the berth visit that owns the mooring operation
  produces a non-zero duration; intermediate berths in a shifting sequence
  correctly receive zero.
  
  Affected files:
  - dml/fact/berth_visit/prepare_mooring_unmooring.sql (fact pipeline)
  - quality_control/accuracy/berth_visit/mooring_components.sql (QC accuracy check)
  
  A backfill of fact_berth_visit → fact_port_visit → Silver MV → Gold KPI
  is required for BEANR, NLRTM, NLAMS from 2023-01-01 to clear existing negatives.
- `2212a5b2` **Panji Y. Wiwaha** (2026-08-10): fix(fact-berth-visit): prevent overcounting when terminal visit window encloses multiple berths
  When a vessel shifts berths within the same terminal, a single terminal visit
  is linked to all berth visits in the group. If its mooring window chronologically
  encloses all of them (mooring_start < every berth_start, mooring_end > every
  berth_end), every berth satisfies the existing ordering guard and each receives
  the full mooring/unmooring operation — overcounting in fact_port_visit.
  
  Fix: introduce ranked_berth_visit CTE (ROW_NUMBER partitioned by terminal_visit_ods_id)
  so that mooring_duration is attributed only to the first berth in the group
  (earliest start_timestamp) and unmooring_duration only to the last (latest
  end_timestamp). The rank guard is applied in addition to the existing ordering guard.
  
  Applied to both the fact pipeline and the QC accuracy check.
- `a8d24ff8` **Panji Y. Wiwaha** (2026-08-10): fix(fact-berth-visit): use NULLS LAST in unmooring_rank window to protect BARGE records
  DESC ordering defaults to NULLS FIRST in PostgreSQL. A BARGE berth visit with a
  null end_timestamp (permitted by the BARGE branch) would receive unmooring_rank=1,
  then fail the mooring_end_timestamp > bv.end_timestamp comparison (null comparison
  evaluates false). Every completed berth in that terminal group would be excluded
  from unmooring_duration as a result.
  
  Fix: add NULLS LAST to both window ORDER BY clauses for symmetry and to make the
  intended null treatment explicit. The DESC NULLS LAST fix is the load-bearing
  change; ASC already defaults to NULLS LAST but is made explicit for consistency.
- `d1af8aa8` **Panji Y. Wiwaha** (2026-08-10): fix(fact-berth-visit): make ranked_berth_visit window ordering fully deterministic
  ROW_NUMBER() with ORDER BY timestamp alone is non-deterministic when two berth
  visits in the same terminal group share an equal start_timestamp or end_timestamp.
  PostgreSQL may assign rank=1 to a different peer on successive runs, so the fact
  load and the mirrored QC accuracy check can disagree on which berth visit owns
  the mooring or unmooring duration.
  
  Add id ASC as a stable tiebreaker to both window ORDER BY clauses so the winning
  row is identical across every run regardless of execution plan.
- `e2e206e8` **Panji Y. Wiwaha** (2026-08-10): fix(fact-berth-visit): make ranked_berth_visit guard-aware to prevent stale links from displacing valid berths
  Without this fix, ROW_NUMBER is evaluated before the timestamp guard. A stale
  berth link whose start_timestamp is earlier than a valid berth's can claim
  mooring_rank=1, fail the ordering guard, and force the valid berth to rank 2
  where the rank guard silences it — silently zeroing a real mooring/unmooring
  duration.
  
  Fix: join ods_terminal_visit into ranked_berth_visit and use a CASE expression
  inside the window ORDER BY. Non-qualifying berths (those that fail the
  mooring_start < berth_start or mooring_end > berth_end check) receive NULL from
  the CASE, which sorts them to the end of the partition via NULLS LAST. Only
  chronologically valid berths compete for rank 1. The redundant LEFT JOIN to
  ods_terminal_visit in payload_fact_berth_visit is removed; terminal timestamps
  are now read directly from ranked_berth_visit.
  
  m

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F735%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F735%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F735%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F735%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<details>
<summary><b>Items Reviewed</b></summary>

- ✅ Review PR #735
</details>


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-10)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-08-10)

LGTM

## Review Comments

### panjiyudasetya — 2026-08-10 on `teqplay/templates/sql/dml/fact/berth_visit/prepare_mooring_unmooring.sql`

Resolved by 2212a5b

### panjiyudasetya — 2026-08-10 on `teqplay/templates/sql/dml/fact/berth_visit/prepare_mooring_unmooring.sql`

Resolved by a8d24ff

### panjiyudasetya — 2026-08-10 on `teqplay/templates/sql/dml/fact/berth_visit/prepare_mooring_unmooring.sql`

Resolved by d1af8aa

### panjiyudasetya — 2026-08-10 on `teqplay/templates/sql/dml/fact/berth_visit/prepare_mooring_unmooring.sql`

Resolved by e2e206e

## Comments

### panjiyudasetya — 2026-08-10

augment review

### panjiyudasetya — 2026-08-10

augment review

### panjiyudasetya — 2026-08-10

 augment review

### panjiyudasetya — 2026-08-10

augment review
