---
id: github:teqplay/vesselvoyage-backend:pr:682
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 682
title: TCC-581 Fix EOSP leaving edge case
author: Darius-Wattimena
state: closed
date: '2025-12-09'
merged_at: '2025-12-09'
base_branch: develop
head_branch: TCC-581-eosp-leaving-edge-case
url: https://github.com/teqplay/vesselvoyage-backend/pull/682
labels: []
linked_issues: []
explicit_links: []
---
# PR #682: TCC-581 Fix EOSP leaving edge case

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/682  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-581-eosp-leaving-edge-case`  
**Created:** 2025-12-09  
**Merged:** 2025-12-09  

## Description

Similar fix like the previous PR but now focused on EOSP end events.

Fixes https://vesselvoyagedev.teqplay.nl/#/ships/1015868/story/a94fd389-75e9-4fa1-8647-925d82ac7a4d.VISIT?mode=period&months=3 where the BEGNE port ATA would be before the visit start time.

## Commits

- `198e604e` **Darius Wattimena** (2025-12-09): Fix an issue where it was still possible to have a port ata outside of the visit time
- `254ad638` **Darius Wattimena** (2025-12-09): Update existing test to match new behaviour
- `8fc0e9ca` **Darius Wattimena** (2025-12-09): Refactor port area activity time correction logic so it is reused by both components

## Reviews

### github-actions[bot] — COMMENTED (2025-12-09)

Review completed. The fix correctly addresses the EOSP leaving edge case by ensuring port activity start times are aligned with visit boundaries. The implementation is sound and the test update properly validates the expected behavior.

### michel-teqplay — DISMISSED (2025-12-09)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-09)

## Pull request overview

This PR fixes an edge case in EOSP (End of Sea Passage) end event processing where port area activities could start before their containing visit's start time. The fix ensures that when a new visit is created due to overlapping EOSPs, any port activities that started before the new visit's start time are adjusted to align with the visit boundaries.

- Adds logic to adjust port area activity start times when creating a new visit with a zero-second voyage
- Updates the corresponding test to expect the corrected port activity timing

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt` | Implements port area activity start time correction in `handleAsFinishVisitWithZeroSecondVoyage` to prevent activities from starting before the new visit start time |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt` | Updates test expectations to verify that port activities are corrected to start at the new visit start time |

### michel-teqplay — APPROVED (2025-12-09)

_No comment._

## Review Comments

### Copilot — 2025-12-09 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt`

The `matchingPortActivity` search on line 538-542 doesn't check if the activity is ongoing (has no end time), but `ongoingOtherMainPortAreaActivities` (defined on line 503-507) only contains ongoing activities. 

If a matching port activity has already ended, it won't be in `ongoingOtherMainPortAreaActivities`. The operation `ongoingOtherMainPortAreaActivities - matchingPortActivity + correctedMatchingPortActivity` would then add a finished activity to a list that should only contain ongoing activities for the new visit.

Consider adding `&& portAreaActivity.isOngoing()` to the condition on line 541 to ensure consistency with the `ongoingOtherMainPortAreaActivities` filter, or document why finished activities should be included in the new visit's port activities.
```suggestion
            portAreaActivity.areaId == portAreaId && portAreaActivity.start.time <= newVisitStart.time && portAreaActivity.isOngoing()
```
