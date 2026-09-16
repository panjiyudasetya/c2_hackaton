---
id: github:teqplay/vesselvoyage-backend:pr:625
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 625
title: TCC-470 always update visit eta
author: Darius-Wattimena
state: closed
date: '2025-10-03'
merged_at: '2025-10-03'
base_branch: develop
head_branch: TCC-470-always-update-visit-eta
url: https://github.com/teqplay/vesselvoyage-backend/pull/625
labels: []
linked_issues: []
explicit_links: []
---
# PR #625: TCC-470 always update visit eta

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/625  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-470-always-update-visit-eta`  
**Created:** 2025-10-03  
**Merged:** 2025-10-03  

## Description

_No description._

## Commits

- `b1837145` **Darius Wattimena** (2025-10-03): Update TrueDestinationEtaProcessor to handle previous visit updates and add new parameters for ETA processing
- `73c4c5bd` **Darius Wattimena** (2025-10-03): Remove unused ETA prediction configurations from application properties which have been removed before
- `dee0c5b8` **Darius Wattimena** (2025-10-03): Update test to be the expected outcome
- `4701e1ba` **Darius Wattimena** (2025-10-03): Update tests to fully check the ship status as well
- `e5f1c4f2` **Darius Wattimena** (2025-10-03): Remove unneeded cast in test

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-03)

## Pull Request Overview

This PR implements functionality to always update visit ETA predictions by removing configuration flags that previously disabled ETA predictions and extending the ETA processor to update both current voyage and previous visit entries.

- Removes the `processing.enable-eta-predictions` configuration property to always enable ETA processing
- Extends `TrueDestinationEtaProcessor` to update both voyage and previous visit entries with ETA predictions
- Adds comprehensive test coverage for the new ETA update scenarios

### Reviewed Changes

Copilot reviewed 5 out of 5 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/resources/application.properties | Removes the eta-predictions enable flag to always enable ETA processing |
| src/test/resources/application.properties | Removes the eta-predictions enable flag from test configuration |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt | Refactors processor to handle both current voyage and previous visit ETA updates |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/TestUtil.kt | Adds new parameters to test utility for ETA testing |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessorTest.kt | Adds comprehensive test cases for new ETA update scenarios |
</details>

### Jamie-de-Leest — APPROVED (2025-10-03)

_No comment._

## Review Comments

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessor.kt`

[nitpick] This logic creates a new ESoF inline within the parameter assignment. Consider extracting this to a separate method or using the existing `createNewESoF` utility function for consistency and better maintainability.

### Copilot — 2025-10-03 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/eta/TrueDestinationEtaProcessorTest.kt`

[nitpick] The explicit type annotation was removed, but the variable is still being cast implicitly. Consider keeping the explicit type `PredictionProcessingResult.PredictionProcessingIssue` for clarity, or add a comment explaining the expected type.
```suggestion
        val issue: PredictionProcessingResult.PredictionProcessingIssue = result.issues.single()
```
