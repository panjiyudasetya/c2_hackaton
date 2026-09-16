---
id: confluence:1260879873
source: confluence
type: page
space: TC
title: Data Ingestion from REST API into Snowflake
author: Ryan Kharisma Rakhmat
date: '2026-06-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1260879873
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1260879873
---
# Data Ingestion from REST API into Snowflake

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1260879873  

## Content

# 1. Backgrounds

For our Batching Ingestions in the previous data pipeline using Airflow and Postgres RDS, most of the data are comes from the REST API of the existing teqplay systems. There are 3 different systems that we are using for data ingestion using the REST API such as: POMA, CSI and VesselVoyage. This document will guide you the experiment of data ingestion from REST API into Snowflake datawarehouse as the proof of concept for our next data pipeline.

This document demonstrates sample REST API ingestion into Snowflake. We will ingest a dummy JSON API into our data warehouse. The data that we are using are comes from this simple REST API at the URL : <https://jsonplaceholder.typicode.com> that consist of Free fake and reliable API for testing and prototyping. The API that we are hit are as below:

|  |  |  |
| --- | --- | --- |
| **Endpoint** | **Records** | **Description** |
| /posts | 100 | Blog posts with userId, title, and body |
| /users | 10 | User profiles with name, email, address, and company |
| /comments | 500 | Comments linked to posts via postId |
| /todos | 200 | Todo items with userId, title, and completion status |

For the experiment we are going to make the two approaches. First one is using only snowflake and UDF Python that will call from the worksheet of the Snowflake. The second one is using the third party tools named `Fivetran` that will be connect to the Rest API and then push the data into `Snowflake` warehouse.

**Key Finding:** The native Snowflake UDF approach is blocked on trial accounts due to the External Access Integration restriction. The Fivetran Connector SDK approach successfully bypasses this limitation by running API calls on Fivetran's own infrastructure rather than inside Snowflake's compute sandbox.

# 2. Approach 1: Native Snowflake Python UDF with External Access Integration

## 2.1 Architecture Overview

The first approach leverages Snowflake's native capability to execute Python code inside the warehouse compute environment using **User-Defined Functions (UDFs)** and **User-Defined Table Functions (UDTFs)**. To allow these functions to reach external hosts over the internet, Snowflake provides the **External Access Integration (EAI)** feature — an account-level object that whitelists specific external hosts and optionally manages authentication secrets.

The intended data flow is as follows:

* A **Network Rule** is created to whitelist the target host ([jsonplaceholder.typicode.com](http://jsonplaceholder.typicode.com))
* An **External Access Integration** is created at the account level, referencing the network rule
* Python UDFs and UDTFs are created with the EAI reference, enabling them to make outbound HTTPS calls
* Functions are called from the Snowflake worksheet, which executes them on Snowflake's warehouse compute nodes
* API responses are returned as SQL result sets (VARCHAR, VARIANT, or TABLE types)

## 2.2 Implementation Steps

**Step 1 — Account-Level Setup**

The setup begins with *SYSADMIN* privileges, as Network Rules and External Access Integrations are account-level objects that require elevated permissions:

-- Using Teqplay WH Datawarehouse

wide760USE WAREHOUSE TEQPLAY\_WH;

-- Switch to account sysadmin role

wide760USE ROLE SYSADMIN;

-- Create dedicated database and schema

wide760CREATE DATABASE IF NOT EXISTS API\_INGESTION\_PROTO;
CREATE SCHEMA  IF NOT EXISTS API\_INGESTION\_PROTO.JSONPLACEHOLDER\_CONNECTOR;
USE SCHEMA API\_INGESTION\_PROTO.JSONPLACEHOLDER\_CONNECTOR;

**Step 2 — Network Rule Definition**

A Network Rule defines which external hosts Snowflake compute is permitted to reach. The *MODE = EGRESS* setting specifies outbound traffic, and *TYPE = HOST\_PORT* identifies the destination by hostname:

wide760CREATE OR REPLACE NETWORK RULE jsonplaceholder\_network\_rule
    MODE       = EGRESS
    TYPE       = HOST\_PORT
    VALUE\_LIST = ('jsonplaceholder.typicode.com');

**Step 3 — External Access Integration**

The External Access Integration (EAI) is the account-level bridge object referenced by UDFs. Since JSONPlaceholder is a public API, no authentication secrets are required:

wide760CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION jsonplaceholder\_access\_integration
    ALLOWED\_NETWORK\_RULES           = (jsonplaceholder\_network\_rule)
    ALLOWED\_AUTHENTICATION\_SECRETS  = none
    ENABLED                         = TRUE;

**Step 4 — Python UDTF Definition**

User-Defined Table Function or `UDTF` takes an input and returns a full table as its output. With the `EAI` in place, Python UDTFs reference it via the *EXTERNAL\_ACCESS\_INTEGRATIONS* parameter. The example below is a scalar UDTF that fetches a todos by completed boolean as the filtering and returns the related completed or uncompleted records. Snowflake calls the *process()* method and yields one row per record::

wide760CREATE OR REPLACE FUNCTION get\_todos(completed boolean) returns
table (userId number, id number, title varchar, completed boolean)
LANGUAGE PYTHON
RUNTIME\_VERSION = 3.8
HANDLER = 'ApiData'
EXTERNAL\_ACCESS\_INTEGRATIONS = (apis\_access\_integration)
PACKAGES = ('requests')
AS
$$
import requests
class ApiData:
def process(self, completed):
data = requests.get("https://jsonplaceholder.typicode.com/todos").json()
for row in data:
if row["completed"] == completed:
yield (row["userId"], row["id"], row["title"], row["completed"])
$$; 

-- Call the UDF from a Snowflake worksheet

wide760select \* from table(get\_todos(FALSE));

## 2.3 Blockers and Errors Encountered

**Error 1 — External Access Not Supported on Trial Accounts**

> **SQL compilation error:** External access is not supported for trial accounts.

This error appears at Step 3 when attempting to *CREATE EXTERNAL ACCESS INTEGRATION* on a Snowflake trial account. The External Access Integration feature is restricted to paid Snowflake accounts. The restriction operates at the account tier level and cannot be bypassed through any SQL workaround within Snowflake itself.

**Error 2 — Snowflake Notebooks Also Blocked**

An alternative approach using Snowflake Notebooks — which could potentially bypass the EAI restriction by running Python in a different execution context — was also attempted. However, this produced a network-level DNS resolution failure:

> **ConnectionError:** HTTPSConnectionPool(host='[jsonplaceholder.typicode.com](http://jsonplaceholder.typicode.com)', port=443): Max retries exceeded with url: /users (Caused by NameResolutionError("Failed to resolve '[jsonplaceholder.typicode.com](http://jsonplaceholder.typicode.com)': [Errno -2] Name or service not known"))

This error confirms that Snowflake's entire compute sandbox — including both warehouse nodes and notebook instances — has outbound internet access completely blocked on trial accounts. The DNS resolution itself fails, indicating that the restriction operates at the network infrastructure level, not the application level.

## 2.4 Root Cause Analysis

The fundamental issue is a **unidirectional network boundary** enforced by Snowflake on trial accounts:

> **Trial Account Network Architecture:** Snowflake Compute (warehouse + notebooks)   → Outbound to external internet: ✗ BLOCKED (DNS resolution fails)   ← Inbound from external clients:  ✓ ALLOWED (connector, driver, APIs)  This is a deliberate security and resource-management constraint on trial tier accounts.

# 3. Approach 2: Fivetran Connector SDK

## 3.1 Architecture Overview

The second approach uses **Fivetran** — a fully managed ELT (Extract, Load, Transform) platform — as the intermediary between the REST API source and the Snowflake destination. Fivetran's Connector SDK allows engineers to write custom Python connectors that run on **Fivetran's own cloud infrastructure**, completely independent of Snowflake's compute environment. This is the key architectural distinction that bypasses the trial account limitation.

The data flow is as follows:

* A custom Python connector is written using the Fivetran Connector SDK
* The connector is tested locally on the developer's machine (which has unrestricted internet access)
* The connector is deployed to Fivetran's cloud infrastructure using the Fivetran CLI
* Fivetran executes the connector on its own servers, calling the REST API on a configurable schedule
* Fivetran pushes the ingested data into the Snowflake destination using its native Snowflake connector
* Tables are automatically created and maintained in Snowflake by Fivetran

## 3.2 Prerequisites and Initial Setup

**Fivetran Account**

A Fivetran account is required. Fivetran offers a 30-day free trial that includes full access to the Connector SDK and all destination types including Snowflake. No credit card is required to start the trial.

**Snowflake Destination Configuration**

A dedicated Fivetran user, role, and warehouse must be created in Snowflake to serve as the destination connection. For now we are using the existing warehouse and users for the connections:

-- Run as SYSADMIN in Snowflake

wide760USE ROLE SYSADMIN;

– Use existing Warehouse and create a new database

wide760USE WAREHOUSE TEQPLAY\_WH;
CREATE DATABASE IF NOT EXISTS API\_INGESTION\_PROTO;
USE DATABASE API\_INGESTION\_PROTO;

**SDK Installation**

In the local Python environment we need to install the Fivetran SDK.

# Install Fivetran Connector SDK (requires Python 3.9+)

wide760pip install fivetran-connector-sdk

# Verify installation

wide760fivetran version

## 3.3 Custom Connector Implementation

The Fivetran Connector SDK requires a Python file with two core functions: *schema()* — which defines the destination table structures — and *update()* — which contains the sync logic. Below is the complete connector for JSONPlaceholder:

# connector.py

wide760import requests
import json
from fivetran\_connector\_sdk import Connector, Operations as op, Logging as log
# ── Schema definition ──────────────────────────────────────────────────────────
def schema(configuration: dict):
"""
Tells Fivetran the table structures and primary keys.
Fivetran auto-creates these tables in Snowflake.
"""
return [
{
"table": "posts",
"primary\_key": ["id"],
"columns": {
"id": "INT",
"user\_id": "INT",
"title": "STRING",
"body": "STRING",
}
},
{
"table": "users",
"primary\_key": ["id"],
"columns": {
"id": "INT",
"name": "STRING",
"username": "STRING",
"email": "STRING",
"city": "STRING",
"company": "STRING",
}
},
{
"table": "comments",
"primary\_key": ["id"],
"columns": {
"id": "INT",
"post\_id": "INT",
"name": "STRING",
"email": "STRING",
"body": "STRING",
}
},
{
"table": "todos",
"primary\_key": ["id"],
"columns": {
"id": "INT",
"user\_id": "INT",
"title": "STRING",
"completed": "BOOLEAN",
}
},
]
# ── Sync logic ─────────────────────────────────────────────────────────────────
def update(configuration: dict, state: dict):
"""
Called by Fivetran on every scheduled sync.
`state` persists between runs for incremental logic.
`configuration` holds secrets/config from the Fivetran dashboard.
"""
base\_url = "https://jsonplaceholder.typicode.com"
headers = {"Content-Type": "application/json"}
# ── 1. Sync /posts ─────────────────────────────────────────────────────
log.info("Fetching posts...")
response = requests.get(f"{base\_url}/posts", headers=headers, timeout=30)
response.raise\_for\_status()
for post in response.json():
yield op.upsert(
table="posts",
data={
"id": post["id"],
"user\_id": post["userId"],
"title": post["title"],
"body": post["body"],
}
)
log.info(f"Synced {len(response.json())} posts")
# ── 2. Sync /users ─────────────────────────────────────────────────────
log.info("Fetching users...")
response = requests.get(f"{base\_url}/users", headers=headers, timeout=30)
response.raise\_for\_status()
for user in response.json():
yield op.upsert(
table="users",
data={
"id": user["id"],
"name": user["name"],
"username": user["username"],
"email": user["email"],
"city": user.get("address", {}).get("city", ""),
"company": user.get("company", {}).get("name", ""),
}
)
log.info(f"Synced {len(response.json())} users")
# ── 3. Sync /comments ──────────────────────────────────────────────────
log.info("Fetching comments...")
response = requests.get(f"{base\_url}/comments", headers=headers, timeout=30)
response.raise\_for\_status()
for comment in response.json():
yield op.upsert(
table="comments",
data={
"id": comment["id"],
"post\_id": comment["postId"],
"name": comment["name"],
"email": comment["email"],
"body": comment["body"],
}
)
log.info(f"Synced {len(response.json())} comments")
# ── 4. Sync /todos ─────────────────────────────────────────────────────
log.info("Fetching todos...")
response = requests.get(f"{base\_url}/todos", headers=headers, timeout=30)
response.raise\_for\_status()
for todo in response.json():
yield op.upsert(
table="todos",
data={
"id": todo["id"],
"user\_id": todo["userId"],
"title": todo["title"],
"completed": todo["completed"],
}
)
log.info(f"Synced {len(response.json())} todos")
# ── Checkpoint state (no cursor needed — full refresh every sync) ──────
yield op.checkpoint(state={
"last\_sync": "full\_refresh"
})
# ── Entrypoint ─────────────────────────────────────────────────────────────────
connector = Connector(update=update, schema=schema)
if \_\_name\_\_ == "\_\_main\_\_":
# Local debug run — writes output to ./warehouse/ folder
connector.debug()

## 3.4 Local Testing with fivetran debug

Before deploying, the connector is validated locally. The *fivetran debug* command simulates the Fivetran runtime on the developer's local machine and writes output to a local DuckDB warehouse file:

# Run local debug — simulates full Fivetran sync

wide760fivetran debug --configuration configuration.json

# Expected output:

# INFO  Fetching posts...     → 100 rows synced

# INFO  Fetching users...     →  10 rows synced

# INFO  Fetching comments...  → 500 rows synced

# INFO  Fetching todos...     → 200 rows synced

# INFO  Sync SUCCEEDED

**✅ Local debug succeeded.** All 810 total records (100 posts + 10 users + 500 comments + 200 todos) were correctly fetched from the live API and written to the local warehouse simulation. This confirms the connector logic is correct before cloud deployment.

## 3.5 Deployment to Fivetran Cloud

**Step 1 — Create new destinations in Fivetran**

The Fivetran Destination to the Snowflake should be created first as below `Warehouse` destinations:

**Step 2 — Deploy with Correct CLI Syntax**

An important API change in recent Fivetran SDK versions: the **--api-secret** flag was removed. The correct syntax uses only **--api-key** with the base64-encoded combined value:

# INCORRECT (old syntax — will throw "unrecognized arguments" error)

wide760fivetran deploy --api-key KEY --api-secret SECRET ...

# CORRECT (new syntax — single base64-encoded combined key)

wide760fivetran deploy \
    --api-key $FIVETRAN\_API\_KEY \
    --destination Warehouse \
    --connection jsonplaceholder\_connector \
    --configuration configuration.json

The **--destination** flag refers to the **Fivetran destination name** — the name assigned to the Snowflake connection inside the Fivetran dashboard (found under Destinations page), ***not*** the Snowflake database or warehouse name. The **--configuration** flag explicitly points to the configuration file, preventing a warning about the file being present but not used.

**Step 3 — Successful Deployment Output**

wide760INFO  Fivetran-Connector-SDK: Deploying project to connection
      'jsonplaceholder\_connector' in destination 'Warehouse'.
INFO  Fivetran-Connector-SDK: Packaging your project for upload...
INFO  Fivetran-Connector-SDK: Uploading your project...
INFO  Fivetran-Connector-SDK: The connection has been created successfully.
INFO  Fivetran-Connector-SDK: Python Version: 3.13.x
INFO  Fivetran-Connector-SDK: Connection ID: supplementary\_unacquainted
INFO  Visit: https://fivetran.com/dashboard/connections/.../status

**Step 4 — Enable and sync the connector**

## 3.6 Querying Data in Snowflake After Sync

After the first sync completes, Fivetran automatically creates a schema in the destination database named after the connection. All four tables are available for querying immediately:

-- Fivetran auto-creates schema: FIVETRAN\_DB.JSONPLACEHOLDER\_CONNECTOR

wide760USE DATABASE API\_INGESTION\_PROTO;

-- Check table on the Database

wide760SHOW TABLES IN DATABASE API\_INGESTION\_PROTO;

-- All tables available

wide760SELECT \* FROM JSONPLACEHOLDER\_CONNECTOR.POSTS ORDER BY id LIMIT 10;
SELECT \* FROM JSONPLACEHOLDER\_CONNECTOR.USERS ORDER BY id;
SELECT \* FROM JSONPLACEHOLDER\_CONNECTOR.COMMENTS WHERE post\_id = 1;
SELECT \* FROM JSONPLACEHOLDER\_CONNECTOR.TODOS where completed = TRUE;

 The result of number 4 query below here in Snowflake:

-- Cross-endpoint JOIN

wide760SELECT
u.name,
u.company,
p.id AS post\_id, p.title
FROM JSONPLACEHOLDER\_CONNECTOR.POSTS p
JOIN JSONPLACEHOLDER\_CONNECTOR.USERS u ON p.user\_id = u.id;

# 4. Comparative Analysis

## 4.1 Side-by-Side Comparison

|  |  |  |
| --- | --- | --- |
| **Dimension** | **Approach 1: Snowflake Native UDF** | **Approach 2: Fivetran Connector SDK** |
| **Works on trial account** | ❌ Blocked — EAI not supported | ✅ Fully supported |
| **API call location** | Inside Snowflake compute (blocked on trial) | Fivetran cloud infra (unrestricted) |
| **Setup complexity** | Low — pure SQL + Python in worksheet | Medium — SDK install, CLI, deploy flow |
| **Scheduling / automation** | Manual or via Snowflake Tasks | Built-in, configurable (5 min to 24 hr) |
| **Schema management** | Manual DDL required | Auto-created and maintained by Fivetran |
| **Incremental sync support** | Manual cursor/state logic required | Built-in state management via checkpoint |
| **Real-time / ad-hoc queries** | ✅ Yes — UDF called inline in SQL | ❌ No — batch sync only |
| **Cost model** | Snowflake compute credits per call | Fivetran MAR-based pricing + Snowflake load |
| **Production readiness** | High — native, no external dependencies | High — managed infrastructure, monitoring built-in |
| **Best suited for** | Ad-hoc API enrichment, real-time UDF calls, single-query lookups | Recurring ETL pipelines, multi-table ingestion, production data flows |

## 4.2 Architectural Trade-offs

**When to Choose the Snowflake Native UDF Approach**

1. The use case requires **real-time or on-demand API calls** embedded within SQL queries (e.g., enriching a result set with live API data per row)
2. The team wants to minimize external dependencies and keep all logic within the Snowflake ecosystem
3. The organization has a **paid Snowflake account** where External Access Integration is available
4. API call volume is low and Snowflake compute cost per call is acceptable
5. The data does not need to be persisted — only consumed during query execution

**When to Choose the Fivetran Connector SDK Approach**

1. A **scheduled, recurring sync** is needed (e.g., daily refresh of API data into the warehouse)
2. Multiple API endpoints need to be ingested and stored as structured, queryable Snowflake tables
3. The team wants automatic schema management, monitoring, and alerting without building infrastructure
4. The environment is a Snowflake trial account or any context where EAI is unavailable
5. The pipeline needs to be maintainable by multiple engineers over time with a clear deployment process

# 5. Lessons Learned and Key Takeaways

## 5.1 Technical Lessons

1. **Trial account limitations are network-level, not application-level.**

The DNS resolution failure in Snowflake Notebooks confirmed that the egress restriction on trial accounts operates at the infrastructure network layer. No amount of Python-level workarounds (retries, alternative HTTP libraries, proxy settings) can bypass a DNS block at the compute node level. The only viable workarounds are: (a) upgrade the Snowflake account, or (b) move compute outside of Snowflake.

2. **Local debug is an essential validation step before cloud deployment.**

The *fivetran debug* command runs the connector entirely on the local machine, which has unrestricted internet access. This makes it possible to validate connector logic, schema definitions, and data transformations before deploying to Fivetran's cloud. Skipping this step and deploying directly risks discovering logic errors only after waiting for a cloud sync cycle to complete.

## 5.2 Architectural Lessons

1. The two approaches are **complementary, not competing**. Snowflake UDFs are optimized for real-time, inline API enrichment. Fivetran is optimized for scheduled, persistent data pipeline management.
2. For production REST API ingestion pipelines, **Fivetran (or similar managed ELT tools e.g Airflow)** is the more appropriate choice due to built-in scheduling, monitoring, schema evolution handling, and operational reliability.
3. The Snowflake UDF approach becomes attractive for **event-driven enrichment** scenarios — where a SQL query needs to dynamically call an API per row at query time rather than batch-loading data upfront.

# 6. Conclusion

This experiment successfully implemented and compared two distinct approaches for ingesting REST API data into a Snowflake Data Warehouse. While the **native Snowflake UDF approach** represents the more elegant, dependency-free architectural pattern, it is categorically unavailable on Snowflake trial accounts due to the External Access Integration restriction — a limitation that operates at the compute network infrastructure level and cannot be worked around through any SQL or Python technique within Snowflake itself.

The **Fivetran Connector SDK approach** proved to be a robust, production-appropriate alternative that completely bypasses the Snowflake trial restriction. By executing API calls on Fivetran's own cloud infrastructure rather than inside Snowflake's compute environment, it decouples the network egress concern from the warehouse tier. The resulting data pipeline is fully managed, automatically scheduled, and delivers structured, queryable tables to the Snowflake destination without any manual DDL or infrastructure management.

For engineers building real-world data pipelines that ingest REST API data into Snowflake, the choice between these approaches should be guided by the **query pattern** (real-time vs. batch), **account tier** (trial vs. paid), and **operational requirements** (ad-hoc enrichment vs. recurring scheduled sync). Both approaches are valid in their appropriate contexts, and a mature data platform may employ both simultaneously.

**Recommendation:** For production scheduled ingestion pipelines on any Snowflake tier → use Fivetran Connector SDK or equivalent managed ELT tool. For real-time inline API enrichment on paid Snowflake accounts → use native Python UDFs with External Access Integration.

# References

Snowflake Documentation. (2025). CREATE EXTERNAL ACCESS INTEGRATION. Snowflake Inc. <https://docs.snowflake.com/sql-reference/sql/create-external-access-integration>

Snowflake Documentation. (2025). External Network Access Overview. Snowflake Inc. <https://docs.snowflake.com/developer-guide/external-network-access/creating-using-external-network-access>

Snowflake Documentation. (2025). Python UDF Handler. Snowflake Inc. <https://docs.snowflake.com/developer-guide/udf/python/udf-python-introduction>

Fivetran Documentation. (2025). Connector SDK Setup Guide. Fivetran Inc. <https://fivetran.com/docs/connector-sdk/setup-guide>

Fivetran Documentation. (2025). Connector SDK CLI Commands. Fivetran Inc. <https://fivetran.com/docs/connector-sdk/working-with-connector-sdk>

Fivetran Documentation. (2025). Fivetran REST API — Getting Started. Fivetran Inc. <https://fivetran.com/docs/rest-api/getting-started>

Fivetran Documentation. (2025). Connector SDK Beginner's Tutorial. Fivetran Inc. <https://fivetran.com/docs/connector-sdk/tutorials/beginners-tutorial>

Fivetran GitHub. (2025). fivetran/connector\_sdk — Example Connectors Repository. <https://github.com/fivetran/fivetran_connector_sdk>

JSONPlaceholder. (2025). Free Fake REST API for Testing. <https://jsonplaceholder.typicode.com>