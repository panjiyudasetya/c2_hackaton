---
id: github:teqplay/dataflow_dag_core:pr:754
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 754
title: 'PTO-2819 Delivery 2: Pipeline activation for the `TUG` and `BUNKER` SOF ingestion'
author: panjiyudasetya
state: closed
date: '2026-09-03'
merged_at: '2026-09-04'
base_branch: develop
head_branch: PTO-2819-pt2
url: https://github.com/teqplay/dataflow_dag_core/pull/754
labels: []
linked_issues: []
explicit_links: []
---
# PR #754: PTO-2819 Delivery 2: Pipeline activation for the `TUG` and `BUNKER` SOF ingestion

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/754  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2819-pt2`  
**Created:** 2026-09-03  
**Merged:** 2026-09-04  

## Description

### Description

Continues from Deliver 1 (merged in #752), which established the `VesselType` model and schema foundation. This PR activates end-to-end ingestion for TUG and BUNKER vessels through the SOF pipeline — batch and streaming — and closes all schema parity gaps.

### What changed

#### Schema & migrations
- Extended `vessel_type` CHECK constraints to include `TUG` and `BUNKER` in `stg_statement_of_fact`, `stg_statement_of_fact_deleted`, and `sof_processing_queue`
- Added idempotent DROP/ADD CONSTRAINT migrations for all three tables, wired into `prepare_migrations()`

#### SOF metadata validation (`sof_validate_metadata.sql` + `validate_metadata()`)
- Replaced the hardcoded per-vessel-type `is_valid` branch with parameterised boolean flags (`requires_port`, `requires_terminal`, `requires_berth`) passed from Python via `VesselType` properties — one SQL template now serves all vessel types
- Fixed `has_ship` CTE: TUG and BUNKER now look up by IMO (same as SEA_VESSEL), not by MMSI (which is the BARGE path)

#### Streaming path activation
- Added `resolve_vessel_type()` in `utils.py`: inspects `ship.categories` per message and overrides the consumer's default type when TUG or BUNKER is detected — so TUG/BUNKER messages arriving on the sea-vessel RabbitMQ queue are tagged correctly before staging
- `SOFRMQTransformer` calls `resolve_vessel_type` per message; both queue record builders use `sof.vessel_type` (resolved) rather than `self._vessel_type` (consumer default)
- `SOFRMQValidator._is_sof_completed` now uses `requires_slow_moving_periods` as the single gate: TUG and BUNKER are always considered complete at the SOF level and pass through unconditionally (same behaviour as BARGE in the batch path)

#### Completion semantics — TUG / BUNKER / BARGE
TUG, BUNKER, and BARGE SOFs may arrive without a top-level `end` timestamp. Completeness for these vessel types is evaluated at the terminal/berth visit level at fact load time, not at the SOF envelope level. On both the batch and streaming paths, `_is_sof_completed` returns `True` unconditionally for these types. Only SEA_VESSEL requires `end` + `slowMovingPeriods`. This is consistent with the original BARGE behaviour on `develop`, where `_is_sof_completed` was never called for BARGE at all.

#### Stream DAGs
- Added sequential TUG → BUNKER task groups (UPDATE then DELETE, `TriggerRule.ALL_DONE`) to both `ods_sof/stream_dag.py` and `fact_sof/stream_dag.py`, chained after the existing BARGE groups

#### ODS DML
- Applied NULL-safe end-time predicates (`sof.end IS NOT NULL AND (sof.end ->> 'timestamp') IS NOT NULL`) across all 11 ODS `stg_to_ods` queries, QC completeness queries, and the `conditional_filtering` macro

#### Pilot fact DML
- Extended `proceed_delta.sql` to include TUG and BUNKER in three places: `pilot_events` filter, completion sub-condition, and `port_visit_context` ship JOIN

---

### Tests
- Added `tests/unit/test_sof_is_completed.py` with 22 parametrized cases covering both batch (`SOFService`) and streaming (`SOFRMQValidator`) paths against a shared truth table, plus `resolve_vessel_type` category detection
- Truth table: TUG/BUNKER → `True` regardless of `end`; SEA_VESSEL → `False` without both `end` and `slowMovingPeriods`; BARGE → `True` always

---

### Deployment notes
- `prepare_database` must run before the streaming DAGs are activated to apply the three constraint migrations
- The sea-vessel RMQ consumer now processes TUG and BUNKER messages — no config change required; detection is automatic via `ship.categories`

## Commits

- `f4e3cd7f` **Panji Y. Wiwaha** (2026-09-02): feat(sof-validation): replace hardcoded is_valid with per-type boolean flags
  sof_validate_metadata.sql now accepts %(requires_port)s, %(requires_terminal)s,
  and %(requires_berth)s boolean params so the final is_valid expression is driven
  entirely by VesselType properties — adding a new vessel type requires no SQL change.
  
  The has_ship CASE is also corrected: TUG and BUNKER vessels have IMOs (same as
  SEA_VESSEL), so they now use the IMO lookup branch instead of falling through to
  the BARGE MMSI branch that would always return FALSE for them.
  
  validate_metadata() in SOFProcessingQueueRepository instantiates VesselType and
  passes the three requires_* flags into the params dict. This commit ships the SQL
  and Python sides together to avoid a KeyError on the missing params during the
  deploy window.
- `fe400270` **Panji Y. Wiwaha** (2026-09-02): feat(fact-dml): extend pilot delta query to include TUG and BUNKER vessels
  proceed_delta.sql previously hard-coded IN ('SEA_VESSEL', 'BARGE'), silently
  excluding TUG and BUNKER pilot events from fact_pilot.
  
  Three places updated:
  - Outer vessel_type filter: now IN ('SEA_VESSEL', 'BARGE', 'TUG', 'BUNKER')
  - Completion sub-condition: TUG/BUNKER grouped with SEA_VESSEL (require both
    port_visit_start and port_visit_end timestamps, unlike BARGE)
  - ods_ship JOIN: TUG/BUNKER use the IMO branch (same as SEA_VESSEL), not the
    BARGE MMSI branch
- `3da5b185` **Panji Y. Wiwaha** (2026-09-02): feat(stream-dags): add TUG and BUNKER sequential task groups to ODS and fact stream DAGs
  Both ods_sof__stream and fact_sof__stream now process four vessel types in order:
  SEA_VESSEL UPDATE → SEA_VESSEL DELETE → BARGE UPDATE → BARGE DELETE →
  TUG UPDATE → TUG DELETE → BUNKER UPDATE → BUNKER DELETE
  
  TUG and BUNKER groups are appended at the end to minimise change to existing
  behaviour. All groups use TriggerRule.ALL_DONE so a failure in one type does not
  block subsequent types. The new groups are immediate no-ops until the streaming
  consumer starts writing TUG/BUNKER records in Delivery 3.
- `4cab9f45` **Panji Y. Wiwaha** (2026-09-02): feat(sof-streaming): activate TUG and BUNKER ingestion on the sea-vessel RMQ consumer
  resolve_vessel_type() added to utils.py: reads ship.categories from the raw SOF
  value dict and returns 'TUG' or 'BUNKER' when found, otherwise falls back to the
  caller-supplied default.
  
  transformators.py: _to_staging_sof now calls resolve_vessel_type per-message so
  each SOFStagingData carries its correct vessel_type before hitting the database.
  Queue record builders (_to_pending_processing_queue, _to_ignored_processing_queue)
  now read sof.vessel_type instead of the class-level self._vessel_type, so
  sof_processing_queue rows are also correctly typed.
  
  validators.py: _is_tug_or_bunker_vessels removed — TUG/BUNKER no longer rejected
  at the gate. _is_sof_completed is now vessel-type-aware: it checks
  VesselType.requires_slow_moving_periods so TUG/BUNKER pass with only an 'end'
  timestamp (their empty slowMovingPeriods arrays are not a rejection reason).
  
  base.py: _resolve_vessel_type static method added (delegates to utils); docstrings
  updated to reflect the expanded vessel type support.
- `c913bd3c` **Panji Y. Wiwaha** (2026-09-03): feat(ddl): extend stg_statement_of_fact_deleted vessel_type constraint to include TUG and BUNKER
  Mirrors the same change already applied to stg_statement_of_fact and
  sof_processing_queue in Delivery 1. The DDL file is updated so fresh
  installs create the table with the correct constraint, and the migration
  appends a DROP CONSTRAINT / ADD CONSTRAINT pair so existing deployments
  are upgraded without a table rebuild.
- `7431f265` **Panji Y. Wiwaha** (2026-09-03): fix(sof-service): align batch _is_sof_completed with streaming for TUG/BUNKER
  TUG and BUNKER were falling through to `return True` without checking
  `end`, while the streaming path correctly required `end` first.
  Restructured to check `is_barge` (skip), then `end` (gate), then
  `requires_slow_moving_periods` — matching the streaming validator.
- `3f2b2a70` **Panji Y. Wiwaha** (2026-09-03): refactor(sof-streaming): remove dead wrapper, promote VesselType import, document noqa scope
  - Remove _resolve_vessel_type static wrapper from base.py — it had zero
    callers; transformators.py already calls resolve_vessel_type directly
  - Move VesselType import from inside resolve_vessel_type() to module
    level in utils.py (no circular import justification existed)
  - Add comment in sof_validate_metadata.sql explaining why --noqa:
    disable=all covers the full file (psycopg2 %(name)s::boolean casts
    produce false-positive PRS errors in sqlfluff)
- `405b417b` **Panji Y. Wiwaha** (2026-09-03): fix(sof): TUG/BUNKER always considered complete at SOF level on both paths
  Top-level sof.end is not the completeness gate for TUG and BUNKER —
  they may arrive without it. Completeness for these types is evaluated
  at the terminal/berth level at fact load time.
  
  Batch path: simplify _is_sof_completed to gate on requires_slow_moving_periods
  only (True for SEA_VESSEL, False for all others). Streaming path: align to
  the same rule — remove the `if not sof.end: return False` guard that
  incorrectly blocked TUG/BUNKER without a top-level end timestamp.
  Add tests to reflect the correct truth table.
- `b1bca291` **Panji Y. Wiwaha** (2026-09-03): fix(sof-streaming): guard resolve_vessel_type against explicit ship: null payload
  data.get('ship', {}) returns None when ship is explicitly null in the
  message — the default {} only applies to missing keys. Subsequent
  .get('categories') on None raises AttributeError and rolls back the
  entire consumer batch. Fix by checking isinstance(ship, dict) before
  calling .get(). Add regression test case to lock in the fallback-to-
  default behavior.
- `1746ae46` **Panji Y. Wiwaha** (2026-09-03): fix(fact-dml): exempt TUG/BUNKER from port-visit end timestamp requirement in pilot delta
  ods_port_visit.end_timestamp derives from sof.end, which is optional
  for TUG and BUNKER. Grouping them with SEA_VESSEL (requiring
  port_visit_end_timestamp IS NOT NULL) silently excluded all TUG/BUNKER
  pilot facts when the SOF had no top-level end. Group TUG/BUNKER with
  BARGE instead — no port-visit timestamp requirement — consistent with
  completeness being evaluated at the terminal/berth level at fact load.
- `0af563d6` **Panji Y. Wiwaha** (2026-09-03): fix(sof-validation): replace coalesce with jsonb_typeof guard for terminal/berth arrays
  SOFStagingData.to_tuple() serializes None (absent visit arrays) via
  dumps_with_decimal, which produces the JSON literal 'null'. PostgreSQL
  stores this as a JSONB scalar, not a SQL NULL, so coalesce(col, '[]')
  is a no-op and jsonb_array_elements raises "cannot extract elements from
  a scalar" before the requires_terminal/requires_berth flags can make the
  checks optional.
  
  Replace coalesce with CASE WHEN jsonb_typeof(col) = 'array' to fall
  back to '[]' for both SQL NULL and JSON null inputs.
- `46b69f1d` **Panji Y. Wiwaha** (2026-09-03): fix(sof-streaming): extend missing-metadata recovery to cover TUG/BUNKER ships
  sof_extract_missing_metadata.sql only had missing_sea_vessel_ships and
  missing_barge_ships CTEs. TUG/BUNKER records with a non-null ship_id
  whose IMO was absent from ods_ship had no matching LEFT JOIN in
  blocked_entries, fell through to ready_entries, were reset to PENDING,
  then immediately deferred again — looping indefinitely.
  
  Add missing_tug_bunker_ships (IMO lookup, same as SEA_VESSEL), wire it
  into blocked_entries and the missing_ship_ids / missing_ship_imos
  aggregates in the final SELECT.
  
  Also apply the jsonb_typeof guard to the terminal_visits and berth_visits
  array extractions (same JSON-null issue as sof_validate_metadata.sql).
- `228c4fff` **Panji Y. Wiwaha** (2026-09-03): fix(ods-dml): replace != '[]' array guard with jsonb_typeof across all SOF ODS loaders
  SOFStagingData.to_tuple() serializes absent visit arrays (e.g. no
  terminalVisits in payload) as JSON null via dumps_with_decimal(None).
  PostgreSQL stores this as a JSONB scalar, not SQL NULL, so the existing
  guard `col != '[]'` evaluates to TRUE for JSON null and passes it to
  jsonb_array_elements, which raises "cannot extract elements from a scalar".
  
  TUG/BUNKER SOFs are now accepted without visit arrays, so this pre-
  existing latent bug becomes a guaranteed crash on the newly activated
  paths.
  
  Replace `col != '[]'` with `jsonb_typeof(col) = 'array'` in all ten
  affected ODS stg_to_ods loaders:
    anchor_stop, berth_visit, encounter, lock_stop, ship_to_ship_transfers,
    slow_moving_period, terminal_visit, tug_event (berth_visits +
    arrival_tugs/departure_tugs), unclassified_stop, visited_approach_area.
- `7709c51a` **Panji Y. Wiwaha** (2026-09-03): fix(sof-validation): require port for TUG/BUNKER and unblock null-port records
  Two high-severity issues addressed:
  
  1. TUG/BUNKER records with a non-null port_id that has no matching ODS port
     were passing metadata validation (requires_port_completeness was False),
     proceeding to fact loading, and producing no facts due to the INNER JOIN
     to ods_port in the fact loaders — silently marked FACTS_PROCESSING_COMPLETED.
     Fix: requires_port_completeness now returns True for TUG and BUNKER.
  
  2. TUG/BUNKER records with a null port_id (port is legitimately absent from
     the payload) were unconditionally blocked in sof_extract_missing_metadata
     by the ds.port_id IS NULL guard, with no port to fetch — remaining
     DEFERRED forever after all other required metadata was resolved.
     Fix: scope the ds.port_id IS NULL block to vessel types where port is
     strictly required (i.e. exclude TUG/BUNKER).
  
     When a null-port TUG/BUNKER record reaches sof_validate_metadata, the
     port check now passes when port_unlocode IS NULL, preventing a further
     infinite-validation loop.
- `8d6037cb` **Panji Y. Wiwaha** (2026-09-03): fix(ods-dml): combine jsonb_typeof + jsonb_array_length for explicit non-empty guard
  jsonb_typeof(col) = 'array' prevents the crash when col is a JSON null scalar,
  but leaves the non-empty intent implicit. Add AND jsonb_array_length(col) > 0
  to make both conditions self-documenting: the type guard prevents the crash,
  the length guard communicates that empty arrays are intentionally excluded.
  
  Functionally equivalent — jsonb_array_elements([]) already returns zero rows —
  but unambiguous compared to the previous col != '[]' string check.
- `528b52c6` **Panji Y. Wiwaha** (2026-09-03): fix(ddl): extend ods_port_visit vessel_type constraint to include TUG and BUNKER
  The CHECK constraint on visit_vessel_type only allowed SEA_VESSEL and BARGE,
  causing every TUG/BUNKER ODS load to fail with a constraint violation and roll
  back to PENDING. Updated both the DDL (for new databases) and the migration
  script (to re-create the constraint on live databases via DROP IF EXISTS +
  ADD CONSTRAINT).
- `49353c72` **Panji Y. Wiwaha** (2026-09-03): fix(sof-streaming): handle portless TUG/BUNKER and scope optional metadata blocks
  Two issues fixed:
  
  1. Portless TUG/BUNKER payloads silently ignored (FB2):
     find_unlocode_in_message() returns the UNKNOWN sentinel when no port is
     present, which caused _get_invalid_reason to mark the record IGNORED before
     the optional-port metadata rule could run. In _to_staging_sof, the UNKNOWN
     sentinel is now converted to None for TUG/BUNKER; the validator does not
     treat a None unlocode as an error, and sof_validate_metadata.sql's existing
     IS NULL escape hatch passes the port check for portless records.
     SOFStagingData.unlocode widened to Optional[str] to carry this state.
  
  2. Optional terminal IDs blocking TUG/BUNKER records indefinitely (FB3):
     blocked_entries in sof_extract_missing_metadata.sql applied the terminal
     and berth overlap checks unconditionally, but requires_terminal_completeness
     is True only for SEA_VESSEL and requires_berth_completeness is True only for
     SEA_VESSEL and BUNKER. The checks are now guarded by vessel_type so TUG is
     not blocked by missing optional berth or terminal IDs, and BUNKER is not
     blocked by missing optional terminal IDs.
- `1d517ad2` **Panji Y. Wiwaha** (2026-09-03): fix(ddl): extend vessel_type CHECK constraints to include TUG and BUNKER
  Extend CHECK constraints on ods_berth_visit, ods_terminal_visit,
  fact_berth_visit, fact_terminal_visit, fact_port_visit, fact_pilot, and
  fact_pilot_delta from ('SEA_VESSEL', 'BARGE') to include 'TUG' and
  'BUNKER'. Without this, the streaming path would fail with a constraint
  violation as soon as the first TUG or BUNKER record reaches these tables.
  
  Schema migrations use NOT VALID to skip full-table validation scans,
  keeping lock duration minimal on large production tables. All existing
  rows remain valid under the extended constraint.
  
  Also adds a new migration for fact_pilot_delta (previously had no
  migration entry) and wires it into run_fact_migrations().
- `b108d0a3` **Panji Y. Wiwaha** (2026-09-03): fix(sof-streaming): pass portless TUG/BUNKER through UNLOCODE-based filters
  Portless TUG/BUNKER records have UNKNOWN_UNLOCODE as their unlocode,
  which caused two filter stages to silently drop them before the
  transformer could normalize the sentinel to None:
  
  1. _filter_data: by_customer_code and by_unlocode_whitelist both call
     find_unlocode_in_message, which returns UNKNOWN for portless records.
     'UNKNOWN' never matches any real UNLOCODE, so these records were
     discarded before reaching _persist_update_messages.
  
  2. _filter_by_fully_mapped_status: same pattern — UNKNOWN is never in
     the FULLY_MAPPED cache, so every portless TUG/BUNKER UPDATE was
     silently ignored when the cache had any entries.
  
  Fix: add _is_portless_tug_or_bunker() which detects these records by
  combining the UNKNOWN sentinel with a vessel-type check. Use it to
  split portless records out of _filter_data before UNLOCODE filtering
  and merge them back after, and as a bypass condition in
  _filter_by_fully_mapped_status.
- `1fa6d874` **Panji Y. Wiwaha** (2026-09-03): fix(ddl): extend vessel_type constraint to TUG/BUNKER on all remaining fact tables
  Operational event tables (fact_tug, fact_anchor, fact_bunkering and
  their delta variants, fact_ship_to_ship_transfers) and KPI summary
  tables (fact_port_calls, fact_port_calls_terminal,
  fact_port_performance_analytics, fact_stdev_*) all derived
  vessel_type from ods_port_visit.visit_vessel_type. Their CHECK
  constraints still permitted only SEA_VESSEL/BARGE, so any fact load
  touching a TUG or BUNKER port visit would fail with a constraint
  violation and keep retrying.
  
  DDL updated for 12 tables; schema migrations append NOT VALID
  DROP/ADD CONSTRAINT for live databases. NOT VALID skips the full-table
  scan, keeping lock duration minimal. Existing rows (SEA_VESSEL/BARGE
  only) remain valid under the extended constraint.
- `eeefc7e4` **Panji Y. Wiwaha** (2026-09-03): fix(sof): scope portless bypass to Teqplay whitelist and guard soft-deleted ships
  - _filter_data: portless TUG/BUNKER records no longer bypass the customer
    boundary for non-Teqplay customers; the whitelist split is now inside the
    Teqplay+whitelist branch only, so portless records correctly drop out via
    by_customer_code() for third-party customers
  - sof_validate_metadata.sql: add deleted_timestamp IS NULL to both EXISTS
    branches of the has_ship CASE so soft-deleted ods_ship rows are not
    treated as present during validation
  - sof_extract_missing_metadata.sql: add deleted_timestamp IS NULL to all
    three missing_*_ships NOT EXISTS subqueries (sea_vessel, barge, tug/bunker)
    so soft-deleted ships are correctly reported as missing and trigger a
    metadata fetch rather than silently producing no facts
- `e9bc716d` **Panji Y. Wiwaha** (2026-09-04): fix(ddl): correct wrong table name in stdev_time_terminal_visit migration
  Lines 18-22 referenced fact_stdev_time_terminal_visit_overall instead of
  fact_stdev_time_terminal_visit, causing prepare_database to fail on a
  non-existent table and blocking all subsequent migrations.
- `a5e054c4` **Panji Y. Wiwaha** (2026-09-04): fix(sof): remove vessel_type join condition from hard_delete_queue_aware
  DELETE payloads often omit ship.categories, resolving to the service
  default instead of the vessel_type stored at UPDATE time. The
  stg.vessel_type = del.vessel_type JOIN condition prevented staging
  cleanup when types diverged, leaving orphaned TUG/BUNKER rows behind
  after the ODS/fact delete succeeded. entry_id is unique in staging so
  it is sufficient to identify the row.
- `53a50b1b` **Panji Y. Wiwaha** (2026-09-04): fix(sof): drop vessel_type from cross-record blocking checks in queue
  DELETE payloads often omit ship.categories, resolving to the service
  default instead of the vessel_type stored at UPDATE time. The
  vessel_type match in sof_fetch_pending_delete and sof_mark_stale_deletes
  made a TUG/BUNKER UPDATE invisible to a SEA_VESSEL DELETE for the same
  entry_id, allowing the DELETE to proceed unblocked and leaving the ODS
  record soft-deleted despite a newer UPDATE. entry_id alone identifies
  the record; the vessel_type filter on the UPDATE side is preserved.
- `e00d8dab` **Panji Y. Wiwaha** (2026-09-04): fix(sof): handle TUG/BUNKER in fact base query and fix soft-deleted metadata checks
  prepare_base_query.sql: TUG/BUNKER fell into the SEA_VESSEL else-branch
  which requires end_timestamp IS NOT NULL. Portless TUG/BUNKER visits
  have no top-level end so the base CTE returned zero rows, emitting no
  facts while the queue was still marked FACTS_PROCESSING_COMPLETED.
  Added an is_tug_bunker branch that drops the end_timestamp requirement
  and filters by visit_vessel_type IN ('TUG', 'BUNKER').
  
  sof_extract_missing_metadata.sql: missing_ports/terminals/berths did
  not filter deleted_timestamp IS NULL in their NOT EXISTS predicates, so
  soft-deleted ODS entities were treated as present. Fact loaders require
  active records, so deferred SOFs with a deleted port/terminal/berth
  emitted no facts but reached FACTS_PROCESSING_COMPLETED. Added the
  deleted_timestamp guard to all three CTEs.
- `521282ba` **Panji Y. Wiwaha** (2026-09-04): fix(sof): preserve message order in whitelist filter and add deleted_timestamp guards
  base.py: _filter_data returned portless + filtered_data, reordering
  messages so portless records came before port-bearing ones. Since
  to_staging_sof_map keeps the last message per entry_id, an older
  port-bearing update could overwrite a newer portless update from the
  same batch. Fixed by collecting whitelist-passed message identities and
  filtering data in its original consumption order.
  
  sof_validate_metadata.sql: has_port, has_all_terminals, and
  has_all_berths did not guard against soft-deleted ODS rows, unlike the
  recovery query fixed earlier. A SOF with a deleted port/terminal/berth
  was treated as valid, proceeded past the deferred queue, and was marked
  FACTS_PROCESSING_COMPLETED against retired metadata. Added
  deleted_timestamp IS NULL to all three EXISTS predicates.

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-03)

### 🟡 Changes recommended

`resolve_vessel_type()` can raise an exception when the payload contains a non-dict `ship` (e.g., `ship: null`), which would crash streaming ingestion unless made null-safe (and covered by a regression test).

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

Activates end-to-end SOF ingestion for `TUG` and `BUNKER` vessels across batch and RabbitMQ streaming, aligning schema constraints and validation/completion semantics with the expanded `VesselType` model.

**Changes:**
- Extends staging schema + migration logic to allow `TUG`/`BUNKER` vessel types and updates pilot fact delta logic to include them.
- Parameterizes SOF metadata validation in SQL via per-vessel-type completeness flags provided by Python (`VesselType` properties).
- Enables streaming detection/routing by resolving vessel type from `ship.categories`, updates transformer/validator behavior, and wires new sequential task groups into ODS and fact stream DAGs.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `tests/unit/test_sof_is_completed.py` | Adds a shared truth-table test suite for batch vs streaming SOF completion rules and vessel-type resolution. |
| `tests/unit/__init__.py` | Unit test package marker. |
| `teqplay/templates/sql/migration/staging/statement_of_fact_deleted/schema_migration.sql` | Adds idempotent DROP/ADD of the `vessel_type` CHECK constraint for deleted SOF staging. |
| `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql` | Reworks metadata validation to use completeness flags and updates ship lookup rules for TUG/BUNKER. |
| `teqplay/templates/sql/dml/fact/pilot/proceed_delta.sql` | Expands pilot fact delta logic to include TUG/BUNKER and updates completion + ship join conditions accordingly. |
| `teqplay/templates/sql/ddl/staging/statement_of_fact_deleted.sql` | Extends the `vessel_type` CHECK constraint to include `TUG` and `BUNKER`. |
| `teqplay/services/streaming/rabbitmq/sof/validators.py` | Aligns streaming completion validation with `VesselType.requires_slow_moving_periods` semantics. |
| `teqplay/services/streaming/rabbitmq/sof/utils.py` | Adds `resolve_vessel_type()` for category-based vessel type detection in streaming messages. |
| `teqplay/services/streaming/rabbitmq/sof/transformators.py` | Uses resolved vessel type per message and propagates it into staging + processing-queue records. |
| `teqplay/services/streaming/rabbitmq/sof/sea_vessel.py` | Updates validation semantics documentation for sea-vessel queue behavior with TUG/BUNKER detection. |
| `teqplay/services/streaming/rabbitmq/sof/base.py` | Clarifies that the consumer’s `vessel_type` is a default fallback used by resolution. |
| `teqplay/services/statement_of_fact.py` | Simplifies batch completion logic to mirror the `requires_slow_moving_periods` gate. |
| `teqplay/repositories/statement_of_fact.py` | Passes completeness flags from `VesselType` into the SQL metadata validation template. |
| `teqplay/dags/warehouse/ods/ods_sof/stream_dag.py` | Adds sequential TUG → BUNKER update/delete groups to the ODS SOF stream DAG. |
| `teqplay/dags/mart/fact_sof/stream_dag.py` | Adds sequential TUG → BUNKER update/delete groups to the fact SOF stream DAG. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 14/15 changed files
- **Comments generated:** 2
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-03)

_No comment._

### ryan-kharisma — DISMISSED (2026-09-03)

Looks good to me

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-09-04)

LGTM

## Review Comments

### Copilot — 2026-09-03 on `teqplay/services/streaming/rabbitmq/sof/utils.py`

resolve_vessel_type can raise AttributeError when the message contains an explicit 'ship': None (or any non-dict), because data.get('ship', {}) returns None and then .get('categories') is called on it. This is plausible since SOFStagingData.from_dict sets ship=data.get('ship') and ship is optional in real payloads.

### Copilot — 2026-09-03 on `tests/unit/test_sof_is_completed.py`

test_resolve_vessel_type does not cover the case where the payload includes 'ship': None (or a non-dict ship), which currently triggers an exception in resolve_vessel_type; adding a regression case would lock in the intended fallback-to-default behavior.

### panjiyudasetya — 2026-09-03 on `teqplay/services/statement_of_fact.py`

TUG/BUNKER is streaming-only here; the batch wiring would be implemented in another PR. The code is preparatory, not broken.

### panjiyudasetya — 2026-09-03 on `tests/unit/test_sof_is_completed.py`

Resolved by b1bca29

### panjiyudasetya — 2026-09-03 on `teqplay/services/streaming/rabbitmq/sof/utils.py`

Resolved by b1bca29

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/fact/pilot/proceed_delta.sql`

Resolved by 1746ae4

### panjiyudasetya — 2026-09-03 on `teqplay/services/streaming/rabbitmq/sof/utils.py`

Resolved by b1bca29

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

Resolved by 0af563d

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

Resolved by 46b69f1

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

Resolved by 46b69f1

### panjiyudasetya — 2026-09-03 on `teqplay/dags/warehouse/ods/ods_sof/stream_dag.py`

Resolved by 228c4ff

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/anchor_stop/stg_to_ods.sql`

If you actually want "is an array AND non-empty," combine it explicitly: 

jsonb_typeof(col) = 'array' AND jsonb_array_length(col) > 0 

— this is unambiguous and self-documenting, whereas col != '[]' conflates "is array" and "is non-empty" into one fragile string check.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/berth_visit/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/encounter/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/lock_stop/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/ship_to_ship_transfers/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/slow_moving_period/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/terminal_visit/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/tug_event/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/tug_event/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/unclassified_stop/stg_to_ods.sql`

same with the one above.

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/visited_approach_area/stg_to_ods.sql`

same with the one above.

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

Resolved by 7709c51

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/processing_queue/sof_extract_missing_metadata.sql`

Resolved by 0f7d073

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/ods/anchor_stop/stg_to_ods.sql`

Resolved by 8d6037c. A bit of context why I need to change the implementation is that JSON null and an empty array are different `JSONB` values:

```sql
'null'::jsonb != '[]'::jsonb  -- TRUE
```

As a result, col != '[]' allows JSON null to pass through. If the next operation is `jsonb_array_elements(col)`, PostgreSQL attempts to extract elements from a JSON scalar and raises:

```
cannot extract elements from a scalar
```

The behavior is:
| Col | `col != '[]'` | Safe for `jsonb_array_elements`? |
| :--- | :---  | :---  |
| SQL `NULL`  | NULL → filtered out | Yes |
| JSON `null` | TRUE → passes through | No |
| [] | FALSE → filtered out | Yes |
| Non-empty array | TRUE → passes through | Yes |

`jsonb_typeof(col) = 'array'` expresses the actual requirement: only process values whose JSON type is an array. JSON null has type `'null'`, so it is correctly filtered out.

Therefore in this case, I agree to add additional length check:
```sql
jsonb_typeof(col) = 'array' AND jsonb_array_length(col) > 0
```

### panjiyudasetya — 2026-09-03 on `teqplay/services/streaming/rabbitmq/sof/transformators.py`

Resolved by 49353c7

### panjiyudasetya — 2026-09-03 on `teqplay/dags/warehouse/ods/ods_sof/stream_dag.py`

Resolved by 528b52c

### panjiyudasetya — 2026-09-03 on `teqplay/templates/sql/dml/processing_queue/sof_extract_missing_metadata.sql`

Resolved by 49353c7

### ryan-kharisma — 2026-09-03 on `teqplay/templates/sql/dml/ods/anchor_stop/stg_to_ods.sql`

okay cool 

### panjiyudasetya — 2026-09-03 on `teqplay/services/streaming/rabbitmq/sof/transformators.py`

Resolved by b108d0a

### panjiyudasetya — 2026-09-03 on `teqplay/tasks/prepare_db/migration_task_groups.py`

Resolved by 1fa6d87

### panjiyudasetya — 2026-09-04 on `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

Resolved eeefc7e

### panjiyudasetya — 2026-09-04 on `teqplay/services/streaming/rabbitmq/sof/base.py`

Resolved eeefc7e

### panjiyudasetya — 2026-09-04 on `teqplay/templates/sql/migration/fact/stdev_time_terminal_visit_overall/schema_migration.sql`

Resolved e9bc716

### panjiyudasetya — 2026-09-04 on `teqplay/services/streaming/rabbitmq/sof/transformators.py`

Resolved a5e054c

### panjiyudasetya — 2026-09-04 on `teqplay/templates/sql/dml/staging/sof/hard_delete_queue_aware.sql`

Resolved 53a50b1

### panjiyudasetya — 2026-09-04 on `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

Resolved e00d8da

### panjiyudasetya — 2026-09-04 on `teqplay/dags/mart/fact_sof/stream_dag.py`

Resolved e00d8da

### panjiyudasetya — 2026-09-04 on `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

Resolved 521282b

### panjiyudasetya — 2026-09-04 on `teqplay/services/streaming/rabbitmq/sof/base.py`

Resolved 521282b

## Comments

### panjiyudasetya — 2026-09-03

augment review

### panjiyudasetya — 2026-09-03

augment review

### panjiyudasetya — 2026-09-03

augment review

### panjiyudasetya — 2026-09-03

augment review

### panjiyudasetya — 2026-09-03

augment review

### panjiyudasetya — 2026-09-03

augment review

### panjiyudasetya — 2026-09-04

augment review

### panjiyudasetya — 2026-09-04

augment review

### panjiyudasetya — 2026-09-04

augment review

### panjiyudasetya — 2026-09-04

augment review

### panjiyudasetya — 2026-09-04

augment review

### panjiyudasetya — 2026-09-04

augment review
