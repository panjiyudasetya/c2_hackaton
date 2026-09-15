---
id: github:teqplay/dataflow_dag_core:pr:729
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 729
title: Release 1.54.0 to master
author: panjiyudasetya
state: closed
date: '2026-07-23'
merged_at: '2026-07-23'
base_branch: master
head_branch: release/1.54.0
url: https://github.com/teqplay/dataflow_dag_core/pull/729
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2839
---
# PR #729: Release 1.54.0 to master

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/729  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `release/1.54.0`  
**Created:** 2026-07-23  
**Merged:** 2026-07-23  

## Description


## [1.54.0] - 2026-07-23
### Changed
- Promotes `visit_id` as primary key in `ods_port_visit` (#726, #727)

## Commits

- `1779858e` **Panji Y. Wiwaha** (2026-07-10): Merge pull request #721 from teqplay/release/1.53.0
  Release 1.53.0 to develop
- `de54642b` **Panji Y. Wiwaha** (2026-07-16): Merge pull request #724 from teqplay/hotfix/1.53.1
  Release 1.53.1 to develop
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
- `202500c7` **Panji Y. Wiwaha** (2026-07-22): Merge pull request #726 from teqplay/chore/set-visit-id-as-pk
  PTO-2839 Promotes `visit_id` as primary key in `ods_port_visit`
- `35909b8f` **Panji Y. Wiwaha** (2026-07-22): fix(fact-migration): guard between_eos_entry_and_pob_duration backfill against GENERATED ALWAYS columns
  The plain-column UPDATE backfill fails on databases where the column is
  already GENERATED ALWAYS AS STORED (attgenerated = 's'). Wrap it in a
  DO $$ block that checks pg_attribute.attgenerated = '' before executing,
  so the backfill only runs on databases that still hold the column as a
  plain double precision.
- `59f374a4` **Panji Y. Wiwaha** (2026-07-22): Merge pull request #727 from teqplay/fix/generated-column-issue
  fix(fact-migration): Guard `between_eos_entry_and_pob_duration` backfill against GENERATED ALWAYS columns
- `7a24b68f` **Panji Y. Wiwaha** (2026-07-23): Bump version 1.54.0

## Reviews

### ryan-kharisma — APPROVED (2026-07-23)

LGTM
