---
id: confluence:1323204609
source: confluence
type: page
space: TC
title: Bunkering Encounter Ingestion Plan
author: Panji Y. Wiwaha
date: '2026-08-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1323204609
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1323204609
---
# Bunkering Encounter Ingestion Plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1323204609  

## Content

# **Bunkering Encounter Ingestion Plan**

## **1. Context and Objective**

### **Current State**

`fact_bunkering` is currently populated by three distinct write paths:

* **Path A - Batch SOF**  
  The Sea Vessel and Barge SOF DAGs performed DELETE then chunked direct upserts into `fact_bunkering` without using a delta-table strategy.
* **Path B - Streaming Delete SOF**  
  The stream DAG performs a hard DELETE on `fact_bunkering` without using a delta-table strategy.
* **Path C - Operational Events**  
  The operational events DAG uses a delta-table strategy via `fact_bunkering_delta`. It performs a DELETE followed by an INSERT from the delta.

### **Problem**

SOF is the only data source feeding all three paths. If SOF data is absent, delayed, or incomplete for a visit, no bunkering row is produced even when the encounter physically occurred.

### **Objective**

Introduce an independent ingestion path that populates `fact_bunkering` without any SOF dependency. Two candidate routes are evaluated below. **Pick one.**

## **2. Concurrency Risks in the Current Architecture**

Before adding a new ingestion path, the existing concurrency risks must be understood. All three current paths write to the same `fact_bunkering` table with no coordination between them.

### **Risk 1 - Path A vs Path C (Concurrent** `DELETE` **and** `INSERT` **on the same rows)**

Path A issues:

sqlwide760trueDELETE FROM fact\_bunkering WHERE vessel\_type = '...' AND visit\_id IN (...)

followed immediately by a chunked direct UPSERT.

Path C issues:

sqlwide760trueDELETE FROM fact\_bunkering WHERE visit\_id IN (SELECT DISTINCT visit\_id FROM fact\_bunkering\_delta)

followed by an INSERT from the delta table.

Path A is triggered on-demand (manually or via SOF ingestion). Path C runs every 15 minutes. If they both target the same `visit_id` set at the same time, PostgreSQL row-level locks will cause one to block behind the other. If the lock acquisition order differs across the two DELETE and INSERT steps, a deadlock is possible.

### **Risk 2 - Path B vs Path A or C (Hard** `DELETE` **racing an active** `INSERT`**)**

Path B issues a `DELETE FROM fact_bunkering WHERE visit_id = any(...)` for SOF deletion events. This can run at any time and can remove rows that Path A or Path C just inserted for the same `visit_id`.

### **Risk 3 - Shared** `fact_bunkering_delta` **with** `TRUNCATE`

Path C uses a single shared `fact_bunkering_delta` table and terminates with `TRUNCATE TABLE fact_bunkering_delta`. If `fact_operational_events_dag.py` runs two concurrent instances (i.e. `max_active_runs` is not set to 1), the TRUNCATE from one run clears data written by the other. This must be verified.

### **Best Practice Recommendation**

**Make** `fact_operational_events_dag.py` **the single writer to** `fact_bunkering` **for all new ingestion.**

Path A and Path B writing directly to `fact_bunkering` is a pre-existing risk outside the scope of this plan. However, **any new ingestion route introduced by this plan must not add a fourth direct writer**. Instead, all new routes must feed the queue so that Path C remains the exclusive writer for new bunkering data. This eliminates concurrency risk for the new data at the cost of a small latency increase (bounded by the 15-minute Path C interval).

## **3. Data Sources**

### **Source A - REST API**

wide760trueGET {vessel\_voyage\_url}/encounter/byImo/{imo}?type=BUNKER&start=...&end=...

Example response:

jsonwide760true{
"shipId": "e921256e-d351-4b4f-9647-42fb41e0caad",
"name": "ZITA SCHULTE",
"mmsi": 235116958,
"imo": 9694385,
"encounters": [
{
"id": "0d72a1b0-6465-4d5b-941e-4de06978d993.VISIT:884cfaf7-97f8-41d5-a298-013cd45f4f11",
"shipId": "e33fa7fd-2444-4584-b6eb-9b2b1e8c999b",
"mmsi": 373373000,
"imo": 9319961,
"name": "EAGLE NAVIGATOR",
"portUnlocode": "PACTB",
"start": {
"location": { "lat": 9.368523, "lon": -79.934823 },
"time": "2024-07-01T09:19:40Z"
},
"end": {
"location": { "lat": 9.368275, "lon": -79.934421 },
"time": "2024-07-01T16:31:58Z"
}
}
]
}

Key characteristics:

* Query target is the **cargo vessel IMO**
* Encounter ID format: `{encounter_uuid}.VISIT:{visit_uuid}` - visit ID is directly embedded
* `portUnlocode` is present in the response
* The encounter object describes the **service (bunker) vessel**

### **Source B - Streaming**

| **Key Config** | **Value** |
| --- | --- |
| Queue name | `ServiceVesselComponent-events-queue` |
| Host name | `rabbitmq.dev.teqplay.dev` |
| Vhost | `ServiceVesselComponentDev` |

Example payload:

jsonwide760true{
"encounterId": "5f148a99-c55d-483f-b7be-644d712e4320",
"serviceVessel": {
"imo": "9692923",
"mmsi": "563025420",
"vesselId": "5f7c1480-...",
"vesselRole": "BUNKER"
},
"relatedVessel": {
"imo": "1012713",
"mmsi": "319080700",
"vesselId": "88793467-...",
"vesselRole": null
},
"startTime": "2025-07-18T07:39:53.235",
"endTime": "2025-07-18T10:35:43.000",
"startLocation": {
"lat": 1.238448,
"lon": 103.815091
},
"endLocation": {
"lat": 1.237913,
"lon": 103.814403
},
"visitRef": "ab37901f-f1ae-4790-8b50-b6f4ec9792f8.VISIT"
}

Key characteristics:

* Bunker vessel identified by `vesselRole = 'BUNKER'` in the service vessel JSON
* Encounter ID is a **plain UUID** with no embedded visit reference
* Visit ID is in `visitRef` as `{visit_uuid}.VISIT` - the UUID before `.VISIT` is the port visit ID
* `portUnlocode` is **not available** in the payload; it must be resolved from `ods_port_visit`

## **4. Route A - API On-Demand (Manually Triggered)**

### **4.1 Why Automatic Scheduling Is Not Viable**

The total tracked fleet is **291,571 ships**. The encounter endpoint is only queryable per ship by IMO, MMSI, or ship ID. There is no endpoint that returns all bunkering encounters within a time range across the full fleet in one call.

Even scoping the query to ships with an active port visit does not fully solve the problem. The number of concurrently active port visits across a global fleet can still be very large, and the exact scale is unknown without measuring it first. Scheduling this automatically therefore carries a real risk of:

* Saturating the API beyond its rate limits
* DAG runs overlapping when the previous cycle has not finished
* Unpredictable execution time per cycle depending on fleet activity

**Conclusion:** Route A cannot be operated as an automatic scheduled pipeline. It is instead a manually triggered on-demand DAG. The operator provides explicit inputs: one or more ship IMOs, a start time, and an end time. This makes the scope fully predictable and eliminates all scheduling risk.

### **4.2 Transaction Safety**

Route A does **not** write directly to `fact_bunkering`. It writes to `stg_bunker_encounter`, transforms to `ods_encounter`, then enqueues `visit_id`s to `vessel_operational_queue`. Path C (`fact_operational_events_dag.py`) handles the final write. This design adds no new concurrency risk on `fact_bunkering`.

### **4.3 Architecture**

### **4.4 DAG** `staging_bunker_encounter_api`

**Trigger:** manual only. No schedule.

**Required Airflow Params:**

| **Param** | **Type** | **Description** |
| --- | --- | --- |
| `imo` | `str` | Vargo vessel IMOs to query |
| `start_time` | `str` | ISO 8601 start of the encounter window |
| `end_time` | `str` | ISO 8601 end of the encounter window |

### **4.5 Staging Table** `stg_bunker_encounter`

sqlwide760trueCREATE TABLE IF NOT EXISTS stg\_bunker\_encounter (
id VARCHAR(255) NOT NULL,
visit\_id VARCHAR(255) NOT NULL,
service\_ship\_id VARCHAR(255),
service\_ship\_imo VARCHAR(50),
service\_ship\_mmsi VARCHAR(50),
cargo\_ship\_id VARCHAR(255),
cargo\_ship\_imo VARCHAR(50),
cargo\_ship\_mmsi VARCHAR(50),
port\_unlocode VARCHAR(20),
start\_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
start\_lat DOUBLE PRECISION,
start\_lon DOUBLE PRECISION,
end\_timestamp TIMESTAMP WITH TIME ZONE,
end\_lat DOUBLE PRECISION,
end\_lon DOUBLE PRECISION,
ingested\_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
PRIMARY KEY (id)
);

### **4.6 Visit ID Extraction**

The encounter ID embeds the visit ID directly:

rubywide760truedef extract\_visit\_id(encounter\_id: str) -> str:
# encounter\_id format: {uuid}.VISIT:{visit\_uuid}
return encounter\_id.split(".VISIT:")[1]

### **4.7 Column Mapping: API Response to** `stg_bunker_encounter`

| **Staging column** | **API source** |
| --- | --- |
| `id` | `encounter.id` |
| `visit_id` | Extracted from `encounter.id` suffix |
| `service_ship_id` | `encounter.shipId` |
| `service_ship_imo` | `encounter.imo` |
| `service_ship_mmsi` | `encounter.mmsi` |
| `cargo_ship_id` | Response root `shipId` |
| `cargo_ship_imo` | Response root `imo` |
| `cargo_ship_mmsi` | Response root `mmsi` |
| `port_unlocode` | `encounter.portUnlocode` |
| `start_timestamp` | `encounter.start.time` |
| `start_lat / start_lon` | `encounter.start.location` |
| `end_timestamp` | `encounter.end.time` |
| `end_lat / end_lon` | `encounter.end.location` |

### **4.8 Service Class** `BunkerEncounterExtractor`

Extends the existing `DataExtractor` base class. In test mode (`is_testing_mode()`), returns fixture data. Handles per-ship API calls and maps the response to staging row dicts.

### **4.9 New Components**

| **Component** | **Type** | **Notes** |
| --- | --- | --- |
| `stg_bunker_encounter` | Table | Raw API response per encounter |
| `BunkerEncounterExtractor` | Service class | Extends `DataExtractor` |
| `staging_bunker_encounter_api` | DAG | Manually triggered; requires `imo`, `start_time`, `end_time` |

Existing components unchanged: `ods_encounter`, `vessel_operational_queue`, `fact_operational_events_dag.py`.

### **4.10 Pros and Cons**

| **Pros** | **Cons** |
| --- | --- |
| No direct writes to `fact_bunkering`; zero additional concurrency risk | Not automated; requires manual triggering per ship and time range |
| Fully predictable scope; operator controls exactly which ships and window to query | Not suitable as a standalone continuous ingestion pipeline |
| Visit ID embedded in encounter ID; no join or timestamp overlap needed | API rate limits still apply; large `imo` inputs must be sized carefully |
| Idempotent; UPSERT on encounter ID, safe to rerun for the same inputs | Coverage gaps between manual runs are the operator's responsibility |
| Simple implementation; no watermark, no scheduler, no active-ship discovery logic |  |

## **5. Route B: Streaming**

### **5.1 Transaction Safety**

Route B does **not** write directly to `fact_bunkering`. It writes to `staging.bunker_encounter_stream`, transforms to `ods_encounter`, then enqueues `visit_id`s to a dedicated `bunker_encounter_queue`. Path C (`fact_operational_events_dag.py`) is extended to poll this queue and handles the final write. This design adds no new concurrency risk on `fact_bunkering`.

### **5.2 Architecture**

### **5.3 DAG** `staging_bunker_encounter_stream`

**Schedule:** every 5 minutes.

Rows where `visit_id` has no match in `ods_port_visit` are written to staging with `port_unlocode = NULL` and held until the port visit is ingested. The transform step guards with `WHERE visit_id IN (SELECT visit_id FROM ods_port_visit)` before writing to `ods_encounter`.

### 4.3 Staging Table: `stg_bunker_encounter_stream`

sqlwide760trueCREATE TABLE IF NOT EXISTS stg\_bunker\_encounter\_stream (
id VARCHAR(255) NOT NULL,
visit\_id VARCHAR(255) NOT NULL,
service\_ship\_id VARCHAR(255),
service\_ship\_imo VARCHAR(50),
service\_ship\_mmsi VARCHAR(50),
cargo\_ship\_id VARCHAR(255),
cargo\_ship\_imo VARCHAR(50),
cargo\_ship\_mmsi VARCHAR(50),
port\_unlocode VARCHAR(20),
start\_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
start\_lat DOUBLE PRECISION,
start\_lon DOUBLE PRECISION,
end\_timestamp TIMESTAMP WITH TIME ZONE,
end\_lat DOUBLE PRECISION,
end\_lon DOUBLE PRECISION,
processed BOOLEAN NOT NULL DEFAULT false,
ingested\_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
PRIMARY KEY (id)
);

The `processed` flag marks rows that have been successfully written to `ods_encounter` and enqueued.

### **5.5 Visit ID Extraction**

rubywide760truedef extract\_visit\_id(visit\_ref: str) -> str:
# visitRef format: {visit\_uuid}.VISIT
return visit\_ref.replace(".VISIT", "")

### **5.6 Column Mapping: Streaming Payload to** `stg_bunker_encounter_stream`

| **Staging column** | **Streaming source** |
| --- | --- |
| `id` | `encounterId` (plain UUID) |
| `visit_id` | Extracted from `visitRef` |
| `service_ship_id` | `serviceVessel.vesselId` |
| `service_ship_imo` | `serviceVessel.imo` |
| `service_ship_mmsi` | `serviceVessel.mmsi` |
| `cargo_ship_id` | `relatedVessel.vesselId` |
| `cargo_ship_imo` | `relatedVessel.imo` |
| `cargo_ship_mmsi` | `relatedVessel.mmsi` |
| `port_unlocode` | Resolved from `ods_port_visit` via `visit_id` |
| `start_timestamp` | `startTime` |
| `start_lat / start_lon` | `startLocation.lat / lon` |
| `end_timestamp` | `endTime` |
| `end_lat / end_lon` | `endLocation.lat / lon` |

### **5.7 Queue Table** `bunker_encounter_queue`

sqlwide760trueCREATE TABLE IF NOT EXISTS bunker\_encounter\_queue (
id VARCHAR(255) NOT NULL,
encounter\_id VARCHAR(255) NOT NULL,
visit\_id VARCHAR(255) NOT NULL,
state VARCHAR(20) NOT NULL DEFAULT 'PENDING',
retry\_count INTEGER NOT NULL DEFAULT 0,
created\_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
updated\_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
PRIMARY KEY (id)
);
CREATE INDEX IF NOT EXISTS idx\_bunker\_queue\_state
ON bunker\_encounter\_queue (state);

Idempotency key: `md5(encounter_id)`. Re-enqueuing an existing visit resets it to `PENDING` so updates are reprocessed, consistent with the SOF streaming pattern.

### 4.7 Queue State Machine

A failure callback on `fact_operational_events_dag.py` rolls all `PROCESSING` rows back to `PENDING` and increments `retry_count`. Rows that exceed `max_retries` (recommended: 3) move to `FAILED` and are excluded from polling until manually reset.

### 5.9 Fact Loading `fact_operational_events_dag.py`

`operational_events_dag.py` runs every 15 minutes with the task chain:

wide760truestart -> fact\_tug -> fact\_pilot -> fact\_anchor -> fact\_bunkering -> monitoring
-> end

The `fact_bunkering` task group (`run_fact_bunkering_processing` in `bunkering_task_groups.py`) is extended to also poll `bunker_encounter_queue` alongside `vessel_operational_queue`. The existing delta pattern is unchanged.

### **5.10 Service Class** `BunkerEncounterStreamConsumer`

Key responsibilities:

* Read unprocessed rows from the streaming source where `serviceVessel.vesselRole = 'BUNKER'` and `processed = false`
* Extract `visit_id` from `visitRef`
* Resolve `port_unlocode` via `ods_port_visit`
* Map to `staging.bunker_encounter_stream` schema
* Mark source rows as processed after successful staging write

### **5.11 New Components**

| **Component** | **Type** | **Notes** |
| --- | --- | --- |
| `stg_bunker_encounter_stream` | Table | Raw streaming payload per encounter |
| `bunker_encounter_queue` | Table | Queue with state machine, same pattern as SOF |
| `BunkerEncounterStreamConsumer` | Service class | Reads streaming source, maps to staging schema |
| `staging_bunker_encounter_stream` | DAG | Short-interval streaming consumer |

Existing components with minor extension: `ods_encounter` (new rows added), `fact_operational_events_dag.py` (extended to poll `bunker_encounter_queue` within `run_fact_bunkering_processing`).

### **5.12 Pros and Cons**

| **Pros** | **Cons** |
| --- | --- |
| No direct writes to `fact_bunkering`; zero additional concurrency risk | Completeness bounded by streaming source coverage; vessels not in the stream are silently absent |
| Near real-time latency (minutes) | `portUnlocode` requires a join to `ods_port_visit`, introducing a timing dependency |
| Queue pattern provides exactly-once processing and safe retry | No native backfill; historical data requires a separate mechanism |
| Consistent with the existing SOF streaming and queue pattern | Adds operational surface area: streaming DAG health, queue state, and failure callbacks all need monitoring |

## **6. Route Comparison**

| **Factor** | **Route A: API On-Demand** | **Route B: Streaming** |
| --- | --- | --- |
| Direct writes to `fact_bunkering` | No; routes through `vessel_operational_queue` and Path C | No; routes through `bunker_encounter_queue` and Path C |
| Concurrency risk added | None | None |
| Ingestion mode | Manual; operator provides IMO, start time, end time | Automated; continuous near real-time |
| Data freshness | On-demand only; gaps between manual runs are not filled automatically | Near real-time (minutes) |
| Fleet coverage | Operator-controlled; exactly the ships and window provided | Bounded by streaming source subscription scope |
| Suitable as standalone pipeline | No; 291,571 ships make automatic scheduling infeasible | Yes; if streaming source covers the full fleet |
| Visit ID linkage | Direct; embedded in encounter ID | Requires `ods_port_visit` join |
| Port unlocode | In API response | Requires `ods_port_visit` join |
| Backfill capability | Yes; re-run with any IMO and time range | No; streaming is forward-only |
| Fact loading integration | Reuses `vessel_operational_queue` and `fact_operational_events_dag.py` unchanged | Extends `fact_operational_events_dag.py` to poll `bunker_encounter_queue` |
| Implementation complexity | Lower; no scheduler, no watermark, no ship discovery | Higher (queue, state machine, failure callbacks) |
| Operational complexity | Low; no persistent state to maintain | Queue state monitoring, streaming DAG health |
| Aligns with existing patterns | `DataExtractor` | SOF streaming + queue |

## **7. Pre-existing Concurrency Risk (Out of Scope but Flagged)**

The following risks exist in the current architecture independent of this plan and should be addressed separately:

| **Risk** | **Location** | **Recommendation** |
| --- | --- | --- |
| Path A (batch SOF) and Path C (operational events) both issue DELETE then INSERT on `fact_bunkering` with no coordination | `refresh_task_groups.py` vs `bunkering_task_groups.py` | Migrate Path A to also use the queue pattern, making Path C the sole writer |
| Path B (streaming SOF delete) issues a hard DELETE on `fact_bunkering` concurrently with Path A or C inserts | `deletion_task_groups.py` | Coordinate the delete with the queue; or use PostgreSQL advisory locks to serialize access |
| `fact_bunkering_delta` is TRUNCATEd at the end of each Path C run | `clear_delta_table.sql` | Verify `max_active_runs = 1` is set on `fact_operational_events_dag.py` to prevent concurrent runs from clearing each other's delta data |

## **8. Open Questions**

| **#** | **Question** | **Impacts** |
| --- | --- | --- |
| 1 | Is there a global time-range endpoint that returns all bunkering encounters without requiring a per-ship call? | If yes, Route A could be redesigned as an automated pipeline regardless of fleet size |
| 2 | What are the API rate limits for `/encounter/byImo`? | Determines the maximum safe `imo` size per Route A DAG run |
| 3 | What percentage of the active fleet is covered by the streaming source? | Determines whether Route B can be the sole continuous ingestion path or only provides partial coverage |
| 4 | Is `max_active_runs = 1` set on `fact_operational_events_dag.py`? | If not, concurrent runs of Path C will TRUNCATE each other's `fact_bunkering_delta` data mid-flight |
| 5 | Is the streaming source reliable enough to be the primary ingestion mechanism? Downtime windows and delivery guarantees must be understood. | Risk assessment for Route B |