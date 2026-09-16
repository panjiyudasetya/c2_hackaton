---
id: github:teqplay/vesselvoyage-backend:pr:603
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 603
title: Release 10 Sep 2025
author: Darius-Wattimena
state: closed
date: '2025-09-10'
merged_at: '2025-09-10'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/603
labels: []
linked_issues: []
explicit_links: []
---
# PR #603: Release 10 Sep 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/603  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-09-10  
**Merged:** 2025-09-10  

## Description

_No description._

## Commits

- `cbcbc842` **Darius Wattimena** (2025-08-22): Adjusted accuracy checks and endpoints to be easier for frontend
- `164a7a0a` **Darius Wattimena** (2025-08-25): Clean up code and adjusted test case so it actually works
- `00c23436` **Darius Wattimena** (2025-08-25): Merge branch 'develop' into TCC-332
- `ff494dba` **Darius Wattimena** (2025-08-25): Merge branch 'develop' into TCC-332
- `89d731e3` **Darius Wattimena** (2025-08-25): Merge branch 'develop' into TCC-332
- `166eeb6c` **Darius Wattimena** (2025-08-25): Updated id field in TimestampAccuracy model
- `f20e24ed` **Darius Wattimena** (2025-08-25): Removed unused endpoints
- `b11e1bfd` **Darius Wattimena** (2025-08-25): Renamed permission class names with Auth prefix to make them not clash with the Swagger annotation names
- `1be9f69d` **Darius Wattimena** (2025-08-25): Add Swagger annotations for timestamp accuracy endpoints
- `9253b8bb` **Darius Wattimena** (2025-08-25): Make sure we don't create or update when both activityId and expected are null
- `a51ff76a` **Darius Wattimena** (2025-08-25): Added more documentation on the input models
- `592dc718` **Darius Wattimena** (2025-08-25): Updated annotation so description is placed on the correct place
- `8e3010be` **Darius Wattimena** (2025-08-26): Fixed test
- `14a80e04` **Darius Wattimena** (2025-08-26): PR feedback
- `24d569ce` **Darius Wattimena** (2025-08-26): Updated description to be a bit clearer
- `2f10a7f9` **Darius Wattimena** (2025-08-27): Merge branch 'develop' into TCC-332
- `661bad96` **Darius Wattimena** (2025-08-27): PR feedback + adjusted response to include all categories, even when there is no expected timestamp for said category
- `7820f61c` **Darius Wattimena** (2025-08-27): Additional fixes
- `699338bf` **Darius Wattimena** (2025-09-03): Merge branch 'develop' into TCC-332
- `1407564a` **Darius Wattimena** (2025-09-05): Adjusted processing to also delete the expected timestamps when the visit is deleted
- `c133d025` **Darius Wattimena** (2025-09-05): Add an endpoint to be able to delete expected timestamps by visit id
- `f52c875c` **Darius Wattimena** (2025-09-05): Fix revents test so it compiles again
- `c208e320` **Darius Wattimena** (2025-09-05): Adjusted existing tests which called the wrong verify call
- `15fdf18c` **Darius Wattimena** (2025-09-05): Merge pull request #598 from teqplay/TCC-332
  TCC-332

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-10)

## Pull Request Overview

This release PR updates the vessel voyage processing system to implement timestamp accuracy validation functionality. The changes include refactoring existing accuracy models into a dedicated `accuracy` package, enhancing the timestamp accuracy service with new CRUD operations, and updating authorization references throughout the codebase.

- Major refactoring of timestamp accuracy validation system with improved data model
- API endpoint updates for better REST compliance and comprehensive validation features
- Authorization model updates replacing `Operation`/`Resource` with `AuthOperation`/`AuthResource`

### Reviewed Changes

Copilot reviewed 48 out of 48 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| TimestampAccuracyService.kt | Enhanced service with new CRUD operations, improved accuracy checking logic, and activity ID tracking |
| ProcessingTimestampAccuracyController.kt | Complete API redesign with proper REST endpoints, validation, and comprehensive documentation |
| ReventsRecalculationService.kt | Added cleanup of accuracy timestamps when visits are deleted |
| Multiple model files | Refactored accuracy models into dedicated package with improved structure |
| Multiple controller files | Updated authorization references from `Operation`/`Resource` to `AuthOperation`/`AuthResource` |
</details>

## Review Comments

### Copilot — 2025-09-10 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt`

These verify statements are checking `newESoFDataSource` but the context suggests this should be verifying operations that were never called. The duplication appears to be replacing what should have been `newVoyageDataSource` verifications, potentially masking test failures if `newVoyageDataSource` operations are incorrectly called.

### Copilot — 2025-09-10 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

The `checkedActivities` set is being populated with `actualTimestamp.activityId` which could be null based on the `VisitTimestamp` data class definition. Adding null values to a set may cause unexpected behavior. Consider filtering out null activity IDs or handling them explicitly.
```suggestion
            actualTimestamp.activityId?.let { checkedActivities.add(it) }
```

### Copilot — 2025-09-10 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

This filter is checking if `expectedTimestamp.activityId` is not in `checkedActivities`, but `expectedTimestamp.activityId` can be null. The `in` operator with null values may not work as expected. Consider adding null safety checks.
```suggestion
            expectedTimestamp.activityId == null || expectedTimestamp.activityId !in checkedActivities
```

### Copilot — 2025-09-10 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

The `timestamps.map { actual -> actual.activityId }` operation is performed for every element in the `expected` list, creating multiple intermediate lists. Consider extracting this to a variable or using a set for better performance: `val actualActivityIds = timestamps.map { it.activityId }.toSet()`
```suggestion
        val actualActivityIds = timestamps.map { it.activityId }.toSet()
        val leftOverExpected = expected.filter { expected -> expected.activityId !in actualActivityIds }
```
