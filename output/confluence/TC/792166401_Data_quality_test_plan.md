---
id: confluence:792166401
source: confluence
type: page
space: TC
title: Data quality test plan
author: Darius Wattimena
date: '2026-01-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792166401
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792166401
---
# Data quality test plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792166401  

## Content

# **Purpose & Objectives**

This document defines the tests, monitoring controls, and escalation workflow required to guarantee data quality across the end‑to‑end AIS to data mart pipeline.

Our goals are to:

1. Detect and contain issues as far upstream and as early as possible (“fail fast”).
2. Align every check with one or more of the six DAMA‑UK data‑quality dimensions, Completeness, Uniqueness, Timeliness, Validity, Accuracy, Consistency.
3. Guarantee existing quality when making changes over time.
4. Provide actionable, automated testing and clear ownership of tests.
5. Establish a feedback loop so every incident drives tighter quality checks, better metadata, or improved reference data.

# **Scope**

The plan covers both realtime and backfill (Re‑events) flows, plus the Context‑Mapping Validation environment. Availability of the components required are not in the testplan but are captured by our SLA’s. All core components are captured on our Prio 1 SLA and our datawarehouse and Datamart are currently under Prio 2 SLA.

**Real time**

|  |  |  |  |
| --- | --- | --- | --- |
| **Stage** | **Function** | **Inputs** | **Outputs** |
| Raw AIS Data | Ingest vendor messages | Raw AIS | Parsed AIS at internal Queue |
| Monitoring | Enrich & convert messages to events (Encounter, Area, Stop, etc.) | Raw AIS, CSI, Poma | Event streams |
| VesselVoyage | Aggregate events into Statements‑of‑Fact (SoF); polish jitter | Event streams, CSI and Poma | SoF tables |
| Data Warehouse | Persist CSI, Poma & VesselVoyage data | Source API’s | DW tables |
| Data Mart(s) | Curated facts for BI | DW tables | Fact tables/views |

**Post adding data**

|  |  |  |  |
| --- | --- | --- | --- |
| **Re‑events** | Replay archived AIS through revents AIS‑Engine; merge to VesselVoyage | Archived AIS | Event streams for vesselvoyage |

**Context mapping**

|  |  |  |  |
| --- | --- | --- | --- |
| **Context Mapping Validation** | Test new port/infrastructure mappings end‑to‑end before prod merge | Draft CSI/Poma records | Validation report, by running full revents flow |

## **Data‑Quality Dimensions & KPI Targets**

|  |  |  |  |
| --- | --- | --- | --- |
| **Dimension** | **KPI** | **Target** | **Alert Threshold** |
| **Completeness** | % mandatory fields present per batch | 99,9% | 98% |
| **Uniqueness** | Duplicate per batch | 99,9% | 98% |
| **Timeliness** | End‑to‑end latency (ingest → SoF) | TBD | TBD |
| **Validity** | Schema / rule failures per batch | 99% | 95% |
| **Accuracy** | External reference mismatch (IMO, port code) | TBD | TBD |
| **Consistency** | Daily row‑count deltas between stages | 99,9% | 99% |

KPI’s will be used for a highover metric on those KPI’s in obeya.

## **Product & Responsibilities**

|  |  |  |
| --- | --- | --- |
| **Product** | **Primary Responsibilities** | **Owner** |
| **Raw AIS Data** | Correctness of AIS data source | Core components |
| **Data source** | Context information (Poma & CSI) | Core components (Functionality) & context mapping (Data) |
| **AIS‑Engine** | Event logic, storing data | Core components |
| **VesselVoyage** | Making decisions and finetuning data | Core components |
| **Data warehouse** | Storing source data | Data Platform |
| **Data mart** | Storing fact tables from combined sources | Data Platform |
| **PowerBI dashboard** | Displaying structured data | Data Platform |

## Control Points & Automated Tests

By testing as early as possible in the pipeline, we spend less time hunting for and fixing defects, avoid costly end-to-end re-runs, and give each downstream stage a solid, already-validated foundation on which to build.

### Raw AIS Ingest

* **Schema validation** JSON registry (Validity, Completeness).
* **No Duplicate detection** on identifier + timestamp window (Uniqueness).
* **Latency watermark**: `(ingest_ts – ais_msg_ts)` (Timeliness).
* **Jitter‑polish score:** monitor drop in positional variance (Accuracy).
* **Throughput fluctuation** Data throughput should be higher than predefined values (Consistency).
* **Logical correctness** Data points (order) should be correct (Correctness)

Can be tested earlier:

* none

### Data source

* **Infrastructure completeness:** All required information filled in (Completeness)
* **Ship completeness:** All required ship information filled in (Completeness)
* **Infrastructure correct:** All infrastructure information is correctly mapped (Correctness)
* **CSI correct**: All ship information is correctly updated and recent (Correctness)

Can be tested earlier:

* none

### Monitoring

* **Reference joins** must resolve to valid CSI & Poma IDs (Accuracy).
* **Streaming assertions** enforce not‑nulls, value ranges (Validity).
* **Micro‑service input-output tests** in CI/CD protect event generation contracts (Consistency).
* **Temporal business rules:** No stop before start, no two anchors at the same time ect (Validity, Completeness).
* **Throughput fluctuation** Data throughput should be higher than predefined values (Consistency).

Can be tested earlier:

* **Jitter‑polish score:** monitor drop in positional variance (Accuracy).
* **Infrastructure completeness:** All required information filled in (Completeness)
* **Ship completeness:** All required ship information filled in (Completeness)

### VesselVoyage

* **SoF reconciliation:** record‑count match vs source events (Consistency).
* **SoF Completeness:** All required fields are there (**required fields are TBD**)
* **Visit completeness:** All ships that went into port have a visit (Completeness).
* **input-output tests** in CI/CD protect logic generation contracts (Consistency).
* **Temporal business rules:** order of actions chronologically across different events. (Validity).

Can be tested earlier:

* **Jitter‑polish score:** monitor drop in positional variance (Accuracy).
* **Temporal business rules:** No stop before start, no two anchors at the same time ect (Validity, Completeness).

### Data Warehouse

* **Load completeness check:** row counts vs VesselVoyage (or other sources) snapshot (Completeness).
* **SCD integrity tests:** duplicate natural keys, out‑of‑order updates (Uniqueness, Timeliness).

Can be tested earlier:

* **SoF Completeness:** All required fields are there (**required fields are TBD**)
* **Temporal business rules:** No stop before start, no two anchors at the same time ect (Validity, Completeness).

### Data Marts

* **dbt tests:** `not_null`, `accepted_values`, `relationship` (Validity).
* **Aggregation parity:** mart totals vs source facts within tolerance (Consistency, Accuracy, Completeness).
* **Fact input-output tests** in CI/CD protect event generation contracts (Consistency).

Can be tested earlier:

* **SoF Completeness:** All required fields are there (**required fields are TBD**)
* **Reference joins** must resolve to valid CSI & Poma IDs (Accuracy).
* **Temporal business rules:** No stop before start, no two anchors at the same time ect (Validity, Completeness).

# Feedback loop & **Regression guardrail**

Whenever a KPI reaches the alert threshold the following measures will be taken.

1. The problem is assessed.
2. The priority of said problem is determined.
3. The problem is picked up.
4. The KPI is updated so it also covers the problem.

The following flow diagram illustrates what steps will be taken and questions that will be asked when addressing the KPI alarm:

The owners of the effected component’s are responsible for creating the backlog item and creating tests to cover said KPI as part of the fix. This will ensure that the exact scenario won’t recur.

# Focus first phase

*Raw AIS:*

* *No Duplicate detection on identifier + timestamp window (Uniqueness).*
* *Data throughput should be higher than predefined values (Consistency).*

Internal Datasource:

* All required information filled in (Completeness)

Monitoring:

* Temporal business rules, no end event before start event, no two anchors at the same time ect (Validity).
* Data throughput should be higher than predefined values (Consistency).

Vessel Voyage:

* All required fields are there (Completeness)
* All ships that went into port have a visit (Completeness)

Data warehouse:

* Row counts vs Vessel Voyage snapshot (Completeness).

Data mart:

* Mart totals vs source facts within tolerance (Completeness).
* Fact input-output tests in CI/CD protect event generation contracts (Consistency).

## **Shared completeness of** ***validated*** **data**

### Poma

Port760

* Area (inner area)
* Name
* Display Name
* Unique Unlocode
* Country Code
* EOS containing all areas of a port
* Anchorage (All validated or marked as no Anchorage)
* Pilot boarding place (All validated or marked as no Pilot boarding place)
* Terminals (All validated)
* Berths (All validated)
Terminal760

* ID
* Name
* Cargo Type
* Area
* Mapped to port
* Berths (All validated)
Berth760

* ID
* Name
* Cargo Type
* Mooring Type (quay, jetty, ect) (Only for PTO port ports)
* Area
* Mapped to port
Anchorage760

* ID
* Name
* Area
* Mapped to port
Pilot boarding place760

* ID
* Name
* Area
* Mapped to port

### CSI

Ship760

* ID
* Name
* MMSI
* Category V2 or Role
* Dimensions (Length, Beam)
* DWT (or TEU if Category V2 = Container)

Nice-to-have completeness

* Gross tonnage
* Construction Year
* Flag

### Statement of facts

VesselVoyage Visit760

* Visit has end time
* Port has end time on all
* Sub port has end time on all
PTO Statement of Facts760

* Pilot Inbound encounter (or Pilot area ATD) (above 75 length) or port has no pilot area
* Pilot Outbound encounter (or Pilot area ATA) (above 75 length) or port has no pilot area
* Tug (above 150 length)
* port ata & atd
* eos ata & atd
* stop, defining a visit

### Data warehouse

* Are all the Statement of Facts, Ships and Ports ingested that were requested.

# Specific test cases written down

Core Components: [Core Components test cases](https://docs.google.com/spreadsheets/d/14lhCHbDNMcmBZKVCIpiyqnuLT4xhENncYOuw9bu1y-4/edit?gid=1536383276#gid=1536383276)

Datawarehouse + Datamart: <https://docs.google.com/spreadsheets/d/1JJ2Z3q-NyfFyUg70FJQ6bVYPtJ-uXlj18XpN9VKEZ-8/edit?gid=0#gid=0>