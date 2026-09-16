---
id: confluence:1205075969
source: confluence
type: page
space: TC
title: I. KPI / Metrics Layer Research Proposal
author: Panji Y. Wiwaha
date: '2026-05-20'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#2.-Problem-Statement
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#3.-Conceptual-Architecture-%E2%80%94-The-Five-Layers
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#4.-The-KPI-Hypercube-%E2%80%94-A-Universal-Mental-Model
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#5.-Use-Case-Analysis
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#6.-The-Grain-Problem-%E2%80%94-The-Most-Critical-Design-Decision
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#7.-The-Two-KPI-Computation-Patterns
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#8.-Design-Principles
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#9.-Scientific-Foundations
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#10.-Industry-Validation
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#11.-Counterarguments-and-Limitations
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#12.-References
---
# I. KPI / Metrics Layer Research Proposal

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969  

## Content

# **KPI / Metrics Layer — Research Proposal**

**Project:** Teqplay Data Platform KPI  
**Domain:** Maritime Port Intelligence  
**Status:** Research & Design Phase  
**Date:** May 2026

---

## **Table of Contents**

1. Preface
2. [Problem Statement](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#2.-Problem-Statement)
3. [Conceptual Architecture — The Five Layers](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#3.-Conceptual-Architecture-%E2%80%94-The-Five-Layers)
4. [The KPI Hypercube — A Universal Mental Model](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#4.-The-KPI-Hypercube-%E2%80%94-A-Universal-Mental-Model)
5. [Use Case Analysis](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#5.-Use-Case-Analysis)
6. [The Grain Problem — The Most Critical Design Decision](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#6.-The-Grain-Problem-%E2%80%94-The-Most-Critical-Design-Decision)
7. [The Two KPI Computation Patterns](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#7.-The-Two-KPI-Computation-Patterns)
8. [Design Principles](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#8.-Design-Principles)
9. [Scientific Foundations](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#9.-Scientific-Foundations)
10. [Industry Validation](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#10.-Industry-Validation)
11. [Counterarguments and Limitations](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#11.-Counterarguments-and-Limitations)
12. [References](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal#12.-References)

## **1. Preface**

This document proposes a conceptual design for a KPI/Metrics Layer atop the existing Teqplay Data Mart. The layer supports high-performance analytical queries for REST and Postgres API consumers at global maritime scale, covering multiple business use cases such as port activity, berth occupancy, operational efficiency, and trade flow analysis.

The core thesis is: a KPI layer is not a transformed copy of existing fact tables but a library of pre-computed answers to known question shapes. Every design decision—grain, dimensions, metrics, computation pattern—must derive from a precise understanding of which questions to answer, at what granularity, and with which filters.

The proposed architecture is grounded in E.F. Codd's relational model (1970), Codd's OLAP rules (1993), Kimball's dimensional modeling theory (1996–2013), and the convergent findings of Lambda, Kappa, and Medallion data architectures developed independently between 2011 and 2020. It is validated by published engineering implementations at Airbnb, Uber, LinkedIn, and Stripe between 2019 and 2023.

## **2. Problem Statement**

### **2.1 The Current State**

The current data platform produces atomic fact tables (`fact_port_visit`, `fact_berth_visit`, `fact_ship_to_ship_transfers`) and a limited set of daily aggregate tables (`fact_port_calls`, `fact_port_performance_analytics`). Ship dimension attributes — specifically `cargo_type` and `dwt` — reside in `dim_ship`, not in the fact tables.

### **2.2 The Gap**

A representative API query requirement is:

> *Return the* `visits_count` *for a specific* `period` *at port* `unlocode` *for ships where* `cargo_type` *is 'Tanker' and* `DWT` *falls within a range.*

Currently, answering this requires a runtime JOIN between `fact_port_visit` and `dim_ship`. At global scale with worldwide port data, this JOIN is costly, has unpredictable latency, and yields results that vary depending on the last update of `dim_ship`.

### 2.3 The Broader Risk

Without a dedicated KPI layer, teams and API consumers compute identical metrics differently. Booking conversion at Airbnb was calculated in seven ways across seven teams before Minerva was built. Trip counts at Uber yielded contradictory A/B test results. Port visit counts at Teqplay will face similar entropy as the API surface expands.

The issue is not just performance. It is **metric consistency**: ensuring that `visits_count` has the same meaning across contexts, is computed identically from the same source, and has the same granularity.

## **3. Conceptual Architecture — The Five Layers**

The proposed KPI architecture comprises five conceptual layers. These layers are not novel; they represent the convergent conclusion of three independently developed architectural patterns—Lambda (Marz, 2011), Kappa (Kreps, 2014), and Medallion (Databricks, 2020)—all of which independently reached the same structural separation.

### Layer 0 — Raw Atomic Events

The immutable foundation contains one row per discrete business event. In the Teqplay context, these existing fact tables are: `fact_port_visit`, `fact_berth_visit`, `fact_anchor`, `fact_pilot`, `fact_bunkering`, and `fact_ship_to_ship_transfers`.

This layer must not be queried directly by the API. It serves as the auditable, complete record of all events. In Lambda Architecture, this is the Batch Layer; in Medallion terms, Bronze.

**Key property:** Rows exist only when events occur. A berth with no ships on a given day has no row here. This absence is acceptable at this layer but becomes an issue at Layer 2 for asset-centric KPIs, addressed in Section 7.

### Layer 1 — Enriched Events

The context resolution layer handles JOIN operations between events and dimensions, performing them **once, at write time**, rather than at every query.

In the Teqplay context, this layer embeds ship attributes (`cargo_type`, `dwt_bucket`, `ship_category`) and location hierarchy (`berth → terminal → port → country`) into each event row during processing. In Medallion terms, this corresponds to Silver.

**The critical principle:** Ship metadata changes over time. A vessel reclassified from 'General Cargo' to 'Tanker' should reflect its classification at the visit time, not its current one. Resolving context at write time automatically enforces this historical accuracy.

### Layer 2 — Time Spine (for asset-centric KPIs only)

A complete calendar of all asset-period combinations. This layer is required only for asset-centric KPIs where the absence of events is meaningful.

For berth occupancy, a berth exists 24 hours daily. If there are no ship visits on Tuesday, the occupancy rate will be 0%, which is not uncommon. The time spine is a cross-join of all berths against all calendar days. Event data is LEFT JOINed onto it. Without this spine, idle days disappear from the dataset, preventing accurate occupancy rate calculation.

In DBT, this concept is formalized as the `time_spine` model, required for any period-over-period or occupancy metric calculation.

### Layer 3 — KPI Tables (the pre-computation layer)

One table per analytical subject, each with a declared grain. API consumers query this layer directly. Queries require no JOINs or dimension lookups. A single index scan on a narrow, pre-aggregated table returns results in sub-millisecond time.

Each KPI table addresses a specific business question category. The subjects proposed for Teqplay's maritime domain appear in Section 5. In Medallion terms, this corresponds to Gold.

### Layer 4 — Metric Registry (governance layer)

A lightweight metadata table or configuration store records each metric's definition: its name, subject table, column name, unit of measure, computation method, data owner, and any benchmark or threshold values.

This layer does not perform computations. Its purpose is governance—ensuring that `visits_count` has a consistent meaning and that new KPI layer consumers can discover available metrics without reading source code. This concept was independently developed at Airbnb (Minerva metric definitions in YAML), Uber (Databook metric registry), and DBT Labs (MetricFlow semantic layer definitions).

## **4. The KPI Hypercube — A Universal Mental Model**

Each KPI represents a cell in a multi-dimensional hypercube, explaining the necessity of certain design decisions.

E.F. Codd formally described this hypercube in his 1993 white paper *"Providing OLAP to User-Analysts: An IT Mandate"*, defining OLAP operations—Slice, Dice, Drill-Down, Roll-Up, and Pivot—as actions on a multi-dimensional data space. A REST API query is a Dice operation: it fixes multiple axes to specific values and returns the measure in the resulting cell.

The hypercube has five axes:

**Axis 1 — WHERE (Geography).** The event or asset location. In maritime terms: berth, terminal, port, country, region. These form a natural hierarchy; queries can operate at any level and roll up or drill down through it.

**Axis 2 — WHEN (Time Period).** The time window for computing the metric. In maritime terms: day, week, month, quarter, year. The time-axis grain is a key design choice for the KPI table.

**Axis 3 — WHO (Actor Properties).** Properties of the actor in the event. In maritime terms: vessel type, cargo type, DWT class, flag state, shipping line. These must be low-cardinality for practical KPI dimensions. A raw `ship_id` cannot be a KPI dimension, but `cargo_type` with ten distinct values can.

**Axis 4 — WHAT (Event Subject).** The activity type is measured. In maritime terms: port visit, berth occupancy, anchoring wait, ship-to-ship transfer, bunkering event. This axis determines which KPI table the query routes to.

**Axis 5 — THE MEASURE.** The numerical value fills each cell. Four categories exist: count measures (visits, unique ships), duration measures (avg stay hours, avg wait hours), rate measures (occupancy %, utilization %), and volume measures (total DWT handled, cargo ops count).

## **5. Use Case Analysis**

Use cases are the entry point for every design decision in the KPI layer. Before any table is designed, any grain is declared, or any metric is named, the use case must be fully described in terms of its subject, filters, time window, and metric type. The following four use cases are proposed as the initial scope.

### 5.1 Port Activity (Port Calls / Completed Visits)

**Business question:** *How many ships visited port X in period Y, broken down by cargo type and vessel size class?*

**Subject:** The completed port visit. A visit begins when a ship enters the port area and ends when it departs. Only completed visits — those with both a start and an end timestamp — are included in this KPI. Incomplete or in-progress visits are excluded.

**Grain:** One row per combination of port × time period × vessel type × cargo type × DWT bucket. This is the minimum grain required to answer the representative query described in Section 2.2, where `cargo_type = 'Tanker'` and `DWT` within a range are both filter dimensions.

**Key dimensions:**

* Port UNLOCODE (*WHERE*)
* Period start date and period type — daily, monthly, yearly (*WHEN*)
* Vessel type — SEA\_VESSEL, BARGE (*WHO*)
* Cargo type — Tanker, Dry Bulk, Container, General Cargo, etc. (*WHO*)
* DWT bucket — Handysize, Handymax, Panamax, Aframax, Suezmax, VLCC (*WHO*)

**Key metrics:**

* `visits_count` — total completed port visits in the period
* `unique_ships_count` — distinct ships that visited (not double-counted for multiple visits)
* `avg_turnaround_time_hours` — average total time from port entry to departure
* `avg_wait_before_berth_hours` — average pre-berth waiting time (anchor + slow-moving)
* `avg_moored_duration_hours` — average time actively moored at a berth
* `avg_cargo_operation_duration_hours` — average time cargo operations were active
* `total_cargo_operations_count` — total number of cargo operations across all visits

**Computation pattern:** Event-centric (Kimball Transaction Fact Table, Type 1). Rows exist only when visits occur. No time spine required. The computation is a GROUP BY aggregation over enriched port visit events within the period, filtered to completed visits.

**DWT bucketing rationale:** Raw DWT values (continuous double precision floats) cannot be efficiently indexed for range queries. Pre-bucketing into named size classes—aligned with IMO and industry vessel classification conventions—converts a float range filter into an equality lookup, which B-tree indexes handle in O(log n). Kimball describes this technique as "banding dimensions" in The Data Warehouse Toolkit (2013), Chapter 5.

### 5.2 Berth Occupancy (Infrastructure Utilization)

**Business question:** *What percentage of time was berth X occupied during period Y, and how does this vary by the cargo type of visiting ships?*

**Subject:** The berth as a physical asset — not the ship visit. This is the fundamental structural difference from Use Case 5.1. Here, the unit of observation is the berth itself, and time passes whether a ship is present or not.

**Grain:** One row per combination of berth × calendar day. Monthly and yearly views are derived by aggregating daily rows — the daily grain is the minimum that preserves the ability to detect peak utilization days or idle stretches.

**Key dimensions:**

* Berth ID (*WHERE* — the physical asset)
* Terminal ID (*WHERE* — parent of berth)
* Port UNLOCODE (*WHERE* — parent of terminal)
* Calendar date (*WHEN*)

**Key metrics:**

* `occupied_hours` — total hours during which a ship was moored at this berth on this day
* `idle_hours` — `24 - occupied_hours` (this is meaningful data, not an absence of data)
* `occupancy_rate` — `occupied_hours / 24.0`, expressed as a ratio between 0.0 and 1.0
* `vessels_served_count` — number of distinct ship visits that used this berth on this day
* `total_dwt_handled` — sum of DWT of all ships that used this berth on this day
* `dominant_cargo_type` — the cargo type most frequently handled on this day

**Computation pattern:** Asset-centric (Kimball Periodic Snapshot Fact Table, Type 2). A time spine is mandatory. The computation begins with a cross-join of all active berths against all calendar days within the computation window. Berth visit event data is LEFT JOINed onto this spine. Days with no ship visits produce a row with `occupied_hours = 0` and `occupancy_rate = 0.0`, not a missing row.

**Critical distinction from Use Case 5.1:** If you attempt to compute berth occupancy using only event data (without the time spine), any day with zero ship visits produces no row. When you then sum `occupied_hours` over a month and divide by total days, the denominator comes from counting rows — not from the true number of days in the month. The result will overstate occupancy on any port with idle days. This is a correctness error, not a performance issue.

### 5.3 Operational Efficiency (Waiting Time and Congestion)

**Business question:** *How long do ships wait before accessing a berth, and how does this vary by port, vessel type, and period?*

**Subject:** The waiting phase of a port call — the time between a ship arriving in the port area (or EOS entry) and the moment it is moored at a berth. This includes anchor time, slow-moving/drifting time, and any holding patterns before berth assignment.

**Grain:** One row per combination of port × time period × vessel type. Cargo type and DWT bucket can be added as dimensions if the API requires filtering at that level.

**Key metrics:**

* `avg_wait_before_berth_hours` — average of `before_visit_anchor_duration + total_slowmoving_duration_arrival`
* `avg_anchor_duration_hours` — isolated anchor wait time
* `avg_pilot_response_hours` — time between pilot request and pilot on board
* `p95_wait_hours` — 95th percentile wait time (identifies congestion outliers)
* `congestion_index` — ratio of wait time to total turnaround time (0.0–1.0)

**Computation pattern:** Event-centric (Kimball Transaction Fact Table, Type 1). Aggregates over completed port visits with non-null wait components.

### 5.4 Trade Flow (Origin-Destination Connectivity)

**Business question:** How many ships arrived at port X from port Y in period Z, and what cargo types are dominant on that route?

**Subject:** The voyage leg — the movement from a previous port to the current port. The `prev_port_unlocode` field in `fact_port_visit` provides the origin.

**Grain:** One row per combination of origin port × destination port × time period × cargo type.

**Key metrics:**

* `route_calls_count` — number of vessel calls on this origin-destination pair in the period
* `dominant_cargo_type` — most frequent cargo type on this route
* `unique_ships_count` — distinct ships that operated on this route

**Computation pattern:** Event-centric (Kimball Transaction Fact Table, Type 1). Requires that `prev_port_unlocode` be populated, limiting coverage to visits where the previous port is known.

### 5.5 Framework for Future Use Cases

Every new use case that arrives must be evaluated through the same five questions before any table design begins:

1. **What is the subject?** The physical or logical thing being measured.
2. **What is the grain?** One row in this KPI table represents exactly what combination of dimensions?
3. **Is it event-centric or asset-centric?** Does idle time need to be represented? If yes, a time spine is required.
4. **What are the dimensions?** Every dimension must have a bounded, low cardinality.
5. **What are the metrics?** Each metric must have a type (count, duration, rate, volume), a unit, and a consistent computation definition.

If the grain of a new use case is shared with an existing KPI table, add columns to that table. If the grain is new, create a new table. Never mix grains in a single table.

## **6. The Grain Problem — The Most Critical Design Decision**

The grain of a table is the precise statement of what one row represents. Kimball's first law of dimensional modeling is: *"The grain must be declared before choosing dimensions or facts."* This is not a guideline — it is a constraint. Choosing dimensions before the grain produces tables that are ambiguous, unjoinable, or that silently produce wrong answers.

### 6.1 Why Grain Errors Are Silent

A grain error does not raise an exception. A query on a table with mixed or undeclared grain returns a number that appears plausible and may approximate the correct value in typical cases. The error emerges in edge cases—ports with high activity, days spanning midnight across time zones, berths used by multiple ships simultaneously—where the undeclared grain causes double-counting or over-averaging.

This error type is the most dangerous: numerically plausible, never alerting, and silently contaminating downstream decisions.

### 6.2 The Grain Decision for Each KPI Table

| KPI Table | Declared Grain | Row Count Example |
| --- | --- | --- |
| `kpi_port_activity` | 1 row per port × period × vessel\_type × cargo\_type × dwt\_bucket | ~500K rows/year for global coverage |
| `kpi_berth_occupancy` | 1 row per berth × calendar day | ~365 × active berth count |
| `kpi_operational_efficiency` | 1 row per port × period × vessel\_type | ~50K rows/year |
| `kpi_trade_flow` | 1 row per origin × destination × period × cargo\_type | ~2M rows/year (globally) |

### 6.3 The Consequence of Mixing Grains

Suppose `kpi_port_activity` is designed with grain: `port × period` (omitting `cargo_type` and `dwt_bucket`). A query for `cargo_type = 'Tanker'` must then be answered at runtime with a WHERE clause against a table that was not built to support it. The query returns the correct count for that period — but it is now doing runtime aggregation from a pre-aggregated table, which is not possible without also storing the underlying data. The pre-aggregation provides no benefit. The table is used as a fact table, not a KPI table.

The only solution is to declare the grain at the finest level of detail that any API consumer will ever need, then build the KPI table at that grain from the start.

## **7. The Two KPI Computation Patterns**

All KPI metrics in the maritime domain, and in any domain, reduce to one of two computation patterns. Understanding which pattern applies to a given use case determines the entire technical implementation — the table structure, the presence or absence of a time spine, the Airflow DAG logic, and the SQL template used.

### 7.1 Pattern A — Event Aggregation (Event-Centric)

**When to use:** The subject of the KPI is an event (a visit, a transfer, an anchor). Idle periods are not meaningful — a day with no port calls is simply not in scope.

**Computation:**

wide760SELECT
port\_unlocode,
date\_trunc('month', completion\_date) AS period\_start,
vessel\_type,
cargo\_type,
dwt\_bucket,
COUNT(\*) AS visits\_count,
COUNT(DISTINCT ship\_id) AS unique\_ships\_count,
AVG(total\_turnaround\_hours) AS avg\_turnaround\_time\_hours
FROM enriched\_port\_visit
WHERE completion\_date IS NOT NULL
AND completion\_date >= :period\_start
AND completion\_date < :period\_end
GROUP BY 1, 2, 3, 4, 5

**Key property:** If no visits occurred for a given combination of dimensions in a period, no row is produced. This is correct behavior for event-centric KPIs.

### 7.2 Pattern B — Time Spine Join (Asset-Centric)

**When to use:** The subject of the KPI is an asset (a berth, a quay, a terminal). The asset exists in every period regardless of activity. Idle periods are data, not gaps.

**Computation (conceptual):**

wide760-- Step 1: Build the time spine
WITH spine AS (
SELECT berth\_id, calendar\_date
FROM dim\_berth CROSS JOIN dim\_date
WHERE dim\_date.calendar\_date BETWEEN :period\_start AND :period\_end
AND dim\_berth.is\_active = TRUE
),
-- Step 2: Aggregate events per berth per day
daily\_activity AS (
SELECT
berth\_id,
DATE(moored\_start) AS activity\_date,
SUM(moored\_duration\_hours) AS occupied\_hours,
COUNT(\*) AS vessels\_served\_count
FROM enriched\_berth\_visit
WHERE moored\_start >= :period\_start
GROUP BY 1, 2
)
-- Step 3: LEFT JOIN so idle days get occupied\_hours = 0
SELECT
spine.berth\_id,
spine.calendar\_date,
COALESCE(daily\_activity.occupied\_hours, 0) AS occupied\_hours,
COALESCE(daily\_activity.occupied\_hours, 0) / 24.0 AS occupancy\_rate,
24.0 - COALESCE(daily\_activity.occupied\_hours, 0) AS idle\_hours,
COALESCE(daily\_activity.vessels\_served\_count, 0) AS vessels\_served\_count
FROM spine
LEFT JOIN daily\_activity
ON spine.berth\_id = daily\_activity.berth\_id
AND spine.calendar\_date = daily\_activity.activity\_date

**Key property:** The LEFT JOIN guarantees that every berth × day combination produces a row, even if `occupied_hours = 0`. This is the only correct way to compute occupancy rates when idle periods must be distinguishable from missing data.

## **8. Design Principles**

The following six principles govern every decision in the KPI layer. They are derived from the scientific foundations in Section 9 and the industry evidence in Section 10.

### Principle 1 — Declare the Grain First

Before naming any column, write the table's grain as a complete English sentence: "One row in this table represents one [subject] per [time period] per [dimension 1] per [dimension 2]." If you cannot write this sentence, do not design the table.

*Source: Kimball & Ross (2013), Chapter 1, p. 18 — "Declaring the grain is the pivotal step in a dimensional design."*

### Principle 2 — Never Mix Grains

A KPI table must have a single grain. Adding a column meaningful only at a coarser grain (e.g., a monthly total column in a daily grain table) violates this rule. This creates a table where some rows require knowledge of which columns apply to which grain for correct interpretation.

### Principle 3 — Resolve Context at Write Time

Every join between a fact and a dimension — ship attributes, location hierarchy, period classification — must happen at ETL time (when the KPI is computed), not at query time (when the API request arrives). This principle has two consequences: (1) query latency becomes a single-table scan; (2) historical accuracy is preserved, because ship attributes are frozen as of the visit date, not overwritten by current dimension values.

### Principle 4 — Represent Idle Time Explicitly (for asset-centric KPIs)

Any KPI measuring the utilization or availability of a physical asset must use the time spine pattern. A missing row must never be interpreted as "zero activity." It must be represented as a row with explicit zero values, so that the distinction between "zero activity" and "data not available for this period" is unambiguous.

### Principle 5 — Low Cardinality for All Dimensions

Every dimension column in a KPI table must have bounded, low cardinality — typically fewer than 50 distinct values. High-cardinality attributes (ship ID, IMO number, MMSI) cannot serve as KPI dimensions because they prevent effective pre-aggregation. They must be bucketed, classified, or replaced by categorical representations before entering the KPI layer.

*Source: Kimball & Ross (2013), Chapter 5 — "Banding a continuous fact into discrete ranges."*

### Principle 6 — Single Source of Truth per Metric

Each metric must have exactly one definition, stored in exactly one place (the metric registry), computed by exactly one process (the KPI refresh DAG), from exactly one source (the enriched event layer). Any deviation from this — computing `visits_count` in two different DAGs, or defining `avg_turnaround_hours` differently for different API endpoints — is a metric consistency violation that will eventually produce contradictory outputs.

*Source: Airbnb Engineering Blog (2021) — Minerva was built specifically because this principle was violated in production, with 7 divergent definitions of the same metric across 7 teams.*

## **9. Scientific Foundations**

The architecture described in this document is not a design preference or an engineering opinion. It is derived from three independent lines of evidence — mathematical theory, applied data engineering, and convergent systems architecture — that all point to the same structural conclusions.

### 9.1 Mathematical and Theoretical Foundation — E.F. Codd (1970, 1993)

E.F. Codd's contributions are the deepest foundation of the entire proposal.

**The Relational Model (1970).** In *"A Relational Model of Data for Large Shared Data Banks"* (ACM Communications, Vol. 13, No. 6), Codd proved that every relation (table) must have a key that uniquely identifies each tuple (row). This key is the mathematical equivalent of what Kimball later named the *grain* in dimensional modeling. The grain is not a convention that data engineers invented for convenience — it is a formal mathematical requirement of the relational model. A table without a grain is a table without a key, which Codd proved cannot be correctly queried or maintained.

**The OLAP 12 Rules (1993).** In *"Providing OLAP to User-Analysts: An IT Mandate"* (E.F. Codd & Associates, commissioned by Arbor Software), Codd enumerated 12 requirements for OLAP systems. Rule 4 — *"Uniform Reporting Performance"* — states that OLAP reporting performance must not degrade as the number of dimensions or database size increases. This rule is the formal mandate for pre-aggregation. It is mathematically impossible to satisfy Rule 4 if KPIs are computed at query time from atomic fact tables at global scale. The pre-computation layer is not an optimization — it is the only architecture that can satisfy Codd's Rule 4.

The five OLAP operations Codd defined — Slice, Dice, Drill-Down, Roll-Up, and Pivot — map directly onto the five axes of the KPI Hypercube described in Section 4. The Hypercube mental model is a direct re-expression of Codd's multi-dimensional data space in domain-specific terms.

### 9.2 Applied Engineering Science — Ralph Kimball (1996–2013)

Kimball operationalized Codd's abstract theory into a concrete engineering practice that has been empirically validated across hundreds of enterprise data warehouses over 30 years.

**The Three Fact Table Types.** In *"The Data Warehouse Toolkit"* (Wiley, 1st ed. 1996, 3rd ed. 2013), Kimball identified that all analytical data falls into one of three structural types based on the relationship between events, assets, and time. These are not stylistic categories — they are mathematically distinct:

* **Transaction Fact Table (Chapter 3):** One row per discrete event. Measures are facts about that event. Idle time is structurally unrepresentable. This is the correct model for port calls, operational events, and trade flow.
* **Periodic Snapshot Fact Table (Chapter 4):** One row per asset per regular time period. Every period is represented, including idle periods. This is the correct model for berth occupancy, quay utilization, and any KPI where the denominator is time-in-existence, not event count.
* **Accumulating Snapshot Fact Table (Chapter 11):** One row per entity lifecycle, updated as milestones are reached. This is the correct model for tracking a port visit from arrival through pilot, berth, cargo operations, and departure — measuring the duration between each milestone.

**The Factless Fact Table (Chapter 11).** Kimball also formally described the factless fact table — a table with no numeric measures that records coverage: which assets were active on which days. This is the structural equivalent of the time spine. The time spine is not a trick or a workaround; it is a recognized formal construct in dimensional modeling, named and described by Kimball 28 years ago.

**The Bus Matrix.** Kimball's Dimensional Bus Architecture specifies that all KPI tables sharing the same conformed dimensions — the same definitions of `vessel_type`, `cargo_type`, `period` — can be queried together in a single API layer without requiring cross-table JOINs. The shared dimension vocabulary described in Section 4 is the bus matrix for the maritime KPI layer.

### 9.3 Convergent Systems Architecture (2011–2020)

Three independent architectural frameworks, developed for different companies and different problem domains, all arrived at the same three-tier structure.

**Lambda Architecture (Marz & Warren, 2011).** Developed at Twitter for large-scale data processing. The three layers — Batch Layer (immutable raw data), Speed Layer (real-time incremental updates), and Serving Layer (pre-computed views) — correspond directly to Layer 0 (raw events), the streaming ingest pipeline, and Layer 3 (pre-computed KPI tables) in the proposed architecture.

**Kappa Architecture (Jay Kreps, 2014).** Developed at LinkedIn as a simplification of Lambda, arguing that the Batch Layer and Speed Layer can be unified as a single reprocessable stream. The Serving Layer — pre-computed outputs queryable at low latency — remains identical. Kappa validates that the serving/KPI layer is not an artifact of batch processing; it is necessary regardless of whether the upstream is batch or streaming.

**Medallion Architecture (Databricks, 2020).** Developed for Apache Spark and Delta Lake, the Bronze (raw), Silver (enriched), and Gold (serving) layers correspond to Layer 0, Layer 1, and Layer 3 of the proposed architecture, respectively. This framework was developed independently of Kimball yet converged on the same three-tier structure.

**The significance of convergence.** Lambda, Kappa, and Medallion were built for Twitter, LinkedIn, and Databricks' customers, respectively. They targeted different scales, technologies, and business domains. All three independently reached the same structural conclusion: a pre-computed serving layer atop enriched events atop raw immutable data. When independent engineering teams converge on the same architecture without coordination, it represents the strongest architectural validation outside a controlled experiment.

## **10. Industry Validation**

The following case studies demonstrate that the proposed architecture addresses a real, recurring, and costly problem in data engineering — not a theoretical concern.

### 10.1 Airbnb — Minerva (2021)

**The problem.** Before Minerva, Airbnb's data engineering teams discovered that booking conversion rate — their primary business metric — was computed in seven different ways across seven different teams. Each team had a slightly different definition: some included same-day cancellations, some did not; some counted guest-initiated bookings only, some included host-initiated; some computed monthly, some weekly. When executives compared dashboards, the numbers contradicted each other. Engineers spent an estimated 20% of their time reconciling metric definitions instead of building new capabilities.

**The solution.** Minerva is a centralized metric platform built on three components: (1) a YAML-based metric registry where each metric has exactly one definition authored by one team; (2) a pre-computation layer that materializes all metrics at the declared grain daily; (3) an API that routes all metric queries to the pre-computed layer. The YAML registry is the implementation of Principle 6 (Single Source of Truth per Metric).

**The outcome.** Published in the Airbnb Engineering Blog (*"Minerva — How Airbnb Achieves Metric Consistency at Scale"*, January 2021). Metric reconciliation time was eliminated. Dashboard load times dropped from seconds to milliseconds. New metrics could be added and immediately available to all consumers without any API changes.

**Relevance to this proposal.** The metric consistency problem Airbnb faced is a structural consequence of not having a metric layer, not a consequence of scale. The problem emerges at any organization where multiple teams independently query the same fact tables to answer the same questions. Teqplay will face this as the API surface grows.

### 10.2 Uber — UMetric / Databook (2019)

**The problem.** Uber's data teams found that trip count — the most fundamental Uber metric — produced contradictory results in A/B test analyses. Two teams running the same experiment on the same date range, querying the same underlying event tables, produced different numbers because they applied different filtering rules (canceled trips, pool vs. solo, surge pricing periods). The contradictory results led to incorrect product decisions being shipped.

**The solution.** UMetric (later integrated into Databook) formalized metric definitions with mandatory grain declarations, required dimension filters to be specified per metric, and materialized all metrics as pre-computed tables. Published in Uber Engineering Blog (*"Databook: Turning Big Data into Knowledge at Uber"*, 2019).

**Relevance to this proposal.** Trip count at Uber is structurally identical to `visits_count` at Teqplay — both count completions of a multi-stage process (trip start → end vs. ship arrival → departure), both are filtered by actor properties (vehicle type vs. vessel type), and both are computed over time periods. The solution is also identical: pre-declared grain, single definition, pre-computation.

### 10.3 LinkedIn — Apache Calcite / Metrics Layer (2016–2020)

**The problem.** LinkedIn's analytics infrastructure served hundreds of internal dashboards. As the number of dashboards grew, each team began writing its own SQL against shared fact tables. The same metric computed with slightly different SQL produced slightly different numbers. Data quality investigations repeatedly traced errors to inconsistent metric implementations rather than upstream data problems.

**The solution.** LinkedIn invested in a formal semantic layer on top of its data warehouse, in which metric SQL was registered once and reused. This later influenced the design of Apache Calcite's semantic query model and contributed to the industry push toward semantic layers as a first-class architectural component.

### 10.4 DBT Labs — MetricFlow (2022–2024)

**The significance.** dbt MetricFlow's introduction of the `time_spine` model as a first-class concept in the dbt semantic layer (documented at <http://docs.getdbt.com> ) formalizes the time spine concept in mainstream data engineering tooling. Before MetricFlow, the time spine was known to experienced Kimball practitioners but was not part of any widely used framework. MetricFlow's inclusion of it confirms that the pattern is now considered a standard requirement for any metric platform, not an advanced technique.

The MetricFlow YAML specification for a metric requires: a `type` (simple, ratio, cumulative, or derived), a `measure` (the aggregation), a `dimensions` list (the filtering axes), and a `time` declaration (the grain). This is a direct implementation of the Grain Principle and the Hypercube model in a production-grade, open-source tool.

### 10.5 Stripe — Sigma / Unified Metrics Layer (2023)

**The problem.** Stripe processes millions of transactions daily across dozens of payment products. Different product teams computed payment success rate differently — by card type, by merchant, by geography — producing incompatible KPIs that made cross-product comparison impossible.

**The solution.** Stripe built a unified metric layer in which each metric definition includes its grain, computation logic, and authorized dimensions. Consumers query the metric layer by name, not by SQL. Published in Stripe's engineering blog (*"How Stripe builds data products"*, 2023).

**Relevance to this proposal.** The `authorized dimensions` concept in Stripe's metric layer maps directly to Principle 5 (Low Cardinality for All Dimensions)—dimensions that are not declared for a metric cannot be used to filter it, preventing consumers from accidentally creating ad hoc sub-grains that break metric consistency.

## **11. Counterarguments and Limitations**

Intellectual honesty requires stating where this proposal could be wrong, what assumptions it depends on, and under what conditions the architectural choices should be revisited.

### 11.1 Counterargument — "Modern Columnar Databases Make Pre-Aggregation Unnecessary"

**The claim.** Columnar databases — ClickHouse, DuckDB, BigQuery, Snowflake — execute vectorized scans over billions of rows in seconds without pre-aggregation. Pre-computing KPI tables is only necessary because PostgreSQL is a row-oriented database. If Teqplay migrates to a columnar warehouse, the KPI layer is redundant.

**When this argument is correct.** If the target database is columnar, and query patterns are highly variable and unpredictable, and sub-second (not sub-10ms) latency is acceptable, then runtime aggregation over enriched fact tables is architecturally valid without a pre-computation layer.

**Why does it not apply to the current Teqplay context?** Teqplay currently operates on PostgreSQL for both OLTP (streaming pipeline) and OLAP (API queries). PostgreSQL is a row-oriented database. A full-table sequential scan of `fact_port_visit` at global scale, with a runtime JOIN to `dim_ship`, will not achieve sub-10ms p99 latency regardless of the indexing strategy. Furthermore, the API's query patterns are predictable — the filter dimensions (`cargo_type`, `dwt_bucket`, `period`, `unlocode`) are known in advance. Pre-aggregation is the correct response to a known, stable query pattern.

**The condition for revisiting.** If Teqplay migrates the OLAP workload to a columnar system (e.g., Snowflake, DuckDB, or ClickHouse), and if API latency requirements relax to sub-second rather than sub-10ms, then the KPI pre-computation layer can be replaced with a semantic layer (e.g., dbt MetricFlow on Snowflake) that generates SQL at query time. The layer model remains identical; the execution mechanism changes.

### 11.2 Counterargument — "One Wide Fact Table Is Simpler"

**The claim.** Rather than maintaining multiple KPI tables with different grains, a single wide fact table with all attributes — ship properties, location hierarchy, period, all metrics — eliminates the need to know which KPI table to query. This is the "wide table" pattern advocated by anti-Kimball practitioners and data vault proponents.

**When this argument is correct.** If query patterns are completely unpredictable, if the schema changes frequently, or if the team lacks the bandwidth to maintain multiple tables, a single wide denormalized table is operationally simpler to maintain.

**Why does it create problems at scale?** A single wide table mixing different grains (port-level and berth-level metrics, for example) produces rows that are partially null — berth columns are null on port-level rows and vice versa. This is a grain violation that makes aggregate queries incorrect without case-by-case awareness of which columns apply at which level. The simplicity gained in maintenance is lost in query correctness complexity.

### 11.3 Counterargument — "Use Real-Time OLAP (Apache Druid, Apache Pinot)"

**The claim.** For high-performance analytical queries at scale, use a dedicated real-time OLAP engine—Apache Druid (used by Uber) or Apache Pinot (used by LinkedIn)—instead of Postgres with pre-computed tables. These engines ingest raw events in real time and compute aggregations on the fly with sub-second latency over billions of events.

**When this argument is correct.** If KPIs must be seconds-fresh (updated within seconds of each ship event), if query concurrency is extremely high (thousands of concurrent API consumers), or if the team is willing to operate and maintain a separate OLAP infrastructure.

**Why it does not apply to the current Teqplay context.** The KPI update cadence at Teqplay is daily — daily refresh DAGs are the existing pattern, and no business requirement for real-time KPI freshness has been identified. The operational complexity of running Apache Pinot or Druid (JVM cluster management, Zookeeper/Kafka integration, segment management) is significant and would require dedicated infrastructure expertise. PostgreSQL with pre-computed KPI tables achieves identical query latency for the specific, predictable query patterns at issue, at a fraction of the operational cost.

### 11.4 Counterargument — "dbt MetricFlow Is the Industry Standard Now"

**The claim.** dbt MetricFlow (the dbt semantic layer) is the emerging industry standard for defining and serving metrics. Rather than building a custom KPI layer in Postgres + Airflow, adopt MetricFlow and define metrics in YAML. MetricFlow handles grain, time spine, and dimension vocabulary automatically.

**The partially valid case.** MetricFlow's YAML-based metric definitions directly implement Principle 6 (Single Source of Truth per Metric) and the Hypercube model. If Teqplay adopts dbt as the transformation layer, MetricFlow is a strong candidate for the metric registry (Layer 4).

**The limitation.** MetricFlow generates SQL at query time from semantic layer definitions. It does not pre-compute persistent KPI tables but materializes to Postgres on request or to the configured data warehouse. For sub-10ms REST API latency on PostgreSQL, a pre-materialized KPI table with covering indexes consistently outperforms MetricFlow's query-time SQL generation. MetricFlow is architecturally correct; it is a tool choice, not an architecture choice.

### 11.5 Scope Limitations of This Proposal

This proposal is intentionally scoped to the conceptual and architectural level. The following topics are deferred to implementation-phase documents:

* **DDL specifications** for each KPI table (column types, constraints, index definitions).
* **Airflow DAG design** for the KPI refresh pipeline (partitioned backfill, error handling, dependency on upstream fact tables).
* **Data quality validation** for KPI tables (row count sanity checks, metric drift detection, comparison against source fact tables).
* **API contract definition** (endpoint design, query parameter schema, response format).
* **Metric registry implementation** (whether implemented as a Postgres table, a YAML file, or a third-party tool such as dbt MetricFlow or Atlan).
* **Partitioning strategy** for `kpi_berth_occupancy` given its large row count at daily grain with global berth coverage.

## **12. References**

### Primary Academic References

| Reference | Contribution to This Proposal |
| --- | --- |
| Codd, E.F. (1970). *"A Relational Model of Data for Large Shared Data Banks."* ACM Communications, Vol. 13, No. 6, pp. 377–387. | Formal definition of the relation key, which is the mathematical basis for grain declaration. |
| Codd, E.F. (1993). *"Providing OLAP to User-Analysts: An IT Mandate."* E.F. Codd & Associates (commissioned by Arbor Software Corp.). | The 12 OLAP rules include Rule 4 (Uniform Reporting Performance), which mandates pre-aggregation in OLAP systems. They define Slice, Dice, Drill-Down, Roll-Up, and Pivot—the five operations on the KPI Hypercube. |
| Kimball, R. & Ross, M. (2013). *"The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling."* 3rd Edition. Wiley. | The three fact table types (Transaction, Periodic Snapshot, Accumulating Snapshot). The Factless Fact Table as the time spine foundation. The Dimensional Bus Architecture. Grain as the first design decision. |
| Kimball, R. (1996). *"The Data Warehouse Toolkit."* 1st Edition. Wiley. | Original formulation of dimensional modeling and the fact table taxonomy. |
| Inmon, W.H. (2005). *"Building the Data Warehouse."* 4th Edition. Wiley. | Alternative DWH architectural perspective; the counterpoint to Kimball's bottom-up bus architecture, referenced for completeness. |

### Systems Architecture References

| Reference | Contribution to This Proposal |
| --- | --- |
| Marz, N. & Warren, J. (2015). *"Big Data: Principles and Best Practices of Scalable Real-Time Data Systems."* Manning Publications. | Lambda Architecture — the three-tier (Batch, Speed, Serving) convergent architecture pattern. |
| Kreps, J. (2014). *"Questioning the Lambda Architecture."* O'Reilly Media (blog). Available: <http://radar.oreilly.com> | Kappa architecture confirms the necessity of the pre-computed serving layer regardless of whether the upstream is batch or streaming. |
| Databricks (2020). *"Medallion Architecture."* Databricks Documentation. Available: <http://docs.databricks.com> | Bronze, Silver, Gold three-tier pattern—independent convergence to the same three-layer structure as Lambda and Kappa. |

### Industry Engineering References

| Reference | Contribution to This Proposal |
| --- | --- |
| Airbnb Engineering Blog (January 2021). *"Minerva — How Airbnb Achieves Metric Consistency at Scale."* Available: <http://medium.com/airbnb-engineering> | Primary evidence for the metric consistency problem: 7 divergent definitions of the same metric across 7 teams, 20% engineering time lost to reconciliation. |
| Uber Engineering Blog (2019). *"Databook: Turning Big Data into Knowledge at Uber."* Available: [eng.uber.com](http://eng.uber.com). | Evidence for the grain consistency problem: contradictory A/B test results from divergent trip count definitions. |
| dbt Labs (2022–2024). *"MetricFlow Documentation — Time Spine."* Available: <http://docs.getdbt.com/docs/build/metricflow-time-spine> | Formal inclusion of the time spine as a primary concept in mainstream data tools validates the asset-centric KPI pattern. |
| Stripe Engineering Blog (2023). *"How Stripe Builds Data Products."* Available: <http://stripe.com/blog/engineering> | Evidence supports authorized dimensions as a metric governance mechanism, validating Principle 5 (Low Cardinality for All Dimensions). |
| LinkedIn Engineering Blog (2019). *"Open Sourcing Brooklin: Near Real-Time Data Streaming at Scale."* Available: [engineering.linkedin.com](http://engineering.linkedin.com). | LinkedIn's data infrastructure context for their semantic layer work and Apache Calcite contributions. |

### Database Performance References

| Reference | Contribution to This Proposal |
| --- | --- |
| ClickHouse Inc. (2023). *"ClickHouse Benchmark."* Available: <http://clickhouse.com/benchmark> | Primary source for the counterargument that columnar databases reduce the need for pre-aggregation. Referenced to support the honest limitations in Section 11.1. |
| PostgreSQL Documentation (2024). *"Index Types — B-Tree."* Available: <http://postgresql.org/docs> | Basis for the DWT bucketing rationale in Section 5.1 — B-tree indexes handle equality lookups in O(log n), making bucketed dimensions more efficient than range filters on continuous values. |