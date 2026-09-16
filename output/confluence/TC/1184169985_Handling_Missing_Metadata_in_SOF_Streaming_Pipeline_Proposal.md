---
id: confluence:1184169985
source: confluence
type: page
space: TC
title: Handling Missing Metadata in SOF Streaming Pipeline Proposal
author: Panji Y. Wiwaha
date: '2026-04-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1184169985
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1184169985
---
# Handling Missing Metadata in SOF Streaming Pipeline Proposal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1184169985  

## Content

# **Handling Missing Metadata in SOF Streaming Pipeline Proposal**

## **I. Problem Statement**

### **Current Situation**

The SOF (Statement of Fact) streaming pipeline processes vessel visit records every 5 minutes. These records reference master data entities:

* **Ships** (via IMO/MMSI)
* **Ports** (via UNLOCODE)
* **Terminals** (via area ID)
* **Berths** (via area ID)

### **The Problem**

SOF records frequently arrive **before** their referenced metadata exists in ODS master tables. This occurs because:

1. **Timing mismatch** - SOF stream updates faster than metadata ingestion
2. **New entities** - Ships/ports appearing for the first time in the system
3. **API sync delays** - CSI/POMA API ingestion may lag behind real-world operations

### **Impact**

| **Issue** | **Consequence** |
| --- | --- |
| **ODS transformation failures** | Foreign key violations, failed DAG runs |
| **Alert fatigue** | Repeated "missing metadata" errors in Slack |
| **Manual intervention** | Operators must trigger metadata refresh manually |
| **Data delays** | Valid SOF records blocked by a few missing dependencies |

## **II. Proposed Architecture**

A **two-component solution** (in red) that validates metadata before processing and automatically recovers deferred records:

| **Component** | **DAG** | **Schedule** | **Purpose** |
| --- | --- | --- | --- |
| **Staging Stream DAG** | `sea_vessel_stream_dag.py` | @ 1 min | RabbitMQ → Staging + Queue |
| **ODS Stream DAG** (modified) | `stream_dag.py` | @ 5 min | Validates metadata, defers records with missing dependencies |
| **Recovery Stream DAG** (new) | `sof_metadata_recovery_dag.py` | @ 1 hour | Ingests missing metadata, re-enables deferred records |

### **Key Design Principles**

1. **Self-contained** - Recovery DAG owns its complete micro-ETL flow
2. **Targeted ingestion** - Only fetches specific missing entities, not full refresh
3. **No external dependencies** - Does not trigger or wait for manual DAGs
4. **Sequential guarantees** - ODS/DIM transformation completes before clearing notes

### **Workflow Summary**

**ODS Stream (Every 5 min)**

1. Fetch `PENDING` records (excluding `note='MISSING_METADATA'`)
2. Validate metadata exists in ODS tables
3. **Valid records** → Continue to ODS transformation
4. **Invalid records** → Set `note='MISSING_METADATA'`, remain `PENDING`

**Recovery Stream (Hourly)**

1. Fetch `PENDING` records with `note='MISSING_METADATA'`
2. Extract unique missing entity IDs (ships, ports, terminals, berths)
3. Execute targeted API calls (CSI for ships, POMA for infrastructure)
4. Run inline ODS/DIM transformations for new entities only
5. Clear `MISSING_METADATA` note → Records return to ODS stream

## **III. Why This Approach?**

### **Options Considered**

| **Option** | **Description** |
| --- | --- |
| **(A) SQL-Level Filtering** | Add `EXISTS` clauses to the fetch query to skip records with missing metadata |
| **(B) Modify Manual DAGs to Scheduled** | Convert existing manual ingestion DAGs to run on a schedule for automatic metadata refresh |
| **(C) Self-Contained Recovery** | New recovery DAG that owns its own micro-ETL for missing entities |

### **Options Comparison**

| **Criteria** | **(A) SQL Filtering** | **(B) Modify Manual DAGs to Scheduled** | **(C) Self-Contained Recovery** |
| --- | --- | --- | --- |
| **Visibility** | Silent filtering, no tracking | DAG execution visible | Explicit deferral with `note` column |
| **Fetches Missing Data** | None - waits indefinitely | Yes - full table refresh | Yes - targeted API calls |
| **Scope** | N/A | Full table refresh | Only missing entities |
| **Design Intent** | N/A | DAGs are designed for manual use,  not automation | Purpose-built for recovery |
| **Query Performance** | 4+ subqueries with JSONB parsing | No overhead | Validation only on fetched batch |
| **Separation of Concerns** | Mixes validation with fetch | Repurposes existing DAGs | Clear ownership boundaries |
| **Maintenance Risk** | Complex SQL to maintain | Changes affect manual workflows | Isolated, no side effects |

### **Comparison Summary**

* **Option A** → hides the problem without solving it. Here is an example of the complex where clause query to maintain:

  sqlSELECT ...
  FROM sof\_processing\_queue
  ...
  WHERE
  ...
  -- Ship must exist in ODS
  AND EXISTS (
  SELECT 1 FROM ods\_ship s
  WHERE s.imo = sof.ship ->> 'id'
  )
  -- Port must exist in ODS
  AND EXISTS (
  SELECT 1 FROM ods\_port p
  WHERE p.unlocode = sof.unlocode
  )
  -- All terminals must exist (if any)
  AND NOT EXISTS (
  SELECT 1
  FROM jsonb\_array\_elements(sof.terminal\_visits) AS tv
  WHERE NOT EXISTS (
  SELECT 1 FROM ods\_terminal t
  WHERE
  t.id = tv -> 'area' ->> 'id'
  AND tv -> 'area' ->> 'type' = 'terminal'
  )
  )
  -- All berths must exist (if any)
  AND NOT EXISTS (
  SELECT 1
  FROM jsonb\_array\_elements(sof.berth\_visits) AS bv
  WHERE NOT EXISTS (
  SELECT 1 FROM ods\_berth b
  WHERE
  b.id = bv -> 'area' ->> 'id'
  AND tv -> 'area' ->> 'type' = 'berth'
  )
  );
* **Option B** → repurposes DAGs designed for manual execution; changes could impact existing manual workflows
* **Option C** → provides a purpose-built solution without modifying existing DAG behavior

## **IV. Overall Summary**

| **Aspect** | **Requirements** |
| --- | --- |
| **Validation location** | New task in `stream_dag.py` after `fetch_pending_records`. |
| **Deferral mechanism** | Set `note='MISSING_METADATA'` column in `sof_processing_queue`. |
| **Recovery mechanism** | New self-contained DAG with inline micro-ETL. |
| **ODS/DIM handling** | Sequential execution within recovery DAG task groups requires conditional SQL template rendering to process only targeted entities. |
| **External dependencies** | None - fully independent of manual DAGs. |

## **IV. Tasks Plan**

| **Domain** | **Plan** | **Tasks** | **Notes** |
| --- | --- | --- | --- |
| **API Updates** | Add a new API in dataflow plugins | * Add an API to get a list of ships by multiple IDs | POST /shipRegister/id [ <id1>, <id2>, ... ]   * In case of failure, i.e., the ID is also not present in the CSI data:    + Add a retry mechanism, for example, retry them by tomorrow / the day after, or limit them by retry count.   + Skip the rest all of the remaining tasks. |
| * Add an API to get a list of ship-mapping by multiple IMOs | POST /shipMapping/imo [ <imo1>, <imo2>, ... ] |
| * Add an API to get a list of ports by multiple IDs | POST /port/bulk [ <id1>, <id2>, ... ] |
| * Add an API to get a list of terminals by multiple IDs | POST /terminal/bulk [ <id1>, <id2>, ... ] |
| * Add an API to get a list of berths by multiple IDs | POST /berth/bulk [ <id1>, <id2>, ... ] |
| **ODS STREAM** (modified)  `ods_sof/` `stream_dag.py` | Update ODS processing tasks | * Add a new task after `fetch_pending_records` to identify which IDs have complete or missing metadata * Add a branching task to process pending tasks separately based on metadata completion status. * Update the pending queues that are missing metadata in the `sof_processing_queue` table and set the `note='MISSING_METADATA'`. | N/A |
| **RECOVERY STREAM** (new) | Implement missing metadata ingestion and re-enable deferred pending records | * Fetch deferred pending records * Extract missing metadata IDs (missing ships, ports, terminals, berths) * Execute micro ETL—targeted STAGING ingestion, ODS processing, and DIM processing * Unset missing metadata notes; `note=NULL` | N/A |