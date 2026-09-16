---
id: github:teqplay/vesselvoyage-backend:pr:428
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 428
title: Fix overlap function
author: leonjoosse
state: closed
date: '2025-02-20'
merged_at: '2025-02-20'
base_branch: develop
head_branch: fix-startend-overlap
url: https://github.com/teqplay/vesselvoyage-backend/pull/428
labels: []
linked_issues: []
explicit_links: []
---
# PR #428: Fix overlap function

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/428  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `fix-startend-overlap`  
**Created:** 2025-02-20  
**Merged:** 2025-02-20  

## Description

Fix for the `StartEnd.overlaps(other)` util, the previous implementation did not consider an equal end to be an override, which it actually is. See the test cases for examples.

This function is used in PTO SOF for checking overlap between tugs and berth visits, and for overlap between slow moving periods & berth/anchor/lock activities.

## Commits

- `811d2df0` **leonj** (2025-02-20): Fix overlap function

## Reviews

### TeqJoostD — COMMENTED (2025-02-20)

_No comment._

### leonjoosse — COMMENTED (2025-02-20)

_No comment._

### Darius-Wattimena — APPROVED (2025-02-20)

_No comment._

## Review Comments

### TeqJoostD — 2025-02-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/startEndUtils.kt`

I think

`this.start <= other.end && other.start <= this.end`

Is enough
https://stackoverflow.com/a/325964


### leonjoosse — 2025-02-20 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/startEndUtils.kt`

It's end exclusive. But maybe I should use property checks instead of these functions :P 

