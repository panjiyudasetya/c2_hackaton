---
id: confluence:891453441
source: confluence
type: page
space: TC
title: Manual Handling Guide for Airflow DAG Failure
author: Ryan Kharisma Rakhmat
date: '2025-09-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/891453441
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/891453441
---
# Manual Handling Guide for Airflow DAG Failure

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/891453441  

## Content

## 1. Introduction

This document provides guidelines for manually handling failed Airflow jobs. The primary DAG in scope is `start\_etl\_pipeline`, which orchestrates multiple dependent tasks, including sub-DAGs such as `staging\_ingestion`. Failures in these tasks can propagate and block downstream jobs. The goal is to ensure proper recovery and rerun strategies without compromising data consistency.

## 2. Identifying Failures

1. Open the Airflow UI and navigate to the DAG `start\_etl\_pipeline`.
2. Inspect the task grid to identify failed tasks (marked in red).
3. Check if the failed task is a TriggerDagRunOperator (e.g., `run\_staging\_ingestion`), which starts another DAG.
4. Drill down into the triggered DAG (e.g., `staging\_ingestion`) to see which mapped or individual tasks failed.

## 3. Handling Sub-DAG Failures

When a TriggerDagRunOperator fails, the issue is typically within the triggered DAG. Follow these steps:

1. Navigate to the triggered DAG (e.g., `staging\_ingestion`).
2. Open the failed task (e.g., `run\_staging\_sof\_ingestion`).
3. Review logs to identify root cause (e.g., connection issues, data inconsistencies, timeout).
4. If the failure is transient (e.g., timeout), clear the failed task and rerun it.
5. If failure is due to bad input or configuration, fix the issue (e.g., source data, parameter update) before rerunning.
6. Re-run only the failed mapped tasks instead of the whole DAG to save time when possible.

## 4. Restart Strategies

Depending on the failure type, use one of the following strategies:

* Clear Task: Clears the failed task instance so Airflow can rerun it on the next scheduler cycle.
* Rerun with Upstream: If data dependencies are broken, clear failed task along with upstream tasks.
* Rerun Downstream: If failure blocks downstream tasks, clear the failed task and rerun downstream dependencies.
* Full DAG Rerun: For critical inconsistencies, rerun the entire DAG run.

## 5. Escalation & Best Practices

* Always review logs before rerunning tasks to avoid repeated failures.
* Document root cause and corrective action in a runbook or issue tracker.
* Escalate to the Data Engineering team if failures persist after multiple retries.
* For external system issues (e.g., database outages), coordinate with the responsible team.

## 6. Conclusion

By following this manual handling guide, operators can safely recover Airflow DAGs such as `start\_etl\_pipeline` and its sub-DAGs (`staging\_ingestion`) after task failures. Consistent application of these practices minimizes downtime and ensures reliable ETL processing.

## 7. Screenshots for Reference

The following screenshots illustrate typical failure cases in Airflow DAGs and how to inspect them:

Failure in `start_etl_pipeline` at task `run_staging_ingestion`. The task failed with TriggerDagRunOperator.

Failure observed in `staging\_ingestion` DAG. The task `run\_staging\_sof\_ingestion` shows multiple retries and warnings.

Mapped tasks view in `staging\_ingestion` DAG showing some tasks failed while others succeeded.

Clear and Retry task for starting to re-running Only Failed task then click the `Clear` button there.

Progressing `staging\_ingestion` DAG run with some mapped tasks running and others succeeded.

Final status of `start\_etl\_pipeline` where `run\_staging\_ingestion` failed, blocking downstream transformations. You can set to `Success` because previously has successfully re-running the `staging_ingestions` DAG.