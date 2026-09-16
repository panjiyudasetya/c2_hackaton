---
id: confluence:1300070401
source: confluence
type: page
space: TC
title: Technical FuelBoss Data Ingestions
author: Ryan Kharisma Rakhmat
date: '2026-08-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1300070401
explicit_links:
- jira:PTO-2874
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1300070401
---
# Technical FuelBoss Data Ingestions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1300070401  

## Content

Table of Contents

1. Achitecture Overview

2. Bronze Layer
3. Silver Layer
4. Gold Layer
5. Orchestration
6. Naming Conventions and Governance
7. Open Items requiring source-team sign-off before build

# FuelBoss data platform

**Warehouse:** OFINITI\_WH  |  **Database:** OFINITI  |

**Source:** FuelBoss via Fivetran **Audience:** Data platform team (implementation spec)

**Status:** Draft — items marked ⚠️ **ASSUMPTION** need confirmation before build

---

## 1. Architecture overview

Data flows from Fivetran into a Snowflake Medallion Architecture, with dbt managing all transformations to produce governed, high-quality datasets for reporting, applications, and advanced analytics.

|  |  |  |  |
| --- | --- | --- | --- |
| Layer | Schema | Materialization | Refresh trigger |
| Bronze | OFINITI.BRONZE | Raw table per source object (Fivetran-managed) | Fivetran sync (recommend 1h) |
| Silver | OFINITI.SILVER | Incremental tables, fed by a Snowflake STREAM per source table acting as the changed-data buffer (see §3) | dbt job, on Fivetran sync completion |
| Gold | OFINITI.GOLD | Incremental tables | dbt job, after Silver completes |

Recommended tooling: **dbt** for Silver/Gold transformations, orchestrated by a scheduler (dbt Cloud jobs, Airflow, or Fivetran’s post-sync webhook → dbt Cloud API trigger) so Gold never runs against a half-landed Bronze sync.

---

## 2. Bronze layer

**Purpose:** immutable landing zone for Fivetran’s raw payloads. No business logic here — only load mechanics.

### 2.1 Source objects

The source doc lists **9** raw initial tables (all prefixed MT\_DOC\_):

|  |  |
| --- | --- |
| Bronze table (suggested naming) | Feeds Silver view |
| MT\_DOC\_ASSET\_JOB\_ROLES\_OVERVIEW | STG\_ASSET\_JOB\_ROLES |
| MT\_DOC\_FUELBOSS\_BUNKERING\_LOCATION | STG\_BUNKERING\_LOCATIONS |
| MT\_DOC\_FUELBOSS\_BUNKER\_OPERATION | STG\_BUNKER\_OPERATIONS |
| MT\_DOC\_FUELBOSS\_COMPANY | STG\_COMPANIES |
| MT\_DOC\_FUELBOSS\_NOMINATION | STG\_NOMINATIONS |
| MT\_DOC\_FUELBOSS\_OPERATION\_DOCUMENT | STG\_OPERATIONAL\_DOCUMENTS |
| MT\_DOC\_FUELBOSS\_OPERATION\_STANDARD | STG\_OPERATION\_STANDARDS |
| MT\_DOC\_FUELBOSS\_VESSEL | STG\_VESSELS |
| MT\_DOC\_FUEL\_TYPE | STG\_FUEL\_TYPES |

### 2.2 Load pattern

* Fivetran lands each source object as a table with a VARIANT payload column (or already-flattened columns, depending on connector type — confirm which Fivetran connector is in use: *generic API/webhook* **vs** *a certified FuelBoss connector*).

* Treat Bronze as **append/merge, never delete**. Fivetran handles Change Data Capture (CDC); do not add dbt logic upstream of Bronze.

* Every Bronze table should carry Fivetran’s standard metadata columns: \_FIVETRAN\_SYNCED, \_FIVETRAN\_DELETED, \_FIVETRAN\_ID (or equivalent primary key from source).

* **Schema drift:** enable Fivetran’s “allow new columns” setting; Silver views should explicitly select columns (**not SELECT \***) so new upstream fields don’t silently break downstream models — they’ll instead surface as “new column not yet modeled,” which is the safer failure mode.

### 2.3 Bronze-layer checks (data platform team owns these)

* Freshness check per table: alert if \_FIVETRAN\_SYNCED is older than 2x the expected sync interval.

* Row-count sanity check post-sync (**catch silent zero-row loads**).

* No transformation, filtering, or business logic — that’s a Silver responsibility, kept out of Bronze so replays/backfills are always possible from raw truth.

### 2.4 End-to-end table lineage (MT\_DOC → STG → MART)

The diagram below shows every table-level dependency left to right:

MT\_DOC to STG to MART table lineage

each Bronze MT\_DOC\_\* landing table into its 1:1 Silver STG\_\* model, then how those Silver models converge into the three Gold marts. ASSET\_OPERATORS feeds MART\_BUNKER\_OPERATIONS, which in turn feeds MART\_TOTAL\_FUEL\_DELIVERED.

the two gold-to-gold dependencies are highlighted in purple to distinguish them from the silver-to-gold joins.

---

## 3. Silver layer

**Purpose:** one conformed, typed, deduplicated view/table per business entity. This is where JSON is flattened, types are cast, and light business rules (e.g. dedup on latest record) are applied — but no cross-entity joins yet.

**Schema:** OFINITI.SILVER\_FUELBOSS

### 3.1 Staging models

|  |  |  |
| --- | --- | --- |
| Model | Grain | Key transformation notes |
| STG\_ASSET\_JOB\_ROLES | 1 row per asset | Cast JOB\_ROLES\_COUNT to NUMBER |
| STG\_BUNKERING\_LOCATIONS | 1 row per location | — |
| STG\_BUNKER\_OPERATIONS | 1 row per operation | Cast OPERATION\_STARTED\_AT\_UTC, PHASE\_30\_AT, PHASE\_110\_AT to TIMESTAMP\_TZ; confirm phase semantics (see §4.2) |
| STG\_COMPANIES | 1 row per company | — |
| STG\_FUEL\_TYPES | 1 row per fuel type | — |
| STG\_NOMINATIONS | 1 row per nomination | Links bunkering location, receiver vessel, supplier asset, fuel type |
| STG\_OPERATIONAL\_DOCUMENTS | 1 row per (operation, document type) | SIGNING\_STATUS is a coded field (0–4) — build a SIGNING\_STATUS lookup/seed to decode; confirm code meanings with source team (⚠️ not documented)  0- not starter  1- requested  2-open  3-signed by  4-signed by everyone |
| STG\_OPERATION\_STANDARDS | 1 row per standard | — |
| STG\_VESSELS | 1 row per vessel | — |

### 3.2 Delta capture: Snowflake Streams as the changed-data buffer

Rather than re-scanning full Bronze tables on every run, each Silver model is fed by a **Snowflake STREAM** sitting on top of its Bronze source. A stream automatically tracks every row inserted, updated, or deleted since the last time it was consumed — it *is* the “temporary place for changed data”: once a DML statement (a MERGE, in this case) reads from it and commits, its offset advances and it empties back down to just the next batch of changes. There’s no watermark table to maintain and no risk of that bookkeeping drifting out of sync with Bronze.

The following diagram shows how the contents of a standard stream change as rows in the source table are updated. Whenever a DML statement consumes the stream contents, the stream position advances to track the next set of DML changes to the table ([*Snowflake Docs*](https://docs.snowflake.com/en/user-guide/streams-intro))

**Snowflake Streams** is a change data capture (CDC) object that records data changes made to a table or view. It allows ELT workflows, such as dbt or Snowflake Tasks, to process only incremental changes.

**One-time setup per source table** (run once, not part of the dbt DAG — put these in a macros/setup\_streams.sql run-operation macro or an infra/bootstrap script):

wide760truecreate stream if not exists SILVER\_FUELBOSS.BUNKER\_OPERATIONS\_STREAM
    on table BRONZE\_FUELBOSS.MT\_DOC\_FUELBOSS\_BUNKER\_OPERATION
    append\_only = false;  -- false so updates/deletes are captured, not just inserts

Repeat for all 9 Bronze source tables. Register each stream as a dbt source so models can {{ source(...) }} it like any other object:

*# models/staging/\_sources.yml*

wide760truesources:
- name: bronze\_fuelboss\_streams
schema: SILVER\_FUELBOSS
tables:
- name: bunker\_operations\_stream
identifier: BUNKER\_OPERATIONS\_STREAM
      # ... one entry per stream

**Operational note for the platform team:** a stream goes stale (and has to be recreated, losing its buffered changes) if it isn’t consumed within the source table’s DATA\_RETENTION\_TIME\_IN\_DAYS. With hourly Fivetran syncs and an hourly dbt job this isn’t a practical risk, but add a monitoring check on stream staleness (SYSTEM$STREAM\_HAS\_DATA / SHOW STREAMS) alongside the existing freshness checks.

### 3.3 Standard staging model pattern (dbt)

Each Silver model is now materialized='incremental' with a merge strategy, reading from the stream instead of the raw Bronze table. Because a stream only ever contains what’s changed since the last consumption, every dbt run merges a small delta rather than rescanning all of Bronze — and because the read happens inside the same transaction as the merge, Snowflake advances the stream’s offset automatically on commit. No separate “clear the delta table” step is needed.

*-- models/staging/stg\_bunker\_operations.sql*

sqlwide760true{{ config(
    materialized='incremental',
    unique\_key='operation\_id',
    incremental\_strategy='merge',
    merge\_update\_columns=[
        'nomination\_id', 'operation\_standard\_id', 'operation\_started\_at\_utc',
        'phase\_30\_at', 'phase\_110\_at', 'receiver\_company\_id',
        'supplier\_company\_id', '\_loaded\_at', '\_is\_deleted'
    ]
) }}
with delta as (
    -- reading from the stream both captures the changes AND (on commit) consumes them
    select \* from {{ source('bronze\_fuelboss\_streams', 'bunker\_operations\_stream') }}
),
renamed as (
    select
        nomination\_id::varchar(36)          as nomination\_id,
        operation\_id::varchar(36)           as operation\_id,
        operation\_standard\_id::varchar(36)  as operation\_standard\_id,
        operation\_started\_at\_utc::timestamp\_tz as operation\_started\_at\_utc,
        phase\_30\_at::timestamp\_tz           as phase\_30\_at,
        phase\_110\_at::timestamp\_tz          as phase\_110\_at,
        receiver\_company\_id::varchar(36)    as receiver\_company\_id,
        supplier\_company\_id::varchar(36)    as supplier\_company\_id,
        \_fivetran\_synced                    as \_loaded\_at,
        (metadata$action = 'DELETE')        as \_is\_deleted
    from delta
    qualify row\_number() over (
        partition by operation\_id
        order by \_fivetran\_synced desc, metadata$action desc  -- if a row was both updated and deleted in the same batch, keep the delete
    ) = 1
)
select \* from renamed

Apply the same stream-sourced, incremental-merge pattern to each of the 9 models — a stream on its Bronze source, a dbt model reading from that stream, deduplicated on the natural key, with \_is\_deleted carried through rather than physically removing rows. Physical deletes are avoided at this layer so Gold-layer history stays intact; Gold models and BI tooling can filter where not \_is\_deleted as needed.

### 3.4 Silver-layer dbt tests

For every staging model, apply as a minimum:

* not\_null + unique on the natural key (operation\_id, company\_id, vessel\_id, etc.)

* relationships test from foreign keys (e.g. STG\_BUNKER\_OPERATIONS.supplier\_company\_id → STG\_COMPANIES.company\_id)

* accepted\_values on coded fields once SIGNING\_STATUS codes are confirmed

---

## 4. Gold layer

**Schema:** OFINITI.GOLD\_FUELBOSS

**Purpose:** business-ready, denormalized, join-resolved tables for BI/reporting consumption.

### 4.1 DIM\_ASSET\_OPERATORS

**Grain:** 1 row per supplier company (asset operator lookup).

|  |  |
| --- | --- |
| Field | Source |
| SUPPLIER\_COMPANY\_ID | STG\_COMPANIES.company\_id |
| ASSET\_OPERATOR | ⚠️ **ASSUMPTION** — no source column maps directly to “asset operator” name in the documented Silver models. Two build options: |

**Option A (recommended if no upstream field exists):** build as a dbt **seed** (seeds/asset\_operator\_map.csv) maintained by the business/ops team, left-joined to STG\_COMPANIES on company\_id. This is the standard pattern when a mart needs a manually-curated business mapping that isn’t in the source system.

**Option B:** if FuelBoss actually returns an operator field inside the company or vessel payload that wasn’t captured in the data dictionary, add it to STG\_COMPANIES (or a new STG\_ASSET\_OPERATORS staging model) instead of hardcoding a seed.

**Action for data platform team:** confirm with the FuelBoss source-system owner before building — this determines whether §4.1 is a seed-backed static table or a proper incremental model.

*-- models/marts/asset\_operators.sql*

sqlwide760true{{ config(materialized='table') }}
select
    c.company\_id  as supplier\_company\_id,
    m.asset\_operator
from {{ ref('stg\_companies') }} c
left join {{ ref('asset\_operator\_map') }} m   -- seed, or replace with real source once confirmed
    on c.company\_id = m.company\_id
where not c.\_is\_deleted

### 4.2 FACT\_BUNKER\_OPERATIONS

**Grain:** 1 row per bunker operation (a single fuel-delivery transaction).

This is the central fact table — every other field is resolved via joins from Silver.

|  |  |
| --- | --- |
| Field | Resolved from |
| ID | STG\_BUNKER\_OPERATIONS.operation\_id |
| OPERATION\_DATE | date(operation\_started\_at\_utc) |
| SUPPLIER\_COMPANY\_ID / SUPPLIER\_COMPANY\_NAME | STG\_BUNKER\_OPERATIONS.supplier\_company\_id → STG\_COMPANIES |
| ASSET\_OPERATOR | → ASSET\_OPERATORS (§4.1) on supplier\_company\_id |
| RECEIVER\_COMPANY\_ID / RECEIVER\_COMPANY\_NAME | STG\_BUNKER\_OPERATIONS.receiver\_company\_id → STG\_COMPANIES |
| RECEIVER\_VESSEL\_NAME / RECEIVER\_VESSEL\_IMO | STG\_NOMINATIONS.receiver\_vessel\_id → STG\_VESSELS |
| RECEIVER\_VESSEL\_JOB\_ROLES | STG\_VESSELS.vessel\_id → STG\_ASSET\_JOB\_ROLES.asset\_id |
| SUPPLIER\_ASSET\_NAME / SUPPLIER\_ASSET\_IMO | STG\_NOMINATIONS.supplier\_asset\_id → STG\_VESSELS (vessels table reused as asset registry — ⚠️ confirm) |
| SUPPLIER\_ASSET\_JOB\_ROLES | STG\_NOMINATIONS.supplier\_asset\_id → STG\_ASSET\_JOB\_ROLES.asset\_id |
| OPERATION\_STANDARD | STG\_BUNKER\_OPERATIONS.operation\_standard\_id → STG\_OPERATION\_STANDARDS |
| PORT\_NAME | STG\_NOMINATIONS.bunkering\_location\_id → STG\_BUNKERING\_LOCATIONS |
| FUEL\_TYPE | STG\_NOMINATIONS.fuel\_type\_id → STG\_FUEL\_TYPES |
| NOMINATED\_QUANTITY | STG\_NOMINATIONS.nominated\_quantity\_range — ⚠️ source field is named as a *range* (sample value "50"); confirm whether this is a single number, a range string needing parsing, or a bucket code, since the Gold field is a plain NUMBER |
| DURATION\_MINUTES | ⚠️ **ASSUMPTION**: datediff('minute', phase\_30\_at, phase\_110\_at). Confirm phase code meaning with source team — “30” and “110” read like workflow/status codes, not obviously start/end. Needs sign-off before hardcoding the calculation |
| BDN\_SIGNED | Derived boolean from STG\_OPERATIONAL\_DOCUMENTS where document\_type = 'BDN', signing\_status mapped to true/false once codes are confirmed |

*-- models/marts/mart\_bunker\_operations.sql*

sqlwide760true{{ config(
    materialized='incremental',
    unique\_key='id',
    incremental\_strategy='merge',
    post\_hook="delete from {{ this }} where id in (select operation\_id from {{ ref('stg\_bunker\_operations') }} where \_is\_deleted)"
) }}
with ops as (
    select \* from {{ ref('stg\_bunker\_operations') }}
    where not \_is\_deleted
    {% if is\_incremental() %}
      and \_loaded\_at > (select max(\_loaded\_at) from {{ this }})
    {% endif %}
),
nom as (select \* from {{ ref('stg\_nominations') }}),
companies as (select \* from {{ ref('stg\_companies') }}),
vessels as (select \* from {{ ref('stg\_vessels') }}),
job\_roles as (select \* from {{ ref('stg\_asset\_job\_roles') }}),
locations as (select \* from {{ ref('stg\_bunkering\_locations') }}),
fuel\_types as (select \* from {{ ref('stg\_fuel\_types') }}),
standards as (select \* from {{ ref('stg\_operation\_standards') }}),
asset\_operators as (select \* from {{ ref('asset\_operators') }}),
bdn as (
    select
        operation\_id,
        max(case when document\_type = 'BDN' then signing\_status\_bool else false end) as bdn\_signed
    from {{ ref('stg\_operational\_documents') }}
    group by operation\_id
)
select
    ops.operation\_id                                   as id,
    date(ops.operation\_started\_at\_utc)                 as operation\_date,
    ops.supplier\_company\_id,
    sup.company\_name                                   as supplier\_company\_name,
    ao.asset\_operator,
    ops.receiver\_company\_id,
    rec.company\_name                                   as receiver\_company\_name,
    rv.vessel\_name                                      as receiver\_vessel\_name,
    rv.vessel\_imo                                       as receiver\_vessel\_imo,
    rjr.job\_roles\_count                                 as receiver\_vessel\_job\_roles,
    sv.vessel\_name                                      as supplier\_asset\_name,
    sv.vessel\_imo                                       as supplier\_asset\_imo,
    sjr.job\_roles\_count                                 as supplier\_asset\_job\_roles,
    std.operation\_standard\_name                         as operation\_standard,
    loc.port\_name,
    ft.fueltype\_name                                    as fuel\_type,
    nom.nominated\_quantity\_range                        as nominated\_quantity,
    datediff('minute', ops.phase\_30\_at, ops.phase\_110\_at) as duration\_minutes,
    coalesce(bdn.bdn\_signed, false)                     as bdn\_signed
from ops
left join nom          on ops.nomination\_id = nom.nomination\_id
left join companies sup on ops.supplier\_company\_id = sup.company\_id
left join companies rec on ops.receiver\_company\_id = rec.company\_id
left join asset\_operators ao on ops.supplier\_company\_id = ao.supplier\_company\_id
left join vessels rv    on nom.receiver\_vessel\_id = rv.vessel\_id
left join vessels sv    on nom.supplier\_asset\_id = sv.vessel\_id
left join job\_roles rjr on nom.receiver\_vessel\_id = rjr.asset\_id
left join job\_roles sjr on nom.supplier\_asset\_id = sjr.asset\_id
left join locations loc on nom.bunkering\_location\_id = loc.bunkering\_location\_id
left join fuel\_types ft  on nom.fuel\_type\_id = ft.fuel\_type\_id
left join standards std  on ops.operation\_standard\_id = std.operation\_standard\_id
left join bdn            on ops.operation\_id = bdn.operation\_id

**Gold-layer tests:** unique + not\_null on id; not\_null on operation\_date, supplier\_company\_id, receiver\_company\_id; freshness test on operation\_date vs. current date to catch stalled pipelines.

**Soft-delete handling**: STG\_\* models carry \_is\_deleted rather than physically removing rows (§3.3), so both Gold models must filter it out — otherwise records deleted at source stay visible in the mart and remain inside sum(nominated\_quantity) in MART\_TOTAL\_FUEL\_DELIVERED, inflating fuel-delivered totals over time. Because MART\_BUNKER\_OPERATIONS is an incremental merge, the where not \_is\_deleted filter alone only stops newly-deleted rows from being loaded; rows already merged in a prior run would persist. The post\_hook removes those previously-loaded ids on each run, so the delete actually propagates. MART\_TOTAL\_FUEL\_DELIVERED needs no filter of its own — it aggregates the already-filtered mart — and ASSET\_OPERATORS is a full-rebuild table, so the where clause is sufficient there.

### 4.3 FACT\_TOTAL\_FUEL\_DELIVERED

**Grain:** 1 row per supplier company per rolling period.

⚠️ **ASSUMPTION**: the sample row shows PERIOD\_START = 2026-05-18, PERIOD\_END = 2026-06-17 — a 30-day window. This looks like a **rolling 30-day trailing window recalculated on each refresh**, not a fixed calendar month. Confirm the intended period logic (rolling 30-day vs. calendar month vs. some other business-defined period) with stakeholders before building — the aggregation grain changes materially depending on the answer.

*-- models/marts/mart\_total\_fuel\_delivered.sql*

sqlwide760true{{ config(materialized='table') }}
with bounds as (
    select
        dateadd('day', -30, current\_date()) as period\_start,
        current\_date()                       as period\_end
),
agg as (
    select
        supplier\_company\_id,
        supplier\_company\_name,
        sum(nominated\_quantity)  as total\_fuel\_delivered\_mt,
        count(\*)                 as operation\_count
    from {{ ref('mart\_bunker\_operations') }}
    cross join bounds
    where operation\_date between bounds.period\_start and bounds.period\_end
    group by supplier\_company\_id, supplier\_company\_name
)
select
    agg.\*,
    bounds.period\_start,
    bounds.period\_end,
    current\_timestamp() as refreshed\_at
from agg
cross join bounds

**Gold-layer tests:** not\_null on supplier\_company\_id, total\_fuel\_delivered\_mt; a custom test asserting period\_end >= period\_start; a freshness check on refreshed\_at.

---

## 5. Orchestration

dbt orchestration flow

1. Fivetran sync completes → fires a webhook (or is polled) that triggers the dbt job.

2. dbt job runs in order: stg\_\* models → asset\_operators → mart\_bunker\_operations → mart\_total\_fuel\_delivered. Express this as ref() dependencies so dbt’s DAG handles ordering automatically — don’t hardcode a manual run order.

3. Run dbt test after each layer; fail the job (and alert) on any Gold-layer test failure so bad data never reaches BI tools.

4. Recommended cadence: Fivetran sync hourly (adjust to source data volatility); dbt job triggered on sync completion rather than a fixed cron, to avoid running Gold against a partially-landed Bronze sync.

5. Because each Silver model consumes its Snowflake stream on run (advancing the offset on commit), **every scheduled dbt run permanently drains the buffered changes** — there’s no safe way to “peek” at a stream without consuming it in the same transaction. If a run fails partway through Silver, do not re-trigger it casually: check which streams were already consumed (SYSTEM$STREAM\_HAS\_DATA returns false once drained) before deciding whether a re-run would miss data or double-process it. Wrapping each stream-consuming merge in a single transaction per model (dbt’s default behavior) keeps consumption atomic with the merge, so a failed model doesn’t silently drop changes — but a partially failed *job* (some models succeeded, some didn’t) needs the same care as any other partial-pipeline failure.

## 6. Naming & governance conventions

* Bronze: MT\_DOC\_<SOURCE\_OBJECT\_NAME>, no transformation.

* Silver: STG\_<ENTITY\_PLURAL>, ODS\_<ENTITY\_PLURAL>, one per business entity, 1:1 with a Bronze source. STG will be in View and ODS will be in Table.

* Gold: FACT\_<BUSINESS\_QUESTION> for fact/aggregate tables, DIM\_<ENTITY\_NAME> plain entity name for dimension/lookup tables (e.g. DIM\_ASSET\_OPERATORS).

* Every Gold model gets a dbt description and column-level docs — this is the layer BI consumers query directly, so it should be self-documenting via dbt docs generate.

## 7. Open items requiring source-team sign-off before build

1. Confirm whether a 10th Bronze source object exists (doc says “10 tables,” 9 are listed). Are the ASSET\_OPERATOR on the mart table also comes from FuelBoss data? Answers: it should come from fuel boss database. Need to ingest from bronze layer.

2. Confirm SIGNING\_STATUS code meanings (0–4) in STG\_OPERATIONAL\_DOCUMENTS. Answers: 0- not starter

   1- requested

   2-open

   3-signed by

   4-signed by everyone

3. Confirm PHASE\_30\_AT / PHASE\_110\_AT semantics and whether DURATION\_MINUTES should be computed from these two fields. answers: no info yet, needs to check with fuel boss

4. Confirm source of ASSET\_OPERATOR — seed/manual mapping vs. an unlisted source field. same as number 1.
5. Confirm whether vessels and “assets” (supplier side) are genuinely the same entity/table, or whether a separate asset registry should exist. This is on Nominations table that have fields called `Receiver_Vessel_ID` and `Supplier_Asset_ID` are both of them are vessel or asset? answers: it is different.

6. Confirm NOMINATED\_QUANTITY\_RANGE format (single value vs. range vs. bucket code) and required parsing. answers: nominated quantity is no range at the beginning. it is freetext.

7. Confirm the period logic for MART\_TOTAL\_FUEL\_DELIVERED (rolling 30-day vs. calendar month vs. other). answers: weekly basis, just set week-of-the year.

| **Ticket ID** | **Name** | **Descriptions** | **Complexity** |
| --- | --- | --- | --- |
| * [PTO-2874](https://teqplaybv.atlassian.net/browse/PTO-2874) | Initiate discussion for confirming fuelBoss data sources | set a meeting and confirm all of those 7 questions above | 2 |
|  | Fivetran to Snowflake Sync Bronze Table | Ingest fuelBoss data using fivetran to be available on snowflake | the fuelboss team will do it. (Other ofiniti team) |
|  | Webhook triggers dbt jobs for data transformations | After the fivetran ingestion is complete, send the webhook to trigger the dbt to be running. | just check if it is on snowflake should be on Data Platform side, if on fivetran will be their side. |
|  | dbt projects data transformations bronze, silver, gold. | create a complete dbt data transformations orchestrations from bronze, silver, gold tables. | our side |
|  | dbt test: ID: not-null, unique, relationships. All layers: bronze, silver, gold. | testing some data in the specific layer about the not-null, unique, relationship, availability, and completeness. | our side |
| PTO-28895c406517-69e9-3c5d-b831-d2bed7d442a4System Jira | snowflake dbt alert on failure and send to slack channel or email. | send some alert if the errors happens to be aware of the pipeline failure / success status of data ingestions. | our side |