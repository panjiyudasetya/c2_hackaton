---
id: confluence:1134592001
source: confluence
type: page
space: TC
title: Streaming Metric
author: Ryan Kharisma Rakhmat
date: '2026-03-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1134592001
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1134592001
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/whiteboard/1134723074
---
# Streaming Metric

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1134592001  

## Content

Streaming Observability Specification

<https://teqplaybv.atlassian.net/wiki/spaces/TC/whiteboard/1134723074>

For the streaming data solutions in airflow, we are subscribing the queue from rabbitmq then the airflow will insert/update the streaming data into postgresql datawarehouse/mart.

In this documents we are proposing the core metrics for the streaming as below:

1. Throughput

   1. Producer
   2. Consumer
   3. Write DB Rate
   4. End to End Lag
2. Infrastructure

   1. CPU
   2. Memory
   3. Airflow cfg

We are hoping the metrics will collectively answers:

* Are we keeping up?
* Is data fresh?
* Where is the bottleneck?
* Are we losing data?

Purpose

Define critical monitoring metrics to ensure:

* low latency data delivery
* high reliability and fault tolerance
* stable throughput under the load
* SLA compliance for freshness
* system scalability

**Metric Definitions**

## 1. Producer Throughput

### Definition

Rate at which messages are published into RabbitMQ.

### Formula

Producer Rate = Delta of Messages Published

Delta Time

Sample Calculation

Messages at 10:00 = 120,000  
Messages at 10:01 = 126,000

(126000−120000)/60=100 messages/sec(126000 - 120000) / 60 = 100 \ messages/sec(126000−120000)/60=100 messages/sec

### Operational Interpretation

| Condition | Meaning |
| --- | --- |
| Stable | Normal flow |
| Sudden spike | Traffic burst |
| Drop to zero | Producer failure |

## 2. Consumer Throughput

### Definition

Rate at which messages are processed and acknowledged.

### Formula

Consumer Rate = Delta of Messages Processed

Delta Time

Sample Calculation

Processed:  
118,000 → 123,400 in 60 seconds

5400/60=90 messages/sec

### Operational Interpretation

If:

Producer Rate **>** Consumer Rate

Backlog will grow.

---

## 3. Write DB Rate

### Definition

Time required to persist processed messages into PostgreSQL. This is happens when writing to Staging Table, ODS Table and also Fact Table.

DB Commit Time = Tcommit − Tinsert\_start

### Operational Meaning

High DB → I/O pressure, lock contention, WAL saturation.

---

## 4. End-to-End Lag — Business SLA Metric

### Definition

Total time from publish to warehouse commit.

E2E Lag=Tcommit−Tpublish

### Sample

Publish: 10:00:00  
Commit: 10:03:00

Lag = 180 sec.

If SLA = 300 sec → violation.

### Operational Meaning

Primary business-facing metric.

If this rises:

* Check queue wait
* Check DB latency
* Check backlog growth

---

## 5. Infrastructure CPU

### Definition

CPU percentage usage and time while the system is running the streaming pipeline. Focusing on this processes:

* rmq → stg
* stg → ods
* ods → fact

---

## 6. Infrastructure Memory

### Definition

Memory percentage usage and time while the system is running the streaming pipeline. Focusing on this processes:

* rmq → stg
* stg → ods
* ods → fact

---

## 7. Infrastructure Airflow config

### Definition

Configurations of Airflow that we are using for this streaming related to performances. e.g :

* concurrency

---

We are focus on the four metric that we will build in grafana dashboard:

**Panel Group 1 – Throughput**

* Producer rate

  + Will be read from rabbitmq log about specific queue related to our SEA\_VESSEL or BARGE streaming visits data.
  + Will be x messages per seconds for each queue.
* Consumer rate

  + Would be the messages we are consuming for each queue (x messege per seconds).
  + Also we need to add additional data to our logs e.g in S3 or Cloudwatch to check the list of visits that we are getting from the producer. This is needed to check visit that we are acknowledge or discard (incomplete visits: no-slowmoving, no-end\_time, category type in TUG/BUNKER)
* Write DB rate

  + We will capture the time of DB write for Staging, ODS, and Fact
  + Also we need new logs to get this measurements.
* End to End Lag - Businees SLA

  + This one is for the total time from rabbitmq publish message, airflow consume messages, db write staging, ods and fact.
  + Also need new log to calculate this.

**Panel Group 2 – Infrastructure**

* CPU

  + For this one is need to capture the CPU percentage usage and time while the system is running the streaming pipeline. also need a comparison if 1 streaming running vs 2 streaming running.

    - rmq → stg
    - stg → ods
    - ods → fact
* Memory

  + For this one is need to capture the Memory percentage usage and time while the system is running the streaming pipeline. also need a comparison if 1 streaming running vs 2 streaming running.

    - rmq → stg
    - stg → ods
    - ods → fact
* Airflow

  + Worker Concurrency : *AIRFLOW\_\_CELERY\_\_WORKER\_CONCURRENCY*
  + Max Active Runs per Dag : `max_active_runs`

**THROUGHPUT**

| **Environment** | **Streaming DAG** | **Producer Rate** | **Consumer Rate** | **Write DB Rate** | **End to End Lag** |
| --- | --- | --- | --- | --- | --- |
| POCCA DEV | SEA VESSEL | this is around **15** messages per seconds. | processed 2000 messages in 1 minutes 9 seconds. so the rate are: **28** messages per seconds. with notes that the dags is running once per 2 minutes.  `[2026-03-02 05:29:20,246] All consumed sea vessel messages (2000/2000 valid) written to Parquet cache: /mnt/data/tmp/files/streaming-rabbitmq-sof-sea-vessel/raw-data/91762fba-6cfa-445d-8404-f579e41fa273.parquet (2.68 MB)[2026-03-02 05:29:20,260] Filtered 3 sea vessel SOF items for customer: USCRP` | **Write to Staging:** `[2026-03-02 05:32:07,060] Running statement: INSERT INTO STG_STATEMENT_OF_FACT[2026-03-02 05:32:07,163] Rows affected: 3`-> 0,103 Seconds  **Write to ODS:** `[2026-03-02 05:34:16,666] Accumulated 3 entry_ids for batch processing (SEA_VESSEL). [2026-03-02 05:34:16,667] Done. Returned value was: {'is_streaming_data': True, 'entry_ids': ['ea27f7a3-57df-4de6-808d-b18f20362ca3.VISIT', '09a1a0b8-2ce8-401d-be33-8a2f1099ed68.VISIT', 'f4279dd7-2684-4ac6-b1f7-0f251ee52b2a.VISIT']}`-> then wait for the batching (this will run after ~10 consecutive of messages is gathered) →`[2026-03-02 05:42:35,191] Running statement: WITH base_port_visit[2026-03-02 05:45:15,728] Marking task as SUCCESS. dag_id=ods_sof__sea_vessel_updated`-> 160.537 Seconds.  **Write to Fact:** `[2026-03-02 05:47:49,700] Running statement: INSERT INTO fact_ship_to_ship_transfers[2026-03-02 05:53:53,386] Marking task as SUCCESS. dag_id=fact_sof__sea_vessel_updated`v → 363.686 Seconds.  conclusions:   * STG : 0.103 seconds * ODS : 160.537 seconds * FACT : 363.686 seconds * ***Total : 524.326 seconds (around 8 minutes)*** | although the total of Write DB rate are : 14 minutes.  but for this one will be get from consumer rate start and the ends of write DB into facts. so `05:53:53,386` - `05:29:20,246` =  ***24 minutes, 33 seconds, and 140 milliseconds.*** |
|  | BARGE | this is around **5** messages per seconds. | Processed 219 messages in 16 seconds. so the rate are: **13** messages per seconds. with notes that the dags is running once per 2 minutes.  `[2026-03-02 05:27:13,322] All consumed barge messages (219/219 valid) written to Parquet cache: /mnt/data/tmp/files/streaming-rabbitmq-sof-barge/raw-data/9f0f4b41-7e16-433d-b015-e272f93e22fb.parquet (0.35 MB) [2026-03-02 05:27:13,322] Filtered 1 barge SOF items for customer: USCRP` | **Write to Staging:** `[2026-03-02 05:28:40,044] Running statement: INSERT INTO STG_STATEMENT_OF_FACT[2026-03-02 05:28:40,057] Rows affected: 1`-> 0,013 seconds  **Write to ODS:** `[2026-03-02 05:30:30,137] Accumulated 1 entry_ids for batch processing (BARGE). [2026-03-02 05:30:30,137] Done. Returned value was: {'is_streaming_data': True, 'entry_ids': ['d540c388-ec81-4040-9a32-2f1f99b2f85c.VISIT']}`-> then wait for the batching (this will run after ~10 consecutive of messages is gathered) →`[2026-03-02 05:41:44,283] Running statement: WITH base_port_visit[2026-03-02 05:44:56,637] Marking task as SUCCESS. dag_id=ods_sof__barge_updated`-> 192,354 Seconds  **Write to Fact:** `[2026-03-02 05:47:13,571] Running statement:[2026-03-02 05:53:35,187] Marking task as SUCCESS. dag_id=fact_sof__barge_updated`-> 381,616 Seconds.  conclusions:   * STG : 0,013 seconds * ODS : 192,354 seconds * FACT : 381,616 seconds * ***Total : 573,983 seconds (around 9 minutes)*** | although the total of Write DB rate are : 14 minutes.  but for this one will be get from consumer rate start and the ends of write DB into facts. so `05:53:35,187` - `05:27:13,322` =  ***26 minutes, 21 seconds, and 865 milliseconds.*** |
| POCCA LIVE | SEA VESSEL | this is around **25** messages per seconds. | processed 2380 messages in 33 seconds. so the rate are: **72** messages per seconds. with notes that the dags is running once per 2 minutes.  `[2026-02-27 03:54:36,314] All consumed sea vessel messages (2380/2380 valid) written to Parquet cache: /mnt/data/tmp/files/streaming-rabbitmq-sof-sea-vessel/raw-data/81b63f2c-6f1b-43c8-8e6b-f28d7cf6280f.parquet (3.15 MB) [2026-02-27 03:54:36,323] Filtered 3 sea vessel SOF items for customer: USCRP` | **Write to Staging**: `[2026-02-27 03:55:08,492] Running statement: INSERT INTO STG_STATEMENT_OF_FACT` `[2026-02-27 03:55:08,510] Rows affected: 3` → 0.018 seconds  **Write to ODS**: `[2026-02-27 03:55:36,330] Accumulated 3 entry_ids for batch processing (SEA_VESSEL). [2026-02-27 03:55:36,330] Done. Returned value was: {'is_streaming_data': True, 'entry_ids': ['b1ad2166-cb45-4f9a-a29f-d383c7496c36.VISIT', '1d3a6ab3-086f-40ed-a52e-b7f222fa31f8.VISIT', '5aa7f7e1-2bae-467d-bf3a-b99037065de6.VISIT']}`-> then wait for the batching (this will run after ~10 consecutive of messages is gathered) → `[2026-02-27 04:06:19,154] Running statement: WITH base_port_visit AS (` `[2026-02-27 04:08:11,534] Marking task as SUCCESS. dag_id=ods_sof__sea_vessel_updated`-> 112.38 seconds  **Write to Fact**: `[2026-02-27 04:10:08,132] Running statement: INSERT INTO fact_ship_to_ship_transfers (` `[2026-02-27 04:22:27,578] Marking task as SUCCESS. dag_id=fact_sof__sea_vessel_updated`-> 739.446 seconds  conclusions:   * STG : 0.018 seconds * ODS : 112.38 seconds * FACT : 739.446 seconds * ***Total : 851.844 seconds (around 14 minutes)*** | although the total of Write DB rate are : 14 minutes.  but for this one will be get from consumer rate start and the ends of write DB into facts. so `04:22:27,578` - `03:54:36,314` =  ***27 minutes, 51 seconds, and 264 milliseconds.*** |
|  | BARGE | This is around **4** messages per seconds. | Processed 277 messages in 3 seconds. so the rate are **92** messages per seconds. with notes that the dags is running once per 2 minutes.  `[2026-02-27 03:54:06,800] All consumed barge messages (277/277 valid) written to Parquet cache: /mnt/data/tmp/files/streaming-rabbitmq-sof-barge/raw-data/173e2105-5efd-46a1-a72d-d1d6b5fab132.parquet (0.41 MB) [2026-02-27 03:54:06,800] Filtered 4 barge SOF items for customer: USCRP` | **Write to Staging**: `[2026-02-27 03:54:27,569] Running statement: INSERT INTO STG_STATEMENT_OF_FACT` `[2026-02-27 03:54:27,587] Rows affected: 4`-> 0.018 Seconds  **Write to ODS**: `[2026-02-27 03:54:58,710] Accumulated 4 entry_ids for batch processing (BARGE). [2026-02-27 03:54:58,710] Done. Returned value was: {'is_streaming_data': True, 'entry_ids': ['7ac6108b-d3bf-4f73-a403-b5cf78745436.VISIT', '6172dc80-9308-4d37-9b59-87ce457a7965.VISIT', '4431a330-8c3b-4be6-a0a4-5d70f6db6818.VISIT', '80c1f561-d43d-4482-84e5-f672371a799d.VISIT']}`-> then wait for the batching (this will run after ~10 consecutive of messages is gathered) →`[2026-02-27 04:06:18,260] Running statement: WITH base_port_visit AS[2026-02-27 04:08:15,752] Marking task as SUCCESS. dag_id=ods_sof__barge_updated` → 117.492 Seconds.  **Write to Fact**: `[2026-02-27 04:09:50,917] Running statement:[2026-02-27 04:22:34,999] Marking task as SUCCESS. dag_id=fact_sof__barge_updated` → 764.082 Seconds  conclusions:   * STG : 0.018 seconds * ODS : 117.492 seconds * FACT : 764.082 seconds * ***Total : 969.354 seconds (around 16 minutes)*** | although the total of Write DB rate are : 16 minutes.  but for this one will be get from consumer rate start and the ends of write DB into facts. so `04:22:34,999` - `03:54:06,800` =  ***28 minutes, 28 seconds, and 199 milliseconds.*** |

**INFRASTRUCTURE**

| **Environment** | **Streaming DAG** | **CPU**  rmq → stg | **CPU**  stg → ods | **CPU**  ods -> fact | **Memory**  rmq → stg | **Memory**  stg → ods | **Memory**  ods → fact | **POD Restart** | **Airflow cfg**  worker concurrency | **Airflow cfg**  max active runs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| POCCA DEV | SEA VESSEL | RequestsCPU: 500m  Limits CPU: 1 | RequestsCPU: 500m  Limits CPU: 1 | Requests CPU: 500m  Limits CPU: 1 | Requests Memory: 6Gi  Limits Memory: 6Gi | Requests Memory: 6Gi  Limits Memory: 6Gi | Requests Memory: 6Gi  Limits Memory: 6Gi | 2 | 3 | 1 |
|  | BARGE | RequestsCPU: 500m  Limits CPU: 1 | RequestsCPU: 500m  Limits CPU: 1 | Requests CPU: 500m  Limits CPU: 1 | Requests Memory: 6Gi  Limits Memory: 6Gi | Requests Memory: 6Gi  Limits Memory: 6Gi | Requests Memory: 6Gi  Limits Memory: 6Gi | 2 | 3 | 1 |
| POCCA LIVE | SEA VESSEL | RequestsCPU: 500m,  Limits CPU: 2, | RequestsCPU: 500m,  Limits CPU: 2, | Requests CPU: 500m,  Limits CPU: 2, | Requests Memory: 4Gi  Limits Memory: 6Gi | Requests Memory: 4Gi  Limits Memory: 6Gi | Requests Memory: 4Gi  Limits Memory: 6Gi | NO | 3 | 1 |
|  | BARGE | RequestsCPU: 500m,  Limits CPU: 2, | RequestsCPU: 500m,  Limits CPU: 2, | Requests CPU: 500m,  Limits CPU: 2, | Requests Memory: 4Gi  Limits Memory: 6Gi | Requests Memory: 4Gi  Limits Memory: 6Gi | Requests Memory: 4Gi  Limits Memory: 6Gi | NO | 3 | 1 |

**Some Screenshot as an attachments**

1. rabbitmq console screenshot in POCCA LIVE:

2. rabbitmq console screenshot in POCCA DEV:

3. another screenshot: