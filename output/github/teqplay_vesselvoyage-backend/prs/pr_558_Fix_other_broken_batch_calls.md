---
id: github:teqplay/vesselvoyage-backend:pr:558
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 558
title: Fix other broken batch calls
author: Darius-Wattimena
state: closed
date: '2025-07-07'
merged_at: '2025-07-07'
base_branch: develop
head_branch: batch-calls
url: https://github.com/teqplay/vesselvoyage-backend/pull/558
labels: []
linked_issues: []
explicit_links: []
---
# PR #558: Fix other broken batch calls

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/558  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `batch-calls`  
**Created:** 2025-07-07  
**Merged:** 2025-07-07  

## Description

Moved all existing batch calls to avoid a typing issue

## Commits

- `d3d85843` **Darius Wattimena** (2025-07-07): Moved all existing batch calls to avoid a typing issue

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-07)

## Pull Request Overview

This PR refactors batch retrieval methods to use array-based deserialization, avoiding typing issues with generic responses.

- Removed the generic `findByIds` in `BaseSubClient` and added concrete implementations in each subclient.
- Updated batch calls in `Entries`, `Visit`, and `Voyage` subclients to use `postForObject<Array<T>>(...).toList()`.
- Added KDoc comments for the new `findByIds` methods.


<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt:157**
* This method retrieves `Visit` instances but takes `List<EntryId>`. Consider using a more specific `VisitId` type (if available) to make the API clearer and prevent confusion.
```
        fun findByIds(ids: List<EntryId>): List<Visit> {
```
**client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt:94**
* New batch methods lack accompanying tests. Please add unit tests for `findByIds` in each subclient to cover typical and edge-case behaviors.
```
        fun findByIds(ids: List<EntryId>): List<Entry> {
```
</details>

### TeqJoostD — APPROVED (2025-07-07)

_No comment._

## Review Comments

### Copilot — 2025-07-07 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

The `findByIds` implementation is duplicated across three subclients. Consider moving a generic array-based batch method into `BaseSubClient` to reduce repetition.
```suggestion
        // Removed from Entries. Moved to BaseSubClient.
```
