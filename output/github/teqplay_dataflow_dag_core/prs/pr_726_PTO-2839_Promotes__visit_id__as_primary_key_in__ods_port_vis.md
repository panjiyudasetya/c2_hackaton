---
id: github:teqplay/dataflow_dag_core:pr:726
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 726
title: PTO-2839 Promotes `visit_id` as primary key in `ods_port_visit`
author: panjiyudasetya
state: closed
date: '2026-07-17'
merged_at: '2026-07-22'
base_branch: develop
head_branch: chore/set-visit-id-as-pk
url: https://github.com/teqplay/dataflow_dag_core/pull/726
labels: []
linked_issues: []
explicit_links: []
---
# PR #726: PTO-2839 Promotes `visit_id` as primary key in `ods_port_visit`

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/726  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `chore/set-visit-id-as-pk`  
**Created:** 2026-07-17  
**Merged:** 2026-07-22  

## Description

### Description

Promotes `visit_id` (`entry_id` from SOF is a permanent, immutable identifier) to the primary key of `ods_port_visit`, replacing `id` (`generation_id` from SOF is a mutable identifier that changes with every SOF API update event). All ODS child tables' `port_visit_id` column now stores `entry_id` instead of `generation_id`.

### Motivation

`generation_id` changes every time SOF emits an update for a visit. Under the old schema this caused every SOF update to cascade-delete and re-insert all child records (terminal_visit, berth_visit, anchor_stop, etc.), which was expensive and caused transient data gaps. With `visit_id` (entry_id) as PK, an SOF update is a plain `UPDATE` on `ods_port_visit` — no cascade delete needed, child records are stable.

### What changed

**DDL (Group 1)**
- `ods_port_visit`: PK column changed from `id` to `visit_id`; the separate `UNIQUE (visit_id)` constraint was dropped (now covered by PK); `UNIQUE (visit_id, version)` kept.
- All 11 ODS child tables: FK `REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE`.
- `fact/temp/terminal_visits`: 3 FK constraints updated to reference `visit_id`.

**ODS DML (Group 2)**
- `port_visit/stg_to_ods`: `ON CONFLICT` key changed to `visit_id`; `generation_id` becomes a plain updated column.
- `port_visit/delete_changed_generation_id`: Now a no-op (kept for DAG compatibility; the Airflow task is removed in Group 3).
- All 11 child `stg_to_ods` files: `port_visit_id` populated from `entry_id`; FK existence sub-query updated to `SELECT visit_id`.
- All child `soft_delete` files: `WHERE port_visit_id` filter updated to compare against `pv.visit_id`.
- `pilot/stg_to_ods`: `JOIN ods_encounter ON e.port_visit_id = pv.visit_id` (was `pv.id`).
- `slow_moving_period/cleanup`: streaming DELETE condition updated to `pv.visit_id`.

**Airflow (Group 3)**
- `stream_task_groups.py`: `delete_changed_generation_id` task removed from the SOF streaming DAG.

**Fact layer (Group 4)**
- All `fact/port_visit/prepare_*`, `fact/terminal_visit/prepare_*`, `fact/berth_visit/prepare_*`, `fact/tug/proceed*`: ODS child joins changed from `pv.id` to `pv.visit_id` (F1 fix).
- `fact/pilot/proceed_delta.sql`: streaming delta joins `ods_pilot` to `port_visit_context` via `pe.visit_id = pvc.visit_id` (entry_id ↔ entry_id) and outputs `pvc.port_visit_id` (generation_id) to keep the `md5` fact ID consistent with batch mode.
- `fact/pilot/proceed.sql` and `fdw_proceed.sql`: **unchanged** — their temp tables (`temp_fact_pilot_*`) store generation_id, so `pv.id = inb.port_visit_id` remains correct.

**Quality control & backup (Group 5)**
- All QC accuracy, completeness, validity, and uniqueness-check files: F1 join conditions updated from `pv.id` to `pv.visit_id`.
- FDW validation files: `split_part(port_visit_id, '_', 2)` extracts entry_id for ODS child joins (was `split_part(..., 1)` which extracted generation_id).
- `backup/warehouse/cleanup_ods_child_tables.sql`: 6 DELETE conditions updated.

### One-time live database migration

Run this script **once** against the live database before deploying this branch:

```sql
-- ============================================================
-- PREREQUISITES
--   1. Pause ALL SOF DAGs before running Step A.
--   2. Verify the old ods_port_visit constraint names against
--      the live database with the query below — the script
--      drops them by name and will fail if they differ.
--
-- SELECT conname, contype
-- FROM   pg_constraint
-- WHERE  conrelid = 'ods_port_visit'::regclass
-- ORDER  BY contype;
-- ============================================================

-- ============================================================
-- PRE-FLIGHT  (read-only — run and review before anything else)
-- ============================================================

-- 1. Guard: no NULL visit_id in parent
SELECT count(*) AS null_visit_id_count
FROM ods_port_visit
WHERE visit_id IS NULL;
-- Expected: 0

-- 2. Guard: no orphaned child rows
SELECT count(*) AS orphan_count
FROM (
    SELECT port_visit_id FROM ods_terminal_visit
    UNION ALL SELECT port_visit_id FROM ods_berth_visit
    UNION ALL SELECT port_visit_id FROM ods_anchor_stop
    UNION ALL SELECT port_visit_id FROM ods_encounter
    UNION ALL SELECT port_visit_id FROM ods_lock_stop
    UNION ALL SELECT port_visit_id FROM ods_pilot
    UNION ALL SELECT port_visit_id FROM ods_ship_to_ship_transfers
    UNION ALL SELECT port_visit_id FROM ods_slow_moving_period
    UNION ALL SELECT port_visit_id FROM ods_unclassified_stop
    UNION ALL SELECT port_visit_id FROM ods_visited_approach_area
    UNION ALL SELECT port_visit_id FROM ods_port_visit_terminal_visits
) orphans
WHERE NOT EXISTS (
    SELECT 1 FROM ods_port_visit p WHERE p.id = orphans.port_visit_id
);
-- Expected: 0

-- ============================================================
-- TRANSACTION A (revised) — current DEV state:
--   FK constraints already reference ods_port_visit(visit_id)
--   PK is still on id — needs swapping.
-- ============================================================
BEGIN;

-- Step 1: Drop all child FK constraints first.
--   (They depend on ods_port_visit_unique_visit_id, blocking the PK swap.)
ALTER TABLE ods_terminal_visit             DROP CONSTRAINT ods_terminal_visit_fkey_port_visit;
ALTER TABLE ods_berth_visit                DROP CONSTRAINT ods_berth_visit_fkey_port_visit;
ALTER TABLE ods_anchor_stop                DROP CONSTRAINT ods_anchor_stop_fkey_port_visit;
ALTER TABLE ods_encounter                  DROP CONSTRAINT ods_encounter_fkey_port_visit;
ALTER TABLE ods_lock_stop                  DROP CONSTRAINT ods_lock_stop_fk_port_visit;
ALTER TABLE ods_pilot                      DROP CONSTRAINT ods_pilot_fkey_port_visit;
ALTER TABLE ods_ship_to_ship_transfers     DROP CONSTRAINT ods_ship_to_ship_transfers_fkey_port_visit;
ALTER TABLE ods_slow_moving_period         DROP CONSTRAINT ods_slow_moving_period_fkey_port_visit;
ALTER TABLE ods_unclassified_stop          DROP CONSTRAINT ods_unclassified_stop_fkey_port_visit;
ALTER TABLE ods_visited_approach_area      DROP CONSTRAINT ods_visited_approach_area_fk_port_visit;
ALTER TABLE ods_port_visit_terminal_visits DROP CONSTRAINT ods_port_visit_terminal_visits_fkey_port_visit;

-- Step 2: Re-add FK constraints referencing the new PK.
--   NOT VALID: skips validation of existing rows (still have generation_id values).
ALTER TABLE ods_terminal_visit         ADD CONSTRAINT ods_terminal_visit_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_berth_visit            ADD CONSTRAINT ods_berth_visit_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_anchor_stop            ADD CONSTRAINT ods_anchor_stop_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_encounter              ADD CONSTRAINT ods_encounter_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_lock_stop              ADD CONSTRAINT ods_lock_stop_fk_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_pilot                  ADD CONSTRAINT ods_pilot_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_ship_to_ship_transfers ADD CONSTRAINT ods_ship_to_ship_transfers_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_slow_moving_period     ADD CONSTRAINT ods_slow_moving_period_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_unclassified_stop      ADD CONSTRAINT ods_unclassified_stop_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_visited_approach_area  ADD CONSTRAINT ods_visited_approach_area_fk_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;
ALTER TABLE ods_port_visit_terminal_visits ADD CONSTRAINT ods_port_visit_terminal_visits_fkey_port_visit
    FOREIGN KEY (port_visit_id) REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE NOT VALID;

COMMIT;


-- ============================================================
-- TRANSACTION B — Remap child port_visit_id: generation_id → entry_id
-- DML only: row-level locks, no table-level exclusive lock.
-- Rolls back cleanly if the post-remap check fails.
-- ============================================================
BEGIN;

UPDATE ods_terminal_visit         AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_berth_visit            AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_anchor_stop            AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_encounter              AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_lock_stop              AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_pilot                  AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_ship_to_ship_transfers AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_slow_moving_period     AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_unclassified_stop      AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_visited_approach_area  AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;
UPDATE ods_port_visit_terminal_visits AS c SET port_visit_id = p.visit_id FROM ods_port_visit AS p WHERE c.port_visit_id = p.id;

-- Post-remap guard: abort if any child row still points to a stale generation_id
DO $$
DECLARE unmapped_count INTEGER;
BEGIN
    SELECT count(*) INTO unmapped_count
    FROM (
        SELECT port_visit_id FROM ods_terminal_visit
        UNION ALL SELECT port_visit_id FROM ods_berth_visit
        UNION ALL SELECT port_visit_id FROM ods_anchor_stop
        UNION ALL SELECT port_visit_id FROM ods_encounter
        UNION ALL SELECT port_visit_id FROM ods_lock_stop
        UNION ALL SELECT port_visit_id FROM ods_pilot
        UNION ALL SELECT port_visit_id FROM ods_ship_to_ship_transfers
        UNION ALL SELECT port_visit_id FROM ods_slow_moving_period
        UNION ALL SELECT port_visit_id FROM ods_unclassified_stop
        UNION ALL SELECT port_visit_id FROM ods_visited_approach_area
        UNION ALL SELECT port_visit_id FROM ods_port_visit_terminal_visits
    ) child
    WHERE NOT EXISTS (
        SELECT 1 FROM ods_port_visit pv WHERE pv.visit_id = child.port_visit_id
    );
    IF unmapped_count > 0 THEN
        RAISE EXCEPTION 'Post-remap check failed: % child rows have no matching visit_id — rolling back', unmapped_count;
    END IF;
END $$;

COMMIT;

-- ============================================================
-- TRANSACTION C — Validate FK constraints after remap
-- ============================================================
ALTER TABLE ods_terminal_visit         VALIDATE CONSTRAINT ods_terminal_visit_fkey_port_visit;
ALTER TABLE ods_berth_visit            VALIDATE CONSTRAINT ods_berth_visit_fkey_port_visit;
ALTER TABLE ods_anchor_stop            VALIDATE CONSTRAINT ods_anchor_stop_fkey_port_visit;
ALTER TABLE ods_encounter              VALIDATE CONSTRAINT ods_encounter_fkey_port_visit;
ALTER TABLE ods_lock_stop              VALIDATE CONSTRAINT ods_lock_stop_fk_port_visit;
ALTER TABLE ods_pilot                  VALIDATE CONSTRAINT ods_pilot_fkey_port_visit;
ALTER TABLE ods_ship_to_ship_transfers VALIDATE CONSTRAINT ods_ship_to_ship_transfers_fkey_port_visit;
ALTER TABLE ods_slow_moving_period     VALIDATE CONSTRAINT ods_slow_moving_period_fkey_port_visit;
ALTER TABLE ods_unclassified_stop      VALIDATE CONSTRAINT ods_unclassified_stop_fkey_port_visit;
ALTER TABLE ods_visited_approach_area  VALIDATE CONSTRAINT ods_visited_approach_area_fk_port_visit;
ALTER TABLE ods_port_visit_terminal_visits VALIDATE CONSTRAINT ods_port_visit_terminal_visits_fkey_port_visit;


-- ============================================================
-- POST-MIGRATION — Validate FK constraints + refresh statistics
-- ShareUpdateExclusiveLock: concurrent reads and writes allowed.
-- Run these after DAGs are re-enabled; each is independent.
-- ============================================================
ALTER TABLE ods_terminal_visit             VALIDATE CONSTRAINT ods_terminal_visit_fkey_port_visit;
ALTER TABLE ods_berth_visit                VALIDATE CONSTRAINT ods_berth_visit_fkey_port_visit;
ALTER TABLE ods_anchor_stop                VALIDATE CONSTRAINT ods_anchor_stop_fkey_port_visit;
ALTER TABLE ods_encounter                  VALIDATE CONSTRAINT ods_encounter_fkey_port_visit;
ALTER TABLE ods_lock_stop                  VALIDATE CONSTRAINT ods_lock_stop_fk_port_visit;
ALTER TABLE ods_pilot                      VALIDATE CONSTRAINT ods_pilot_fkey_port_visit;
ALTER TABLE ods_ship_to_ship_transfers     VALIDATE CONSTRAINT ods_ship_to_ship_transfers_fkey_port_visit;
ALTER TABLE ods_slow_moving_period         VALIDATE CONSTRAINT ods_slow_moving_period_fkey_port_visit;
ALTER TABLE ods_unclassified_stop          VALIDATE CONSTRAINT ods_unclassified_stop_fkey_port_visit;
ALTER TABLE ods_visited_approach_area      VALIDATE CONSTRAINT ods_visited_approach_area_fk_port_visit;
ALTER TABLE ods_port_visit_terminal_visits VALIDATE CONSTRAINT ods_port_visit_terminal_visits_fkey_port_visit;

ANALYZE ods_port_visit;
ANALYZE ods_terminal_visit;
ANALYZE ods_berth_visit;
ANALYZE ods_anchor_stop;
ANALYZE ods_encounter;
ANALYZE ods_lock_stop;
ANALYZE ods_pilot;
ANALYZE ods_ship_to_ship_transfers;
ANALYZE ods_slow_moving_period;
ANALYZE ods_unclassified_stop;
ANALYZE ods_visited_approach_area;
ANALYZE ods_port_visit_terminal_visits;
```

### Test plan

- [ ] Run the one-time migration SQL against staging; verify zero orphan rows found
- [ ] Trigger a full SOF batch DAG run on staging; confirm ODS child row counts match pre-migration
- [ ] Trigger a SOF streaming update for an existing visit; verify child records are updated in place (no cascade delete)
- [ ] Validate QC DAG runs green (uniqueness, accuracy, completeness checks)
- [ ] Spot-check `fact_pilot` row counts match between batch and streaming mode for the same visit

## Commits

- `aedad2be` **Panji Y. Wiwaha** (2026-07-17): chore(ddl): set visit_id as primary key on ods_port_visit, update child FK constraints
  - ods_port_visit: PK changed from id (generation_id) to visit_id (entry_id);
    dropped separate UNIQUE (visit_id) constraint, kept UNIQUE (visit_id, version)
  - All 11 ODS child tables: REFERENCES ods_port_visit (visit_id) ON DELETE CASCADE
  - fact/temp/terminal_visits: 3 FK constraints updated to REFERENCES ods_port_visit (visit_id)
- `3d84cfe0` **Panji Y. Wiwaha** (2026-07-17): chore(ods-dml): migrate ODS write queries to use entry_id (visit_id) as port_visit FK
  - port_visit stg_to_ods: ON CONFLICT key changed to visit_id; generation_id kept as
    plain column; delete_changed_generation_id now a no-op (visit_id PK never changes)
  - All 11 child stg_to_ods files: port_visit_id populated from entry_id instead of
    generation_id; ON CONFLICT WHERE and FK subquery updated to match visit_id
  - All child soft_delete files: WHERE port_visit_id filter updated to use visit_id
  - pilot/stg_to_ods: JOIN ods_encounter ON e.port_visit_id = pv.visit_id (was pv.id)
  - slow_moving_period/cleanup: DELETE WHERE updated from pv.id to pv.visit_id
- `560b410e` **Panji Y. Wiwaha** (2026-07-17): chore(airflow): remove delete_changed_generation_id task from SOF streaming DAG
  With visit_id as PK the generation_id column is no longer the conflict key, so
  an updated SOF event causes a plain column UPDATE rather than a DELETE + re-INSERT.
  The cascade-delete guard is no longer needed and the task is removed from the DAG.
- `fbcdec56` **Panji Y. Wiwaha** (2026-07-17): chore(fact-dml): fix F1 join conditions after ods_port_visit PK migration
  ODS child tables now store entry_id in port_visit_id; joins to ods_port_visit that
  previously compared child.port_visit_id to pv.id (generation_id) returned zero rows.
  
  - fact/port_visit/* prepare_* files: ODS child joins changed to pv.visit_id
  - fact/terminal_visit/* prepare_* files: same F1 fix pattern
  - fact/berth_visit/* prepare_* files: same F1 fix pattern
  - fact/tug/proceed.sql, proceed_delta.sql: F1 join fix
  - fact/pilot/proceed_delta.sql: streaming delta now joins ods_pilot to
    port_visit_context via pe.visit_id = pvc.visit_id (entry_id = entry_id) and
    outputs pvc.port_visit_id (generation_id) to keep md5 ID consistent with batch mode
  
  Note: fact/pilot/proceed.sql and fdw_proceed.sql retain pv.id = inb.port_visit_id
  because the temp tables they read are populated with generation_id by prepare_selected_*.
- `81236910` **Panji Y. Wiwaha** (2026-07-17): chore(quality-control): fix ODS child join conditions for visit_id PK migration
  QC and backup queries that joined ODS child tables to ods_port_visit using the old
  generation_id PK (pv.id) now use pv.visit_id (entry_id) to match the new PK.
  
  - uniqueness_check/ods_berth_visit, ods_terminal_visit: ON condition updated
  - accuracy/berth_visit/* and accuracy/tug/*: F1 join fix pattern
  - accuracy/port_visit/waiting_time_components, sailing_duration_components,
    port_travel_duration_components, drifting_duration_components: ODS child joins fixed;
    inter-CTE joins (F2) left unchanged
  - accuracy/port_visit/fdw/*: split_part pattern updated to extract entry_id
    (split_part(..., 2)) for ODS child joins; ods_port_visit self-join left unchanged
  - accuracy/pilot/fdw/summary_validation: F1 join fix
  - completeness/berth_visit/*, terminal_visit/*, tug_event/*: prepare and compare files
  - completeness/encounter/prepare_ods_encounter_pilot: port_visit_ids CTE changed to
    SELECT visit_id; two F1 join conditions fixed; safe generation_id joins left unchanged
  - validity/port_visit_anchor_overlaps: two F1 join conditions fixed
  - backup/warehouse/cleanup_ods_child_tables: 6 DELETE WHERE conditions fixed
- `903cb272` **Panji Y. Wiwaha** (2026-07-18): fix: correct ON CONFLICT target and pilot FDW join after visit_id PK migration
  ods/port_visit/stg_to_ods.sql:
    ON CONFLICT (visit_id, version) → ON CONFLICT (visit_id)
    With visit_id as PK the conflict target must be the PK column alone.
    The old target only fired when (visit_id, version) were both identical;
    a SOF re-send with the same entry_id but a new version bypassed the
    conflict clause and hit a PK duplicate-key error at runtime.
  
  quality_control/accuracy/pilot/fdw/summary_validation.sql:
    Reverted upv.port_visit_id = pv.visit_id → pv.id
    unique_port_visit_ids derives port_visit_id from fact_pilot.port_visit_id
    which is generation_id (pv.id), not entry_id. The previous migration
    change incorrectly treated this as an F1 join; matching against pv.id
    is correct here and was not affected by the PK change.
- `a78ccaf3` **Panji Y. Wiwaha** (2026-07-19): fix(ddl): add UNIQUE (id) constraint on ods_port_visit to enforce generation_id uniqueness
  With visit_id as PK, ods_port_visit.id (generation_id) lost its only uniqueness
  constraint. Generation_id is globally unique in practice — stg_statement_of_fact
  enforces PRIMARY KEY (generation_id) and UNIQUE (entry_id) — but without a DDL
  constraint the invariant was unenforced, leaving downstream joins keyed on pv.id
  (fact layer, QC validation) silently vulnerable to any out-of-band write.
  
  The one-time migration SQL must also run:
    ALTER TABLE ods_port_visit ADD CONSTRAINT ods_port_visit_unique_id UNIQUE (id);
  before deploying.
- `58cfae90` **Panji Y. Wiwaha** (2026-07-19): fix(quality-control): output pv.id as port_visit_id in encounter_inbound/outbound CTEs
  prepare_ods_encounter_pilot.sql replicates proceed.sql logic to compute matching
  md5 IDs for completeness comparison. The encounter_inbound and encounter_outbound
  CTEs sourced port_visit_id from ods_pilot.port_visit_id (entry_id post-migration)
  instead of pv.id (generation_id), causing their md5 hashes to diverge from the
  batch proceed.sql output and producing incorrect completeness results.
  
  Fix: output pv.id AS port_visit_id in both encounter CTEs (join condition
  ON inb/outb.port_visit_id = pv.visit_id is correct and unchanged — entry_id is
  the right key to look up the port_visit row after the PK migration).
- `e8d81e72` **Panji Y. Wiwaha** (2026-07-20): fix(ods-dml): add version to ON CONFLICT DO UPDATE in port_visit stg_to_ods
  hashed_staging_and_ods_data joins staging to ODS on (visit_id AND version).
  With ON CONFLICT (visit_id) and version absent from DO UPDATE SET, a SOF update
  with a new version left ods_port_visit.version stale. On every subsequent run the
  version mismatch caused the LEFT JOIN to find no ODS row, ods_data hashed to
  all-nulls, staging_data != ods_data was always true, and the row was re-updated
  on every DAG execution even when no payload fields had changed.
- `410e4375` **Panji Y. Wiwaha** (2026-07-20): fix(ods-dml): fix port_visit guard subquery in 8 child stg_to_ods files
  All 8 files had a guard subquery of the form:
    port_visit_id IN (SELECT opv.id FROM ods_port_visit AS opv ...)
  
  After the PK migration, port_visit_id in ODS child tables stores entry_id
  (ods_port_visit.visit_id), but the subquery still compared against opv.id
  (generation_id). Since the two ID types never match, every incoming record
  was silently filtered out, preventing any new child rows from reaching ODS
  and therefore the fact layer.
  
  Files fixed: anchor_stop, berth_visit (×2), encounter, lock_stop,
  ship_to_ship_transfers, terminal_visit (×2), unclassified_stop,
  visited_approach_area. pilot and slow_moving_period were already correct.
- `53a9de3f` **Panji Y. Wiwaha** (2026-07-20): refactor(fact-dml): rename port_visit_id to port_visit_gen_id in pilot temp tables
  All four pilot temp tables (selected/encounter × inbound/outbound) store
  ods_port_visit.id (generation_id), not ods_port_visit.visit_id (entry_id).
  Rename the column from port_visit_id to port_visit_gen_id to make the
  distinction explicit and avoid confusion with the entry_id-based visit_id.
  
  Updated consistently across DDL, all four prepare files, and both
  proceed/fdw_proceed join references.
- `291e564f` **Panji Y. Wiwaha** (2026-07-21): fix(fact-dml): fix berth/terminal join on entry_id and repair migration for between_eos_entry_and_pob_duration
  - add_berths_summary.sql, add_terminals_summary.sql, add_shifting_inside_terminals.sql:
    fact_berth_visit/fact_terminal_visit.port_visit_id stores entry_id (sof.entry_id),
    but filtered_port_visits only exposed generation_id (fact_port_visit.id).
    Added visit_id to filtered_port_visits CTE and changed base CTEs to join on
    fpv.visit_id (entry_id) while outputting fpv.id (generation_id) so downstream
    UPDATE joins remain correct.
  
  - schema_migration.sql: between_eos_entry_and_pob_duration was originally added as
    a plain double precision column. A later commit changed the migration to GENERATED
    ALWAYS AS, but ADD COLUMN IF NOT EXISTS is a no-op on databases that already had
    the plain column, leaving it unpopulated. Added DROP COLUMN IF EXISTS before the
    ADD to force conversion to a stored generated column on all existing databases.
- `ea9e7276` **Panji Y. Wiwaha** (2026-07-21): fix(ods-dml): restore hard-delete before re-ingest in SOF UPDATE streaming path
  The delete_changed_generation_id task was removed on the assumption that
  ON CONFLICT (visit_id) DO UPDATE was sufficient for SOF updates. However,
  without a delete+cascade step, child records removed from SOF (e.g. a
  terminal visit dropped between updates) persist in ODS indefinitely since
  stg_to_ods only upserts — it never removes.
  
  Restore the task with simplified logic: hard-delete ods_port_visit by
  visit_id for streaming UPDATE events. ON DELETE CASCADE wipes all children,
  then ingest_ods_sof_level_1/2/3 re-inserts the current SOF state cleanly.
  
  The generation_id change check is no longer needed since visit_id is now
  the PK — every streaming UPDATE unconditionally deletes and re-inserts.

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-17)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F726%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-07-18)

_No comment._

### panjiyudasetya — COMMENTED (2026-07-18)

_No comment._

### augmentcode[bot] — COMMENTED (2026-07-18)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F726%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-07-19)

_No comment._

### augmentcode[bot] — COMMENTED (2026-07-19)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F726%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-07-20)

_No comment._

### panjiyudasetya — COMMENTED (2026-07-20)

_No comment._

### augmentcode[bot] — COMMENTED (2026-07-20)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F726%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-07-20)

_No comment._

### ryan-kharisma — APPROVED (2026-07-22)

LGTM

## Review Comments

### panjiyudasetya — 2026-07-18 on `teqplay/templates/sql/quality_control/accuracy/pilot/fdw/summary_validation.sql`

Resolved by 903cb27

### panjiyudasetya — 2026-07-18 on `teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql`

Resolved by 903cb27

### panjiyudasetya — 2026-07-19 on `teqplay/templates/sql/ddl/ods/port_visit.sql`

resolved by a78ccaf

### panjiyudasetya — 2026-07-20 on `teqplay/templates/sql/quality_control/completeness/encounter/prepare_ods_encounter_pilot.sql`

Resolved by 58cfae9

### panjiyudasetya — 2026-07-20 on `teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql`

Resolved by e8d81e7

### panjiyudasetya — 2026-07-20 on `teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql`

The `ranked_hashed_data` / `unique_and_clean_port_visit` CTEs serve a different purpose: they detect whether a row has changed `(staging_data != ods_data)`, not whether there are duplicate `visit_ids`. The `row_number() OVER (PARTITION BY staging_data)` deduplication there removes identical staging payloads submitted twice in the same batch, which is a different concern from same-`visit_id` duplicates.

## Comments

### panjiyudasetya — 2026-07-18

augment review

### panjiyudasetya — 2026-07-19

augment review

### panjiyudasetya — 2026-07-20

augment review

### panjiyudasetya — 2026-07-21

I've run comparison checks between the LOCAL and DEV data marts. So far, the contents are identical, @ryan-kharisma. See the comparison files [here](https://drive.google.com/drive/folders/10LnD2h-8kNzsfaO7CI1piaCN0SlGaxRU?usp=drive_link).
