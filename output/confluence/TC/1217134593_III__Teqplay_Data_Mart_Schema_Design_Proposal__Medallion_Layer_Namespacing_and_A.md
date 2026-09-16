---
id: confluence:1217134593
source: confluence
type: page
space: TC
title: 'III. Teqplay Data Mart Schema Design Proposal: Medallion Layer Namespacing
  and Access Control Strategy'
author: Panji Y. Wiwaha
date: '2026-05-21'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#1.-Preface
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#2.-Relationship-to-the-Prior-Proposal
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#3.-The-Three-Schema-Strategy
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#4.-Schema%3A-public-%E2%80%94-Bronze-Layer-(Layer-0
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#5.-Schema%3A-silver-%E2%80%94-Silver-Layer-(Layers-1-and-2
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#6.-Schema%3A-gold-%E2%80%94-Gold-Layer-(Layers-3-and-4
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#7.-Access-Control-Model
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#8.-DDL-Patterns-and-Cross-Schema-References
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#9.-Impact-on-the-Prepare-Database-DAG
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#10.-Design-Principles
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#11.-References
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal?atl_f=PAGETREE
---
# III. Teqplay Data Mart Schema Design Proposal: Medallion Layer Namespacing and Access Control Strategy

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593  

## Content

# **Teqplay Data Mart Schema Design Proposal — Medallion Layer Namespacing**

**Project:** Teqplay Data Platform  
**Domain:** Maritime Port Intelligence  
**Status:** Implementation Design Phase  
**Predecessor Document:** <https://teqplaybv.atlassian.net/wiki/x/AQDURw>   
**Date:** May 2026

---

## Table of Contents

1. [Preface](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#1.-Preface)
2. [Relationship to the Prior Proposal](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#2.-Relationship-to-the-Prior-Proposal)
3. [The Three-Schema Strategy](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#3.-The-Three-Schema-Strategy)
4. [Schema: public — Bronze Layer (Layer 0)](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#4.-Schema%3A-public-%E2%80%94-Bronze-Layer-(Layer-0))
5. [Schema: silver — Silver Layer (Layers 1 and 2)](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#5.-Schema%3A-silver-%E2%80%94-Silver-Layer-(Layers-1-and-2))
6. [Schema: gold — Gold Layer (Layers 3 and 4)](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#6.-Schema%3A-gold-%E2%80%94-Gold-Layer-(Layers-3-and-4))
7. [Access Control Model](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#7.-Access-Control-Model)
8. [DDL Patterns and Cross-Schema References](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#8.-DDL-Patterns-and-Cross-Schema-References)
9. [Impact on the Prepare Database DAG](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#9.-Impact-on-the-Prepare-Database-DAG)
10. [Design Principles](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#10.-Design-Principles)
11. [References](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1217134593/III.+Teqplay+Data+Mart+Schema+Design+Proposal+Medallion+Layer+Namespacing+and+Access+Control+Strategy#11.-References)

## **1. Preface**

This document specifies the physical schema namespacing strategy for the Teqplay Data Mart database, as a direct implementation design follow-up to the KPI Layer Research Proposal. Where the predecessor document established the conceptual five-layer architecture and its scientific foundations, this document translates those concepts into a concrete, deployable PostgreSQL schema layout.

The central proposal is a three-schema model that maps directly onto the Medallion Architecture tiers described in the prior proposal:

* `public` — the existing schema, unchanged. Contains all Bronze-layer dimensional and fact tables that form Layer 0 of the KPI architecture.
* `silver` — a new schema. Contains all intermediate computation tables: the enriched event tables (Layer 1) and the time spine scaffold (Layer 2). These tables are internal to the KPI refresh pipeline and might never be queried directly by API consumers.
* `gold` — a new schema. Contains all final, pre-aggregated KPI tables (Layer 3) and the metric registry metadata tables (Layer 4). This is the only schema that external consumers — REST API clients via PostgREST and BI tools — are authorized to read.

This namespacing strategy serves three purposes beyond architectural clarity. First, it enforces access control at the database level rather than by application-layer convention. Second, it enables PostgREST to expose a single, clean schema to API clients without any server-side filtering logic — the `api_web_anon` role is granted access to `silver` and `gold` only, and the `REVOKE` on `public` ensures the Bronze layer is never reachable from the API surface. Third, it establishes a foundation that survives scope expansion — any future Gold table, whether a KPI table, an export snapshot, or an API response cache, belongs in `gold` without requiring any changes to the PostgREST configuration or the role grants.

## **2. Relationship to the Prior Proposal**

The [KPI Layer Research Proposal](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1205075969/I.+KPI+Metrics+Layer+Research+Proposal?atl_f=PAGETREE) established:

* A five-layer conceptual architecture grounded in Codd's relational model, Kimball's dimensional modeling theory, and the convergent findings of Lambda, Kappa, and Medallion architectures.
* Two computation patterns: Pattern A (event aggregation for event-centric KPIs) and Pattern B (time spine join for asset-centric KPIs such as berth occupancy).
* Four initial KPI subjects: port activity, berth occupancy, operational efficiency, and trade flow.
* A governance model based on a YAML metric registry mirrored to a Postgres metadata table.

This document resolves the single open implementation question from Section 11.5 of that proposal — the physical table organization — by specifying the schema layout, the access control model, the DDL conventions for cross-schema references, and the changes required in the `prepare_database_dag`.

No conceptual decisions in the prior proposal are altered or overridden here. This document is strictly additive.

## **3. The Three-Schema Strategy**

### **3.1 Design Philosophy**

A PostgreSQL schema is a namespace. It is not a security boundary on its own, but it is the unit at which `GRANT` statements operate for bulk access control. Organizing tables by schema means that the permission model can be expressed as three statements — one per schema — rather than as one statement per table. As the KPI layer grows from four KPI tables to twenty, the access control policy remains unchanged.

The schema names chosen — `public`, `silver`, `gold` — are the Medallion Architecture tier names. This choice is deliberate. Naming the intermediate layer `silver` and the final layer `gold` produces an internally consistent naming system. The alternative — naming the final layer `kpi` while keeping `silver` for the intermediate layer — mixes two different naming systems (domain-specific and medallion-tier) within the same database, creating ambiguity for any engineer who joins the team without prior context.

### **3.2 Why Schemas Over Naming Conventions**

The Teqplay Data Warehouse uses a prefix-based naming convention: `stg_` for staging tables, `ods_` for operational data store tables. MART applies the prefixes `dim_` for dimensions and `fact_` for facts. This convention works well and should be retained for existing tables.

However, for the new KPI architecture, schemas provide capabilities that prefixes cannot:

**Access isolation.** A `GRANT SELECT ON ALL TABLES IN SCHEMA gold` statement grants read access to every current and future Gold table in a single operation. With prefix-only naming in a shared `public` schema, there is no equivalent mechanism — each new table requires a separate `GRANT`, and it is easy to forget one.

**PostgREST schema exposure.** PostgREST exposes one or more schemas as its API surface, controlled entirely by the database role model. The `api_web_anon` role is granted `USAGE` and `SELECT` on `silver` and `gold` only, and is explicitly revoked from `public`. PostgREST therefore surfaces exactly the tables that external consumers should see, with no server-side filtering configuration required. If a new KPI table is added to `gold`, it is automatically visible to the API. If a Bronze or Silver table is added to `public`, it is automatically invisible. The access boundary is maintained by the database, not by PostgREST configuration.

**Operational clarity.** A query referencing `silver.enriched_port_visits` is unambiguous about which architectural tier it belongs to without reading any documentation. A query referencing `enriched_port_visit` in the `public` schema is ambiguous until the naming convention is known.

### **3.3 The Three Schemas at a Glance**

| Schema | Medallion Tier | Layers | Contents | Queryable by API? |
| --- | --- | --- | --- | --- |
| `public` | Bronze | Layer 0 | `dim_*`, `fact_*` tables | No — internal pipeline only |
| `silver` | Silver | Layers 1, 2 | Enriched event materialized views, time spine materialized view | No — internal pipeline only |
| `gold` | Gold | Layers 3, 4 | KPI tables, metric registry | Yes — sole API-facing schema |

## **4. Schema: public — Bronze Layer (Layer 0)**

### **4.1 Role and Responsibility**

The `public` schema is the existing Teqplay Data Mart schema and requires no structural changes. It contains the normalized dimensional and fact tables that form Layer 0 of the KPI architecture: the immutable, auditable record of every business event and every entity that participated in those events.

These tables are the source of truth for all downstream computation. They are populated by the existing ETL pipeline — staging ingestion, ODS transformation, dimension loading, and fact loading — and are unchanged by the introduction of the KPI layer.

### **4.2 Table Catalog**

**Dimension tables** — entity master data, slowly changing:

| Table | Description |
| --- | --- |
| `dim_ship` | Ship master data including `cargo_type`, `dwt`, `vessel_type`, classification attributes |
| `dim_port` | Port master data including `unlocode`, `country_code`, geographic coordinates |
| `dim_berth` | Berth master data including `terminal_id`, `harbour_id`, physical specifications |
| `dim_terminal` | Terminal master data, parent of berths |
| `dim_date` | Calendar dimension — one row per day, used for date joins and time spine construction |
| `dim_time` | Time-of-day dimension, used for sub-daily analysis |

**Fact tables** — atomic event records, append-only:

| Table | Description |
| --- | --- |
| `fact_port_visit` | One row per completed or in-progress port visit |
| `fact_berth_visit` | One row per berth stop within a port visit |
| `fact_pilot` | Pilot event records (inbound and outbound) per visit |
| `fact_port_calls` | Daily aggregate of port calls by port and vessel type (existing mart output) |
| `fact_port_performance_analytics` | Port performance metrics and outlier flags (existing mart output) |

### **4.3 What the public Schema Does Not Contain**

The introduction of `silver` and `gold` schemas creates a clear exclusion rule: no new table that serves an intermediate computation purpose or a final KPI purpose belongs in `public`. Specifically:

* Enriched event tables belong in `silver`, not in `public`.
* Time spine tables belong in `silver`, not in `public`.
* KPI aggregate tables belong in `gold`, not in `public`.
* Metric registry tables belong in `gold`, not in `public`.

The `public` schema is closed to new additions after this design is adopted. Any table created after this point that does not fit the existing `dim_` or `fact_` Bronze pattern belongs in `silver` or `gold`.

## **5. Schema: silver — Silver Layer (Layers 1 and 2)**

### **5.1 Role and Responsibility**

The `silver` schema contains all intermediate computation surfaces produced by the KPI refresh pipeline, implemented as **PostgreSQL materialized views**. These views exist solely to make Layer 3 (Gold) writes fast and free of runtime JOIN operations. They are never queried directly by API consumers, BI tools, or any external system.

A materialized view is chosen over a dedicated table for the silver layer because historical accuracy of dimension attributes is not a hard requirement for this platform. Enriched attributes — such as `cargo_type` and `dwt_bucket` — always reflect the current state of the underlying dimension tables at the time of the last refresh. This is the correct trade-off: it eliminates the upsert pipeline complexity in exchange for the accepted behavior that a dimension change propagates backward through all historical enriched rows on the next daily refresh.

The silver schema is refreshed once per day during the KPI refresh cycle, before the Gold tables are computed. No external process reads from or writes to this schema outside of the KPI refresh pipeline.

### **5.2 Layer 1 — Enriched Event Materialized Views**

Layer 1 materialized views are controlled denormalizations of the Bronze-layer fact tables. Each row in a Layer 1 view corresponds to exactly one row in the corresponding Bronze-layer fact table, with dimension attributes resolved by a JOIN that is defined once in the view query and re-executed on each daily refresh via `REFRESH MATERIALIZED VIEW CONCURRENTLY`.

Only the dimension attributes that will appear in a `WHERE`, `GROUP BY`, or `PARTITION BY` clause in a Layer 3 computation are embedded. Attributes that will never serve as KPI filter dimensions remain in the dimension tables and are never denormalized.

**Layer 1 materialized view catalog:**

| Materialized View | Source | Embedded Attributes |
| --- | --- | --- |
| `silver.enriched_port_visits` | `public.fact_port_visits` + `public.dim_ship` + `public.dim_port` | `cargo_type`, `dwt_bucket`, `country_code`, `vessel_type` |
| `silver.enriched_berth_visits` | `public.fact_berth_visits` + `public.dim_berth` + `public.dim_terminal` | `terminal_id`, `port_unlocode`, `cargo_type`, `dwt_bucket` |

### **5.3 Layer 2 — Time Spine Materialized View**

The Layer 2 time spine is implemented as a materialized view — the ideal fit for this use case. A time spine is a cross-join of all active assets against all calendar days. Its source tables (`dim_berth`, `dim_date`) are stable, low-cardinality dimensions that change rarely. A full refresh of this view is fast and cheap, and there is no historical accuracy concern because the time spine carries no event data — it is a scaffold of asset × date slots only.

When event data from `silver.enriched_berth_visit` is LEFT JOINed onto this spine, every asset-day combination produces a row in the Gold result — including days with no ship activity. This is the only architecturally correct way to compute occupancy rates on physical assets, as established by Kimball's Periodic Snapshot Fact Table pattern.

**Layer 2 materialized view catalog:**

| Materialized View | Source | Description |
| --- | --- | --- |
| `silver.time_spine_berth` | `public.dim_berth` × `public.dim_date` | One row per active berth per calendar day — the scaffold for `gold.kpi_berth_occupancy` |

### **5.4 Naming Convention Within the silver Schema**

Materialized views in the `silver` schema do not carry a layer prefix because the schema itself is the namespace. The view names use descriptive identifiers that reflect their content and origin:

* Enriched event views: `enriched_{source_entity}` — e.g., `enriched_port_visit`
* Time spine views: `time_spine_{asset}` — e.g., `time_spine_berth`

## **6. Schema: gold — Gold Layer (Layers 3 and 4)**

### **6.1 Role and Responsibility**

The `gold` schema is the sole external schema in the Data Mart. It contains two table categories: pre-aggregated KPI tables (Layer 3) answering known business questions within sub-10ms latency, and metric registry tables (Layer 4) defining every metric.

The `gold` schema is the only one accessible to external API consumers via the PostgREST role model. The `silver` schema is readable by the PostgREST `api_web_anon` role for exposing enriched intermediate views when the `public` schema is revoked. This boundary is enforced at the database level without application-layer logic.

### **6.2 Layer 3 — KPI Tables**

Each KPI table addresses a single analytical subject at the specified grain. No JOINs occur at query time. A single covering index scan returns the answer to any valid API query within the sub-10ms latency target. The four initial KPI subjects, their grains, and their tables are as follows:

| Table | Declared Grain | Computation Pattern |
| --- | --- | --- |
| `gold.kpi_port_activity` | 1 row per port × period × vessel\_type × cargo\_type × dwt\_bucket | Pattern A — event aggregation over `silver.enriched_port_visit` |
| `gold.kpi_berth_occupancy` | 1 row per berth × calendar day | Pattern B — time spine LEFT JOIN against `silver.enriched_berth_visit` |
| `gold.kpi_operational_efficiency` | 1 row per port × period × vessel\_type | Pattern A — event aggregation over `silver.enriched_port_visit` |
| `gold.kpi_trade_flow` | 1 row per origin × destination × period × cargo\_type | Pattern A — event aggregation over `silver.enriched_port_visit` |

### **6.3 Layer 4 — Metric Registry Tables**

The metric registry lives in the `gold` schema alongside the KPI tables it governs. This placement is deliberate: the registry describes what is in the `gold` schema; it is therefore part of the `gold` schema. Placing it in a separate schema (`meta`, `registry`) would add a schema boundary between the registry and the tables it references, with no architectural benefit.

| Table | Description |
| --- | --- |
| `gold.meta_metric` | One row per metric. Records name, display name, source KPI table, column, formula, unit, time grain, geographic dimension, computation pattern, and owning team. |
| `gold.meta_metric_dimension` | One row per authorized dimension per metric. Records whose dimensions (WHO, WHEN, WHERE axes) may legally be used to filter each metric. |

The `gold.meta_metric` and `gold.meta_metric_dimension` tables are populated by a one-time migration DAG and updated manually — they are never written to by the daily KPI refresh DAG. Their content is the YAML metric registry described in the prior proposal, mirrored to Postgres for API discoverability via `GET /metrics/{metric_name}`.

### **6.4 Naming Convention Within the gold Schema**

* KPI tables: `kpi_{subject}` — e.g., `kpi_port_activity`, `kpi_berth_occupancy`
* Metric registry tables: `meta_{entity}` — e.g., `meta_metric`, `meta_metric_dimension`

The `kpi_` prefix disambiguates KPI aggregate tables from the `meta_` registry tables within the same schema, while the schema name `gold` provides the tier-level namespace.

## **7. Access Control Model**

The three-schema layout maps to three permission tiers, each represented by a PostgreSQL role. The PostgREST role model uses two dedicated database roles — `api_web_anon` and `api_authenticator` — that are separate from the Airflow pipeline role. All grants are applied once during database initialization.

### **7.1 Schema Initialization and PostgREST Role Setup**

The following SQL is the canonical initialization script for the medallion schemas and all PostgREST roles. It is idempotent and safe to run on every database initialization cycle.

wide760-- Step 1: Create medallion schemas
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;
-- Step 2: Create a read-only API role scoped to silver and gold only
CREATE ROLE api\_web\_anon NOLOGIN;
GRANT USAGE ON SCHEMA silver TO api\_web\_anon;
GRANT SELECT ON ALL TABLES IN SCHEMA silver TO api\_web\_anon;
GRANT USAGE ON SCHEMA gold TO api\_web\_anon;
GRANT SELECT ON ALL TABLES IN SCHEMA gold TO api\_web\_anon;
-- Step 3: Create an API authenticator role that PostgREST connects as
CREATE ROLE api\_authenticator NOINHERIT LOGIN PASSWORD '<super-strong-password>';
GRANT api\_web\_anon TO api\_authenticator;
-- Step 4: Explicitly revoke public schema access from the API role
REVOKE ALL ON SCHEMA public FROM api\_web\_anon;

### **7.2 The PostgREST Role Architecture**

PostgREST employs a two-role pattern that aligns with the medallion schema boundary:

`api_web_anon` is the anonymous request role. It lacks login capability (`NOLOGIN`) and holds the schema grants. PostgREST switches to this role for requests without a signed JWT. It can `SELECT` from `silver` and `gold`, and nothing else—`public` is explicitly revoked, making Bronze-layer fact and dimension tables inaccessible via the API regardless of PostgREST configuration.

`api_authenticator` is the connection role. PostgREST connects to the database as this role. Declared `NOINHERIT`, it holds no permissions—it serves as the handshake role PostgREST uses to establish the connection, then switches to `api_web_anon` for queries. This separation follows the principle of least privilege: the login credential grants no data access itself.

The PostgREST configuration file targets this role and the `gold` schema as the primary exposed schema:

wide760# postgrest.conf
db-uri = "postgres://api\_authenticator:<super-strong-password>@<host>:5432/<mart-db>"
db-schemas = "gold, silver"
db-anon-role = "api\_web\_anon"

### **7.3 The Airflow Pipeline Role**

The Airflow KPI refresh DAG uses a distinct role (`data_engineer`), that is never exposed to PostgREST. It requires full read-write access to `public`, `silver`, and `gold` (pipeline targets) for data preparation and transformation.

### **7.4 Permission Matrix**

| Role | `public` | `silver` | `gold` | Login |
| --- | --- | --- | --- | --- |
| `data_engineering` | `CRUD` | `CRUD` | `CRUD` | Yes |
| `api_authenticator` | — | — | — | Yes (NOINHERIT — no direct data access) |
| `api_web_anon` | `REVOKED` | `SELECT` | `SELECT` | No (NOLOGIN) |

## **8. DDL Patterns and Cross-Schema References**

### **8.1 Schema Creation**

Both `silver` and `gold` must be created before any table within them is created. The idiomatic pattern is:

wide760CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;

These statements are idempotent and safe to run on every database initialization.

### **8.2 DDL With Explicit Schema Prefix**

All DDL files for Silver and Gold objects must include the schema prefix in the definition. They must not rely on `search_path` to resolve the schema, because `search_path` is a session-level setting that can be overridden and creates implicit dependencies.

**Silver materialized view example:**

wide760-- teqplay/templates/sql/ddl/silver/enriched\_port\_visit.sql
CREATE MATERIALIZED VIEW IF NOT EXISTS silver.enriched\_port\_visit AS
SELECT
fpv.port\_visit\_id
, fpv.port\_unlocode
, dp.country\_code
, fpv.ship\_id
, fpv.visit\_vessel\_type AS vessel\_type
, ds.cargo\_type
, CASE
WHEN ds.dwt < 10000 THEN 'Small'
WHEN ds.dwt < 25000 THEN 'Handysize'
WHEN ds.dwt < 45000 THEN 'Handymax'
WHEN ds.dwt < 80000 THEN 'Panamax'
WHEN ds.dwt < 120000 THEN 'Aframax'
WHEN ds.dwt < 200000 THEN 'Suezmax'
ELSE 'VLCC'
END AS dwt\_bucket
, fpv.end\_date\_iso\_date
, fpv.end\_timestamp
, fpv.total\_moored\_duration
, fpv.before\_visit\_anchor\_duration
FROM public.fact\_port\_visit fpv
LEFT JOIN public.dim\_ship ds ON fpv.ship\_id = ds.id
LEFT JOIN public.dim\_port dp ON fpv.port\_unlocode = dp.unlocode
WHERE fpv.end\_timestamp IS NOT NULL
WITH DATA;
-- Required for REFRESH MATERIALIZED VIEW CONCURRENTLY
CREATE UNIQUE INDEX IF NOT EXISTS silver\_enriched\_port\_visit\_pkey
ON silver.enriched\_port\_visit (port\_visit\_id);
CREATE INDEX IF NOT EXISTS silver\_enriched\_port\_visit\_lookup
ON silver.enriched\_port\_visit (port\_unlocode, end\_date\_iso\_date, cargo\_type, dwt\_bucket);

The `WITH DATA` clause populates the view immediately on creation. The unique index on `port_visit_id` is mandatory for `REFRESH MATERIALIZED VIEW CONCURRENTLY`, which allows the daily refresh to complete without blocking reads from the KPI refresh DAG.

**Silver time spine materialized view example:**

wide760-- teqplay/templates/sql/ddl/silver/time\_spine\_berth.sql
CREATE MATERIALIZED VIEW IF NOT EXISTS silver.time\_spine\_berth AS
SELECT
db.id AS berth\_id
, db.terminal\_id
, db.main\_port AS port\_unlocode
, dd.iso\_date AS calendar\_date
FROM public.dim\_berth db
CROSS JOIN public.dim\_date dd
WHERE dd.iso\_date >= '2023-01-01'
WITH DATA;
CREATE UNIQUE INDEX IF NOT EXISTS silver\_time\_spine\_berth\_pkey
ON silver.time\_spine\_berth (berth\_id, calendar\_date);

**Gold KPI table example:**

wide760-- teqplay/templates/sql/ddl/gold/kpi\_port\_activity.sql
CREATE TABLE IF NOT EXISTS gold.kpi\_port\_activity (
id uuid NOT NULL DEFAULT gen\_random\_uuid()
, port\_unlocode varchar(255) NOT NULL
, country\_code varchar(10)
, period\_start date NOT NULL
, period\_type varchar(20) NOT NULL CHECK (period\_type IN ('daily', 'monthly', 'yearly'))
, vessel\_type varchar(50) NOT NULL
, cargo\_type varchar(100)
, dwt\_bucket varchar(50)
, visits\_count integer NOT NULL DEFAULT 0
, unique\_ships\_count integer NOT NULL DEFAULT 0
, avg\_turnaround\_hours double precision
, avg\_wait\_before\_berth\_hours double precision
, avg\_moored\_duration\_hours double precision
, total\_cargo\_operations integer
, refreshed\_at timestamp NOT NULL DEFAULT now()
, CONSTRAINT gold\_kpi\_port\_activity\_pkey PRIMARY KEY (id)
, CONSTRAINT gold\_kpi\_port\_activity\_unique UNIQUE (
port\_unlocode, period\_start, period\_type, vessel\_type, cargo\_type, dwt\_bucket
)
);
CREATE INDEX IF NOT EXISTS gold\_kpi\_port\_activity\_lookup
ON gold.kpi\_port\_activity (port\_unlocode, period\_type, period\_start, cargo\_type, dwt\_bucket);

### **8.3 Cross-Schema References in DML**

SQL templates that read from one schema and write to another must use explicit schema-qualified names for all table references. There must be no unqualified table names in Silver or Gold DML templates, even if the `search_path` would resolve them correctly in the current session.

Since the silver layer is now implemented as materialized views, there are no INSERT DML templates for the silver schema. The transformation query is embedded in the DDL view definition (Section 8.2). The only DML operation for the silver layer is the daily `REFRESH MATERIALIZED VIEW CONCURRENTLY` call, which is issued directly from the Airflow operator — no SQL template file is needed.

**Silver refresh (issued directly from the Airflow operator — no template file required):**

wide760refresh\_silver\_enriched\_port\_visit = SQLExecuteQueryOperator(
task\_id='refresh\_silver\_enriched\_port\_visit',
conn\_id=ConnectionID.DATA\_MART,
sql='REFRESH MATERIALIZED VIEW CONCURRENTLY silver.enriched\_port\_visit;',
autocommit=True
)
refresh\_silver\_time\_spine\_berth = SQLExecuteQueryOperator(
task\_id='refresh\_silver\_time\_spine\_berth',
conn\_id=ConnectionID.DATA\_MART,
sql='REFRESH MATERIALIZED VIEW CONCURRENTLY silver.time\_spine\_berth;',
autocommit=True
)

**Pattern A KPI aggregation DML example (silver → gold):**

wide760-- teqplay/templates/sql/dml/gold/refresh\_kpi\_port\_activity.sql
INSERT INTO gold.kpi\_port\_activity (
port\_unlocode, country\_code, period\_start, period\_type,
vessel\_type, cargo\_type, dwt\_bucket,
visits\_count, unique\_ships\_count,
avg\_turnaround\_hours, avg\_wait\_before\_berth\_hours,
avg\_moored\_duration\_hours, total\_cargo\_operations
)
SELECT
port\_unlocode
, country\_code
, date\_trunc('month', end\_date\_iso\_date)::date AS period\_start
, 'monthly' AS period\_type
, vessel\_type
, COALESCE(cargo\_type, 'Unknown') AS cargo\_type
, COALESCE(dwt\_bucket, 'Unknown') AS dwt\_bucket
, COUNT(\*) AS visits\_count
, COUNT(DISTINCT ship\_id) AS unique\_ships\_count
, AVG(total\_moored\_duration) AS avg\_turnaround\_hours
, AVG(before\_visit\_anchor\_duration) AS avg\_wait\_before\_berth\_hours
, AVG(total\_moored\_duration) AS avg\_moored\_duration\_hours
, SUM(0) AS total\_cargo\_operations
FROM silver.enriched\_port\_visit
WHERE end\_date\_iso\_date >= {{ params.period\_start }} --noqa: TMP
AND end\_date\_iso\_date < {{ params.period\_end }} --noqa: TMP
GROUP BY 1, 2, 3, 4, 5, 6, 7
ON CONFLICT (port\_unlocode, period\_start, period\_type, vessel\_type, cargo\_type, dwt\_bucket)
DO UPDATE SET
visits\_count = EXCLUDED.visits\_count
, unique\_ships\_count = EXCLUDED.unique\_ships\_count
, avg\_turnaround\_hours = EXCLUDED.avg\_turnaround\_hours
, refreshed\_at = now();

## **9. Impact on the Prepare Database DAG**

The `prepare_database_dag` (`teqplay/dags/pipeline/prepare_database_dag.py`) manages all DDL operations. Introducing `silver` and `gold` schemas requires three additions to the existing `ddl_task_groups.py` task group structure.

### **9.1 Schema Creation Tasks**

Two new tasks must run before any silver or gold table creation task. They belong at the beginning of the `prepare_fact_tables` task group (or a new `prepare_kpi_tables` task group, depending on how the DAG is structured):

wide760create\_silver\_schema = SQLExecuteQueryOperator(
task\_id='create\_silver\_schema',
conn\_id=ConnectionID.DATA\_MART,
sql='CREATE SCHEMA IF NOT EXISTS silver;',
autocommit=True
)
create\_gold\_schema = SQLExecuteQueryOperator(
task\_id='create\_gold\_schema',
conn\_id=ConnectionID.DATA\_MART,
sql='CREATE SCHEMA IF NOT EXISTS gold;',
autocommit=True
)

### **9.2 Silver Materialized View Creation Tasks**

One task per silver materialized view, using the DDL templates in `teqplay/templates/sql/ddl/silver/`. These tasks run once during database initialization. The `REFRESH MATERIALIZED VIEW CONCURRENTLY` calls that populate the views on each subsequent day are the responsibility of the KPI refresh DAG, not the prepare database DAG.

wide760create\_silver\_enriched\_port\_visit = SQLExecuteQueryOperator(
task\_id='create\_silver\_enriched\_port\_visit',
conn\_id=ConnectionID.DATA\_MART,
sql='silver/enriched\_port\_visit.sql',
autocommit=True
)
create\_silver\_time\_spine\_berth = SQLExecuteQueryOperator(
task\_id='create\_silver\_time\_spine\_berth',
conn\_id=ConnectionID.DATA\_MART,
sql='silver/time\_spine\_berth.sql',
autocommit=True
)

### **9.3 Gold Table Creation Tasks**

One task per gold table, using the new DDL templates in `teqplay/templates/sql/ddl/gold/`:

wide760create\_gold\_kpi\_port\_activity = SQLExecuteQueryOperator(
task\_id='create\_gold\_kpi\_port\_activity',
conn\_id=ConnectionID.DATA\_MART,
sql='gold/kpi\_port\_activity.sql',
autocommit=True
)
create\_gold\_meta\_metric = SQLExecuteQueryOperator(
task\_id='create\_gold\_meta\_metric',
conn\_id=ConnectionID.DATA\_MART,
sql='gold/meta\_metric.sql',
autocommit=True
)

### **9.4 Task Dependency Order**

The schema creation tasks must precede all object creation tasks within their respective schemas. The dependency chain within the new KPI preparation task group is:

wide760create\_silver\_schema ──> [create\_silver\_enriched\_port\_visit, create\_silver\_time\_spine\_berth]
create\_gold\_schema ──> [create\_gold\_kpi\_port\_activity, create\_gold\_kpi\_berth\_occupancy, ...]
──> [create\_gold\_meta\_metric, create\_gold\_meta\_metric\_dimension]

The silver materialized view creation does not need to precede the gold table creation in the `prepare_database_dag`, because the DDL for a materialized view does not execute a data scan — `WITH DATA` populates the view at creation time, but this happens within the silver DDL task itself and the gold tables are empty at this stage.

The ordering that matters is in the **KPI refresh DAG**: silver materialized views must be refreshed before the gold aggregation DML runs, because the gold INSERT queries read from `silver.enriched_port_visit` and `silver.time_spine_berth`. The dependency chain in the KPI refresh DAG is therefore:

wide760[refresh\_silver\_enriched\_port\_visit, refresh\_silver\_time\_spine\_berth]
──> [refresh\_gold\_kpi\_port\_activity, refresh\_gold\_kpi\_berth\_occupancy, ...]

## **10. Design Principles**

The following principles govern the schema strategy. They are derivations of the architectural foundations established in the prior proposal, applied to the specific context of PostgreSQL schema namespacing.

### **Principle 1 — One Schema Per Medallion Tier**

Every table belongs to exactly one schema. The schema is determined by the table's medallion tier, not by its naming convention, its content, or its access pattern. There are no exceptions to this rule. A table that serves two tiers (e.g., a table that is both an enriched intermediate and a final API surface) indicates a design error — the table's responsibility must be separated into two tables in two schemas.

### **Principle 2 — The gold Schema Is the Only External Surface**

No external consumer — REST API client via PostgREST, BI tool, or ad-hoc analyst — queries `public` or `silver` for KPI purposes. If an API query requires data from `public` or `silver`, it means the corresponding Gold table has not yet been built. The correct response is to build the Gold table, not to expose `public` or `silver` to the consumer.

### **Principle 3 — Schema Names Must Be Self-Documenting**

The schema names `silver` and `gold` must not be renamed to domain-specific alternatives (e.g., `enriched`, `kpi`) after this design is adopted. The Medallion terminology is the stable reference frame. Domain-specific names require prior context to interpret; Medallion tier names are universally understood in data engineering without any project-specific knowledge.

### **Principle 4 — Explicit Schema Prefixes in All SQL Templates**

No SQL template file in `teqplay/templates/sql/` may reference a `silver` or `gold` table without its schema prefix. Reliance on `search_path` for resolution is prohibited. This rule ensures that any SQL template is readable and unambiguous in isolation, without knowledge of the session's `search_path` configuration.

### **Principle 5 — Access Control Is Applied at Schema Granularity**

Service account permissions are applied to entire schemas, not to individual tables. When a new KPI table is added to `gold`, it is automatically accessible to all accounts granted `SELECT` on the `gold` schema via `ALTER DEFAULT PRIVILEGES`. No per-table `GRANT` statement is required. Any deviation from this — granting access to individual tables within a schema — must be treated as a temporary exception, documented, and resolved in the next database migration cycle.

## **11. References**

This document derives from and extends the references established in the prior proposal. The following additional references are specific to the schema namespacing and access control design.

| Reference | Contribution to This Document |
| --- | --- |
| Kimball, R. & Ross, M. (2013). *"The Data Warehouse Toolkit."* 3rd Edition. Wiley. | The Dimensional Bus Architecture — the shared dimension vocabulary that makes cross-KPI-table queries possible without additional schema complexity. |
| Databricks (2020). *"Medallion Architecture."* Databricks Documentation. Available: <http://docs.databricks.com> . | Origin of the Bronze / Silver / Gold tier naming, adopted here for PostgreSQL schema namespacing. |
| PostgreSQL Documentation (2024). *"Schemas."* Available: <http://postgresql.org/docs/current/ddl-schemas.html> . | PostgreSQL schema semantics: `GRANT` at schema granularity, `search_path` behaviour, `ALTER DEFAULT PRIVILEGES` for inherited permissions. |
| PostgreSQL Documentation (2024). *"Privileges."* Available: <http://postgresql.org/docs/current/ddl-priv.html> . | Formal definition of `USAGE`, `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE` privilege semantics on schemas and tables. |
| Airbnb Engineering Blog (January 2021). *"Minerva — How Airbnb Achieves Metric Consistency at Scale."* Available: <http://medium.com/airbnb-engineering> . | Metric registry placement rationale — Minerva co-locates metric definitions with the pre-computed tables they govern, which informs the decision to place `gold.meta_metric` in the `gold` schema. |
| PostgREST Documentation (2024). *"Schema Isolation."* Available: <http://postgrest.org/en/stable/references/api/schemas.html> . | PostgREST `db-schemas` and `db-anon-role` configuration — the basis for the two-role pattern (`api_web_anon` / `api_authenticator`) and the `REVOKE ALL ON SCHEMA public` enforcement documented in Section 7. |
| I. KPI / Metrics Layer Research Proposal (Teqplay, May 2026). | Predecessor document. Establishes the five-layer conceptual architecture, two computation patterns, four KPI subjects, and metric registry design that this document physically implements. |