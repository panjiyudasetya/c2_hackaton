---
id: github:teqplay/dataflow_dag_core:pr:768
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 768
title: Refactor SOF - Introduce `PUSHBARGE` vessel type and resolve from `ship.role`
author: panjiyudasetya
state: closed
date: '2026-09-14'
merged_at: '2026-09-15'
base_branch: develop
head_branch: fix/vessel_type
url: https://github.com/teqplay/dataflow_dag_core/pull/768
labels: []
linked_issues: []
explicit_links: []
---
# PR #768: Refactor SOF - Introduce `PUSHBARGE` vessel type and resolve from `ship.role`

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/768  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `fix/vessel_type`  
**Created:** 2026-09-14  
**Merged:** 2026-09-15  

## Description

### Description

- **TUG → PUSHBARGE**: The `TUG` vessel type constant was invalid. The correct SOF classification is `PUSHBARGE`. All references updated across the stack.
- **Vessel type source**: Detection switched from `ship.categories` to `ship.role` in both batch (`StatementOfFactService`) and streaming (`resolve_vessel_type`). 
  - ship.role = 'PUSHBARGE'` → `vessel_type = 'PUSHBARGE'`;
  - `ship.role = 'BUNKER'` → `vessel_type = 'BUNKER'`.
- **DAG rename**: `fact_sof__tug` → `fact_sof__pushbarge`, including all wiring in `fact_daily_refresh_dag` and `fact_transformation_dag`.
- **Streaming port exclusion**: `include_port_visit=False` for PUSHBARGE preserved in the streaming fact pipeline — equivalent to the batch pipeline's port-level exclusion.
- **Migrations squashed**: Since this branch has not been deployed to production, the two-step migration (add TUG → rename to PUSHBARGE) is collapsed into a single block that directly adds `PUSHBARGE` to each CHECK constraint (20 files).

### Files changed

| Area | Notes |
|---|---|
| Model & services | `VesselType.PUSHBARGE`, `is_pushbarge`; SOF batch + streaming services |
| DAGs | `pushbarge_vessel_dag.py` (new), `tug_vessel_dag.py` (deleted), refresh + transformation DAGs |
| Tasks | `main_task_groups`, `stream_task_groups`, `common.py`, `vessel_voyage_task_groups` |
| SQL DDL | 22 files — CHECK constraints updated |
| SQL DML / QC | ~35 files — filter literals updated |
| Schema migrations | 20 `schema_migration.sql` files squashed |

### Dev data cleanup — run before `prepare_database`

The squashed migration adds the `PUSHBARGE` CHECK constraint directly with no `UPDATE` step. Any existing rows with `vessel_type = 'TUG'` will violate the new constraint. Run the script below manually on dev to purge stale data first.

Execute top-to-bottom (fact tables first, staging last) to respect FK dependencies:

```sql
BEGIN;

-- Fact tables
DELETE FROM fact_port_performance_analytics
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_stdev_time_terminal_visit_monthly
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_stdev_time_terminal_visit
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_port_calls
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_port_calls_terminal
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_bunkering_delta
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_bunkering
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_anchor_delta
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_anchor
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_pilot_delta
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_pilot
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_tug_delta
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_tug
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_ship_to_ship_transfers
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_terminal_visit
WHERE visit_vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_berth_visit
WHERE visit_vessel_type IN ('TUG', 'BUNKER');

DELETE FROM fact_port_visit
WHERE visit_vessel_type IN ('TUG', 'BUNKER');

-- ODS tables
DELETE FROM ods_terminal_visit
WHERE visit_vessel_type IN ('TUG', 'BUNKER');

DELETE FROM ods_berth_visit
WHERE visit_vessel_type IN ('TUG', 'BUNKER');

DELETE FROM ods_port_visit
WHERE visit_vessel_type IN ('TUG', 'BUNKER');

-- Processing queue
DELETE FROM sof_processing_queue
WHERE vessel_type IN ('TUG', 'BUNKER');

-- Staging
DELETE FROM stg_statement_of_fact_deleted
WHERE vessel_type IN ('TUG', 'BUNKER');

DELETE FROM stg_statement_of_fact
WHERE vessel_type IN ('TUG', 'BUNKER');

COMMIT;
```

## Commits

- `5d1f7c91` **Panji Y. Wiwaha** (2026-09-14): refactor(sof): rename TUG to PUSHBARGE and resolve vessel type from ship.role
  - Rename VesselType.TUG → VesselType.PUSHBARGE and is_tug → is_pushbarge
  - Update VALID_TYPES to include PUSHBARGE instead of TUG
  - Change vessel type detection source from ship.categories to ship.role
    in both batch (StatementOfFactService) and streaming (resolve_vessel_type)
  - Update SOFStagingData docstring to reflect accepted vessel types
- `06b38918` **Panji Y. Wiwaha** (2026-09-14): refactor(dags): rename fact_sof__tug to fact_sof__pushbarge
  - Add FACT_SOF_PUSHBARGE to MartDagID and remove FACT_SOF_TUG
  - Replace tug_vessel_dag.py with pushbarge_vessel_dag.py
  - Update fact_daily_refresh_dag, fact_transformation_dag, stream_dag,
    and ods_sof stream_dag to reference PUSHBARGE throughout
- `c4972e89` **Panji Y. Wiwaha** (2026-09-14): refactor(tasks): update vessel type references from TUG to PUSHBARGE
  - Replace ('TUG', 'BUNKER') tuple checks with ('PUSHBARGE', 'BUNKER')
    in main_task_groups, stream_task_groups, and vessel_voyage_task_groups
  - Update get_vessel_type_from_domain to return VesselType.PUSHBARGE
- `bd32e279` **Panji Y. Wiwaha** (2026-09-14): refactor(sql): replace TUG with PUSHBARGE in DDL constraints and DML templates
  - Update CHECK constraint values from 'TUG' to 'PUSHBARGE' across all
    DDL files (staging, ods, fact tables)
  - Replace vessel_type = 'TUG' filter conditions with 'PUSHBARGE' in
    all DML and quality_control SQL templates
- `96248697` **Panji Y. Wiwaha** (2026-09-14): refactor(migration): squash TUG→PUSHBARGE migrations into single PUSHBARGE blocks
  Since the branch has not been deployed to production, collapse the two-step
  migration (add TUG + rename to PUSHBARGE) into a single step that directly
  adds PUSHBARGE to the CHECK constraint. Removes the intermediate UPDATE and
  duplicate DROP/ADD CONSTRAINT blocks across all 20 affected migration files.
- `6eb98e75` **Panji Y. Wiwaha** (2026-09-14): fix(tests): update test_sof_is_completed for PUSHBARGE rename and ship.role detection
  - Replace all VesselType.TUG references with VesselType.PUSHBARGE to fix
    pytest collection failure caused by the removed TUG constant
  - Rewrite test_resolve_vessel_type and test_batch_resolve_vessel_type to
    exercise ship.role instead of the removed ship.categories detection path
  - Add missing edge cases: role key absent and role explicitly None
  - Fix batch test expected values to match VesselType instances returned
    by _resolve_vessel_type for detected PUSHBARGE/BUNKER roles

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-14)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F768%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-14)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-14)

### 🟡 Changes recommended

Existing tests reference the removed `VesselType.TUG`, causing pytest collection to fail; two documentation nits also remain.

*Get a fresh assessment by requesting another Copilot review.*

<details>
<summary>Pull request overview</summary>

This PR replaces SOF vessel type `TUG` with `PUSHBARGE`, resolves vessel types from `ship.role`, and updates pipelines, DAGs, SQL, and constraints.

**Changes:**
- Updates batch and streaming vessel classification.
- Renames and rewires PUSHBARGE fact processing.
- Updates DDL, DML, QC filters, and migrations.
</details>

<details>
<summary>File summaries</summary>

| File | Summary |
|---|---|
| `teqplay/templates/sql/quality_control/completeness/tug_event/prepare_ods_data.sql` | Updates PUSHBARGE QC filtering. |
| `teqplay/templates/sql/quality_control/completeness/terminal_visit/prepare_ods_data.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/quality_control/completeness/port_visit/prepare_ods_data.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/quality_control/completeness/encounter/prepare_ods_encounter_pilot.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/quality_control/completeness/encounter/prepare_ods_encounter_bunkering.sql` | Updates PUSHBARGE QC filtering. |
| `teqplay/templates/sql/quality_control/completeness/berth_visit/prepare_ods_data.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/quality_control/completeness/anchor_stop/prepare_ods_data.sql` | Updates PUSHBARGE QC filtering. |
| `teqplay/templates/sql/quality_control/accuracy/tug/summary_accuracy.sql` | Updates PUSHBARGE accuracy filtering. |
| `teqplay/templates/sql/quality_control/accuracy/port_visit/port_travel_duration_components.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/quality_control/accuracy/pilot/summary_accuracy.sql` | Updates PUSHBARGE accuracy filtering. |
| `teqplay/templates/sql/quality_control/accuracy/bunkering/summary_accuracy.sql` | Updates PUSHBARGE accuracy filtering. |
| `teqplay/templates/sql/migration/staging/statement_of_fact/schema_migration.sql` | Updates staging constraints. |
| `teqplay/templates/sql/migration/staging/statement_of_fact_deleted/schema_migration.sql` | Updates deleted-staging constraints. |
| `teqplay/templates/sql/migration/processing_queue/schema_migration.sql` | Updates queue constraints. |
| `teqplay/templates/sql/migration/ods/terminal_visit/schema_migration.sql` | Updates ODS constraints. |
| `teqplay/templates/sql/migration/ods/port_visit/schema_migration.sql` | Updates ODS constraints. Nit (1 vote): migration comment still says `TUG`. |
| `teqplay/templates/sql/migration/ods/berth_visit/schema_migration.sql` | Updates ODS constraints. |
| `teqplay/templates/sql/migration/fact/tug/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/terminal_visit/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/stdev_time_terminal_visit_overall/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/stdev_time_terminal_visit_monthly/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/ship_to_ship_transfers/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/port_visit/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/port_performance_analytics/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/port_calls/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/port_calls_terminal/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/pilot/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/pilot_delta/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/bunkering/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/berth_visit/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/migration/fact/anchor/schema_migration.sql` | Updates fact constraints. |
| `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql` | Updates vessel validation. |
| `teqplay/templates/sql/dml/processing_queue/sof_update_state.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/dml/processing_queue/sof_mark_stale_updates.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/dml/processing_queue/sof_mark_stale_deletes.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/dml/processing_queue/sof_fetch_pending_update.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/dml/processing_queue/sof_fetch_pending_delete.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/dml/processing_queue/sof_fetch_ods_completed.sql` | Updates vessel documentation. |
| `teqplay/templates/sql/dml/processing_queue/sof_extract_missing_metadata.sql` | Updates vessel filters. |
| `teqplay/templates/sql/dml/fact/tug/hard_delete.sql` | Updates PUSHBARGE deletion handling. |
| `teqplay/templates/sql/dml/fact/tug/delete_orphaned_visits.sql` | Updates orphan cleanup filtering. |
| `teqplay/templates/sql/dml/fact/terminal_visit/prepare_base_terminal_visit.sql` | Updates streaming vessel handling. |
| `teqplay/templates/sql/dml/fact/ship_to_ship/hard_delete.sql` | Updates PUSHBARGE deletion handling. |
| `teqplay/templates/sql/dml/fact/pilot/proceed_delta.sql` | Updates vessel filters and joins. |
| `teqplay/templates/sql/dml/fact/pilot/prepare_selected_outbound.sql` | Updates vessel classification. |
| `teqplay/templates/sql/dml/fact/pilot/prepare_selected_inbound.sql` | Updates vessel classification. |
| `teqplay/templates/sql/dml/fact/pilot/prepare_encounter_outbound.sql` | Updates vessel classification. |
| `teqplay/templates/sql/dml/fact/pilot/prepare_encounter_inbound.sql` | Updates vessel classification. |
| `teqplay/templates/sql/dml/fact/pilot/hard_delete.sql` | Updates PUSHBARGE deletion handling. |
| `teqplay/templates/sql/dml/fact/pilot/delete_orphaned_visits.sql` | Updates orphan cleanup filtering. |
| `teqplay/templates/sql/dml/fact/bunkering/hard_delete.sql` | Updates PUSHBARGE deletion handling. |
| `teqplay/templates/sql/dml/fact/bunkering/delete_orphaned_visits.sql` | Updates orphan cleanup filtering. |
| `teqplay/templates/sql/dml/fact/berth_visit/prepare_base_berth_visit.sql` | Updates streaming vessel handling. |
| `teqplay/templates/sql/dml/fact/anchor/hard_delete.sql` | Updates PUSHBARGE deletion handling. |
| `teqplay/templates/sql/dml/fact/anchor/delete_orphaned_visits.sql` | Updates orphan cleanup filtering. |
| `teqplay/templates/sql/ddl/staging/statement_of_fact.sql` | Allows PUSHBARGE in staging constraints. |
| `teqplay/templates/sql/ddl/staging/statement_of_fact_deleted.sql` | Allows PUSHBARGE in deleted-staging constraints. |
| `teqplay/templates/sql/ddl/sof_processing_queue.sql` | Allows PUSHBARGE in queue constraints. |
| `teqplay/templates/sql/ddl/ods/terminal_visit.sql` | Allows PUSHBARGE in ODS constraints. |
| `teqplay/templates/sql/ddl/ods/port_visit.sql` | Allows PUSHBARGE in ODS constraints. |
| `teqplay/templates/sql/ddl/ods/berth_visit.sql` | Allows PUSHBARGE in ODS constraints. |
| `teqplay/templates/sql/ddl/fact/tug.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/tug_delta.sql` | Allows PUSHBARGE in delta constraints. |
| `teqplay/templates/sql/ddl/fact/terminal_visit.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/stdev_time_terminal_visit_overall.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/stdev_time_terminal_visit_monthly.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/ship_to_ship_transfers.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/port_visit.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/port_performance_analytics.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/port_calls.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/port_calls_terminal.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/pilot.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/pilot_delta.sql` | Allows PUSHBARGE in delta constraints. |
| `teqplay/templates/sql/ddl/fact/bunkering.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/bunkering_delta.sql` | Allows PUSHBARGE in delta constraints. |
| `teqplay/templates/sql/ddl/fact/berth_visit.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/anchor.sql` | Allows PUSHBARGE in fact constraints. |
| `teqplay/templates/sql/ddl/fact/anchor_delta.sql` | Allows PUSHBARGE in delta constraints. |
| `teqplay/tasks/quality/completeness/vessel_voyage_task_groups.py` | Excludes PUSHBARGE from port-visit QC. |
| `teqplay/tasks/quality/common.py` | Maps QC domains to PUSHBARGE. |
| `teqplay/tasks/fact/sof/stream_task_groups.py` | Formatting-only changes. |
| `teqplay/tasks/fact/sof/main_task_groups.py` | Updates PUSHBARGE fact handling. |
| `teqplay/services/streaming/rabbitmq/sof/utils.py` | Resolves vessel type from `ship.role`. |
| `teqplay/services/streaming/rabbitmq/sof/transformators.py` | Handles portless PUSHBARGE records. |
| `teqplay/services/streaming/rabbitmq/sof/base.py` | Updates streaming classification. |
| `teqplay/services/statement_of_fact.py` | Resolves batch type from `ship.role`. |
| `teqplay/models/vessel_type.py` | Introduces PUSHBARGE. Critical (3 votes): existing tests reference `VesselType.TUG`, causing pytest collection to fail. |
| `teqplay/models/statement_of_fact.py` | Updates vessel-type documentation. |
| `teqplay/dags/warehouse/ods/ods_sof/stream_dag.py` | Rewires ODS streaming tasks. |
| `teqplay/dags/pipeline/fact_transformation_dag.py` | Wires PUSHBARGE fact processing. Nit (1 vote): comment incorrectly says port visit facts are loaded. |
| `teqplay/dags/mart/fact_sof/stream_dag.py` | Adds PUSHBARGE streaming processing. |
| `teqplay/dags/mart/fact_sof/pushbarge_vessel_dag.py` | Adds the PUSHBARGE batch DAG. |
| `teqplay/dags/mart/fact_daily_refresh_dag.py` | Adds PUSHBARGE refresh wiring. |
| `teqplay/dags/mart/__init__.py` | Adds the PUSHBARGE DAG identifier. |
</details>

<details>
<summary>Review details</summary>

### Suppressed comments (2)

**teqplay/dags/pipeline/fact_transformation_dag.py:158**
* This orchestration comment says the PUSHBARGE branch loads “port visit facts,” but `pushbarge_vessel_dag.py` intentionally omits `load_fact_port_visit` and only loads berth/terminal facts. Please correct the comment so the documented DAG behavior matches the implemented port-level exclusion.
```
    # this DAG runs unconditionally after SEA_VESSEL to load PUSHBARGE-stamped port visit facts.
```
**teqplay/templates/sql/migration/ods/port_visit/schema_migration.sql:81**
* The constraint now allows `PUSHBARGE`, but the preceding migration comment still says it accepts `TUG`. Update the comment so operators do not infer that the removed SOF vessel type remains valid.

- **Files reviewed:** 95/95 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — COMMENTED (2026-09-14)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-14)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F768%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-14)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-14)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-09-15)

LGTM

## Review Comments

### panjiyudasetya — 2026-09-14 on `teqplay/models/vessel_type.py`

resolved 6eb98e7

### Copilot — 2026-09-14 on `teqplay/models/vessel_type.py`

Removing `TUG` here breaks the existing unit-test module during import: `tests/unit/test_sof_is_completed.py` still references `VesselType.TUG` in its parametrized cases (for example, lines 33, 70, and 102), so pytest collection raises `AttributeError` before any tests run. Update those cases to `PUSHBARGE` and change the resolution fixtures from `ship.categories` to `ship.role` so the suite can execute and cover this refactor.

### panjiyudasetya — 2026-09-14 on `teqplay/models/vessel_type.py`

Resolved by 6eb98e7

### panjiyudasetya — 2026-09-14 on `teqplay/templates/sql/migration/staging/statement_of_fact/schema_migration.sql`

It is correct that the migration will abort if TUG rows exist when it runs. But that's exactly what the pre-condition script prevents. The script is the documented safety gate that must run first, and the NOT VALID clause on fact/ODS constraints is an additional layer of defense for environments where those tables have retained data but the migration needs to proceed. The PR description makes the dependency explicit, which is the right place for it.

## Comments

### panjiyudasetya — 2026-09-14

augment review

### panjiyudasetya — 2026-09-14

augment review
