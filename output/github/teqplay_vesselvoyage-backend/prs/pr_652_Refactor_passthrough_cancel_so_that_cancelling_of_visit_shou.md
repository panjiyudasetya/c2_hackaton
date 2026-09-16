---
id: github:teqplay/vesselvoyage-backend:pr:652
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 652
title: Refactor passthrough cancel so that cancelling of visit should not happen when
  ship to ship transfer is present
author: TeqJoostD
state: closed
date: '2025-10-27'
merged_at: '2025-10-28'
base_branch: develop
head_branch: sts-passthrough-fix
url: https://github.com/teqplay/vesselvoyage-backend/pull/652
labels: []
linked_issues: []
explicit_links: []
---
# PR #652: Refactor passthrough cancel so that cancelling of visit should not happen when ship to ship transfer is present

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/652  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `sts-passthrough-fix`  
**Created:** 2025-10-27  
**Merged:** 2025-10-28  

## Description

_No description._

## Commits

- `423e33db` **TeqJoostD** (2025-10-27): Refactor passthrough cancel so that cancelling of visit should not happen when ship to ship transfer is present

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-27)

## Pull Request Overview

This PR refactors the passthrough cancellation logic to prevent visit cancellation when a ship-to-ship transfer is present during an End of Sea Passage (EOSP) event. The core change modifies the `isPassThrough()` function to check for both stops and ship-to-ship transfers when determining if a visit qualifies as a passthrough.

Key changes:
- Modified `isPassThrough()` to check both `stops` and `shipToShipTransfers` instead of only `stops`
- Changed the signature of `isPassThrough()` to operate on `NewVisitShipStatus` instead of `NewVisit` to access ESoF data
- Added test infrastructure to support ship-to-ship transfer scenarios in test cases

### Reviewed Changes

Copilot reviewed 5 out of 5 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| EntriesBuilder.kt | Added `ShipToShipTransferBuilder` class and integrated it into the test DSL for building ship-to-ship transfer scenarios |
| EventProcessingScenarioTest.kt | Added comprehensive test case verifying that visits with ship-to-ship transfers are not treated as passthroughs |
| helperFunctions.kt | Updated helper functions to accept optional `location` parameter for more flexible test setup |
| entryUtils.kt | Refactored `isPassThrough()` to check both stops and ship-to-ship transfers, changing its signature to accept `NewVisitShipStatus` |
| EndOfSeaPassageEndProcessor.kt | Updated call site to use `status.isPassThrough()` instead of `currentVisit.isPassThrough()` |
</details>

### TeqJoostD — COMMENTED (2025-10-27)

_No comment._

### Darius-Wattimena — APPROVED (2025-10-28)

_No comment._

## Review Comments

### Copilot — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

The null-safe operator with `?: true` makes the condition return `true` when `esof` is null. This means a visit with no ESoF data would be considered a passthrough, which may not align with the intent. Consider using `!= false` pattern or explicitly checking for null to make the logic clearer: `(this.visit.esof?.shipToShipTransfers?.isEmpty() != false)`
```suggestion
    // Returns true only if stops are empty and shipToShipTransfers is present and empty.
    return this.visit.entry.stops.isEmpty() &&
        (this.visit.esof?.shipToShipTransfers?.isEmpty() == true)
```

### TeqJoostD — 2025-10-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

esof == null means no ship to ship transfer noob
