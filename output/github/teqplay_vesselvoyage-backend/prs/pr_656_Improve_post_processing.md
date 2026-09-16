---
id: github:teqplay/vesselvoyage-backend:pr:656
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 656
title: Improve post processing
author: Darius-Wattimena
state: closed
date: '2025-10-30'
merged_at: '2025-10-31'
base_branch: develop
head_branch: improve-post-processing
url: https://github.com/teqplay/vesselvoyage-backend/pull/656
labels: []
linked_issues: []
explicit_links: []
---
# PR #656: Improve post processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/656  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `improve-post-processing`  
**Created:** 2025-10-30  
**Merged:** 2025-10-31  

## Description

_No description._

## Commits

- `fdbb557b` **Darius Wattimena** (2025-10-27): Remove locking from post-processing
- `14c7d690` **Darius Wattimena** (2025-10-27): Remove unused locking service
- `8809a8ac` **Darius Wattimena** (2025-10-30): Added some testing for post-processing service
- `d4f03e79` **Darius Wattimena** (2025-10-30): Added a bunch of more tests for possible usecases

## Reviews

### TeqJoostD — DISMISSED (2025-10-30)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-30)

## Pull Request Overview

This PR removes the IMO-based locking mechanism (`ImoLockService`) from the post-processing workflow. The change simplifies the code by removing the lock wrapper around the post-processing logic.

- Removed `ImoLockService` dependency from `PostProcessingService` constructor
- Removed `executeBlocking` lock wrapper from `runPostProcessingTasks` method  
- Unindented all code that was previously wrapped in the lock block


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt:132**
* The comment 'Shuffle entries to prevent locking mechanism' is now misleading since the locking mechanism has been removed. This comment should be updated or removed to accurately reflect the current implementation.
```
            // Shuffle entries to prevent locking mechanism
```
</details>

### TeqJoostD — APPROVED (2025-10-31)

_No comment._

## Review Comments

### Copilot — 2025-10-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

Removing the IMO lock introduces a potential race condition. Multiple threads can now concurrently process different entries for the same IMO, leading to a read-modify-write race on the ship status. Thread A could read the status, then Thread B reads the same status, and both update it based on stale data. This violates the atomicity that the lock previously guaranteed. Consider reintroducing synchronization for status updates or implementing optimistic locking at the database level.
