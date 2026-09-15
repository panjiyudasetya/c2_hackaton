---
id: github:teqplay/dataflow_dag_core:pr:744
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 744
title: Release 1.56.0 to master
author: panjiyudasetya
state: closed
date: '2026-08-21'
merged_at: '2026-08-21'
base_branch: master
head_branch: release/1.56.0
url: https://github.com/teqplay/dataflow_dag_core/pull/744
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2898
---
# PR #744: Release 1.56.0 to master

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/744  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `release/1.56.0`  
**Created:** 2026-08-21  
**Merged:** 2026-08-21  

## Description


## [1.56.0] - 2026-08-21
### Added
- Add new KPI: Terminal Occupancy Duration (#739)
- Add new KPI: Terminal Sailing Duration (#740)
- Add Claude Code configuration (#741)

### Changed
- Change KPI Weekly Bunkering DAG wiring into a dedicated DAG for weekly refresh (#738)

### Removed
- Remove `.augment` configuration (#741)

## Commits

- `724f9d63` **Ryan Kharisma Rakhmat** (2026-08-10): Merge pull request #736 from teqplay/release/1.55.0
  Release 1.55.0 to develop
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
- `83414fa9` **Panji Y. Wiwaha** (2026-08-13): Merge pull request #738 from teqplay/chore/move-weekly-kpi-to-weekly-refresh-dag
  Chore - Fix bunkering weekly KPI DAG wiring
- `6137c7ca` **Panji Y. Wiwaha** (2026-08-13): feat(kpi-terminal-occupancy): add DDL and DML for gold.kpi_terminal_occupancy_monthly
  Grain: terminal × calendar_month (time-spine pattern — idle months produce zero rows).
  Sources: silver.enriched_berth_visit_monthly_mooring (mooring hours, visit counts)
           and silver.enriched_berth_exchange_monthly (empty quay and vessel exchange).
  port_name resolved from dim_port.name via dim_berth.port = dim_port.unlocode.
  terminal_capacity_hours = berth_count × hours_in_month (active berths from dim_berth).
- `9cecc20d` **Panji Y. Wiwaha** (2026-08-13): feat(kpi-terminal-occupancy): add load, QC, and metric registry task groups
  Provides four exports consumed by the gold refresh DAG:
    - load_kpi_terminal_occupancy_monthly: DB-to-DB SQLExecuteQueryOperator task group
    - qc_negative_metrics_validation: warns on negative occupied/exchange hours
    - qc_terminal_occupancy_rate_exceeded: warns when rate > 1.0 (signals dim_berth data issue)
    - register_kpi_terminal_occupancy_metrics: upserts 12 metric definitions into kpi_metric_registry
- `6a102f50` **Panji Y. Wiwaha** (2026-08-13): feat(kpi-terminal-occupancy): wire into prepare_db and gold_kpi_monthly_refresh DAGs
  prepare_db: add create_kpi_terminal_occupancy_monthly operator to prepare_gold_tables() chain.
  gold_kpi_monthly_refresh: import task groups, define kpi_terminal_occupancy_monthly() task group,
  append to chain() after kpi_berth_stay_duration_monthly.
- `484a645d` **Panji Y. Wiwaha** (2026-08-13): fix(kpi-terminal-occupancy): correct has_data to include exchange-only rows
  has_data was derived solely from mooring_agg, so rows with nonzero exchange
  metrics but no mooring data (visits lacking mooring timestamps) were incorrectly
  labelled as time-spine placeholders. Updated to true when either mooring_agg
  or exchange_agg has a row for the terminal/month. DDL column comment updated
  to match the corrected contract.
- `37c90364` **Panji Y. Wiwaha** (2026-08-14): Merge pull request #739 from teqplay/PTO-2898
  PTO-2898 Add monthly terminal occupancy
- `538f0c87` **ryan_at_teqplay** (2026-08-18): feat(kpi-terminal-sailing): add sailing_in/out_duration to fact_terminal_visit
  Nets overlapping anchorage and slow-moving time out of the existing
  steaming_in/out_duration window, mirroring fact_port_visit sailing_in/out
  calculation. Includes the schema migration for existing deployments.
- `f091a2cf` **ryan_at_teqplay** (2026-08-18): feat(kpi-terminal-sailing): add DDL and DML for gold.kpi_terminal_sailing_duration_monthly
  Adds silver.enriched_terminal_visit_monthly_sailing (dimension-embedded,
  event-centric) and gold.kpi_terminal_sailing_duration_monthly (terminal x
  visit_vessel_type x calendar_month, sums/averages/event counts).
- `c2c1d4df` **ryan_at_teqplay** (2026-08-18): feat(kpi-terminal-sailing): add load, QC, and metric registry task groups
- `3db33301` **ryan_at_teqplay** (2026-08-18): feat(kpi-terminal-sailing): wire into prepare_db and gold/silver refresh DAGs
- `02d76619` **ryan_at_teqplay** (2026-08-18): fix(kpi-terminal-sailing): create silver/gold KPI objects during migrations
  prepare_silver_tables()/prepare_gold_tables() only run when is_new_database=True,
  so existing deployments running migrations (is_need_run_migration=True) never
  created silver.enriched_terminal_visit_monthly_sailing or
  gold.kpi_terminal_sailing_duration_monthly, causing the scheduled refresh/load
  to fail with relation does not exist. Adds a run_kpi_migrations() step that
  re-runs their idempotent DDL as part of prepare_migrations().
- `f36ac615` **ryan_at_teqplay** (2026-08-18): fix(kpi-terminal-sailing): correct anchor/slow-moving overlap in sailing duration calc
  Two bugs in the steaming-in/out overlap subquery for sailing_in/out_duration:
  1. The BETWEEN predicate required both event endpoints inside the steaming
     window, so events that only partially overlapped (starting before or
     ending after the window) were skipped entirely instead of having their
     intersecting portion subtracted, overstating the sailing KPI. Now uses
     least(end, to) - greatest(start, from) to sum only the overlapping portion.
  2. Soft-deleted ods_anchor_stop/ods_slow_moving_period rows were read without
     filtering deleted_timestamp, so withdrawn events kept suppressing the
     published sailing duration after a visit was rebuilt. Added the missing
     deleted_timestamp IS null filters.
- `4600ee65` **Panji Y. Wiwaha** (2026-08-18): docs: clarify SQL formatting rules and add domain tag
  Adds conventions-review domain tag and expands SQL keyword/identifier
  casing rule with concrete examples for keywords, literals, and types.
- `9e8a7f0f` **Panji Y. Wiwaha** (2026-08-18): chore: remove leftover .augment rule files
  These were leftover config from the Augment AI tool, superseded by
  CLAUDE.md as the single source of guidance for this repo.
- `ff80bfba` **Panji Y. Wiwaha** (2026-08-18): Merge pull request #741 from teqplay/chore/add-dataplatform-domain
  Chore - Clean up `CLAUDE.md` and remove unused `.augment` rule files
- `88ac57a1` **ryan_at_teqplay** (2026-08-18): style(kpi-terminal-sailing): fix sqlfluff layout.indent and line-length violations
  No logic changes: reflows the sum(to_hours_duration(least(...) - greatest(...)))
  overlap expressions to satisfy layout.indent (LT02), and adds noqa: LT05 on
  lines exceeding max_line_length where wrapping would hurt readability more
  than it helps, matching the convention already used elsewhere in this file.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `52884f1a` **Ryan Kharisma Rakhmat** (2026-08-18): Merge pull request #740 from teqplay/PTO-2899_KPI_Terminal_Sailing
  Pto 2899 kpi terminal sailing
- `a3d59592` **Panji Y. Wiwaha** (2026-08-21): Bump version 1.56.0

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-21)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F744%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-21)

_No comment._

### ryan-kharisma — APPROVED (2026-08-21)

LGTM

## Review Comments

### panjiyudasetya — 2026-08-21 on `teqplay/tasks/prepare_db/migration_task_groups.py`

No need to include it in the migration path. The gold terminal occupancy object is new, so Airflow users need to enable the prepare database option to make it available instead of relying on schema migration.

## Comments
