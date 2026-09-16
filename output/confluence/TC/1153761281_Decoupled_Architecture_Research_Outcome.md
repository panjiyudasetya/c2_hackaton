---
id: confluence:1153761281
source: confluence
type: page
space: TC
title: Decoupled Architecture Research Outcome
author: Panji Y. Wiwaha
date: '2026-03-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1153761281
explicit_links:
- jira:PTO-2547
- jira:PTO-2542
- jira:PTO-2543
- jira:PTO-2544
- jira:PTO-2545
- jira:PTO-2546
- jira:PTO-2548
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1153761281
---
# Decoupled Architecture Research Outcome

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1153761281  

## Content

# **Decoupled Architecture Research Outcome**

## **Summary**

The Statement of Facts (SOF) streaming pipeline was re-architected from a monolithic, synchronous processing model to a decoupled, queue-based architecture. The key improvements include:

1. **Consolidated DAGs** → Combined UPDATE/DELETE and SEA\_VESSEL/BARGE into single DAGs to avoid database blocking
2. **Queue-based state machine** -> Persistent tracking of message processing state
3. **Race condition prevention** → “*Newer action wins*” rule enforced at every step
4. **Failure recovery** -> Automatic rollback via callbacks

## **Architecture Updates**

#### ***Before: Monolithic Architecture***

**Problems**

* Database blocking - Concurrent UPDATE and DELETE DAGs blocked each other on shared tables
* Race conditions - No coordination between UPDATE and DELETE operations
* Memory issues - Large batch processing caused OOM errors
* Stuck records - No recovery mechanism for failed processing

#### ***After: Decoupled Queue - Based Architecture (2 Combined DAGs)***

#### ***Key Design Decisions***

| **Decision** | **Rationale** |
| --- | --- |
| Combined DAGs | Single DAG per layer (ODS/Fact) prevents database blocking between operations |
| Sequential vessel types | SEA\_VESSEL before BARGE ensures deterministic processing order |
| `UPDATE` before `DELETE` | Ensures correct data state - updates complete before deletions |
| `TriggerRule.ALL_DONE` | Downstream groups run even if upstream fails (prevents stalling) |

### **State Machine Lifecycle**

#### ***State Description***

* `PENDING` → Initial state after message consumed from RabbitMQ
* `ODS_PROCESSING_STARTED` → ODS DAG has picked up the record
* `ODS_PROCESSING_COMPLETED` → ODS transformations finished successfully
* `FACTS_PROCESSING_STARTED` → Fact DAG has picked up the record
* `FACTS_PROCESSING_COMPLETED` → Fact transformations finished (terminal state)
* `CANCELLED` → Record superseded by newer action (terminal state)
* `IGNORED` → Filtered out by business rules (terminal state)

#### ***Normal Flow***

wide760PENDING → ODS\_PROCESSING\_STARTED → ODS\_PROCESSING\_COMPLETED
ODS\_PROCESSING\_COMPLETED → FACTS\_PROCESSING\_STARTED → FACTS\_PROCESSING\_COMPLETED

#### ***Failure Recovery (Automatic Rollback)***

| **Layer** | **Failure State** | **Rolls Back To** |
| --- | --- | --- |
| **ODS** | `ODS_PROCESSING_STARTED` | `PENDING` |
| **FACT** | `FACTS_PROCESSING_STARTED` | `ODS_PROCESSING_COMPLETED` |

#### ***Cancellation Rules (“Newer Action Wins”)***

| **Scenario** | **SQL To Run** | **Effect** |
| --- | --- | --- |
| **UPDATE** completes | `sof_mark_stale_deletes.sql` | Cancels older `PENDING` DELETEs |
| **DELETE** completes | `sof_mark_stale_updates.sql` | Cancels older `PENDING` UPDATEs |

### **State Machine Design Principles**

1. **Immutable** `updated_at` - The original message timestamp remains unchanged; the updated timestamp changes only when RabbitMQ updates the message
2. **Dedicated transition timestamps** - Each state change has its own column (`ods_started_at`, `facts_completed_at`, etc.)
3. **Automatic rollback** - `on_failure_callback` ensures no stuck records
4. **Retention cleanup** - Terminal states cleaned up after N days (Planned)

### **Race Condition Fixes**

#### ***Immutable*** `updated_at` ***Timestamps***

The `updated_at` column is **immutable** after queue insertion. State transitions use dedicated timestamp columns:

| **Transition** | **Timestamp Column** |
| --- | --- |
| → `ODS_PROCESSING_STARTED` | `ods_started_at` |
| → `ODS_PROCESSING_COMPLETED` | `ods_completed_at` |
| → `FACTS_PROCESSING_STARTED` | `facts_started_at` |
| → `FACTS_PROCESSING_COMPLETED` | `facts_completed_at` |
| → `CANCELLED` | `cancelled_at` |

#### ***Timestamp-Aware Fetch Logic***

**UPDATE Fetch Logic** (`sof_fetch_pending_update.sql`)

* Blocks if `DELETE` is in progress or newer
* Allows if no conflicting `DELETE` exists

**DELETE Fetch Logic** (`sof_fetch_pending_delete.sql`)

* Blocks if `UPDATE` is in progress or newer
* Allows if no conflicting `UPDATE` exists

#### **Queue-Aware Staging Hard-Delete**

sqlwide760-- Only deletes staging data OLDER than the DELETE being processed
DELETE FROM stg\_statement\_of\_fact AS stg
WHERE stg.updated\_timestamp < del.updated\_at;

### **Memory/Stability Improvements**

#### *Worker Pod Restart Analysis*

Data retrieved from [[DEV] POD Restart Monitoring](https://docs.google.com/spreadsheets/d/1bAABvfICNR3qsnfMPN_H3otUhheCnbWHKbQ7cfsB8MU/edit?gid=0#gid=0)

| **Date/Time** | **Pod** | **Exit Code** | **Reason** | **Analysis** |
| --- | --- | --- | --- | --- |
| `2026-03-09 08:10:29Z` | worker-0 | **137** | SIGKILL | **Error** - Force termination |
| `2026-03-09 08:50:03Z` | webserver | **137** | OOMKilled | **OOM** - Kernel killed |
| `2026-03-10 01:55:27Z` | worker-0 | **0** | Completed | **Graceful** - Clean shutdown |

**Key Observation:** After deploying the decoupled architecture, worker pods transitioned from OOM errors (exit code 137) to graceful shutdowns (exit code 0).

## **Before vs After Comparison**

| **Aspect** | **Before** | **After** |
| --- | --- | --- |
| **DAG Count** | 4 separate DAGs (`UPDATE`/`DELETE` × `SEA_VESSEL`/`BARGE`) | 2 combined DAGs (ODS + Fact) |
| **Database Blocking** | Concurrent DAGs block each other | Sequential execution prevents blocking |
| **Memory Usage** | High (large batch processing) | Low (controlled via queue) |
| **Race Conditions** | Uncoordinated `UPDATE`/`DELETE` | “Newer action wins” rule |
| **Failure Recovery** | Records stuck in processing state | Automatic rollback via callbacks |
| **Processing Order** | Non-deterministic | `SEA_VESSEL` → `BARGE`  `UPDATE` → `DELETE` |
| **Worker Stability** | OOM restarts (exit code 137) | Graceful shutdowns (exit code 0) |

## **Conclusion**

The decoupled architecture successfully resolves all identified issues:

| **Issue** | **Solution** |
| --- | --- |
| **Database blocking** | Combined DAGs with sequential execution |
| **OOM errors** | Queue-based controlled batch processing |
| **Race conditions** | “Newer action wins” with timestamp checks |
| **Zombie records** | Symmetric stale cancellation |
| **Stuck records** | Failure callbacks with automatic rollback |
| **Processing order** | Deterministic: `SEA_VESSEL` → `BARGE`, `UPDATE` → `DELETE` |

## **Next Steps**

1. Try out in the POCCA DEV environment
2. Address infrastructure and data stream processing issues
3. Implement a retention policy to manage backpressure queues
4. Combine data stream throughput metrics with Airflow pod status (i.e., CPU and Memory Usage)

| **#** | **Infrastructure issue** | **Mitigation** |
| --- | --- | --- |
| [#2547](https://teqplaybv.atlassian.net/browse/PTO-2547) | Worker - Graceful Shutdowns | * Reduce Concurrency to 4; Tasks queue up longer, but the worker stays healthy. * Keep Concurrency 8, Relax Probe Settings; The worker may be unresponsive for longer before Kubernetes notices. * Scale up the worker pod into two replicas; This could maintain a throughput of 8+ concurrent tasks while ensuring that health checks continue to pass. |
| **#** | **Stream processing issue** | **Mitigation** |
| [#2542](https://teqplaybv.atlassian.net/browse/PTO-2542) | Tug fact table refresh is too slow | * Limit data processing to visit IDs derived from the consumed messages. |
| [#2543](https://teqplaybv.atlassian.net/browse/PTO-2543) | Pilot fact table refresh is too slow | * Limit data processing to visit IDs derived from the consumed messages. |
| [#2544](https://teqplaybv.atlassian.net/browse/PTO-2544) | Bunkering fact table refresh is too slow | * Limit data processing to visit IDs derived from the consumed messages. |
| [#2545](https://teqplaybv.atlassian.net/browse/PTO-2545) | The anchor fact table refresh is too slow | * Limit data processing to visit IDs derived from the consumed messages. |
| [#2546](https://teqplaybv.atlassian.net/browse/PTO-2546) | Cascade deletion is not functioning correctly when the generation ID differs, but the visit ID remains the same. | * Use the bottom-up deletion strategy. |
| [#2548](https://teqplaybv.atlassian.net/browse/PTO-2548) | Ensure ODS processing functions correctly when POMA/Ship DWH are out of sync | * When running ODS processing, retrieve only pending visit IDs if the port, terminal, berth, and ship are known. |