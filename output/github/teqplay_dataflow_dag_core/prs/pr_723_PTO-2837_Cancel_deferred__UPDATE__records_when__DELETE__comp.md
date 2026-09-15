---
id: github:teqplay/dataflow_dag_core:pr:723
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 723
title: PTO-2837 Cancel deferred `UPDATE` records when `DELETE` completes for the same
  `entry_id`
author: panjiyudasetya
state: closed
date: '2026-07-16'
merged_at: '2026-07-16'
base_branch: master
head_branch: fix/orphan-deferred-records
url: https://github.com/teqplay/dataflow_dag_core/pull/723
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2837
---
# PR #723: PTO-2837 Cancel deferred `UPDATE` records when `DELETE` completes for the same `entry_id`

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/723  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `fix/orphan-deferred-records`  
**Created:** 2026-07-16  
**Merged:** 2026-07-16  

## Description

### Description
When a visit was marked as `DEFERRED` due to missing metadata, and that visit was subsequently deleted before the metadata was resolved, the `DEFERRED` record was never cancelled. It remained in the processing queue indefinitely and was picked up by the recovery DAG on every run without making any progress.

### What changed
`sof_mark_stale_updates.sql` previously only cancelled `PENDING UPDATE` records when a `DELETE` completed for the same `entry_id`. The state filter has been extended to also include `DEFERRED`, so stale deferred records are now correctly cancelled alongside pending ones.

The existing timestamp guard (`upd.updated_at < del.updated_at`) is unchanged, it continues to ensure that `UPDATE` records arriving after the `DELETE` (i.e. legitimate restore-after-delete events) are preserved.

### How to test
1. Create a visit that gets marked `DEFERRED` due to missing metadata.
2. Delete that visit before resolving the missing metadata.
3. Verify the `DEFERRED` record in `sof_processing_queue` transitions to `CANCELLED` after the `DELETE` completes.
4. Verify the recovery DAG no longer picks up that record on subsequent runs.

### One-time cleanup query (run when the patch is deployed)
Run the following to cancel existing orphaned records:
```sql
UPDATE sof_processing_queue AS pq
SET
    state        = 'CANCELLED'
    , note       = 'Stale: staging data hard-deleted by a subsequent DELETE event'
    , cancelled_at = now()
WHERE
    pq.action_type = 'UPDATE'
    AND pq.state   = 'DEFERRED'
    AND NOT EXISTS (
        SELECT 1 FROM stg_statement_of_fact AS sof
        WHERE sof.entry_id = pq.entry_id
    );
```

## Commits

- `491f530d` **Panji Y. Wiwaha** (2026-07-16): fix(sof): cancel DEFERRED UPDATE records when DELETE completes for the same entry_id
  DEFERRED UPDATE rows were not included in the stale-update cancellation check,
  leaving them in the queue indefinitely after their staging data was hard-deleted
  by a subsequent DELETE event.
- `a1c19bb6` **Panji Y. Wiwaha** (2026-07-16): docs(sof): update sof_mark_stale_updates comments to reflect PENDING/DEFERRED cancellation
- `03e5a1de` **Panji Y. Wiwaha** (2026-07-16): remove(helm): remove outdated Helm config and values files
- `9c78e1d4` **Panji Y. Wiwaha** (2026-07-16): remove(docs): remove irrelevant and outdated documentation files
- `06c60894` **Panji Y. Wiwaha** (2026-07-16): refactor(docs): reorganize KPI and monitoring docs into structured subdirectories
- `8340ac67` **Panji Y. Wiwaha** (2026-07-16): add(scripts): add visit ID reconciliation scripts
- `43ded44c` **Panji Y. Wiwaha** (2026-07-16): fix(ga): sqlfluff linter checks

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-16)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F723%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-07-16)

_No comment._

### ryan-kharisma — APPROVED (2026-07-16)

LGTM

## Review Comments

### panjiyudasetya — 2026-07-16 on `teqplay/templates/sql/dml/processing_queue/sof_mark_stale_updates.sql`

Resolved by a1c19bb
