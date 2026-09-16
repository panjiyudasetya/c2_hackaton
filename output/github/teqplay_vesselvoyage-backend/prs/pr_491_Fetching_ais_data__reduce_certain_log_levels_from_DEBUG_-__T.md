---
id: github:teqplay/vesselvoyage-backend:pr:491
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 491
title: Fetching ais data, reduce certain log levels from DEBUG -> TRACE
author: leonjoosse
state: closed
date: '2025-05-01'
merged_at: '2025-05-01'
base_branch: develop
head_branch: ais-fetching-logs
url: https://github.com/teqplay/vesselvoyage-backend/pull/491
labels: []
linked_issues: []
explicit_links: []
---
# PR #491: Fetching ais data, reduce certain log levels from DEBUG -> TRACE

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/491  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `ais-fetching-logs`  
**Created:** 2025-05-01  
**Merged:** 2025-05-01  

## Description

_No description._

## Commits

- `92d7cdd8` **leonj** (2025-05-01): Fetching ais data, reduce certain log levels from DEBUG -> TRACE

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-01)

## Pull Request Overview

This pull request updates logging levels from DEBUG (and one INFO) to TRACE in order to reduce log verbosity for AIS data fetching and trace processing.  
- Updates to log level conversions in trace processing and historic trace generation  
- Consistent logging level change across multiple services supporting AIS and trace functionalities

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt | Changed log level calls from DEBUG/INFO to TRACE and reformatted one log statement to a multi-line lambda. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/TraceService.kt | Updated several logging calls from DEBUG to TRACE, including multiline log lambdas in several methods. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/AisFetchingService.kt | Adjusted a log statement from DEBUG to TRACE during AIS trace fetching. |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/service/TraceService.kt:278**
* [nitpick] For improved readability, consider rewriting the multiline logging lambda using a single string interpolation rather than concatenating strings.
```
$entryId, force = $force)
```
</details>

### Darius-Wattimena — DISMISSED (2025-05-01)

_No comment._

### Darius-Wattimena — APPROVED (2025-05-01)

_No comment._

## Review Comments

### Copilot — 2025-05-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt`

[nitpick] Consider using a single Kotlin string template instead of splitting the message over multiple lines with concatenation to improve readability.
```suggestion
                """
                Resumed entry has no Trace, using canceled entry one 
                (imo = $imo, resumed = $resumedVoyageId, canceled = $canceledVisitId)
                """.trimIndent()
```
