---
id: github:teqplay/dataflow_dag_core:pr:731
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 731
title: Release 1.54.1 to develop
author: panjiyudasetya
state: closed
date: '2026-08-03'
merged_at: '2026-08-03'
base_branch: develop
head_branch: hotfix/1.54.1
url: https://github.com/teqplay/dataflow_dag_core/pull/731
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2866
---
# PR #731: Release 1.54.1 to develop

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/731  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `hotfix/1.54.1`  
**Created:** 2026-08-03  
**Merged:** 2026-08-03  

## Description


## [1.54.1] - 2026-08-03
### Fixed
- Fix slow fact_bunkering query and add chunk-processing logs (#730)

## Commits

- `32ae5abd` **Panji Y. Wiwaha** (2026-07-16): Merge pull request #725 from teqplay/hotfix/1.53.1
  Release 1.53.1 to master
- `eb5eafe9` **Panji Y. Wiwaha** (2026-07-23): Merge pull request #729 from teqplay/release/1.54.0
  Release 1.54.0 to master
- `f731fef4` **Panji Y. Wiwaha** (2026-07-24): fix(fact-bunkering): fix slow fact_bunkering query and add chunk-processing logs
  The proceed.sql query missing deleted_timestamp IS null on the ods_encounter,
  ods_berth_visit, and ods_terminal_visit joins prevented Postgres from using
  the partial indexes built for these lookups, forcing full sequential scans
  (EXPLAIN ANALYZE showed ~27s spent scanning ~1.3M+ rows for a 459-row result).
  Applied the same fix to the QC accuracy template that reconstructs the same
  data, so both stay consistent.
  
  Also added logging around process_data_in_chunks to make the executed query,
  total available records, and chunk progress visible when diagnosing stalled
  DAG runs.
- `9ce98df9` **Panji Y. Wiwaha** (2026-07-24): Merge pull request #730 from teqplay/fix/fact-bunkering
  PTO-2866 Fix slow `fact_bunkering` query and add chunk-processing logs
- `8b475352` **Panji Y. Wiwaha** (2026-08-03): Bump version 1.54.1

## Reviews

### ryan-kharisma — APPROVED (2026-08-03)

LGTM

### augmentcode[bot] — COMMENTED (2026-08-03)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments
