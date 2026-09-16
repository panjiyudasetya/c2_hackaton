---
id: github:teqplay/vesselvoyage-backend:pr:676
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 676
title: TCC-504 fix activities before visit
author: Darius-Wattimena
state: closed
date: '2025-12-04'
merged_at: '2025-12-08'
base_branch: develop
head_branch: TCC-504-fix-activities-before-visit
url: https://github.com/teqplay/vesselvoyage-backend/pull/676
labels: []
linked_issues: []
explicit_links: []
---
# PR #676: TCC-504 fix activities before visit

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/676  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-504-fix-activities-before-visit`  
**Created:** 2025-12-04  
**Merged:** 2025-12-08  

## Description

_No description._

## Commits

- `b6c3ea93` **Darius Wattimena** (2025-11-07): Attempt to fix swap time making a lot of visits corrupted
- `61e66714` **Darius Wattimena** (2025-11-12): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `bf270d46` **Darius Wattimena** (2025-11-13): Fix an issue where the stops wouldn't be added to the poma entities to load in for the story page in the frontend
- `add4d832` **Darius Wattimena** (2025-11-13): Fix an issue where it is possible to have activities that are not part of the visit after potentially moving the start time of the new visit in the future
- `34dc8b6f` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `61a26dec` **Darius Wattimena** (2025-12-04): Add additional test case for testing the usecase where we split the visit when we confirm a different other ongoing EOSP
- `bfc0fa50` **Darius Wattimena** (2025-12-04): Fixed issues where not all previous voyages updates would trigger a post-processing calculation
- `17b74518` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `bb0b7845` **Darius Wattimena** (2025-12-04): Fix an issue where splitting of a visit would have different results in status and changes list
- `72da5db9` **Darius Wattimena** (2025-12-04): Cleanup
- `e78b71aa` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `9f535f7e` **Darius Wattimena** (2025-12-04): Apply suggestions from code review
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `4ccbc7e5` **Darius Wattimena** (2025-12-04): Remove fixed TODO
- `d8ee09d2` **Darius Wattimena** (2025-12-04): Merge remote-tracking branch 'origin/TCC-504-fix-activities-before-visit' into TCC-504-fix-activities-before-visit
- `8c7c2533` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `d8722e97` **Darius Wattimena** (2025-12-08): Added documentation for EOSP en Stop processors

## Reviews

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The changes implement a comprehensive solution for properly handling activity splitting when visits are replaced or restructured. The new `splitVisitActivities` function provides a clean abstraction for this complex logic, and the test updates demonstrate the expected behavior changes.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-04)

## Pull request overview

This PR fixes an issue where activities that started before a visit's start time were incorrectly being kept on the visit instead of being moved to the previous voyage. The fix introduces a new `splitVisitActivities` utility function that properly partitions activities based on a split time, ensuring that only activities that could have occurred during a visit remain associated with it.

**Key Changes:**
- Introduced `splitVisitActivities` function to partition visit/voyage activities based on a split time
- Updated visit confirmation and port switching logic to use activity splitting 
- Added filtering to only consider ongoing port activities when checking for visit swaps

### Reviewed changes

Copilot reviewed 8 out of 8 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt` | Added `splitVisitActivities` function to split activities between visit and voyage based on timestamp |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt` | Integrated `splitVisitActivities` into visit confirmation logic to properly handle activity splitting |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt` | Added filtering for ongoing port activities and improved swap time calculation for overlapping ports |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt` | Integrated `splitVisitActivities` when replacing visits with other main ports |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt` | Added stops to voyage POMA entities to ensure stops are included in voyage stories |
| `src/test/kotlin/nl/teqplay/vesselvoyage/util/TestUtil.kt` | Added `pilotAreaActivities` parameter to `createNewVisit` test utility |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt` | Added comprehensive test case for visit switching with activity splitting; removed unused import |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingScenarioTest.kt` | Updated expected test results to reflect activities correctly moved to previous voyage |
</details>

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The implementation looks solid with proper activity splitting logic and comprehensive test coverage. The changes correctly address the issue of activities occurring before visit start times.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The implementation looks solid with proper activity splitting logic and comprehensive test coverage.

### github-actions[bot] — COMMENTED (2025-12-04)

Review completed. The implementation looks solid with proper activity splitting logic and comprehensive test coverage. No suggestions at this time.

### github-actions[bot] — COMMENTED (2025-12-08)

Review completed. The implementation looks solid with good handling of edge cases and proper activity management. The new utility functions provide clean abstractions for common operations.

### github-actions[bot] — COMMENTED (2025-12-08)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-08)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-08)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-08)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-08)

_No comment._

### TeqJoostD — APPROVED (2025-12-08)

_No comment._

## Review Comments

### Copilot — 2025-12-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

The `decision` field is missing from the `NewEventProcessingResult`. Other methods in this file (e.g., lines 241, 422, 463, 493, 582, 608, 652, 689) and similar changes in `StopBaseProcessor.kt` include decision strings for debugging purposes. Consider adding a decision string here to maintain consistency and aid in debugging, such as:
```kotlin
decision = "Replacing visit because of main port switch. Activities before ${correctedStart.time} moved to previous voyage."
```
```suggestion
            readyForPostProcessing = updatedPreviousVoyage?.let { listOf(updatedPreviousVoyage._id) } ?: emptyList(),
            decision = "Replacing visit because of main port switch. Activities before ${correctedStart.time} moved to previous voyage."
```

### Copilot — 2025-12-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

Typo in documentation: "contained" should be "contains" (present tense for consistency with "only contains" in the second part of the sentence).
```suggestion
 * @return A pair of [EntryESoFWrapper] containing the updated Voyage that now contains the old activities and the updated Visit which only contains activities that could've happened during the visit.
```

### Copilot — 2025-12-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

Typo in comment: "activites" should be "activities".
```suggestion
    // Split all activities based on the new visit
```

### Copilot — 2025-12-04 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt`

Typo in comment: "maintined" should be "maintained".
```suggestion
        // Activities that will be maintained after splitting
```

## Comments

### TeqJoostD — 2025-12-05

Could have a little more documentation. And maybe provide a description instead of fix. OTHERWISE LGTM!!!!!!!!
