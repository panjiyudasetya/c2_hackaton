---
id: confluence:1215365136
source: confluence
type: page
space: TC
title: II. REST API Exposure Proposal — Teqplay Data Mart
author: Panji Y. Wiwaha
date: '2026-05-21'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#1.-Preface
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#2.-Background-%26-Goal
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#3.-Core-Constraints
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.-Tool-Profiles
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.1-PostgREST
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.2-Postrust
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.3-Hasura-DDN
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.4-NpgsqlRest
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#5.-Comparison-Matrix
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#6.-Time-to-Market-Ranking
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#7.-Recommendation
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#8.-Appendix
---
# II. REST API Exposure Proposal — Teqplay Data Mart

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136  

## Content

# REST API Exposure Proposal — Teqplay Data Mart

**Project:** Teqplay Data Platform — API Serving Layer  
**Domain:** Maritime Port Intelligence  
**Status:** Formal Proposal  
**Date:** May 2026

---

## Table of Contents

1. [Preface](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#1.-Preface)
2. [Background & Goal](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#2.-Background-%26-Goal)
3. [Core Constraints](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#3.-Core-Constraints)
4. [Tool Profiles](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.-Tool-Profiles)

   * [4.1 PostgREST](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.1-PostgREST)
   * [4.2 Postrust](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.2-Postrust)
   * [4.3 Hasura DDN](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.3-Hasura-DDN)
   * [4.4 NpgsqlRest](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#4.4-NpgsqlRest)
5. [Comparison Matrix](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#5.-Comparison-Matrix)
6. [Time-to-Market Ranking](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#6.-Time-to-Market-Ranking)
7. [Recommendation](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#7.-Recommendation)
8. [Appendix — Performance Benchmark Reference](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1215365136/II.+REST+API+Exposure+Proposal+Teqplay+Data+Mart#8.-Appendix)

## **1. Preface**

The immediate goal is to expose two specific KPI tables — `kpi_port_activity` and `kpi_berth_occupancy` — to external clients as a REST API, with the sole KPI of **collecting structured client feedback** on data shape, query patterns, and missing dimensions.

**The plan in one paragraph.** The KPI pipeline uses a two-tier storage strategy. The `silver` schema holds **materialized views** that resolve dimension JOINs once per day, producing enriched event data as the input to aggregation. The `gold` schema holds **dedicated tables** — `gold.kpi_port_activity` and `gold.kpi_berth_occupancy` — written to by the Airflow pipeline via a daily upsert. PostgREST sits in front of both schemas, translating HTTP requests into SQL queries against the `gold` tables as the primary API surface. Which tool to use for that gateway is the primary question this document answers.

**Why materialized views for silver, dedicated tables for gold?** Silver materialized views resolve the enrichment JOIN once at refresh time and are simple to operate — `REFRESH MATERIALIZED VIEW CONCURRENTLY` rebuilds the entire enriched snapshot without blocking reads. Gold KPI tables are dedicated tables because the upsert pattern (`INSERT … ON CONFLICT DO UPDATE`) supports partial date-range refreshes and backfills without rebuilding the entire table, and because pipeline writes and API reads can run concurrently with no lock contention. Access control is enforced at the schema level: the `api_web_anon` PostgREST role is granted `SELECT` on `silver` and `gold` only, and is explicitly revoked from `public`.

This proposal evaluates five open-source, self-hostable tools for that specific purpose. Each tool is assessed on its **documented** features, strengths, and weaknesses for direct schema exposure. Performance comparisons are based only on published, reproducible benchmark data. Where no benchmark data exists for a tool, this document states that explicitly and defines what must be measured before a production decision is made.

**The four candidates:**

* **PostgREST** — Haskell-based, schema-derived REST gateway. Largest community.
* **Postrust** — Rust-based drop-in replacement for PostgREST. REST + GraphQL + Realtime.
* **Hasura DDN** — GraphQL supergraph engine with a declarative metadata workflow.
* **NpgsqlRest** — .NET-based REST server driven by plain `.sql` annotation files.

## **2. Background & Goal**

### **2.1 The Two KPI Tables in Scope**

This proposal covers exactly two tables. No other tables are in scope.

| Table | Grain | Purpose |
| --- | --- | --- |
| `kpi_port_activity` | Port × Period | Summarises vessel visit counts, turnaround times, and port-level activity metrics per port and time period |
| `kpi_berth_occupancy` | Berth × Period | Summarises berth utilisation, idle time, and occupancy rates per berth and time period |

Both tables are produced by the Airflow pipeline. Because each row is a pre-computed aggregate, API queries against these tables are narrow key lookups or small range scans — not expensive aggregation queries.

### **2.2 The Silver / Gold Storage Strategy**

The KPI pipeline uses two physically distinct storage types, each chosen for the role it plays in the data flow. PostgREST exposes both the `silver` and `gold` schemas directly — no additional wrapper views are created on top of them.

**Silver — Materialized Views (enrichment layer)**

The `silver` schema contains PostgreSQL materialized views that resolve the JOIN between raw fact tables and dimension tables once per day. These views are the input to the gold aggregation step.

* `silver.enriched_port_visit` — materializes `fact_port_visit` joined to `dim_ship` and `dim_port`, embedding `cargo_type`, `dwt_bucket`, and `country_code` into each event row
* `silver.enriched_berth_visit` — materializes `fact_berth_visit` joined to `dim_berth` and `dim_terminal`
* `silver.time_spine_berth` — materializes a `dim_berth × dim_date` cross-join, providing the complete berth × day scaffold required for occupancy rate calculations

The Airflow KPI refresh DAG runs `REFRESH MATERIALIZED VIEW CONCURRENTLY` on each silver view before the gold aggregation step. The `CONCURRENTLY` mode is required because the `api_web_anon` role has `SELECT` on the `silver` schema — reads must not be blocked during the refresh.

Historical accuracy of dimension attributes (e.g., `cargo_type` reflecting a ship's classification at the time of its visit) is **not** a hard requirement for this platform. Materialized views are therefore the correct choice: they are simpler to operate than a dedicated table with an upsert pipeline, and the accepted trade-off — a dimension change propagates backward through all historical enriched rows on the next refresh — is documented and acceptable.

**Gold — Dedicated Tables (KPI layer, primary API surface)**

The `gold` schema contains regular PostgreSQL tables holding the pre-aggregated KPI answers that external clients query via PostgREST.

* `gold.kpi_port_activity` — one row per port × period × vessel type × cargo type × DWT bucket
* `gold.kpi_berth_occupancy` — one row per berth × calendar day

The Airflow KPI refresh DAG writes to these tables via an `INSERT … ON CONFLICT DO UPDATE` (upsert) pattern, targeting only the date window being processed. This means the refresh can run for a specific date range without touching the rest of the table — partial backfills are cheap and do not require a full table rebuild.

Dedicated tables are chosen over materialized views for the gold layer for two reasons. First, `REFRESH MATERIALIZED VIEW` (even with `CONCURRENTLY`) rebuilds the entire result set on every run — there is no partial or incremental refresh. Second, a gold materialized view refresh would block or compete with PostgREST reads on the primary API surface during the refresh window. A dedicated table with an upsert allows the Airflow DAG to write rows while PostgREST reads from the same table concurrently, with no lock contention.

**Why not wrapper views on top of gold tables?**

The earlier design proposed creating `mv_kpi_port_activity` and `mv_kpi_berth_occupancy` as materialized views on top of the gold tables, and exposing only those wrappers to the API role. This is no longer necessary. PostgREST's schema-level role model (`api_web_anon` granted `SELECT` on `gold` only) provides the same access boundary without an additional database object. If column-level visibility needs to change, the gold table DDL is the single migration point — not a separate view definition.

**Storage strategy summary:**

| Layer | Schema | Storage Type | Refreshed by | Queryable via PostgREST? |
| --- | --- | --- | --- | --- |
| Enrichment | `silver` | Materialized view | `REFRESH MATERIALIZED VIEW CONCURRENTLY` | Yes — `api_web_anon` has `SELECT` |
| KPI output | `gold` | Dedicated table | `INSERT … ON CONFLICT DO UPDATE` | Yes — `api_web_anon` has `SELECT` |

### **2.3 Goal: Collecting Client Feedback**

The goal of this API exposure is not to build a production API. It is to **collect structured client feedback** on:

* Whether the metric definitions (`visits_count`, `occupancy_rate_pct`) match client expectations
* Which filter dimensions clients actually use (port, berth, date range, cargo type)
* What is missing from the current KPI column set

Every tool and design decision in this proposal is evaluated against that goal. Time-to-market and operational simplicity outweigh throughput at this stage.

## **3. Core Constraints**

### **3.1 Architectural Decoupling**

The API serving layer must be a **separate service** from the `dataflow_dag_core` Airflow project. The only shared artifact is the **PostgreSQL connection** — specifically, read-only access to the `mart` schema.

### **3.2 Historical Accuracy (Principle 3)**

MART tables already contain frozen, enriched attributes (e.g., `cargo_type` as it was at write time, not today's value). The API must **read from MART tables directly** and must not join them to live dimension tables at query time. This is enforced at the database role level: the API role has `USAGE` on the `mart` schema only, with explicit column grants per table.

### **3.3 Cost and Licensing**

All tools must be MIT- or Apache 2.0-licensed and self-hostable at no additional cost. Business Source License (BSL) and cloud-only tools are excluded.

## **4. Tool Profiles**

All four tools expose a PostgreSQL database as a REST API, require no custom application code for basic CRUD operations, and can be self-hosted. The profiles below focus on what matters for MART table exposure: how quickly it can be deployed, how it enforces access control, and the performance ceiling when serving pre-aggregated KPI rows.

### **4.1 PostgREST**

**Language / Runtime:** Haskell binary  |  **Licence:** MIT  |  **Stars:** 23,000+  
**Docs:** [docs.postgrest.org/en/v14](https://docs.postgrest.org/en/v14/)

**What it is.** The original and most battle-tested schema-derived REST gateway for PostgreSQL. PostgREST reads the Postgres schema at startup and automatically generates a REST endpoint for every table, view, and function that the configured database role can access. It powers Supabase in production and has the largest ecosystem of community tutorials and client-side libraries of any tool in this evaluation.

**How it works for MART tables.**

1. Create an `api_kpi_reader` Postgres role with `USAGE` on the `mart` schema (see Section 6).
2. Grant `SELECT` on `kpi_port_activity` and `kpi_berth_occupancy` only.
3. Point PostgREST at that role with a JWT signing secret.
4. Clients receive filterable REST endpoints immediately, with no code written:

wide760# Query port activity KPI for Rotterdam, January 2026
curl "https://api.teqplay.nl/kpi\_port\_activity?port\_unlocode=eq.NLRTM&period\_date=gte.2026-01-01&period\_date=lt.2026-02-01" \
-H "Authorization: Bearer <jwt>"

**Performance.** ~1,749 req/s at 100 concurrent users (January 2026 benchmark). For MART table queries backed by composite B-tree indexes, sub-10 ms p99 is achievable when co-located with Postgres. The Haskell runtime has higher memory overhead than Go/Rust alternatives, but is stable and well-tuned for long-running server workloads.

**Strengths.**

* Fastest time-to-market: deployable from Docker in under one day.
* Largest production case study base and community.
* Full OpenAPI 3.0 spec auto-generated from schema.
* Row-Level Security (RLS) and JWT role switching built-in.
* Seamless upgrade path: grant role access to new schema versions without restart.

**Limitations.**

* No GraphQL — REST only.
* No named/pre-defined query endpoints without database-stored functions.
* No built-in Admin UI or GraphQL Playground.
* ~20 MB binary; Haskell runtime is unfamiliar to most teams.
* 2.6× slower than NpgsqlRest at high concurrency (framework overhead only).

### **4.2 Postrust**

**Language / Runtime:** Rust binary  |  **Licence:** MIT  |  **Binary size:** ~3.5 MB  
**Docs:** [postrust.org](https://postrust.org/)  |  **Compare:** [postrust.org/compare](https://postrust.org/compare/)

**What it is.** A Rust-based, drop-in PostgREST replacement that extends the PostgREST query syntax with GraphQL, realtime subscriptions (PostgreSQL `LISTEN/NOTIFY`), native AWS Lambda support, and a built-in Admin UI. Postrust is serverless-first: its ~3.5 MB binary cold-starts in ~50 ms on AWS Lambda, enabling per-request billing with no container warm-up cost.

**Key differentiators over PostgREST.**

| **Feature** | **Postrust** | **PostgREST** |
| --- | --- | --- |
| GraphQL API | Built-in | Not supported |
| Realtime subscriptions | Built-in (LISTEN/NOTIFY) | Not supported |
| Admin UI (Swagger, Scalar, GraphQL Playground) | Built-in | Not included |
| AWS Lambda (native binary) | ~50ms cold start | Container only |
| Binary size | ~3.5 MB | ~20 MB |
| Custom routes (Rust/Axum) | Yes | No |
| pgvector / semantic search | Native | Limited |
| PostgREST filter syntax | Compatible | — |

**Performance.** Postrust uses the same PostgREST filter-to-SQL translation layer and the same `libpq`-compatible Postgres wire protocol; the Postgres-side query plan is identical to PostgREST for equivalent requests. The difference lies in the overhead of HTTP parsing and serialization, which must be measured. See Section 8 for the benchmarking plan.

**Strengths.**

* Drop-in replacement: existing PostgREST configurations migrate without changes.
* REST + GraphQL in one binary — clients choose the query style that suits them.
* Built-in Admin UI removes the need for a separate Swagger deployment.
* Real-time subscriptions via PostgreSQL `LISTEN/NOTIFY` — clients can subscribe to live KPI updates as MART tables are refreshed by the Airflow pipeline.
* Custom Rust/Axum routes allow adding business-specific endpoints without a full custom service.
* Smallest operational footprint: single ~3.5 MB binary, zero runtime dependencies.
* MIT licensed, open source.

**Limitations.**

* Newer project — smaller production case study base than PostgREST.
* GraphQL adds surface area; clients unfamiliar with GraphQL need onboarding.
* Rust ecosystem requires Rust toolchain for building custom routes.

### **4.3 Hasura DDN**

**Language / Runtime:** Haskell engine + DDN CLI + connectors  |  **Licence:** Apache 2.0  
**Docs:** [hasura.io/docs/3.0/data-modeling/model](https://hasura.io/docs/3.0/data-modeling/model/)

**What it is.** Hasura DDN (Data Delivery Network) v3 is a declarative GraphQL supergraph engine. Rather than reading the schema at startup, Hasura uses a CLI-driven metadata authoring workflow: you introspect the data source, add models, create a supergraph build, and serve it. The result is a fully typed GraphQL API over any connected data source.

**How the DDN workflow looks for MART tables.**

wide760# Introspect the mart schema
ddn connector introspect my\_pg
# Add the KPI models
ddn model add my\_pg kpi\_port\_activity
ddn model add my\_pg kpi\_berth\_occupancy
# Build the supergraph
ddn supergraph build local
# Serve
ddn run docker-start

Clients then query via GraphQL:

wide760query {
kpiPortActivity(
where: { portUnlocode: { \_eq: "NLRTM" }, periodDate: { \_gte: "2026-01-01" } }
limit: 100
) {
portUnlocode
periodDate
visitsCount
avgTurnaroundHours
}
}

**Performance.** No public benchmark for Hasura DDN v3 against plain PostgreSQL materialized views with a read-only role exists at time of writing. Hasura v3 routes queries through a connector layer (the `ndc-postgres` connector), which adds a serialization step between the engine and Postgres. The overhead of this layer under the specific access patterns of `kpi_port_activity` and `kpi_berth_occupancy` must be measured. See Section 8.

**Strengths.**

* Richest feature set: relationships, permissions, event triggers, and remote schemas.
* Full-featured Admin Console with visual query builder.
* Real-time subscriptions via GraphQL.
* Native query support: expose custom SQL as a model.
* Strong access control: field-level permissions per role.

**Limitations.**

* **Highest operational complexity** of any option. Requires DDN CLI, connector configuration, supergraph build step, and either cloud or self-hosted engine deployment.
* The DDN metadata authoring loop (introspect → build → serve) adds friction to rapid iteration during the client feedback phase.
* Resource-intensive: the engine plus connector uses significantly more memory than PostgREST or Postrust for equivalent workloads.
* Apache 2.0 license; commercial features and cloud-managed service require a paid plan.
* No native REST API — GraphQL only. Clients must use GraphQL or a GraphQL-to-REST gateway.
* Longest time-to-first-endpoint: 2–4 hours for a team unfamiliar with DDN CLI.

### **4.4 NpgsqlRest**

**Language / Runtime:** .NET binary  |  **Licence:** MIT  |  **Version:** v3.15.x (May 2026)  
**Docs:** [npgsqlrest.github.io/guide/sql-files.html](https://npgsqlrest.github.io/guide/sql-files.html)

**What it is.** NpgsqlRest is a .NET-based REST server that creates endpoints in two ways: (1) auto-scanning PostgreSQL functions and procedures, and (2) reading plain `.sql` files at startup and creating one endpoint per file. The SQL file approach is uniquely well-suited for MART table exposure because it gives the data team full control over exactly which queries are published as API endpoints, with no application code required.

**How SQL file endpoints work.**

wide760-- sql/kpi/port-activity.sql
-- HTTP GET
-- @param $1 port\_unlocode text
-- @param $2 from\_date date default '2026-01-01'
-- @param $3 to\_date date default '2026-12-31'
SELECT
port\_unlocode,
period\_date,
visits\_count,
avg\_turnaround\_hours,
berth\_occupancy\_rate\_pct
FROM mart.kpi\_port\_activity
WHERE port\_unlocode = $1
AND period\_date BETWEEN $2 AND $3
ORDER BY period\_date DESC;

This single file creates `GET /api/kpi/port-activity?port_unlocode=NLRTM&from_date=2026-01-01`. Static type checking runs at startup — SQL errors against the actual schema are caught before the server accepts any requests. Parameters with defaults are optional in both generated TypeScript types and the OpenAPI spec.

**Performance.** At 100 concurrent users, 1 record: **4,588 req/s** — the benchmark leader among all schema-derived tools (January 2026). 2.6× faster than PostgREST at equivalent load.

**Strengths.**

* **SQL file endpoints**: data team writes plain SQL files, no function DDL, no code.
* **Fastest published performance** of all four candidates (~4,588 req/s at 100VU, Jan 2026 study).
* **Static type checking** at startup catches SQL errors before serving traffic.
* TypeScript client code auto-generated from SQL file annotations.
* Rich annotation system: `@param`, `@result`, `@single`, `@cached`, `@sse` (Server-Sent Events).
* Built-in response caching, rate limiting, CORS, OpenAPI 3.0.
* MIT licensed.

**Limitations.**

* Requires **.NET runtime** — not currently in the Teqplay stack.
* SQL file endpoint feature is unique to NpgsqlRest; migrating to another tool later requires rewriting the endpoint definitions.
* Smaller community than PostgREST; fewer published production case studies.
* .NET operational experience required for deployment and debugging.

## **5. Comparison Matrix**

All four tools fully support PostgreSQL materialized views. The table below covers every dimension relevant to this evaluation, based solely on **documented behavior**.

### **5.1 Feature & Capability Comparison**

| **Criterion** | **PostgREST** | **Postrust** | **Hasura DDN** | **NpgsqlRest** |
| --- | --- | --- | --- | --- |
| **Licence** | MIT | MIT | Apache 2.0 | MIT |
| **REST API** | Available | Available | GraphQL only | Available |
| **GraphQL API** | N/A | Available | Available | N/A |
| **Realtime subscriptions** | N/A | LISTEN/NOTIFY | Available | SSE |
| **JWT authentication** | Available | Available | Available | Available |
| **Row-Level Security (RLS)** | Available | Available | Available | Available |
| **OpenAPI 3.0 auto-generation** | Available | Available | N/A | Available |
| **Built-in Admin UI** | N/A | Swagger + Playground | Console | N/A |
| **Named/fixed endpoints** | Via DB functions | Via DB functions | native queries | SQL files |
| **Column-level access control** | Postgres role grant | Postgres role grant | Metadata field permissions | SQL file column selection |
| **New runtime required** | No (Haskell binary) | No (Rust binary) | Yes (DDN CLI + engine) | Yes (.NET runtime) |
| **Config to the first endpoint** | 14 env vars | ~14 env vars | DDN CLI + build + serve | 21 lines + `.sql` files |
| **Time to first live endpoint** | < 1 day | < 1 day | Half-day to full day | 1–2 days |
| **Operational complexity** | Low | Low | High | Medium |
| **Active maintenance** | Available | Available | Available | Available |

### **5.2 Published Performance Data**

Only two of the four candidates have public benchmark data for PostgreSQL REST workloads.

**Source:** January 2026 NpgsqlRest benchmark study — Hetzner CCX33, 8 vCPUs, 32 GB RAM, all services in Docker on the same host, `generate_series()` test function (pure framework overhead, no table I/O).

| Tool | Benchmark available | 100 VU / 1 row (req/s) | 100 VU / 100 rows (req/s) | Peak Memory |
| --- | --- | --- | --- | --- |
| **NpgsqlRest** | Jan 2026 study | **4,588** | 377 | 321 MB |
| **PostgREST v14** | Jan 2026 study | 1,749 | 342 | ~150 MB |
| **Postrust** | None published | — | — | — |
| **Hasura DDN v3** | None published | — | — | — |

**Important context.** The benchmark above measures framework HTTP overhead with no real table I/O. For `kpi_port_activity` and `kpi_berth_occupancy` with composite B-tree indexes, Postgres query execution time dominates at most concurrency levels. The framework overhead only becomes a bottleneck when the Postgres query is under 1 ms. This is why a targeted benchmark against the actual materialized views must be run before a decision on a production tool is made. See Section 8 for the benchmarking plan.

## **6. Time-to-Market Ranking**

This section ranks the tools by how long it takes from a cold start to a live endpoint that a client can call against `kpi_port_activity` or `kpi_berth_occupancy`.

**Prerequisite for all tools (Postgres setup):**

wide760-- Step 1: Create medallion schemas
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS gold;
-- Step 2: Create the two materialized views
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
-- Step 3: Create a read-only API role scoped to silver and gold only
CREATE ROLE api\_web\_anon NOLOGIN;
GRANT USAGE ON SCHEMA silver TO api\_web\_anon;
GRANT SELECT ON ALL TABLES IN SCHEMA silver TO api\_web\_anon;
GRANT USAGE ON SCHEMA gold TO api\_web\_anon;
GRANT SELECT ON ALL TABLES IN SCHEMA gold TO api\_web\_anon;
-- Step 4: Create an API authenticator role that PostgREST connects as
CREATE ROLE api\_authenticator NOINHERIT LOGIN PASSWORD '<super-strong-password>';
GRANT api\_web\_anon TO api\_authenticator;
-- GRANT CONNECT ON DATABASE "<mart-database-name>" TO api\_authenticator;
-- Step 5: Explicitly revoke public schema access from the API role
REVOKE ALL ON SCHEMA public FROM api\_web\_anon;

The Airflow DAG that writes to the underlying KPI tables should also trigger a refresh:

wide760-- Run after each KPI pipeline execution
REFRESH MATERIALIZED VIEW CONCURRENTLY gold.kpi\_port\_activity;
REFRESH MATERIALIZED VIEW CONCURRENTLY gold.kpi\_berth\_occupancy;

### Tier 1 — Live in < 1 Business Day

**PostgREST** and **Postrust** auto-discover and expose all objects that the configured role can access. After the Postgres setup above, point the tool at the `mart` schema:

wide760# docker-compose.yml (PostgREST — Postrust uses identical env vars)
services:
postgrest:
image: postgrest/postgrest:v14
environment:
PGRST\_DB\_URI: postgres://api\_authenticator:secret@db:5432/MART-DB
PGRST\_DB\_SCHEMA: gold
PGRST\_DB\_ANON\_ROLE: api\_web\_anon
PGRST\_JWT\_SECRET: your-32-character-secret-here
ports:
- "3000:3000"

The tool reads the schema, finds `kpi_port_activity` and `kpi_berth_occupancy`, and immediately exposes them at `GET /kpi_port_activity` and `GET /kpi_berth_occupancy`. No code is written. An OpenAPI spec is generated automatically.

Example client request:

wide760GET /kpi\_port\_activity?port\_unlocode=eq.NLRTM&period\_date=gte.2026-01-01&order=period\_date.desc
Authorization: Bearer <jwt>

### Tier 2 — Live in 1–2 Business Days

**NpgsqlRest** requires a .NET runtime and one `.sql` annotation file per endpoint. Once the runtime is set up, each file takes minutes to write. The startup type-check validates the SQL against the actual schema before the server accepts traffic — errors are caught before deployment, not after. The setup overhead is front-loaded; subsequent endpoint additions are fast.

wide760-- sql/kpi/port-activity.sql
-- HTTP GET
-- @param $1 port\_unlocode text
-- @param $2 from\_date date default current\_date - interval '30 days'
-- @param $3 to\_date date default current\_date
SELECT port\_unlocode, period\_date, visits\_count, avg\_turnaround\_hours
FROM gold.kpi\_port\_activity
WHERE port\_unlocode = $1
AND period\_date BETWEEN $2 AND $3
ORDER BY period\_date DESC;

### Tier 3 — Live in Half a Day to a Full Day

**Hasura DDN** requires installing the DDN CLI, running `ddn connector introspect` against the `mart` schema, adding models for each materialized view, building the supergraph, and running the engine. Each metadata iteration requires a full supergraph rebuild. Teams unfamiliar with the DDN workflow will spend time on the toolchain before the first query runs.

## **7. Recommendation**

### **7.1 Tool Selection**

The recommendation is based on documented capabilities only — not on projected performance. Actual performance against `kpi_port_activity` and `kpi_berth_occupancy` must be measured (see Section 8 for the benchmarking plan).

**For collecting client feedback as quickly as possible: PostgREST or Postrust.**

Both tools auto-discover and expose `kpi_port_activity` and `kpi_berth_occupancy` from the configured Postgres role. No endpoint definitions are written. An OpenAPI spec is generated automatically. A JWT-protected endpoint is live in hours. The choice between them is:

| **Decision factor** | **Choose PostgREST** | **Choose Postrust** |
| --- | --- | --- |
| **Community & production case studies** | Larger (23k+ stars, Supabase) | Smaller (newer project) |
| **REST API** | Available | Available |
| **GraphQL API (if clients request it)** | N/A | Built-in |
| **Built-in Swagger UI** | Available | Available |
| **Runtime familiarity** | Haskell binary | Rust binary |
| **Switch cost if the other is preferred later** | Near-zero (Postrust is drop-in) | Near-zero (same env vars) |

Both tools enforce the same access boundary: the `api_kpi_reader` role (defined in Section 6) determines exactly what is visible. No tool configuration can expose more than what Postgres allows. This is the only access control mechanism that matters.

**NpgsqlRest** is the strongest option when the team needs explicit, auditable endpoint definitions (one `.sql` file per approved query) and can absorb the .NET runtime setup cost. It is the right choice if client feedback reveals that open-table filtering produces inconsistent results across clients — which would require named endpoints to be the only access path.

**Hasura DDN** is the right choice if clients specifically request GraphQL and the team needs the DDN feature set (relationships, event triggers, remote schemas). Its operational complexity is not appropriate for a client-feedback experiment where speed to deployment is the priority.

### **7.2 What Happens After Feedback Is Collected**

The tool chosen to collect feedback does not need to be the final production tool. The materialized views and the Postgres role setup (Section 6) are independent of the API tool. If client feedback reveals that the current tool does not meet a requirement — for example, clients need GraphQL and PostgREST was chosen — switching to Postrust requires changing one Docker image reference and restarting. The materialized views, indexes, and role grants do not change.

The feedback collection phase has one concrete output: a list of the actual query patterns clients use, the dimensions they filter by, and the columns they need that are not yet present. That list is the input to any further tool or schema decision.

## **8. Appendix**

### **8.1 Published Benchmark Reference (Framework Overhead Only)**

Only two of the four candidates have published benchmark data. The table below lists those figures alone. No extrapolations or estimates for other tools are included.

**Source:** January 2026 NpgsqlRest benchmark study — Hetzner CCX33, 8 dedicated vCPUs, 32 GB RAM, all services in Docker on the same host.

**What the benchmark measures:** The test function calls `generate_series()` — pure HTTP and serialization overhead with no real table I/O. This is the theoretical ceiling of the framework. Against `kpi_port_activity` and `kpi_berth_occupancy` with covering indexes, actual throughput will depend primarily on Postgres query execution time, not framework overhead.

| Tool | Source | 100 VU / 1 row (req/s) | 100 VU / 100 rows (req/s) | Peak Memory |
| --- | --- | --- | --- | --- |
| **NpgsqlRest v3** | Jan 2026 study | **4,588** | 377 | 321 MB |
| **PostgREST v14** | Jan 2026 study | 1,749 | 342 | ~150 MB |
| Postrust | No public benchmark | — | — | — |
| Hasura DDN v3 | No public benchmark | — | — | — |

### **8.2 Benchmarking Plan**

Before a production tool decision is made, each shortlisted tool must be benchmarked against the actual materialized views, not a synthetic test function. The following plan defines what to measure and how to measure it.

**Test target:** `kpi_port_activity` and `kpi_berth_occupancy` with the composite indexes defined in Section 6, populated with representative data volumes.

**Test queries (three patterns):**

wide760-- Pattern A: single-port, single-period lookup (narrowest — tests key lookup speed)
SELECT \* FROM gold.kpi\_port\_activity
WHERE port\_unlocode = 'NLRTM' AND period\_date = '2026-01-15';
-- Pattern B: single-port, date range (most common expected client query)
SELECT \* FROM gold.kpi\_port\_activity
WHERE port\_unlocode = 'NLRTM'
AND period\_date BETWEEN '2026-01-01' AND '2026-03-31'
ORDER BY period\_date DESC;
-- Pattern C: multi-port, date range (broadest — tests range scan performance)
SELECT \* FROM gold.kpi\_port\_activity
WHERE port\_unlocode IN ('NLRTM', 'DEHAM', 'BEANR')
AND period\_date BETWEEN '2026-01-01' AND '2026-12-31'
ORDER BY port\_unlocode, period\_date DESC;

**Load levels:** 1 VU (baseline latency), 10 VU, 50 VU, 100 VU.

**Metrics to record per tool and pattern:**

| Metric | Target |
| --- | --- |
| p50 latency | Record as-is |
| p95 latency | Record as-is |
| p99 latency | Record as-is; flag if > 100 ms at 10 VU |
| Throughput (req/s) | Record at each VU level |
| Memory at steady state | Record as-is |
| Error rate under load | Must be 0% |

**Tooling:** Use [k6](https://k6.io/) or [vegeta](https://github.com/tsenart/vegeta) with a fixed JWT token. Run each test three times; report the median across runs.

**When to run this benchmark:** After the client feedback phase, when the query patterns above have been validated against actual client usage. The benchmark should be run against the same data volume and index configuration that will be used in production.

### **8.3 Tool Reference Links**

| Tool | Documentation | Repository | Licence |
| --- | --- | --- | --- |
| PostgREST v14 | <https://docs.postgrest.org/en/v14/> | <https://github.com/PostgREST/postgrest> | MIT |
| Postrust | <https://postrust.org/> | <https://github.com/postrust/postrust> | MIT |
| Hasura DDN | <https://hasura.io/docs/3.0/> | <https://github.com/hasura/graphql-engine> | Apache 2.0 |
| NpgsqlRest | <https://npgsqlrest.github.io/> | <https://github.com/NpgsqlRest/NpgsqlRest> | MIT |

---

*This document was produced as part of the Teqplay Data Platform KPI Layer research and design phase. It should be read in conjunction with* `kpi_layer_research_proposal.md`*, which provides the full theoretical and scientific foundation for the five-layer architecture referenced here.*