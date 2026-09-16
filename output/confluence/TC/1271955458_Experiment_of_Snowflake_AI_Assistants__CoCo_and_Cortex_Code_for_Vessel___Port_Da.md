---
id: confluence:1271955458
source: confluence
type: page
space: TC
title: 'Experiment of Snowflake AI Assistants: CoCo and Cortex Code for Vessel & Port
  Data Queries'
author: Ryan Kharisma Rakhmat
date: '2026-07-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1271955458
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1271955458
---
# Experiment of Snowflake AI Assistants: CoCo and Cortex Code for Vessel & Port Data Queries

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1271955458  

## Content

**Snowflake AI Experiment Report**

*Evaluating Snowflake Cortex AI Assistants — CoCo (Worksheet AI) and Cortex Code — for Natural-Language Querying of Vessel & Port Data*

|  |  |
| --- | --- |
| **Prepared by** | Ryan Kharisma Rakhmat |
| **Organization** | Teqplay — Data Engineering |
| **Platform** | Snowflake (<http://app.snowflake.com> ) |
| **AI Tools Tested** | CoCo (in-worksheet AI), Cortex Code (local desktop app) |
| **Environment** | API\_INGESTION\_PROTO database, DEV\_ETL\_MART schema |
| **Document Type** | Experiment / Proof-of-Concept Report |

*This report documents a hands-on experiment with Snowflake's built-in AI assistants — CoCo and Cortex Code — evaluating their ability to interpret natural-language questions, discover relevant tables, generate SQL, and return accurate answers against a maritime vessel-and-port dataset loaded into Snowflake. All results, queries, and timings below are taken directly from the experiment session log.*

# **1. Overview**

Snowflake provides two AI-assisted query interfaces built on Cortex: CoCo, an in-browser assistant embedded directly in the Snowflake worksheet UI, and Cortex Code, a standalone desktop application that connects to a Snowflake account via user credentials. This experiment tested both tools for setup friction, table/schema discovery, SQL generation accuracy, and response latency across a range of query difficulties.

## **1.1 Tools Under Test**

### **CoCo (Worksheet AI)**

●      Runs side-by-side with SQL inside the Snowflake worksheet at <http://app.snowflake.com> .

●      Accepts natural-language questions and answers using a multi-step reasoning process.

●      Generates and tailors SQL queries automatically based on the question asked.

### **Cortex Code**

●      Installed as a separate desktop application on macOS.

●      Connects to Snowflake by selecting “Connect a tool to Snowflake” from the account menu.

●      Authenticates using standard Snowflake account credentials.

●      Initial testing encountered a blocking error: “Oops! Cortex agent was not able to complete the request, please try again.”

## **1.2 Export Capability**

Whether or not the AI can export results as documents (e.g., PDF or Excel).

|  |
| --- |
| **FINDING**  *The answers is Yes. AI can export as a files and currently limited to CSV and HTML formats only. PDF and native Excel (.xlsx) export are not supported.* |

# **2. Experiment Setup**

To move beyond trivial queries, the Development database was exported to CSV and reloaded into a dedicated Snowflake schema, giving CoCo a realistic star-schema environment to reason over.

The exported CSV from AWS RDS PostgreSQL Development server are as below:

## **2.1 Environment Preparation**

|  |
| --- |
| USE WAREHOUSE TEQPLAY\_WH;  USE DATABASE API\_INGESTION\_PROTO;  CREATE OR REPLACE SCHEMA DEV\_ETL\_MART; |

## **2.2 Resulting Schema**

The DEV\_ETL\_MART schema resolved into a proper star schema, discovered by the AI across two follow-up prompts:

|  |  |  |
| --- | --- | --- |
| **Table** | **Role** | **Key Columns Used in Experiment** |
| FACT\_PORT\_VISIT | Fact table — one row per vessel port visit | VISIT\_ID, SHIP\_ID, PORT\_UNLOCODE, START\_TIMESTAMP, END\_TIMESTAMP, ANCHOR\_DURATION, DRIFTING\_DURATION, TOTAL\_MOORED\_DURATION |
| FACT\_BERTH\_VISIT | Fact table — berth-level tug activity | VISIT\_ID, UNIQUE\_TUGS\_ARRIVAL\_COUNT, UNIQUE\_TUGS\_DEPARTURE\_COUNT |
| FACT\_ANCHOR | Fact table — anchor / stationary events | Duration and event-level anchor data |
| DIM\_SHIP | Dimension — vessel master data | ID, NAME, IMO, GROSS\_TONNAGE, LENGTH\_OVER\_ALL, BEAM, DWT, SHIP\_CATEGORY, TYPE |
| DIM\_PORT | Dimension — port master data | UNLOCODE, NAME, DISPLAY\_NAME, COUNTRY\_CODE |

# **3. Test Queries and Results**

Six natural-language questions of increasing complexity were posed to CoCo. For each, CoCo's table-discovery process, generated SQL, and final answer are reported as observed in the session.

|  |
| --- |
| --Trying to run sample query to check whether the ingestions is success or not  SELECT COUNT(\*)  FROM DEV\_ETL\_MART.FACT\_PORT\_VISIT  WHERE port\_unlocode = 'NLRTM'  LIMIT 100; |

## **3.1 Query 1 — Biggest Ships Visiting Rotterdam (Exploratory)**

**Prompt: “Do you know the biggest 5 ships that visits Rotterdam in this years?”**

CoCo first searched for ship/port-related tables and initially selected STREAMING\_DB\_\_PROTO.BRONZE.STG\_SOF, a raw staging table with VARIANT (semi-structured) columns, before confirming Rotterdam data existed there.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **DATA COVERAGE CAVEAT**  *The staging table (STG\_SOF) only contained 44 Rotterdam records from a single date (2026-07-01), producing a limited, non-representative result before the schema was clarified.* | | | | |
| **#** | **Ship Name** | **IMO** | **Length (m)** | **Vessel Type** |
| 1 | NYK VIRGO | 9312810 | 338 | Sea Vessel |
| 2 | MSC MAEVA | 9289128 | 325 | Sea Vessel |
| 3 | KIEL EXPRESS | 9229855 | 321 | Sea Vessel |
| 4 | MSC NAIROBI X | 9605243 | 300 | Sea Vessel |
| 5 | VENTURE PELICAN | 9970569 | 298 | Sea Vessel |

## **3.2 Query 2 — Same Question, Re-scoped to DEV\_ETL\_MART Star Schema**

**Follow-up prompt: “find it on the API\_INGESTION\_PROTO.DEV\_ETL\_MART schema?”**

CoCo inspected DIM\_SHIP, DIM\_PORT, and FACT\_PORT\_VISIT, retrieved their columns, and re-ran the analysis using GROSS\_TONNAGE as the ranking metric instead of length.

|  |
| --- |
| SELECT      s.NAME AS ship\_name, s.IMO, s.GROSS\_TONNAGE,      s.LENGTH\_OVER\_ALL AS length\_m, s.BEAM AS beam\_m, s.DWT,      s.SHIP\_CATEGORY, s.TYPE AS ship\_type,      MIN(fpv.START\_TIMESTAMP) AS first\_visit,      COUNT(\*) AS visit\_count  FROM API\_INGESTION\_PROTO.DEV\_ETL\_MART.FACT\_PORT\_VISIT fpv  JOIN API\_INGESTION\_PROTO.DEV\_ETL\_MART.DIM\_SHIP s      ON fpv.SHIP\_ID = s.ID  WHERE fpv.PORT\_UNLOCODE = 'NLRTM'    AND YEAR(fpv.START\_TIMESTAMP) = 2026  GROUP BY s.NAME, s.IMO, s.GROSS\_TONNAGE, s.LENGTH\_OVER\_ALL,           s.BEAM, s.DWT, s.SHIP\_CATEGORY, s.TYPE  ORDER BY s.GROSS\_TONNAGE DESC NULLS LAST  LIMIT 5 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **#** | **Ship Name** | **IMO** | **Gross Tonnage** | **Length (m)** | **Type** | **Visits** |
| 1 | CMA CGM SAINT GERMAIN | 9987201 | 237,742 | 400 | Container | 2 |
| 2 | EVER ALLY | 9975791 | 236,680 | 399 | Container | 1 |
| 3 | EVER ACME | 9943267 | 236,673 | 400 | Container | 1 |
| 4 | CMA CGM CONCORDE | 9839208 | 236,583 | 400 | Container | 1 |
| 5 | CMA CGM RIVOLI | 9839193 | 236,583 | 400 | Container | 2 |

Observation: switching the ranking metric from length to gross tonnage and scoping to the proper star schema changed the result set entirely — all top-5 vessels became mega container ships (~400 m, 236,000+ GT), underscoring how sensitive the AI's answer is to which table/metric it selects unless the user disambiguates.

## **3.3 Query 3 — 10 Busiest US Ports**

**Prompt: “Show me the 10 most busiest port in the United State”**

|  |
| --- |
| SELECT      p.UNLOCODE, p.NAME AS port\_name, p.DISPLAY\_NAME,      COUNT(\*) AS total\_visits  FROM API\_INGESTION\_PROTO.DEV\_ETL\_MART.FACT\_PORT\_VISIT fpv  JOIN API\_INGESTION\_PROTO.DEV\_ETL\_MART.DIM\_PORT p      ON fpv.PORT\_UNLOCODE = p.UNLOCODE  WHERE p.COUNTRY\_CODE = 'US'  GROUP BY p.UNLOCODE, p.NAME, p.DISPLAY\_NAME  ORDER BY total\_visits DESC  LIMIT 10 |

 The answers are:

|  |  |  |  |
| --- | --- | --- | --- |
| **#** | **Port** | **UNLOCODE** | **Total Visits** |
| 1 | Port of New York | USNYC | 8,254 |
| 2 | Port of Corpus Christi | USCRP | 7,896 |
| 3 | Port of New Orleans | USMSY | 5,985 |
| 4 | Port of Savannah | USSAV | 4,095 |
| 5 | Baltimore, MD | USBAL | 3,253 |
| 6 | South Louisiana | USLUA | 3,085 |
| 7 | Beaumont, TX | USBPT | 2,467 |
| 8 | Baton Rouge, LA | USBTR | 2,312 |
| 9 | Port of Plaquemines | USPLQ | 1,863 |
| 10 | Port of Houston | USHOU | 1,412 |

This query completed quickly with no schema-discovery back-and-forth, since the tables were already established in context from the prior queries.

## **3.4 Query 4 — Ships Visiting Rotterdam Last Month**

**Prompt: “How many ship visited Port of Rotterdam last month?”**

|  |
| --- |
| SELECT      COUNT(DISTINCT fpv.SHIP\_ID) AS unique\_ships,      COUNT(\*) AS total\_visits  FROM API\_INGESTION\_PROTO.DEV\_ETL\_MART.FACT\_PORT\_VISIT fpv  WHERE fpv.PORT\_UNLOCODE = 'NLRTM'    AND fpv.START\_TIMESTAMP >= '2026-06-01'    AND fpv.START\_TIMESTAMP < '2026-07-01' |

Result: 2,001 unique ships; 2,568 total visits (some vessels visited more than once) in June 2026.

## **3.5 Query 5 — Visits With More Than Two Tugs (Complex, Multi-Table)**

**Prompt: “Which are the 10 most recent visits with more than two tugs at the Port of Rotterdam? Please prioritize using visit\_id when joining the main tables. Please include visit ID, vessel name, IMO, ship category, arrival tugs, departure tugs, and total tugs.”**

CoCo first queried INFORMATION\_SCHEMA.COLUMNS to locate tug-related fields, identified FACT\_BERTH\_VISIT as the source, confirmed the join key (VISIT\_ID) existed on both fact tables, and only then generated the final query — a three-step discovery process before execution.

|  |
| --- |
| SELECT      fpv.VISIT\_ID, s.NAME AS vessel\_name, s.IMO, s.SHIP\_CATEGORY,      bv.UNIQUE\_TUGS\_ARRIVAL\_COUNT AS arrival\_tugs,      bv.UNIQUE\_TUGS\_DEPARTURE\_COUNT AS departure\_tugs,      (COALESCE(bv.UNIQUE\_TUGS\_ARRIVAL\_COUNT, 0) +       COALESCE(bv.UNIQUE\_TUGS\_DEPARTURE\_COUNT, 0)) AS total\_tugs,      fpv.START\_TIMESTAMP AS visit\_start  FROM API\_INGESTION\_PROTO.DEV\_ETL\_MART.FACT\_PORT\_VISIT fpv  JOIN API\_INGESTION\_PROTO.DEV\_ETL\_MART.FACT\_BERTH\_VISIT bv      ON fpv.VISIT\_ID = bv.VISIT\_ID  JOIN API\_INGESTION\_PROTO.DEV\_ETL\_MART.DIM\_SHIP s      ON fpv.SHIP\_ID = s.ID  WHERE fpv.PORT\_UNLOCODE = 'NLRTM'    AND (COALESCE(bv.UNIQUE\_TUGS\_ARRIVAL\_COUNT, 0) +         COALESCE(bv.UNIQUE\_TUGS\_DEPARTURE\_COUNT, 0)) > 2  ORDER BY fpv.START\_TIMESTAMP DESC  LIMIT 10 |

 The answers are:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **Vessel** | **IMO** | **Category** | **Arr. Tugs** | **Dep. Tugs** | **Total** | **Visit Start** |
| 1 | MSC VAISHNAVI R. | 9227340 | Container | 2 | 1 | 3 | 2026-06-17 |
| 2 | SANTA CLARA MAERSK | 9444716 | Container | 2 | 2 | 4 | 2026-06-16 |
| 3 | NIKOLAY ZUBOV | 9768526 | Tanker | 4 | 2 | 6 | 2026-06-16 |
| 4 | FERASET | 9747651 | Bulk Carrier | 2 | 2 | 4 | 2026-06-16 |
| 5 | MSC ALICANTE | 9480174 | Container | 2 | 3 | 5 | 2026-06-16 |
| 6 | MSC BRITTANY | 9724049 | Container | 2 | 1 | 3 | 2026-06-16 |
| 7 | CARTAGENA EXPRESS | 9777618 | Container | 1 | 2 | 3 | 2026-06-16 |
| 8 | VAGA MAERSK | 9778545 | Container | 1 | 2 | 3 | 2026-06-15 |
| 9 | MAERSK BALI | 9394870 | Container | 2 | 1 | 3 | 2026-06-15 |
| 10 | ALFA FINLANDIA | 9823041 | Tanker | 1 | 2 | 3 | 2026-06-15 |

NIKOLAY ZUBOV (tanker) required the most tugs overall (6 total). Container vessels dominated the list, consistent with their larger size typically requiring tug assistance.

## **3.6 Query 6 — Stationary Vessels With Movement Event Breakdown (Most Complex)**

**Prompt: “Which vessels visited Port of Rotterdam in July-August 2025 and remained stationary for more than 30 minutes? Show me their movement events during the visit”**

This was the most demanding prompt in the session. CoCo needed two schema-discovery passes: first checking FACT\_PORT\_VISIT, FACT\_ANCHOR, FACT\_BERTH\_VISIT, and FACT\_PILOT for duration/anchor/stationary-related columns, then pulling the full column list of FACT\_ANCHOR before settling on FACT\_PORT\_VISIT's built-in duration fields as the most complete source.

|  |
| --- |
| WITH stationary\_visits AS (      SELECT          fpv.VISIT\_ID, fpv.SHIP\_ID,          fpv.START\_TIMESTAMP AS visit\_start,          fpv.END\_TIMESTAMP AS visit\_end,          fpv.ANCHOR\_DURATION, fpv.DRIFTING\_DURATION,          fpv.TOTAL\_MOORED\_DURATION, fpv.SAILING\_IN\_DURATION,          fpv.SAILING\_OUT\_DURATION, fpv.SHIFTING\_DURATION,          fpv.TOTAL\_WAITING\_TIME\_BEFORE\_ARRIVAL\_DURATION,          fpv.TOTAL\_WAITING\_TIME\_DURING\_VISIT\_DURATION,          fpv.TURN\_AROUND\_TIME\_DURATION      FROM API\_INGESTION\_PROTO.DEV\_ETL\_MART.FACT\_PORT\_VISIT fpv      WHERE fpv.PORT\_UNLOCODE = 'NLRTM'        AND fpv.START\_TIMESTAMP >= '2025-07-01'        AND fpv.START\_TIMESTAMP < '2025-09-01'        AND fpv.ANCHOR\_DURATION > 30  )  SELECT      sv.VISIT\_ID, s.NAME AS vessel\_name, s.IMO, s.SHIP\_CATEGORY,      sv.visit\_start, sv.visit\_end,      sv.ANCHOR\_DURATION AS anchor\_min,      sv.DRIFTING\_DURATION AS drifting\_min,      sv.SAILING\_IN\_DURATION AS sailing\_in\_min,      sv.TOTAL\_MOORED\_DURATION AS moored\_min,      sv.SAILING\_OUT\_DURATION AS sailing\_out\_min,      sv.SHIFTING\_DURATION AS shifting\_min,      sv.TOTAL\_WAITING\_TIME\_BEFORE\_ARRIVAL\_DURATION AS wait\_before\_min,      sv.TOTAL\_WAITING\_TIME\_DURING\_VISIT\_DURATION AS wait\_during\_min,      sv.TURN\_AROUND\_TIME\_DURATION AS turnaround\_min  FROM stationary\_visits sv  JOIN API\_INGESTION\_PROTO.DEV\_ETL\_MART.DIM\_SHIP s      ON sv.SHIP\_ID = s.ID  ORDER BY sv.ANCHOR\_DURATION DESC  LIMIT 20 |

Top results (durations in minutes; truncated to 10 of 20 returned rows for readability):

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **#** | **Vessel** | **Category** | **Anchor** | **Drift** | **Moored** | **Wait During** | **Turnaround** |
| 1 | ALFA BALTICA | Tanker | 1,041 | 1 | 25 | 0 | 66 |
| 2 | ZHI YUAN KOU | General Cargo | 915 | 0 | 384 | 800 | 1,194 |
| 3 | EFFIE MAERSK | Tanker | 695 | 19 | 131 | 0 | 1,341 |
| 4 | ARKLOW RACER | General Cargo | 623 | 1 | 237 | 584 | 1,455 |
| 5 | ZHONG REN 121 | General Cargo | 580 | 0 | 428 | 580 | 1,172 |
| 6 | FIGARO | General Cargo | 557 | 23 | 15 | 0 | 599 |
| 7 | ARKLOW RALLY | General Cargo | 546 | 1 | 29 | 499 | 1,085 |
| 8 | FURTUNA | Tanker | 515 | 0 | 7 | 0 | 27 |
| 9 | HAPPY PENGUIN | Tanker | 491 | 1 | 46 | 0 | 57 |
| 10 | TITAN HARMONY | Tanker | 475 | 1 | 99 | 0 | 153 |

Key observations from CoCo's own summary: ALFA BALTICA had the longest anchor time (~17 hours), tankers and general cargo vessels dominated extended-stationary cases (likely berth or cargo-schedule waits), and several vessels also logged significant in-visit waiting time alongside their anchor duration.

# **4. Response Time Summary**

Observed end-to-end response times (question submission to final answer) as reported during the session:

|  |  |  |  |
| --- | --- | --- | --- |
| **Query** | **Complexity** | **Discovery Steps** | **Response Time** |
| Q1 — Biggest ships (initial, staging table) | Exploratory | 1 table search | Less than 10 seconds |
| Q2 — Biggest ships (DEV\_ETL\_MART, re-scoped) | Moderate | 3 metadata lookups | Less than 10 seconds |
| Q3 — 10 busiest US ports | Simple | 0 (context reused) | Less than 10 seconds |
| Q4 — Ships visiting Rotterdam last month | Simple | 0 (context reused) | ≈ 14 seconds |
| Q5 — Visits with > 2 tugs (multi-table, ordered) | Complex | 2 metadata lookups | ≈ 33 seconds |
| Q6 — Stationary vessels with movement events | Most complex | 2 metadata lookups | ≈ 48 seconds |

Trend observed: response time scaled with query complexity and the number of schema-discovery steps CoCo needed before it could write a confident final query — from ~14 seconds for a single-table aggregate to ~48 seconds for a multi-column, multi-metric query requiring two rounds of column exploration.