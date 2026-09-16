---
id: github:teqplay/vesselvoyage-backend:pr:818
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 818
title: Name partial port indexes to stop startup index drop/rebuild churn
author: TeqJoostD
state: closed
date: '2026-07-14'
merged_at: null
base_branch: develop
head_branch: fix/partial-index-name-conflict
url: https://github.com/teqplay/vesselvoyage-backend/pull/818
labels: []
linked_issues: []
explicit_links: []
---
# PR #818: Name partial port indexes to stop startup index drop/rebuild churn

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/818  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `fix/partial-index-name-conflict`  
**Created:** 2026-07-14  

## Description

## Problem

Dev logs show recalculation runs failing with:

```
MongoQueryException: Command failed with error 175 (QueryPlanKilled): '... query plan killed :: index 'destinationPort_1_start.time_1' for collection 'vesselvoyage.voyageV2Normalized' dropped'
```

## Cause

#812 (e4d551e3) added partial `end == null` indexes on `originPort + start.time` and `destinationPort + start.time` to `voyageV2Normalized`. These share their key pattern with the pre-existing non-partial indexes, so both resolve to the same default (key-derived) index name, e.g. `destinationPort_1_start.time_1`.

The skeleton's `ensureIndex` handles a create conflict by dropping the existing index and recreating it. So on every startup:

1. the non-partial `ensureIndex` finds the partial variant under that name → drop → rebuild as non-partial
2. the partial `ensureIndex` finds the non-partial variant → drop → rebuild as partial

Each drop kills in-flight query plans on the collection (the QueryPlanKilled errors above, which abort the revents merge scenario), the collection gets two full index rebuilds per startup, and only one of the two index variants ever exists at a time — so either the ONGOING port queries or the general port queries are always unindexed.

`visitV2Normalized` is not affected: its partial index has a different key set than the non-partial one, so the default names don't collide.

## Fix

Give the partial indexes explicit names (`..._ongoing`) so they can coexist with the non-partial ones and `ensureIndex` becomes idempotent again.

On first deploy there will be one final conflict-driven rebuild (the currently stored index under the default name is whichever variant won last), after which both indexes exist and restarts are no-ops.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `4edd6c8c` **TeqJoostD** (2026-07-14): Name partial port indexes to stop startup index drop/rebuild churn
  The partial (end == null) originPort/destinationPort indexes share their
  key pattern with the non-partial ones, so both resolve to the same
  default index name. On every startup ensureIndex hit an
  IndexOptionsConflict and fell back to drop-and-recreate, dropping
  'destinationPort_1_start.time_1' (and the originPort equivalent) while
  queries were running. This surfaced as QueryPlanKilled (error 175)
  failures in ReventsRecalculationService and left the port indexes in a
  permanent rebuild loop, with only one of the two variants existing at a
  time.
  
  Giving the partial indexes explicit names lets them coexist with the
  non-partial ones, making ensureIndex idempotent again.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-14)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments
