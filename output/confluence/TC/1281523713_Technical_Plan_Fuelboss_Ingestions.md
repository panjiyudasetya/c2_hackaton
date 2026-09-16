---
id: confluence:1281523713
source: confluence
type: page
space: TC
title: Technical Plan Fuelboss Ingestions
author: Ryan Kharisma Rakhmat
date: '2026-07-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1281523713
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1281523713
---
# Technical Plan Fuelboss Ingestions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1281523713  

## Content

# **1. Purpose and Scope**

This document defines a plan for ingesting data from operational sources into an analytical environment using the ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) approaches. Data ingestion is the process that moves data from its operational plane — CRMs, ERPs, maritime systems, financial systems, IoT sensors, APIs, documents, and other source systems — into the analytical plane, where it powers dashboards, AI models, and other analytical products. Selecting the right ingestion pattern is a strategic decision that determines how well an organization can scale its analytical capability as data sources multiply.

|  |  |  |
| --- | --- | --- |
| **Pattern** | **Summary** | **Best Fit** |
| **ETL** (Extract, Transform, Load) | Data is extracted, transformed on a dedicated server, then loaded into the analytics platform. | Centralized, visually managed pipelines; moderate data volumes. |
| **ELT** (Extract, Load, Transform) | Raw data is extracted and loaded first; transformation runs later inside the analytics platform. | Large, varied data sets; teams needing flexible, best-of-breed tooling. |

This plan adopts ETL and ELT as the primary ingestion patterns because they scale to many heterogeneous sources, decouple ingestion from the operational systems, and support governed, auditable pipelines — requirements that Unified Data Repository and pure Data Virtualization struggle to meet at scale.

# **2. The ETL Approach**

In ETL, data is extracted from source systems, transformed on a dedicated ETL server or engine, and then loaded into the target analytical store (e.g., a data warehouse or operational data store). Transformation logic is centralized and typically configured through a visual design interface, often supplemented with scripting (python/java/scala) or SQL.

## **2.1 Advantages**

* **Centralized logic —** all transformation rules live in one managed environment, simplifying oversight of how source data is shaped for analysis.
* **User-friendly design —** visual, drag-and-drop pipeline builders let a broader range of skill levels contribute to pipeline development.

## **2.2 Limitations**

* **Vendor lock-in —** dependence on a specific ETL tool makes migration costly if pricing or features change.
* **Performance constraints —** transformations run on the ETL server itself, which rarely matches the compute power of a modern cloud data warehouse, creating a throughput bottleneck.
* **Opaque data lineage —** visual abstraction can hide the real complexity of transformations, making lineage and auditing harder for anyone outside the tool.
* **Limited scalability —** many ETL tools were not built for DataOps-style industrialization as platforms grow.
* **Rigidity —** tools that cannot accommodate unusual ingestion requirements force workarounds that accumulate technical debt.

Note: some of these limitations are mitigated by ETL tools built into a specific cloud data warehouse suite. Tool selection should account for this.

# **3. The ELT Approach**

ELT restructures the same three steps: Extract and Load (EL) happen first, moving raw data directly into the analytics platform without immediate transformation. Transformation (T) happens afterward, inside the platform, and can run on an independent schedule from extraction and loading.

## **3.1 Advantages**

* **Enhanced flexibility —** decoupling extraction/loading from transformation allows different tools to be matched to different data types and transformation needs.
* **Aligned performance —** transformation runs inside the data platform, using its full distributed compute power — well suited to large data volumes.
* **Improved scalability —** the multi-tool flexibility of ELT makes it easier to choose transformation tools built for automation and scale.

## **3.2 Limitations**

* **Multi-tool governance —** using separate tools for extraction, loading, and transformation requires disciplined governance of licensing, pricing, updates, and support.
* **Orchestration complexity —** a more varied toolkit needs sophisticated orchestration (commonly DAG-based) to guarantee transformations only run after extraction and loading succeed.

# **4. ETL vs. ELT: Decision Criteria**

|  |  |  |
| --- | --- | --- |
| **Criterion** | **ETL** | **ELT** |
| Where transformation runs | Dedicated ETL server/engine | Inside the analytics platform (uses platform compute) |
| Scalability for large volumes | Constrained by ETL server capacity | Scales with the data platform's distributed compute |
| Tooling model | Single, integrated tool | Best-of-breed tools per stage; more moving parts |
| Governance overhead | Lower — one vendor/tool to manage | Higher — multiple tools, licenses, and update cycles |
| Orchestration needs | Built into the tool's workflow engine | Requires explicit DAG-based orchestration |
| Data lineage visibility | Can be opaque behind visual abstraction | Depends on tooling; transformation logic is typically code-based and more auditable |
| Vendor lock-in risk | Higher | Lower — stages can be swapped independently |

Recommendation: default to ELT when data volumes are large, sources are varied, and the organization can support an orchestration layer (e.g., a DAG-based scheduler) and multi-tool governance. Favor ETL when a single managed tool, simpler governance, and moderate data volumes are priorities, or when an ETL suite is already tightly integrated with the target cloud data warehouse.

# **5. Implementation Plan**

The following phased plan applies to either approach; steps marked (ELT) are specific to an ELT build.

## **Phase 1 — Source Assessment**

1. Inventory operational sources: CRMs, ERPs, maritime systems, financial systems, IoT sensors, APIs, documents, and other unconventional formats.
2. Classify each source by volume, velocity, change frequency, and criticality to downstream analytics.
3. Identify constraints on each source system (query load tolerance, network zone, access method).

Here is the source of Fuelboss data in Microsoft SQL Server as below architecture diagram that groups into the 5 groups as (1)the external data provider, (2)bunkering schedule, (3)bunkering operations, (4)bunkering inventory and (5)gatekeeper:

## **Phase 2 — Pattern and Tool Selection**

4. Confirm ETL vs. ELT per source or per domain, using the decision criteria in previous sections.
5. Select extraction/loading tooling; for ELT, select transformation tooling separately (e.g., SQL-based transformation frameworks running in the warehouse).
6. Evaluate vendor lock-in exposure and total cost of ownership before committing.

## **Phase 3 — Pipeline Design**

7. Design extraction jobs (full loads, incremental/CDC, or batch schedules) per source.
8. Define the loading target: staging area, operational data store, or data warehouse schema.
9. (ELT) Design transformation models to run inside the platform, decoupled from extraction/loading schedules.

10.(ETL) Design transformation logic within the ETL tool, keeping it centralized and documented.

## **Phase 4 — Orchestration and Governance**

11.(ELT) Implement DAG-based orchestration to sequence extraction, loading, and transformation, with dependency checks.

12.Establish governance for tool licensing, update cycles, and support ownership across all tools in the pipeline.

13.Define data lineage documentation and auditing practices, particularly where visual ETL tools obscure transformation logic.

## **Phase 5 — Build, Test, and Deploy**

14.Build pipelines incrementally, starting with the highest-priority sources identified in Phase 1.

15.Test for data quality, schema drift handling, and failure recovery (especially for incremental/CDC extraction).

16.Deploy with monitoring and alerting on job failures, latency, and data volume anomalies.

## **Phase 6 — Monitor and Evolve**

17.Track pipeline performance against growing data volumes and new source types.

18.Periodically re-evaluate the ETL/ELT tooling decision as the platform scales or vendor roadmaps shift.

19.Assess readiness for emerging patterns (Section 6) as real-time requirements grow.

# **6. Emerging Patterns to Plan For**

Two emerging patterns should inform the longer-term evolution of this plan, even if not adopted immediately:

* **Push over pull —** instead of the analytical plane pulling data on a schedule, operational systems push changes as they occur. This suits organizations with strong application development capacity, but requires resilient handling of push failures, typically via streaming infrastructure.
* **Stream processing —** continuous, low-latency event flows (e.g., for IoT monitoring or financial transactions) can feed ELT/ETL pipelines through streaming consumers, or be queried directly from a streaming cache. Architectures such as Kappa and Lambda describe how to unify streaming and static data sources.

These patterns can be layered onto the ETL/ELT foundation as specific sources or use cases demand lower latency than batch ingestion can provide.

# **7. Conclusion**

**ETL** and **ELT** remain the most broadly applicable patterns for ingesting data at scale from diverse operational sources. ETL offers centralized, accessible tooling at the cost of performance ceilings and potential vendor lock-in; ELT offers superior flexibility and scalability at the cost of multi-tool governance and orchestration complexity. This plan recommends ELT as the default for large-scale, multi-source ingestion, with ETL retained for simpler, lower-volume, or tightly-integrated-suite scenarios. Both approaches should be executed through the six-phase plan above, with the emerging push and streaming patterns evaluated as real-time requirements emerge.