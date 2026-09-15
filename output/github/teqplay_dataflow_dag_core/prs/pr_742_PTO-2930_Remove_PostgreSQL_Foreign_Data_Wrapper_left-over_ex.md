---
id: github:teqplay/dataflow_dag_core:pr:742
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 742
title: PTO-2930 Remove PostgreSQL Foreign Data Wrapper left-over experiment
author: panjiyudasetya
state: closed
date: '2026-08-19'
merged_at: '2026-08-21'
base_branch: develop
head_branch: PTO-2930
url: https://github.com/teqplay/dataflow_dag_core/pull/742
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2930
---
# PR #742: PTO-2930 Remove PostgreSQL Foreign Data Wrapper left-over experiment

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/742  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2930`  
**Created:** 2026-08-19  
**Merged:** 2026-08-21  

## Description

### Description
- Remove all PostgreSQL Foreign Data Wrapper (FDW) DAGs, task groups, SQL templates, and QC checks — the experiment was successful but we decided not to adopt FDW at this stage
- Remove FDW-related Airflow variable keys (`SOF_STREAMING_RUN_COUNTER`, `SOF_STREAMING_BATCH_DATA`, and variants) that were introduced as part of the experiment
- Restore "legacy" labels and docstrings that were added in anticipation of FDW becoming the primary workflow (`FactTransformationParams`, `fact_transformation_dag.py`)
- Simplify `ddl/fact/temp/terminal_visits.sql` — remove the `use_fdw` Jinja conditional that skipped FK constraints; FK constraints are now always included
- Retain the performance indexes that were added to ODS and fact tables during the FDW experiment — they provide general query benefit and are not FDW-specific

### What was removed
| Category | Count |
|---|---|
| DAGs (`fact_transformation_fdw`, `sea_vessel_fdw`, `barge_fdw`, `accuracy/fdw`) | 4 files |
| Task group functions (`load_fact_*_fdw` across `main_task_groups.py` and `refresh_task_groups.py`) | 8 functions |
| QC task group files (`*_fdw_task_groups.py`) | 4 files |
| DML `fdw_proceed.sql` templates | 8 files |
| FDW infrastructure SQL (`import_schema.sql`, `drop_foreign_tables.sql`) | 2 files |
| QC accuracy SQL under `fdw/` subdirectories | 19 files |
| DAG ID enum entries | 3 entries |

### Test plan

- [ ] Existing `fact_transformation` DAG and its sub-DAGs (`fact_sof__sea_vessel`, `fact_sof__barge`) are unaffected
- [ ] `prepare_database` DDL DAG runs without errors — no references to removed FDW operators
- [ ] Silver / Gold KPI monthly refresh is unaffected
- [ ] No remaining `fdw` references in source files

## Commits

- `ae04d73b` **Panji Y. Wiwaha** (2026-08-19): chore(fdw): remove PostgreSQL Foreign Data Wrapper experiment
  The FDW approach was successfully validated but we decided not to adopt it
  at this stage. This removes all FDW-specific DAGs, task groups, SQL templates,
  QC checks, and related variable keys, leaving only the legacy Python-chunking
  workflow.

## Reviews

### ryan-kharisma — APPROVED (2026-08-21)

Looks Good

## Comments
