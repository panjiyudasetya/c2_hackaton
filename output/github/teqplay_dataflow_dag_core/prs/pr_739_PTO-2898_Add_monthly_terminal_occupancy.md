---
id: github:teqplay/dataflow_dag_core:pr:739
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 739
title: PTO-2898 Add monthly terminal occupancy
author: panjiyudasetya
state: closed
date: '2026-08-13'
merged_at: '2026-08-14'
base_branch: develop
head_branch: PTO-2898
url: https://github.com/teqplay/dataflow_dag_core/pull/739
labels: []
linked_issues: []
explicit_links: []
---
# PR #739: PTO-2898 Add monthly terminal occupancy

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/739  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2898`  
**Created:** 2026-08-13  
**Merged:** 2026-08-14  

## Description

### Description

- Adds `gold.kpi_terminal_occupancy_monthly`, a new Layer 3 KPI table that aggregates quay occupancy and vessel exchange metrics at terminal level, one row per terminal × calendar month
- Follows the time-spine pattern — idle months produce explicit zero-value rows so gaps are visible without frontend inference
- Wires the new KPI into the existing `prepare_database` and `gold__kpi_monthly_refresh` DAGs with no new DAGs required

### Context

`gold.kpi_berth_occupancy_monthly` already provides berth-level occupancy, and `gold.kpi_overall_port_performance_monthly` provides port-level averages. This table fills the missing terminal-level view, enabling per-terminal utilisation comparisons within a port.

### What changed

**SQL layer**
- `teqplay/templates/sql/ddl/kpi/gold/kpi_terminal_occupancy_monthly.sql` — new table with PK `(terminal_id, calendar_month)`, covering index on grain columns, port-scoped index, and column comments
- `teqplay/templates/sql/dml/kpi/terminal_occupancy_monthly/load_kpi.sql` — TRUNCATE + CTE INSERT; time spine built from `dim_terminal × dim_berth × calendar_spine`; `port_name` resolved from `dim_port.name` (authoritative); `terminal_capacity_hours = berth_count × hours_in_month`

**Task group**
- `teqplay/tasks/kpi/terminal_occupancy_monthly_task_groups.py` — four exports following the standard KPI pattern:
  - `load_kpi_terminal_occupancy_monthly` — DB-to-DB load via `SQLExecuteQueryOperator`
  - `qc_negative_metrics_validation` — warns on negative occupied/exchange hours
  - `qc_terminal_occupancy_rate_exceeded` — warns when `terminal_occupancy_rate > 1.0` (signals incorrect berth count in `dim_berth`)
  - `register_kpi_terminal_occupancy_metrics` — upserts 12 metric definitions into `gold.kpi_metric_registry`

**DAG wiring**
- `teqplay/tasks/prepare_db/ddl_task_groups.py` — `create_kpi_terminal_occupancy_monthly` added to `prepare_gold_tables()` chain
- `teqplay/dags/mart/gold_kpi_monthly_refresh_dag.py` — imports, `kpi_terminal_occupancy_monthly()` task group, and `chain()` extended

### Key metrics exposed

| Column | Description |
|---|---|
| `terminal_occupied_hours` | Sum of mooring hours across all berths in the terminal |
| `terminal_capacity_hours` | `berth_count × hours_in_month` |
| `terminal_occupancy_rate` | `terminal_occupied_hours / terminal_capacity_hours` |
| `total_empty_quay_hours` | Sum of empty quay gap hours across all berths |
| `avg_empty_quay_hours_per_exchange` | Average empty quay duration per exchange event |
| `avg_vessel_exchange_hours` | Average operational handover per valid exchange pair |
| `vessels_served_count` | Distinct vessels moored across all terminal berths |

### Test plan

- [ ] Run `prepare_database` DAG and confirm `gold.kpi_terminal_occupancy_monthly` is created with correct schema
- [ ] Trigger `gold__kpi_monthly_refresh` for a 3-month window and confirm rows are produced for every active terminal × month combination in the range
- [ ] Verify idle months produce rows with `terminal_occupied_hours = 0`, `is_idle_month = true`, `has_data = false`
- [ ] Verify `terminal_occupancy_rate` does not exceed 1.0 for any terminal with correctly registered berths
- [ ] Confirm `gold.kpi_metric_registry` contains all 12 metric entries for `kpi_terminal_occupancy_monthly`
- [ ] Cross-check `SUM(terminal_occupied_hours)` for a port against `SUM(jetty_occupied_hours)` from `kpi_berth_occupancy_monthly` for the same port and month (should match when aggregated across all ship types)

## Commits

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

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-13)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F739%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-13)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-13)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-08-14)

LGTM

## Review Comments

### panjiyudasetya — 2026-08-13 on `teqplay/templates/sql/dml/kpi/terminal_occupancy_monthly/load_kpi.sql`

Resolved by 484a645

## Comments

### panjiyudasetya — 2026-08-13

augment review

### ryan-kharisma — 2026-08-14

I just curious for this PR changes, why we don't have the silver layer for terminal KPI?

### panjiyudasetya — 2026-08-14

Good question, @ryan-kharisma, Currently, the silver layer is designed to handle two expensive operations once: month-boundary clipping via `generate_series` and dimension embedding for ship type, berth, terminal, and port attributes. `silver.enriched_berth_visit_monthly_mooring` already handles both. Each berth visit is expanded by calendar month with mooring hours clipped to the month boundary, and `terminal_id` is already embedded.

Terminal occupancy can consume this output with a simple `GROUP BY terminal_id, calendar_month`, without additional row expansion or dimension joins. Introducing a dedicated `silver.enriched_terminal_occupancy_monthly` view would add infrastructure overhead, such as another materialized view to refresh and index, without reducing any meaningful complexity. The berth silver layer has already absorbed the expensive processing, so terminal occupancy only needs to aggregate the results.

Is that answer your question?

### ryan-kharisma — 2026-08-14

OK then, if it is already on berth enriched I agree.
