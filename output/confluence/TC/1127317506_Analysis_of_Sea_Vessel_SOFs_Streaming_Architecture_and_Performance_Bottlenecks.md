---
id: confluence:1127317506
source: confluence
type: page
space: TC
title: Analysis of Sea Vessel SOFs Streaming Architecture and Performance Bottlenecks
author: Panji Y. Wiwaha
date: '2026-02-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1127317506
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1127317506
---
# Analysis of Sea Vessel SOFs Streaming Architecture and Performance Bottlenecks

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1127317506  

## Content

# **Sea Vessel Statement of Facts (SOF) Streaming Architecture and Performance Bottlenecks**

Analysis Report :

## **I. Problem Statement**

### **Background**

The data engineering team operates a real-time streaming pipeline that ingests **Statement of Facts (SOF)** data for sea vessels from a RabbitMQ message queue. This data represents vessel voyage events, including port visits, terminal visits, berth visits, pilot activities, ship-to-ship transfers, and so on.

### **Observed Issues**

The team has identified the following operational concerns:

| **Issue** | **Observation** |
| --- | --- |
| **Processing Delays** | The fact layer transformation takes approximately ~**18 minutes** to complete |
| **Queue Accumulation** | The pipeline may not keep pace with incoming message volume, causing the RabbitMQ queue to grow over time |
| **End-to-End Latency** | Data takes **25–30 minutes** from arrival in the queue to availability in the fact tables |
| **Resource Constraints** | Workers operate with limited resources (**4Gi memory**, **1 CPU core**) |

### **Business Impact**

* **Data Freshness**: Downstream consumers (dashboards, reports, APIs) experience delays of up to 30 minutes
* **Queue Backlog Risk**: If the message arrival rate exceeds processing capacity, the backlog grows indefinitely
* **Operational Visibility**: Port operations teams may work with stale vessel movement data

### **Objective**

This report provides a comprehensive analysis of the current streaming architecture to:

1. Document the existing pipeline design and configuration
2. Identify performance bottlenecks and throughput limitations
3. Quantify processing capacity and latency characteristics
4. Establish a baseline for evaluating architectural improvements

## **II. Executive Summary**

The current SOF streaming architecture uses **Apache Airflow** to orchestrate a pull-based data pipeline that consumes vessel voyage messages from **RabbitMQ** and transforms them through staging, ODS, and fact layers.

### **Key Findings**

| **Finding** | **Detail** |
| --- | --- |
| **Maximum Throughput** | ~167 messages per minute (~240,000 per day) |
| **Primary Bottleneck** | Fact layer processing consumes **60%** of the total cycle time |
| **End-to-End Latency** | 25–30 minutes from message arrival to fact table |
| **Backpressure Handling** | None — queue grows if the arrival rate exceeds the capacity |
| **Memory Risk** | Unknown — requires measurement of actual message payload sizes |

### **Conclusion**

If the message arrival rate exceeds **~167 messages per minute**, a queue backlog will accumulate indefinitely. The Fact layer is the primary bottleneck, taking **~18 minutes out of a ~30 minutes** total cycle.

## **III. System Configuration**

### **Infrastructure Resources**

| **Resource** | **Request** | **Limit** |
| --- | --- | --- |
| **CPU** | 500m | 1 core |
| **Memory** | 3 Gi | 4 Gi |

### **Pipeline Parameters**

| **Parameter** | **Value** |
| --- | --- |
| Messages per subscriber batch | 500 |
| Batch threshold (iterations before ODS) — configurable | 10 |
| **Total messages per ODS cycle** | **5,000** |

## **IV. Architecture Overview**

### **Pipeline Stages**

| **#** | **Stage** | **Component** | **Function** |
| --- | --- | --- | --- |
| 1 | **Source** | RabbitMQ | Message queue for vessel voyage events |
| 2 | **Subscriber** | `rmq_sof__sea_vessel_` `subscriber_dag` | Consumes messages, applies filtering, and saves to Parquet |
| 3 | **Handler** | `staging_sof__sea_vessel_` `updated_handler_dag` | Loads data to staging tables, triggers ODS |
| 4 | **ODS** | `ods_sof__sea_vessel_` `updated` | Accumulates batches, transforms to ODS layer |
| 5 | **Fact** | `fact_sof__sea_vessel_` `updated` | Final dimensional model transformations |

### **Data Flow Pattern**

### **Processing Model Characteristics**

| **Characteristic** | **Description** |
| --- | --- |
| **Consumption Pattern** | Pull-based polling via Airflow scheduler (**~500 messages**) |
| **Batch Strategy** | **Accumulate 10** iterations before ODS processing |
| **Execution Model** | Fully sequential — each stage waits for completion |
| **Intermediate Storage** | Parquet files on disk |
| **State Management** | Airflow Variables stored in metadata database |

## **V. Performance Analysis**

### **Processing Duration by Stage**

| **Stage** | **Duration** | **Percentage** |
| --- | --- | --- |
| Accumulation (10 × subscriber runs) | ~10 min | 33% |
| ODS Processing (Level 1 → 2 → 3) | ~2 min | 7% |
| **Fact Processing (4 sequential tables)** | **~18 min\*** | **60%** |
| **Total Cycle Time** | **~30 min** | 100% |

<https://airflowpocca.dev.teqplay.dev/dags/fact_sof__sea_vessel_updated/grid?dag_run_id=manual__2026-02-25T10%3A34%3A02.265146%2B00%3A00&num_runs=50>\*

### **Throughput Capacity**

| **Metric** | **Value** |
| --- | --- |
| Messages per cycle | 5,000 |
| Cycle duration | ~30 minutes |
| **Throughput (per minute)** | **~167 messages** |
| **Throughput (per hour)** | **~10,000 messages** |
| **Throughput (per day)** | **~240,000 messages** |

### **End-to-End Latency**

| **Scenario** | **Latency** |
| --- | --- |
| Best case — message arrives at iteration 10 | ~20 minutes |
| Worst case — message arrives at iteration 1 | ~30 minutes |
| **Average latency** | **~25 minutes** |

## **VI. Bottleneck Identification**

### **Primary Bottleneck: Fact Layer**

The fact processing stage consumes **60% of the total cycle time** due to:

* Sequential execution of four fact tables
* Complex transformations with multiple prepare/proceed/after steps

| **Fact Table** | **Complexity** |
| --- | --- |
| `fact_ship_to_ship` | Simple (proceed only) |
| `fact_berth_visit` | Complex (prepare → proceed → after) |
| `fact_terminal_visit` | Complex (prepare → proceed → after) |
| `fact_port_visit` | **Most Complex** (11 prepare → proceed → 5 after) |

### **Secondary Bottleneck: Batch Accumulation**

The 10-iteration accumulation strategy adds **~10 minutes of latency** before ODS processing begins.

## **VII. Risk Assessment**

### **Queue Backlog Risk**

When the message arrival rate exceeds the processing capacity of **167 messages/minute**, a backlog accumulates:

wide760Backlog Growth Rate = (Arrival Rate − 167) × time

**Example Scenario: Arrival rate of 300 messages/minute**

| **Time Elapsed** | **Backlog Size** |
| --- | --- |
| **1 hour** | ~8,000 messages |
| **1 day** | ~192,000 messages |
| **1 week** | ~1.3 million messages |

### **Memory Risk Assessment**

#### **Unknown Variables**

The following factors affect memory consumption but **have not been measured**:

| **Variable** | **Impact** | **Msg Size** |
| --- | --- | --- |
| **Average message payload size** | Directly affects memory per batch | Unknown |
| **Message size variance** | Large messages could spike memory | Unknown |
| **Number of UNLOCODEs** | More ports = more diverse/larger payloads | Unknown |
| **Vessel event complexity** | Vessels with many events have larger SOFs | Unknown |
| **Peak vs. average message sizes** | Worst-case memory requirements | Unknown |

#### **Memory Consumption Factors**

| **Factor** | **Description** |
| --- | --- |
| **Geographic scope** | SOF data may arrive from ports worldwide, not a single port |
| **Vessel complexity** | Some vessels have extensive event histories (pilots, tugs, berth shifts) |
| **Concurrent processing** | Multiple streaming DAGs may run on the same worker |
| **Data copies in memory** | Pipeline creates multiple in-memory copies (`sofs[]`, `all_consumed[]`, `updated_sofs[]`, `deleted_sofs[]`) |

#### **Known Configuration**

| **Configuration** | **Value** |
| --- | --- |
| **Worker memory limit** | 4 Gi |
| **Worker memory request** | 3 Gi |
| **Messages per batch** | 500 |
| **Safety limit for all consumed messages** | 1,000 (2× batch size) |

#### **Keys to take away**

To accurately assess memory risk, the following measurements are needed:

1. **Message size profiling** — Sample actual RabbitMQ messages to determine min/avg/max payload sizes
2. **Memory monitoring** — Instrument worker pods to capture peak memory usage during processing
3. **Port distribution analysis** — Understand the geographic spread and volume per UNLOCODE
4. **Stress testing** — Test with worst-case message sizes and concurrent DAG execution

**Conclusion:** Without concrete data on message size, memory risk **cannot be definitively assessed**. The current 4Gi limit may or may not be sufficient depending on actual payload characteristics.

## **VIII. Summary of Findings**

| **Area** | **Status** | **Details** |
| --- | --- | --- |
| **Throughput** | Limited | Max ~167 msg/min; queue backlog if exceeded |
| **Latency** | High | 25–30 minutes end-to-end |
| **Bottleneck** | Identified | The fact layer consumes 60% of the cycle time |
| **Memory** | Unknown | Requires measurement of actual payload sizes |
| **Scalability** | Constrained | Sequential processing limits horizontal scaling |
| **Backpressure** | None | No mechanism to handle arrival rate spikes |

## **IX. Architecture Characteristics Summary**

| **Aspect** | **Current State** |
| --- | --- |
| **Processing model** | Pull-based (Airflow scheduler polling) |
| **Execution flow** | Fully sequential (no parallelism) |
| **Batch strategy** | 10 iterations accumulated before processing |
| **Coupling** | Tightly coupled stages |
| **Backpressure handling** | Not implemented |
| **Intermediate storage** | Disk-based (Parquet files) |
| **Orchestration** | Apache Airflow with `TriggerDagRunOperator` |