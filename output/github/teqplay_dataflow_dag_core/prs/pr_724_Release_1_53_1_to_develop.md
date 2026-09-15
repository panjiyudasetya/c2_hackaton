---
id: github:teqplay/dataflow_dag_core:pr:724
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 724
title: Release 1.53.1 to develop
author: panjiyudasetya
state: closed
date: '2026-07-16'
merged_at: '2026-07-16'
base_branch: develop
head_branch: hotfix/1.53.1
url: https://github.com/teqplay/dataflow_dag_core/pull/724
labels: []
linked_issues: []
explicit_links: []
---
# PR #724: Release 1.53.1 to develop

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/724  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `hotfix/1.53.1`  
**Created:** 2026-07-16  
**Merged:** 2026-07-16  

## Description


## [1.53.1] - 2026-07-16
### Fixed
- Cancel deferred `UPDATE` records when `DELETE` completes for the same `entry_id` (#723) 

## Commits

- `6c39d407` **Panji Y. Wiwaha** (2026-07-02): Merge pull request #719 from teqplay/hotfix/1.52.1
  Release 1.52.1 to master
- `696d1b6f` **Panji Y. Wiwaha** (2026-07-10): Merge pull request #722 from teqplay/release/1.53.0
  Release 1.53.0 to master
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
- `c18480d6` **Panji Y. Wiwaha** (2026-07-16): Merge pull request #723 from teqplay/fix/orphan-deferred-records
  PTO-2837 Cancel deferred `UPDATE` records when `DELETE` completes for the same `entry_id`
- `7e10ec72` **Panji Y. Wiwaha** (2026-07-16): Bump version 1.53.1

## Reviews

### ryan-kharisma — APPROVED (2026-07-16)

LGTM

### augmentcode[bot] — COMMENTED (2026-07-16)

Review completed. 5 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F724%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments
