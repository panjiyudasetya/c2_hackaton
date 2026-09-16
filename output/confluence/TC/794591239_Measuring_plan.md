---
id: confluence:794591239
source: confluence
type: page
space: TC
title: Measuring plan
author: Gavin den Hollander
date: '2025-08-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794591239
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794591239
---
# Measuring plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/794591239  

## Content

## Purpose & Objectives

This document defines **how we measure, monitor, and improve** the *elapsed time* and *rework effort* required to deliver PTO reporting on ports, from the first step of entering the context mapping to having the data available in BI.

Our goals:

1. **Predictability** – know with 90 % confidence how long each delivery will take.
2. **Transparency** – surface where time is spent and why.
3. **Continuous improvement** – spot bottlenecks and reduce waste caused by retries.

> *Testing & validation rules live in a separate Test Plan. This plan focuses solely on time & process metrics.*

## Scope & Flow

The measurement covers *both* realtime and back‑fill (Re‑events) paths and the Context‑Mapping Validation loop.

|  | **Stage** | **Baseline Duration** | **Description** |
| --- | --- | --- | --- |
| 1 | **Port Data Request** | 1h? | Request for data is done, request is planned in. |
| 2 | **Mapping in Poma** | 2 – 10 h | Create terminals, berths, EOS, anchorage records for a port. |
| 3 | **Context Mapping** **Revents Monitoring** | 1 – 15 h | Run archived AIS through dedicated AIS‑Engine to regenerate events. |
| 4 | **Context Mapping** **VesselVoyage post-processing** | 1-2h | Import revents results into VesselVoyage and determine drifting. |
| 5 | **Context Mapping** **Data Warehouse load** | 0.1 – 2 h | Persist CSI, Poma & VesselVoyage tables. |
| 6 | **Context Mapping** **Data Mart build** | 1 – 10 h | Transform facts/views for BI. |
| 7 | **Context Mapping** **Data Validation** | 4 – 7 h (+3 – 28 h per change) | Validate mappings in sandbox; redo if issues. |
| 8 | **Revents Monitoring** | 1 – 15 h | Run archived AIS through dedicated AIS‑Engine to regenerate events. |
| 9 | **VesselVoyage post-processing** | 1-2h | Import revents results into VesselVoyage and determine drifting. |
| 10 | **Data Warehouse load** | 0.1 – 2 h | Persist CSI, Poma & VesselVoyage tables. |
| 11 | **Data Mart build** | 1 – 10 h | Transform facts/views for BI. |
| 12 | **BI data import** | 1h? |  |
| 13 | **BI validation** | 8 – 24 h (+3 – 28 h per issue) | End‑to‑end QA before customer release. |
| 14 | **Deliver requested data** | 1h? |  |
| 15 | **Total** | **22 – 124 h** | Example w/ one mapping redo & one defect loop |

## Key Metrics & Definitions

|  |  |  |  |
| --- | --- | --- | --- |
| **Metric** | **Definition** | **Unit** | **Granularity** |
| **Stage Cycle Time (SCT)** | End‑Timestamp − Start‑Timestamp for each stage instance. | hours | per stage, per port |
| **Total Lead Time (TLT)** | Final BI ready time − initial Poma save time. | hours | per port |
| **Rework Count (RC)** | # of times a stage had to be rerun due to defects or spec changes. | count | per stage, per port |
| **Rework Time (RT)** | Σ (elapsed time spent on all retries) | hours | per port |
| **Predictability Index (PI)** | 95th‑pct SCT ÷ 50th‑pct SCT (lower = more predictable). | ratio | per stage, rolling 30‑d |
| **Mean Time To Recovery (MTTR)** | Avg. time to fix a failed run and achieve success. | hours | per stage, rolling 30‑d |
| **Throughput** | # ports delivered / week. | count | weekly |

## Data‑Collection Schema

A central `pipeline_metrics` table will store one record per *stage attempt*.

|  |  |
| --- | --- |
| **Field** | **Notes** |
| `attempt_id` | unique per execution |
| `reason_id` | Jira delivery Id |
| `port_unlocode` | e.g., NLRTM |
| `stage` | name of stage e.g. **Revents Monitoring** |
| `start_ts` | Timestamp |
| `end_ts` | Timestamp |
| `duration_hrs` | auto‑calc |
| `terminals_cnt` | snapshot at start |
| `ship_cnt` | sea vessel count, nullable |
| `port_days_span` | days between first & last AIS msg processed |
| `retry` | true if attempt ≥ 2 |
| `reason_recalc` | DEFECT, SCOPE\_CHANGE, DATA\_GAP, CODE\_PATCH, CONTEXT\_MAPPING |
| `issue_id` | link to Jira |
| `owner_team` | CoreComponent or DataPlatform Team |

### Capture Method

We will start out by capturing all stages by hand first. Later we will capture each stage as follows:

|  |  |  |
| --- | --- | --- |
| **Stage** | **Capture** | **Tool/Source** |
| **Port Data Request** | Manual | Jira |
| **Mapping in Poma** | Manual | Jira |
| **Revents Monitoring** | Automated | Prometheus |
| **VesselVoyage post-processing** | Automated | Prometheus |
| **Data Warehouse load** | Automated | Airflow |
| **Data Mart build** | Automated | Airflow |
| **Data validation** | Manual | Jira |

**Note:** The team handling the card is responsible for writing down the metrics in the sheet.

Removed stages. But still captured:

|  |  |  |
| --- | --- | --- |
| **~~Deliver requested data~~** | ~~Manual~~ | ~~Jira~~ |

|  |  |  |
| --- | --- | --- |
| **~~BI data import~~** | ~~Manual?~~ | ~~?~~ |
| **~~BI validation~~** | ~~Manual?~~ | ~~?~~ |

|  |  |  |
| --- | --- | --- |
| **~~Context Mapping~~** **~~Revents Monitoring~~** | ~~Automated~~ | ~~Prometheus~~ |
| **~~Context Mapping~~** **~~VesselVoyage post-processing~~** | ~~Automated~~ | ~~Prometheus~~ |
| **~~Context Mapping~~** **~~Data Warehouse load~~** | ~~Automated~~ | ~~BigQuery job metadata~~ |
| **~~Context Mapping~~** **~~Data Mart build~~** | ~~Automated~~ | ~~dbt run\_artifacts~~ |
| **~~Context Mapping~~** **~~Data Validation~~** | ~~Automated test harness~~ | ~~Great Expectations runner~~ |

## KPI’s

Baseline Duration are currently set, but are approximate values. The baseline values will be redefined after 5 round of mesuaring. Once the baseline is redefined, the team wil set KPI’s for all steps.  
At a minimum one high over KPI will be generated and used in Obeya to give an overview of the measurements. This will be used to steer one the process highover.

## Improvement process

The Teams will sit together to review the current process and KPI’s go over the lessens learned and review outliers to see what we can learn from them. This should happen at least every month in the beginning phases.

Once a value is below the set KPI, might it during the review or escalated by the team the following process should be followed to assure improvement takes place.