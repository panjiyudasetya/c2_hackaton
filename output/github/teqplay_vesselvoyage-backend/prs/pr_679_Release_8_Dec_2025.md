---
id: github:teqplay/vesselvoyage-backend:pr:679
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 679
title: Release 8 Dec 2025
author: Darius-Wattimena
state: closed
date: '2025-12-08'
merged_at: '2025-12-08'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/679
labels: []
linked_issues: []
explicit_links: []
---
# PR #679: Release 8 Dec 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/679  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-12-08  
**Merged:** 2025-12-08  

## Description

_No description._

## Commits

- `b6c3ea93` **Darius Wattimena** (2025-11-07): Attempt to fix swap time making a lot of visits corrupted
- `61e66714` **Darius Wattimena** (2025-11-12): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `bf270d46` **Darius Wattimena** (2025-11-13): Fix an issue where the stops wouldn't be added to the poma entities to load in for the story page in the frontend
- `add4d832` **Darius Wattimena** (2025-11-13): Fix an issue where it is possible to have activities that are not part of the visit after potentially moving the start time of the new visit in the future
- `0587a847` **Darius Wattimena** (2025-11-24): Update skeleton version to 2.10.0 and add NATS dependency
- `5b228b67` **Darius Wattimena** (2025-11-24): Fix NATS consumer timeout by adding drain duration so it doesn't get stuck indefinitely
- `933736a6` **Darius Wattimena** (2025-11-27): Merge branch 'develop' into TCC-530-nats-timeout-fix
- `1359af7a` **Darius Wattimena** (2025-12-01): Merge pull request #673 from teqplay/TCC-530-nats-timeout-fix
  TCC-530 nats timeout fix
- `84e91d3c` **Darius Wattimena** (2025-12-01): Up ETA predictor models to latest develop release
- `ed8dcbc8` **Darius Wattimena** (2025-12-01): Extend internal esof model to include a new field for port ETDs
- `4e1239b1` **Darius Wattimena** (2025-12-01): Rework eta processor to not make use of any generics and adjust logic to also process ETD predictions
- `bcfa133f` **Darius Wattimena** (2025-12-02): Enhance TrueDestinationEtaProcessor to handle broken predictions and improve validation logic for ETA and ETD
- `a9239c5c` **Darius Wattimena** (2025-12-02): Add test for port visit segment without arrival time in TrueDestinationEtaProcessor
- `9792e998` **Darius Wattimena** (2025-12-03): Adjusted existing tests and added tests to make sure ETD processing works as expected
- `f07fe6fa` **Darius Wattimena** (2025-12-03): Align ETD processing with expectations
- `2960c0dc` **Darius Wattimena** (2025-12-03): Refactor status update logic in TrueDestinationEtaProcessor for clarity
- `ba851d07` **Darius Wattimena** (2025-12-04): ktlint
- `d54ef707` **Darius Wattimena** (2025-12-04): Add tests to validate ETD population in JourneyService for various scenarios
- `4adf82f3` **Darius Wattimena** (2025-12-04): Implement ETD support in JourneyService
- `34dc8b6f` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `61a26dec` **Darius Wattimena** (2025-12-04): Add additional test case for testing the usecase where we split the visit when we confirm a different other ongoing EOSP
- `bfc0fa50` **Darius Wattimena** (2025-12-04): Fixed issues where not all previous voyages updates would trigger a post-processing calculation
- `5a77b308` **Darius Wattimena** (2025-12-04): Merge pull request #674 from teqplay/TCC-458-etd-predictions
  TCC-458 etd predictions
- `17b74518` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `bb0b7845` **Darius Wattimena** (2025-12-04): Fix an issue where splitting of a visit would have different results in status and changes list
- `3df118ae` **Darius Wattimena** (2025-12-04): Merge pull request #675 from teqplay/TCC-458-expose-etd
  TCC-458 expose etd
- `72da5db9` **Darius Wattimena** (2025-12-04): Cleanup
- `e78b71aa` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `9f535f7e` **Darius Wattimena** (2025-12-04): Apply suggestions from code review
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `4ccbc7e5` **Darius Wattimena** (2025-12-04): Remove fixed TODO
- `d8ee09d2` **Darius Wattimena** (2025-12-04): Merge remote-tracking branch 'origin/TCC-504-fix-activities-before-visit' into TCC-504-fix-activities-before-visit
- `0501a0c2` **Darius Wattimena** (2025-12-04): Don't throw an error when eta and etd are null or no arrival time is provided
- `8ec9edf6` **Darius Wattimena** (2025-12-04): Update comment to make sense
- `7f38e3cf` **Darius Wattimena** (2025-12-04): Merge pull request #677 from teqplay/TCC-458-ignore-prediction-errors
  TCC-458 Ignore prediction errors in TrueDestinationEtaProcessor
- `8c7c2533` **Darius Wattimena** (2025-12-04): Merge branch 'develop' into TCC-504-fix-activities-before-visit
- `d8722e97` **Darius Wattimena** (2025-12-08): Added documentation for EOSP en Stop processors
- `72cb5a1b` **Darius Wattimena** (2025-12-08): Merge pull request #676 from teqplay/TCC-504-fix-activities-before-visit
  TCC-504 fix activities before visit

## Reviews

### michel-teqplay — APPROVED (2025-12-08)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-08)

## Code Review Summary

I've conducted a comprehensive review of this release PR. The changes appear to be well-structured and include important enhancements to the vessel voyage tracking system. I've identified a few areas for potential improvement that I'll comment on inline.

### Key Observations:
- ✅ Good addition of the `postProcessed` field to NewESoF for better state tracking
- ✅ Proper test coverage for new functionality
- ✅ Consistent code style and patterns
- ⚠️ Some areas could benefit from additional validation and error handling

### Overall Assessment:
The code quality is good and the changes align with the existing architecture. The additions are logical and well-integrated.

### github-actions[bot] — COMMENTED (2025-12-08)

## Additional Code Review Observations

After examining the detailed changes, I have a few specific recommendations:

### 🔍 **NewESoF Model Enhancement**
The addition of `currentPortEtd` field is well-designed, but consider adding validation to ensure it's only set for visits, not voyages, as documented.

### 📊 **Test Coverage**
Excellent expansion of test coverage, particularly for the ETA processor scenarios. The new test cases cover important edge cases.

### 🏗️ **Architecture Improvements**
The `splitVisitActivities` function is a good addition for handling complex visit transitions. The logic appears sound for redistributing activities between visits and voyages.

### ⚠️ **Potential Areas for Improvement**
1. **Error Handling**: Some methods could benefit from more explicit error handling for edge cases
2. **Documentation**: The extensive documentation added to `EndOfSeaPassageEndProcessor` is excellent - consider applying similar documentation standards to other complex processors
3. **Performance**: The activity splitting logic involves multiple list operations - consider if any optimizations are needed for high-volume scenarios

### ✅ **Positive Aspects**
- Consistent code style throughout
- Good separation of concerns
- Comprehensive test coverage for new functionality
- Clear business logic documentation

Overall, this is a well-executed release with thoughtful improvements to the vessel tracking system.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-08)

## Pull request overview

This release implements estimated time of departure (ETD) prediction capabilities and improves activity management when vessels transition between ports. The main addition is the `currentPortEtd` field to the ESoF (Electronic Statement of Facts) model, along with comprehensive documentation improvements across processor classes.

**Key Changes:**
- Added ETD prediction support via new `currentPortEtd` field in NewESoF model
- Implemented `splitVisitActivities` function to properly redistribute activities when visits are split or swapped
- Enhanced processor documentation with detailed business context and edge case descriptions
- Updated message handlers to use explicit drain timeouts for graceful shutdowns

### Reviewed changes

Copilot reviewed 15 out of 16 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewESoF.kt | Added `currentPortEtd` field with clear documentation that it's null for voyages |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt | Refactored to handle both ETA and ETD predictions, correctly applying ETD only to visit ESoFs |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt | Added `splitVisitActivities` function to redistribute activities between visits and voyages based on timing |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt | Integrated activity splitting when confirming visits and swapping ports |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt | Added comprehensive KDoc documentation explaining business logic and edge cases |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt | Added extensive documentation for EOSP exit handling scenarios |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyService.kt | Updated to populate ETD in departure port from ESoF data |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/StoryService.kt | Added stops to voyage POMA entities list |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/*.kt | Added explicit drain timeouts to message handlers |
| src/test/kotlin/.../TrueDestinationEtaProcessorTest.kt | Comprehensive tests for ETD prediction handling in both visit and voyage scenarios |
| src/test/kotlin/.../EventProcessingServiceTest.kt | Added test for visit splitting with multiple activity types |
| src/test/kotlin/.../JourneyServiceTest.kt | Tests for ETD population in journey API responses |
| build.gradle | Updated skeleton and etapredictor dependency versions |
</details>

## Review Comments

### Copilot — 2025-12-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

The import `kotlin.collections.ifEmpty` is unnecessary. The `ifEmpty` function is available by default in Kotlin's standard library and doesn't need to be explicitly imported.
```suggestion

```
