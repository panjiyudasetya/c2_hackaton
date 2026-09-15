---
id: github:teqplay/vesselvoyage-backend:pr:846
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 846
title: Hotfix release 6 Aug 2026
author: Darius-Wattimena
state: closed
date: '2026-08-06'
merged_at: '2026-08-06'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/846
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1158
---
# PR #846: Hotfix release 6 Aug 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/846  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-08-06  
**Merged:** 2026-08-06  

## Description

_No description._

## Commits

- `6e915833` **Darius Wattimena** (2026-08-06): TCC-1158 Upsert instead of insert new normalized documents
  A recalculation (repair story / full story recreate) regenerates the
  same deterministic document ids (e.g. "{entryId}:{startEventId}" for
  encounters). When a leftover document from an earlier partial write or
  failed cleanup is still present, the diff-based save built an
  InsertOneModel for it, failing the whole entry with an E11000 duplicate
  key error.
  
  Writing new documents as upserting replaces instead makes the write
  idempotent: a stale leftover is simply overwritten with the freshly
  calculated version, so recalculations self-heal instead of getting
  stuck. This covers all normalized child collections (encounters, slow
  moving periods, STS transfers, area activities and stops) since they
  share buildDiffWriteModels.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `880c69cc` **Darius Wattimena** (2026-08-06): Merge pull request #845 from teqplay/TCC-1158
  TCC-1158 Upsert instead of insert new normalized documents

## Reviews

### TeqJoostD — APPROVED (2026-08-06)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-06)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments
