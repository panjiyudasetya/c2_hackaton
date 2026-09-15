---
id: github:teqplay/dataflow_dag_core:pr:740
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 740
title: Pto 2899 kpi terminal sailing
author: ryan-kharisma
state: closed
date: '2026-08-18'
merged_at: '2026-08-18'
base_branch: develop
head_branch: PTO-2899_KPI_Terminal_Sailing
url: https://github.com/teqplay/dataflow_dag_core/pull/740
labels: []
linked_issues: []
explicit_links: []
---
# PR #740: Pto 2899 kpi terminal sailing

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/740  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `develop` ← `PTO-2899_KPI_Terminal_Sailing`  
**Created:** 2026-08-18  
**Merged:** 2026-08-18  

## Description

Building the "Sailing In/Out" KPI at the terminal-visit level:

1. 538f0c87 — Fact layer: sailing_in_duration/sailing_out_duration on fact_terminal_visit

New columns computed by netting overlapping ods_anchor_stop + ods_slow_moving_period time out of the existing steaming_in_duration/steaming_out_duration windows (mirrors how fact_port_visit.sailing_in/out_duration is already calculated).
Wired through prepare_steaming_in_duration.sql, prepare_steaming_out_duration.sql, proceed.sql, load_to_datamart.sql, and the temp-table DDL.
Added the ALTER TABLE ... ADD COLUMN IF NOT EXISTS migration for existing deployments.
2. f091a2cf — Silver + Gold DDL/DML

silver.enriched_terminal_visit_monthly_sailing: dimension-embedded, event-centric materialized view (one row per terminal visit where sailing in/out applies).
gold.kpi_terminal_sailing_duration_monthly: aggregated KPI table, grain terminal × visit_vessel_type × calendar_month, with totals/averages/event counts.
3. c2c1d4df — Task groups

New terminal_sailing_duration_monthly_task_groups.py: load task group, two QC checks (negative durations, event-centric validation), and metric registry registration — following the same pattern as berth_stay_duration_monthly.
4. 3db33301 — Wiring

Registered the new DDL in prepare_db's prepare_silver_tables()/prepare_gold_tables().
Added the refresh task to silver_enriched_monthly_refresh_dag.py and the KPI task group to gold_kpi_monthly_refresh_dag.py.

## Commits

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
- `88ac57a1` **ryan_at_teqplay** (2026-08-18): style(kpi-terminal-sailing): fix sqlfluff layout.indent and line-length violations
  No logic changes: reflows the sum(to_hours_duration(least(...) - greatest(...)))
  overlap expressions to satisfy layout.indent (LT02), and adds noqa: LT05 on
  lines exceeding max_line_length where wrapping would hurt readability more
  than it helps, matching the convention already used elsewhere in this file.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-18)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F740%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-18)

_No comment._

### panjiyudasetya — COMMENTED (2026-08-18)

_No comment._

### panjiyudasetya — COMMENTED (2026-08-18)

_No comment._

### ryan-kharisma — COMMENTED (2026-08-18)

_No comment._

### ryan-kharisma — COMMENTED (2026-08-18)

_No comment._

### ryan-kharisma — COMMENTED (2026-08-18)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-18)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F740%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — COMMENTED (2026-08-18)

_No comment._

### ryan-kharisma — COMMENTED (2026-08-18)

_No comment._

### panjiyudasetya — APPROVED (2026-08-18)

LGTM 🚀

## Review Comments

### panjiyudasetya — 2026-08-18 on `teqplay/tasks/prepare_db/ddl_task_groups.py`

This feedback is valid, @ryan-kharisma. Please check them out.

### panjiyudasetya — 2026-08-18 on `teqplay/templates/sql/dml/fact/terminal_visit/prepare_steaming_in_duration.sql`

Reading soft-deleted anchor events could produce an incorrect duration. Please check again.

### panjiyudasetya — 2026-08-18 on `teqplay/templates/sql/dml/fact/terminal_visit/prepare_steaming_in_duration.sql`

+1

### ryan-kharisma — 2026-08-18 on `teqplay/tasks/prepare_db/ddl_task_groups.py`

alredy addressed in 02d76619

### ryan-kharisma — 2026-08-18 on `teqplay/templates/sql/dml/fact/terminal_visit/prepare_steaming_in_duration.sql`

already addressed at this f36ac615

### ryan-kharisma — 2026-08-18 on `teqplay/templates/sql/dml/fact/terminal_visit/prepare_steaming_in_duration.sql`

already addressed at this f36ac615

### ryan-kharisma — 2026-08-18 on `teqplay/templates/sql/migration/fact/terminal_visit/schema_migration.sql`

we can re-run the data after that

### ryan-kharisma — 2026-08-18 on `teqplay/templates/sql/dml/fact/terminal_visit/proceed.sql`

FDW will be remove. so it is not relevant

## Comments

### ryan-kharisma — 2026-08-18

auggie-review

### ryan-kharisma — 2026-08-18

augment review
