---
id: github:teqplay/dataflow_dag_core:pr:722
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 722
title: Release 1.53.0 to master
author: panjiyudasetya
state: closed
date: '2026-07-10'
merged_at: '2026-07-10'
base_branch: master
head_branch: release/1.53.0
url: https://github.com/teqplay/dataflow_dag_core/pull/722
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2818
---
# PR #722: Release 1.53.0 to master

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/722  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `release/1.53.0`  
**Created:** 2026-07-10  
**Merged:** 2026-07-10  

## Description


## [1.53.0] - 2026-07-10
### Deprecated
- Deprecate and purge legacy file-cache-based SOF streaming DAGs (#720)

## Commits

- `d254496d` **Panji Y. Wiwaha** (2026-06-26): Merge pull request #715 from teqplay/release/1.52.0
  Release 1.52.0 to develop
- `6fa2e706` **Panji Y. Wiwaha** (2026-07-02): Merge pull request #718 from teqplay/hotfix/1.52.1
  Release 1.52.1 to develop
- `846a9a03` **Panji Y. Wiwaha** (2026-07-08): remove(sof): delete legacy file-cache-based SOF DAGs and task groups
  Removes 22 DAGs that used the old file-caching streaming architecture
  (v1) in favour of the queue-based decoupled architecture (v2) already
  in production via the staging_sof stream DAGs.
  
  Deleted DAG groups:
  - streaming/rabbitmq_sof: barge/sea_vessel subscriber + handler DAGs
    (including deferrable variants)
  - mart/fact_sof: barge_deleted, barge_updated, sea_vessel_deleted,
    sea_vessel_updated, streaming (hard-deletion), streaming (updated)
  - warehouse/ods/ods_sof: barge_deleted, barge_updated, sea_vessel_deleted,
    sea_vessel_updated, soft_deletion, streaming_ingestion, hard_deletion
  - utilities: analyze_streaming_consumed_messages
  
  Also removes teqplay/tasks/streaming/sof/ task layer (task_consumers,
  task_groups, utils) which existed solely to support these DAGs.
  
  DAG ID enum entries removed from the relevant __init__.py files.
  
  Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
- `9ac272c6` **Panji Y. Wiwaha** (2026-07-08): remove(sof): remove legacy RabbitMQ service classes, operators, and triggers
  Strips out the v1 file-caching service hierarchy and the two operator/
  trigger classes that depended on it, now that all consuming DAGs are gone.
  
  Services:
  - BaseSOFRMQService (1100+ lines) removed from base.py; kept BaseSOFRMQServiceWithoutCache
  - BargeRMQService removed from barge.py; kept BargeRMQServiceWithoutCache
  - SeaVesselRMQService removed from sea_vessel.py; kept SeaVesselRMQServiceWithoutCache
  
  Operators:
  - RabbitMQDeferrableOperator removed (used only by deleted subscriber DAGs)
  - RabbitMQBatchDeferrableOperator removed (never wired to any DAG)
  - BasicRabbitMQDeferrableOperator retained (used by staging_sof stream DAGs)
  
  Triggers:
  - RabbitMQMessageTrigger removed from rabbitmq_trigger.py
  - RabbitMQBatchTrigger removed from rabbitmq_trigger.py
  - BasicRabbitMQMessageTrigger retained; triggers/__init__.py updated accordingly
  
  Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
- `9c092978` **Panji Y. Wiwaha** (2026-07-09): Merge pull request #720 from teqplay/PTO-2818
  PTO-2818 Deprecate and purge legacy file-cache-based SOF streaming DAGs
- `a76aaf15` **Panji Y. Wiwaha** (2026-07-10): Bump version 1.53.0

## Reviews

### ryan-kharisma — APPROVED (2026-07-10)

LGTM

## Comments
