---
id: github:teqplay/dataflow_dag_core:pr:730
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 730
title: PTO-2866 Fix slow `fact_bunkering` query and add chunk-processing logs
author: panjiyudasetya
state: closed
date: '2026-07-24'
merged_at: '2026-07-24'
base_branch: master
head_branch: fix/fact-bunkering
url: https://github.com/teqplay/dataflow_dag_core/pull/730
labels: []
linked_issues: []
explicit_links: []
---
# PR #730: PTO-2866 Fix slow `fact_bunkering` query and add chunk-processing logs

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/730  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `fix/fact-bunkering`  
**Created:** 2026-07-24  
**Merged:** 2026-07-24  

## Description

### Summary
- `proceed.sql` (the query populating fact_bunkering) was missing `deleted_timestamp IS null` on the `ods_encounter`, `ods_berth_visit`, and `ods_terminal_visit` joins. Those tables have partial indexes (`idx_encounter_bunkering`, `idx_berth_visit_overlap`, `idx_terminal_visit_overlap`) built specifically with that predicate. Without it in the query, Postgres couldn't prove the index applied and fell back to full sequential scans. EXPLAIN ANALYZE showed ~27s spent scanning ~1.3M+ rows across those three tables to return a 459-row result. Adding the predicate (matching what fdw_proceed.sql already does) lets the planner use the existing indexes instead.
- Applied the identical fix to `bunkering_components.sql` under `quality_control/accuracy/bunkering/`, which reconstructs the same `fact_bunkering` shape from ODS tables for accuracy validation. Keeping it in sync avoids the QC query silently diverging from the fact-table logic it's checking against (or being slow for the same reason).
- Added logging in `process_data_in_chunks` (`teqplay/tasks/fact/sof/utils.py`) so DAG logs now show the executed query, plus a checkpoint after `cursor.execute()` returns. This was what let us pinpoint that a previous "stuck" run was actually a slow query stalled inside the first `fetchmany()`, not a hang on the mart insert.

### Test plan
- [ ] Re-run the fact_sof__barge DAG's load_fact_bunkering task and confirm chunk-processing logs show the new query/count/progress lines.
- [ ]  EXPLAIN ANALYZE the updated proceed.sql query and confirm it now uses `idx_encounter_bunkering` / `idx_berth_visit_overlap` / `idx_terminal_visit_overlap` (index scans, not seq scans).
- [ ]  Run the QC accuracy check for bunkering and confirm results are unchanged (aside from the performance improvement).

## Commits

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

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-24)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F730%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-07-24)

_No comment._

### ryan-kharisma — APPROVED (2026-07-24)

LGTM

## Review Comments

### panjiyudasetya — 2026-07-24 on `teqplay/tasks/fact/sof/utils.py`

updated pr description.

## Comments

### panjiyudasetya — 2026-07-24

I tested it locally by running Airflow against the production database (ESALG, Jun 1 - Jul 1, 2026). At this point, I no longer see any "stuck" bunkering fact processing, @ryan-kharisma.

<img width="1624" height="1000" alt="image" src="https://github.com/user-attachments/assets/bc9ab418-02e1-4abb-8967-276b9535df53" />

