---
id: github:teqplay/vesselvoyage-backend:pr:619
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 619
title: TCC-435 accuracy testing report generation
author: Jamie-de-Leest
state: closed
date: '2025-09-29'
merged_at: '2025-10-06'
base_branch: develop
head_branch: TCC-435-accuracy-testing-report-generation
url: https://github.com/teqplay/vesselvoyage-backend/pull/619
labels: []
linked_issues: []
explicit_links: []
---
# PR #619: TCC-435 accuracy testing report generation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/619  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-435-accuracy-testing-report-generation`  
**Created:** 2025-09-29  
**Merged:** 2025-10-06  

## Description

_No description._

## Commits

- `4c22883b` **Jamie de Leest** (2025-09-29): feat: add accuracy report generation and CSV export
- `c7b496e6` **Jamie de Leest** (2025-09-29): test: add tests for accuracy report functions
- `731fbe99` **Jamie de Leest** (2025-09-29): chore: ktlint
- `8160bd00` **Jamie de Leest** (2025-09-30): chore: implement feedback

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-29)

## Pull Request Overview

This PR implements accuracy testing report generation functionality that allows exporting timestamp accuracy data in both JSON and CSV formats. The implementation adds new endpoints and services to generate comprehensive reports of accuracy checks across different vessel visits.

- Adds new `AccuracyReportEntry` model to structure accuracy report data with vessel and port information
- Implements `getAccuracyReport` and `getAccuracyReportCsv` methods in `TimestampAccuracyService` for report generation
- Adds REST endpoints `/report` and `/report/csv` to expose the report functionality

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| AccuracyReportEntry.kt | New data class for structuring accuracy report entries with vessel and accuracy check information |
| TimestampAccuracyService.kt | Adds report generation methods with CSV export functionality and time-based filtering |
| ProcessingTimestampAccuracyController.kt | Exposes new REST endpoints for JSON and CSV report generation |
| TimestampAccuracyServiceTest.kt | Comprehensive test coverage for the new report generation functionality |

### TeqJoostD — COMMENTED (2025-09-30)

_No comment._

### TeqJoostD — APPROVED (2025-09-30)

_No comment._

### Darius-Wattimena — APPROVED (2025-10-02)

_No comment._

## Review Comments

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

The method modifies the HttpServletResponse parameter directly but doesn't return anything to indicate success or failure. Consider returning a status indicator or throwing exceptions for error cases to make the API more explicit about its outcomes.

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

When `visit.portAreaActivities.firstOrNull()` returns null, an empty string is passed to `getPortByAreaId`. This could cause unexpected behavior or inefficient lookups. Consider handling the null case explicitly by returning null or a default value without making the service call.
```suggestion
                    unlocode = visit.portAreaActivities.firstOrNull()?.areaId
                        ?.let { infraService.getPortByAreaId(it)?.unlocode }
```

### Copilot — 2025-09-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

[nitpick] The local extension function `toBit()` is defined inside the method scope. Consider moving this to a companion object or utility class to improve reusability and testability.

### TeqJoostD — 2025-09-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

Would agree since unlocode is nullable
