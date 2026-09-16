---
id: github:teqplay/vesselvoyage-backend:pr:614
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 614
title: TCC-436 add total accuracy score endpoint
author: Jamie-de-Leest
state: closed
date: '2025-09-24'
merged_at: '2025-09-26'
base_branch: develop
head_branch: TCC-436-add-total-accuracy-score-endpoint
url: https://github.com/teqplay/vesselvoyage-backend/pull/614
labels: []
linked_issues: []
explicit_links: []
---
# PR #614: TCC-436 add total accuracy score endpoint

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/614  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-436-add-total-accuracy-score-endpoint`  
**Created:** 2025-09-24  
**Merged:** 2025-09-26  

## Description

_No description._

## Commits

- `b29b2ca6` **Jamie de Leest** (2025-09-23): fix: change logic for areAllVisitsAccurate so that it checks not filled in Category's
- `06c1dff7` **Jamie de Leest** (2025-09-24): feat: add endpoint to retrieve accuracy scores for timestamps
- `612511b6` **Jamie de Leest** (2025-09-24): test: expand accuracy check results in TimestampAccuracyServiceTest

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-24)

## Pull Request Overview

This PR implements a total accuracy score endpoint that calculates both overall and time-filtered accuracy percentages for timestamp accuracy checks. The feature adds an endpoint to retrieve accuracy statistics over configurable time periods.

- Adds utility function to check if an Instant is within a specified number of past days
- Implements accuracy score calculation service method with time-based filtering
- Creates REST endpoint to expose accuracy scores with configurable day range

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/dateTimeUtils.kt | Adds utility function to check if timestamp is within past N days |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/accuracy/AccuracyScoreResponse.kt | Creates data class for accuracy score response |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt | Implements accuracy calculation logic and fixes category handling bug |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingTimestampAccuracyController.kt | Adds REST endpoint for accuracy scores |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/DateTimeUtilsTest.kt | Adds comprehensive tests for date utility function |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyServiceTest.kt | Updates existing tests and adds new tests for accuracy score functionality |
</details>

### michel-teqplay — APPROVED (2025-09-24)

_No comment._

## Review Comments

### Copilot — 2025-09-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingTimestampAccuracyController.kt`

This endpoint uses POST method but appears to be a read-only operation that retrieves data without side effects. Consider using @GetMapping instead to follow REST conventions for read operations.
```suggestion
    @GetMapping("/score")
```

### Copilot — 2025-09-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyService.kt`

When percentagesPerCategory is empty, calling average() will throw an exception. Add a check to return 0.0 when there are no categories to avoid runtime errors.
```suggestion
        val totalAccuracy = if (percentagesPerCategory.isEmpty()) {
            0.0
        } else {
            percentagesPerCategory.values.average()
        }
```
