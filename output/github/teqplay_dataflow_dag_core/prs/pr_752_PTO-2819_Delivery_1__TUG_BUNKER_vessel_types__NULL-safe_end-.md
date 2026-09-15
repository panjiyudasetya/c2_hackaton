---
id: github:teqplay/dataflow_dag_core:pr:752
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 752
title: 'PTO-2819 Delivery 1: TUG/BUNKER vessel types, NULL-safe end-time predicates'
author: panjiyudasetya
state: closed
date: '2026-09-02'
merged_at: '2026-09-03'
base_branch: develop
head_branch: PTO-2819-pt1
url: https://github.com/teqplay/dataflow_dag_core/pull/752
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2819
---
# PR #752: PTO-2819 Delivery 1: TUG/BUNKER vessel types, NULL-safe end-time predicates

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/752  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2819-pt1`  
**Created:** 2026-09-02  
**Merged:** 2026-09-03  

## Description

### Description

Delivery 1 of the TUG/BUNKER SOF ingestion plan. Non-breaking — all existing SEA_VESSEL and BARGE processing is unchanged.

- **`VesselType` model** — Add `TUG` and `BUNKER` as first-class constants. Update `VALID_TYPES`. Add five new properties: `requires_port_completeness`, `requires_terminal_completeness`, `requires_berth_completeness` (consumed in Delivery 2), `requires_slow_moving_periods` (consumed now), `is_tug`, `is_bunker` (consumed in Delivery 3). Remove the now-dead `requires_sof_completion`.
- **DDL + migration** — Extend `vessel_type CHECK` constraints on `stg_statement_of_fact` and `sof_processing_queue` to accept `'TUG'` and `'BUNKER'`. New idempotent migration (`DROP CONSTRAINT IF EXISTS` + `ADD CONSTRAINT`) for already-running environments, wired into `prepare_tables()` between `prepare_sof_processing_queue` and `prepare_vessel_operational_queue`.
- **`SOFService._is_sof_completed`** — Delegates to `VesselType.requires_slow_moving_periods` instead of hardcoding SEA_VESSEL logic. BARGE/TUG/BUNKER always return `True`. SEA_VESSEL behaviour is identical to before.
- **`SOFService.is_sof_valid`** — `_is_tug_or_bunker_vessels` now only runs for `SEA_VESSEL`. Without this, `SOFService(vessel_type='TUG')` would have rejected every tug SOF regardless of `self._vessel_type`.
- **NULL-safe `sof.end` predicate** — Applied to all 11 ODS `stg_to_ods.sql` batch templates, 6 QC completeness `compare_staging_vs_ods.sql` templates, and the shared `filter_by_time_range` macro (propagates to all `prepare_ods_data.sql` callers). `NULL > value` evaluates to `NULL` in PostgreSQL — previously any SOF without an end time was silently excluded. The NULL-safe form `(col IS NULL OR col > value)` covers the new ongoing-visit scenario added to all overlap comments.

### What is NOT in this PR (future deliveries)

- Delivery 2: `sof_validate_metadata.sql` per-vessel-type completeness rules
- Delivery 3: stream routing for TUG/BUNKER, removal of `_is_tug_or_bunker_vessels`
- Delivery 4: ODS/fact table changes for TUG/BUNKER visits
- Delivery 5: KPI and QC coverage for TUG/BUNKER

### Test plan

- [ ] `pytest tests/` — no regressions on existing SEA_VESSEL and BARGE paths
- [ ] Run `prepare_database` DAG on dev — `migrate_add_tug_bunker_vessel_types` succeeds and both CHECK constraints are updated
- [ ] `VesselType('TUG')` and `VesselType('BUNKER')` no longer raise `ValueError`
- [ ] `SOFService(vessel_type='TUG').is_sof_valid({'end': {...}, 'slowMovingPeriods': [], 'ship': {'categories': {'0': 'TUG'}}})` returns `True` (was `False` before)
- [ ] Batch ODS transformation over a range that includes NULL-end staging rows — confirm they are no longer silently dropped

## Commits

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

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-02)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F752%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-02)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-02)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F752%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-02)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-02)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — COMMENTED (2026-09-02)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-02)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-02)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-02)

_No comment._

### ryan-kharisma — APPROVED (2026-09-02)

LGTM

## Review Comments

### panjiyudasetya — 2026-09-02 on `teqplay/templates/sql/dml/ods/anchor_stop/stg_to_ods.sql`

Resolved by 1d912d8

### panjiyudasetya — 2026-09-02 on `teqplay/tasks/prepare_db/ddl_task_groups.py`

Resolved by bb85e5d

### ryan-kharisma — 2026-09-02 on `teqplay/models/vessel_type.py`

for this new type of service vessel (tug and bunker) I think we need to add more boolean here to check whether it is service vessel or not.

### ryan-kharisma — 2026-09-02 on `teqplay/services/statement_of_fact.py`

I think this one can use the `is_service_vessel` boolean.

### panjiyudasetya — 2026-09-02 on `teqplay/models/vessel_type.py`

Wouldn't it be better to start with the specific vessel types covered by this card before generalizing it to all service vessels, @ryan-kharisma?

### panjiyudasetya — 2026-09-02 on `teqplay/services/statement_of_fact.py`

Same concern as in my previous reply.

### ryan-kharisma — 2026-09-02 on `teqplay/models/vessel_type.py`

ok we will do it later.

## Comments

### panjiyudasetya — 2026-09-02

augment review

### panjiyudasetya — 2026-09-02

augment review
