---
id: github:teqplay/vesselvoyage-backend:pr:587
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 587
title: TCC-112 timestamp accuracy daily report
author: Darius-Wattimena
state: closed
date: '2025-08-08'
merged_at: '2025-08-25'
base_branch: develop
head_branch: TCC-112
url: https://github.com/teqplay/vesselvoyage-backend/pull/587
labels: []
linked_issues: []
explicit_links: []
---
# PR #587: TCC-112 timestamp accuracy daily report

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/587  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-112`  
**Created:** 2025-08-08  
**Merged:** 2025-08-25  

## Description

_No description._

## Commits

- `92a59c60` **Darius Wattimena** (2025-08-08): Added logic so we can create reports of the timestamp accuracy based using cron
- `844d70cf` **Darius Wattimena** (2025-08-08): Adjusted the createDate of the report to be the time we initiate the cron instead of doing it at the end
- `ccff25a5` **Darius Wattimena** (2025-08-08): Merge branch 'TCC-101-automated-testing' into TCC-112
- `db05bb21` **Darius Wattimena** (2025-08-08): Added missing profiles

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-08)

## Pull Request Overview

This PR implements a daily timestamp accuracy reporting system that validates vessel visit timestamps on a scheduled basis. The feature generates reports containing accuracy metrics and stores them in a MongoDB collection.

- Adds a scheduled service to validate timestamp accuracy for all visits daily at 7 AM UTC
- Creates a data model and data source for storing timestamp accuracy reports
- Configures cron scheduling through application properties

### Reviewed Changes

Copilot reviewed 5 out of 5 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/resources/application.properties | Adds cron configuration for daily 7 AM UTC execution |
| src/test/resources/application.properties | Adds test configuration for cron scheduling |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyReportService.kt | Implements scheduled reporting service with accuracy validation logic |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/TimestampAccuracyReport.kt | Defines data model for timestamp accuracy reports |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/TimestampAccuracyReportDataSource.kt | Provides MongoDB data access for storing reports |
</details>

### TeqJoostD — DISMISSED (2025-08-15)

_No comment._

### TeqJoostD — APPROVED (2025-08-22)

_No comment._

## Review Comments

### Copilot — 2025-08-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyReportService.kt`

This creates an intermediate collection during the flatMap operation. Consider using asSequence() to process the data lazily and improve memory efficiency when dealing with large datasets.
```suggestion
        val countByResponseResult = responseForAllVisits.asSequence().flatMap { response -> response.result.values }
```

### Copilot — 2025-08-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/TimestampAccuracyReportService.kt`

Logging the entire report object at INFO level may produce excessive output in production. Consider logging only key metrics or reducing to DEBUG level.
