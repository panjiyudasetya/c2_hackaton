---
id: github:teqplay/dataflow_dag_core:pr:756
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 756
title: Release 1.58.0 to master
author: ryan-kharisma
state: closed
date: '2026-09-04'
merged_at: '2026-09-04'
base_branch: master
head_branch: release/1.58.0
url: https://github.com/teqplay/dataflow_dag_core/pull/756
labels: []
linked_issues: []
explicit_links: []
---
# PR #756: Release 1.58.0 to master

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/756  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `master` ← `release/1.58.0`  
**Created:** 2026-09-04  
**Merged:** 2026-09-04  

## Description


## [1.58.0] - 2026-09-04
### Added
- ID-token content permissions for reusable workflow jobs (#753)
- Tug Bunker Vessel Types additional support (#752)
- All Average and All StdDev value for Fact Performance Analytics (#751)

### Changed
- Eliminate deadlocks on other fact tables fia lock ordering, pool and retries (#750)
- Eliminate deadlocks on fact performance analytics (#749)


## Commits

- `42aee4dd` **Panji Y. Wiwaha** (2026-08-27): Merge pull request #747 from teqplay/release/1.57.0
  Release 1.57.0 to develop
- `717e805d` **ryan_at_teqplay** (2026-08-28): fix(port-performance-analytics): batch fact_port_visit outlier-flag update to avoid deadlocks
  update_port_visit_from_temp ran a single UPDATE over the entire vessel-type
  slice of fact_port_visit, which held its locks long enough to collide with
  the streaming pipeline's continuous writes to the same table (deadlock
  detected while updating tuple in relation fact_port_visit, incident
  2026-08-15). Replace it with a Python task that commits 5,000-row batches
  instead of one large transaction, shortening the lock window per batch, and
  add task-level retries so a batch that still loses a rare deadlock retries
  instead of failing the whole DAG run.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `c6c79745` **ryan_at_teqplay** (2026-08-28): chore(docker-compose): raise local worker cpu limit and disable triggerer
  The worker's cpus limit (1, matching the Kubernetes deployment) starves it
  locally given AIRFLOW__CELERY__WORKER_CONCURRENCY=5, causing task timeouts
  and failed healthchecks — raise it to 4 for local dev. Also comment out the
  triggerer service locally to free up resources; left in place (commented)
  so it's easy to re-enable.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `d3c22349` **ryan_at_teqplay** (2026-08-28): revert: drop local-dev docker-compose tweaks from this branch
  This branch is meant to ship without the local worker cpu/triggerer
  changes from c6c79745 — those are local-environment tweaks, not part of
  this PR's scope. Revert them here so the pushed branch doesn't include them.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `8252bf2e` **ryan_at_teqplay** (2026-08-31): refactor(port-performance-analytics): move outlier-flag SQL to template files
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `7cc85852` **Ryan Kharisma Rakhmat** (2026-08-31): Merge pull request #749 from teqplay/PTO-2967
  PTO-2967 Fix deadlock on fact performance analytics
- `1268582f` **Panji Y. Wiwaha** (2026-08-31): fix(fact-port-visit): lock rows in consistent visit_id order on all after-proceed UPDATEs
  All five after-proceed UPDATE templates for fact_port_visit now acquire
  row locks via ORDER BY visit_id FOR UPDATE before writing. Templates with
  an existing filtered_port_visits CTE have the clause added there; the
  zero-fill template, which previously had no pre-filter CTE, gains a new
  locked_rows CTE with the same batch/stream scope filter.
  
  This removes the circular-wait condition that caused deadlocks when the
  streaming DAG and batch/daily-refresh writers updated overlapping rows in
  different heap-scan orders — mirroring the fix already applied to
  update_port_visit_outlier_flags.sql (incident 2026-08-15).
- `30ad533e` **Panji Y. Wiwaha** (2026-08-31): fix(fact-port-visit): move delete_fact_port_visit to fact_sql_pool
  The streaming delete stream used streaming_sql_pool while the streaming
  update stream used fact_sql_pool. Because the pools are independent,
  DELETE and INSERT...ON CONFLICT DO UPDATE could run concurrently on
  overlapping visit_ids, causing an index/heap lock inversion deadlock.
  
  Moving only delete_fact_port_visit to fact_sql_pool serialises it with
  all UPDATE writers on that table. The other eight tables in the deletion
  chain remain on streaming_sql_pool as they are not contended.
- `426fcacd` **Panji Y. Wiwaha** (2026-08-31): fix(fact-deletions): move streaming-written table deletions to fact_sql_pool
  fact_ship_to_ship_transfers, fact_berth_visit, and fact_terminal_visit are
  all written by the streaming update stream using fact_sql_pool. Having their
  hard deletes on streaming_sql_pool allowed DELETE and INSERT...ON CONFLICT to
  run concurrently on the same rows, creating the same index/heap lock inversion
  deadlock as was present on fact_port_visit.
  
  Batch-only tables (fact_anchor, fact_bunkering, fact_pilot, fact_tug,
  fact_stdev_time_terminal_visit) remain on streaming_sql_pool — they have no
  high-frequency concurrent writers, so the overlap window with a deletion is
  too small to justify the added serialisation.
- `baceca1c` **Panji Y. Wiwaha** (2026-08-31): fix(fact-deletions): move anchor/bunkering/pilot/tug deletions to fact_sql_pool
  These four tables all use INSERT ... ON CONFLICT (id) DO UPDATE in their
  batch load path, which runs on fact_sql_pool. Having their hard deletes on
  streaming_sql_pool allows DELETE and INSERT ON CONFLICT to run concurrently,
  creating the same index/heap lock inversion deadlock (Scenario B) as the
  streaming-written tables fixed previously.
  
  fact_stdev_time_terminal_visit is intentionally left on streaming_sql_pool —
  its load templates use plain DELETE + INSERT with no ON CONFLICT clause, so
  the lock inversion mechanism does not apply.
- `f20db688` **Panji Y. Wiwaha** (2026-08-31): fix(fact-port-visit): add retries on all fact table writers as deadlock safety net
  PostgreSQL raises 40P01 when it detects and resolves a deadlock by aborting
  one transaction. Adding retries=2, retry_delay=15s on all proceed tasks
  (fact_berth_visit, fact_terminal_visit, fact_port_visit) and the five
  after-proceed UPDATE operators on fact_port_visit means an aborted
  transaction self-recovers rather than failing the DAG.
  
  This is a safety net — Fixes 1 and 2 (consistent lock ordering + pool
  consolidation) eliminate the known deadlock conditions structurally. Retries
  cover any edge case not anticipated by those fixes.
  
  update_port_visit_from_temp already carries retries=2, retry_delay=15s from
  incident 2026-08-15 and is unchanged.
- `1026abcc` **Panji Y. Wiwaha** (2026-09-01): fix(fact-operational-events): add retries to delta merge and cleanup operators
  merge_delta_to_fact (DELETE + INSERT ON CONFLICT), delete_orphaned_visits,
  and clear_delta_table now carry retries=2 / retry_delay=15 s across all four
  event types (anchor, bunkering, pilot, tug).
  
  Deadlock window: concurrent hard-deletion on fact_sql_pool can race the
  DELETE + INSERT ON CONFLICT pattern in merge_delta_to_fact; retries absorb
  transient 40P01 errors without surfacing them as DAG failures.
- `c67dbe50` **Panji Y. Wiwaha** (2026-09-01): fix(fact-sof-stream): add retries to prepare and drop-temp-tables operators
  All create_temp_tables, prepare_*, and drop_temp_tables_success/failure
  operators in load_fact_berth_visit, load_fact_terminal_visit, and
  load_fact_port_visit now carry retries=2 / retry_delay=15 s.
  
  These DATA_WAREHOUSE DDL and DML tasks can deadlock under concurrent
  DAG runs (streaming + batch) due to PostgreSQL catalog-level lock
  contention on the same schema. Retries absorb transient 40P01 errors
  without surfacing them as DAG failures.
- `1c9ed8e8` **Panji Y. Wiwaha** (2026-09-01): fix(fact-deletions): lock rows in ascending id order before hard delete to prevent index/heap inversion
  All eight hard_delete.sql templates now wrap their DELETE in a subquery
  that pre-locks the target rows in ascending id order using FOR UPDATE:
  
      DELETE FROM fact_x
      WHERE id IN (
          SELECT id FROM fact_x
          WHERE <filter>
          ORDER BY id
          FOR UPDATE
      );
  
  PostgreSQL's INSERT ... ON CONFLICT DO UPDATE scans the unique index
  (ascending key order) and then locks the heap tuple. Without this fix,
  a concurrent DELETE locks the heap tuple first, then removes the index
  entry, creating a circular lock dependency (index/heap inversion) that
  causes 40P01 errors. Pre-locking in the same ascending order as the
  index eliminates the cycle.
  
  Sharing fact_sql_pool limits total concurrent fact-table DB operations
  (resource management) but does not serialize tasks unless slots=1, so
  the pool assignment alone cannot prevent the inversion. Updated pool
  comments to reflect this accurately.
  
  Affected tables: fact_port_visit, fact_berth_visit, fact_terminal_visit,
  fact_ship_to_ship_transfers, fact_anchor, fact_bunkering, fact_pilot, fact_tug.
- `8a294359` **Panji Y. Wiwaha** (2026-09-01): fix(fact-deletions): use correct ON CONFLICT column in hard_delete lock-ordering subqueries
  The previous commit used `id` as the ordering column in the FOR UPDATE
  subquery for fact_port_visit, fact_berth_visit, and fact_terminal_visit.
  These tables do not have an `id` column as the ON CONFLICT target:
  
    fact_port_visit       -> ON CONFLICT (visit_id)
    fact_berth_visit      -> ON CONFLICT (berth_visit_id)
    fact_terminal_visit   -> ON CONFLICT (terminal_visit_id)
  
  Using the wrong column would cause "column does not exist" errors for
  berth_visit and terminal_visit, and would lock in the wrong order for
  port_visit (mis-aligning with the unique index INSERT ON CONFLICT scans).
  
  Each template now selects and orders by the same column the INSERT ON
  CONFLICT index scan uses, so lock acquisition order is consistent and
  the circular dependency cannot form.
- `e36493de` **Panji Y. Wiwaha** (2026-09-01): Merge pull request #750 from teqplay/PTO-2967
  PTO-2967 Eliminate deadlocks on fact tables via lock ordering, pool consolidation, and retries
- `c2846a81` **ryan_at_teqplay** (2026-09-01): add new columns for all avg and stddev
- `8ebfe0bd` **ryan_at_teqplay** (2026-09-01): add all for mooring
- `a25320ca` **ryan_at_teqplay** (2026-09-01): fix(port-performance-analytics): add all_average/all_stddev for remaining 5 metrics, fix invalid GROUP BY
  Extends the all_average_value/all_standard_deviation pattern from Moored to
  Shifting, SteamingIn, SteamingOut, WaitDuringVisit and WaitBeforeArrival:
  average_value/standard_deviation stay scoped to occurred events (duration > 0),
  while all_average_value/all_standard_deviation cover every visit in the period
  with NULL duration coalesced to 0.
  
  Also fixes calculate_moored.sql, which grouped by port_unlocode while selecting
  the raw (ungrouped) duration column - invalid in Postgres and would fail at
  run time. All 6 calculate_*.sql templates now split into a base CTE, an
  all-visits aggregate, and a >0-filtered aggregate, joined on port_unlocode.
- `0b6d95f8` **ryan_at_teqplay** (2026-09-01): fix(port-performance-analytics): load all_average/all_stddev into fact_port_performance_analytics
  load_to_datamart.sql was only inserting average_value/standard_deviation for
  all 6 metrics, silently dropping all_average_value/all_standard_deviation even
  though those columns are NOT NULL on fact_port_performance_analytics - the
  insert only worked at all because the columns didn't exist in any upstream
  temp table until now. Wires them through for every metric branch, coalesced
  to 0 on insert (temp columns are nullable when a port has zero matching
  visits), and keeps them in sync on conflict.
- `0b07c6be` **ryan_at_teqplay** (2026-09-01): fix(port-performance-analytics): backfill all_average/all_stddev on migration to avoid NotNullViolation
  ADD COLUMN ... NOT NULL with no DEFAULT fails immediately on a non-empty
  table (psycopg2.errors.NotNullViolation: column "all_average_value" ...
  contains null values) - fact_port_performance_analytics already has rows in
  every environment this migration runs against. Add with DEFAULT 0 to backfill
  existing rows, then drop the default so future inserts must supply a value
  explicitly, matching average_value/standard_deviation and the vessel_type
  column earlier in this same migration file. The backfilled 0s are a
  placeholder only: fact_port_performance_analytics is fully deleted and
  reloaded per vessel_type by load_to_datamart.sql, so the next
  load_performance_analytics run overwrites them with real values.
  
  Verified by running the migration against the local MART DB directly.
- `ea1fe0c2` **ryan_at_teqplay** (2026-09-02): fix sqlfluff linter
- `7e5bb0a4` **Ryan Kharisma Rakhmat** (2026-09-02): Merge pull request #751 from teqplay/PTO-2981
  Pto 2981
- `56c69500` **Panji Y. Wiwaha** (2026-09-02): feat(vessel-type): add TUG and BUNKER as first-class vessel types
  Add TUG and BUNKER ClassVar constants to VesselType, update VALID_TYPES,
  and expose five new properties that encode each type's completeness and
  validation rules:
  
    requires_port_completeness      -- SEA_VESSEL only
    requires_terminal_completeness  -- SEA_VESSEL only
    requires_berth_completeness     -- SEA_VESSEL and BUNKER
    requires_sof_completion         -- SEA_VESSEL only (must have end timestamp)
    requires_slow_moving_periods    -- SEA_VESSEL only
  
  These properties will be consumed by sof_validate_metadata.sql (Delivery 2)
  and the stream routing layer (Delivery 3), keeping all vessel-type rules in
  a single authoritative location rather than scattered across SQL and Python.
- `bfa214be` **Panji Y. Wiwaha** (2026-09-02): feat(ddl): extend vessel_type CHECK constraints to include TUG and BUNKER
  - Extend inline CHECK constraints on stg_statement_of_fact and
    sof_processing_queue to accept 'TUG' and 'BUNKER' in addition to the
    existing 'SEA_VESSEL' and 'BARGE' values.
  - Add migrations/add_tug_bunker_vessel_types.sql: an idempotent ALTER TABLE
    migration (DROP CONSTRAINT IF EXISTS + ADD CONSTRAINT) that upgrades the
    constraints on both tables in already-running environments.
  - Register the migration as a new task (migrate_add_tug_bunker_vessel_types)
    in prepare_tables(), sequenced between prepare_sof_processing_queue and
    prepare_vessel_operational_queue.
- `4eb153f6` **Panji Y. Wiwaha** (2026-09-02): fix(sof-service): make _is_sof_completed vessel-type-aware
  Replace the hardcoded SEA_VESSEL logic with delegation to the new
  VesselType properties:
  
    - requires_slow_moving_periods=True  -> must have end + non-empty slowMovingPeriods
    - requires_sof_completion=True       -> must have end timestamp
    - both False (BARGE, TUG, BUNKER)    -> always considered complete
  
  SEA_VESSEL behaviour is unchanged. BARGE, TUG, and BUNKER records are
  accepted unconditionally at ingestion time; infrastructure-level completeness
  checks for BUNKER are handled in Delivery 2 (sof_validate_metadata.sql).
- `064fed8d` **Panji Y. Wiwaha** (2026-09-02): fix(ods-dml): apply NULL-safe sof.end predicate to all ODS batch queries
  TUG and BUNKER SOFs may have no end time. The previous predicate
    AND ((sof.end ->> 'time')::timestamp) > %(start)s
  evaluates to NULL when sof.end IS NULL, which PostgreSQL treats as FALSE,
  silently dropping all in-progress visits from batch runs.
  
  Replace with the NULL-safe form across all 11 ODS stg_to_ods templates:
    AND (
        sof.end IS NULL
        OR ((sof.end ->> 'time')::timestamp) > %(start)s
    )
  
  Also adds scenario (e) to the overlap comment in each file to document
  the new case.
  
  Affected templates: anchor_stop, berth_visit, encounter, lock_stop,
  port_visit, ship_to_ship_transfers, slow_moving_period, terminal_visit,
  tug_event, unclassified_stop, visited_approach_area.
- `7ed8d757` **Panji Y. Wiwaha** (2026-09-02): fix(qc-completeness): apply NULL-safe ss.end predicate to all completeness QC queries
  Mirror the same NULL-safe fix applied to ODS DML templates: a NULL sof.end
  (ongoing visit) would cause the record to be excluded from the staging-vs-ODS
  comparison, producing a false completeness gap.
  
  Replace with the NULL-safe form across all 6 completeness QC templates:
    AND (
        ss.end IS NULL
        OR (ss.end ->> 'time')::timestamp > '{{ start }}'
    )
  
  Also adds scenario (e) to the overlap comment in each file.
  
  Affected templates: anchor_stop, berth_visit, encounter, port_visit,
  terminal_visit, tug_event.
- `0c0eace1` **Panji Y. Wiwaha** (2026-09-02): fix(sof-service): gate _is_tug_or_bunker_vessels on SEA_VESSEL type in is_sof_valid
  _is_tug_or_bunker_vessels inspects ship.categories and rejects any record
  whose ship is categorised as TUG or BUNKER — unconditionally, regardless of
  self._vessel_type. This meant that instantiating SOFService(vessel_type='TUG')
  and feeding it a real tug SOF would have is_sof_valid return False on every
  record, making the new VesselType constants dead code.
  
  Fix: restructure is_sof_valid to only call _is_tug_or_bunker_vessels when
  self._vessel_type.is_sea_vessel is True. For all other vessel types the
  completion check is the sole gate (which for BARGE, TUG, and BUNKER always
  returns True). The _is_tug_or_bunker_vessels method itself is unchanged and
  will be removed in Delivery 3 once the stream routing layer is updated.
- `546eed02` **Panji Y. Wiwaha** (2026-09-02): fix(qc-macro): apply NULL-safe end-time predicate in filter_by_time_range
  The macro compared column_name_end > start directly. When column_name_end
  IS NULL (an ongoing visit with no recorded end time), Postgres evaluates the
  comparison as NULL, which is treated as FALSE, silently excluding the row.
  
  This caused a guaranteed staging-vs-ODS mismatch: compare_staging_vs_ods.sql
  (staging side) was fixed to include NULL-end rows, but prepare_ods_data.sql
  (ODS side) called this macro and still filtered them out.
  
  Replace with the NULL-safe form:
    (column_name_end IS NULL OR column_name_end > start)
  
  Also adds scenario (e) to the overlap comment to document the new case.
  All six prepare_ods_data.sql callers pick up the fix automatically.
- `2401007e` **Panji Y. Wiwaha** (2026-09-02): refactor(sof): update docstrings and remove dead code after vessel-type expansion
  - SOFService class and __init__ docstrings updated to list all four vessel
    types (SEA_VESSEL, BARGE, TUG, BUNKER) with their respective behaviours.
  
  - Drop the dead requires_sof_completion arm from _is_sof_completed: both
    requires_slow_moving_periods and requires_sof_completion were True only for
    SEA_VESSEL, so the second branch was unreachable. The single
    requires_slow_moving_periods check covers all current cases.
  
  - Remove VesselType.requires_sof_completion: the property had no callers
    after the dead arm was dropped. The remaining four completeness properties
    (requires_port_completeness, requires_terminal_completeness,
    requires_berth_completeness, requires_slow_moving_periods) are consumed in
    Delivery 2 (sof_validate_metadata.sql) and Delivery 1 respectively.
- `b01bbbf5` **Panji Y. Wiwaha** (2026-09-02): fix(sql-linter): use lowercase for NULL end-time checks
- `1d912d8b` **Panji Y. Wiwaha** (2026-09-02): fix(sql-linter): use correct NULL-safe predicate for JSONB end-time column
  The previous fix used `sof.end IS null` / `ss.end IS null` to detect
  absent end times. This is wrong for JSONB columns: when the API returns
  JSON null for the `end` field, dumps_with_decimal serializes it as the
  string 'null', which PostgreSQL stores as the JSONB value null -- not SQL
  NULL. Consequently `sof.end IS null` evaluates to false, and the
  timestamp comparison `(sof.end ->> 'time')::timestamp > %(start)s` then
  returns SQL NULL (falsy), silently excluding the row.
  
  Replace the column-level IS null check with a key-extraction check:
  
    (sof.end ->> 'time') IS null
  
  Key extraction on a JSONB null value returns SQL NULL, so this correctly
  handles SQL NULL, JSONB null, and objects missing the 'time' key -- the
  three ways an absent end time can appear in the staging table.
  
  Affected: 11 ODS stg_to_ods templates and 6 QC completeness
  compare_staging_vs_ods templates. The filter_by_time_range macro is
  unaffected (it operates on ODS timestamp columns, not JSONB).
- `a877ec94` **Panji Y. Wiwaha** (2026-09-02): fix(migrations): wire vessel-type constraint migration into prepare_migrations()
  The migrate_add_tug_bunker_vessel_types operator was only reachable via
  prepare_tables(), which is skipped on existing deployments (is_new_database=False).
  Adding the same operator to prepare_migrations() ensures existing environments
  also receive the extended CHECK constraints before any TUG/BUNKER records are
  inserted into stg_statement_of_fact or sof_processing_queue.
- `bb85e5da` **Panji Y. Wiwaha** (2026-09-02): refactor(migrations): move vessel-type constraint migrations to sql/migration/
  The add_tug_bunker_vessel_types.sql in ddl/migrations/ was cross-layer
  (staging + processing_queue) and outside the canonical migration directory.
  
  Split into per-table schema_migration.sql files following project convention:
  - migration/staging/statement_of_fact/schema_migration.sql (appended)
  - migration/processing_queue/schema_migration.sql (new)
  
  prepare_tables() no longer runs the ALTER migration — the DDL already
  creates both tables with the extended TUG/BUNKER constraint.
  prepare_migrations() now wires a dedicated run_processing_queue_migrations
  operator; the stg migration is covered by run_staging_migrations().
- `a4dbf117` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs
- `bcd9be89` **Panji Y. Wiwaha** (2026-09-03): Merge pull request #752 from teqplay/PTO-2819-pt1
  PTO-2819 Delivery 1: TUG/BUNKER vessel types, NULL-safe end-time predicates
- `d3de7b76` **Panji Y. Wiwaha** (2026-09-03): Merge pull request #753 from teqplay/add-reusable-workflow-permissions
  ci: add id-token/contents permissions for reusable workflow jobs
- `5f3252bc` **ryan_at_teqplay** (2026-09-04): Bump version 1.58.0
- `610801e8` **ryan_at_teqplay** (2026-09-04): fix typo

## Reviews

### panjiyudasetya — DISMISSED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F756%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-04)

### 🔵 Needs a closer look

It includes wide-reaching Airflow + SQL + schema migration changes that can affect pipeline correctness and production locking behavior.

<details>
<summary>Pull request overview</summary>

Release PR for **v1.58.0**, rolling up recent pipeline/warehouse changes into `master` (schema + SQL templates + Airflow task orchestration), plus CI workflow permission hardening.

**Changes:**
- Add **TUG/BUNKER vessel type** support across validation and CHECK constraints, and make SOF time-range filtering **NULL-end safe** (ongoing visits).
- Extend **fact_port_performance_analytics** with “all-visits” baselines (`all_average_value`, `all_standard_deviation`) and adjust calculation/loading templates accordingly.
- Reduce deadlock risk via **consistent row lock ordering**, **pool consolidation**, **retries**, and **batched** outlier-flag updates; add GitHub Actions job permissions for reusable workflow OIDC.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| teqplay/templates/sql/quality_control/macros/conditional_filtering.sql | Makes time-window overlap filtering NULL-end safe for QC macros. |
| teqplay/templates/sql/quality_control/completeness/tug_event/compare_staging_vs_ods.sql | QC completeness: allow NULL end time in date-range predicate. |
| teqplay/templates/sql/quality_control/completeness/terminal_visit/compare_staging_vs_ods.sql | QC completeness: allow NULL end time in date-range predicate. |
| teqplay/templates/sql/quality_control/completeness/port_visit/compare_staging_vs_ods.sql | QC completeness: allow NULL end time in date-range predicate. |
| teqplay/templates/sql/quality_control/completeness/encounter/compare_staging_vs_ods.sql | QC completeness: allow NULL end time in date-range predicate. |
| teqplay/templates/sql/quality_control/completeness/berth_visit/compare_staging_vs_ods.sql | QC completeness: allow NULL end time in date-range predicate. |
| teqplay/templates/sql/quality_control/completeness/anchor_stop/compare_staging_vs_ods.sql | QC completeness: allow NULL end time in date-range predicate. |
| teqplay/templates/sql/migration/staging/statement_of_fact/schema_migration.sql | Migration: extend stg_statement_of_fact vessel_type constraint for TUG/BUNKER. |
| teqplay/templates/sql/migration/processing_queue/schema_migration.sql | Migration: extend sof_processing_queue vessel_type constraint for TUG/BUNKER. |
| teqplay/templates/sql/migration/fact/port_performance_analytics/schema_migration.sql | Migration: add all-visits baseline columns + column comments. |
| teqplay/templates/sql/dml/ods/visited_approach_area/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/unclassified_stop/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/tug_event/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/terminal_visit/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/slow_moving_period/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/ship_to_ship_transfers/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/lock_stop/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/encounter/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/berth_visit/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/ods/anchor_stop/stg_to_ods.sql | ODS load: NULL-safe end-time filter. |
| teqplay/templates/sql/dml/fact/tug/hard_delete.sql | Fact delete: pre-lock rows in deterministic order before delete to reduce deadlocks. |
| teqplay/templates/sql/dml/fact/terminal_visit/hard_delete.sql | Fact delete: pre-lock rows by ON CONFLICT key before delete. |
| teqplay/templates/sql/dml/fact/ship_to_ship/hard_delete.sql | Fact delete: pre-lock rows in deterministic order before delete to reduce deadlocks. |
| teqplay/templates/sql/dml/fact/port_visit/hard_delete.sql | Fact delete: pre-lock rows by visit_id before delete. |
| teqplay/templates/sql/dml/fact/port_visit/add_zero_fill_to_null_duration.sql | Fact update: lock target rows consistently before zero-filling NULL durations. |
| teqplay/templates/sql/dml/fact/port_visit/add_terminals_summary.sql | Fact update: add ORDER BY/FOR UPDATE lock ordering in scoped CTE. |
| teqplay/templates/sql/dml/fact/port_visit/add_ship_to_ship_summary.sql | Fact update: add ORDER BY/FOR UPDATE lock ordering in scoped CTE. |
| teqplay/templates/sql/dml/fact/port_visit/add_shifting_inside_terminals.sql | Fact update: add ORDER BY/FOR UPDATE lock ordering in scoped CTE. |
| teqplay/templates/sql/dml/fact/port_visit/add_berths_summary.sql | Fact update: add ORDER BY/FOR UPDATE lock ordering in scoped CTE. |
| teqplay/templates/sql/dml/fact/port_performance_analytics/update_port_visit_outlier_flags.sql | New: batched/ordered update template for applying outlier flags. |
| teqplay/templates/sql/dml/fact/port_performance_analytics/update_port_visit_from_temp.sql | Removed: old single-statement bulk update (deadlock-prone). |
| teqplay/templates/sql/dml/fact/port_performance_analytics/select_pending_outlier_flags.sql | New: stable ordering query for batched outlier-flag updates. |
| teqplay/templates/sql/dml/fact/port_performance_analytics/load_to_datamart.sql | Load: include new all-visits baseline columns and upsert them. |
| teqplay/templates/sql/dml/fact/port_performance_analytics/calculate_wait_during_visit.sql | Calc: compute occurred-only + all-visits baselines. |
| teqplay/templates/sql/dml/fact/port_performance_analytics/calculate_wait_before_arrival.sql | Calc: compute occurred-only + all-visits baselines (NULL→0). |
| teqplay/templates/sql/dml/fact/port_performance_analytics/calculate_steaming_out.sql | Calc: compute occurred-only + all-visits baselines (NULL→0). |
| teqplay/templates/sql/dml/fact/port_performance_analytics/calculate_steaming_in.sql | Calc: compute occurred-only + all-visits baselines (NULL→0). |
| teqplay/templates/sql/dml/fact/port_performance_analytics/calculate_shifting.sql | Calc: compute occurred-only + all-visits baselines (NULL→0 via components). |
| teqplay/templates/sql/dml/fact/port_performance_analytics/calculate_moored.sql | Calc: compute occurred-only + all-visits baselines (NULL→0). |
| teqplay/templates/sql/dml/fact/pilot/hard_delete.sql | Fact delete: pre-lock rows in deterministic order before delete to reduce deadlocks. |
| teqplay/templates/sql/dml/fact/bunkering/hard_delete.sql | Fact delete: pre-lock rows in deterministic order before delete to reduce deadlocks. |
| teqplay/templates/sql/dml/fact/berth_visit/hard_delete.sql | Fact delete: pre-lock rows by ON CONFLICT key before delete. |
| teqplay/templates/sql/dml/fact/anchor/hard_delete.sql | Fact delete: pre-lock rows in deterministic order before delete to reduce deadlocks. |
| teqplay/templates/sql/ddl/staging/statement_of_fact.sql | DDL: expand vessel_type CHECK to include TUG/BUNKER. |
| teqplay/templates/sql/ddl/sof_processing_queue.sql | DDL: expand vessel_type CHECK to include TUG/BUNKER. |
| teqplay/templates/sql/ddl/fact/temp/port_performance_analytics.sql | Temp DDL: add all-visits baseline columns; defines outlier-flags temp table PK. |
| teqplay/templates/sql/ddl/fact/port_performance_analytics.sql | Fact DDL: add all-visits baseline columns. |
| teqplay/tasks/prepare_db/migration_task_groups.py | Orchestration: add processing queue migrations step. |
| teqplay/tasks/fact/sof/refresh_task_groups.py | Replace bulk outlier update with batched TaskFlow implementation + retries. |
| teqplay/tasks/fact/sof/main_task_groups.py | Add retries/retry_delay across fact SOF task groups to mitigate deadlock retries. |
| teqplay/tasks/fact/sof/deletion_task_groups.py | Move hard-deletes into fact_sql_pool for consistent resource/lock grouping. |
| teqplay/tasks/fact/operational_events/tug_task_groups.py | Add retries/retry_delay to tug operational event writers. |
| teqplay/tasks/fact/operational_events/pilot_task_groups.py | Add retries/retry_delay to pilot operational event writers. |
| teqplay/tasks/fact/operational_events/bunkering_task_groups.py | Add retries/retry_delay to bunkering operational event writers. |
| teqplay/tasks/fact/operational_events/anchor_task_groups.py | Add retries/retry_delay to anchor operational event writers. |
| teqplay/services/statement_of_fact.py | Update SOF validation rules to support SEA_VESSEL/BARGE/TUG/BUNKER behaviors. |
| teqplay/models/vessel_type.py | Add TUG/BUNKER constants + completeness/validation properties. |
| teqplay/__init__.py | Bump package version to 1.58.0. |
| CHANGELOG.md | Add 1.58.0 release notes. |
| .github/workflows/SBOM upload.yml | Add OIDC/contents permissions for reusable workflow job. |
</details>

<details>
<summary>Review details</summary>

### Suppressed comments (1)

**teqplay/templates/sql/migration/fact/port_performance_analytics/schema_migration.sql:56**
* Typo in column comment: "occured" → "occurred" (and subject/verb agreement).

- **Files reviewed:** 61/61 changed files
- **Comments generated:** 4
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/master?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — APPROVED (2026-09-04)

_No comment._

## Review Comments

### Copilot — 2026-09-04 on `CHANGELOG.md`

Changelog entry has a typo: "fia" should be "via".

### Copilot — 2026-09-04 on `teqplay/templates/sql/migration/fact/port_performance_analytics/schema_migration.sql`

Comment grammar is incorrect ("is include"). Consider rephrasing for clarity.

### Copilot — 2026-09-04 on `teqplay/templates/sql/migration/fact/port_performance_analytics/schema_migration.sql`

Comment header is unclear ("For a Column"). Consider a clearer label.

### Copilot — 2026-09-04 on `teqplay/templates/sql/migration/fact/port_performance_analytics/schema_migration.sql`

Typo in column comment: "occured" → "occurred" (and subject/verb agreement).

This issue also appears on line 56 of the same file.

## Comments
