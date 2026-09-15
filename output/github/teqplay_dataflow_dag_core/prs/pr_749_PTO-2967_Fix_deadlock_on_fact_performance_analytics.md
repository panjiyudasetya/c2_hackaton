---
id: github:teqplay/dataflow_dag_core:pr:749
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 749
title: PTO-2967 Fix deadlock on fact performance analytics
author: ryan-kharisma
state: closed
date: '2026-08-28'
merged_at: '2026-08-31'
base_branch: develop
head_branch: PTO-2967
url: https://github.com/teqplay/dataflow_dag_core/pull/749
labels: []
linked_issues: []
explicit_links: []
---
# PR #749: PTO-2967 Fix deadlock on fact performance analytics

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/749  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `develop` ← `PTO-2967`  
**Created:** 2026-08-28  
**Merged:** 2026-08-31  

## Description

fix(port-performance-analytics): batch fact_port_visit outlier-flag update to avoid deadlocks

Description:

Summary
update_port_visit_from_temp ran one unscoped UPDATE fact_port_visit over the whole vessel-type slice, holding locks long enough to deadlock against the streaming pipeline's concurrent writes to the same table (incident 2026-08-15). Replaced it with a Python task that commits 5,000-row batches instead of one large transaction.
Added retries=2, retry_delay=15s on the task so a batch that still loses a rare deadlock retries instead of failing the whole fact_daily_refresh run.
Removed the now-unused update_port_visit_from_temp.sql template.

Test plan
 DagBag parses fact_daily_refresh_dag.py cleanly; task resolves at the same task-id path with pool=fact_sql_pool, retries=2.
 Verified batching logic against a throwaway Postgres (12,345 rows, batch_size=5000 → 3 batches of 5000/5000/2345); all rows updated correctly, unrelated vessel-type rows left untouched.


## Commits

- `717e805d` **ryan_at_teqplay** (2026-08-28): fix(port-performance-analytics): batch fact_port_visit outlier-flag update to avoid deadlocks
  update_port_visit_from_temp ran a single UPDATE over the entire vessel-type
  slice of fact_port_visit, which held its locks long enough to collide with
  the streaming pipeline's continuous writes to the same table (deadlock
  detected while updating tuple in relation fact_port_visit, incident
  2026-08-15). Replace it with a Python task that commits 5,000-row batches
  instead of one large transaction, shortening the lock window per batch, and
  add task-level retries so a batch that still loses a rare deadlock retries
  instead of failing the whole DAG run.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `c6c79745` **ryan_at_teqplay** (2026-08-28): chore(docker-compose): raise local worker cpu limit and disable triggerer
  The worker's cpus limit (1, matching the Kubernetes deployment) starves it
  locally given AIRFLOW__CELERY__WORKER_CONCURRENCY=5, causing task timeouts
  and failed healthchecks — raise it to 4 for local dev. Also comment out the
  triggerer service locally to free up resources; left in place (commented)
  so it's easy to re-enable.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `d3c22349` **ryan_at_teqplay** (2026-08-28): revert: drop local-dev docker-compose tweaks from this branch
  This branch is meant to ship without the local worker cpu/triggerer
  changes from c6c79745 — those are local-environment tweaks, not part of
  this PR's scope. Revert them here so the pushed branch doesn't include them.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `8252bf2e` **ryan_at_teqplay** (2026-08-31): refactor(port-performance-analytics): move outlier-flag SQL to template files
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-28)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-31)

_No comment._

### ryan-kharisma — COMMENTED (2026-08-31)

_No comment._

### panjiyudasetya — APPROVED (2026-08-31)

Looking good to me now! 🚢

## Review Comments

### panjiyudasetya — 2026-08-31 on `teqplay/tasks/fact/sof/refresh_task_groups.py`

Is there any reason why we shouldn't put this in the SQL template?

### ryan-kharisma — 2026-08-31 on `teqplay/tasks/fact/sof/refresh_task_groups.py`

okay already addressed on this: 717e805d

## Comments

### ryan-kharisma — 2026-08-28

already tested on local env also:
<img width="1466" height="853" alt="Screenshot 2026-08-28 at 16 45 29" src="https://github.com/user-attachments/assets/d35280db-4262-4684-85ab-70a776d35aa4" />

