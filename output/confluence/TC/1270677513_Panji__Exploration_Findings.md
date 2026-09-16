---
id: confluence:1270677513
source: confluence
type: page
space: TC
title: '[Panji] Exploration Findings'
author: Panji Y. Wiwaha
date: '2026-07-03'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1270677513
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1270677513
---
# [Panji] Exploration Findings

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1270677513  

## Content

## **Snowflake’s strengths and weaknesses during exploration**

| Area | Summary |
| --- | --- |
| **Objective** | Explore Snowflake's key strengths and trade-offs. |
| **Strengths** | * **Query across multiple databases** without moving data first. * **Automatically optimizes data storage** to improve performance and reduce costs. * **Tracks data changes automatically**, making incremental updates much easier. * **Built-in workflow automation** for scheduled or event-driven pipelines. * **Familiar developer experience** with seamless workflows between VS Code and Snowsight. * **End-to-end data platform** for ingestion, transformation, governance, and analytics. |
| **Considerations** | * **Limited manual performance tuning** compared to traditional databases. * **Optimization features consume credits**, so they should be used carefully. * **SQL queries consume compute credits**, so efficient queries help control costs. |

## **Near-Real Time Ingestion Discovery**

| Area | Summary |
| --- | --- |
| **Objective** | Demonstrate real-time data ingestion from RabbitMQ into Snowflake without intermediate storage. |
| **Outcome** | Successfully built a working end-to-end prototype with fully automated data ingestion and processing. |
| **What was built** | A Java consumer that streams data from RabbitMQ into Snowflake, along with automated processing to load and reconcile the data. |
| **Why it's efficient** | No intermediate storage, processes only new data, avoids unnecessary compute costs, and prevents duplicate records. |
| **Key discovery** | The consumer can potentially run directly inside Snowflake, simplifying deployment, reducing latency, and minimizing credential management. |
| **Known limitations** | Currently relies on a single consumer, has limited handling for schema changes, and lacks monitoring and alerting. |

## **Data Exposure Strategy for Snowflake Schema to Internal Applications**

| Area | Summary |
| --- | --- |
| **Objective** | Identify the best way to expose curated Snowflake data to internal applications while keeping it secure, performant, and easy to maintain. |
| **Option 1: Direct SQL Access** | Best for Power BI. Simple to operate and delivers good performance when using Materialized Views. |
| **Option 2: SQL API** | Suitable for internal scripts and automation. Easy to use for one-off tasks, but not ideal as a shared API because it lacks built-in documentation and developer-friendly features. |
| **Option 3: FastAPI on SPCS** | Best for engineering teams. Provides a modern REST API with built-in documentation, validation, and secure authentication managed by Snowflake. |
| **Key Finding** | Different consumers have different needs. Power BI should use Direct SQL, while applications should use FastAPI. The SQL API is best reserved for ad-hoc scripting. |
| **Recommended Architecture** | Use Materialized Views as the shared data layer, Direct SQL for Power BI, FastAPI for applications, and SQL API for internal scripts. |
| **Security** | Access is controlled through Snowflake roles, network restrictions, data masking, and full audit logging. |