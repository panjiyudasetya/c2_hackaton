---
id: github:teqplay/vesselvoyage-backend:pr:680
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 680
title: TCC-581 fix missing port ata
author: Darius-Wattimena
state: closed
date: '2025-12-09'
merged_at: '2025-12-09'
base_branch: develop
head_branch: TCC-581-fix-special-case
url: https://github.com/teqplay/vesselvoyage-backend/pull/680
labels: []
linked_issues: []
explicit_links: []
---
# PR #680: TCC-581 fix missing port ata

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/680  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-581-fix-special-case`  
**Created:** 2025-12-09  
**Merged:** 2025-12-09  

## Description

_No description._

## Commits

- `8ca94b91` **Darius Wattimena** (2025-12-09): Fix an issue where the port area activity would be filtered out in waters where a lot of EOSPs overlap
- `9e9d51ec` **Darius Wattimena** (2025-12-09): ktlint
- `a9904789` **Darius Wattimena** (2025-12-09): Fix so we don't put the Port ATA to an older time when we entered the port after the EOSP ATA
- `e5c0e270` **Darius Wattimena** (2025-12-09): Add test for updating port area activity start time on new confirmed visit
- `ed2b94bc` **Darius Wattimena** (2025-12-09): Cleaned up code and added some better comments why the changes need to be made
- `708d9574` **Darius Wattimena** (2025-12-09): Clarify comment on port activity time adjustment logic for overlapping EOSPs

## Reviews

### github-actions[bot] — COMMENTED (2025-12-09)

Review completed. The fix correctly addresses the port area activity filtering issue in overlapping EOSP scenarios. The test coverage validates the fix and the code changes are well-documented.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-09)

## Pull request overview

This PR fixes a special case (TCC-581) where port area activities need to have their start time updated when switching to a new confirmed visit during overlapping EOSP scenarios. The fix ensures that when a vessel's visit is switched to a different port, any matching port area activities that started before the new visit's start time are aligned with the new visit start time.

- Adds logic to update port area activity start times when switching visits
- Includes comprehensive test coverage for the new behavior

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt | Implements logic to find and update matching port area activities when switching to a new confirmed visit, ensuring start times are aligned with the new visit start time |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt | Adds test case validating that port area activities are correctly updated when switching to a new confirmed visit |

### michel-teqplay — DISMISSED (2025-12-09)

_No comment._

### michel-teqplay — APPROVED (2025-12-09)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-09)

Review completed. The changes look good - the fix properly handles the edge case where port activities might start after the new visit start time, preventing incorrect time adjustments. The added test coverage validates the fix effectively.

## Review Comments

### Copilot — 2025-12-09 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt`

The comment on line 167 is incomplete. It ends mid-sentence with "which" but doesn't finish the thought. This should be completed to explain what would happen if we moved the matching port activity to a later time.
```suggestion
                    // Otherwise we'd be moving the matching port activity to a later time, which could result in an incorrect visit record by making it appear that the vessel entered the port later than it actually did. This may cause logical inconsistencies in visit tracking and reporting.
```

### Copilot — 2025-12-09 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt`

The null check for `updatedPortActivity` at line 179 is redundant. Since `updatedPortActivity` is created by calling `.copy(start = newVisitStart)` on `matchingPortActivity` at line 170, it will be null if and only if `matchingPortActivity` is null. The condition can be simplified to just check `matchingPortActivity != null`.
```suggestion
                    portAreaActivities = if (matchingPortActivity != null) {
```
