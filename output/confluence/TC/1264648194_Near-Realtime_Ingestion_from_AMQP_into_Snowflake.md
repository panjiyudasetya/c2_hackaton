---
id: confluence:1264648194
source: confluence
type: page
space: TC
title: Near-Realtime Ingestion from AMQP into Snowflake
author: Panji Y. Wiwaha
date: '2026-07-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1264648194
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1264648194
---
# Near-Realtime Ingestion from AMQP into Snowflake

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1264648194  

## Content

# **Exploration Report: Near-Realtime Ingestion from AMQP into Snowflake**

## **1. Background & Objective**

The goal of this exploration is to answer a single question:

> ***Can we build a real-time streaming data pipeline from an AMQP message broker (RabbitMQ) directly into Snowflake, without any intermediate storage layer like S3 or Kafka?***

Two approaches were considered:

| **Approach** | **Description** | **Status** |
| --- | --- | --- |
| **Snowpipe Streaming** | Custom Java consumer using Snowflake Ingest SDK | Implemented & explored |
| **Snowflake OpenFlow** | Managed native Snowflake connector | Unexplored; Not available on a free-tier account |

This report covers the implemented approach end-to-end: from the Java consumer that reads from RabbitMQ, to the Snowflake pipeline that processes and reconciles the data.

## **2. Architecture Overview**

The pipeline has two distinct parts:

1. `snowpipe-amqp-consumer`, the Java application that bridges RabbitMQ to Snowflake
2. `01-amqp-streaming-pipeline`, the Snowflake workspace in Snowsight for setting up warehouse, schemas, DDL, tasks

## **3. Part 1:** `snowpipe-amqp-consumer`

### **3.1 Why Is This Consumer Needed?**

Snowflake does not have a native AMQP connector (outside of OpenFlow, which requires an enterprise account). To stream data from RabbitMQ into Snowflake, a custom bridge application is required.

The consumer is a small backend service that does not perform heavy transformation. Its responsibilities are:

* Subscribe to one or more RabbitMQ queues
* Parse each raw JSON message into a structured row
* Buffer rows and flush them to Snowflake via the **Snowpipe Streaming API**

This design keeps the consumer stateless and easy to reason about. All business logic lives downstream in SQL.

### **3.2 How It Works Internally**

Each message goes through a defined chain:

AMQP Messages Flow

The produced row schema per message:

| **Column** | **Source** |
| --- | --- |
| `id` | Random UUID generated at ingest time |
| `payload` | Full raw JSON object (stored as VARIANT) |
| `queue_name` | Source RabbitMQ queue name |
| `ingest_ts` | UTC timestamp when the consumer processed the message |
| `channel_id` | Injected by `SnowpipeClient`, used to identify the Snowpipe channel |

> *Event time is **not** extracted at the consumer level. It should be derived from* `payload` *in SQL (e.g.* `payload:timestamp::TIMESTAMP`*) per event type.*

### **3.3 Prerequisites**

| **Requirement** | **Details** |
| --- | --- |
| **JDK** | 17–21 to run Gradle; Java 11 toolchain is auto-provisioned for the build |
| **Docker** | Required for containerised runs (recommended) |
| **RabbitMQ** | A running broker with at least one accessible queue |
| **Snowflake account** | With Snowpipe Streaming enabled and key-pair authentication configured |
| **RSA key pair** | Generated locally; public key registered on the Snowflake user |

### **3.4 Generating the RSA Key Pair**

Snowpipe Streaming uses **key-pair authentication** since it does not support password authentication. Therefore, we need to generate an RSA key pair and register the public key with the Snowflake user.

**Step 1 — Generate the private and public keys:**

bashwide760openssl rsa -in snowflake\_key.pem -pubout -out snowflake\_key.pub

**Step 2 — Get the public key:**

bashwide760cat snowflake\_key.pub | tr -d '\n'

Copy and paste it into the next step, removing this header and footer:

* `-----BEGIN PUBLIC KEY-----` (header)
* `-----END PUBLIC KEY-----` (footer)

**Step 3 — Register the public key on the Snowflake user:**

sqlwide760ALTER USER <your\_snowflake\_user>
SET RSA\_PUBLIC\_KEY='<paste content of snowflake\_key.pub, header/footer stripped>';

**Step 4 — Encode the private key for the environment variable:**

The consumer accepts the private key as a Base64 string (PEM headers and whitespace are stripped automatically):

bashwide760# macOS
cat snowflake\_key.pem | tr -d '\n'

Copy the output into `SNOWFLAKE_PRIVATE_KEY` in your `.env` file, removing the header and footer.

### **3.5 Configuration**

Copy `.env.example` to `.env` and fill in all required values:

bashwide760# RabbitMQ
RABBITMQ\_HOST=your-broker-host
RABBITMQ\_QUEUES=vhost:queue-name # or comma-separated: vhost1:queue1,vhost2:queue2
RABBITMQ\_USER=guest
RABBITMQ\_PASSWORD=guest
# Snowflake
SNOWFLAKE\_ACCOUNT=your-account-identifier
SNOWFLAKE\_USER=your-snowflake-user
SNOWFLAKE\_PRIVATE\_KEY=<base64-encoded-private-key>
SNOWFLAKE\_ROLE=SYSADMIN
SNOWFLAKE\_WAREHOUSE=TEQPLAY\_WH
SNOWFLAKE\_DATABASE=STREAMING\_DB\_\_PROTO
SNOWFLAKE\_DATABASE\_SCHEMA=RAW
SNOWFLAKE\_STREAMING\_TABLE\_NAME=EVENTS
# Optional tuning (defaults shown)
BATCH\_SIZE=500
FLUSH\_INTERVAL\_MS=5000
RABBITMQ\_TLS=false

### **3.6 Running on Docker**

The project includes a multi-stage `Dockerfile` and a `docker-compose.yml`.

**Build and run with Docker Compose (recommended):**

wide760docker compose build --no-cache app && docker compose up

Stop the container with `Ctrl+C`. The consumer will **flush any buffered rows to Snowflake before exiting** (graceful shutdown via `SIGTERM`).

### **3.7 How the Consumer Connects to Snowflake**

This is the key bridge between the two parts of the pipeline.

When the consumer starts, `SnowpipeClient` uses the Snowflake Ingest SDK to:

1. Authenticate to Snowflake using the RSA private key
2. Open a **named streaming channel** (`rmq-<queue>-<hostname>`) against the target table
3. Stream row batches directly into `RAW.EVENTS` via that channel

The channel name is stored in the `channel_id` column for every inserted row, providing full traceability of which consumer instance produced each record.

On the Snowflake side, channels write directly to the **target table** (`RAW.EVENTS`). The PIPE object defined during the SQL setup (Part 2) specifies the `COPY INTO` configuration that governs how incoming data is processed before being written to the table, including options such as `MATCH_BY_COLUMN_NAME`.

In short: **the consumer writes → the PIPE governs how → the table stores → the STREAM detects → the TASK processes**.

## **4. Part 2: Snowflake SQL Setup on Snowsight**

All SQL is organised under `sql/` in three sequential folders: `01-setup`, `02-ddl`, and `03-tasks`. They must be executed in order.

### **4.1 Step 1 — Warehouse & Database (**`01-setup/`**)**

`01-database.sql`

sqlwide760-- Create and activate compute warehouse
CREATE WAREHOUSE TEQPLAY\_WH WITH WAREHOUSE\_SIZE = XSMALL;
USE WAREHOUSE TEQPLAY\_WH;
-- Create the prototype database
CREATE DATABASE STREAMING\_DB\_\_PROTO WITH
COMMENT = 'Teqplay''s prototype database for streaming pipeline';

`02-schema.sql`

sqlwide760USE DATABASE STREAMING\_DB\_\_PROTO;
-- RAW: landing zone for all incoming events (append-only, no transformation)
CREATE SCHEMA IF NOT EXISTS RAW;
-- BRONZE: reconciled, deduplicated staging tables
CREATE SCHEMA IF NOT EXISTS BRONZE;

The two-schema design enforces a clear separation of concerns:

* **RAW** is an immutable landing zone where data arrives exactly as the consumer sends it
* **BRONZE** is where business logic is applied (deduplication, conflict resolution)

### **4.2 Step 2 — DDL: RAW Layer (**`02-ddl/01-raw/01-events.sql`)

#### **4.2.1 The EVENTS Table**

sqlwide760CREATE TABLE STREAMING\_DB\_\_PROTO.RAW.EVENTS (
id STRING COMMENT 'Unique identifier of the event.',
payload VARIANT COMMENT 'Full raw message payload as JSON (VARIANT).',
queue\_name STRING COMMENT 'Source RabbitMQ queue name.',
channel\_id STRING COMMENT 'Snowpipe Streaming channel identifier.',
ingest\_date DATE COMMENT 'Ingestion date set by the consumer.',
ingest\_ts TIMESTAMP COMMENT 'UTC ingestion timestamp set by the consumer.'
)
CLUSTER BY (ingest\_date, payload:\_type::VARCHAR);

**Why** `CLUSTER BY (ingest_date, payload:_type)`**?**

Snowflake physically groups data into micro-partitions based on these two columns. Since most analytical queries filter by date range and event type (e.g., *"show me all SOF events from last week"*), Snowflake skips partitions that don't match. This reduces the data scanned and lowers the compute costs.

#### **4.2.2 The PIPE Object**

sqlwide760CREATE OR REPLACE PIPE STREAMING\_DB\_\_PROTO.RAW.EVENTS
AS COPY INTO EVENTS
FROM TABLE(DATA\_SOURCE(TYPE => 'STREAMING'))
MATCH\_BY\_COLUMN\_NAME = CASE\_INSENSITIVE;

**What does** `FROM TABLE(DATA_SOURCE(TYPE => 'STREAMING'))` **mean?**

`'STREAMING'` is a reserved value, but it belongs to a different category than `'CSV'` or `'JSON'`. Here is how they differ:

| Context | Syntax | What `TYPE` means |
| --- | --- | --- |
| Classic Snowpipe (file-based) | `COPY INTO t FROM @stage FILE_FORMAT = (TYPE = 'CSV')` | **File format type** It tells Snowflake how to parse a staged file |
| Snowpipe Streaming | `COPY INTO t FROM TABLE(DATA_SOURCE(TYPE => 'STREAMING'))` | **Data source type** It tells Snowflake where the data *comes from* |

`DATA_SOURCE` is a Snowflake **table function** used in the `FROM` clause of the `COPY INTO` statement. `TYPE => 'STREAMING'` is a named argument to that function, and `'STREAMING'` is the only valid value in this context. It tells Snowflake:

> *"This PIPE will not read from a file stage (e.g. S3, internal stage). Instead, data will be pushed directly by the Snowpipe Streaming SDK via its named channels."*

Because no file is involved, there is no file format (`CSV`, `JSON`, etc.). The data arrives as pre-parsed rows from the SDK. `'CSV'` and `'JSON'` are not equivalent alternatives to `'STREAMING'`; they operate at different levels of the ingestion pipeline.

**Why a custom PIPE?**

Snowpipe Streaming automatically creates a **default pipe** for each table on demand. This allows the SDK to write to a table without an explicit `CREATE PIPE` statement. Create a custom PIPE only when you need specific COPY options or in-flight transformations. Here, the PIPE is created explicitly to apply `MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE`, which instructs Snowflake to match column names from the SDK row map to the table's columns case-insensitively. Without this, case mismatches between the consumer's row map and the DDL could cause data to land in the wrong columns or be rejected.

#### **4.2.3 The STREAM (CDC)**

sqlwide760CREATE OR REPLACE STREAM STREAMING\_DB\_\_PROTO.RAW.SOF\_STREAM
ON TABLE STREAMING\_DB\_\_PROTO.RAW.EVENTS
APPEND\_ONLY = TRUE;

**Why a STREAM?**

A `STREAM` is a *Change Data Capture* (CDC) object that tracks which rows in `RAW.EVENTS` downstream tasks have consumed using an internal offset (high-water mark). When queried, it returns **only new rows** since the last consumption, so tasks never scan the entire RAW table.

`APPEND_ONLY = TRUE` applies because `RAW.EVENTS` is insert-only by design, avoiding UPDATE/DELETE metadata tracking and reducing stream overhead.

### **4.3 Step 3 — DDL: BRONZE Layer (**`02-ddl/02-bronze/01-stg-sof.sql`**)**

sqlwide760CREATE TABLE IF NOT EXISTS STREAMING\_DB\_\_PROTO.BRONZE.STG\_SOF (
entry\_id VARCHAR NOT NULL,
action VARCHAR NOT NULL,
payload\_hash VARCHAR NOT NULL, -- MD5 of full payload; dedup fingerprint
raw\_payload VARIANT NOT NULL,
last\_seen\_ts TIMESTAMP\_NTZ NOT NULL, -- ingest\_ts of the winning row
is\_deleted BOOLEAN NOT NULL DEFAULT FALSE,
CONSTRAINT pk\_sof PRIMARY KEY (entry\_id)
);

`STG_SOF` holds the **current state** of each entity identified by `entry_id`. It is the reconciliation task's output, ensuring one row per entity records the latest state.

`payload_hash` (MD5 of the full payload) serves as a deduplication fingerprint: if the same payload arrives again, the row remains unchanged.

### **4.4 Step 4 — Task: SOF Reconciliation (**`03-tasks/01-sof-reconcile-task.sql`**)**

sqlwide760-- Grant EXECUTE TASK privilege (requires ACCOUNTADMIN once)
USE ROLE ACCOUNTADMIN;
GRANT EXECUTE TASK ON ACCOUNT TO ROLE SYSADMIN;
USE ROLE SYSADMIN;
CREATE OR REPLACE TASK BRONZE.sof\_reconcile\_task
WAREHOUSE = TEQPLAY\_WH
SCHEDULE = '3 MINUTE'
WHEN SYSTEM$STREAM\_HAS\_DATA('RAW.SOF\_STREAM')
AS
MERGE INTO BRONZE.STG\_SOF AS target
USING (
SELECT
payload:value:entryId::VARCHAR AS entry\_id,
payload:action::VARCHAR AS action,
MD5(payload::VARCHAR) AS payload\_hash,
ingest\_ts,
payload AS raw\_payload
FROM RAW.SOF\_STREAM
WHERE payload:\_type::VARCHAR = 'SOF'
) AS source
ON target.entry\_id = source.entry\_id
-- Update: same entity, different content, newer arrival
WHEN MATCHED
AND source.action != 'DELETE'
AND source.payload\_hash != target.payload\_hash
AND source.ingest\_ts > target.last\_seen\_ts
THEN UPDATE SET
target.action = source.action,
target.payload\_hash = source.payload\_hash,
target.raw\_payload = source.raw\_payload,
target.last\_seen\_ts = source.ingest\_ts,
target.is\_deleted = FALSE
-- Soft delete: mark the record as deleted without removing it
WHEN MATCHED AND source.action = 'DELETE'
THEN UPDATE SET
target.is\_deleted = TRUE,
target.last\_seen\_ts = source.ingest\_ts
-- Insert: entity never seen before
WHEN NOT MATCHED THEN
INSERT (entry\_id, action, payload\_hash, raw\_payload, last\_seen\_ts, is\_deleted)
VALUES (source.entry\_id, source.action, source.payload\_hash,
source.raw\_payload, source.ingest\_ts, source.action = 'DELETE');
-- Tasks are created suspended; explicitly resume
ALTER TASK BRONZE.sof\_reconcile\_task RESUME;

**Why a TASK?**

Snowflake Tasks are the built-in scheduler, so no external orchestration tool (Airflow, cron) is needed. The critical line is the `WHEN` condition: `SYSTEM$STREAM_HAS_DATA('RAW.SOF_STREAM')` skips execution when the stream has no new data. This means **compute is consumed only when data needs processing**.

**Why MERGE instead of INSERT?**

Raw event streams are noisy. The same `entryId` may arrive multiple times from retries, duplicate publishing, or system replays. A naive `INSERT` creates one row per message, inflating the table with duplicates. `MERGE` solves this by treating `entry_id` as the unique key and applying three cases:

| Case | Condition | Action |
| --- | --- | --- |
| **Update** | Same entity, different payload, newer timestamp | Update to the latest state |
| **Soft delete** | `action = 'DELETE'` | Set `is_deleted = TRUE` |
| **Insert** | Entity not yet seen | Insert a new row |

The result is exactly **one row per entity** in `BRONZE.STG_SOF`, always holding the latest known state.

## **5. Prototype Results & Findings**

### **Goal Achievement**

The prototype successfully demonstrates a working end-to-end streaming pipeline from RabbitMQ (AMQP) to Snowflake using the Snowpipe Streaming architecture. No intermediate storage (S3, Kafka, etc.) is required.

### **Why This Pipeline Is Efficient**

| **Component** | **Efficiency Gain** | **Mechanism** |
| --- | --- | --- |
| **CLUSTER BY** | Query cost reduction | Partition pruning scans only matching micro-partitions |
| **PIPE** | No staging overhead | Direct streaming with Ingest SDK (bypasses S3/Kafka) |
| **STREAM** | Processing cost reduction | Incremental CDC. Tasks will process only the new rows |
| **TASK WHEN clause** | Compute cost reduction | Skips execution if the stream is empty |
| **MERGE** | Data quality | Idempotent upserts prevent duplicates and handle deletes |

The combination of these five mechanisms produces a pipeline that is both cost-efficient and operationally simple.

### **Lessons Learned**

These are the mistakes and surprises I encountered and what I learned from the prototype.

1. **You connect to the table, not the PIPE.** An initial reading of the Snowpipe Streaming documentation can give the impression that a PIPE behaves like a Kafka connector target that consumers write into. In practice, the Ingest SDK connects directly to the Snowflake account and writes into the target table. The PIPE serves as a configuration layer, defining how incoming data should be handled (for example, case-insensitive column matching).

   Snowflake automatically creates a default PIPE for each table when one is not explicitly defined. In this implementation, an explicit PIPE was created solely to enable the `MATCH_BY_COLUMN_NAME` option.

   Understanding this behavior upfront would have avoided spending time exploring the documentation from the wrong perspective.
2. **A broken schema won't crash the pipeline but will silently corrupt your data.** This issue is subtle and easy to miss. When the upstream payload changes (for example, a field is renamed), the RAW table stores it without problem — it accepts any raw JSON blob. The problem arises later, in the BRONZE layer, when the MERGE task tries to extract a field that no longer exists by that name. Instead of failing loudly, it returns `NULL` and continues. The pipeline appears healthy, but the data might be incorrect. This is why agreeing on a stable payload contract with the upstream team matters more than most realise.
3. `'STREAMING'` **in the PIPE definition is not a file format like** `'CSV'` **or** `'JSON'`**.** Each type is used to answer different questions. `CSV` and `JSON` tell Snowflake *how to read a staged file*. `STREAMING` tells Snowflake *there is no file* — data is pushed directly by the SDK.
4. **Without a data guard, the TASK runs on an empty table every minute, and you still pay for it.** Snowflake TASK schedules are time-based, not data-based. If no new data arrives in the stream, the TASK still wakes, spins the warehouse, and runs the MERGE against zero rows. The fix is one line: `WHEN SYSTEM$STREAM_HAS_DATA(...)`, which tells the TASK to skip execution when no new data exists. It's easy to forget because everything works without it, but the credit waste adds up quickly on a busy schedule.
5. **The channel name is free traceability; use it deliberately.** The consumer sets the channel name to `rmq-<queue>-<hostname>`. Snowflake records this in the `channel_id` column of every row the consumer writes. While not intended for monitoring, it provides valuable visibility in a multi-consumer setup by showing which consumer instance wrote each row and helping detect stalled consumers. A small naming choice at the consumer level creates a built-in audit trail on Snowflake.
6. **The RSA private key needs extra preparation before it works in Docker.** Snowflake key-pair authentication guides show how to generate a `.pem` file for interactive authentication. However, passing the private key as an environment variable inside a Docker container fails with the raw PEM format (multi-line with `-----BEGIN...-----` headers). We must remove the header and footer and convert the key into a single unbroken string. This step is poorly documented and caused unexpected authentication failures during initial deployment.
7. **The consumer could run entirely inside Snowflake using Snowpark Container Services (SPCS).** During the prototype, the consumer was deployed as an external Docker container communicating with Snowflake over the public internet. Further exploration revealed support for running containerized workloads natively through Snowpark Container Services (SPCS), a managed container runtime within the Snowflake platform. Since the consumer is already packaged as a Docker image, deployment as an SPCS service would require minimal changes.

   The primary advantage is network locality. Running the container within SPCS enables communication with Snowflake over its internal network rather than the public internet, reducing network latency between the consumer and the Snowpipe Streaming endpoint while removing the need to expose Snowflake credentials externally. Authentication can leverage Snowflake's native identity and access model instead of externally managed RSA keys.

   As a result, the consumer becomes a first-class component within the Snowflake ecosystem rather than an external process, allowing the entire ingestion pipeline to operate as a self-contained solution on a single platform.

### **Limitations Identified**

1. **Free-tier constraint:** Snowflake OpenFlow could not be tested as an alternative because it is unavailable on free-tier accounts.
2. **Consumer resilience:** A single consumer instance is a single point of failure. Production use would require multiple instances with independent channels.
3. **Schema evolution:** If the upstream payload structure changes (e.g., field renames), the SQL extraction paths in the MERGE task must be updated manually. The VARIANT column in RAW absorbs the change silently, but the BRONZE layer breaks.
4. **Monitoring gaps:** No alerting is in place for ingestion lag, Snowpipe channel errors, or task failures.

## **6. Recommended Next Steps (If Moving to Production)**

1. **High Availability:** Deploy multiple consumer instances in a Snowflake ecosystem, one per queue, each with a unique channel name. Snowflake tracks offset independently per channel.
2. **Observability:** Monitor `SYSTEM$PIPE_STATUS()` and task history; integrate with Grafana for alerting on lag or failures.
3. **Schema Evolution Strategy:** Introduce schema versioning (a `schemaVersion` field in the payload) and use `COALESCE` in extraction queries to support multiple payload versions simultaneously.
4. **Disaster Recovery:** Configure a dead-letter exchange in RabbitMQ to capture messages that fail parsing. These are currently nacked without requeue and silently lost.

## **7. Appendix: Technical Stack**

| **Layer** | **Technology** | **Version** |
| --- | --- | --- |
| Consumer language | Java | 11 (build: JDK 21 via Docker) |
| Build tool | Gradle (Shadow plugin) | 9.6 |
| Snowflake Ingest SDK | `net.snowflake:snowflake-ingest-sdk` | 4.4.3 |
| AMQP client | `com.rabbitmq:amqp-client` | 5.32.0 |
| JSON parsing | Jackson Databind | 2.18.8 |
| Testing | JUnit 5 + Mockito | 5.11.3 / 5.14.2 |
| Snowflake warehouse size | XSMALL | — |
| Snowflake schemas | RAW, BRONZE | — |
| Deployment | Docker Compose | — |

## **8. References**

### **Snowflake Documentation**

* [Snowpipe Streaming Overview](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-overview)
* [Key-Pair Authentication & Key Rotation](https://docs.snowflake.com/en/user-guide/key-pair-auth)
* [Streams — Change Data Capture](https://docs.snowflake.com/en/user-guide/streams-intro)
* [Tasks — Scheduling SQL Statements](https://docs.snowflake.com/en/user-guide/tasks-intro)
* [MERGE Statement](https://docs.snowflake.com/en/sql-reference/sql/merge)
* [Table Clustering & Micro-partitions](https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions)
* [SYSTEM$STREAM\_HAS\_DATA](https://docs.snowflake.com/en/sql-reference/functions/system_stream_has_data)
* [SYSTEM$PIPE\_STATUS](https://docs.snowflake.com/en/sql-reference/functions/system_pipe_status)
* [Snowflake OpenFlow (Enterprise)](https://docs.snowflake.com/en/user-guide/openflow)

### **AMQP Consumer (Working Prototype)**

* [snowpipe-amqp-consumer](https://github.com/teqplay/snowpipe-amqp-consumer)