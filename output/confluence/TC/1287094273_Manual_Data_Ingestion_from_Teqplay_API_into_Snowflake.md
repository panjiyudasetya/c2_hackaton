---
id: confluence:1287094273
source: confluence
type: page
space: TC
title: Manual Data Ingestion from Teqplay API into Snowflake
author: Ryan Kharisma Rakhmat
date: '2026-07-15'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1287094273
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1287094273
---
# Manual Data Ingestion from Teqplay API into Snowflake

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1287094273  

## Content

# Data Ingestion in Snowflake

In the previous documents about REST API ingestions. We are having difficulties in the credentials things. But now we can do the API Ingestions inside the snowflake. Here is the steps for Data ingestions from API:

## 01 Create a Network Rule

wide760-- use teqplay warehouse, database and schema
USE WAREHOUSE TEQPLAY\_WH;
USE DATABASE API\_INGESTION\_PROTO;
USE SCHEMA PUBLIC;
-- create an api network rule for this base url api.teqplay.nl with https
CREATE OR REPLACE NETWORK RULE teqplay\_api\_network\_rule
MODE = EGRESS
TYPE = HOST\_PORT
VALUE\_LIST = ('api.teqplay.nl:443');
-- create the secret for API creds
CREATE OR REPLACE SECRET teqplay\_api\_credentials
TYPE = GENERIC\_STRING
SECRET\_STRING = '{"client\_id":"DataEngineering","client\_secret":"it is secret"}';

## 02 EAI— External Access Integration

wide760-- create an EAI
CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION teqplay\_api\_access\_integration
ALLOWED\_NETWORK\_RULES = (teqplay\_api\_network\_rule)
ALLOWED\_AUTHENTICATION\_SECRETS = (teqplay\_api\_credentials)
ENABLED = TRUE;

## 03 Python UDTF — User Defined Table Function

wide760-- create UDTF
CREATE OR REPLACE FUNCTION fetch\_teqplay\_api\_data(endpoint STRING)
RETURNS TABLE (uniqueId STRING, name STRING, raw\_json VARIANT)
LANGUAGE PYTHON
RUNTIME\_VERSION = '3.12'
HANDLER = 'ApiDataFetcher'
PACKAGES = ('requests')
EXTERNAL\_ACCESS\_INTEGRATIONS = (teqplay\_api\_access\_integration)
SECRETS = ('teqplay\_api\_credentials' = teqplay\_api\_credentials)
AS
$$
import \_snowflake
import requests
import json
from datetime import datetime, timedelta
BASE\_URL = "https://api.teqplay.nl/"
AUTH\_ENDPOINT = "v1/auth/token"
class ApiDataFetcher:
def \_\_init\_\_(self):
self.\_token = None
self.\_token\_expiry = None
self.\_session = requests.Session()
self.\_authenticate()
def \_authenticate(self):
creds = json.loads(\_snowflake.get\_generic\_secret\_string("teqplay\_api\_credentials"))
resp = self.\_session.post(
BASE\_URL+AUTH\_ENDPOINT,
json={
"client\_id": creds["client\_id"],
"client\_secret": creds["client\_secret"],
},
timeout=10,
)
resp.raise\_for\_status()
payload = resp.json()
self.\_token = payload["access\_token"]
expires\_in = payload.get("expires\_in", 3600)
# refresh a bit early to avoid edge-of-expiry failures
self.\_token\_expiry = datetime.utcnow() + timedelta(seconds=expires\_in - 60)
def \_ensure\_valid\_token(self):
if self.\_token is None or datetime.utcnow() >= self.\_token\_expiry:
self.\_authenticate()
def process(self, endpoint: str):
"""endpoint is a column value passed in from the calling SQL,
e.g. a resource path or query parameter driven by another table."""
self.\_ensure\_valid\_token()
headers = {"Authorization": f"Bearer {self.\_token}"}
url = BASE\_URL + endpoint
resp = self.\_session.get(url, headers=headers, timeout=30)
if resp.status\_code == 401:
# token expired mid-flight — refresh once and retry
self.\_authenticate()
headers = {"Authorization": f"Bearer {self.\_token}"}
resp = self.\_session.get(url, headers=headers, timeout=30)
resp.raise\_for\_status()
data = resp.json()
items = data
for record in items:
yield (record.get("uniqueId"), record.get("name"), json.dumps(record))
$$;

## 04 SQL Result Set

wide760-- test it with get infra ports
select \* from TABLE(fetch\_teqplay\_api\_data('v1/infra/port'));
-- create a raw tables and hit the API data (infra port, terminal and berth)
CREATE OR REPLACE TABLE API\_INGESTION\_PROTO.PUBLIC.raw\_ports AS
SELECT \* FROM TABLE(fetch\_teqplay\_api\_data('v1/infra/port'));

After we are doing ingestions, then we create some task transformations in the snowflake for transforming STG to ODS and then to Dimensions.

Here are some tasks windows in snowflake

# Teqplay ELT Pipeline Summary

## Overview

This project implements a medallion-architecture ELT pipeline that ingests maritime infrastructure data (ports, terminals, and berths) from the Teqplay API into Snowflake, transforming it through four layers: Raw → Bronze (Staging) → Silver (ODS) → Gold (Dimensional).

All objects reside in `API_INGESTION_PROTO.PUBLIC` and run on the `TEQPLAY_WH` warehouse.

---

## 01 Init — API Connection & Raw Ingestion Setup

**Files:** `teqplay_api_data.sql`, `ApiDataFetcher.py`

Sets up the foundational infrastructure to call the Teqplay REST API from within Snowflake:

1. **Network Rule** (`teqplay_api_network_rule`) — allows HTTPS egress to `api.teqplay.nl:443`
2. **Secret** (`teqplay_api_credentials`) — stores `client_id` and `client_secret` for OAuth token exchange
3. **External Access Integration** (`teqplay_api_access_integration`) — binds the network rule and secret together
4. **Python UDTF** (`fetch_teqplay_api_data`) — a table function that authenticates against the Teqplay API, fetches a given endpoint, and yields rows of `(uniqueId, name, raw_json)`

The UDTF handles token refresh automatically and is called with endpoint paths like `v1/infra/port`, `v1/infra/terminal`, and `v1/infra/berth`.

---

## 02 RAW Ingestions — Landing Raw JSON Data

**Files:** `raw_tables_creations.sql`, `ddl.sql`, `ingest_berth.sql`, `ingest_port.sql`, `ingest_terminal.sql`

Creates three raw landing tables and populates them by calling the UDTF:

| Table | API Endpoint | Description |
| --- | --- | --- |
| `raw_ports` | `v1/infra/port` | Port infrastructure records |
| `raw_terminals` | `v1/infra/terminal` | Terminal infrastructure records |
| `raw_berths` | `v1/infra/berth` | Berth infrastructure records |

Each table has columns: `UNIQUEID` (string), `NAME` (string), `RAW_JSON` (variant/string containing the full JSON payload).

Ingestion tasks run on a weekly schedule (10,080 minutes) using `MERGE` to upsert new/changed records.

---

## 03 Bronze Transformation Job — JSON Parsing (Staging)

**Files:** `stage_berth.sql`, `stage_port.sql`, `stage_terminal.sql`

Parses the `RAW_JSON` column from each raw table into strongly-typed, snake\_case columns using `PARSE_JSON()` and variant extraction. Each runs as a scheduled Snowflake Task (`MERGE INTO stg_*`).

### Key transformations:

* **stg\_berth** — Extracts 27 fields including `_id`, `name`, `nameLong`, `location` (variant), `length`, `width`, `draught`, `functionType`, `cargoCategoryType`, `ports`, etc.
* **stg\_port** — Extracts 28 fields including `unlocode`, `countryCode`, `country` (variant), `location` (variant), various area geometries, `destinations`, `deletedTimestamp`, etc.
* **stg\_terminal** — Extracts 19 fields including `displayName`, `authorityId`, `location` (variant), `mooringArea`, `functionType`, `cargoCategoryType`, etc.

All staging tables are keyed on `id` (from `_id` in the JSON).

---

## 04 Silver Transformations Job — Flattening & Reshaping (ODS)

**Files:** `ddl.sql`, `ods_berth.sql`, `ods_port.sql`, `ods_terminal.sql`

Flattens variant/nested fields from staging into simple scalar columns, preparing a clean relational structure for dimensional modeling. Each runs as a scheduled Task (`MERGE INTO ods_*`).

### Key transformations:

* **ods\_berth** — Extracts `latitude`/`longitude` from the `location` variant; maps `display_name` → `terminal`; exposes `cargo_category_type`, `function_type`; adds placeholder columns for future enrichment (`owner`, `mooring_type`, `terminal_id`)
* **ods\_port** — Extracts `latitude`/`longitude` from `location`; extracts `country.fullName` → `country_name`; keeps `unlocode` as the business key
* **ods\_terminal** — Extracts `latitude`/`longitude` from `location`; takes first element of `cargo_category_type` array; adds placeholder columns for future data (`city`, `country`, `region`, `capacity`, `terminal_company`, etc.)

---

## 05 Gold Transformation Job — Dimensional Models

**Files:** `ddl.sql`, `dim_berth.sql`, `dim_port.sql`, `dim_terminal.sql`

Creates final dimension tables by joining ODS entities together for downstream analytics. Each runs as a scheduled Task (`MERGE INTO dim_*`).

### dim\_port

* Selects from `ods_port` with quality filters: `unlocode IS NOT NULL`, `latitude IS NOT NULL`, `longitude IS NOT NULL`
* Business key: `unlocode`
* Fields: `unlocode`, `country_code`, `country_name`, `display_name`, `latitude`, `longitude`, `name`, `main_port`, `deleted_timestamp`

### dim\_terminal

* Joins `ods_terminal` with `ods_port` on `ports[0] = unlocode` to get the port display name
* Business key: `id`
* Fields: `id`, `name`, `name_with_port` (concatenated), `company`, `deleted_timestamp`

### dim\_berth

* Joins `ods_berth` with `ods_port` on `main_port = unlocode` for port context
* Business key: `id`
* Fields: `id`, `latitude`, `longitude`, `name`, `name_long`, `port`, `port_display_name`, `port_name`, `terminal`, `terminal_id`, `type` (first cargo category), `length`, `function_type`, `deleted_timestamp`

---

## Data Flow Diagram

wide760Teqplay API (api.teqplay.nl)
│
▼
┌─────────────────────────┐
│ 01 Init │ Network Rule + Secret + UDTF
└────────────┬────────────┘
│
▼
┌─────────────────────────┐
│ 02 RAW Ingestions │ raw\_ports, raw\_terminals, raw\_berths
│ (JSON payloads) │ Schedule: weekly MERGE
└────────────┬────────────┘
│
▼
┌─────────────────────────┐
│ 03 Bronze (Staging) │ stg\_port, stg\_terminal, stg\_berth
│ (Typed columns) │ Schedule: weekly MERGE
└────────────┬────────────┘
│
▼
┌─────────────────────────┐
│ 04 Silver (ODS) │ ods\_port, ods\_terminal, ods\_berth
│ (Flattened scalars) │ Schedule: weekly MERGE
└────────────┬────────────┘
│
▼
┌─────────────────────────┐
│ 05 Gold (Dimensions) │ dim\_port, dim\_terminal, dim\_berth
│ (Joined & enriched) │ Schedule: weekly MERGE
└─────────────────────────┘

---

## Scheduling

All transformation tasks run on a **weekly cadence** (10,080 minutes). Tasks are created in a suspended state and must be resumed with `ALTER TASK <name> RESUME;` to activate.

## Technology Stack

| Component | Technology |
| --- | --- |
| Compute | Snowflake Warehouse (`TEQPLAY_WH`) |
| Orchestration | Snowflake Tasks (scheduled MERGE) |
| API Access | External Access Integration + Python UDTF |
| Data Format | JSON → VARIANT → typed columns |
| Architecture | Medallion (Raw → Bronze → Silver → Gold) |