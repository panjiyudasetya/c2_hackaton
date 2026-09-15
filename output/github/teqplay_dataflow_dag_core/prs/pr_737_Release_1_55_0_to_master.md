---
id: github:teqplay/dataflow_dag_core:pr:737
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 737
title: Release 1.55.0 to master
author: ryan-kharisma
state: closed
date: '2026-08-10'
merged_at: '2026-08-10'
base_branch: master
head_branch: release/1.55.0
url: https://github.com/teqplay/dataflow_dag_core/pull/737
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2869
- jira:PTO-2873
---
# PR #737: Release 1.55.0 to master

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/737  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `master` ← `release/1.55.0`  
**Created:** 2026-08-10  
**Merged:** 2026-08-10  

## Description


## [1.55.0] - 2026-08-10
### Added
- KPI Bunkering (#733)
- Location Fields in Fact Bunkering (#744)
### Changed
- Guard Fact Berth Visit Mooring and Unmooring duration (#735)


## Commits

- `4867f34f` **Panji Y. Wiwaha** (2026-07-23): Merge pull request #728 from teqplay/release/1.54.0
  Release 1.54.0 to develop
- `82935fff` **Panji Y. Wiwaha** (2026-08-03): Merge pull request #731 from teqplay/hotfix/1.54.1
  Release 1.54.1 to develop
- `46f0881a` **Panji Y. Wiwaha** (2026-08-05): feat(bunkering-weekly): add DDL for silver and gold bunkering_weekly tables
  Adds CREATE OR REPLACE TABLE statements for:
  - silver.enriched_bunkering_weekly
  - gold.kpi_bunkering_weekly
  
  Wires both into the prepare_silver_tables and prepare_gold_tables
  task groups in ddl_task_groups.py.
- `6c8ff5eb` **Panji Y. Wiwaha** (2026-08-05): feat(bunkering-weekly): add task group, DML, and wire into gold KPI DAG
  Introduces the full bunkering_weekly KPI pipeline:
  - bunkering_weekly_task_groups.py: load, QC (negative durations +
    event-centric), and metric registry registration tasks
  - dml/kpi/bunkering_weekly/load_kpi.sql: TRUNCATE + INSERT logic
  - gold_kpi_monthly_refresh_dag.py: adds kpi_bunkering_weekly()
    task group to the DAG chain
  
  Grain: port_unlocode × vessel_type × ship_type × calendar_week
         × berth_id × terminal_id.
  Source: silver.enriched_bunkering_weekly.
- `4a3fbd40` **Panji Y. Wiwaha** (2026-08-05): docs: add CLAUDE.md with commands, architecture, and coding standards
- `1bee0448` **Panji Y. Wiwaha** (2026-08-05): docs: add README with architecture diagrams
- `4e209051` **ryan_at_teqplay** (2026-08-05): add locations to the fact bunkering
- `195e9d74` **Panji Y. Wiwaha** (2026-08-05): fix(reconciliation): correctly diagnose deleted visits as CANCELLED
  Use LATERAL to pick the most recent queue entry per visit across all
  action types, so a DELETE action supersedes an earlier UPDATE. Add a
  diagnosis branch for action_type='DELETE' + FACTS_PROCESSING_COMPLETED
  so visits removed from fact after processing are labelled CANCELLED
  instead of AVAILABLE_IN_FACT.
- `5f26c8f5` **Panji Y. Wiwaha** (2026-08-05): fix(bunkering-weekly): wire silver MV into refresh DAG and fix terminal consistency
  - Add refresh_enriched_bunkering_weekly task to silver__enriched_monthly_refresh
    so the MV is populated before gold__kpi_monthly_refresh reads from it.
  - Fix terminal_id/terminal_name resolved from independent COALESCEs to a paired
    CASE expression, preventing rows where terminal_id is NULL ('' in Gold) while
    terminal_name is non-null due to dim_berth.terminal leaking through.
  
  m
- `18388938` **ryan_at_teqplay** (2026-08-07): add new location columns to merge delta to fact sql
- `b4be18b8` **ryan_at_teqplay** (2026-08-07): add location to fdw proceed sql
- `f8b97b28` **Panji Y. Wiwaha** (2026-08-07): Merge pull request #733 from teqplay/PTO-2869
  PTO-2869
- `11d1e2bc` **Ryan Kharisma Rakhmat** (2026-08-07): Merge pull request #734 from teqplay/PTO-2867_Add_Location_In_Fact_Bunkering
  PTO 2867 Add locations to the fact bunkering
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
- `a06e582a` **Panji Y. Wiwaha** (2026-08-10): Merge pull request #735 from teqplay/PTO-2873
  fix(fact-berth-visit): Guard mooring/unmooring duration against inverted terminal visit timestamps
- `51e0e804` **ryan_at_teqplay** (2026-08-10): Bump version 1.55.0

## Reviews

### panjiyudasetya — APPROVED (2026-08-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F737%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments
