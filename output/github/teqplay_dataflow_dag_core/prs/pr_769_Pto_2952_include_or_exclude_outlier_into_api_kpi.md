---
id: github:teqplay/dataflow_dag_core:pr:769
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 769
title: Pto 2952 include or exclude outlier into api kpi
author: ryan-kharisma
state: open
date: '2026-09-15'
merged_at: null
base_branch: develop
head_branch: PTO-2952_Include_or_Exclude_Outlier_into_API_KPI
url: https://github.com/teqplay/dataflow_dag_core/pull/769
labels: []
linked_issues: []
explicit_links: []
---
# PR #769: Pto 2952 include or exclude outlier into api kpi

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/769  
**State:** open | **Author:** ryan-kharisma  
**Base ← Head:** `develop` ← `PTO-2952_Include_or_Exclude_Outlier_into_API_KPI`  
**Created:** 2026-09-15  

## Description

# Outlier Exclusion for KPI Calculations

## Summary

Extends outlier exclusion to 8 gold-layer KPIs by reusing the existing per-metric outlier
flags on `fact_port_visit` (previously computed but never consumed downstream). Bare column
names now default to outlier-excluded values; a new `<field>_include_outliers` column
preserves the previous, all-inclusive value for comparison.

## Shared mechanism

`fact_port_visit` has six boolean outlier flags, each computed as `avg ± 5·stddev` per
`(port_unlocode, vessel_type)` in `fact_port_performance_analytics` /
`calculate_outlier_flags.sql`:

- `is_wait_before_arrival_within_range`
- `is_wait_during_visit_within_range`
- `is_steaming_in_within_range`
- `is_steaming_out_within_range`
- `is_moored_within_range`
- `is_shifting_within_range`

**Naming convention applied everywhere:**
- Bare column name = **outlier-excluded default** (new behavior)
- `<field>_include_outliers` = **all-inclusive** (previous behavior, preserved under a new name)
- A `NULL` flag (unscored — not enough history, or no matching visit) is treated as
  **fail-closed** (excluded from the default, same as a `false` flag)

---

## 1. `kpi_portcall_duration_monthly`

**Tables:** `silver.enriched_portcall_duration_monthly` → `gold.kpi_portcall_duration_monthly`

| Field (now outlier-excluded default) | Formula (must be `true`) |
|---|---|
| `waiting_time_before_arrival` | `is_wait_before_arrival_within_range` |
| `waiting_time_during_visit` | `is_wait_during_visit_within_range` |
| `waiting_duration` | both wait flags |
| `mooring_duration`, `unmooring_duration`, `moored_duration` | `is_moored_within_range` (one flag covers all three sub-phases) |
| `turn_around_time_duration` | **all six** flags (it sums all six components) |
| `port_visit_count`, `avg_tat_per_visit` | denominator = visits passing all six flags |

Each gained a `_include_outliers` counterpart. `pilot_duration` unchanged (no flag covers
pilotage).

---

## 2. `kpi_portcall_performance_monthly`

**Tables:** `silver.enriched_portcall_performance_monthly` → `gold.kpi_portcall_performance_monthly`

| Field | Formula |
|---|---|
| `anchorage_waiting_duration` | `is_wait_before_arrival_within_range` AND `is_wait_during_visit_within_range` |
| `inport_travel_duration` | `is_steaming_in_within_range` AND `is_steaming_out_within_range` AND `is_shifting_within_range` |
| `total_portcall_duration` | all six flags (wall-clock span of the whole visit) |
| `port_visit_count`, `avg_total_duration_per_visit` | derived from the `total_portcall_duration` gate |

`_include_outliers` counterparts added for all of the above. `pilot_waiting_duration`,
`tug_waiting_duration`, `boatmen_waiting_duration`, `bunker_waiting_duration` unchanged (no
flag covers pilot/tug/boatmen/bunker).

---

## 3. `kpi_overall_port_performance_monthly` — no code change, automatic inheritance

This table joins `enriched_portcall_performance_monthly` and
`enriched_berth_visit_monthly_mooring` by their **bare** column names
(`total_portcall_duration`, `port_visit_count`, `mooring_hours`). Since those bare names now
mean "outlier-excluded," this KPI's `avg_portcall_duration`, `port_visit_count`,
`avg_quay_occupancy_rate`, and `active_berth_count` silently became outlier-excluded too —
documented in the table/DML comments, not a separate feature build.

---

## 4. `kpi_berth_stay_duration_monthly`

**Tables:** `silver.enriched_berth_visit_monthly_stay` → `gold.kpi_berth_stay_duration_monthly`
**Join added:** `fact_berth_visit` → `fact_port_visit` via `port_visit_id` (new —
`fact_berth_visit` has no outlier infra of its own).

| Field | Formula |
|---|---|
| `total_berth_stay_hours`, `total_mooring_duration`, `total_moored_duration`, `total_unmooring_duration`, `berth_visit_count`, `vessels_served_count`, `avg_berth_stay_per_visit` | `is_moored_within_range` (looked up from the port visit) |

**Accepted approximation:** the flag is computed on the *whole port call's* total moored time
(may span multiple berth legs under one `port_visit_id`); applying it per berth-visit row is
a documented trade-off, not a genuine berth-level statistic.

---

## 5. `kpi_berth_occupancy_monthly`

**Tables:** `silver.enriched_berth_visit_monthly_mooring` → `gold.kpi_berth_occupancy_monthly`
**Join:** same `fact_port_visit` lookup via `port_visit_id`, added to this silver view
(shared with #6 below).

| Field | Formula |
|---|---|
| `jetty_occupied_hours`, `jetty_idle_hours`, `jetty_occupancy_rate`, `quay_occupied_hours`, `quay_occupancy_rate`, `vessels_served_count`, `visits_count`, `avg_mooring_hours_per_visit` | `is_moored_within_range` |

`is_idle_month`/`has_data` deliberately stay on the **all-inclusive** hours (so a month with
only outlier-flagged activity isn't misreported as idle).

---

## 6. `kpi_terminal_occupancy_monthly`

**Tables:** same `silver.enriched_berth_visit_monthly_mooring` (no new silver work — reused
#5's join) → `gold.kpi_terminal_occupancy_monthly`

| Field | Formula |
|---|---|
| `terminal_occupied_hours`, `terminal_idle_hours`, `terminal_occupancy_rate`, `vessels_served_count`, `visits_count` | `is_moored_within_range` |

**Out of scope:** `total_empty_quay_hours`, `total_vessel_exchange_hours`, `exchange_count`,
`avg_empty_quay_hours_per_exchange`, `avg_vessel_exchange_hours` (from
`enriched_berth_exchange_monthly`) — these measure the gap *between two different vessels*,
not one visit's duration, so no flag applies.

---

## 7. `kpi_anchorage_duration_monthly`

**Tables:** `silver.enriched_anchorage_duration_monthly` → `gold.kpi_anchorage_duration_monthly`
**Join added:** `fact_anchor` → `fact_port_visit` via `port_visit_id`.

| Field | Formula |
|---|---|
| `total_duration`, `avg_duration`, `min_duration`, `max_duration`, `anchorage_count` | phase-dependent (see below) |

**Formula detail:** each anchor event is classified as "before" or "during" the visit by
comparing its `start_timestamp` to `fact_port_visit.pilot_onboard_inbound_timestamp` (the
real before/during boundary used elsewhere in the fact layer), then gated on
`is_wait_before_arrival_within_range` (before) or `is_wait_during_visit_within_range`
(during). No pilot timestamp / no matching visit → fail-closed.

**Accepted approximation:** the borrowed flags measure the visit's *combined*
slow-moving + anchor wait time, not this specific anchor event; a single anchor event isn't
split across phases the way the fact layer's own duration computation does.

---

## 8. `kpi_terminal_sailing_duration_monthly`

**Tables:** `silver.enriched_terminal_visit_monthly_sailing` →
`gold.kpi_terminal_sailing_duration_monthly`
**Join added:** `fact_terminal_visit` → `fact_port_visit` via `port_visit_id`.

| Field | Formula |
|---|---|
| `total_sailing_in_duration`, `sailing_in_event_count`, `avg_sailing_in_duration` | `is_steaming_in_within_range` |
| `total_sailing_out_duration`, `sailing_out_event_count`, `avg_sailing_out_duration` | `is_steaming_out_within_range` |

This is the most direct mapping of the set — sailing-in/out duration *is* the same
"steaming in/out" concept the flags were built from, and the silver view already isolates a
single terminal-visit leg per direction, avoiding multi-row ambiguity. Also includes the
**first-ever schema migration** for this KPI (previously only had fresh-install DDL, wired
into `run_kpi_migrations`), and a fix to `qc_event_centric_validation`, which would otherwise
misfire on a legitimate row where every contributing event happened to be outlier-flagged.


## Consistent shape across all 8 changes

Every KPI change touches the same 5 layers:

1. **Silver MV** — join to `fact_port_visit` (where not already present) + gate + rename
2. **Gold DDL** — new `_include_outliers` columns + comments
3. **Gold DML** — aggregate both variants
4. **Migration** — `ALTER TABLE ADD COLUMN` for the new columns only (bare columns already
   existed in production, so they're left untouched — they simply start receiving
   outlier-excluded values on the next reload)
5. **Task-group QC + metric registry** — negative-value checks, a "clean ≤ all-inclusive"
   invariant check, and registry entries for every new column


## Commits

- `025a4392` **ryan_at_teqplay** (2026-09-11): feat(kpi): exclude outlier visits from portcall_duration_monthly metrics
  Duration/count columns (waiting_time_before_arrival, moored_duration,
  turn_around_time_duration, port_visit_count, avg_tat_per_visit, etc.)
  now default to excluding visits flagged as statistical outliers by
  fact_port_visit's existing per-metric outlier flags. The all-inclusive
  values move to new *_include_outliers columns.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `77196400` **ryan_at_teqplay** (2026-09-14): feat(kpi): exclude outlier visits from portcall_performance_monthly metrics
  anchorage_waiting_duration, inport_travel_duration, total_portcall_duration,
  and port_visit_count now default to excluding visits flagged as statistical
  outliers by fact_port_visit's existing per-metric outlier flags, mapped per
  component (wait flags for anchorage, steaming/shifting flags for travel, all
  six for the whole-visit total). All-inclusive values move to new
  *_include_outliers columns. pilot/tug/boatmen/bunker waiting durations are
  unaffected - no fact_port_visit flag covers them.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `23f81948` **ryan_at_teqplay** (2026-09-14): feat(kpi): exclude outlier visits from berth_stay_duration_monthly metrics
  fact_berth_visit has no outlier/stddev infrastructure of its own, so this
  looks up fact_port_visit's existing is_moored_within_range flag via
  port_visit_id as an approximation. total_berth_stay_hours,
  total_mooring_duration, total_moored_duration, total_unmooring_duration,
  berth_visit_count, vessels_served_count, and avg_berth_stay_per_visit now
  default to excluding berth visits whose looked-up flag was not true.
  All-inclusive values move to new *_include_outliers columns.
  
  Known caveat (accepted trade-off): the flag is computed on the whole port
  call's total moored duration, which may span multiple berth visits under
  one port_visit_id - a multi-berth port call applies one flag value to all
  of its berth visits, not a true per-berth-visit statistic.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `7a75462a` **ryan_at_teqplay** (2026-09-14): feat(kpi): exclude outlier visits from berth_occupancy_monthly metrics
  Same fact_port_visit.is_moored_within_range lookup via port_visit_id used
  for berth_stay_duration_monthly, applied to enriched_berth_visit_monthly_mooring.
  jetty_occupied_hours, jetty_idle_hours, jetty_occupancy_rate, quay_occupied_hours,
  quay_occupancy_rate, vessels_served_count, visits_count, and
  avg_mooring_hours_per_visit now default to excluding berth visits whose looked-up
  flag was not true. All-inclusive values move to new *_include_outliers columns.
  is_idle_month/has_data stay computed from the all-inclusive hours so a month with
  only outlier-flagged activity isn't misreported as idle.
  
  kpi_overall_port_performance_monthly reads this same silver view's bare
  mooring_hours column, so its quay_occupied_hours/active_berth_count now
  inherit outlier exclusion automatically (same free inheritance already
  noted for its portcall-duration component) - documented, not a new feature
  for that KPI.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `8b46a955` **ryan_at_teqplay** (2026-09-14): feat(kpi): exclude outlier visits from terminal_occupancy_monthly metrics
  Reuses the fact_port_visit.is_moored_within_range lookup already exposed on
  silver.enriched_berth_visit_monthly_mooring (via port_visit_id) for
  berth_occupancy_monthly. terminal_occupied_hours, terminal_idle_hours,
  terminal_occupancy_rate, vessels_served_count, and visits_count now default
  to excluding berth visits whose looked-up flag was not true. All-inclusive
  values move to new *_include_outliers columns. is_idle_month/has_data stay
  computed from the all-inclusive hours so a month with only outlier-flagged
  activity isn't misreported as idle.
  
  total_empty_quay_hours/total_vessel_exchange_hours/exchange_count/
  avg_empty_quay_hours_per_exchange/avg_vessel_exchange_hours (sourced from
  enriched_berth_exchange_monthly) stay out of scope - they measure the gap
  between two different vessels' visits, not a single visit's own duration,
  so no fact_port_visit flag applies.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `a31cdc99` **ryan_at_teqplay** (2026-09-15): feat(kpi): exclude outlier visits from anchorage_duration_monthly metrics
  fact_anchor has no outlier/stddev infrastructure of its own, so this reuses
  fact_port_visit's is_wait_before_arrival_within_range / is_wait_during_visit_within_range
  flags via a port_visit_id lookup. Each anchor event is classified as "before"
  or "during" the visit by comparing its start_timestamp against
  pilot_onboard_inbound_timestamp (the real before/during boundary used
  elsewhere in the fact layer), then gated on the matching flag.
  
  total_duration, avg_duration, min_duration, max_duration, and anchorage_count
  now default to excluding anchor events whose looked-up flag was not true.
  All-inclusive values move to new *_include_outliers columns.
  
  Accepted approximation (per explicit direction): the borrowed flags measure
  a visit's combined slow-moving-plus-anchor wait time being within range, not
  a specific anchor event's own duration, and a single anchor event isn't
  split across phases the way the fact layer's own duration computation does.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `c02ef579` **ryan_at_teqplay** (2026-09-15): fix(kpi): wire up unchained QC tasks for kpi_portcall_duration_monthly
  qc_efficiency_ratios_validation and qc_event_centric_validation were
  defined but never imported/chained into the DAG, so they silently never
  ran - including the outlier-exclusion invariant checks added earlier in
  this branch. Chains them in parallel after load, matching every other KPI
  task group in this file.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `8e142f53` **ryan_at_teqplay** (2026-09-15): feat(kpi): exclude outlier visits from terminal_sailing_duration_monthly metrics
  fact_terminal_visit has no outlier/stddev infrastructure of its own (the
  pre-existing fact_stdev_time_terminal_visit_monthly/_overall tables compute
  a different metric at a degenerate grain and are unused downstream), so
  this reuses fact_port_visit's is_steaming_in_within_range /
  is_steaming_out_within_range flags via a port_visit_id lookup. Unlike the
  berth-visit/anchorage cases this maps directly - sailing in/out duration is
  exactly the "steaming in"/"steaming out" concept the flags were computed
  from, and the Silver source already restricts each duration to the single
  terminal visit (first/last leg) that carries it, avoiding multi-row
  ambiguity.
  
  total_sailing_in_duration, total_sailing_out_duration, sailing_in_event_count,
  sailing_out_event_count, avg_sailing_in_duration, and avg_sailing_out_duration
  now default to excluding terminal visits whose looked-up flag was not true.
  All-inclusive values move to new *_include_outliers columns.
  
  This KPI had never needed a schema-evolution migration before (only
  fresh-install CREATE re-runs existed), so this adds the first
  migration/schema_migration.sql files for it and wires them into
  run_kpi_migrations, verified via direct TaskGroup construction since the
  DAG module itself requires an unrelated Airflow Variable not set in this
  environment.
  
  Also fixes qc_event_centric_validation's zero-activity check, which
  previously would have misfired for a row where every contributing event
  happened to be outlier-flagged (outlier-excluded counts both 0, but real
  activity existed) - it now checks the *_include_outliers counts instead.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-15)

### 🟡 Changes recommended

One or more issues must be addressed before approval.

*Get a fresh assessment by requesting another Copilot review.*

<details>
<summary>Pull request overview</summary>

This PR updates monthly KPI pipelines so default metrics exclude outliers while retaining all-inclusive values through `_include_outliers` columns and migrations.

**Changes:**
- Propagates outlier filtering through Silver views and Gold KPI loads.
- Adds schema migrations, metric registration, and QC validation.
- Updates event-centric handling and refresh orchestration.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| teqplay/templates/sql/migration/kpi/silver/terminal_visit_monthly_sailing/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/migration/kpi/gold/terminal_sailing_duration_monthly/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/migration/kpi/gold/terminal_occupancy_monthly/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/migration/kpi/gold/portcall_performance_monthly/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/migration/kpi/gold/portcall_duration_monthly/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/migration/kpi/gold/berth_stay_duration_monthly/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/migration/kpi/gold/berth_occupancy_monthly/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/migration/kpi/gold/anchorage_duration_monthly/schema_migration.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/terminal_sailing_duration_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/terminal_occupancy_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/portcall_performance_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/portcall_duration_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/overall_port_performance_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/berth_stay_duration_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/berth_occupancy_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/dml/kpi/anchorage_duration_monthly/load_kpi.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_terminal_visit_monthly_sailing.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_portcall_performance_monthly.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_stay.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_mooring.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_terminal_sailing_duration_monthly.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_terminal_occupancy_monthly.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_portcall_performance_monthly.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_overall_port_performance_monthly.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_berth_stay_duration_monthly.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_berth_occupancy_monthly.sql | Updated as part of this pull request. |
| teqplay/templates/sql/ddl/kpi/gold/kpi_anchorage_duration_monthly.sql | Updated as part of this pull request. |
| teqplay/tasks/prepare_db/migration_task_groups.py | Updated as part of this pull request. |
| teqplay/tasks/kpi/terminal_sailing_duration_monthly_task_groups.py | Updated as part of this pull request. |
| teqplay/tasks/kpi/terminal_occupancy_monthly_task_groups.py | Updated as part of this pull request. |
| teqplay/tasks/kpi/portcall_performance_monthly_task_groups.py | Updated as part of this pull request. |
| teqplay/tasks/kpi/anchorage_duration_monthly_task_groups.py | Updated as part of this pull request. |
| teqplay/dags/mart/gold_kpi_monthly_refresh_dag.py | Updated as part of this pull request. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 39/39 changed files
- **Comments generated:** 11
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

## Review Comments

### Copilot — 2026-09-15 on `teqplay/tasks/kpi/portcall_performance_monthly_task_groups.py`

The event-centric check below still uses only outlier-excluded metrics, even though this loader now deliberately preserves legitimate zero-duration and outlier-only visit cells via `all_port_visit_count` and `port_visit_count_include_outliers`. Those rows can satisfy the current all-zero predicate and produce a false DQ error every refresh. Gate this validation on the inclusive activity count (`all_port_visit_count = 0`, with the inclusive metrics used for diagnostics), as the updated portcall-duration check does.

### Copilot — 2026-09-15 on `teqplay/templates/sql/ddl/kpi/gold/kpi_overall_port_performance_monthly.sql`

This KPI is one of the eight consumers whose bare source metrics are now outlier-excluded, but the table still has no `*_include_outliers` columns for `avg_portcall_duration`, `port_visit_count`, `avg_quay_occupancy_rate`, or `active_berth_count`, and its DML never reads the all-inclusive Silver values. The existing `all_*` columns only cover zero-duration/missing records, so the previous all-inclusive KPI values are lost rather than preserved as promised. Add and populate the corresponding include-outlier columns (with migration and registry entries), or explicitly remove this KPI from the outlier-default scope.

### Copilot — 2026-09-15 on `teqplay/templates/sql/ddl/kpi/gold/kpi_portcall_performance_monthly.sql`

These new all-inclusive columns keep a port-call-performance row when every contributing visit is outlier-flagged, so its bare duration/count metrics can legitimately all be zero while `*_include_outliers` remains positive. However, `qc_event_centric_validation` for this KPI still treats all-zero bare `total_portcall_duration`, `anchorage_waiting_duration`, `pilot_waiting_duration`, and `port_visit_count` as a zero-activity row, producing a false DQ error for that valid case. Key that validator on the all-inclusive activity columns, as done for the port-call-duration KPI.

### Copilot — 2026-09-15 on `teqplay/templates/sql/ddl/kpi/silver/enriched_anchorage_duration_monthly.sql`

`fact_anchor.port_visit_id` is loaded from the parent visit key (`pv.visit_id`; see `templates/sql/dml/fact/anchor/proceed.sql:7-9`), while `fact_port_visit.port_visit_id` is a distinct primary key. This predicate consequently fails to find the flags for normal anchor events, so all new outlier-excluded anchorage values are treated as unscored and dropped; join on `fpv.visit_id`.

### Copilot — 2026-09-15 on `teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_mooring.sql`

`fact_berth_visit.port_visit_id` is the parent `fact_port_visit.visit_id` key, not `fact_port_visit.port_visit_id` (the latter is the parent table's separate primary key). With this predicate the flag lookup misses normal visits, making `mooring_hours` zero and the default occupancy/count metrics exclude all visits; join on `fpv.visit_id`.

### Copilot — 2026-09-15 on `teqplay/templates/sql/ddl/kpi/silver/enriched_berth_visit_monthly_stay.sql`

`fact_berth_visit.port_visit_id` uses the parent visit key (`fact_port_visit.visit_id`; see `templates/sql/dml/fact/port_visit/add_berths_summary.sql:37-44`), whereas `fact_port_visit.port_visit_id` is its separate primary key. This lookup misses normal parent rows, so the new mooring flag is NULL and the default berth-stay metrics exclude every visit; use `fpv.visit_id` for this join.

### Copilot — 2026-09-15 on `teqplay/templates/sql/ddl/kpi/silver/enriched_terminal_visit_monthly_sailing.sql`

`fact_terminal_visit.port_visit_id` is populated with the parent visit key (`fact_port_visit.visit_id`; see `templates/sql/dml/fact/port_visit/add_terminals_summary.sql:37-41`), while `fact_port_visit.port_visit_id` is a separate primary-key column (`templates/sql/ddl/fact/port_visit.sql:3-4,120`). This join therefore misses normal visits, leaving both new default sailing metrics unscored and fail-closed; join on `fpv.visit_id` instead.

### Copilot — 2026-09-15 on `teqplay/templates/sql/dml/kpi/overall_port_performance_monthly/load_kpi.sql`

These changed source semantics make the overall roll-up's bare portcall and occupancy values outlier-excluded, but this KPI still has no matching `*_include_outliers` columns. The existing `all_*` fields include zero-duration/ongoing activity and therefore do not preserve the prior all-inclusive completed-activity values, so this eighth KPI loses the include/exclude pair promised by the shared API contract. Add corresponding include-outlier aggregates/schema/registry entries, or explicitly define this KPI as an exception.

### Copilot — 2026-09-15 on `teqplay/templates/sql/dml/kpi/portcall_performance_monthly/load_kpi.sql`

The bare `total_portcall_duration` and `port_visit_count` are now zeroed/excluded for outlier-flagged visits, but `qc_event_centric_validation` still identifies zero-activity rows using those bare fields (and the other default metrics). A valid port/month cell whose visits are all outliers can therefore be reported as a false zero-activity row even when `port_visit_count_include_outliers`/`all_port_visit_count` is positive. Gate this QC on an all-inclusive activity count, as the other event-centric KPIs do.

### Copilot — 2026-09-15 on `teqplay/tasks/kpi/berth_occupancy_monthly_task_groups.py`

This newly added QC task is never imported or invoked by `gold_kpi_monthly_refresh_dag.py`; only `qc_null_ship_length_warn` and `qc_quay_rate_exceeded` are chained after the load. As a result, the outlier-exclusion checks are dead code and will not run for the berth occupancy KPI. Add this task to the DAG import and the parallel post-load QC chain.

### Copilot — 2026-09-15 on `teqplay/tasks/kpi/terminal_occupancy_monthly_task_groups.py`

This newly added QC task is never imported or invoked by `gold_kpi_monthly_refresh_dag.py`; the terminal occupancy chain still runs only the negative-metric and rate checks. Therefore the outlier-exclusion validation never executes for this KPI. Add this task to the DAG import and the parallel post-load QC chain.

## Comments
