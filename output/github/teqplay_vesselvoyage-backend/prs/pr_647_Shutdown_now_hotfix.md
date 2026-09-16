---
id: github:teqplay/vesselvoyage-backend:pr:647
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 647
title: Shutdown now hotfix
author: TeqJoostD
state: closed
date: '2025-10-21'
merged_at: null
base_branch: develop
head_branch: shutdownNow-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/647
labels: []
linked_issues: []
explicit_links: []
---
# PR #647: Shutdown now hotfix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/647  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `shutdownNow-hotfix`  
**Created:** 2025-10-21  

## Description

_No description._

## Commits

- `acdb3658` **TeqJoostD** (2025-10-21): fix: replace shutdownNow with cooperative shutdown in AisStreamingMessageHandler
- `8f62f3f4` **Joost Dambrink** (2025-10-21): Merge branch 'develop' into shutdownNow-hotfix

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-21)

## Pull Request Overview

This PR implements a hotfix to address shutdown-related issues in the AIS streaming message handler by replacing the aggressive `shutdownNow()` approach with a graceful shutdown mechanism. Additionally, it introduces a temporary `filterMultipleOngoing` parameter to various API endpoints and increases the post-processing batch size.

Key changes:
- Refactored the AIS message handler shutdown process to use graceful termination with polling and timeout-based blocking instead of thread interruption
- Added a `filterMultipleOngoing` parameter to voyage and visit API endpoints (marked as temporary with TODO for removal)
- Increased post-processing batch size from 1000 to 5000 and added shuffling to prevent lock contention

### Reviewed Changes

Copilot reviewed 7 out of 7 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `AisStreamingMessageHandler.kt` | Implements graceful shutdown mechanism using `AtomicBoolean` flag and polling-based worker loop instead of thread interruption |
| `PostProcessingService.kt` | Increases batch size constant and adds shuffling to prevent locking issues |
| `ApiVoyageV2Controller.kt` | Adds `filterMultipleOngoing` parameter to the voyage endpoint with default value |
| `ApiVisitV2Controller.kt` | Adds `filterMultipleOngoing` parameter to the visit endpoint with default value |
| `VesselVoyageClient.kt` | Adds `filterMultipleOngoing` parameter to client methods and fixes query parameter name typo |
| `VoyagesByPortRequest.kt` | Adds `filterMultipleOngoing` property to request data classes with documentation noting it's a hotfix |
| `VisitByPortRequest.kt` | Adds `filterMultipleOngoing` property to request data class with TODO for removal |
</details>

### michel-teqplay — CHANGES_REQUESTED (2025-10-21)

_No comment._

## Review Comments

### Copilot — 2025-10-21 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VoyagesByPortRequest.kt`

This documentation states 'not sure what this does since no documentation', which is unhelpful for future maintainers. Even for a temporary hotfix, the comment should explain the intended behavior or impact of this field. Consider documenting what 'filtering multiple ongoing entries' means in the context of voyages.
```suggestion
     * When true, filters out voyages where a ship has multiple ongoing entries (i.e., voyages that have not been marked as finished).
     * This is a hotfix for certain endpoints to prevent duplicate or overlapping ongoing voyage records for the same ship.
     * If false, all ongoing voyages are included, even if there are multiple per ship.
     * TODO(TCC-498): Please remove ASAP and refactor. If you modify voyage filtering logic, review the impact of this field.
```

### Copilot — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The comment 'Shuffle entries to prevent locking mechanism' is unclear. It should explain what locking mechanism is being prevented and how shuffling achieves this. Consider clarifying whether this prevents database locks, application-level locks, or deadlocks.
```suggestion
            // Shuffle entries to reduce the risk of database row locks and deadlocks.
            // By processing entries in a random order, we avoid repeatedly accessing the same rows in the same sequence,
            // which can lead to contention and locking issues in concurrent batch processing.
```

### michel-teqplay — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

This does not need to be an `AtomicBoolean`, a normal `Boolean` marked as `@Volatile` should do the trick.

### michel-teqplay — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

What is the effect of this, are we just dropping/discarding data here? To unblock blocking read operations, a poison pill works much better.

### michel-teqplay — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

This is going to be an issue I believe. The `shutdown` code is also called in the situation where we're not seeing ais messages coming in, to force a reconnect. If we do this, and then reconnect, none of the mongo calls are going to work, because the application is interrupted. At least, that would be my suspicion. If we take ths approach, we need to find a way to test the reconnect scenario.

### michel-teqplay — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Again, using a poison pill prevents having to wait for the timeout :)
