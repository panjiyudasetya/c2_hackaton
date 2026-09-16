---
id: github:teqplay/vesselvoyage-backend:pr:557
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 557
title: Fix batch call of traces breaking
author: Darius-Wattimena
state: closed
date: '2025-07-07'
merged_at: '2025-07-07'
base_branch: develop
head_branch: fix-batch-trace-call
url: https://github.com/teqplay/vesselvoyage-backend/pull/557
labels: []
linked_issues: []
explicit_links: []
---
# PR #557: Fix batch call of traces breaking

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/557  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-batch-trace-call`  
**Created:** 2025-07-07  
**Merged:** 2025-07-07  

## Description

_No description._

## Commits

- `fdd2330b` **Darius Wattimena** (2025-07-07): Fix batch call of traces breaking

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-07)

## Pull Request Overview

This PR fixes a batch trace retrieval method that was breaking by adjusting how the REST template deserializes and returns the trace list.

- Changed the generic type of `postForObjectWithParams` from `List<Trace>` to `Array<Trace>` and converted it to a Kotlin `List` via `.toList()`.
- Ensures the function signature still returns `List<Trace>` while matching the underlying HTTP response structure.

### TeqJoostD — APPROVED (2025-07-07)

_No comment._

## Review Comments

### Copilot — 2025-07-07 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

Add or update unit tests to cover the new array-to-list conversion in this batch trace call, including cases for non-null, null, and empty responses to ensure the fix works under all scenarios.
