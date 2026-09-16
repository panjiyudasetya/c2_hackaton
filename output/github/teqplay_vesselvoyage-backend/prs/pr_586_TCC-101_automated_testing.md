---
id: github:teqplay/vesselvoyage-backend:pr:586
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 586
title: TCC-101 automated testing
author: Darius-Wattimena
state: closed
date: '2025-08-08'
merged_at: '2025-08-22'
base_branch: develop
head_branch: TCC-101-automated-testing
url: https://github.com/teqplay/vesselvoyage-backend/pull/586
labels: []
linked_issues: []
explicit_links: []
---
# PR #586: TCC-101 automated testing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/586  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-101-automated-testing`  
**Created:** 2025-08-08  
**Merged:** 2025-08-22  

## Description

_No description._

## Commits

- `98fa3ebe` **Darius Wattimena** (2025-08-07): Extended PTO SOF and SlowMovingPeriod models to have all implement the ApiStartEnd interface to make it easier to get the start and end
- `90f72810` **Darius Wattimena** (2025-08-07): Added logic so we can check the accuracy of timestamps comparing them with the actual data that is in the Visit and the Esof models
- `b3701401` **Darius Wattimena** (2025-08-07): Changed so we return the accuracy result checks as well
- `67774490` **Darius Wattimena** (2025-08-07): Added authorization on endpoints so they can only be called by developers
- `a7cc4c0b` **Darius Wattimena** (2025-08-08): Adjust CorrectTimestampService so we know a bit more what is wrong when checking the result
- `82e03ad5` **Darius Wattimena** (2025-08-08): Added unit tests to cover all different checks that need to be done for timestamp checking
- `b6dc497f` **Darius Wattimena** (2025-08-08): Add AccuracyCheckResponse and code cleanup
- `1a08b978` **Darius Wattimena** (2025-08-08): Merge branch 'develop' into TCC-101-automated-testing
- `b461eee8` **Darius Wattimena** (2025-08-08): Renamed to TimestampAccuracy to be more descriptive what the classes are about
- `19d3fc29` **Darius Wattimena** (2025-08-08): Apply suggestions from code review
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-08)

## Pull Request Overview

This PR implements TCC-101 automated testing by adding timestamp accuracy checking functionality. The system validates that vessel voyage timestamps fall within acceptable thresholds compared to expected values, providing automated accuracy assessment for various timestamp categories.

Key changes:
- New timestamp accuracy service with comprehensive validation logic
- Data models for accuracy checking with support for 11 different timestamp categories
- REST API endpoints for managing accuracy entries and running checks
- Common interface for API models to standardize timestamp handling

### Reviewed Changes

Copilot reviewed 10 out of 10 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `TimestampAccuracyService.kt` | Core service implementing accuracy validation logic with 6-minute threshold |
| `TimestampAccuracyServiceTest.kt` | Comprehensive test suite covering all service methods and validation scenarios |
| `TimestampAccuracy.kt` | Data model for expected timestamps with category-based organization |
| `AccuracyCheckResult.kt` | Enum defining possible accuracy check outcomes |
| `AccuracyCheckResponse.kt` | Response model for accuracy check results |
| `TimestampAccuracyDataSource.kt` | MongoDB data access layer for timestamp accuracy entries |
| `ProcessingTimestampAccuracyController.kt` | REST controller exposing CRUD and validation endpoints |
| `ApiStartEnd.kt` | Common interface for API models with start/end timestamps |
| `PtoStatementOfFactsView.kt` | Updated existing models to implement ApiStartEnd interface |
| `SlowMovingPeriod.kt` | Updated to implement ApiStartEnd interface |
</details>

### TeqJoostD — APPROVED (2025-08-15)

_No comment._

## Review Comments

### Copilot — 2025-08-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/AccuracyCheckResult.kt`

There are spelling errors in the comment: 'withint' should be 'within' and 'the one of' should be 'one of'.
```suggestion
     * Indicate that one of the timestamps is not within the boundaries to call it accurate.
```

### Copilot — 2025-08-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

Grammar error in comment: 'seen as accuracy' should be 'seen as accurate'.
```suggestion
         * The threshold for timestamps to be seen as accurate.
```

### Copilot — 2025-08-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

The DRIFTING case calls `mapToVisitTimestamps()` on a nullable `CategorizedPeriods` object, but this method is only defined for non-null `CategorizedPeriods`. This will cause a compilation error.
```suggestion
            TimestampCategory.DRIFTING -> if (apiSof.slowMovingPeriods != null) apiSof.slowMovingPeriods.mapToVisitTimestamps() else emptyList()
```
