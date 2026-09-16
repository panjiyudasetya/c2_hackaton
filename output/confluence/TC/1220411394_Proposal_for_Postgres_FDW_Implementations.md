---
id: confluence:1220411394
source: confluence
type: page
space: TC
title: Proposal for Postgres FDW Implementations
author: Panji Y. Wiwaha
date: '2026-08-24'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1220411394
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1220411394
---
# Proposal for Postgres FDW Implementations

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1220411394  

## Content

# Proposal Airflow Performance Improvement

## Optimization of Data Engineering Pipelines Using PostgreSQL FDW Architecture

---

# 1. Executive Summary

This proposal aims to improve the performance, scalability, and operational efficiency of the organization’s data engineering platform by replacing dataframe-heavy ETL patterns with database-native processing using PostgreSQL Foreign Data Wrapper (FDW).

At first we are examining our curent architecture of the ETL as below:

Above diagram is occured on our batching and streaming implementations of ETL from our ODS-> FACT and also ODS-> DIM. For example on the Load Fact Port Visit as below:

| **phase** | **list of tasks** | **descriptions** |
| --- | --- | --- |
| prepare | inbound, outbound, base\_query, duration\_between\_terminal,drifting\_duration\_between\_terminal, anchor\_duration\_between\_terminal, slowmoving\_duration\_details, base\_data, shifting, anchor\_duration\_detail, sailing\_duration | Data Preparations take places on Data Warehouse (DWH) |
| proceed | proceed | Airflow (get the data from DWH then put in Memory then ingested those rows into MART) |
| add\_summary | berths, terminals, shifting\_inside\_terminals, ship\_to\_ship, | Additional Summary takes places on Data MART (MART) |

We can imagine if on the `proceed` phase we got thousands or millions of rows data, the airflow could be so struggling to handle that heavy loads.

Other than that our DQC pipeline also using dataframe-heavy ETL as below:

Above diagram is explaining our QC Pipeline works, the heavy things here are comparing the data from datawarehouse and mart, here is the sample of Cross-database validations for Quality Checks:

| **quality dimension** | **case** | **descriptions** |
| --- | --- | --- |
| Validity | port visit `pilot_durations` validity checks | There are steps to do validity/accuracy/completeness checks here as below:   1. load fact or dim data from MART 2. load ods data from DWH 3. join fact and ods in polars dataframe 4. compare and checks the discrepancy 5. get some invalid visits to put in the logs 6. clean up dataframe |
| Accuracy | port visit accuracy checks |
| Completeness | ods and dim completeness checks. |

sample codes:

wide760def \_load\_fact\_port\_visit\_data(visit\_domain: str, \*\*context) -> Any:
"""
Load fact\_port\_visit data for validity checks.
This function loads data from two databases:
1. DATA\_MART: Fact layer data with duration fields
2. DATA\_WAREHOUSE: ODS layer data for anchor overlaps
"""
# 1. Load fact data from DATA\_MART
fact\_hook = PostgresHook(postgres\_conn\_id=ConnectionID.DATA\_MART)
with closing(fact\_hook.get\_conn()) as fact\_conn:
fact\_df = pl.read\_database(query=fact\_query, connection=fact\_conn)
# 2. Load ODS data from DATA\_WAREHOUSE
ods\_hook = PostgresHook(postgres\_conn\_id=ConnectionID.DATA\_WAREHOUSE)
with closing(ods\_hook.get\_conn()) as ods\_conn:
ods\_df = pl.read\_database(query=ods\_query, connection=ods\_conn)
# 3. Join fact data with anchor overlaps
joined\_df = fact\_df.join(ods\_df, on='visit\_id', how='left')

The current ETL architecture relies extensively on dataframe processing inside orchestration tasks executed by Apache Airflow. This design introduces several operational bottlenecks:

* Long-running ETL and fact-processing jobs e.g when ingesting ports in 2 years the facts creations is very long.
* Increasing memory consumption on Airflow workers
* Excessive data movement between databases and application memory, e.g in DQC comparison ods with fact.
* Reduced concurrency and scheduler throughput
* Growing infrastructure cost

The proposed solution introduces a database-centric ELT architecture leveraging PostgreSQL FDW capabilities to directly query and transform data across PostgreSQL instances without loading large datasets into application memory.

The expected outcome includes:

* 40–80% reduction in Airflow task execution time
* Significant reduction in worker memory utilization
* Reduced network and serialization overhead
* Higher pipeline stability and scalability
* Lower infrastructure costs
* Simplified ETL logic and maintenance

---

# 2. Background and Current Problems

## 2.1 Existing Architecture Overview

Current data pipelines follow this pattern:

wide760DWH PostgreSQL
↓
Python ETL Task (Airflow)
↓
Polars DataFrame Processing
↓
Transformation in Memory
↓
Load to Data Mart PostgreSQL

The orchestration layer is performing both:

* Workflow orchestration
* Heavy data transformation computation

This architecture creates inefficiencies because Airflow workers become data processing engines instead of orchestration engines.

The current pain-point that happens are on the BARGE processing either it is ETL processing from ODS to FACT and also on the DQC parts e.g Validity Checks. Here is the related facts:

* ship to ship
* berth visit
* terminal visit
* port visit
* anchor
* bunkering
* pilot
* tug
* port performance analytics

And also the DQC related are as below:

* completeness ODS to DIM
* completeness ODS to Fact
* accuracy check ODS to Fact (berth visit, terminal visit, port visit, pilot, tug, anchor, and bunkering)
* validity check ODS to Fact (pilot duration summary)

---

# 3. Problem Statement

## Problem 1 — DataFrame Usage Slows Down Airflow

### Current Condition

Large datasets are extracted from DWH databases into Python dataframe objects before transformations occur.

### Impact

* High CPU usage on workers
* Longer DAG duration
* Reduced Airflow scheduler responsiveness
* Worker congestion
* Increased task queue latency

### Root Cause

Dataframe processing introduces:

* Serialization overhead
* Python GIL limitations
* Memory allocation bottlenecks
* Object-copying overhead

---

## Problem 2 — Fact Processing Duration Continues to Increase

### Current Condition

Fact table transformations are becoming progressively slower as data volume grows.

### Impact

* SLA violations
* Delayed reporting
* Reduced freshness of analytics
* Longer backfill duration

### Root Cause

Fact processing currently:

* Pulls entire datasets into memory
* Performs joins outside database engines
* Uses row/object processing patterns
* Repeatedly transfers large datasets over network

This architecture does not scale linearly with data growth.

---

## Problem 3 — Memory Consumption Is Growing Rapidly

### Current Flow

wide760DWH DB → DataFrame in Worker Memory → Transformation → Mart DB

### Impact

* Memory spikes
* Celery instability
* Infrastructure scaling costs
* Kubernetes pod restarts
* Reduced task parallelism

### Root Cause

The architecture duplicates data:

1. Database memory
2. Network buffer
3. Python dataframe memory
4. Serialization/deserialization memory

Large tables may consume multiple times their raw size in dataframe representation.

---

# 4. Proposed Solution

## Implementation of PostgreSQL FDW-Based ELT Architecture

The proposal recommends implementing:

* postgres\_fdw
* SQL-native transformations
* Pushdown query optimization
* Database-side joins and aggregations
* Thin orchestration in Airflow

---

# 5. The Architecture

## Before and After

The left are current architecture is making the load of airflow higher and a lot of pain points. For the right one we are focusing the airflow only for orchestrations of the tasks the processing should be on databases this can make our airflow more reliable and run more efficient no heavy data processing and lower memory and cpu consumptions.

---

# 6. Technical Concept

## How PostgreSQL FDW Works

FDW enables PostgreSQL to query remote PostgreSQL tables as if they were local tables.

Example:

wide760# This query will be run on MART and accessing the Foreign Table From DWH
SELECT \*
FROM ods\_port\_visit pv
LEFT JOIN ods\_port p
ON pv.port\_id = p.id
WHERE p.unlocode = 'USCRP';

Instead of:

* pulling data into Python,
* converting to dataframe,
* processing row-by-row,

the transformation occurs directly inside PostgreSQL query execution and treat the different database table as a foreign table.

---

# 7. Proposed Technical Improvements

## 7.1 Replace DataFrame Transformations with SQL Pushdown

Current approach from `` `teqplay/tasks/quality/accuracy/port_visit_task_groups.py` ``

### Before

wide760@task
def check\_total\_terminal\_count\_accuracy(\*\*context):
"""
Load data with Polars cross-database join, validate in Python.
"""
# Load FACT data from DATA\_MART
df = \_load\_accuracy\_data('summary', template\_params)
# Extract visit IDs for component query
visit\_ids = df.select('visit\_id').to\_series().to\_list()
visit\_ids\_str = "', '".join(str(vid) for vid in visit\_ids)
# Validate using Python logic
validator = TerminalCountAccuracy()
hook = PostgresHook.get\_hook(conn\_id=ConnectionID.DATA\_MART)
passed\_rows, total\_rows, details = validator.validate(
df, hook=hook, template\_params={
\*\*template\_params,
'visit\_ids\_str': visit\_ids\_str
}
)
return create\_accuracy\_report(column\_to\_check, passed\_rows, total\_rows, mismatches)

Issues:

markdownwide760- ❌ Cross-database data transfer (DWH → MART → Python)
- ❌ Python-based validation logic
- ❌ Multiple round-trips to database
- ❌ Memory overhead from DataFrame operations

### After

wide760@task
def check\_total\_terminal\_count\_accuracy(\*\*context):
"""
Validate accuracy using SQL query only.
"""
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
# Execute validation entirely in SQL
result = SQLExecuteQueryOperator(
task\_id='validate\_terminal\_count\_accuracy',
conn\_id=ConnectionID.DATA\_MART,
sql='quality\_control/accuracy/port\_visit/terminal\_count\_accuracy.sql',
parameters={
'unlocode': context['params']['unlocode'],
'start': context['params']['start\_timestamp'],
'end': context['params']['end\_timestamp']
}
).execute(context)
return result

**SQL Template :** `` `quality_control/accuracy/port_visit/terminal_count_accuracy.sql` ``

wide760WITH fact\_data AS (
SELECT
visit\_id,
port\_visit\_id,
total\_terminal\_count AS fact\_terminal\_count
FROM fact\_port\_visit
WHERE port\_unlocode = %(unlocode)s
AND start\_timestamp >= %(start)s
AND start\_timestamp < %(end)s
),
ods\_data AS (
SELECT
port\_visit\_id,
COUNT(DISTINCT terminal\_visit\_id) AS ods\_terminal\_count
FROM fdw\_warehouse.ods\_terminal\_visit
WHERE deleted\_timestamp IS NULL
GROUP BY port\_visit\_id
)
SELECT
fact\_data.visit\_id,
fact\_data.fact\_terminal\_count,
COALESCE(ods\_data.ods\_terminal\_count, 0) AS expected\_terminal\_count,
CASE
WHEN fact\_data.fact\_terminal\_count = COALESCE(ods\_data.ods\_terminal\_count, 0)
THEN 'PASS'
ELSE 'FAIL'
END AS validation\_status
FROM fact\_data
LEFT JOIN ods\_data ON fact\_data.port\_visit\_id = ods\_data.port\_visit\_id;

Benefits:

markdownwide760- ✅ \*\*Zero data transfer\*\* to Python (validation happens in database)
- ✅ \*\*Leverage FDW\*\* for cross-database joins (no Polars needed)
- ✅ \*\*Single query execution\*\* (no multiple round-trips)
- ✅ \*\*Database-optimized\*\* (uses indexes, query planner)
- ✅ \*\*~80% faster\*\* execution time

---

## 7.2 Move Transformation Logic Into Database Layer

Transformations should use:

* SQL joins
* Materialized views
* Incremental merge strategies
* Window functions

wide760sql
-- Complex transformation using window functions, JOINs, and CTEs
-- All logic executed in database - no Python processing
{% set prefix = params.prefix\_temp\_table | default('', true) %}
SELECT DISTINCT ON (bv.berth\_visit\_id)
bv.id,
bv.visit\_id,
bv.berth\_visit\_id,
bv.port\_unlocode,
-- Use window functions for complex calculations
SUM(cargo.duration) OVER (PARTITION BY bv.berth\_visit\_id) AS total\_cargo\_duration,
-- Coalesce for zero-fill null durations
COALESCE(tug.tug\_arrival\_duration, 0) AS tug\_arrival\_duration,
COALESCE(bunker.bunkering\_duration, 0) AS bunkering\_duration
FROM {{ prefix }}temp\_fact\_berth\_visit\_base AS bv
LEFT JOIN {{ prefix }}temp\_fact\_berth\_visit\_cargo AS cargo
ON bv.berth\_visit\_id = cargo.berth\_visit\_id
LEFT JOIN {{ prefix }}temp\_fact\_berth\_visit\_tug AS tug
ON bv.berth\_visit\_id = tug.berth\_visit\_id
LEFT JOIN {{ prefix }}temp\_fact\_berth\_visit\_bunker AS bunker
ON bv.berth\_visit\_id = bunker.berth\_visit\_id
ORDER BY bv.berth\_visit\_id ASC;

Transformations in SQL:

markdownwide760- ✅ \*\*SQL JOINs\*\* for combining data from multiple ODS tables
- ✅ \*\*Window functions\*\* for aggregations (`SUM() OVER (PARTITION BY ...)`)
- ✅ \*\*CTEs (Common Table Expressions)\*\* for multi-step transformations
- ✅ \*\*Temp tables\*\* for intermediate results
- ✅ \*\*COALESCE/NULLIF\*\* for data quality handling

---

## 7.3 Airflow as Orchestrator Only

Airflow DAGS examples:

DAG Structure (`` `teqplay/dags/mart/fact_sof/barge_vessel_dag.py` ``)

wide760with DAG(
dag\_id='fact\_sof\_barge',
schedule=None,
catchup=False,
) as dag:
start = EmptyOperator(task\_id='start')
end = EmptyOperator(task\_id='end')
# Airflow only orchestrates - all logic in SQL
fact\_ship\_to\_ship = SQLExecuteQueryOperator(
task\_id='fact\_ship\_to\_ship',
conn\_id=ConnectionID.DATA\_MART,
sql='fact/ship\_to\_ship/proceed.sql',
parameters={'vessel\_type': 'BARGE'}
)
fact\_berth\_visit = load\_fact\_berth\_visit(
sql\_params={'vessel\_type': 'BARGE'},
template\_params={}
)
fact\_terminal\_visit = load\_fact\_terminal\_visit(
sql\_params={'vessel\_type': 'BARGE'},
template\_params={}
)
fact\_port\_visit = load\_fact\_port\_visit(
sql\_params={'vessel\_type': 'BARGE'},
template\_params={}
)
# Define dependencies (orchestration only)
chain(
start,
fact\_ship\_to\_ship,
fact\_berth\_visit,
fact\_terminal\_visit,
fact\_port\_visit,
end
)

Airflow’s Role:

markdownwide760- ✅ \*\*Orchestration\*\* - Task sequencing and dependencies
- ✅ \*\*Monitoring\*\* - Task status, retries, failure alerts
- ✅ \*\*Scheduling\*\* - Trigger DAGs at specific times
- ✅ \*\*Parameterization\*\* - Pass runtime parameters to SQL
- ❌ \*\*NOT\*\* data transformation (delegated to SQL)

---

# 8. Industry Practices and References

Several major technical organizations advocate database pushdown processing and minimizing dataframe-based ETL for large-scale pipelines.

---

## 8.1 Airbnb

Airbnb engineering promotes SQL-first ETL architectures and uses orchestration platforms primarily for workflow coordination rather than heavy in-memory processing.

Their architecture emphasizes:

* distributed SQL computation
* pushdown processing
* minimizing application-memory transformations

[Airbnb Engineering](https://airbnb.tech/?utm_source=chatgpt.com)

---

## 8.2 Netflix

Netflix data engineering practices emphasize:

* moving compute close to data
* minimizing unnecessary data transfer
* scalable SQL processing frameworks

[Netflix Tech Blog](https://netflixtechblog.com/?utm_source=chatgpt.com)

---

## 8.3 Uber

Uber engineering recommends minimizing Python bottlenecks in high-throughput pipelines and optimizing execution using query pushdowns and distributed storage processing.

[Uber Engineering](https://www.uber.com/blog/engineering/?utm_source=chatgpt.com)

---

## 8.4 LinkedIn

LinkedIn’s data infrastructure architecture emphasizes:

* scalable data movement
* reducing ETL duplication
* optimizing compute locality

[LinkedIn Engineering](https://engineering.linkedin.com/?utm_source=chatgpt.com)

---

## 8.5 PostgreSQL Community Best Practices

The PostgreSQL ecosystem strongly supports FDW-based federation for:

* cross-database querying
* migration simplification
* low-latency analytics
* reduced ETL duplication

[PostgreSQL FDW Documentation](https://www.postgresql.org/docs/current/postgres-fdw.html?utm_source=chatgpt.com)

---

# 9. Benefits Analysis

| Area | Current State | Proposed FDW Architecture |
| --- | --- | --- |
| Airflow CPU Usage | High | Low |
| Memory Consumption | High | Minimal |
| Data Transfer | Large | Reduced |
| Processing Time | Long | Faster |
| Scalability | Limited | Better |
| DAG Stability | Medium | High |
| Operational Complexity | High | Lower |
| Infrastructure Cost | Growing | Optimized |
| Parallelism | Limited | Improved |

---

# 10. Expected Performance Improvements

| Metric | Current | Target Improvement |
| --- | --- | --- |
| DAG Runtime | Baseline | 40–80% faster |
| Memory Usage | Baseline | 60–90% lower |
| Network Transfer | Baseline | 50–70% lower |
| Worker Stability | Medium | High |
| Concurrent Tasks | Limited | Increased |
| Backfill Speed | Slow | Faster |

---

# 11. Risks and Mitigation

| Risk | Mitigation |
| --- | --- |
| Cross-DB latency | Use indexed queries and pushdown filtering |
| FDW query inefficiency | Optimize execution plans |
| Lock/contention | Use incremental processing |
| Network dependency | Deploy within same VPC/subnet |
| SQL complexity growth | Standardize SQL templates |

---

# 12. Implementation Plan

## Phase 1: Assessment (1–2 Weeks)

### Week 1: Identify DataFrame-Heavy Operations

#### Task 1.1: Audit Quality Control DAGs

**Owner:** Data Engineering Team  
**Duration:** 2 days

**Concrete Steps:**

bashwide760# 1. Find all Polars DataFrame usage in quality checks
cd /path/to/dataflow\_dag\_core
rg "pl\.DataFrame|pl\.read\_database" teqplay/services/quality/ -l > analysis/polars\_usage.txt
rg "PostgresHook.\*get\_conn\(\)" teqplay/services/quality/ -l > analysis/db\_connections.txt
# 2. Identify cross-database operations
rg "ConnectionID\.DATA\_MART.\*ConnectionID\.DATA\_WAREHOUSE|ConnectionID\.DATA\_WAREHOUSE.\*ConnectionID\.DATA\_MART" teqplay/ -A 5 -B 5 > analysis/cross\_db\_ops.txt

**Target Files:**

* `teqplay/services/quality/accuracy/*.py` (10 files)
* `teqplay/services/quality/validity/*.py` (7 files)
* `teqplay/services/quality/completeness/*.py` (3 files)
* `teqplay/tasks/quality/**/*.py` (15+ files)

**Deliverable:** `analysis/quality_control_audit.md`

markdownwide760# Quality Control Audit Results
## Cross-Database Operations Using Polars
### Accuracy Checks (10 instances)
1. \*\*BerthVisitAccuracy\*\* (`teqplay/services/quality/accuracy/berth\_visit\_summary\_accuracy.py`)
- Cross-DB: ✅ (FACT → ODS join)
- Memory: ~150MB per check
- Runtime: ~12 seconds
- Records: ~5,000 visits
2. \*\*PortVisitAccuracy\*\* (`teqplay/services/quality/accuracy/port\_visit\_summary\_accuracy.py`)
- Cross-DB: ✅ (FACT → ODS join)
- Memory: ~200MB per check
- Runtime: ~18 seconds
- Records: ~8,000 visits
### Validity Checks (1 instance)
1. \*\*PortVisitDurationValidity\*\* (`teqplay/services/quality/validity/port\_visit\_duration\_validity.py`)
- Cross-DB: ✅ (FACT → ODS join for pilot duration)
- Memory: ~100MB
- Runtime: ~8 seconds
- Records: ~3,000 visits
### Completeness Checks (3 instances)
1. \*\*ODS→DIM Completeness\*\* (`teqplay/tasks/quality/completeness/utils.py::qc\_ods\_dim`)
- Cross-DB: ✅ (ODS → DIM join)
- Memory: ~50MB per check
- Runtime: ~5 seconds
- Records: ~10,000 records
## Total Impact
- \*\*Total Cross-DB Operations:\*\* 14 instances
- \*\*Combined Memory Usage:\*\* ~1.2GB peak
- \*\*Combined Runtime:\*\* ~180 seconds per QC run
- \*\*Migration Priority:\*\* HIGH

#### Task 1.2: Measure Memory Usage

**Owner:** DevOps Team  
**Duration:** 2 days

**Concrete Steps:**

pywide760# Create memory profiling script
# File: scripts/profile\_quality\_checks.py
import tracemalloc
import logging
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
logger = logging.getLogger(\_\_name\_\_)
@task
def profile\_berth\_visit\_accuracy(\*\*context):
"""
Profile memory usage of BerthVisitAccuracy validation.
"""
tracemalloc.start()
# Run validation
from teqplay.services.quality.accuracy.berth\_visit\_summary\_accuracy import BerthVisitSummaryAccuracy
validator = BerthVisitSummaryAccuracy()
# ... validation logic ...
current, peak = tracemalloc.get\_traced\_memory()
tracemalloc.stop()
logger.info(f"Memory usage: Current={current / 1024 / 1024:.2f}MB, Peak={peak / 1024 / 1024:.2f}MB")
return {
'current\_mb': current / 1024 / 1024,
'peak\_mb': peak / 1024 / 1024,
'timestamp': datetime.now().isoformat()
}
with DAG(dag\_id='profile\_quality\_checks', ...) as dag:
profile\_berth\_visit\_accuracy()

**Deliverable:** `analysis/memory_baseline.csv`

csvwide760check\_type,service\_class,peak\_memory\_mb,avg\_memory\_mb,records\_processed,timestamp
accuracy,BerthVisitSummaryAccuracy,152.3,98.5,5234,2026-05-26T10:30:00
accuracy,PortVisitSummaryAccuracy,198.7,145.2,8102,2026-05-26T10:35:00
validity,PortVisitDurationValidity,105.4,82.1,3456,2026-05-26T10:40:00
completeness,ODS\_DIM\_Port,48.9,35.2,12450,2026-05-26T10:45:00

#### Task 1.3: Benchmark Current Runtimes

**Owner:** Data Engineering Team  
**Duration:** 2 days

**Concrete Steps:**

sqlwide760-- Create runtime tracking table
-- File: teqplay/templates/sql/ddl/monitoring/create\_dag\_runtime\_metrics.sql
CREATE TABLE IF NOT EXISTS dag\_runtime\_metrics (
id UUID PRIMARY KEY DEFAULT gen\_random\_uuid(),
dag\_id TEXT NOT NULL,
task\_id TEXT NOT NULL,
execution\_date TIMESTAMP NOT NULL,
duration\_seconds NUMERIC(10, 2) NOT NULL,
memory\_peak\_mb NUMERIC(10, 2),
records\_processed INTEGER,
status TEXT NOT NULL,
created\_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX idx\_dag\_runtime\_metrics\_dag\_task ON dag\_runtime\_metrics(dag\_id, task\_id, execution\_date);pywide760# Add runtime tracking to quality checks
# File: teqplay/tasks/quality/utils/runtime\_tracker.py
import time
import logging
from contextlib import contextmanager
from typing import Dict
logger = logging.getLogger(\_\_name\_\_)
@contextmanager
def track\_runtime(dag\_id: str, task\_id: str, \*\*context):
"""
Context manager to track task runtime and log to database.
"""
start\_time = time.time()
try:
yield
finally:
duration = time.time() - start\_time
# Log to database
from teqplay.repositories.monitoring import MonitoringRepository
repo = MonitoringRepository()
repo.insert\_runtime\_metric(
dag\_id=dag\_id,
task\_id=task\_id,
execution\_date=context['execution\_date'],
duration\_seconds=duration,
status='SUCCESS'
)
logger.info(f"Task {task\_id} completed in {duration:.2f} seconds")

**Deliverable:** `analysis/runtime_baseline.csv`

csvwide760dag\_id,task\_id,avg\_duration\_sec,p50\_duration\_sec,p95\_duration\_sec,p99\_duration\_sec
qc\_accuracy,check\_berth\_visit\_accuracy,12.3,11.8,15.2,18.7
qc\_accuracy,check\_port\_visit\_accuracy,18.5,17.2,22.1,25.9
qc\_validity,check\_port\_visit\_duration\_validity,8.2,7.9,10.1,12.3
qc\_completeness,qc\_ods\_dim\_port,5.1,4.8,6.2,7.5

---

### Week 2: Identify Candidate Fact Tables & Migration Targets

#### Task 1.4: Prioritize Migration Candidates

**Owner:** Data Engineering Lead  
**Duration:** 3 days

**Concrete Steps:**

pywide760# Create migration priority scoring script
# File: scripts/calculate\_migration\_priority.py
import pandas as pd
# Load baseline metrics
memory\_df = pd.read\_csv('analysis/memory\_baseline.csv')
runtime\_df = pd.read\_csv('analysis/runtime\_baseline.csv')
# Calculate priority score (0-100)
# Factors: memory usage (40%), runtime (40%), complexity (20%)
def calculate\_priority(row):
memory\_score = min((row['peak\_memory\_mb'] / 200) \* 40, 40) # Cap at 40
runtime\_score = min((row['avg\_duration\_sec'] / 20) \* 40, 40) # Cap at 40
complexity\_score = 20 if row['cross\_db\_operations'] > 1 else 10
return memory\_score + runtime\_score + complexity\_score
# Generate priority report
priority\_df = pd.merge(memory\_df, runtime\_df, on='check\_type')
priority\_df['priority\_score'] = priority\_df.apply(calculate\_priority, axis=1)
priority\_df = priority\_df.sort\_values('priority\_score', ascending=False)
priority\_df.to\_csv('analysis/migration\_priority.csv', index=False)

**Deliverable:** `analysis/migration_priority.csv`

csvwide760rank,check\_type,service\_class,priority\_score,estimated\_gain,complexity,migration\_order
1,accuracy,PortVisitSummaryAccuracy,85.2,~80% faster,Medium,Wave 1
2,accuracy,BerthVisitSummaryAccuracy,78.5,~75% faster,Medium,Wave 1
3,accuracy,TerminalVisitSummaryAccuracy,72.1,~70% faster,Medium,Wave 2
4,validity,PortVisitDurationValidity,65.8,~60% faster,Low,Wave 1
5,completeness,ODS\_DIM\_Port,45.3,~50% faster,Low,Wave 2

#### Task 1.5: Document Baseline Metrics

**Owner:** Data Engineering Team  
**Duration:** 1 day

**Deliverable:** `analysis/baseline_metrics_summary.md`

markdownwide760# Baseline Metrics Summary
## Current Architecture Performance
### Quality Control Pipeline (End-to-End)
- \*\*Total Runtime:\*\* ~180 seconds per full QC run
- \*\*Peak Memory Usage:\*\* ~1.2GB (across all checks)
- \*\*Database Connections:\*\* 28 concurrent connections (14 to DWH, 14 to MART)
- \*\*Data Transfer:\*\* ~2.5GB transferred from DB to Python per run
### Top 5 Resource-Intensive Checks
1. \*\*PortVisitSummaryAccuracy\*\*
- Runtime: 18.5s avg, 25.9s p99
- Memory: 198.7MB peak
- Cross-DB: Yes (FACT ↔ ODS)
- Records: ~8,000 visits
- \*\*Migration Priority: HIGH\*\*
2. \*\*BerthVisitSummaryAccuracy\*\*
- Runtime: 12.3s avg, 18.7s p99
- Memory: 152.3MB peak
- Cross-DB: Yes (FACT ↔ ODS)
- Records: ~5,000 visits
- \*\*Migration Priority: HIGH\*\*
3. \*\*TerminalVisitSummaryAccuracy\*\*
- Runtime: 10.8s avg, 15.2s p99
- Memory: 130.5MB peak
- Cross-DB: Yes (FACT ↔ ODS)
- Records: ~6,500 visits
- \*\*Migration Priority: MEDIUM\*\*
4. \*\*PortVisitDurationValidity\*\*
- Runtime: 8.2s avg, 12.3s p99
- Memory: 105.4MB peak
- Cross-DB: Yes (FACT ↔ ODS for pilot duration)
- Records: ~3,500 visits
- \*\*Migration Priority: HIGH\*\* (simple logic, easy win)
5. \*\*ODS\_DIM\_Port Completeness\*\*
- Runtime: 5.1s avg, 7.5s p99
- Memory: 48.9MB peak
- Cross-DB: Yes (ODS ↔ DIM)
- Records: ~12,000 ports
- \*\*Migration Priority: MEDIUM\*\*
## Migration Targets (Wave 1)
\*\*Total Expected Improvement:\*\*
- Runtime: ~70-80% reduction (180s → 35-55s)
- Memory: ~85% reduction (1.2GB → 180MB)
- Database load: ~60% reduction (28 → 11 connections)
\*\*Wave 1 Candidates:\*\*
1. PortVisitSummaryAccuracy
2. BerthVisitSummaryAccuracy
3. PortVisitDurationValidity
\*\*Wave 2 Candidates:\*\*
1. TerminalVisitSummaryAccuracy
2. All completeness checks (5 instances)

---

## Phase 2: FDW Infrastructure Setup (1 Week)

### Day 1-2: Enable postgres\_fdw Extension

#### Task 2.1: Install and Enable FDW

**Owner:** Database Admin  
**Duration:** 1 day

**Concrete Steps:**

sqlwide760-- File: teqplay/templates/sql/ddl/fdw/01\_enable\_postgres\_fdw.sql
-- Execute on DATA\_MART database
-- 1. Enable postgres\_fdw extension
CREATE EXTENSION IF NOT EXISTS postgres\_fdw;
-- 2. Verify extension is enabled
SELECT \* FROM pg\_extension WHERE extname = 'postgres\_fdw';
-- Expected output:
-- oid | extname | extowner | extnamespace | extrelocatable | extversion
-- ------+----------------+----------+--------------+----------------+------------
-- 16385 | postgres\_fdw | 10 | 2200 | t | 1.1

**Success Criteria:**

* ✅ Extension installed without errors
* ✅ Version >= 1.1
* ✅ Extension visible in `pg_extension` catalog

#### Task 2.2: Configure Foreign Servers

**Owner:** Database Admin  
**Duration:** 1 day

**Concrete Steps:**

sqlwide760-- File: teqplay/templates/sql/ddl/fdw/02\_create\_foreign\_server.sql
-- Execute on DATA\_MART database
-- Create foreign server pointing to DATA\_WAREHOUSE
CREATE SERVER IF NOT EXISTS fdw\_warehouse
FOREIGN DATA WRAPPER postgres\_fdw
OPTIONS (
host 'dwh.dev.teqplay.dev', -- Replace with actual hostname
port '5432',
dbname 'NEW-ETL-DWH',
-- Performance tuning options
fetch\_size '10000', -- Fetch 10k rows at a time
use\_remote\_estimate 'true', -- Use remote EXPLAIN for query planning
extensions 'postgres\_fdw' -- Allow pushing down postgres\_fdw functions
);
-- Verify server creation
SELECT
srvname,
srvoptions
FROM pg\_foreign\_server
WHERE srvname = 'fdw\_warehouse';
-- Expected output:
-- srvname | srvoptions
-- ---------------+---------------------------------------------------------------
-- fdw\_warehouse | {host=data-warehouse.internal.example.com,port=5432,dbname=data\_warehouse,fetch\_size=10000,use\_remote\_estimate=true}

**Configuration Parameters:**

* `fetch_size`: 10,000 (optimal for ~10k-50k row queries)
* `use_remote_estimate`: true (improves query planning accuracy)
* `extensions`: postgres\_fdw (enables function pushdown)

#### Task 2.3: Configure User Mappings

**Owner:** Database Admin  
**Duration:** 0.5 days

**Concrete Steps:**

sqlwide760-- File: teqplay/templates/sql/ddl/fdw/03\_create\_user\_mapping.sql
-- Execute on DATA\_MART database
-- Create user mapping for Airflow service account
CREATE USER MAPPING IF NOT EXISTS FOR airflow\_user
SERVER fdw\_warehouse
OPTIONS (
user 'fdw\_reader', -- Dedicated read-only user on DATA\_WAREHOUSE
password 'REDACTED' -- Use password from secret manager
);
-- Create user mapping for QC service account (if separate)
CREATE USER MAPPING IF NOT EXISTS FOR qc\_user
SERVER fdw\_warehouse
OPTIONS (
user 'fdw\_reader',
password 'REDACTED'
);
-- Verify user mappings
SELECT
um.umuser::regrole AS local\_user,
um.srvid::regclass AS server\_id,
s.srvname AS foreign\_server,
um.umoptions
FROM pg\_user\_mappings um
JOIN pg\_foreign\_server s
ON s.oid = um.srvid
WHERE s.srvname = 'fdw\_warehouse';
-- Expected output:
-- local\_user | server\_id | foreign\_server | umoptions
-- --------------+-----------+----------------+----------------------------------
-- airflow\_user | 85077086 | fdw\_warehouse | {user=fdw\_reader}
-- qc\_user | 85077086 | fdw\_warehouse | {user=fdw\_reader}

**Security Best Practices:**

* ✅ Use dedicated `fdw_reader` user with **read-only** permissions
* ✅ Store passwords in secret manager (AWS Secrets Manager, HashiCorp Vault)
* ✅ Rotate passwords every 90 days
* ✅ Audit FDW connection logs

sqlwide760-- File: teqplay/templates/sql/ddl/fdw/04\_create\_fdw\_reader\_user.sql
-- Execute on DATA\_WAREHOUSE database
-- Create dedicated FDW reader user
CREATE USER fdw\_reader WITH PASSWORD 'REDACTED';
-- Grant read-only access to ODS schema
GRANT USAGE ON SCHEMA ods TO fdw\_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA ods TO fdw\_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA ods GRANT SELECT ON TABLES TO fdw\_reader;
-- Grant read-only access to staging schema (for completeness checks)
GRANT USAGE ON SCHEMA staging TO fdw\_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA staging TO fdw\_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA staging GRANT SELECT ON TABLES TO fdw\_reader;
-- Verify permissions
SELECT
grantee,
table\_schema,
table\_name,
privilege\_type
FROM information\_schema.table\_privileges
WHERE grantee = 'fdw\_reader'
ORDER BY table\_schema, table\_name;

---

### Day 3-4: Create Foreign Tables

#### Task 2.4: Import ODS Schema

**Owner:** Data Engineering Team  
**Duration:** 1 day

**Concrete Steps:**

sqlwide760-- File: teqplay/templates/sql/ddl/fdw/05\_import\_ods\_schema.sql
-- Execute on DATA\_MART database
-- Create schema for foreign tables
CREATE SCHEMA IF NOT EXISTS fdw\_warehouse;
-- Import all ODS tables from DATA\_WAREHOUSE
IMPORT FOREIGN SCHEMA ods
FROM SERVER fdw\_warehouse
INTO fdw\_warehouse
OPTIONS (import\_default 'true');
-- Verify imported tables
SELECT
foreign\_table\_schema,
foreign\_table\_name,
foreign\_server\_name
FROM information\_schema.foreign\_tables
WHERE foreign\_server\_name = 'fdw\_warehouse'
ORDER BY foreign\_table\_name;
-- Expected output (partial):
-- foreign\_table\_schema | foreign\_table\_name | foreign\_server\_name
-- ----------------------+---------------------------+---------------------
-- fdw\_warehouse | ods\_anchor\_stop | fdw\_warehouse
-- fdw\_warehouse | ods\_berth\_visit | fdw\_warehouse
-- fdw\_warehouse | ods\_encounter | fdw\_warehouse
-- fdw\_warehouse | ods\_pilot | fdw\_warehouse
-- fdw\_warehouse | ods\_port\_visit | fdw\_warehouse
-- fdw\_warehouse | ods\_slow\_moving\_period | fdw\_warehouse
-- fdw\_warehouse | ods\_terminal\_visit | fdw\_warehouse

**Selective Import** (if needed):

sqlwide760-- Import only specific tables
IMPORT FOREIGN SCHEMA ods
LIMIT TO (
ods\_port\_visit,
ods\_terminal\_visit,
ods\_berth\_visit,
ods\_pilot,
ods\_anchor\_stop
)
FROM SERVER fdw\_warehouse
INTO fdw\_warehouse;

#### Task 2.5: Test FDW Connectivity

**Owner:** Data Engineering Team  
**Duration:** 0.5 days

**Concrete Steps:**

sqlwide760-- File: teqplay/templates/sql/ddl/fdw/06\_test\_fdw\_connectivity.sql
-- Execute on DATA\_MART database
-- Test 1: Simple SELECT
SELECT COUNT(\*) FROM fdw\_warehouse.ods\_port\_visit;
-- Test 2: JOIN with local fact table
SELECT
f.visit\_id,
f.total\_terminal\_count AS fact\_count,
COUNT(DISTINCT o.terminal\_visit\_id) AS ods\_count
FROM fact\_port\_visit f
LEFT JOIN fdw\_warehouse.ods\_terminal\_visit o
ON f.port\_visit\_id = o.port\_visit\_id
WHERE f.port\_unlocode = 'SGSIN'
AND f.start\_timestamp >= '2026-05-01'
AND f.start\_timestamp < '2026-05-02'
GROUP BY f.visit\_id, f.total\_terminal\_count
LIMIT 10;
-- Test 3: EXPLAIN ANALYZE to verify pushdown
EXPLAIN (ANALYZE, VERBOSE, BUFFERS)
SELECT
port\_visit\_id,
COUNT(\*) AS terminal\_count
FROM fdw\_warehouse.ods\_terminal\_visit
WHERE deleted\_timestamp IS NULL
AND port\_unlocode = 'SGSIN'
GROUP BY port\_visit\_id;
-- Look for "Foreign Scan" in output - indicates query is pushed to remote server

**Expected EXPLAIN output:**

wide760Foreign Scan on fdw\_warehouse.ods\_terminal\_visit (cost=100.00..150.00 rows=500 width=16)
Output: port\_visit\_id, (count(\*))
Remote SQL: SELECT port\_visit\_id, count(\*) FROM ods.ods\_terminal\_visit
WHERE deleted\_timestamp IS NULL AND port\_unlocode = 'SGSIN'
GROUP BY port\_visit\_id
Planning Time: 2.5 ms
Execution Time: 45.3 ms

**Success Criteria:**

* ✅ `Foreign Scan` appears in EXPLAIN output (query pushdown working)
* ✅ `WHERE` clause is in `Remote SQL` (predicate pushdown working)
* ✅ `GROUP BY` is in `Remote SQL` (aggregation pushdown working)
* ✅ Execution time < 100ms for test queries

---

### Day 5: Network Optimization

#### Task 2.6: Configure Connection Pooling

**Owner:** DevOps Team  
**Duration:** 0.5 days

**Concrete Steps:**

pywide760# File: teqplay/settings/airflow.py
# Update connection configuration for FDW optimization
class ConnectionID:
DATA\_MART = 'AIRFLOW\_CONN\_ID\_MART'
DATA\_WAREHOUSE = 'AIRFLOW\_CONN\_ID\_DWH'
# Airflow connection configuration (set via UI or environment variable)
# Connection ID: AIRFLOW\_CONN\_ID\_MART
# Connection Type: Postgres
# Host: data-mart.internal.example.com
# Schema: public
# Login: airflow\_user
# Password: <from secret manager>
# Port: 5432
# Extra: {
# "connect\_timeout": 10,
# "keepalives": 1,
# "keepalives\_idle": 30,
# "keepalives\_interval": 10,
# "keepalives\_count": 5,
# "application\_name": "airflow\_qc"
# }sqlwide760-- File: teqplay/templates/sql/ddl/fdw/07\_optimize\_fdw\_settings.sql
-- Execute on DATA\_MART database
-- Adjust FDW server options for better performance
ALTER SERVER fdw\_warehouse OPTIONS (
SET fetch\_size '10000', -- Batch size for large result sets
SET use\_remote\_estimate 'true', -- Use remote stats for planning
ADD async\_capable 'true' -- Enable async execution (PG 14+)
);
-- Verify settings
SELECT srvname, srvoptions FROM pg\_foreign\_server WHERE srvname = 'fdw\_warehouse';

#### Task 2.7: Security Validation

**Owner:** Security Team  
**Duration:** 0.5 days

**Concrete Steps:**

bashwide760# Security audit checklist
# File: docs/fdw\_security\_audit.md
## FDW Security Audit Checklist
### Network Security
- [ ] FDW connections use private VPC network (no public internet)
- [ ] Network ACLs restrict DATA\_MART → DATA\_WAREHOUSE traffic to port 5432 only
- [ ] Security groups allow only specific IP ranges
- [ ] TLS/SSL enabled for FDW connections (`sslmode=require`)
### Authentication & Authorization
- [ ] `fdw\_reader` user has \*\*read-only\*\* permissions (SELECT only)
- [ ] `fdw\_reader` cannot modify data (no INSERT/UPDATE/DELETE)
- [ ] `fdw\_reader` cannot access sensitive schemas (e.g., auth, secrets)
- [ ] User mapping passwords stored in secret manager (not hardcoded)
- [ ] Password rotation policy: 90 days
### Audit & Monitoring
- [ ] FDW connection logs enabled on both DATA\_MART and DATA\_WAREHOUSE
- [ ] Monitoring alerts for failed FDW connections
- [ ] Query logging enabled for FDW queries (log\_min\_duration\_statement = 1000)
- [ ] Regular audit of `fdw\_reader` permissions
### Performance & Limits
- [ ] Connection limits configured (max 10 concurrent FDW connections)
- [ ] Query timeout set (statement\_timeout = 60s for FDW queries)
- [ ] Resource limits enforced (work\_mem, temp\_buffers)sqlwide760-- File: teqplay/templates/sql/ddl/fdw/08\_enable\_ssl\_for\_fdw.sql
-- Execute on DATA\_MART database
-- Update foreign server to require SSL
ALTER SERVER fdw\_warehouse OPTIONS (ADD sslmode 'require');
-- Verify SSL is enforced
SELECT srvname, srvoptions FROM pg\_foreign\_server WHERE srvname = 'fdw\_warehouse';
-- Expected output should include: sslmode=require

**Deliverables for Phase 2:**

* ✅ FDW extension enabled on DATA\_MART
* ✅ Foreign server `fdw_warehouse` configured
* ✅ User mappings created for Airflow and QC users
* ✅ All ODS tables imported as foreign tables
* ✅ FDW connectivity tested and validated
* ✅ Security audit completed
* ✅ Documentation: `docs/fdw_setup_guide.md`

---

## Phase 3: ETL Refactoring (2–3 Weeks)

### Week 1: Replace Accuracy Checks (Wave 1)

#### Task 3.1: Refactor PortVisitSummaryAccuracy

**Owner:** Data Engineering Team  
**Duration:** 3 days

**Current Implementation:**

pywide760# teqplay/services/quality/accuracy/port\_visit\_summary\_accuracy.py
# Lines 50-100
class PortVisitSummaryAccuracy(BaseAccuracy):
def validate(self, df: pl.DataFrame, hook, template\_params: Dict) -> tuple:
"""
Validate fact\_port\_visit summary fields against ODS components using Polars.
"""
# Load FACT data from DATA\_MART
fact\_df = df.select(['visit\_id', 'total\_terminal\_count', 'total\_berth\_count'])
# Load ODS data from DATA\_WAREHOUSE using separate connection
ods\_df = self.\_load\_ods\_components(hook, template\_params)
# Join in Python/Polars
joined\_df = fact\_df.join(ods\_df, on='visit\_id', how='left')
# Validate in Python
mismatches = joined\_df.filter(
pl.col('total\_terminal\_count') != pl.col('ods\_terminal\_count')
)
return len(joined\_df) - len(mismatches), len(joined\_df), mismatches.to\_dicts()

**New Implementation:**

sqlwide760-- File: teqplay/templates/sql/quality\_control/accuracy/port\_visit\_summary\_accuracy.sql
-- Execute on DATA\_MART database (uses FDW to access DATA\_WAREHOUSE)
WITH fact\_data AS (
SELECT
visit\_id,
port\_visit\_id,
total\_terminal\_count AS fact\_terminal\_count,
total\_berth\_count AS fact\_berth\_count,
total\_anchor\_count AS fact\_anchor\_count,
total\_ship\_to\_ship\_transfers AS fact\_sts\_count
FROM fact\_port\_visit
WHERE port\_unlocode = %(unlocode)s
AND start\_timestamp >= %(start)s
AND start\_timestamp < %(end)s
AND deleted\_timestamp IS NULL
),
ods\_terminal\_count AS (
SELECT
port\_visit\_id,
COUNT(DISTINCT terminal\_visit\_id) AS ods\_terminal\_count
FROM fdw\_warehouse.ods\_terminal\_visit
WHERE deleted\_timestamp IS NULL
GROUP BY port\_visit\_id
),
ods\_berth\_count AS (
SELECT
port\_visit\_id,
COUNT(DISTINCT berth\_visit\_id) AS ods\_berth\_count
FROM fdw\_warehouse.ods\_berth\_visit
WHERE deleted\_timestamp IS NULL
GROUP BY port\_visit\_id
),
ods\_anchor\_count AS (
SELECT
port\_visit\_id,
COUNT(\*) AS ods\_anchor\_count
FROM fdw\_warehouse.ods\_anchor\_stop
WHERE deleted\_timestamp IS NULL
GROUP BY port\_visit\_id
),
ods\_sts\_count AS (
SELECT
port\_visit\_id,
COUNT(\*) AS ods\_sts\_count
FROM fdw\_warehouse.ods\_ship\_to\_ship\_transfers
WHERE deleted\_timestamp IS NULL
GROUP BY port\_visit\_id
),
validation\_results AS (
SELECT
f.visit\_id,
f.port\_visit\_id,
-- Terminal count validation
f.fact\_terminal\_count,
COALESCE(t.ods\_terminal\_count, 0) AS ods\_terminal\_count,
f.fact\_terminal\_count = COALESCE(t.ods\_terminal\_count, 0) AS terminal\_count\_match,
-- Berth count validation
f.fact\_berth\_count,
COALESCE(b.ods\_berth\_count, 0) AS ods\_berth\_count,
f.fact\_berth\_count = COALESCE(b.ods\_berth\_count, 0) AS berth\_count\_match,
-- Anchor count validation
f.fact\_anchor\_count,
COALESCE(a.ods\_anchor\_count, 0) AS ods\_anchor\_count,
f.fact\_anchor\_count = COALESCE(a.ods\_anchor\_count, 0) AS anchor\_count\_match,
-- STS count validation
f.fact\_sts\_count,
COALESCE(s.ods\_sts\_count, 0) AS ods\_sts\_count,
f.fact\_sts\_count = COALESCE(s.ods\_sts\_count, 0) AS sts\_count\_match
FROM fact\_data f
LEFT JOIN ods\_terminal\_count t ON f.port\_visit\_id = t.port\_visit\_id
LEFT JOIN ods\_berth\_count b ON f.port\_visit\_id = b.port\_visit\_id
LEFT JOIN ods\_anchor\_count a ON f.port\_visit\_id = a.port\_visit\_id
LEFT JOIN ods\_sts\_count s ON f.port\_visit\_id = s.port\_visit\_id
)
SELECT
-- Summary statistics
COUNT(\*) AS total\_records,
SUM(CASE WHEN terminal\_count\_match THEN 1 ELSE 0 END) AS terminal\_count\_passed,
SUM(CASE WHEN berth\_count\_match THEN 1 ELSE 0 END) AS berth\_count\_passed,
SUM(CASE WHEN anchor\_count\_match THEN 1 ELSE 0 END) AS anchor\_count\_passed,
SUM(CASE WHEN sts\_count\_match THEN 1 ELSE 0 END) AS sts\_count\_passed,
-- Accuracy scores
ROUND(100.0 \* SUM(CASE WHEN terminal\_count\_match THEN 1 ELSE 0 END) / COUNT(\*), 2) AS terminal\_count\_accuracy,
ROUND(100.0 \* SUM(CASE WHEN berth\_count\_match THEN 1 ELSE 0 END) / COUNT(\*), 2) AS berth\_count\_accuracy,
ROUND(100.0 \* SUM(CASE WHEN anchor\_count\_match THEN 1 ELSE 0 END) / COUNT(\*), 2) AS anchor\_count\_accuracy,
ROUND(100.0 \* SUM(CASE WHEN sts\_count\_match THEN 1 ELSE 0 END) / COUNT(\*), 2) AS sts\_count\_accuracy,
-- Mismatch details (JSON)
jsonb\_agg(
jsonb\_build\_object(
'visit\_id', visit\_id,
'terminal\_count\_mismatch', CASE WHEN NOT terminal\_count\_match THEN jsonb\_build\_object('fact', fact\_terminal\_count, 'ods', ods\_terminal\_count) END,
'berth\_count\_mismatch', CASE WHEN NOT berth\_count\_match THEN jsonb\_build\_object('fact', fact\_berth\_count, 'ods', ods\_berth\_count) END,
'anchor\_count\_mismatch', CASE WHEN NOT anchor\_count\_match THEN jsonb\_build\_object('fact', fact\_anchor\_count, 'ods', ods\_anchor\_count) END,
'sts\_count\_mismatch', CASE WHEN NOT sts\_count\_match THEN jsonb\_build\_object('fact', fact\_sts\_count, 'ods', ods\_sts\_count) END
)
) FILTER (WHERE NOT (terminal\_count\_match AND berth\_count\_match AND anchor\_count\_match AND sts\_count\_match)) AS mismatches
FROM validation\_results;pywide760# File: teqplay/tasks/quality/accuracy/port\_visit\_task\_groups.py
# Simplified task using SQL-only validation
from airflow.decorators import task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
@task
def check\_port\_visit\_summary\_accuracy(\*\*context):
"""
Validate fact\_port\_visit summary fields using SQL with FDW.
Replaced Polars cross-database join with pure SQL + FDW.
"""
from teqplay.settings.airflow import ConnectionID
from teqplay.helpers.renderer import render\_sql\_template
# Render SQL template
sql = render\_sql\_template(
base\_dir='quality\_control/accuracy',
template\_name='port\_visit\_summary\_accuracy.sql',
template\_params={
'unlocode': context['params']['unlocode'],
'start': context['params']['start\_timestamp'],
'end': context['params']['end\_timestamp']
}
)
# Execute validation query
from airflow.providers.postgres.hooks.postgres import PostgresHook
hook = PostgresHook.get\_hook(conn\_id=ConnectionID.DATA\_MART)
result = hook.get\_first(sql)
# Parse result
total\_records, terminal\_passed, berth\_passed, anchor\_passed, sts\_passed, \
terminal\_accuracy, berth\_accuracy, anchor\_accuracy, sts\_accuracy, mismatches = result
# Build accuracy report
return {
'summary\_accuracy': {
'total\_records': total\_records,
'accuracy\_score': (terminal\_accuracy + berth\_accuracy + anchor\_accuracy + sts\_accuracy) / 4,
'details': {
'terminal\_count': {
'passed': terminal\_passed,
'accuracy': terminal\_accuracy
},
'berth\_count': {
'passed': berth\_passed,
'accuracy': berth\_accuracy
},
'anchor\_count': {
'passed': anchor\_passed,
'accuracy': anchor\_accuracy
},
'sts\_count': {
'passed': sts\_passed,
'accuracy': sts\_accuracy
}
},
'mismatches': mismatches or []
}
}

**Migration Checklist:**

* [ ] Create SQL template: `quality_control/accuracy/port_visit_summary_accuracy.sql`
* [ ] Update task: `teqplay/tasks/quality/accuracy/port_visit_task_groups.py::check_port_visit_summary_accuracy`
* [ ] Remove Polars dependency from `PortVisitSummaryAccuracy` service
* [ ] Add integration test: `tests/integration/quality/test_port_visit_accuracy_sql.py`
* [ ] Run side-by-side comparison (Polars vs SQL) for 1 week
* [ ] Document performance improvements
* [ ] Deploy to production

**Expected Improvements:**

* Runtime: 18.5s → ~3.5s (~81% faster)
* Memory: 198.7MB → ~15MB (~92% reduction)
* Database connections: 2 → 1 (50% reduction)

---

#### Task 3.2: Refactor BerthVisitSummaryAccuracy

**Owner:** Data Engineering Team  
**Duration:** 2 days

**Similar pattern to Task 3.1 - create SQL template with FDW joins**

sqlwide760-- File: teqplay/templates/sql/quality\_control/accuracy/berth\_visit\_summary\_accuracy.sql
WITH fact\_data AS (
SELECT
visit\_id,
berth\_visit\_id,
total\_cargo\_operations AS fact\_cargo\_ops,
total\_tug\_count AS fact\_tug\_count,
total\_mooring\_operations AS fact\_mooring\_ops
FROM fact\_berth\_visit
WHERE port\_unlocode = %(unlocode)s
AND start\_timestamp >= %(start)s
AND start\_timestamp < %(end)s
AND deleted\_timestamp IS NULL
),
ods\_cargo\_ops AS (
SELECT
berth\_visit\_id,
COUNT(\*) AS ods\_cargo\_ops
FROM fdw\_warehouse.ods\_cargo\_operation
WHERE deleted\_timestamp IS NULL
GROUP BY berth\_visit\_id
),
ods\_tug\_count AS (
SELECT
berth\_visit\_id,
COUNT(DISTINCT tug\_id) AS ods\_tug\_count
FROM fdw\_warehouse.ods\_tug\_assistance
WHERE deleted\_timestamp IS NULL
GROUP BY berth\_visit\_id
)
-- ... similar validation logic as port\_visit\_summary\_accuracy.sql

**Migration Checklist:**

* [ ] Create SQL template
* [ ] Update task group
* [ ] Add integration tests
* [ ] Run comparison
* [ ] Deploy

**Expected Improvements:**

* Runtime: 12.3s → ~2.8s (~77% faster)
* Memory: 152.3MB → ~12MB (~92% reduction)

---

#### Task 3.3: Refactor PortVisitDurationValidity

**Owner:** Data Engineering Team  
**Duration:** 2 days

**This is the pilot duration validation we recently fixed!**

sqlwide760-- File: teqplay/templates/sql/quality\_control/validity/port\_visit\_duration\_validity.sql
WITH fact\_data AS (
SELECT
visit\_id,
port\_visit\_id,
pilot\_duration AS fact\_pilot\_duration,
total\_waiting\_time\_during\_visit\_duration,
berth\_duration,
anchor\_duration
FROM fact\_port\_visit
WHERE port\_unlocode = %(unlocode)s
AND start\_timestamp >= %(start)s
AND start\_timestamp < %(end)s
AND deleted\_timestamp IS NULL
),
ods\_pilot\_sum AS (
SELECT
port\_visit\_id,
SUM(duration) AS ods\_pilot\_duration\_sum
FROM fdw\_warehouse.ods\_pilot
WHERE deleted\_timestamp IS NULL
GROUP BY port\_visit\_id
),
-- Load anchor overlaps from ODS (cross-database join via FDW)
ods\_anchor\_overlaps AS (
SELECT
port\_visit\_id,
SUM(overlap\_duration) AS total\_anchor\_overlap
FROM fdw\_warehouse.ods\_anchor\_terminal\_overlap
WHERE deleted\_timestamp IS NULL
GROUP BY port\_visit\_id
),
validation\_results AS (
SELECT
f.visit\_id,
f.port\_visit\_id,
-- Pilot duration validation
f.fact\_pilot\_duration,
COALESCE(p.ods\_pilot\_duration\_sum, 0) AS ods\_pilot\_duration,
ABS(f.fact\_pilot\_duration - COALESCE(p.ods\_pilot\_duration\_sum, 0)) AS pilot\_duration\_diff,
ABS(f.fact\_pilot\_duration - COALESCE(p.ods\_pilot\_duration\_sum, 0)) <= 60 AS pilot\_duration\_valid, -- Allow 60s tolerance
-- Anchor overlap validation
COALESCE(ao.total\_anchor\_overlap, 0) AS anchor\_overlap,
-- Duration rules validation
f.berth\_duration >= 0 AS berth\_duration\_valid,
f.anchor\_duration >= 0 AS anchor\_duration\_valid
FROM fact\_data f
LEFT JOIN ods\_pilot\_sum p ON f.port\_visit\_id = p.port\_visit\_id
LEFT JOIN ods\_anchor\_overlaps ao ON f.port\_visit\_id = ao.port\_visit\_id
)
SELECT
COUNT(\*) AS total\_records,
SUM(CASE WHEN pilot\_duration\_valid THEN 1 ELSE 0 END) AS pilot\_duration\_passed,
SUM(CASE WHEN berth\_duration\_valid THEN 1 ELSE 0 END) AS berth\_duration\_passed,
SUM(CASE WHEN anchor\_duration\_valid THEN 1 ELSE 0 END) AS anchor\_duration\_passed,
ROUND(100.0 \* SUM(CASE WHEN pilot\_duration\_valid AND berth\_duration\_valid AND anchor\_duration\_valid THEN 1 ELSE 0 END) / COUNT(\*), 2) AS overall\_validity\_score,
-- Invalid rows with details
jsonb\_agg(
jsonb\_build\_object(
'visit\_id', visit\_id,
'pilot\_duration\_diff\_hours', ROUND(pilot\_duration\_diff / 3600.0, 2),
'fact\_pilot\_duration', fact\_pilot\_duration,
'ods\_pilot\_duration', ods\_pilot\_duration,
'anchor\_overlap', anchor\_overlap
)
) FILTER (WHERE NOT pilot\_duration\_valid) AS invalid\_pilot\_durations
FROM validation\_results;

**Migration Checklist:**

* [ ] Create SQL template (includes anchor overlap logic from ODS!)
* [ ] Update task: `teqplay/tasks/quality/validity/port_visit_task_groups.py`
* [ ] Remove `_collect_invalid_rows_with_difference` helper (no longer needed)
* [ ] Remove Polars cross-database join logic
* [ ] Add integration tests
* [ ] Deploy

**Expected Improvements:**

* Runtime: 8.2s → ~1.5s (~82% faster)
* Memory: 105.4MB → ~8MB (~92% reduction)
* **Bonus:** Eliminates the value extraction bug we recently fixed!

---

### Week 2: Refactor Completeness Checks

#### Task 3.4: Create Generic Completeness SQL Template

**Owner:** Data Engineering Team  
**Duration:** 2 days

sqlwide760-- File: teqplay/templates/sql/quality\_control/completeness/ods\_dim\_completeness.sql
-- Generic template for ODS → DIM completeness checks
WITH ods\_data AS (
SELECT id
FROM fdw\_warehouse.{{ params.ods\_schema }}.{{ params.ods\_table }}
WHERE deleted\_timestamp IS NULL
),
dim\_data AS (
SELECT id
FROM {{ params.dim\_schema }}.{{ params.dim\_table }}
WHERE deleted\_timestamp IS NULL
)
SELECT
-- ODS counts
(SELECT COUNT(\*) FROM ods\_data) AS ods\_count,
-- DIM counts
(SELECT COUNT(\*) FROM dim\_data) AS dim\_count,
-- Matching counts
(SELECT COUNT(\*)
FROM ods\_data o
INNER JOIN dim\_data d ON o.id = d.id) AS matching\_count,
-- Completeness score
ROUND(100.0 \* (SELECT COUNT(\*) FROM ods\_data o INNER JOIN dim\_data d ON o.id = d.id) /
NULLIF((SELECT COUNT(\*) FROM ods\_data), 0), 2) AS completeness\_score,
-- Missing in DIM
jsonb\_agg(o.id) FILTER (WHERE d.id IS NULL) AS missing\_in\_dim
FROM ods\_data o
LEFT JOIN dim\_data d ON o.id = d.id;pywide760# File: teqplay/tasks/quality/completeness/utils.py
# Simplified qc\_ods\_dim task
@task
def qc\_ods\_dim(
ods\_table\_name: str,
dim\_table\_name: str,
entity\_name: str,
\*\*context
):
"""
Compare ODS vs DIM completeness using SQL with FDW.
Replaced Polars cross-database join with SQL + FDW.
"""
from teqplay.settings.airflow import ConnectionID
from teqplay.helpers.renderer import render\_sql\_template
sql = render\_sql\_template(
base\_dir='quality\_control/completeness',
template\_name='ods\_dim\_completeness.sql',
template\_params={
'ods\_schema': 'ods',
'ods\_table': ods\_table\_name,
'dim\_schema': 'public',
'dim\_table': dim\_table\_name
}
)
from airflow.providers.postgres.hooks.postgres import PostgresHook
hook = PostgresHook.get\_hook(conn\_id=ConnectionID.DATA\_MART)
result = hook.get\_first(sql)
ods\_count, dim\_count, matching\_count, completeness\_score, missing\_in\_dim = result
return {
'completeness': {
'ods\_count': ods\_count,
'dim\_count': dim\_count,
'matching\_count': matching\_count,
'completeness\_score': completeness\_score,
'missing\_count': ods\_count - matching\_count,
'missing\_ids': missing\_in\_dim or []
}
}

**Migration for all completeness checks:**

* [ ] Port: `qc_ods_dim(ods_table='ods_port', dim_table='dim_port')`
* [ ] Ship: `qc_ods_dim(ods_table='ods_ship', dim_table='dim_ship')`
* [ ] Terminal: `qc_ods_dim(ods_table='ods_terminal', dim_table='dim_terminal')`
* [ ] Berth: `qc_ods_dim(ods_table='ods_berth', dim_table='dim_berth')`
* [ ] Anchorage: `qc_ods_dim(ods_table='ods_anchorage', dim_table='dim_anchorage')`

**Expected Improvements (per check):**

* Runtime: 5.1s → ~1.2s (~76% faster)
* Memory: 48.9MB → ~5MB (~90% reduction)

---

### Week 3: Create Materialized Views & Optimize

#### Task 3.5: Create Performance Analytics Materialized View

**Owner:** Data Engineering Team  
**Duration:** 3 days

sqlwide760-- File: teqplay/templates/sql/ddl/materialized\_views/mv\_port\_performance\_monthly.sql
CREATE MATERIALIZED VIEW IF NOT EXISTS mv\_port\_performance\_monthly AS
WITH monthly\_metrics AS (
SELECT
port\_unlocode,
DATE\_TRUNC('month', start\_timestamp) AS month,
-- Duration metrics
AVG(berth\_duration) AS avg\_berth\_duration,
PERCENTILE\_CONT(0.5) WITHIN GROUP (ORDER BY berth\_duration) AS median\_berth\_duration,
PERCENTILE\_CONT(0.95) WITHIN GROUP (ORDER BY berth\_duration) AS p95\_berth\_duration,
STDDEV(berth\_duration) AS stddev\_berth\_duration,
-- Waiting time metrics
AVG(total\_waiting\_time\_during\_visit\_duration) AS avg\_waiting\_time,
PERCENTILE\_CONT(0.5) WITHIN GROUP (ORDER BY total\_waiting\_time\_during\_visit\_duration) AS median\_waiting\_time,
-- Counts
COUNT(\*) AS visit\_count,
COUNT(DISTINCT ship\_id) AS unique\_ships,
SUM(total\_terminal\_count) AS total\_terminal\_visits,
SUM(total\_berth\_count) AS total\_berth\_visits
FROM fact\_port\_visit
WHERE deleted\_timestamp IS NULL
AND start\_timestamp >= CURRENT\_DATE - INTERVAL '24 months' -- Last 2 years
GROUP BY port\_unlocode, DATE\_TRUNC('month', start\_timestamp)
)
SELECT \* FROM monthly\_metrics;
-- Create indexes on materialized view
CREATE INDEX idx\_mv\_port\_perf\_unlocode\_month ON mv\_port\_performance\_monthly(port\_unlocode, month);
CREATE INDEX idx\_mv\_port\_perf\_month ON mv\_port\_performance\_monthly(month DESC);pywide760# File: teqplay/dags/utilities/refresh\_materialized\_views\_dag.py
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
with DAG(
dag\_id='refresh\_materialized\_views',
schedule='0 2 \* \* \*', # Daily at 2 AM
catchup=False
) as dag:
refresh\_port\_performance = SQLExecuteQueryOperator(
task\_id='refresh\_port\_performance\_monthly',
conn\_id=ConnectionID.DATA\_MART,
sql='REFRESH MATERIALIZED VIEW CONCURRENTLY mv\_port\_performance\_monthly;'
)

**Benefits:**

* ✅ Pre-aggregated analytics (no need to scan fact\_port\_visit for monthly reports)
* ✅ ~95% faster queries for port performance dashboards
* ✅ Reduced load on fact tables

---

## Phase 4: Benchmark & Optimization (1 Week)

### Day 1-2: Compare Runtimes

#### Task 4.1: Run Side-by-Side Performance Tests

**Owner:** Data Engineering Team  
**Duration:** 2 days

pywide760# File: scripts/benchmark\_sql\_vs\_polars.py
import time
import tracemalloc
from typing import Dict
def benchmark\_accuracy\_check(method: str, \*\*params) -> Dict:
"""
Benchmark accuracy check using either Polars or SQL method.
"""
tracemalloc.start()
start\_time = time.time()
if method == 'polars':
# Run old Polars-based validation
from teqplay.services.quality.accuracy.port\_visit\_summary\_accuracy import PortVisitSummaryAccuracy
validator = PortVisitSummaryAccuracy()
result = validator.validate(\*\*params)
elif method == 'sql':
# Run new SQL-based validation
from teqplay.tasks.quality.accuracy.port\_visit\_task\_groups import check\_port\_visit\_summary\_accuracy
result = check\_port\_visit\_summary\_accuracy.function(\*\*params)
duration = time.time() - start\_time
current, peak = tracemalloc.get\_traced\_memory()
tracemalloc.stop()
return {
'method': method,
'duration\_sec': duration,
'memory\_peak\_mb': peak / 1024 / 1024,
'memory\_current\_mb': current / 1024 / 1024
}
# Run benchmarks
results = []
for i in range(10): # Run 10 iterations
results.append(benchmark\_accuracy\_check('polars', unlocode='SGSIN', start='2026-05-01', end='2026-05-02'))
results.append(benchmark\_accuracy\_check('sql', unlocode='SGSIN', start='2026-05-01', end='2026-05-02'))
# Export results
import pandas as pd
df = pd.DataFrame(results)
df.to\_csv('analysis/benchmark\_results.csv', index=False)

**Deliverable:** `analysis/benchmark_comparison.md`

markdownwide760# Benchmark Results: SQL vs Polars
## PortVisitSummaryAccuracy
| Metric | Polars (Baseline) | SQL + FDW | Improvement |
|--------|-------------------|-----------|-------------|
| Avg Runtime | 18.5s | 3.5s | \*\*-81%\*\* ⬇️ |
| P95 Runtime | 25.9s | 4.8s | \*\*-81%\*\* ⬇️ |
| Peak Memory | 198.7MB | 15.2MB | \*\*-92%\*\* ⬇️ |
| DB Connections | 2 | 1 | \*\*-50%\*\* ⬇️ |
| Data Transfer | ~450MB | 0MB | \*\*-100%\*\* ⬇️ |
## BerthVisitSummaryAccuracy
| Metric | Polars (Baseline) | SQL + FDW | Improvement |
|--------|-------------------|-----------|-------------|
| Avg Runtime | 12.3s | 2.8s | \*\*-77%\*\* ⬇️ |
| Peak Memory | 152.3MB | 12.1MB | \*\*-92%\*\* ⬇️ |
## Overall QC Pipeline (End-to-End)
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Total Runtime | 180s | 42s | \*\*-77%\*\* ⬇️ |
| Peak Memory | 1.2GB | 180MB | \*\*-85%\*\* ⬇️ |
| DB Connections | 28 | 14 | \*\*-50%\*\* ⬇️ |

---

### Day 3-4: Analyze EXPLAIN Plans & Tune Indexes

#### Task 4.2: Analyze Query Plans

**Owner:** Database Admin  
**Duration:** 2 days

sqlwide760-- File: scripts/analyze\_fdw\_query\_plans.sql
-- Test 1: Verify predicate pushdown
EXPLAIN (ANALYZE, VERBOSE, BUFFERS, COSTS)
SELECT
f.visit\_id,
COUNT(DISTINCT t.terminal\_visit\_id) AS terminal\_count
FROM fact\_port\_visit f
LEFT JOIN fdw\_warehouse.ods\_terminal\_visit t
ON f.port\_visit\_id = t.port\_visit\_id
WHERE f.port\_unlocode = 'SGSIN'
AND f.start\_timestamp >= '2026-05-01'
AND f.start\_timestamp < '2026-05-02'
AND t.deleted\_timestamp IS NULL
GROUP BY f.visit\_id;
-- Look for:
-- ✅ "Foreign Scan" with Remote SQL containing WHERE clause
-- ✅ Hash Join or Merge Join (efficient join algorithm)
-- ❌ Seq Scan on foreign table (indicates missing index on remote table)

**Create missing indexes on DATA\_WAREHOUSE:**

sqlwide760-- File: teqplay/templates/sql/ddl/indexes/ods\_indexes\_for\_fdw.sql
-- Execute on DATA\_WAREHOUSE database
-- Indexes for FDW query performance
CREATE INDEX IF NOT EXISTS idx\_ods\_terminal\_visit\_port\_visit\_id
ON ods\_terminal\_visit(port\_visit\_id)
WHERE deleted\_timestamp IS NULL;
CREATE INDEX IF NOT EXISTS idx\_ods\_berth\_visit\_port\_visit\_id
ON ods\_berth\_visit(port\_visit\_id)
WHERE deleted\_timestamp IS NULL;
CREATE INDEX IF NOT EXISTS idx\_ods\_pilot\_port\_visit\_id
ON ods\_pilot(port\_visit\_id)
WHERE deleted\_timestamp IS NULL;
-- Indexes for FACT table on DATA\_MART
CREATE INDEX IF NOT EXISTS idx\_fact\_port\_visit\_unlocode\_timestamp
ON fact\_port\_visit(port\_unlocode, start\_timestamp)
WHERE deleted\_timestamp IS NULL;
-- Analyze tables after creating indexes
ANALYZE ods\_terminal\_visit;
ANALYZE ods\_berth\_visit;
ANALYZE ods\_pilot;
ANALYZE fact\_port\_visit;

---

### Day 5: Tune PostgreSQL Settings

#### Task 4.3: Optimize Database Configuration

**Owner:** Database Admin  
**Duration:** 1 day

sqlwide760-- File: scripts/tune\_postgres\_for\_fdw.sql
-- Execute on DATA\_MART database
-- Increase work\_mem for large JOINs (per-operation limit)
ALTER SYSTEM SET work\_mem = '256MB'; -- Up from default 4MB
-- Enable parallel query execution
ALTER SYSTEM SET max\_parallel\_workers\_per\_gather = 4;
ALTER SYSTEM SET parallel\_tuple\_cost = 0.01; -- Lower cost encourages parallelism
-- Optimize FDW batch fetching
ALTER SYSTEM SET postgres\_fdw.fetch\_size = 10000;
-- Reload configuration
SELECT pg\_reload\_conf();
-- Verify settings
SHOW work\_mem;
SHOW max\_parallel\_workers\_per\_gather;

**Deliverable:** `docs/postgres_tuning_guide.md`

---

## Phase 5: Production Rollout (1 Week)

### Day 1-3: Gradual Deployment

#### Task 5.1: Deploy Wave 1 (High-Priority Checks)

**Owner:** DevOps Team  
**Duration:** 3 days

**Deployment Strategy:**

yamlwide760# deployment/quality\_checks\_rollout.yaml
wave\_1:
description: "High-priority accuracy & validity checks"
duration: "3 days"
checks:
- PortVisitSummaryAccuracy
- BerthVisitSummaryAccuracy
- PortVisitDurationValidity
rollout:
day\_1:
- Deploy SQL templates to staging
- Run side-by-side comparison (Polars + SQL)
- Validate results match 100%
day\_2:
- Deploy to production (canary: 10% of traffic)
- Monitor error rates, runtime, memory
- Validate QC reports match baseline
day\_3:
- Increase to 100% traffic
- Disable Polars-based checks
- Monitor for 24 hours
wave\_2:
description: "Completeness checks"
duration: "2 days"
checks:
- qc\_ods\_dim (all 5 instances)
rollout:
day\_4:
- Deploy SQL templates
- Run comparison
day\_5:
- Deploy to production 100%

#### Task 5.2: Monitoring & Alerts

**Owner:** DevOps Team  
**Duration:** 1 day

pywide760# File: teqplay/notifications/datadog\_metrics.py
from datadog import statsd
def track\_quality\_check\_metrics(check\_name: str, duration: float, memory\_mb: float, status: str):
"""
Send quality check metrics to Datadog for monitoring.
"""
statsd.histogram('quality\_check.duration', duration, tags=[f'check:{check\_name}'])
statsd.histogram('quality\_check.memory\_mb', memory\_mb, tags=[f'check:{check\_name}'])
statsd.increment('quality\_check.runs', tags=[f'check:{check\_name}', f'status:{status}'])

**Datadog Alerts:**

yamlwide760# monitoring/datadog\_alerts.yaml
- name: "Quality Check Duration Spike"
query: "avg(last\_5m):avg:quality\_check.duration{check:PortVisitSummaryAccuracy} > 10"
message: "Quality check duration exceeded 10s (expected ~3.5s)"
- name: "Quality Check Memory Spike"
query: "avg(last\_5m):avg:quality\_check.memory\_mb{check:PortVisitSummaryAccuracy} > 50"
message: "Quality check memory exceeded 50MB (expected ~15MB)"

---

### Day 4-5: Validation & Documentation

#### Task 5.3: Validate Production Performance

**Owner:** Data Engineering Team  
**Duration:** 2 days

**Validation Checklist:**

* [ ] Runtime reduction: ≥70% for all migrated checks
* [ ] Memory reduction: ≥85% for all migrated checks
* [ ] Zero accuracy/validity score differences between Polars and SQL methods
* [ ] Zero production errors in 48-hour monitoring period
* [ ] Database CPU usage remains stable (no spikes from FDW queries)
* [ ] FDW connection count remains below limit (max 10 concurrent)

**Deliverable:** `docs/production_validation_report.md`

---

#### Task 5.4: Final Documentation

**Owner:** Data Engineering Lead  
**Duration:** 1 day

**Deliverables:**

1. `docs/fdw_setup_guide.md` - FDW infrastructure setup guide
2. `docs/migration_guide_sql_pushdown.md` - Step-by-step migration guide
3. `docs/performance_improvements.md` - Before/after performance metrics
4. `docs/rollback_procedure.md` - Rollback steps if issues arise
5. **Updated architecture diagram** - Include FDW in DQC architecture

---

## Success Criteria

### Phase 1 ✅

* [ ] Baseline metrics documented
* [ ] Migration priority matrix created
* [ ] Executive summary presented to stakeholders

### Phase 2 ✅

* [ ] FDW extension enabled on DATA\_MART
* [ ] Foreign server configured and tested
* [ ] All ODS tables accessible via FDW
* [ ] Security audit passed

### Phase 3 ✅

* [ ] 3+ accuracy checks migrated to SQL
* [ ] 5+ completeness checks migrated to SQL
* [ ] 1+ validity check migrated to SQL
* [ ] Materialized view created and refreshing daily

### Phase 4 ✅

* [ ] Benchmarks show ≥70% runtime improvement
* [ ] Memory usage reduced by ≥85%
* [ ] Query plans optimized (predicates pushed down)
* [ ] Indexes created on remote tables

### Phase 5 ✅

* [ ] Wave 1 deployed to production (100% traffic)
* [ ] Wave 2 deployed to production (100% traffic)
* [ ] Zero production incidents
* [ ] Documentation complete
* [ ] Team trained on new architecture

---

## Timeline Summary

| Phase | Duration | Key Deliverables |
| --- | --- | --- |
| **Phase 1: Assessment** | 1 weeks | Baseline metrics, migration priority matrix |
| **Phase 2: FDW Setup** | 1 week | FDW infrastructure, security validation |
| **Phase 3: ETL Refactoring** | 2-3 weeks | SQL templates, refactored DAGs, materialized views |
| **Phase 4: Optimization** | 1 week | Performance benchmarks, tuned indexes |
| **Phase 5: Rollout** | 1 week | Production deployment, monitoring, docs |
| **Total** | **6-7 weeks** | Production-ready SQL-based QC pipeline |

---

## Risk Mitigation

| Risk | Mitigation |
| --- | --- |
| **FDW performance slower than Polars** | Benchmark early (Phase 2); tune indexes, `fetch_size`, `work_mem` |
| **Network latency between DWH and MART** | Deploy both databases in same VPC; use internal networking |
| **Security concerns with FDW** | Use read-only `fdw_reader` user; SSL required; regular audits |
| **Query plan regression** | Monitor EXPLAIN plans; create indexes proactively |
| **Production incidents during rollout** | Gradual rollout (10% → 100%); maintain Polars code for rollback |
| **Team unfamiliarity with FDW** | Training sessions; comprehensive documentation |

---

## Expected ROI

### Performance Gains

* **Quality check runtime**: 180s → 42s (**77% faster**)
* **Memory usage**: 1.2GB → 180MB (**85% reduction**)
* **Database connections**: 28 → 14 (**50% reduction**)

# 13. Recommended Technical Standards

## Airflow

Recommended usage:

* SQL execution operators
* Lightweight Python operators only
* Minimal XCom payloads
* Avoid dataframe serialization

---

## PostgreSQL

Recommended:

* Partitioned fact tables
* Indexed join columns
* Materialized views
* Incremental merge/upsert
* Query pushdown validation

---

# 14. Success Metrics

The project will be considered successful if:

| KPI | Target |
| --- | --- |
| Airflow task memory usage | ↓ 70% |
| Average DAG runtime | ↓ 50% |
| Worker crashes | Near zero |
| Pipeline SLA achievement | > 95% |
| Infrastructure cost growth | Stabilized |
| Fact processing scalability | Improved |

---

# 15. Financial and Operational Impact

## Operational Savings

Reduction in:

* Airflow worker resource requirements
* Kubernetes resource consumption
* Celery worker scaling
* Retry and failure overhead

### Cost Savings (Estimated)

* **Compute**: ~$500/month (reduced Airflow worker memory requirements)
* **Database**: ~$300/month (fewer connections, reduced I/O)
* **Developer time**: ~40 hours/year (simpler SQL debugging vs Python/Polars)

### Total Estimated Savings: **~$10,000/year**

---

## Engineering Productivity

Benefits:

* Easier debugging
* Simplified ETL logic
* Reduced Python transformation complexity
* Faster onboarding for SQL-oriented engineers

---

# 16. Conclusion

The current dataframe-centric ETL architecture introduces significant scalability and operational limitations for growing data workloads.

Migrating toward a PostgreSQL FDW-based ELT architecture provides:

* better scalability,
* lower memory consumption,
* faster execution,
* improved Airflow stability,
* and reduced operational cost.

This proposal aligns with modern industry best practices adopted by leading technology organizations that prioritize:

* compute locality,
* pushdown processing,
* orchestration separation,
* and database-native transformations.

The implementation of PostgreSQL FDW is expected to significantly modernize the organization’s data engineering platform while preparing the architecture for future data growth and higher throughput demands.