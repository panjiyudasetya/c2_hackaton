---
id: confluence:1338834945
source: confluence
type: page
space: TC
title: 'Ingestion of TUG and BUNKER Vessels in SOF Pipeline: Engineering Plan'
author: Panji Y. Wiwaha
date: '2026-09-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1338834945
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1338834945
---
# Ingestion of TUG and BUNKER Vessels in SOF Pipeline: Engineering Plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1338834945  

## Content

# **Tug & Bunker Vessel SOF Ingestion - Engineering Plan**

## **1. Background**

The SOF pipeline today ingests two vessel types: `SEA_VESSEL` and `BARGE`. TUG and BUNKER vessels arrive through the same sea-vessel RabbitMQ queue. They are currently **excluded** in two places:

* `SOFService._is_tug_or_bunker_vessels()` - batching path
* `SOFRMQValidator._is_tug_or_bunker_vessels()` - streaming path

Detection is done by reading `ship.categories.values()` and checking for `'TUG'` or `'BUNKER'`. When found, the SOF is discarded.

The goal is to stop discarding them and instead ingest them with relaxed completeness rules:

| **Vessel** | **Port completeness** | **Terminal completeness** | **Berth completeness** |
| --- | --- | --- | --- |
| SEA\_VESSEL | Required | Required | Required |
| BARGE | Not checked | Not checked | Not checked |
| **TUG** (new) | Not required | Not required | Not required |
| **BUNKER** (new) | Not required | Not required | **Required** |

## **2. Open Questions - Answered**

### Q1: Should `stg_statement_of_fact.vessel_type` gain `TUG` and `BUNKER` values?

**Yes.** The `vessel_type` column already drives all downstream routing: the processing queue, ODS stream DAG, fact stream DAG, and SQL DML templates. Adding `TUG` and `BUNKER` as first-class values is the only way to apply different validation rules at each pipeline stage **without reaching into JSONB at every step**.

The alternative - keeping them tagged as `SEA_VESSEL` and reading `ship.categories` at every decision point - would scatter vessel-type logic across SQL templates, Python services, and task groups. That violates SRP and makes the pipeline harder to maintain.

### Q2: How to avoid deadlocks? Reuse `[stg|ods|fact]_sof_*` tables or create new ones?

**Reuse all existing tables.** Creating parallel table families (`stg_sof_tug_*`, `ods_sof_tug_*`, etc.) would duplicate schema, DDL, and processing logic for no benefit - the data model is identical. The `vessel_type` column already partitions rows logically.

For deadlock avoidance, the existing mitigations apply:

* Lock rows in ascending `id` order before hard deletes (already enforced by recent fixes).
* Process vessel types **sequentially** inside each stream DAG run, never concurrently. The current order is `SEA_VESSEL UPDATE → SEA_VESSEL DELETE → BARGE UPDATE → BARGE DELETE`. TUG and BUNKER are appended as `TUG UPDATE → TUG DELETE → BUNKER UPDATE → BUNKER DELETE`.
* TUG and BUNKER vessels have distinct IMOs from sea vessels and barges, so they modify different rows in `fact_berth_visit`, `fact_terminal_visit`, etc. Row-level lock contention between vessel types is therefore structural, not accidental.

## **3. Recommended Approach: Add** `TUG` **and** `BUNKER` **as New Vessel Types**

### Why this is the right design

1. **Single source of truth for vessel classification.** `vessel_type` in `stg_statement_of_fact` and `sof_processing_queue` becomes the authoritative routing key - no JSONB inspection needed downstream.
2. **Per-type validation rules.** The metadata validation SQL (`sof_validate_metadata.sql`) already branches per `vessel_type`. Adding TUG/BUNKER branches keeps validation colocated, readable, and testable.
3. **Minimal new infrastructure.** All existing tables, DAGs, and task groups are reused. The change surface is: two CHECK constraints, the `VesselType` model, the filter/validator services, the metadata SQL, and stream DAG ordering.
4. **No deadlock introduction.** Sequential processing order within each DAG run, combined with the existing ascending-ID lock ordering, is sufficient.
5. **Downstream queries remain simple.** `WHERE vessel_type = 'TUG'` is a plain equality filter on an indexed column, not a JSONB operator.

## **4. What Changes - Full Inventory**

### 4.1 Schema changes (migrations)

#### `stg_statement_of_fact.vessel_type` CHECK constraint

wide760true-- Before
CHECK (vessel\_type IN ('SEA\_VESSEL', 'BARGE'))
-- After
CHECK (vessel\_type IN ('SEA\_VESSEL', 'BARGE', 'TUG', 'BUNKER'))

File to update: `teqplay/templates/sql/ddl/staging/statement_of_fact.sql`

> The CHECK constraint change is DDL-only and non-destructive. Existing rows are unaffected. The migration is applied via `prepare_database` as a DDL operator.

#### `sof_processing_queue.vessel_type` CHECK constraint

wide760true-- Before
CHECK (vessel\_type IN ('SEA\_VESSEL', 'BARGE'))
-- After
CHECK (vessel\_type IN ('SEA\_VESSEL', 'BARGE', 'TUG', 'BUNKER'))

File to update: `teqplay/templates/sql/ddl/sof_processing_queue.sql`

#### Migration DDL

Add a migration file (e.g., `teqplay/templates/sql/ddl/migrations/`) executed once to drop and recreate the constraints on existing tables without rebuilding them:

sqlwide760true-- Drop and re-add the CHECK constraint on stg\_statement\_of\_fact
ALTER TABLE stg\_statement\_of\_fact
DROP CONSTRAINT IF EXISTS stg\_statement\_of\_fact\_vessel\_type\_check;
ALTER TABLE stg\_statement\_of\_fact
ADD CONSTRAINT stg\_statement\_of\_fact\_vessel\_type\_check
CHECK (vessel\_type IN ('SEA\_VESSEL', 'BARGE', 'TUG', 'BUNKER'));
-- Drop and re-add the CHECK constraint on sof\_processing\_queue
ALTER TABLE sof\_processing\_queue
DROP CONSTRAINT IF EXISTS sof\_processing\_queue\_vessel\_type\_check;
ALTER TABLE sof\_processing\_queue
ADD CONSTRAINT sof\_processing\_queue\_vessel\_type\_check
CHECK (vessel\_type IN ('SEA\_VESSEL', 'BARGE', 'TUG', 'BUNKER'));

Register this in `prepare_gold_tables()` (or a dedicated migration task group) inside `teqplay/tasks/prepare_db/ddl_task_groups.py`.

### 4.2 Model: `VesselType`

**File:** `teqplay/models/vessel_type.py`

Add two new enum members:

rubywide760trueclass VesselType(str, Enum):
SEA\_VESSEL = "SEA\_VESSEL"
BARGE = "BARGE"
TUG = "TUG"
BUNKER = "BUNKER"
@property
def should\_validate(self) -> bool:
return self == VesselType.SEA\_VESSEL
# --- Metadata completeness rules (consumed by sof\_validate\_metadata.sql via psycopg2 params) ---
@property
def requires\_port\_completeness(self) -> bool:
return self in (VesselType.SEA\_VESSEL,)
@property
def requires\_terminal\_completeness(self) -> bool:
return self in (VesselType.SEA\_VESSEL,)
@property
def requires\_berth\_completeness(self) -> bool:
return self in (VesselType.SEA\_VESSEL, VesselType.BUNKER)
# --- SOF-level completion rules (consumed by SOFService.\_is\_sof\_completed) ---
@property
def requires\_sof\_completion(self) -> bool:
"""Whether the SOF must have an `end` timestamp to be ingested."""
return self in (VesselType.SEA\_VESSEL, VesselType.TUG, VesselType.BUNKER)
@property
def requires\_slow\_moving\_periods(self) -> bool:
"""Whether `slowMovingPeriods` must be non-empty to be considered complete.
TUG and BUNKER vessels routinely have an empty `slowMovingPeriods` array -
`bool([])` is False, so this check must not apply to them."""
return self == VesselType.SEA\_VESSEL

These five properties are the **single source of truth** for all validation rules. Every downstream consumer - Python services, SQL templates - derives its behaviour from them. Adding a new vessel type means updating only this model.

### 4.3 Service: `SOFService` (batching path)

**File:** `teqplay/services/statement_of_fact.py`

**Remove** `_is_tug_or_bunker_vessels()` (and its call in `is_sof_valid()`).

**Add** a method that resolves the vessel type from the raw SOF JSON:

wide760true@staticmethod
def \_resolve\_vessel\_type(data: dict, default: VesselType) -> VesselType:
categories = data.get("ship", {}).get("categories", {})
values = set(categories.values())
if "TUG" in values:
return VesselType.TUG
if "BUNKER" in values:
return VesselType.BUNKER
return default

When loading SOFs in the batching path (`_process_sof_chunk`), call `_resolve_vessel_type` per record and write the resolved `vessel_type` to the staging insert payload.

`is_sof_valid()` currently checks `_is_sof_completed()` which requires both `end` **and** non-empty `slowMovingPeriods`. This is wrong for TUG and BUNKER: in Python, `bool([])` is `False`, so a TUG/BUNKER SOF with a valid `end` but an empty `slowMovingPeriods` array is incorrectly rejected.

Make `_is_sof_completed` per-vessel-type, driven by `VesselType` properties:

rubywide760truedef \_is\_sof\_completed(self, data: dict) -> bool:
has\_end = bool(data.get('end'))
if self.\_vessel\_type.requires\_slow\_moving\_periods:
return has\_end and bool(data.get('slowMovingPeriods'))
if self.\_vessel\_type.requires\_sof\_completion:
return has\_end # TUG, BUNKER: only require end
return True # BARGE: no completion check

### 4.4 Streaming consumer: `BaseSOFRMQServiceWithoutCache`

**File:** `teqplay/services/streaming/rabbitmq/sof/base.py`

The sea-vessel consumer currently discards TUG/BUNKER before writing to `stg_statement_of_fact`. Instead:

1. After receiving a message, detect the vessel type via `_resolve_vessel_type(data, default=VesselType.SEA_VESSEL)`.
2. Write the resolved `vessel_type` into the staging insert.
3. Write the correct `vessel_type` into `sof_processing_queue`.

The FULLY\_MAPPED port filter (`_filter_by_fully_mapped_status()`) should **still apply** to TUG and BUNKER. Port mapping completeness is about whether we have enough dimension data to process the visit at all, which is a prerequisite regardless of vessel type.

### 4.5 Streaming validator: `SOFRMQValidator`

**File:** `teqplay/services/streaming/rabbitmq/sof/validators.py`

Remove `_is_tug_or_bunker_vessels()` and its call. TUG/BUNKER vessels enter the pipeline normally and are routed by `vessel_type`.

### 4.6 Metadata validation SQL

**File:** `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql`

This SQL currently has two branches: `SEA_VESSEL` (strict: port + terminal + berth) and `BARGE` (no checks). Add TUG and BUNKER branches:

**Do not encode the rules in SQL.** The `VesselType` model is the single source of truth. Instead, pass boolean flags as psycopg2 parameters and let the SQL expression be purely declarative:

sqlwide760true-- Replace the hardcoded final SELECT with:
SELECT
entry\_id
, (
has\_ship
AND (NOT %(requires\_port)s::boolean OR has\_port)
AND (NOT %(requires\_terminal)s::boolean OR has\_all\_terminals)
AND (NOT %(requires\_berth)s::boolean OR has\_all\_berths)
) AS is\_valid
, has\_ship
, has\_port
, has\_all\_terminals
, has\_all\_berths
, ship\_imo
, ship\_mmsi
, port\_unlocode
FROM validation\_result;

Pass the flags from `validate_metadata()` in `SOFProcessingQueueRepository`:

wide760truevessel\_type\_enum = VesselType(vessel\_type)
params = {
'entry\_ids': entry\_ids,
'vessel\_type': vessel\_type,
'requires\_port': vessel\_type\_enum.requires\_port\_completeness,
'requires\_terminal': vessel\_type\_enum.requires\_terminal\_completeness,
'requires\_berth': vessel\_type\_enum.requires\_berth\_completeness,
}

Why not `CASE WHEN vessel_type = 'TUG' THEN ...` in the SQL? That would duplicate the validation rules into both Python and SQL. With boolean flags, adding a new vessel type means updating `VesselType` only - the SQL template stays unchanged forever.

The `has_ship` check for TUG and BUNKER uses the same IMO lookup as `SEA_VESSEL`. TUG and BUNKER vessels have IMOs, unlike barges (MMSI). The existing ELSE branch in the CASE for `has_ship` already handles this correctly via the `vessel_type = %(vessel_type)s` WHERE clause on `sof_metadata`.

### 4.7 ODS batching time filter - `NULL` safety

**Files:** `teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql`, `ods/berth_visit/stg_to_ods.sql` (and any other ODS template with this pattern)

The non-streaming WHERE clause reads:

wide760trueWHERE ((sof.start ->> 'time')::timestamp) < %(end)s
AND ((sof.end ->> 'time')::timestamp) > %(start)s

When `sof.end` is NULL, `(sof.end ->> 'time')::timestamp` evaluates to NULL, and `NULL > %(start)s` is NULL (not TRUE). The row is **silently excluded** - no error, no log.

**Current risk level:** Low. The batching API is called with `finished='true'`, which guarantees `sof.end` is always present for fetched SOFs. The streaming path bypasses this filter entirely (`entry_id = any(%(entry_ids)s)`).

**Future risk:** If the batching API call for TUG/BUNKER ever drops the `finished='true'` parameter (to capture in-progress visits), all such rows are silently lost from ODS.

**Fix - make the end predicate NULL-safe:**

wide760trueWHERE ((sof.start ->> 'time')::timestamp) < %(end)s
AND (
sof.end IS NULL
OR (sof.end ->> 'time')::timestamp > %(start)s
)

This is a purely defensive change: zero behaviour change when `sof.end` is always present, but prevents silent data loss if the assumption changes.

### 4.8 ODS task groups

**File:** `teqplay/tasks/ods/sof/base_task_groups.py`

The three ODS ingestion levels produce `ods_port_visit`, `ods_berth_visit`, `ods_terminal_visit`, etc. These are driven by the `stg_to_ods.sql` templates. No structural changes are needed here because:

* TUG: `port_visits` rows may have a `NULL` terminal join. The ODS SQL must tolerate this with `LEFT JOIN` (verify existing SQL already does this).
* BUNKER: `port_visits` rows may have a `NULL` port foreign key if the port is not in `ods_port`. The ODS insert should use `ON CONFLICT DO UPDATE` and leave `port_id` as `NULL` if the port is absent.

**Action:** Audit `teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql`, `ods/berth_visit/stg_to_ods.sql`, and `ods/terminal_visit/stg_to_ods.sql` for hard `INNER JOIN` on `ods_port` or `ods_terminal`. Any such join must become `LEFT JOIN` for TUG/BUNKER rows, or the JOIN should be conditioned on `vessel_type`.

### 4.8 Fact task groups

**File:** `teqplay/tasks/fact/sof/main_task_groups.py`

The fact loading functions `load_fact_port_visit`, `load_fact_terminal_visit`, `load_fact_berth_visit` process all vessel types by joining through ODS. Since TUG may have `NULL` port/terminal references in ODS, the fact SQL must handle NULLs gracefully.

**Grain expectations per vessel type:**

| Table | SEA\_VESSEL | BARGE | TUG | BUNKER |
| --- | --- | --- | --- | --- |
| `fact_port_visit` | Yes | Yes | Yes (port may be NULL) | Yes (port may be NULL) |
| `fact_terminal_visit` | Yes | Yes | May be absent | May be absent |
| `fact_berth_visit` | Yes | Yes | May be absent | Yes (required) |
| `fact_bunkering` | Yes | Yes | No | Yes |
| `fact_tug` | Yes | Yes | No | Yes |

**Action:** Audit the DML templates under `teqplay/templates/sql/dml/fact/` for any filter that would silently exclude TUG/BUNKER rows (e.g., `WHERE vessel_type IN ('SEA_VESSEL', 'BARGE')`). Extend those filters or remove them.

### 4.9 Stream DAG ordering

**Files:**

* `teqplay/dags/warehouse/ods/ods_sof/stream_dag.py`
* `teqplay/dags/mart/fact_sof/stream_dag.py`

Both DAGs process vessel types **sequentially** to avoid concurrent modifications to shared ODS/fact tables. Extend the chain:

wide760trueSEA\_VESSEL UPDATE
→ SEA\_VESSEL DELETE
→ BARGE UPDATE
→ BARGE DELETE
→ TUG UPDATE ← new
→ TUG DELETE ← new
→ BUNKER UPDATE ← new
→ BUNKER DELETE ← new

TUG and BUNKER are appended at the end to minimise change to existing behaviour. All downstream groups use `TriggerRule.ALL_DONE` (already the pattern) so a failure in one type does not block others.

### 4.10 Batching DAGs

Currently, batching is split into `staging_sof__sea_vessel_by_port` and `staging_sof__barge_by_port`, each calling the staging ingest service with a fixed `VesselType`.

Two options:

* **Option A:** Add `staging_sof__tug_by_port` and `staging_sof__bunker_by_port` DAGs (mirrors the sea/barge split). Clear ownership, same pattern.
* **Option B:** Extend the sea-vessel batching DAG to detect TUG/BUNKER at record level and write the correct `vessel_type`.

**Recommendation: Option A.** It follows the existing barge-vs-sea-vessel split. TUG and BUNKER vessels may come from a different API endpoint or query parameter in the future. Keeping them separate avoids coupling.

Similarly for fact batching:

* Add `fact_sof__tug` and `fact_sof__bunker` DAGs, mirroring `fact_sof__sea_vessel` and `fact_sof__barge`.

### 4.11 `fact_daily_refresh`

**File:** `teqplay/dags/mart/fact_daily_refresh_dag.py`

Currently refreshes `SEA_VESSEL` then `BARGE`. Extend to also refresh `TUG` and `BUNKER`:

wide760truerefresh\_fact\_sof(SEA\_VESSEL)
→ refresh\_fact\_sof(BARGE)
→ refresh\_fact\_sof(TUG)
→ refresh\_fact\_sof(BUNKER)

## **5. Deadlock Risk Analysis**

### Existing mitigations

* Lock rows in ascending `id` order before hard deletes (enforced by recent fixes in `fact_deletions`).
* Sequential vessel-type processing within each stream DAG run.
* `sof_processing_queue` state machine prevents a record from being processed by two concurrent runs.

### New risks introduced

**None structural.** TUG/BUNKER vessels have distinct IMOs. They modify different rows in `fact_berth_visit`, `fact_terminal_visit`, `fact_port_visit`. Lock contention between vessel types cannot occur on data rows.

The only theoretical risk is DDL-level: if the migration to alter the CHECK constraint runs while stream DAGs are inserting. Mitigate by:

1. Pause the streaming consumer DAGs (`staging_sof__sea_vessel_stream`, `staging_sof__barge_stream`) during Phase 1 migration.
2. Run `prepare_database`.
3. Resume streaming consumers.

This is a brief maintenance window (~minutes) and is already the standard procedure for `prepare_database` deployments.

## **6. Key Files Summary**

| **Layer** | **File** | **Change** |
| --- | --- | --- |
| Model | `teqplay/models/vessel_type.py` | Add TUG, BUNKER; add three `requires_*` properties |
| DDL | `teqplay/templates/sql/ddl/staging/` `statement_of_fact.sql` | Extend CHECK constraint |
| DDL | `teqplay/templates/sql/ddl/` `sof_processing_queue.sql` | Extend CHECK constraint |
| DDL | new migration file | ALTER TABLE to drop/recreate constraints |
| Prepare DB | `teqplay/tasks/prepare_db/ddl_task_groups.py` | Register migration DDL operator |
| Service | `teqplay/services/statement_of_fact.py` | Remove TUG/BUNKER filter; add `_resolve_vessel_type`; make `_is_sof_completed` per-vessel-type |
| Streaming | `teqplay/services/streaming/rabbitmq/sof/` `base.py` | Call `_resolve_vessel_type`; write correct `vessel_type` |
| Streaming | `teqplay/services/streaming/rabbitmq/sof/` `validators.py` | Remove `_is_tug_or_bunker_vessels` |
| SQL | `teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql` | Replace hardcoded `is_valid` with boolean flag params (`requires_port`, `requires_terminal`, `requires_berth`) |
| ODS SQL | `teqplay/templates/sql/dml/ods/port_visit/` `stg_to_ods.sql` (+ berth\_visit) | Make `sof.end` predicate NULL-safe; audit for hard INNER JOINs |
| Fact SQL | `teqplay/templates/sql/dml/fact/*.sql` | Audit vessel\_type filters |
| DAG | `teqplay/dags/warehouse/ods/ods_sof/` `stream_dag.py` | Add TUG, BUNKER sequential steps |
| DAG | `teqplay/dags/mart/fact_sof/stream_dag.py` | Add TUG, BUNKER sequential steps |
| DAG | `teqplay/dags/mart/fact_daily_refresh_dag.py` | Add TUG, BUNKER refresh steps |
| DAG (new) | `teqplay/dags/warehouse/staging/staging_sof/tug_by_port_dag.py` | TUG batching ingest |
| DAG (new) | `teqplay/dags/warehouse/staging/staging_sof/bunker_by_port_dag.py` | BUNKER batching ingest |
| DAG (new) | `teqplay/dags/mart/fact_sof/` `tug_vessel_dag.py` | TUG fact batching |
| DAG (new) | `teqplay/dags/mart/fact_sof/` `bunker_vessel_dag.py` | BUNKER fact batching |

---

## **7. Delivery Plan**

Each delivery is a self-contained unit (one PR) that leaves Airflow in a valid, working state. SEA\_VESSEL and BARGE processing must be unaffected at the end of every delivery. Dependencies are explicit - do not begin a delivery until its prerequisite is merged and deployed.

### **Delivery 1 - Schema foundation & defensive fixes**

**Prerequisite:** None  
**Deployment window:** Brief streaming pause required for `prepare_database` (same procedure as any DDL migration).  
**Airflow state after deploy:** Identical to before. TUG/BUNKER are still filtered out. New schema is ready but dormant.

### Tasks

**Model**

389
689ac385-f1a7-4f94-adff-0ff502b03ee2
incomplete
`teqplay/models/vessel_type.py` - Add `TUG` and `BUNKER` enum members. Add all five properties: `requires_port_completeness`, `requires_terminal_completeness`, `requires_berth_completeness`, `requires_sof_completion`, `requires_slow_moving_periods`.

**DDL**

390
f4e82ce9-d36f-482d-8eec-a07cf268391b
incomplete
`teqplay/templates/sql/ddl/staging/statement_of_fact.sql` - Extend `vessel_type` CHECK constraint to include `'TUG'` and `'BUNKER'`.

391
2c37b1f9-ddad-40ed-a172-b8d11e134d81
incomplete
`teqplay/templates/sql/ddl/sof_processing_queue.sql` - Same constraint extension.

392
24eae696-af34-4af0-ae8e-d041cb0a2a9a
incomplete
New migration file (e.g. `teqplay/templates/sql/ddl/migrations/add_tug_bunker_vessel_types.sql`) - `ALTER TABLE … DROP CONSTRAINT … ADD CONSTRAINT` for both tables.

393
1a2e31f7-1cf0-41ea-8be3-3149a5a01b0b
incomplete
`teqplay/tasks/prepare_db/ddl_task_groups.py` - Register the migration as a `SQLExecuteQueryOperator`.

**Defensive fixes (zero behaviour change for existing vessel types)**

394
98ca14d6-6cb6-4857-8d1e-e5362e65fab3
incomplete
`teqplay/services/statement_of_fact.py` - Make `_is_sof_completed` per-vessel-type using `requires_sof_completion` and `requires_slow_moving_periods`.

* + For SEA\_VESSEL: behaviour unchanged (requires both `end` and non-empty `slowMovingPeriods`).
  + For BARGE: behaviour unchanged (no check). TUG/BUNKER paths are newly reachable but have no effect until Delivery 3.

395
35b0055b-0f94-4c5e-a2ee-7f34df401ce6
incomplete
`teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql` - Wrap the `sof.end` time predicate in `(sof.end IS NULL OR ...)`. Zero behaviour change while all ingested SOFs have `end` present.

396
a8100807-b55a-45db-9912-e43615fb08a3
incomplete
`teqplay/templates/sql/dml/ods/berth_visit/stg_to_ods.sql` - Same NULL-safe end predicate.

397
990b9e73-58e3-46d2-9114-d4b8a17e25cd
incomplete
Any other ODS DML template that applies the same `(sof.end ->> 'time')::timestamp > %(start)s` pattern - apply the same fix.

#### Why these are grouped

Schema migrations and defensive fixes share a deployment window and are all zero-behaviour-change. There is no reason to open a separate PR for each.

---

### **Delivery 2 - Pipeline readiness (SQL + DAG prep)**

**Prerequisite:** Delivery 1 merged and deployed.  
**Deployment window:** Hot deploy - no streaming pause needed.  
**Airflow state after deploy:** `ods_sof__stream` and `fact_sof__stream` have new TUG/BUNKER task groups. They run every cycle but immediately exit with zero records - no records exist in the queue yet. SEA\_VESSEL and BARGE processing unchanged.

> **Critical ordering constraint within this delivery:** The `sof_validate_metadata.sql` change (boolean flag params) and the `validate_metadata()` Python-side update (passing those params) **must ship together**. If either side ships without the other, every call to `validate_metadata()` will raise a psycopg2 `KeyError` on the missing `%(requires_port)s` parameter. This is the only tight coupling in this delivery.

### Tasks

**Metadata validation SQL + Python (ship together)**

398
9573f6cb-4605-41b9-a185-2792c60254eb
incomplete
`teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql` - Replace the hardcoded `(has_ship AND has_port AND has_all_terminals AND has_all_berths) AS is_valid` with the boolean-flag expression: `(has_ship AND (NOT %(requires_port)s::boolean OR has_port) AND ...)`.

399
be42f1a8-9066-441f-81c9-20b301e3aa58
incomplete
`teqplay/repositories/statement_of_fact.py` - `validate_metadata()`: derive `requires_port`, `requires_terminal`, `requires_berth` from `VesselType(vessel_type)` properties and add them to the `params` dict.

**ODS DML templates - JOIN audit**

400
2c7ff8cb-9aa0-4fa7-b351-87e41ccbfb3f
incomplete
`teqplay/templates/sql/dml/ods/port_visit/stg_to_ods.sql` - Confirm the `ods_port` join is `LEFT JOIN` (it is, per the current file). Confirm `ods_port_visit.port_id` column is nullable. If `NOT NULL`, raise as a blocker before Delivery 3.

401
efd3237c-7bee-4730-917f-b84a2353d0ca
incomplete
`teqplay/templates/sql/dml/ods/terminal_visit/stg_to_ods.sql` - Audit `ods_terminal` join. Must be `LEFT JOIN`.

402
a6e151dd-0f6d-4ec9-8aeb-86564934b0d8
incomplete
`teqplay/templates/sql/dml/ods/berth_visit/stg_to_ods.sql` - Audit `ods_port_visit` join in the `berth_visit` CTE (line 112: `port_visit_id IN (SELECT opv.visit_id FROM ods_port_visit AS opv)`). This is a subquery gate, not a JOIN - it is fine because TUG/BUNKER will have `ods_port_visit` rows even with a NULL `port_id`.

**Fact DML templates - vessel\_type filter audit**

403
4d05e039-7d3c-4cd9-aa7e-a8d6d13f13fd
incomplete
Grep all files under `teqplay/templates/sql/dml/fact/` for `vessel_type IN ('SEA_VESSEL', 'BARGE')` or equivalent hard-coded lists. Extend each match to include `'TUG'` and `'BUNKER'`, or remove the filter if vessel type is not a meaningful discriminator there.

**Stream DAG extensions**

404
1c20ea49-4aa4-4583-af1a-9ef09f120911
incomplete
`teqplay/dags/warehouse/ods/ods_sof/stream_dag.py` - Append TUG UPDATE → TUG DELETE → BUNKER UPDATE → BUNKER DELETE task groups after BARGE DELETE. Use `TriggerRule.ALL_DONE` (existing pattern).

405
9e3bdf8c-e26d-4ffb-8c9d-137a0adca3ce
incomplete
`teqplay/dags/mart/fact_sof/stream_dag.py` - Same extension.

#### Why these are grouped

All changes in this delivery produce no observable data change - they are either SQL structural changes that produce identical results for existing data, or DAG extensions whose new task groups are immediately no-ops. Batching them in one PR reduces review overhead and avoids a gap where the DAGs are extended but the SQL is not yet updated (which would be fine, but is unnecessary churn).

---

### Delivery 3 - Streaming path activation

**Prerequisite:** Deliveries 1 and 2 merged and deployed.  
**Deployment window:** Pause `staging_sof__sea_vessel_stream` → deploy → resume. (The streaming consumer is the only change here. Pausing it for the deploy prevents a window where TUG/BUNKER messages are written to staging with the old `vessel_type='SEA_VESSEL'` label.)  
**Airflow state after deploy:** TUG/BUNKER SOFs arriving via RabbitMQ are now ingested, routed through ODS, and promoted to facts via the streaming path. First live data for these vessel types.

### Tasks

406
86709dae-bba3-4376-a066-04ee9ee5391a
incomplete
`teqplay/services/streaming/rabbitmq/sof/base.py` - Add `_resolve_vessel_type(data, default)` (reads `ship.categories`). Call it after message deserialization. Write the resolved `vessel_type` to the staging insert payload and to `sof_processing_queue`.

407
b74581ed-2cd9-4857-a0e2-d852e7e50980
incomplete
`teqplay/services/streaming/rabbitmq/sof/validators.py` - Remove `_is_tug_or_bunker_vessels()` and its call site. Remove from `SOFRMQValidator.validate()`.

408
af5cf47d-0d00-4c8f-a657-2d1d047936fa
incomplete
`teqplay/services/streaming/rabbitmq/sof/base.py` - Remove `_is_tug_or_bunker_vessels()` from `BaseSOFRMQServiceWithoutCache` (if it also lives here independently of the validator).

#### Why these are grouped - and kept separate from Delivery 2

This delivery is the "open valve." It has a meaningful blast radius: from this point, new vessel types flow into production tables. Keeping it isolated from Delivery 2 means a failed Delivery 3 deploy can be rolled back cleanly without touching any SQL or DAG code. It also means QA can explicitly sign off on Delivery 2 (pipeline readiness) before the valve is opened.

#### Post-deploy verification checklist

* Confirm new TUG rows appear in `stg_statement_of_fact` with `vessel_type = 'TUG'`.
* Confirm new BUNKER rows appear with `vessel_type = 'BUNKER'`.
* Confirm `sof_processing_queue` picks them up as PENDING.
* Confirm `ods_sof__stream` processes them to ODS\_PROCESSING\_COMPLETED.
* Confirm `fact_sof__stream` promotes them to FACTS\_PROCESSING\_COMPLETED.
* Confirm `fact_berth_visit` rows exist for BUNKER entries.
* Confirm SEA\_VESSEL and BARGE row counts in ODS/fact tables are unaffected.

---

### Delivery 4 - Batching path

**Prerequisite:** Delivery 3 merged and deployed (ODS/fact templates already handle TUG/BUNKER; streaming data provides a baseline for QC comparison).  
**Deployment window:** Hot deploy - new DAGs are additive only. No existing DAG is modified.  
**Airflow state after deploy:** Historical TUG/BUNKER SOFs can be backfilled. `fact_daily_refresh` now covers all four vessel types.

### Tasks

**SOFService (batching)**

409
a04c83b6-bfb8-461c-9a3c-f46a9c05baec
incomplete
`teqplay/services/statement_of_fact.py` - Add `_resolve_vessel_type(data, default)` (same logic as the streaming version, shared or duplicated depending on the service boundary). Remove `_is_tug_or_bunker_vessels()` from `_clean_sofs()` / `_process_sof_chunk()`.

**New DAGs**

410
175c3964-8864-4a6e-935a-b5287b93950f
incomplete
`teqplay/dags/warehouse/staging/staging_sof/tug_by_port_dag.py` - Mirror `staging_sof__barge_by_port` with `vessel_type=VesselType.TUG`.

411
b0fdf904-7486-4de2-ac18-306afeab5f3b
incomplete
`teqplay/dags/warehouse/staging/staging_sof/bunker_by_port_dag.py` - Mirror with `vessel_type=VesselType.BUNKER`.

412
bcb2e00f-4b9b-42b7-a794-0a67c4a4c8bb
incomplete
`teqplay/dags/mart/fact_sof/tug_vessel_dag.py` - Mirror `fact_sof__barge` with `vessel_type=VesselType.TUG`.

413
c4c9769a-e9fd-409e-8efe-e4c000e7b4f8
incomplete
`teqplay/dags/mart/fact_sof/bunker_vessel_dag.py` - Mirror with `vessel_type=VesselType.BUNKER`.

**Fact daily refresh extension**

414
ebbff4f4-c4f6-4cd1-8954-500b8898eba9
incomplete
`teqplay/dags/mart/fact_daily_refresh_dag.py` - Append `refresh_fact_sof(TUG)` → `refresh_fact_sof(BUNKER)` to the existing chain.

#### Why these are grouped

All changes are purely additive (new DAGs) or isolated to the batching service path. Nothing here can affect the streaming path or the existing `SEA_VESSEL`/`BARGE` batching DAGs.

---

### Delivery 5 - QC & downstream audit

**Prerequisite:** Delivery 3 merged and deployed (streaming data present for at least one full day).  
**Deployment window:** Hot deploy.  
**Airflow state after deploy:** Quality checks run alongside live ingestion. KPI DML is hardened against NULL `port_id`/`terminal_id` from TUG visits.

### Tasks

**QC checks**

415
a07b8530-f14e-4987-8477-b0073e6d1b62
incomplete
Add `qc_negative_tug` and `qc_event_centric_tug` task groups mirroring the existing QC pattern.

416
eb17d06c-534e-43f6-990d-649cfbd13385
incomplete
Add `qc_negative_bunker` and `qc_event_centric_bunker` task groups.

417
44e26aff-c275-4882-9475-0fabe0e03685
incomplete
Verify `fact_berth_visit` count matches TUG/BUNKER ODS berth visit count (1:1 expected for BUNKER; ≥0 for TUG).

418
581f79e1-efee-4349-b910-eaf8579a2b89
incomplete
Verify `fact_bunkering` rows exist for BUNKER entries with berth-level data.

**KPI DML audit**

419
275ca8de-265b-442e-80e7-833503d34c9f
incomplete
Grep all Gold/Silver DML templates for JOINs or filters on `fact_port_visit` or `fact_terminal_visit` that assume non-NULL `port_id` or `terminal_id`. Wrap such references in `WHERE x.port_id IS NOT NULL` guards where TUG/BUNKER rows should not contribute to the KPI.

420
799b18e9-45bb-4916-87c4-aeddbcb1aa7a
incomplete
Verify `gold.kpi_*` row counts are unaffected by the introduction of TUG/BUNKER data.

---

## 8. Open Items (must resolve before Delivery 3)

1. `ods_port_visit.port_id` **nullability** - The `port_visit/stg_to_ods.sql` uses a `LEFT JOIN ods_port`, so a NULL `port_id` is structurally possible. Confirm the DDL for `ods_port_visit` allows `port_id` to be NULL. If the column has a `NOT NULL` constraint, add a DDL migration to drop it as part of Delivery 1.
2. `ods_berth_visit` **subquery gate** - Line 112 of `berth_visit/stg_to_ods.sql` gates on `port_visit_id IN (SELECT opv.visit_id FROM ods_port_visit …)`. This requires the `ods_port_visit` row to already exist before berth visits are written (ODS Level 2 runs after Level 1 - this is correct by design). Confirm the ODS level ordering holds for TUG/BUNKER by checking `base_task_groups.py`.
3. **TUG/BUNKER RabbitMQ queue** - Assumed to be the same sea-vessel queue as SEA\_VESSEL. If they ever receive a dedicated queue, a separate streaming consumer DAG (mirroring `staging_sof__barge_stream`) is the right addition - no change to SQL or ODS/fact task groups.
4. `slowMovingPeriods` **content for TUG/BUNKER** - Assumed to be an empty array `[]` rather than absent (null). If the API omits the key entirely (`data.get('slowMovingPeriods')` returns `None`), the existing `bool(None)` = `False` behaviour already rejects the record - same root cause, same fix (the `requires_slow_moving_periods` guard in Delivery 1 handles both cases).
5. **Downstream KPI DML** - Gold/Silver KPI queries that JOIN or filter on `fact_port_visit.port_id IS NOT NULL` or `fact_terminal_visit` implicitly assume all rows have dimension keys. Audit these before Delivery 5 to confirm TUG rows (which may have NULL `port_id`) do not silently corrupt KPI aggregations.