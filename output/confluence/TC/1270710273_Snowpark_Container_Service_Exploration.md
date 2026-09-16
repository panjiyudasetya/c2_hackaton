---
id: confluence:1270710273
source: confluence
type: page
space: TC
title: Snowpark Container Service Exploration
author: Panji Y. Wiwaha
date: '2026-07-15'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1270710273
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1270710273
---
# Snowpark Container Service Exploration

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1270710273  

## Content

# **Snowpipe Streaming Application Deployment on SPCS**

## **What is SPCS, and Why Are We Using It?**

**Snowpark Container Services (SPCS)** lets you run your Docker containers directly inside your Snowflake account. You don't need a separate cloud account, Kubernetes cluster, or VM fleet. Build your container image as usual, push it to a Snowflake-hosted registry, and Snowflake runs it on managed compute.

Think of it as "*bring your own app, Snowflake brings the infrastructure.*"

### **Why use SPCS instead of hosting the app elsewhere (e.g., AWS ECS, a VM, your laptop)?**

* **One platform, one bill.** Compute, storage, and now general-purpose application hosting all live under your Snowflake account. No separate cloud subscription just to run a small consumer service.
* **Data stays close to Snowflake.** The app runs on infrastructure that sits next to your Snowflake data, so writes into Snowflake (like our Snowpipe Streaming inserts) have low latency and don't have to cross the public internet.
* **Snowflake handles the undifferentiated heavy lifting.** Compute pools, scaling, restarts, networking, and secrets management are all built in, you don't need to stand up your own container orchestration.
* **Governance for free.** Access to secrets, roles, and data is controlled with the same RBAC model you already use for the rest of Snowflake.

### **Why is SPCS a good fit specifically for our use case?**

Our `snowpipe-amqp-consumer` app is a **long-running background service**: it sits there permanently, listens to a RabbitMQ queue, and streams every message it receives into Snowflake via the Snowpipe Streaming SDK. It never finishes, and it doesn't respond to a schedule. It just runs forever.

SPCS is well-suited to exactly this shape of workload:

* It supports **long-running containers**, not just short batch jobs. The service runs until you stop it.
* It has a **restart policy** (`ALWAYS`), so if the container crashes (e.g., a network blip to RabbitMQ), Snowflake restarts it automatically.
* Because it **doesn't need to serve incoming web traffic**, we don't need to configure an `endpoints` block or expose a public URL. This app only pushes data outward, keeping setup simple.
* The compute pool can be small and fixed (1 node), since a queue consumer doesn't need to scale like a web service.

In short, SPCS provides a simple, low-maintenance home for an always-on data-ingestion worker without requiring a separate container platform.

### **The Deployment Pipeline, at a Glance**

SPCS Deployment Pipeline

Read it top to bottom: our code is built into a Docker image on GitHub, the image is pushed to Snowflake's built-in registry, SPCS runs that image as a service, and inside the container our Java consumer reads from RabbitMQ and streams rows into the `RAW.EVENTS` table using the Snowpipe Streaming SDK.

The rest of this guide walks through deploying `snowpipe-amqp-consumer` into SPCS step by step, using Snowsight.

## **Prerequisites**

Before you start, make sure you have:

* A Snowflake account with SPCS enabled (requires the **Business Critical** or **Enterprise** edition; and paid account)
* Docker is installed on your local machine
* Access to the `snowsql` CLI or a Snowsight worksheet
* Your Snowflake private key, base64-encoded (for key-pair authentication; ask your Snowflake admin if you don't have one)

## **Step 1. Image Registry (**`01-image-registry.sql`**)**

Create a Docker image repository inside Snowflake to host the consumer container image. After creation, copy the `repository_url` from SHOW IMAGE REPOSITORIES output — you'll need it to tag and push your Docker image.

The registry URL uses the org-account regionless format:

> *pmowbhd-sk17095.registry.snowflakecomputing.com/streaming\_db\_\_proto/raw/spcs\_repo/...*

### **Create Docker Image repository in Snowflake**

sqlwide760USE ROLE SYSADMIN;
USE WAREHOUSE TEQPLAY\_WH;
USE DATABASE STREAMING\_DB\_\_PROTO;
USE SCHEMA RAW;
CREATE IMAGE REPOSITORY IF NOT EXISTS STREAMING\_DB\_\_PROTO.RAW.SPCS\_REPO;
SHOW IMAGE REPOSITORIES IN SCHEMA STREAMING\_DB\_\_PROTO.RAW;

### **Build and push Docker Image**

powershellwide760docker tag snowpipe-amqp-consumer:latest \
pmowbhd-sk17095.registry.snowflakecomputing.com/streaming\_db\_\_proto/raw/spcs\_repo/snowpipe-amqp-consumer:latest
docker push \
pmowbhd-sk17095.registry.snowflakecomputing.com/streaming\_db\_\_proto/raw/spcs\_repo/snowpipe-amqp-consumer:latest

## **Step 2. Secrets (**`02-secrets.sql`**)**

Store sensitive credentials as Snowflake secrets for secure injection into the container at runtime. The SPCS platform mounts secrets as environment variables inside the container.

**Security note:** Never commit actual secret values to source control. Use `ALTER SECRET ... SET SECRET_STRING` for rotation.

powershellwide760CREATE OR REPLACE SECRET STREAMING\_DB\_\_PROTO.RAW.RABBITMQ\_PASSWORD
TYPE = GENERIC\_STRING
SECRET\_STRING = '<your-rabbitmq-password>';
SHOW SECRETS;

## **Step 3. External Access Integration (**`03-eai-setup.sql`**)**

Configure network egress rules so the container can reach external services (RabbitMQ).

sqlwide760USE ROLE ACCOUNTADMIN;
CREATE OR REPLACE NETWORK RULE cloudamqp\_egress\_rule
MODE = EGRESS
TYPE = HOST\_PORT
VALUE\_LIST = (
'stingray.rmq.cloudamqp.com:5672'
);
CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION cloudamqp\_access\_integration
ALLOWED\_NETWORK\_RULES = (cloudamqp\_egress\_rule)
ENABLED = TRUE;
DESC EXTERNAL ACCESS INTEGRATION cloudamqp\_access\_integration;

### **IMPORTANT: Don't include Snowflake URLs in the EAI**

When the SPCS service uses SPCS OAuth authentication (`SNOWFLAKE_AUTH_MODE: SPCS`) with the Snowpipe Streaming SDK, traffic to Snowflake APIs is routed internally by the SPCS platform.

Adding Snowflake hostnames (e.g., `pmowbhd-sk17095.snowflakecomputing.com`) to the EAI network rule forces the SDK's traffic through the **external** network path, where SPCS workload-identity tokens are **rejected** with HTTP 401.

| **Destination** | **EAI Required?** | **Reason** |
| --- | --- | --- |
| RabbitMQ (stingray.rmq.cloudamqp.com) | Yes | External third-party service |
| Snowflake streaming API | NO | Routed internally by SPCS platform |

Symptom if misconfigured:

bashwide760 "SpcsTokenManager: received a kick to refresh token ... from get\_subdomain\_name
with reason 401 error with client request"

## **Step 4. Security & Object Configuration (**`04-security-and-object-config.sql`**)**

Provision roles, grants, and infrastructure permissions. This step uses `ACCOUNTADMIN` because it involves account-level grants and role creation.

### **Required Privileges for Snowpipe Streaming (high-performance SDK)**

| **Object** | **Privilege** | **Purpose** |
| --- | --- | --- |
| Table (`EVENTS`) | `INSERT` | Write ingested rows |
| Table (`EVENTS`) | `SELECT` | Channel offset management |
| Pipe (`STREAMING`) | `OPERATE` | Open/manage channels |
| Pipe (`STREAMING`) | `MONITOR` | Health checks |
| Database | `USAGE` | Path resolution |
| Schema | `USAGE` | Path resolution |
| Warehouse | `USAGE` | Metadata operations |

### **Pipe Ownership Requirement**

The `STREAMING` pipe must be owned by the **SAME** role that owns the SPCS service (`SYSADMIN`). If the pipe was created under a different role (e.g., `ACCOUNTADMIN`), transfer ownership:

sqlwide760 GRANT OWNERSHIP ON PIPE STREAMING\_DB\_\_PROTO.RAW.EVENTS
TO ROLE SYSADMIN COPY CURRENT GRANTS;
SELECT SYSTEM$PIPE\_FORCE\_RESUME('STREAMING\_DB\_\_PROTO.RAW.EVENTS');

Next, run this SQL to set up roles, grants, and infrastructure permissions:

sqlwide760USE ROLE ACCOUNTADMIN;
USE WAREHOUSE TEQPLAY\_WH;
USE DATABASE STREAMING\_DB\_\_PROTO;
USE SCHEMA RAW;
-- Allow SYSADMIN to manage SPCS infrastructure
GRANT CREATE COMPUTE POOL ON ACCOUNT TO ROLE SYSADMIN;
GRANT BIND SERVICE ENDPOINT ON ACCOUNT TO ROLE SYSADMIN;
GRANT READ ON IMAGE REPOSITORY STREAMING\_DB\_\_PROTO.RAW.SPCS\_REPO TO ROLE SYSADMIN;
GRANT USAGE ON SECRET STREAMING\_DB\_\_PROTO.RAW.RABBITMQ\_PASSWORD TO ROLE SYSADMIN;
GRANT READ ON SECRET STREAMING\_DB\_\_PROTO.RAW.RABBITMQ\_PASSWORD TO ROLE SYSADMIN;
-- Create the low-privilege runtime role for ingestion
CREATE ROLE IF NOT EXISTS AMQP\_STREAMING\_ROLE;
GRANT ROLE AMQP\_STREAMING\_ROLE TO ROLE SYSADMIN;
-- Grant Snowpipe Streaming privileges to the ingestion role
GRANT USAGE ON WAREHOUSE TEQPLAY\_WH TO ROLE AMQP\_STREAMING\_ROLE;
GRANT USAGE ON DATABASE STREAMING\_DB\_\_PROTO TO ROLE AMQP\_STREAMING\_ROLE;
GRANT USAGE ON SCHEMA STREAMING\_DB\_\_PROTO.RAW TO ROLE AMQP\_STREAMING\_ROLE;
GRANT INSERT ON TABLE STREAMING\_DB\_\_PROTO.RAW.EVENTS TO ROLE AMQP\_STREAMING\_ROLE;
GRANT SELECT ON TABLE STREAMING\_DB\_\_PROTO.RAW.EVENTS TO ROLE AMQP\_STREAMING\_ROLE;
GRANT OPERATE ON PIPE STREAMING\_DB\_\_PROTO.RAW.EVENTS TO ROLE AMQP\_STREAMING\_ROLE;
GRANT MONITOR ON PIPE STREAMING\_DB\_\_PROTO.RAW.EVENTS TO ROLE AMQP\_STREAMING\_ROLE;
-- Allow EAI usage by the service owner
GRANT USAGE ON INTEGRATION cloudamqp\_access\_integration TO ROLE SYSADMIN;
-- Grant the role to a specific user for manual operations
GRANT ROLE AMQP\_STREAMING\_ROLE TO USER "<your-snowlake-username>";

## **Step 5. Deploy the Service (**`05-deploy.sql`**)**

Create the compute pool and launch the streaming service. The service is owned by SYSADMIN, which is the role that also owns the pipe and table.

### **Key Configuration Notes**

| **Parameter** | **Value** | **Explanation** |
| --- | --- | --- |
| `SNOWFLAKE_ACCOUNT` | zt51160 | Account locator only (not org-account format) |
| `SNOWFLAKE_AUTH_MODE` | SPCS | Uses platform workload-identity token |
| `enableCustomCredentials` | true | Exposes `/snowflake/session/token` in container |
| `INSTANCE_FAMILY` | `CPU_X64_XS` | Smallest instance, sufficient for consumption |
| `EXTERNAL_ACCESS_INTEGRATIONS` | `cloudamqp_access_integration` | Only for RabbitMQ egress |

The service uses SPCS OAuth: the platform provides a workload-identity token at `/snowflake/session/token`, which the Snowpipe Streaming SDK uses to authenticate without any stored credentials or key pairs.

sqlwide760USE ROLE SYSADMIN;
-- Create compute pool
DROP COMPUTE POOL IF EXISTS AMQP\_CONSUMER\_POOL;
CREATE COMPUTE POOL AMQP\_CONSUMER\_POOL
MIN\_NODES = 1
MAX\_NODES = 1
INSTANCE\_FAMILY = CPU\_X64\_XS
AUTO\_RESUME = TRUE;
-- Deploy the service
DROP SERVICE IF EXISTS STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC;
CREATE SERVICE STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC
IN COMPUTE POOL AMQP\_CONSUMER\_POOL
FROM SPECIFICATION
$$
spec:
containers:
- name: amqp-consumer
image: pmowbhd-sk17095.registry.snowflakecomputing.com/streaming\_db\_\_proto/raw/spcs\_repo/snowpipe-amqp-consumer:latest
env:
RABBITMQ\_HOST: "stingray.rmq.cloudamqp.com"
RABBITMQ\_PORT: "5672"
RABBITMQ\_TLS: "false"
RABBITMQ\_QUEUES: "jgitpltg:VesselVoyage-PTO-pocca"
RABBITMQ\_USER: "jgitpltg"
SNOWFLAKE\_ACCOUNT: "zt51160"
SNOWFLAKE\_ROLE: "AMQP\_STREAMING\_ROLE"
SNOWFLAKE\_AUTH\_MODE: SPCS
SNOWFLAKE\_WAREHOUSE: "TEQPLAY\_WH"
SNOWFLAKE\_DATABASE: "STREAMING\_DB\_\_PROTO"
SNOWFLAKE\_DATABASE\_SCHEMA: "RAW"
SNOWFLAKE\_STREAMING\_TABLE\_NAME: "EVENTS"
BATCH\_SIZE: "500"
FLUSH\_INTERVAL\_MS: "5000"
secrets:
- snowflakeSecret: STREAMING\_DB\_\_PROTO.RAW.rabbitmq\_password
envVarName: RABBITMQ\_PASSWORD
capabilities:
securityContext:
enableCustomCredentials: true
serviceRoles:
- name: consumer\_svc\_role
$$
EXTERNAL\_ACCESS\_INTEGRATIONS = (cloudamqp\_access\_integration);
-- Grant service role for endpoint access
USE ROLE ACCOUNTADMIN;
GRANT SERVICE ROLE STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC!consumer\_svc\_role
TO ROLE AMQP\_STREAMING\_ROLE;

## **Step 6. Verify (**`06-verify.sql`**)**

Confirm the service is running and data is flowing into the EVENTS table.

sqlwide760USE ROLE SYSADMIN;
Check service status
SELECT SYSTEM$GET\_SERVICE\_STATUS('STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC');
-- Tail container logs
CALL SYSTEM$GET\_SERVICE\_LOGS('STREAMING\_DB\_\_PROTO.RAW.amqp\_consumer\_svc', '0', 'amqp-consumer', 50);
-- Verify rows are flowing
SELECT COUNT(\*), MAX(ingest\_ts) FROM STREAMING\_DB\_\_PROTO.RAW.EVENTS;
-- Check stream has data for downstream processing
SELECT SYSTEM$STREAM\_HAS\_DATA('RAW.SOF\_STREAM');

### **Healthy Log Output**

When everything is working, you should see:

powershellwide760 "SpcsTokenManager: token refreshed. Expires in 600s for STREAMING\_DB\_\_PROTO.RAW.EVENTS..."
"BrokerConnector: Opened connection to stingray.rmq.cloudamqp.com/jgitpltg (1 queue(s))"

And NO `"401 error with client request"` messages.

## **Operational Commands**

sqlwide760-- Suspend (stop consuming, stop billing)
ALTER SERVICE STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC SUSPEND;
ALTER COMPUTE POOL AMQP\_CONSUMER\_POOL SUSPEND;
-- Resume
ALTER COMPUTE POOL AMQP\_CONSUMER\_POOL RESUME;
ALTER SERVICE STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC RESUME;
-- Force restart (picks up fresh tokens)
ALTER SERVICE STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC SUSPEND;
-- (wait ~10 seconds)
ALTER SERVICE STREAMING\_DB\_\_PROTO.RAW.AMQP\_CONSUMER\_SVC RESUME;

## **Lessons Learned & Pitfalls**

### **1. EAI Must NOT Include Snowflake Endpoints**

The SPCS platform provides an internal path for services to reach Snowflake APIs. Adding Snowflake URLs to the EAI routes streaming SDK traffic through the external network, causing persistent HTTP 401 on the `/v2/streaming/hostname` endpoint.

**Symptom**: Token refresh succeeds, but `get_subdomain_name` returns 401 in a loop.  
**Fix**: Only include truly external hosts (RabbitMQ, third-party APIs) in EAI rules.

### **2. Account Identifier Format**

For SPCS OAuth with the Snowpipe Streaming SDK, use the **account locator** (`zt51160`), not the org-account format (`PMOWBHD-SK17095`). The SDK constructs the Snowflake URL internally via the SPCS platform routing.

### **3. Pipe Ownership Must Align with Service Owner**

The `STREAMING` pipe should be owned by the same role that owns the SPCS service (SYSADMIN). If created under `ACCOUNTADMIN`, transfer ownership and force-resume:

sqlwide760 GRANT OWNERSHIP ON PIPE ... TO ROLE SYSADMIN COPY CURRENT GRANTS;
SELECT SYSTEM$PIPE\_FORCE\_RESUME('...');

### **4. Minimum Grants for Snowpipe Streaming**

Beyond `INSERT` on the table, the streaming SDK also requires:

* `SELECT` on the table (offset tracking)
* `OPERATE` and `MONITOR` on the pipe
* `USAGE` on warehouse, database, and schema

## **SPCS AMQP Consumer Prototyping Architecture**

## **Execution Order**

| **#** | **File** | **Role Required** | **Purpose** |
| --- | --- | --- | --- |
| 1 | `01-image-registry.sql` | `SYSADMIN` | Create image repo |
| 2 | `02-secrets.sql` | `SYSADMIN` | Store credentials |
| 3 | `03-eai-setup.sql` | `ACCOUNTADMIN` | Network egress (RabbitMQ) |
| 4 | `04-security-and-object-config.sql` | `ACCOUNTADMIN` | Roles, grants, stage |
| 5 | `05-deploy.sql` | `SYSADMIN` | Compute pool + service |
| 6 | `06-verify.sql` | `SYSADMIN` | Health check |

## **References**

### **Snowpark Container Services**

* [Snowpark Container Services overview](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview)
* [Working with services](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/working-with-services)
* [Working with compute pools](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/working-with-compute-pool)
* [Working with an image registry and repository](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/working-with-registry-repository)
* [Service specification reference](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/specification-reference)
* [Tutorials overview](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview-tutorials)

### **SQL command reference**

* [CREATE COMPUTE POOL](https://docs.snowflake.com/en/sql-reference/sql/create-compute-pool)
* [CREATE SERVICE](https://docs.snowflake.com/en/sql-reference/sql/create-service)
* [CREATE SECRET](https://docs.snowflake.com/en/sql-reference/sql/create-secret)
* [CREATE PIPE](https://docs.snowflake.com/en/sql-reference/sql/create-pipe)
* [DESCRIBE SERVICE](https://docs.snowflake.com/en/sql-reference/sql/desc-service)
* [SYSTEM$GET\_SERVICE\_LOGS](https://docs.snowflake.com/en/sql-reference/functions/system_get_service_logs)

### **Snowpipe Streaming**

* [Snowpipe Streaming overview](https://docs.snowflake.com/en/user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview)
* [Snowpipe Streaming: high-performance architecture](https://docs.snowflake.com/en/user-guide/snowpipe-streaming-high-performance-overview)
* [Tutorial: Get started with Snowpipe Streaming high-performance architecture SDK](https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-getting-started)
* [Best practices for Snowpipe Streaming with high-performance architecture](https://docs.snowflake.com/en/user-guide/snowpipe-streaming/snowpipe-streaming-high-performance-best-practices)