---
id: github:teqplay/dataflow_dag_core:pr:766
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 766
title: PTO-2964  BUNKER vessel ingestion + enforce complete visits for TUG and BUNKER
author: panjiyudasetya
state: closed
date: '2026-09-09'
merged_at: '2026-09-11'
base_branch: develop
head_branch: PTO-2964
url: https://github.com/teqplay/dataflow_dag_core/pull/766
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2964
- jira:PTO-2819
- jira:PTO-2963
---
# PR #766: PTO-2964  BUNKER vessel ingestion + enforce complete visits for TUG and BUNKER

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/766  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2964`  
**Created:** 2026-09-09  
**Merged:** 2026-09-11  

## Description

### Description

Adds BUNKER vessel ingestion (batch DAG, streaming path) and enforces that TUG and BUNKER visits must be fully complete — i.e., must have an `end_timestamp` — before being promoted to any fact table, matching the existing SEA_VESSEL requirement. Also cleans up the SQL template layer to reflect this unified behaviour.

### Functional changes

- **BUNKER batch DAG** (`fact_sof__bunker`) wired into the fact orchestrator
- **BUNKER streaming** enabled in `fact_sof__stream`
- **`fact_port_visit` excluded** for TUG and BUNKER — port visit population only applies to SEA_VESSEL and BARGE; stale rows purged via hard-delete
- **Complete visit required** for TUG and BUNKER: `end_timestamp IS NOT null` now enforced in all fact DML, QC accuracy, completeness, and validity templates
- **Staging insert** fixed: `vessel_type` conflict column corrected

### SQL template cleanup

- All `end_timestamp IS null` escape hatches removed from TUG/BUNKER time-range filter branches
- 3-way `{% if is_barge %}/{% elif is_tug_bunker %}/{% else %}` blocks collapsed to 2-level `{% if is_barge %}/{% else %}` across 29 fact DML and QC component files
- `{% set is_tug_bunker %}` removed everywhere it appeared (now unused)
- Join comment updated: `SEA_VESSEL (default)` → `SEA_VESSEL/TUG/BUNKER (default)`
- `visit_vessel_type` filter moved inside the `{% if not is_streaming_data %}` batch-only block in 13 streaming-capable templates — streaming mode now filters solely by `visit_id`
- 4 QC completeness files (`berth_visit`, `port_visit`, `terminal_visit`, `encounter`) updated to match the same 2-level pattern

## Test plan

- [ ] Unit tests updated for `is_sof_valid` (removal of `_is_sof_completed`) — `pytest tests/unit/test_sof_is_completed.py`
- [ ] Batch resolve tests added for TUG/BUNKER `fact_port_visit` purge
- [ ] Verify BUNKER batch DAG triggers correctly via `start_etl_pipeline`
- [ ] Verify BUNKER streaming path handles `rabbitmq_handler` → `fact_sof__stream` correctly
- [ ] Confirm no TUG/BUNKER rows appear in `fact_port_visit` after hard-delete runs
- [ ] Run `pytest tests/` for full unit suite

## Commits

- `648a63ae` **Panji Y. Wiwaha** (2026-09-08): feat(sof): enable BUNKER vessel ingestion in batching path
  Extends TUG vessel support (PTO-2819) to also resolve BUNKER vessels at
  the point of staging flatten, preventing BARGE-tagged bleed-through and
  enabling correct vessel_type propagation through ODS to fact tables.
- `eeb534ce` **Panji Y. Wiwaha** (2026-09-09): refactor(sof): inline _is_sof_completed into is_sof_valid
- `50693f13` **Panji Y. Wiwaha** (2026-09-09): PTO-2963 feat(sof): add fact_sof__bunker batch DAG and wire into fact orchestrator
  BUNKER records arrive via the SEA_VESSEL and BARGE ingestion paths and are
  stamped with visit_vessel_type='BUNKER' by _resolve_vessel_type. Without a
  dedicated DAG they would be silently skipped by the SEA_VESSEL and BARGE
  fact queries. Mirrors the TUG pattern introduced in PTO-2819-pt3.
- `2cdbac4a` **Panji Y. Wiwaha** (2026-09-09): test(sof): update batch SOF tests to call is_sof_valid after _is_sof_completed removal
- `5c651789` **Panji Y. Wiwaha** (2026-09-09): docs(sof): correct SOFService docstring — TUG/BUNKER bleed-through now accepted
- `59d5facb` **Panji Y. Wiwaha** (2026-09-09): fix(sof): correct vessel_type on conflict in staging insert
  ON CONFLICT DO NOTHING prevented batch reruns from correcting pre-existing
  BARGE-tagged staging rows that belong to TUG/BUNKER vessels. The conflict
  clause now updates vessel_type when it differs, matching the upsert.sql
  behaviour used by the streaming path.
- `4692fb08` **Panji Y. Wiwaha** (2026-09-09): docs(sof): fix BUNKER docstring — berth completeness enforced at fact load, not via sof_validate_metadata.sql
- `81c7060a` **Panji Y. Wiwaha** (2026-09-09): feat(sof): exclude fact_port_visit from TUG and BUNKER fact DAGs
  TUG and BUNKER data is only relevant at the terminal and berth level.
  Port-level fact rows are not needed and are now intentionally skipped.
- `3d683234` **Panji Y. Wiwaha** (2026-09-09): docs(sof): document why fact_port_visit is excluded from TUG and BUNKER DAGs
- `9989d094` **Panji Y. Wiwaha** (2026-09-09): feat(sof): exclude fact_port_visit from TUG and BUNKER in streaming update path
  Port visit is intentionally excluded for TUG and BUNKER in the streaming
  pipeline, consistent with the batch DAGs. Only terminal and berth level
  data is required for these vessel types.
- `d8ad9cb6` **Panji Y. Wiwaha** (2026-09-09): fix(sof): purge stale TUG/BUNKER fact_port_visit rows and add batch resolve tests
  - Migration: DELETE fact_port_visit WHERE visit_vessel_type IN ('TUG', 'BUNKER')
    to remove pre-existing rows that would produce mixed legacy/current port-level
    metrics in fact_daily_refresh aggregations after these vessel types were moved
    to terminal/berth-level only.
  - Tests: add test_batch_resolve_vessel_type covering SOFService._resolve_vessel_type,
    including TUG/BUNKER detection, TUG priority, default fallback, and None guards.
- `03f91db2` **Panji Y. Wiwaha** (2026-09-10): feat(sof): require complete terminal and berth visits for TUG and BUNKER
  Both TUG and BUNKER now require end_timestamp on terminal and berth visits
  before a record is promoted to the fact layer or counted as complete by QC.
  Previously only start_timestamp was required (open-ended visits were allowed).
  
  - VesselType.requires_terminal_completeness: TUG and BUNKER added (was SEA_VESSEL only)
  - VesselType.requires_berth_completeness: TUG added (BUNKER was already included)
  - prepare_base_terminal_visit.sql: TUG/BUNKER branch now requires tv.end_timestamp IS NOT null
  - prepare_base_berth_visit.sql: TUG/BUNKER branch now requires bv.end_timestamp IS NOT null
  - QC completeness/terminal_visit/prepare_ods_data.sql: same end_timestamp guard added
  - QC completeness/berth_visit/prepare_ods_data.sql: same end_timestamp guard added
- `fbb3d37d` **Panji Y. Wiwaha** (2026-09-10): fix(sof): require complete port visits for TUG and BUNKER in DML and QC
  Aligns port visit DML and QC completeness with the new requirement that
  TUG and BUNKER visits must have an end_timestamp to be considered complete.
  
  - prepare_base_query.sql: TUG/BUNKER branch now requires pv.end_timestamp IS NOT null;
    removed the open-ended time-range allowance (OR pv.end_timestamp IS null) that was
    only valid when open-ended visits were accepted
  - QC completeness/port_visit/prepare_ods_data.sql: same end_timestamp guard added
  
  fact_port_visit is not loaded for TUG/BUNKER (excluded from those DAGs), but the
  DMLs must be correct so a future enablement or manual replay does not silently
  admit incomplete records.
- `763bcc72` **Panji Y. Wiwaha** (2026-09-10): fix(sof): remove open-ended end_timestamp allowance for TUG and BUNKER in all fact DML
  All Jinja time-range blocks that special-cased TUG/BUNKER with
    AND (end_timestamp > %(start)s OR end_timestamp IS null)
  are collapsed to the standard
    AND end_timestamp > %(start)s
  because TUG and BUNKER visits now require a complete end_timestamp before
  they are promoted to any fact table. The is_tug_bunker branch was always
  identical to the else branch except for the IS null escape hatch — removing
  it makes every vessel type consistent.
  
  24 files changed across hard_delete, proceed, and prepare_* DML templates
  covering anchor, berth_visit, bunkering, pilot, port_visit, ship_to_ship,
  terminal_visit, and tug fact tables.
- `4f62a0dc` **Panji Y. Wiwaha** (2026-09-10): fix(sof): remove open-ended end_timestamp allowance for TUG and BUNKER in all QC SQLs
  Mirrors the same fix applied to fact DML templates: every is_tug_bunker
  time-range block of the form
    AND (end_timestamp > '{{ start }}' OR end_timestamp IS null)
  is collapsed to the standard
    AND end_timestamp > '{{ start }}'
  because TUG and BUNKER visits now require a complete end_timestamp.
  
  14 files changed across accuracy (port_visit, terminal_visit),
  completeness (encounter), and validity QC templates.
- `e4eaa83a` **Panji Y. Wiwaha** (2026-09-10): refactor(sof): replace redundant vessel_type filter conditionals with direct Jinja variable
  The {% if is_barge %} 'BARGE' / {% elif is_tug_bunker %} '{{ vessel_type }}' / {% else %}
  'SEA_VESSEL' {% endif %} pattern was overused in 20 QC accuracy files where the only
  difference between branches was the vessel_type literal value. Since vessel_type is always
  passed as a concrete string (SEA_VESSEL, BARGE, TUG, BUNKER), the conditional is redundant
  — every branch resolves to exactly the same thing as '{{ vessel_type }}'. Collapsed to a
  single line and removed the now-unused {% set is_barge %} and {% set is_tug_bunker %}
  variables in those files.
  
  Also applies minor noqa / alignment cleanup in 5 component files (replacing the
  --noqa: disable/enable block pattern with inline --noqa: TMP comments).
- `bb42f483` **Panji Y. Wiwaha** (2026-09-10): refactor(sof): simplify vessel_type branching in port_travel_duration_components
  TUG/BUNKER and SEA_VESSEL share the same ship identification (IMO-based) and
  start_timestamp requirement. Collapse the 3-way if/elif/else into 2-level nesting:
  is_barge determines the JOIN and identification check; the inner block adds
  SEA_VESSEL-specific conditions (end_timestamp + pilot timestamps) that are not
  needed for TUG/BUNKER. Removes the now-unused is_tug_bunker set variable.
- `b5b61dca` **Panji Y. Wiwaha** (2026-09-10): refactor(sof): simplify vessel type WHERE blocks across fact DML and QC component files
  Collapses 3-way {% if is_barge %}/{% elif is_tug_bunker %}/{% else %} into 2-level
  {% if is_barge %}/{% else %} now that TUG/BUNKER share IMO identification and both
  require start_timestamp and end_timestamp for a complete visit.
  
  - Removes unused {% set is_tug_bunker %} variable from all 29 files
  - Fixes stale TUG/BUNKER branches that incorrectly omitted end_timestamp requirement
  - Moves visit_vessel_type filter outside the conditional (shared by all vessel types)
  - Updates join comment from "SEA_VESSEL (default)" to "SEA_VESSEL/TUG/BUNKER (default)"
  - sailing_duration_components.sql retains an inner SEA_VESSEL-only block for pilot timestamps
- `3be35fd4` **Panji Y. Wiwaha** (2026-09-10): fix(sof): move visit_vessel_type filter into batch-only block for streaming-safe templates
  In files with is_streaming_data, the vessel type filter was unconditionally applied
  before the batch/streaming branch, causing it to run in streaming mode where visits
  are already identified by visit_id. Move it inside the BATCH MODE block so streaming
  mode filters only by visit_id without any vessel type constraint.
  
  Affected: 13 DML templates across port_visit, berth_visit, and terminal_visit layers.
- `0cfecb06` **Panji Y. Wiwaha** (2026-09-10): fix(sof): complete vessel type WHERE block cleanup across completeness and fact DML files
  - Collapse 3-way if/elif(tug_bunker)/else → 2-level in 4 QC completeness files
    (berth_visit, port_visit, terminal_visit, encounter); fix stale TUG/BUNKER branch
    in encounter that omitted end_timestamp; update join comment to SEA_VESSEL/TUG/BUNKER
  - Remove unused {% set is_tug_bunker %} from 9 additional files where it was defined
    but never referenced (hard_delete files for anchor/bunkering/pilot/ship_to_ship/tug,
    port_visit add_* files, and validity/port_visit_anchor_overlaps.sql)
- `ad291fd2` **Panji Y. Wiwaha** (2026-09-10): fix(sof): exclude TUG/BUNKER from orphan cleanup in operational fact tables
  delete_orphaned_visits.sql for fact_tug, fact_anchor, fact_bunkering, and fact_pilot
  used fact_port_visit as the sole validity check. TUG and BUNKER visits are intentionally
  not written to fact_port_visit, so every TUG/BUNKER operational event row appeared
  orphaned and was purged on the next worker run.
  
  Add AND f.vessel_type NOT IN ('TUG', 'BUNKER') to each orphan query so the check only
  fires for vessel types (SEA_VESSEL, BARGE) that do populate fact_port_visit.
  vessel_type carries an index on all four tables so the filter is cheap.
- `4d133be5` **Panji Y. Wiwaha** (2026-09-10): fix(sof): resolve TUG/BUNKER fact_port_visit gaps in delete, accuracy, and completeness QC
  **Feedback 1 — hard_delete BATCH MODE (5 files)**
  anchor, bunkering, pilot, tug, ship_to_ship hard_delete.sql all scoped batch deletions
  via a fact_port_visit subquery. TUG/BUNKER have no rows there, making batch deletes
  no-ops and leaving stale facts after reruns.
  Fix: add TUG/BUNKER branch that scopes directly against the fact table's own columns
  (unlocode/port_unlocode + start/end timestamps, or single timestamp for fact_pilot).
  SEA_VESSEL/BARGE retain the existing fact_port_visit-scoped path.
  
  **Feedback 2 — completeness ODS→FACT check for TUG/BUNKER**
  check_port_visit_completeness always ran qc_ods_fact against fact_port_visit, which is
  empty for TUG/BUNKER, generating false 0% incompleteness alerts on every DAG run.
  Fix: at DAG parse time, skip qc_ods_fact for TUG/BUNKER and wire a sentinel task
  (skip_ods_fact_check) in its place. write_port_visit_report omits the ODS→FACT row from
  the batch insert when the sentinel's not_applicable flag is set.
  
  **Feedback 3 — accuracy QC filtering via fact_port_visit (7 files)**
  Seven accuracy QC files used LEFT JOIN fact_port_visit + WHERE pv.visit_vessel_type = '...'
  to scope records. For TUG/BUNKER the JOIN resolves to NULL, making every WHERE false
  and returning zero rows — no TUG/BUNKER operational facts were ever validated.
  Fix: drop the fact_port_visit JOIN from all seven files; filter and scope using the
  fact table's own vessel_type, unlocode, and timestamp columns directly. For fact_pilot
  (single timestamp, not a range), replace filter_by_time_range with explicit >= / < guards.
  
  m
- `f98d54cb` **Panji Y. Wiwaha** (2026-09-10): fix(sof): clean up stale berth/terminal rows and skip port_visit accuracy for TUG/BUNKER
  TUG/BUNKER visits require end_timestamp before fact promotion. If a SOF correction
  removes end_timestamp after rows are already in fact_berth_visit / fact_terminal_visit,
  the upsert-only pattern leaves stale rows. Fix: add a cleanup DELETE step (scoped by
  entry_ids in streaming mode, by vessel_type+unlocode+time range in batch mode) that
  runs before the upsert so only visits that remain complete are re-inserted.
  
  Also skip the port_visit accuracy check for TUG/BUNKER in vessel_voyage_data_accuracy:
  fact_port_visit is intentionally empty for these vessel types, causing all five port_visit
  accuracy checks to produce false 0% failures. A skip_port_visit_accuracy sentinel task
  replaces the check group for TUG_VISIT and BUNKER_VISIT domains.
- `5ff02acf` **Panji Y. Wiwaha** (2026-09-10): fix(sof): scope TUG/BUNKER batch hard_delete by port-visit ID via fact_berth_visit
  The TUG/BUNKER batch hard_delete branches previously scoped deletions using the
  operational event's own timestamps (start_timestamp/end_timestamp or pilot.timestamp).
  However, the source queries filter by the PARENT PORT VISIT's timestamps, so events
  belonging to an overlapping port visit but just outside the batch window were never
  deleted, leaving stale rows on SOF corrections.
  
  Fix: replace event-timestamp scope with visit_id-based scope using fact_berth_visit
  as the DATA_MART proxy for the port visit's time range — mirroring the SEA_VESSEL/BARGE
  approach via fact_port_visit. Applied to anchor, bunkering, tug, pilot, and ship_to_ship
  hard_delete files, and both cleanup_incomplete_tug_bunker files (berth_visit uses a
  self-referential visit_id expansion; terminal_visit uses fact_berth_visit directly).
- `348e8fd6` **Panji Y. Wiwaha** (2026-09-10): fix(sof): replace fact_berth_visit proxy with self-proxy in TUG/BUNKER batch hard_delete and align pilot accuracy scope
  Self-proxy: each operational fact table now finds visit_ids by scanning its own
  rows for events overlapping the batch window, then deletes all rows for those
  visits. Eliminates the fact_berth_visit dependency that could leave stale rows
  whenever a TUG/BUNKER visit has no berth facts.
  
    - anchor/hard_delete: self-proxy via fact_anchor (no port_unlocode; uses start/end timestamps)
    - bunkering/hard_delete: self-proxy via fact_bunkering (port_unlocode + start/end timestamps)
    - tug/hard_delete: self-proxy via fact_tug (port_unlocode + start/end timestamps)
    - pilot/hard_delete: self-proxy via fact_pilot (port_unlocode + single timestamp column)
    - ship_to_ship/hard_delete: self-proxy via fact_ship_to_ship_transfers (no port_unlocode; uses start/end timestamps)
    - terminal_visit/cleanup_incomplete_tug_bunker: self-proxy via fact_terminal_visit
  
  Pilot accuracy scope: summary_accuracy.sql now scopes by fact_port_visit overlap
  (start_timestamp < end AND (end_timestamp IS null OR end_timestamp > start))
  instead of fp.timestamp >= start AND < end, matching the port-visit-centric
  scoping used in pilot_components.sql and eliminating the inner-join boundary gap.
- `2d8046e4` **Panji Y. Wiwaha** (2026-09-10): fix(sof): scope TUG/BUNKER cleanup by parent port visit and run BUNKER facts after BARGE branch
  Feedback 1 — BUNKER fact DAG now runs after the BARGE branch
  BUNKER records may arrive via the BARGE ingestion path. Previously
  call_fact_sof_bunker ran before is_include_barge, so when is_barge_included=False
  the BARGE-sourced BUNKER records had never reached ODS yet. A barge_done merge
  node now sits between the BARGE branch and BUNKER, ensuring BUNKER fact processing
  always sees the full set of available BUNKER records in ODS.
  
  Feedback 2 — cleanup scoped by ods_port_visit instead of child timestamps
  The pre-upsert cleanup for fact_berth_visit and fact_terminal_visit was
  finding parent visits from their own child timestamps (self-proxy). A child
  whose timestamps are entirely outside the batch window but whose parent
  overlaps would be omitted by the upsert and also missed by the cleanup,
  leaving a stale fact row.
  
  Fix: convert cleanup_incomplete_tug_bunker to a Python @task for both
  berth_visit and terminal_visit. In batch mode it queries ods_port_visit
  (DATA_WAREHOUSE) for all TUG/BUNKER port_visit IDs overlapping the window
  via fetch_tug_bunker_visit_ids (new helper in utils.py). In streaming mode
  it uses the existing entry_ids. The DELETE then scopes by those visit IDs,
  covering all children regardless of their own timestamps.
- `95918539` **Panji Y. Wiwaha** (2026-09-10): refactor(sof): load cleanup SQL from template file instead of hardcoding
  Replace inline DELETE strings in cleanup_incomplete_tug_bunker_berth and
  cleanup_incomplete_tug_bunker_terminal with render_sql_template calls,
  consistent with how other Python tasks in this module load their SQL.
- `f6ab52e1` **Panji Y. Wiwaha** (2026-09-10): fix(sof): include visits with cleared end_timestamp in TUG/BUNKER cleanup scope
  fetch_tug_bunker_visit_ids used AND pv.end_timestamp > %(start)s to find
  overlapping port visits. A correction that clears end_timestamp sets it to
  NULL, which fails a strict > comparison and excluded the visit from the
  result — so the stale berth/terminal fact rows were never deleted.
  
  Changed the filter to (pv.end_timestamp IS NULL OR pv.end_timestamp > %(start)s)
  so that visits whose end_timestamp was just retracted are still returned,
  allowing cleanup to delete their now-stale fact rows before the upsert runs.
- `ff11edea` **Panji Y. Wiwaha** (2026-09-10): refactor(sof): extract fetch_tug_bunker_visit_ids query into SQL template
  Moved the inline ODS query from fetch_tug_bunker_visit_ids into
  dml/ods/port_visit/fetch_tug_bunker_visit_ids.sql, consistent with the
  project convention of keeping SQL out of Python.
  
  Parameters remain psycopg2-style (%(name)s) and are bound at execution
  time via hook.get_records, same as before — no behaviour change.
- `a6ad8177` **Panji Y. Wiwaha** (2026-09-10): fix(qc): align bunkering and tug summary_accuracy scope with component queries
  bunkering_components.sql and tug_components.sql both scope source rows by
  parent port visit overlap (pv.start_timestamp / pv.end_timestamp). The
  corresponding summary_accuracy.sql files were filtering by the encounter's
  own timestamps, so encounters whose parent overlapped the window but whose
  own timestamps fell outside were silently dropped from the accuracy
  comparison, artificially inflating coverage gaps.
  
  Changed both summary_accuracy.sql files to scope through fact_port_visit
  overlap (same pattern applied to pilot/summary_accuracy.sql previously),
  ensuring the fact side evaluates the same visit set as the component side.
- `4a82db0d` **Panji Y. Wiwaha** (2026-09-10): fix(sof): guard parent end_timestamp in streaming mode and fix TUG/BUNKER accuracy scope
  Streaming correction re-insert bug (Feedback 1):
  prepare_base_berth_visit.sql and prepare_base_terminal_visit.sql filtered
  the streaming branch only by entry_ids, without checking pv.end_timestamp.
  If a batch correction clears the parent port visit's end_timestamp, cleanup
  deletes the stale facts but proceed_fact immediately re-inserts them because
  the child berth/terminal still has an end time. Added
  AND pv.end_timestamp IS NOT null for TUG/BUNKER in the streaming branch to
  block re-insertion when the parent is incomplete.
  
  Accuracy scope empty for TUG/BUNKER (Feedback 2):
  The previous fix scoped all three summary_accuracy.sql files (bunkering,
  tug, pilot) via a fact_port_visit subquery. TUG/BUNKER have no
  fact_port_visit rows (include_port_visit=False), so the subquery returned
  empty and the accuracy comparison processed zero records. Added a
  vessel_type branch so TUG/BUNKER fall back to event-level timestamps,
  keeping the fact side non-empty.

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-09)

### 🟡 Changes recommended

The removal of `SOFService._is_sof_completed` breaks the existing unit test suite unless tests are updated or a compatibility wrapper is restored.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

This PR extends the SOF batching ingestion path to correctly identify and process `BUNKER` vessels (in addition to `SEA_VESSEL`, `BARGE`, and `TUG`) by resolving vessel type from `ship.categories`, and adds a corresponding daily refresh task group to the mart DAG.

**Changes:**
- Updated `SOFService._resolve_vessel_type` to detect `BUNKER` (after `TUG`) and simplified batch SOF validation so only `SEA_VESSEL` requires `end` + `slowMovingPeriods`.
- Removed the batch-path BUNKER filter helper and aligned duplicate-record logging to use the module logger.
- Added a `REFRESH_FACT_SOF_BUNKER` task group and chained it after `TUG` in the daily mart refresh DAG.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `teqplay/services/statement_of_fact.py` | Adds BUNKER vessel-type resolution in batching and simplifies SOF validity/completion logic. |
| `teqplay/dags/mart/fact_daily_refresh_dag.py` | Adds a daily refresh task group for BUNKER and wires it into the DAG chain. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 2/2 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/PTO-2819-pt3?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-09)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — DISMISSED (2026-09-09)

LGTM

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F766%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-10)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-09-11)

LGTM

## Review Comments

### Copilot — 2026-09-09 on `teqplay/services/statement_of_fact.py`

`SOFService._is_sof_completed` was removed, but it’s still referenced by the unit test suite (`tests/unit/test_sof_is_completed.py`). Unless those tests are updated in this PR, CI will fail. Consider reintroducing `_is_sof_completed` as a thin wrapper around the current `is_sof_valid` logic (or update the tests accordingly).

### panjiyudasetya — 2026-09-09 on `teqplay/services/statement_of_fact.py`

Resolved by 603ed70

### panjiyudasetya — 2026-09-09 on `teqplay/services/statement_of_fact.py`

Resolved 81c09d2

### panjiyudasetya — 2026-09-09 on `teqplay/services/statement_of_fact.py`

Resolved 4ebb211

### panjiyudasetya — 2026-09-09 on `teqplay/services/statement_of_fact.py`

Resolved 6512a70

### panjiyudasetya — 2026-09-10 on `teqplay/dags/mart/fact_sof/stream_dag.py`

Resolved ad291fd

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/quality_control/accuracy/anchor/summary_accuracy.sql`

Resolved 4d133be

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/quality_control/completeness/port_visit/prepare_ods_data.sql`

Resolved 4d133be

### panjiyudasetya — 2026-09-10 on `teqplay/dags/mart/fact_sof/bunker_vessel_dag.py`

Resolved 4d133be

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/quality_control/accuracy/port_visit/drifting_duration_accuracy.sql`

Resolved f98d54c

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/dml/fact/berth_visit/prepare_base_berth_visit.sql`

Resolved f98d54c

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/dml/fact/pilot/hard_delete.sql`

Resolved 5ff02ac

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/quality_control/accuracy/pilot/summary_accuracy.sql`

Resolved 348e8fd

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/dml/fact/anchor/hard_delete.sql`

Resolved 348e8fd

### panjiyudasetya — 2026-09-10 on `teqplay/dags/pipeline/fact_transformation_dag.py`

Resolved 2d8046e

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/dml/fact/terminal_visit/cleanup_incomplete_tug_bunker.sql`

Resolved 2d8046e

### panjiyudasetya — 2026-09-10 on `teqplay/tasks/fact/sof/utils.py`

Resolved ff11ede

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/quality_control/accuracy/bunkering/summary_accuracy.sql`

Resolved a6ad817

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/quality_control/accuracy/bunkering/summary_accuracy.sql`

Resolved 4a82db0

### panjiyudasetya — 2026-09-10 on `teqplay/templates/sql/dml/fact/berth_visit/prepare_base_berth_visit.sql`

Resolved 4a82db0

## Comments

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-09

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review

### panjiyudasetya — 2026-09-10

augment review
