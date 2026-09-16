---
id: confluence:1267564545
source: confluence
type: page
space: TC
title: Snowflake Data Exposure for Internal Applications
author: Panji Y. Wiwaha
date: '2026-07-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1267564545
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1267564545
---
# Snowflake Data Exposure for Internal Applications

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1267564545  

## Content

# **Exploration Report: Snowflake Data Exposure for Internal Applications**

## **1. Exploration Summary**

This report evaluates three architectural approaches for exposing curated data from `TEQPLAY_MART.GOLD` to internal applications at Teqplay. The evaluation addresses the need to serve both BI consumers (Power BI) and programmatic API consumers (internal microservices) with governed, performant, and maintainable data access.

Three approaches were evaluated:

| Method | Primary Consumer | Focus | Status |
| --- | --- | --- | --- |
| **Direct SQL Access (JDBC/ODBC)** | Power BI, analytical tools | Native BI connectivity, RBAC, driver overhead | Evaluated. Recommended for BI |
| **SQL API + Materialized Views** | REST clients, automation scripts | Low-latency programmatic access to pre-computed data | Evaluated. Viable for lightweight integrations |
| **FastAPI on SPCS** | Internal microservices, developer teams | Standardized, documented, governed REST API layer | Evaluated. Recommended as primary programmatic path |

The central finding: **JDBC/ODBC** and **FastAPI on SPCS** serve fundamentally different consumer archetypes and are not interchangeable. The **SQL API + Materialized Views** combination offers a useful middle ground but has a significant developer experience limitation detailed in Section 4.2.

## **2. Background & Objective**

The question driving this exploration:

> ***How should Teqplay provide governed, discoverable, and maintainable access to*** `TEQPLAY_MART.GOLD` ***for both BI dashboards and internal API consumers without building and operating a separate data infrastructure layer outside Snowflake?***

As the `GOLD` schema becomes Teqplay's main curated reporting layer, two consumer types have emerged:

1. **BI Authors (Power BI)**. Require a native SQL connectivity, interactive queries, and role-based data scoping with low operational overhead.
2. **Backend Engineers / API consumers**. Require a REST API with structured request/response schemas, discoverable documentation (Swagger/OpenAPI), and the ability to apply custom business logic before returning data.

Serving both groups with the same method is unworkable. BI tools benefit from native drivers and Snowflake's query optimizer. REST API consumers require standardized contracts, versioned endpoints, and clear documentation, none of which Snowflake's SQL API provides natively. This exploration separates these concerns and evaluates dedicated solutions for each.

## **3. Methods Under Exploration**

| Method | Security Model | Performance | Developer Experience | Deployment Complexity |
| --- | --- | --- | --- | --- |
| **JDBC/ODBC** | Role-based + network policy | High (native driver) | Simple. Connector UI in Power BI | None. No server to deploy |
| **SQL API + Materialized Views** | JWT/OAuth + role-scoped queries | Very high (pre-computed MVs) | Poor. No Swagger UI, raw HTTP only | None. Serverless Snowflake endpoint |
| **FastAPI on SPCS** | JWT/OAuth + application-level auth | High (MV-backed, connection pool) | Excellent. Auto-generated Swagger/ReDoc | Medium. Deployed on SPCS or AWS ECS. |

Section 4 explores each method in depth, covering its access model, observed trade-offs, and reference code and SQL for `TEQPLAY_MART.GOLD`.

## **4. Technical Exploration of Methods**

### **4.1 Method 1: Direct SQL Access (JDBC/ODBC)**

#### **Why This Method Was Considered**

JDBC/ODBC is the natural access path for BI tools. Power BI, Tableau, and similar tools include Snowflake connectors using native database protocols. Routing Power BI through an intermediate API layer adds latency and requires maintaining a translation service that provides no analytical value. The key question was not whether JDBC/ODBC was viable, but how to scope it safely, especially regarding access boundaries, RBAC, and compute isolation.

#### **How It Works**

The consuming application connects to Snowflake via the JDBC or ODBC driver, authenticating with a service account tied to a scoped role. All queries run on `TEQPLAY_REPORT_WH` and access only `TEQPLAY_MART.GOLD` objects. The driver manages connection pooling, result pagination, and type mapping.

markdownwide760Power BI → ODBC Driver → TEQPLAY\_REPORT\_WH → TEQPLAY\_MART.GOLD (role-scoped)

The most critical design decision is **role scoping**. A dedicated role (`POWERBI_READER`) has only the necessary privileges, such as `SELECT` on `TEQPLAY_MART.GOLD` and warehouse usage. The service account cannot escalate beyond its assigned role.

sqlwide760-- Create dedicated service account for the application
CREATE USER svc\_powerbi
PASSWORD = '<strong\_password>'
DEFAULT\_ROLE = 'POWERBI\_READER'
DEFAULT\_WAREHOUSE = 'TEQPLAY\_REPORT\_WH'
COMMENT = 'Service account for Power BI integration';
-- Enable MFA for production (optional but recommended)
ALTER USER svc\_powerbi SET MINS\_TO\_BYPASS\_MFA = 0;
sqlwide760-- Create application-specific role
CREATE ROLE POWERBI\_READER
COMMENT = 'Read-only access for Power BI';
-- Grant warehouse usage
GRANT USAGE ON WAREHOUSE TEQPLAY\_REPORT\_WH TO ROLE POWERBI\_READER;
-- Grant database and schema access
GRANT USAGE ON DATABASE TEQPLAY\_MART TO ROLE POWERBI\_READER;
GRANT USAGE ON SCHEMA TEQPLAY\_MART.GOLD TO ROLE POWERBI\_READER;
-- Grant table-level SELECT permissions
GRANT SELECT ON ALL TABLES IN SCHEMA TEQPLAY\_MART.GOLD TO ROLE POWERBI\_READER;
GRANT SELECT ON FUTURE TABLES IN SCHEMA TEQPLAY\_MART.GOLD TO ROLE POWERBI\_READER;
-- Grant to service account
GRANT ROLE POWERBI\_READER TO USER svc\_powerbi;

#### **Compute Isolation**

A dedicated warehouse with a credit quota guard is essential. Without it, costly Power BI queries compete with production pipelines. `AUTO_SUSPEND = 60` shuts the warehouse down when idle.

sqlwide760-- Create dedicated warehouse with auto-suspend
CREATE WAREHOUSE TEQPLAY\_REPORT\_WH WITH
WAREHOUSE\_SIZE = 'SMALL'
AUTO\_SUSPEND = 60 -- suspend after 1 minute of inactivity
AUTO\_RESUME = TRUE
INITIALLY\_SUSPENDED = TRUE
COMMENT = 'Dedicated warehouse for reporting tools';
-- Set resource monitor
CREATE RESOURCE MONITOR TEQPLAY\_REPORT\_WH\_LIMIT WITH
CREDIT\_QUOTA = 100 -- monthly credit limit
TRIGGERS
ON 90 PERCENT DO NOTIFY
ON 100 PERCENT DO SUSPEND;
ALTER WAREHOUSE TEQPLAY\_REPORT\_WH SET RESOURCE\_MONITOR = TEQPLAY\_REPORT\_WH\_LIMIT;

Power BI Snowflake connector connection parameters:

markdownwide760# JDBC Connection String
jdbc:snowflake://<account>.snowflakecomputing.com/?warehouse=TEQPLAY\_REPORT\_WH&db=TEQPLAY\_MART&schema=GOLD
# ODBC Connection Parameters
Server: <account>.snowflakecomputing.com
Database: TEQPLAY\_MART
Schema: GOLD
Warehouse: TEQPLAY\_REPORT\_WH
Role: POWERBI\_READER

#### **Performance considerations: RBAC and driver overhead**

The JDBC/ODBC driver converts Power BI's query model into SQL for Snowflake. Two patterns cause significant overhead:

1. **DirectQuery mode without Materialized Views**. Power BI sends a new SQL query on every visual interaction, scanning raw fact tables each time. Pointing DirectQuery at Materialized Views (pre-computed KPI aggregations in `TEQPLAY_MART.GOLD`) removes this overhead and is recommended.
2. **Over-permissive role grants**. A role with `SELECT` on all tables in `TEQPLAY_MART.GOLD` lets Power BI join and aggregate across all objects. Narrowing grants to specific Materialized Views or Secure Views restricts the BI tool to a controlled data surface

#### **Assessment**

| Dimension | Observation |
| --- | --- |
| **Fit for Power BI** | Excellent. It’s a native connector, no translation layer. |
| **Security** | Strong when role-scoped correctly; the risk is governance, not protocol |
| **Performance** | Depends on query quality; pairing with Materialized Views is critical |
| **Cost** | Pay-per-query; auto-suspend bounds idle cost |
| **Standardization** | None. Power BI defines its own query patterns |
| **Swagger / API docs** | Not applicable. native database protocol |
| **Operational overhead** | Very low. No middleware, no deployment |

JDBC/ODBC suits Power BI but does not meet backend engineers' needs for a discoverable, structured REST API. These approaches serve fundamentally different users and do not compete.

### **4.2 Method 2: SQL API + Materialized Views**

#### **Why This Method Was Considered**

Internal automation scripts and lightweight integrations sometimes need to query Snowflake data over HTTP without deploying a full application server. Snowflake's SQL API enables this: a single HTTPS `POST` can authenticate, execute a SQL statement, and return JSON results. Using Materialized Views addresses the main performance concern: instead of executing costly live aggregations at request time, the API queries pre-computed, scan-free result sets.

This method was evaluated to assess its viability as a quick-start path for API consumers before justifying a full FastAPI deployment (Section 4.3).

#### **How It Works**

The caller submits a SQL statement to Snowflake's HTTPS endpoint using JWT (RSA key-pair) for authentication. Results return as paginated JSON. The caller never holds an open database connection.

markdownwide760API Consumer → HTTPS POST (JWT) → Snowflake SQL API → TEQPLAY\_MART.GOLD Materialized View

Targeting materialized views instead of raw tables significantly reduces query execution time, as the warehouse reads pre-computed partitions rather than scanning and aggregating raw fact data on demand.

sqlwide760-- Create materialized view for monthly KPI summary
CREATE MATERIALIZED VIEW TEQPLAY\_MART.GOLD.monthly\_kpi AS
SELECT
pv.calendar\_month,
...
FROM TEQPLAY\_MART.PUBLIC.fact\_port\_visit pv
WHERE pv.calendar\_month <= DATEADD('month', -1, DATE\_TRUNC('month', CURRENT\_DATE()))
GROUP BY DATE(pv.calendar\_month);
-- Enable automatic refresh
ALTER MATERIALIZED VIEW TEQPLAY\_MART.GOLD.monthly\_kpi RESUME;

For aggregations not requiring real-time freshness, a scheduled task refresh during off-peak hours costs less than continuous automatic refresh:

sqlwide760-- Schedule refresh during off-peak hours
CREATE TASK refresh\_monthly\_kpi\_mv
WAREHOUSE = TEQPLAY\_REPORT\_WH
SCHEDULE = 'USING CRON 0 2 \* \* \* UTC' -- every day at 02:00 UTC
AS
ALTER MATERIALIZED VIEW TEQPLAY\_MART.GOLD.monthly\_kpi REFRESH;
ALTER TASK refresh\_monthly\_kpi\_mv RESUME;

API role scoped to read only from the `TEQPLAY_MART.GOLD` schema, excluding base tables:

sqlwide760CREATE ROLE API\_SERVICE\_ROLE
COMMENT = 'Scoped role for SQL API programmatic access';
GRANT USAGE ON WAREHOUSE TEQPLAY\_REPORT\_WH TO ROLE API\_SERVICE\_ROLE;
GRANT USAGE ON DATABASE TEQPLAY\_MART TO ROLE API\_SERVICE\_ROLE;
GRANT USAGE ON SCHEMA TEQPLAY\_MART.GOLD TO ROLE API\_SERVICE\_ROLE;
GRANT SELECT ON ALL VIEWS IN SCHEMA TEQPLAY\_MART.GOLD TO ROLE API\_SERVICE\_ROLE;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA TEQPLAY\_MART.GOLD TO ROLE API\_SERVICE\_ROLE;
CREATE USER svc\_api\_client
PASSWORD = '<strong\_password>'
DEFAULT\_ROLE = 'API\_SERVICE\_ROLE'
DEFAULT\_WAREHOUSE = 'TEQPLAY\_REPORT\_WH';
GRANT ROLE API\_SERVICE\_ROLE TO USER svc\_api\_client;

RSA key-pair authentication for JWT issuance:

sqlwide760-- openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa\_key.p8 -nocrypt
-- openssl rsa -in rsa\_key.p8 -pubout -out rsa\_key.pub
ALTER USER svc\_api\_client SET RSA\_PUBLIC\_KEY='MIIBIjANBgkqhki...';

Python reference implementation for synchronous and asynchronous SQL API calls:

pywide760import requests
import jwt
import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default\_backend
SNOWFLAKE\_ACCOUNT = "myorg-myaccount"
SNOWFLAKE\_USER = "svc\_api\_client"
PRIVATE\_KEY\_PATH = "rsa\_key.p8"
def generate\_jwt\_token():
with open(PRIVATE\_KEY\_PATH, "rb") as key\_file:
private\_key = serialization.load\_pem\_private\_key(
key\_file.read(), password=None, backend=default\_backend()
)
now = int(time.time())
payload = {
"iss": f"{SNOWFLAKE\_ACCOUNT}.{SNOWFLAKE\_USER}.SHA256:{public\_key\_fingerprint}",
"sub": f"{SNOWFLAKE\_ACCOUNT}.{SNOWFLAKE\_USER}",
"iat": now,
"exp": now + 3600,
}
return jwt.encode(payload, private\_key, algorithm="RS256")
def execute\_sql\_api(sql\_statement):
url = f"https://{SNOWFLAKE\_ACCOUNT}.snowflakecomputing.com/api/v2/statements"
headers = {
"Authorization": f"Bearer {generate\_jwt\_token()}",
"Content-Type": "application/json",
"Accept": "application/json",
"X-Snowflake-Authorization-Token-Type": "KEYPAIR\_JWT",
}
body = {
"statement": sql\_statement,
"timeout": 60,
"database": "TEQPLAY\_MART",
"schema": "GOLD",
"warehouse": "TEQPLAY\_REPORT\_WH",
"role": "API\_SERVICE\_ROLE",
}
response = requests.post(url, json=body, headers=headers)
return response.json()
# Query the pre-computed Materialized View — fast, scan-free
result = execute\_sql\_api(
"SELECT \* FROM TEQPLAY\_MART.GOLD.monthly\_kpi WHERE sale\_date >= DATEADD(day, -30, CURRENT\_DATE())"
)
print(result)

Use asynchronous polling for long exports or large result sets:

pywide760def submit\_async\_query(sql\_statement):
url = f"https://{SNOWFLAKE\_ACCOUNT}.snowflakecomputing.com/api/v2/statements"
body = {
"statement": sql\_statement,
"async": True,
"database": "TEQPLAY\_MART",
"schema": "GOLD",
"warehouse": "TEQPLAY\_REPORT\_WH",
}
response = requests.post(url, json=body, headers=headers)
return response.json()["statementHandle"]
def check\_query\_status(statement\_handle):
url = f"https://{SNOWFLAKE\_ACCOUNT}.snowflakecomputing.com/api/v2/statements/{statement\_handle}"
response = requests.get(url, headers=headers)
return response.json()
def get\_query\_results(statement\_handle):
status = check\_query\_status(statement\_handle)
if status.get("statementStatusUrl"):
result\_url = status["statementStatusUrl"]
response = requests.get(
f"https://{SNOWFLAKE\_ACCOUNT}.snowflakecomputing.com{result\_url}",
headers=headers,
)
return response.json()
return None

#### **Limitation: No native Swagger / OpenAPI UI**

This is the main developer experience gap identified during this exploration and the key reason for Method 3.

Snowflake's SQL API is a raw HTTP API. It **does not** provide a native Swagger UI, ReDoc page, or interactive endpoint explorer at a Snowflake-hosted URL. There is no `/api/v2/docs` or equivalent for developers to inspect endpoints, try requests, or view response schemas.

Snowflake publishes a static OpenAPI specification in its official documentation. However, it describes the **transport protocol** (how to submit a SQL statement and receive rows), not the **data schemas** returned by specific queries against `TEQPLAY_MART.GOLD`.

In practice, this means:

* A backend engineer using the SQL API has **no self-service documentation** for the data structure returned by a query. They must inspect the Materialized View DDL in Snowflake.
* Response schemas change **silently** when the Materialized View definition changes. This means the API boundary does not enforce a contract.
* Every consumer must understand the Snowflake JWT auth flow, the pagination model (10,000 rows per page), and the row/column mapping format. This is a significant integration burden for engineers unfamiliar with Snowflake.
* There is no built-in mechanism for request parameter validation, rate limiting, or structured application-level error responses beyond raw SQL execution errors.

This limitation does not make the SQL API unusable. For internal scripts and lightweight automations by Snowflake-familiar engineers, it is efficient and zero-ops. However, it makes the SQL API a poor foundation for a **team-facing data API product** where discoverability, versioning, and documentation are essential.

This finding directly motivates Method 3.

#### **Assessment**

| Dimension | Observation |
| --- | --- |
| **Consumer fit** | Internal scripts, automation, lightweight one-off integrations |
| **Performance** | Excellent when targeting MVs. Pre-computed results eliminate aggregation overhead |
| **Data freshness** | Bounded by MV refresh schedule (typically hourly or daily) |
| **Standardization** | None. Raw SQL submitted by caller; no schema enforcement |
| **Swagger / API docs** | Not available. No hosted interactive UI; static OpenAPI spec for transport only |
| **Security** | JWT auth is strong; data access governed by role scoping |
| **Result volume** | Limited to 10,000 rows per page; large exports require a pagination loop |
| **Operational overhead** | Very low. It’s a serverless; no application to deploy or maintain |

The SQL API and Materialized Views suit operational simplicity and internal engineers familiar with Snowflake and JWT auth. They are **not** suitable for consumers needing a documented, versioned, stable data API with application-level business logic.

### **4.3 Method 3: Custom Backend Application (FastAPI on SPCS)**

#### **Why This Method Was Considered**

The SQL API exploration (Section 4.2) revealed a key limitation: no native Swagger UI, no schema contract at the API boundary, and no way to apply business logic between caller and data. Each consumer must manage JWT authentication, result pagination, and schema understanding independently—acceptable for internal scripts but unsuitable for a team-facing data API product.

A custom backend application on Snowpark Container Services (SPCS) fills these gaps. FastAPI, a Python web framework, offers:

* Automatic Swagger UI (`/docs`) and ReDoc (`/redoc`) generated from type annotations. This means no extra tooling is needed
* Request parameter validation via Pydantic models before issuing queries
* Structured JSON error responses with meaningful HTTP status codes
* Ability to encode business rules, data transformations, and multi-step query workflows in application code

SPCS keeps this application within Snowflake's trust boundary. An OAuth token injects into the container environment at runtime, removing the need to manage external credentials or key rotation. The service connects to `TEQPLAY_MART.GOLD` via Snowpark Python with the injected token. Therefore, the container holds no Snowflake secrets.

#### **Architecture**

Custom Backend Application Archittecture

#### **FastAPI Service Implementation**

A minimal FastAPI service querying `TEQPLAY_MART.GOLD` using Snowpark Python. Inside SPCS, the OAuth token is read from the container's injected token file; for local development, explicit credentials can be used.

pywide760from fastapi import FastAPI, Query, HTTPException
from snowflake.snowpark import Session
import os
app = FastAPI(
title="Teqplay KPI Data API",
description="Governed REST API for TEQPLAY\_MART.GOLD data surfaces.",
version="1.0.0",
)
def get\_snowflake\_session() -> Session:
"""
Inside SPCS: connects via OAuth token injected at /snowflake/session/token.
Outside SPCS: falls back to environment-variable credentials for local dev.
"""
token\_path = "/snowflake/session/token"
if os.path.exists(token\_path):
with open(token\_path) as f:
token = f.read().strip()
params = {
"account": os.environ["SNOWFLAKE\_ACCOUNT"],
"host": os.environ.get("SNOWFLAKE\_HOST", ""),
"authenticator": "oauth",
"token": token,
"database": "TEQPLAY\_MART",
"schema": "GOLD",
"warehouse": "TEQPLAY\_REPORT\_WH",
"role": os.environ.get("SNOWFLAKE\_ROLE", "API\_SERVICE\_ROLE"),
}
else:
params = {
"account": os.environ["SNOWFLAKE\_ACCOUNT"],
"user": os.environ["SNOWFLAKE\_USER"],
"password": os.environ["SNOWFLAKE\_PASSWORD"],
"database": "TEQPLAY\_MART",
"schema": "GOLD",
"warehouse": "TEQPLAY\_REPORT\_WH",
}
return Session.builder.configs(params).create()
@app.get("/health")
def health():
return {"status": "ok"}
@app.get("/kpi/monthly-summary")
def monthly\_summary(
region: str | None = Query(default=None, description="Filter by region code"),
days: int = Query(default=30, ge=1, le=365, description="Lookback window in days"),
):
"""
Returns pre-computed daily KPI summary from `TEQPLAY\_MART.GOLD.monthly\_kpi`.
Swagger UI automatically renders this docstring, parameter types, and response schema.
"""
session = get\_snowflake\_session()
try:
region\_filter = f"AND region = '{region}'" if region else ""
query = f"""
SELECT \*
FROM TEQPLAY\_MART.GOLD.monthly\_kpi
WHERE calendar\_month < CURRENT\_DATE()
{region\_filter}
ORDER BY calendar\_month DESC
"""
return session.sql(query).to\_pandas().to\_dict(orient="records")
except Exception as e:
raise HTTPException(status\_code=500, detail=str(e))
finally:
session.close()

The Swagger UI is available at `https://<spcs-ingress-endpoint>/docs` once the service runs. No extra tooling or documentation is needed.

#### **SPCS Service Specification**

FastAPI services require an `endpoints` block in the SPCS spec to expose HTTP ingress. This distinguishes them from background consumer services, like the AMQP consumer, which have no inbound traffic.

yamlwide760spec:
containers:
- name: kpi-api
image: <org>-<account>.registry.snowflakecomputing.com/kpi\_db/gold/spcs\_repo/kpi-fastapi-api:latest
env:
SNOWFLAKE\_ACCOUNT: "<your-snowflake-account>"
SNOWFLAKE\_ROLE: "API\_SERVICE\_ROLE"
SNOWFLAKE\_WAREHOUSE: "TEQPLAY\_REPORT\_WH"
SNOWFLAKE\_DATABASE: "TEQPLAY\_MART"
SNOWFLAKE\_SCHEMA: "GOLD"
resources:
requests:
memory: "512Mi"
cpu: "0.5"
limits:
memory: "1Gi"
cpu: "1"
endpoints:
- name: api
port: 8000
public: true

Supporting Snowflake objects required before service creation:

sqlwide760-- Image repository for the FastAPI Docker image
CREATE IMAGE REPOSITORY IF NOT EXISTS TEQPLAY\_MART.GOLD.spcs\_repo;
-- Compute pool: CPU\_X64\_XS is sufficient for a lightweight REST API
CREATE COMPUTE POOL IF NOT EXISTS kpi\_api\_pool
MIN\_NODES = 1
MAX\_NODES = 2
INSTANCE\_FAMILY = CPU\_X64\_XS
AUTO\_RESUME = TRUE
AUTO\_SUSPEND\_SECS = 300;
-- Stage for the service spec YAML
CREATE STAGE IF NOT EXISTS TEQPLAY\_MART.GOLD.spcs\_stage;
-- Deploy the service (after uploading kpi-fastapi-service.yaml to the stage)
CREATE SERVICE TEQPLAY\_MART.GOLD.kpi\_api\_svc
IN COMPUTE POOL kpi\_api\_pool
FROM @TEQPLAY\_MART.GOLD.spcs\_stage
SPEC = 'kpi-fastapi-service.yaml'
MIN\_INSTANCES = 1
MAX\_INSTANCES = 2;
-- Monitor service status and retrieve the public ingress URL
SHOW SERVICES IN SCHEMA TEQPLAY\_MART.GOLD;
SHOW ENDPOINTS IN SERVICE TEQPLAY\_MART.GOLD.kpi\_api\_svc;
CALL SYSTEM$GET\_SERVICE\_LOGS('TEQPLAY\_MART.GOLD.kpi\_api\_svc', '0', 'kpi-api', 100);

#### **SQL API vs. FastAPI on SPCS**

| Dimension | SQL API (raw) | FastAPI on SPCS |
| --- | --- | --- |
| **Swagger / interactive docs** | Not available | Auto-generated at `/docs` |
| **Business logic** | Raw SQL passthrough | Enforced in an application layer |
| **Request validation** | None | Pydantic type-checking on all parameters |
| **Error responses** | Raw Snowflake execution errors | Structured JSON with HTTP status codes |
| **Versioning** | Not supported | HTTP path versioning (`/v1/`, `/v2/`) |
| **Consumer knowledge required** | JWT auth, pagination, Snowflake SQL | Standard HTTP. No Snowflake knowledge needed |
| **Deployment complexity** | None (serverless) | SPCS compute pool + image build and push |
| **Operational cost** | Pay-per-query only | Compute pool cost + per-query cost |
| **Auth model** | JWT per request (caller-managed) | OAuth token (SPCS-injected, zero-config) |

#### **Assessment**

| Dimension | Observation |
| --- | --- |
| **Standardization** | Excellent. HTTP semantics, versioned paths, Pydantic-enforced schemas |
| **Swagger / API docs** | Auto-generated by FastAPI. Zero additional documentation effort |
| **Business logic** | Can encode access rules, data transforms, and multi-step query workflows |
| **Consumer experience** | Any HTTP client works; no Snowflake knowledge required by the consumer |
| **Deployment complexity** | Higher than the raw SQL API. It will requires image registry, compute pool, and SPCS service lifecycle management |
| **Operational cost** | Compute pool runs continuously; idle cost applies even between requests |
| **When justified** | When the API is a product: multiple consumers, versioning requirements, or governance rules that cannot live in a Secure View |

FastAPI on SPCS suits data APIs that must be discoverable, versioned, and documented as first-class products. Deployment overhead is justified when multiple internal teams use the API or when business logic belongs in the application layer rather than SQL views.

## **5. Comparative Analysis**

After exploring all three methods, the matrix below summarises their performance across the dimensions most relevant to Teqplay's data access requirements:

| Dimension | JDBC/ODBC | SQL API + Materialized Views | FastAPI on SPCS |
| --- | --- | --- | --- |
| **Primary consumer** | Power BI, BI tools | Internal scripts, lightweight automation | Backend services, multi-team APIs |
| **Data freshness** | Real-time | Bounded by MV refresh schedule | Depends on the underlying view |
| **Latency** | Low (native driver) | Low (MV scan-free reads) | Low (MV-backed) + HTTP overhead |
| **Standardization** | None. BI tool controls queries | None. Raw SQL from caller | Versioned HTTP endpoints, Pydantic schemas |
| **Swagger / API docs** | Not applicable | No hosted interactive UI | Auto-generated at `/docs` |
| **Business logic** | None | None | Application-layer enforcement |
| **Row-level security** | Via role scoping | Via MV/Secure View + role | Via role (Snowflake) + app logic |
| **Result volume** | Unlimited | 10,000 rows/page (pagination req.) | Configurable in application |
| **Compute cost** | Per query (on-demand) | MV refresh (predictable) + per-query | MV refresh + compute pool (continuous) |
| **Deployment complexity** | Very low | None (serverless) | High. Requires image registry, compute pool, SPCS |
| **Consumer knowledge required** | ODBC/JDBC config | JWT auth, Snowflake SQL, pagination | Standard HTTP only |
| **Operational overhead** | Very low | Very low | Medium. Container lifecycle and image updates are needed |

### **Key Differentiators**

**Standardization gap:** JDBC/ODBC and the raw SQL API impose no constraints on queries — they act as transparent conduits to Snowflake. FastAPI on SPCS is the only method enforcing a contract at the API boundary: named endpoints with typed parameters, validated inputs, and structured responses. This matters when multiple teams share the API.

**Documentation gap:** The lack of a native Swagger UI for the SQL API is the main developer experience difference between Method 2 and Method 3. FastAPI auto-generates interactive documentation from type annotations; the SQL API requires consumers to read Snowflake's static protocol docs and inspect Materialized View DDL in Snowflake.

**Cost structure:** JDBC/ODBC and SQL API incur costs only when queries run. SPCS compute pools incur continuous costs while active, including idle periods. For low-traffic APIs, the `AUTO_SUSPEND_SECS` setting partially mitigates this, but a cold-start penalty applies when the pool resumes.

**Complementarity:** These methods are not mutually exclusive. A practical architecture layers them: Materialized Views as the data surface (shared across all methods), JDBC/ODBC as Power BI transport, and FastAPI on SPCS as the governed REST API for engineering consumers. The SQL API serves as a tactical bridge for ad-hoc scripting before full FastAPI deployment.

## **6. Security Considerations**

Security concerns apply to all three methods. These patterns hold regardless of the access method chosen.

### **Network Policies**

Restrict access by IP address as the first defence. Service accounts for `TEQPLAY_MART.GOLD` must be reachable only from known application subnets, not the open internet.

sqlwide760-- Restrict access by IP address
CREATE NETWORK POLICY api\_access\_policy
ALLOWED\_IP\_LIST = ('203.0.113.0/24', '198.51.100.0/24')
COMMENT = 'Allow access only from corporate network and cloud services';
ALTER USER svc\_api\_client SET NETWORK\_POLICY = api\_access\_policy;

### **Access Auditing**

Snowflake's `ACCOUNT_USAGE` views provide a complete audit trail of queries run by service accounts. The queries below show the access patterns of `svc_powerbi` and `svc_api_client`: who queried what, when, and the compute used.

sqlwide760-- Query history monitoring
SELECT
query\_id,
query\_text,
user\_name,
role\_name,
warehouse\_name,
execution\_time,
total\_elapsed\_time,
rows\_produced,
bytes\_scanned
FROM SNOWFLAKE.ACCOUNT\_USAGE.QUERY\_HISTORY
WHERE start\_time >= DATEADD(day, -7, CURRENT\_TIMESTAMP())
AND user\_name = 'svc\_api\_client'
ORDER BY start\_time DESC;
-- Access history
SELECT
query\_id,
user\_name,
direct\_objects\_accessed,
base\_objects\_accessed,
objects\_modified,
query\_start\_time
FROM SNOWFLAKE.ACCOUNT\_USAGE.ACCESS\_HISTORY
WHERE user\_name IN ('svc\_powerbi', 'svc\_api\_client')
AND query\_start\_time >= DATEADD(day, -1, CURRENT\_TIMESTAMP());

## **7. Strategic Recommendations**

### **Recommended Access Architecture**

The recommended architecture layers all three methods, each serving a distinct consumer category:

wide760Power BI (KPI dashboards)
└── ODBC (POWERBI\_READER role)
└── TEQPLAY\_MART.GOLD Materialized Views ← pre-computed aggregations
└── TEQPLAY\_MART.PUBLIC base tables
Internal scripts / one-off automation
└── SQL API (API\_SERVICE\_ROLE, JWT auth)
└── TEQPLAY\_MART.GOLD Materialized Views ← fast, scan-free reads
└── TEQPLAY\_MART.PUBLIC base tables
Backend services / multi-team consumers
└── FastAPI on SPCS (TEQPLAY\_MART.GOLD.kpi\_api\_svc)
└── TEQPLAY\_MART.GOLD Materialized Views ← governed, versioned endpoints
└── TEQPLAY\_MART.PUBLIC base tables (never exposed directly)

### **Decision Tree: SQL API vs. FastAPI on SPCS**

Use this decision tree when a new programmatic consumer requires access to `TEQPLAY_MART.GOLD`:

wide760Is the consumer an internal engineer familiar with Snowflake auth?
│
├─ YES ──► Is this a one-off script or ad-hoc query?
│ │
│ ├─ YES ──► Use SQL API + Materialized Views
│ │ (serverless, zero deployment, low friction)
│ │
│ └─ NO ───► Will other teams consume this in future?
│ │
│ ├─ YES ──► Use FastAPI on SPCS
│ └─ NO ───► Use SQL API + Materialized Views
│
└─ NO ───► Does the consumer expect a standard REST API?
│
└─ YES ──► Use FastAPI on SPCS
(Swagger UI, no Snowflake knowledge needed)

The defining question is not technical capability; both approaches return the same data. Instead, it concerns **who the consumer is and whether the API is a product**. The SQL API is a tool; FastAPI on SPCS is a service.

### **Per Use Case**

**Use Case 1: Power BI KPI Dashboards**

* Access via ODBC with `POWERBI_READER` role on `TEQPLAY_REPORT_WH`
* Point DirectQuery to Materialized Views in `TEQPLAY_MART.GOLD`, not raw tables
* Set `AUTO_SUSPEND = 60` and use a resource monitor to limit idle compute cost

**Use Case 2: Internal Scripting and Automation**

* Access via SQL API with `API_SERVICE_ROLE` and RSA key-pair / JWT authentication
* Target Materialized Views directly to avoid per-query aggregation overhead
* Implement a pagination loop for result sets over 10,000 rows

**Use Case 3: Governed REST API for Engineering Consumers**

* Deploy FastAPI on SPCS (`TEQPLAY_MART.GOLD.kpi_api_svc`)
* Expose typed, versioned endpoints backed by `TEQPLAY_MART.GOLD` Materialized Views
* Consumers use standard HTTP, no Snowflake knowledge or JWT handling needed

### **Cost Management**

Right-sizing `TEQPLAY_REPORT_WH` based on workload drives most costs. For Power BI DirectQuery, start with an X-Small warehouse and scale up only when concurrency limits performance.

sqlwide760-- Use multi-cluster for concurrent BI query workloads
CREATE WAREHOUSE TEQPLAY\_REPORT\_WH WITH
WAREHOUSE\_SIZE = 'SMALL'
MIN\_CLUSTER\_COUNT = 1
MAX\_CLUSTER\_COUNT = 3
SCALING\_POLICY = 'STANDARD'
AUTO\_SUSPEND = 60;

For the SPCS compute pool, `AUTO_SUSPEND_SECS` limits idle cost when the FastAPI service is idle:

sqlwide760ALTER COMPUTE POOL kpi\_api\_pool SET AUTO\_SUSPEND\_SECS = 300;

Snowflake result caching eliminates compute for repeated identical queries. It is on by default; disable per session only when freshness is required.

sqlwide760-- Disable result cache for a session requiring fresh data
ALTER SESSION SET USE\_CACHED\_RESULT = FALSE;

### **Observability**

Set up monitoring before deploying any method to production. The two views below show query performance by service account and warehouse credit usage.

sqlwide760CREATE VIEW TEQPLAY\_MART.GOLD.api\_query\_performance AS
SELECT
DATE\_TRUNC('hour', start\_time) AS query\_hour,
user\_name,
warehouse\_name,
COUNT(\*) AS query\_count,
AVG(total\_elapsed\_time) AS avg\_execution\_ms,
PERCENTILE\_CONT(0.95) WITHIN GROUP (ORDER BY total\_elapsed\_time) AS p95\_execution\_ms,
SUM(CASE WHEN error\_code IS NOT NULL THEN 1 ELSE 0 END) AS error\_count,
SUM(credits\_used\_cloud\_services) AS total\_credits
FROM SNOWFLAKE.ACCOUNT\_USAGE.QUERY\_HISTORY
WHERE start\_time >= DATEADD(day, -7, CURRENT\_TIMESTAMP())
AND user\_name LIKE 'svc\_%'
GROUP BY DATE\_TRUNC('hour', start\_time), user\_name, warehouse\_name;sqlwide760CREATE VIEW TEQPLAY\_MART.GOLD.warehouse\_costs AS
SELECT
DATE(start\_time) AS usage\_date,
warehouse\_name,
SUM(credits\_used) AS total\_credits,
SUM(credits\_used) \* 3.0 AS estimated\_cost\_usd -- adjust for actual pricing tier
FROM SNOWFLAKE.ACCOUNT\_USAGE.WAREHOUSE\_METERING\_HISTORY
WHERE start\_time >= DATEADD(month, -1, CURRENT\_TIMESTAMP())
GROUP BY DATE(start\_time), warehouse\_name
ORDER BY usage\_date DESC, total\_credits DESC;

## **8. References**

### **Snowflake Documentation**

* [Snowflake SQL API Overview](https://docs.snowflake.com/en/developer-guide/sql-api/index.html)
* [Key-Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/key-pair-auth)
* [Materialized Views](https://docs.snowflake.com/en/user-guide/views-materialized)
* [Secure Views](https://docs.snowflake.com/en/user-guide/views-secure)
* [Snowpark Container Services (SPCS) Overview](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview)
* [SPCS Service Specification Reference](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/specification-reference)
* [SPCS OAuth Token Injection](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/additional-considerations-services-jobs)
* [Network Policies](https://docs.snowflake.com/en/user-guide/network-policies)
* [ACCOUNT\_USAGE — QUERY\_HISTORY](https://docs.snowflake.com/en/sql-reference/account-usage/query_history)
* [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors)

### **FastAPI Documentation**

* [FastAPI — Getting Started](https://fastapi.tiangolo.com/)
* [FastAPI — Automatic Swagger UI](https://fastapi.tiangolo.com/features/#automatic-docs)
* [Snowpark Python API](https://docs.snowflake.com/en/developer-guide/snowpark/python/index)