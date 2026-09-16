---
id: github:teqplay/vesselvoyage-backend:pr:484
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 484
title: 'SPV-2585: Limit AIS data retrieval to max 3 months'
author: leonjoosse
state: closed
date: '2025-04-24'
merged_at: '2025-04-29'
base_branch: develop
head_branch: SPV-2585-aisdata-limit-3months
url: https://github.com/teqplay/vesselvoyage-backend/pull/484
labels: []
linked_issues: []
explicit_links: []
---
# PR #484: SPV-2585: Limit AIS data retrieval to max 3 months

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/484  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2585-aisdata-limit-3months`  
**Created:** 2025-04-24  
**Merged:** 2025-04-29  

## Description

Also limit chunked requests (using `maxDays`), so the total requested days must not exceed the 3 months

Default value is 3 months (90 days), but is configurable through `trace.max-request-length-days`.

## Commits

- `6d011b31` **leonj** (2025-04-23): Limit retrieving AIS to max 90 days (also chunked requests total days cannot be longer)
- `ab9b97ad` **leonj** (2025-04-23): Merge branch 'develop' into SPV-2585-aisdata-limit-3months
- `e9f16440` **leonj** (2025-04-24): Log statements to debug, not warn. Remove comment
- `843a0b18` **Leon Joosse** (2025-04-24): Fix potential NPE in AisFetchingService
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-24)

## Pull Request Overview

This PR limits AIS data retrieval requests to a maximum duration of 3 months by introducing a new configuration parameter, maxRequestLengthDays. Key changes include:
- Adding maxRequestLengthDays configuration in TraceProperties and updating relevant service constructors.
- Updating tests in TraceServiceTest, ProcessingTraceServiceTest, and EntryServiceTest to include the new parameter.
- Implementing validation in ProcessingTraceService, TraceService, and AisFetchingService to abort requests exceeding the maximum configured days.

### Reviewed Changes

Copilot reviewed 7 out of 9 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/TraceServiceTest.kt | Added maxRequestLengthDays in test service instantiation. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/ProcessingTraceServiceTest.kt | Injected TraceProperties mock and updated service constructor. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/EntryServiceTest.kt | Added maxRequestLengthDays in test configuration. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt | Added validation to check request duration against maxRequestLengthDays. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/TraceService.kt | Updated trace retrieval logic to return empty list if request exceeds allowed days. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/AisFetchingService.kt | Added validation to check AIS trace request length. |
| src/main/kotlin/nl/teqplay/vesselvoyage/properties/TraceProperties.kt | Extended properties to include maxRequestLengthDays. |
</details>


<details>
<summary>Files not reviewed (2)</summary>

* **src/main/resources/application.properties**: Language not supported
* **src/test/resources/application.properties**: Language not supported
</details>

### TeqJoostD — APPROVED (2025-04-24)

_No comment._

## Review Comments

### Copilot — 2025-04-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/AisFetchingService.kt`

The condition uses 'endTime' directly, which is nullable, potentially causing a NullPointerException. Consider using the non-null variable 'to' defined on line 56 instead.
```suggestion
        if (Duration.between(startTime, to).toDays() > traceProperties.maxRequestLengthDays) {
            log.debug {
                "Cannot fetch AIS data for IMO $imo: Trace request length (${Duration.between(startTime, to)}) " +
```
