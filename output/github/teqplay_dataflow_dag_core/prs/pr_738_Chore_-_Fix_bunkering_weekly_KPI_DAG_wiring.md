---
id: github:teqplay/dataflow_dag_core:pr:738
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 738
title: Chore - Fix bunkering weekly KPI DAG wiring
author: panjiyudasetya
state: closed
date: '2026-08-13'
merged_at: '2026-08-13'
base_branch: develop
head_branch: chore/move-weekly-kpi-to-weekly-refresh-dag
url: https://github.com/teqplay/dataflow_dag_core/pull/738
labels: []
linked_issues: []
explicit_links: []
---
# PR #738: Chore - Fix bunkering weekly KPI DAG wiring

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/738  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `chore/move-weekly-kpi-to-weekly-refresh-dag`  
**Created:** 2026-08-13  
**Merged:** 2026-08-13  

## Description

### Problem

`gold.kpi_bunkering_weekly` was wired into `gold__kpi_monthly_refresh` and its upstream silver MV (`silver.enriched_bunkering_weekly`) was being refreshed inside `silver__enriched_monthly_refresh`. Both are weekly artefacts running on a monthly cadence — a clear cadence mismatch that caused the KPI to only update once a month and the default param window to be month-aligned instead of week-aligned.

Additionally, the default refresh window for both monthly and weekly KPIs was too narrow: monthly KPIs only retained 12 months of data and weekly only 8 weeks, despite both using a full `TRUNCATE + INSERT` pattern on every run.

### Changes

**New DAGs**
- `silver__enriched_weekly_refresh` — runs every Sunday at 23:00 UTC, refreshes `silver.enriched_bunkering_weekly`, then fire-and-forget triggers `gold__kpi_weekly_refresh`
- `gold__kpi_weekly_refresh` — `schedule=None` (triggered by silver weekly refresh), hosts all weekly gold KPI task groups; currently wires `kpi_bunkering_weekly`

**Rewired DAGs**
- `silver__enriched_monthly_refresh` — removed `refresh_enriched_bunkering_weekly` and the `trigger_gold__kpi_weekly_refresh` that were incorrectly placed here; restored to a clean monthly-only chain
- `gold__kpi_monthly_refresh` — removed `kpi_bunkering_weekly` task group and its imports

**Supporting changes**
- `DagID` — added `SILVER_ENRICHED_WEEKLY_REFRESH` and `GOLD_KPI_WEEKLY_REFRESH`
- `KpiWeeklyParams` — new param class with ISO-week-aligned default date range (104-week rolling window)
- `bunkering_weekly_task_groups` — switched from `KpiMonthlyParams` to `KpiWeeklyParams`
- Default refresh windows extended to **2 years** for both `KpiMonthlyParams` (12 → 24 months) and `KpiWeeklyParams` (8 → 104 weeks), since both DAGs use `TRUNCATE + INSERT` and the window determines how much history is retained on every unparameterised run

### Trigger chain after this PR

```
silver__enriched_weekly_refresh   (cron: Sundays 23:00 UTC)
  → REFRESH silver.enriched_bunkering_weekly
  → trigger gold__kpi_weekly_refresh   (schedule=None)

silver__enriched_monthly_refresh  (cron: 1st of month 01:00 UTC)
  → REFRESH all monthly silver MVs
  → trigger gold__kpi_monthly_refresh  (schedule=None)
```

## Commits

- `26ed6e27` **Panji Y. Wiwaha** (2026-08-13): feat(kpi-weekly): add SILVER/GOLD_KPI_WEEKLY_REFRESH DagIDs and KpiWeeklyParams
  Introduces the DagID entries and parameter class needed by the new weekly
  silver and gold refresh DAGs.
- `02bd15ad` **Panji Y. Wiwaha** (2026-08-13): fix(kpi-weekly): move bunkering weekly KPI from monthly to dedicated weekly gold refresh DAG
  kpi_bunkering_weekly was wired into gold__kpi_monthly_refresh despite being
  a weekly metric. Removes it from the monthly DAG and introduces
  gold__kpi_weekly_refresh (schedule=None, triggered by silver weekly refresh)
  as the correct home for all weekly gold KPI tables.
  
  Also updates bunkering_weekly_task_groups to use KpiWeeklyParams so default
  date ranges are ISO-week-aligned rather than month-aligned.
- `98db663b` **Panji Y. Wiwaha** (2026-08-13): fix(silver-weekly): move enriched_bunkering_weekly refresh out of monthly silver DAG
  silver__enriched_monthly_refresh was refreshing a weekly MV and triggering
  the gold weekly DAG — a cadence mismatch. Removes the bunkering MV refresh
  and its gold-weekly trigger from the monthly DAG, and introduces a dedicated
  silver__enriched_weekly_refresh DAG (cron: Sundays 23:00 UTC) that refreshes
  enriched_bunkering_weekly then fire-and-forget triggers gold__kpi_weekly_refresh.
- `337516f8` **Panji Y. Wiwaha** (2026-08-13): fix(kpi-params): extend default refresh window to 2 years for monthly and weekly KPIs
  KpiMonthlyParams: 12 months → 24 months (months=23 + current month).
  KpiWeeklyParams:   8 weeks → 104 weeks (weeks=103 + current week).
  
  Both DAGs use TRUNCATE + INSERT, so the default window determines how much
  history is retained on every unparameterised run.
- `32d1786a` **Panji Y. Wiwaha** (2026-08-13): fix(silver-weekly): reschedule from Sunday 23:00 to Monday 01:00 UTC
  Running on Sunday 23:00 with day_of_week=6 caused KpiWeeklyParams to select
  the Monday two weeks prior as `end`, publishing the just-ending week one full
  week late. Running on Monday 01:00 UTC (after the ISO week has fully closed at
  midnight) sets day_of_week=0, so end = today - 7 days correctly captures the
  week that just ended.

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-13)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F738%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-13)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-13)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F738%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-13)

_No comment._

### ryan-kharisma — APPROVED (2026-08-13)

LGTM

## Review Comments

### panjiyudasetya — 2026-08-13 on `teqplay/dags/mart/silver_enriched_weekly_refresh_dag.py`

resolved 32d1786

### panjiyudasetya — 2026-08-13 on `teqplay/dags/mart/silver_enriched_weekly_refresh_dag.py`

This one is irrelevant for now.

## Comments

### panjiyudasetya — 2026-08-13

augment review
