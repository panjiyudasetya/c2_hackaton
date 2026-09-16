---
id: github:teqplay/vesselvoyage-backend:pr:620
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 620
title: TCC-468 add approach areas to portreporter sof
author: Jamie-de-Leest
state: closed
date: '2025-10-02'
merged_at: '2025-10-03'
base_branch: develop
head_branch: TCC-468-add-approach-areas-to-PR-SOF
url: https://github.com/teqplay/vesselvoyage-backend/pull/620
labels: []
linked_issues: []
explicit_links: []
---
# PR #620: TCC-468 add approach areas to portreporter sof

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/620  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-468-add-approach-areas-to-PR-SOF`  
**Created:** 2025-10-02  
**Merged:** 2025-10-03  

## Description

_No description._

## Commits

- `6e5a8b18` **Jamie de Leest** (2025-09-30): feat: add appreach areas to PR-SOF
- `b62d8d37` **Jamie de Leest** (2025-09-30): test: add test for approach area in PR-SOF
- `f6837052` **Jamie de Leest** (2025-10-02): chore: apply pr feedback

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-02)

## Pull Request Overview

This PR adds approach area tracking functionality to the port reporter statement of facts (SOF). It enables the system to capture and report on approach areas that ships pass through during their port visits.

- Adds approach area activities to the NewVisit model and related test utilities
- Implements approach area visit generation and mapping in the SOF view generator
- Creates new data models for approach area visit information and API representation

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/TestUtil.kt | Adds approachAreaActivities parameter to createNewVisit test utility |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PortReporterStatementOfFactsViewGeneratorTest.kt | Adds test coverage for approach area functionality in SOF generation |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PortReporterStatementOfFactsViewGenerator.kt | Implements approach area visit generation logic and integrates it into SOF view |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/portreporterview/ApproachAreaVisitInfo.kt | Creates internal model for approach area visit information |
| src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PortReporterStatementOfFactsMapper.kt | Adds mapping from internal model to API response format |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/portreporter/PortReporterStatementOfFactsView.kt | Defines API model for approach area visits in the port reporter SOF response |
</details>

### Darius-Wattimena — COMMENTED (2025-10-02)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-10-02)

Please apply the copilot feedback, besides that the code looks good to me

### Darius-Wattimena — APPROVED (2025-10-03)

_No comment._

## Review Comments

### Copilot — 2025-10-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PortReporterStatementOfFactsMapper.kt`

The @Mapping annotation for 'area' field is incomplete - it's missing the source mapping. This will likely cause a compilation error or incorrect mapping behavior.
```suggestion
    @Mapping(target = "area", source = "area")
```

### Copilot — 2025-10-02 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PortReporterStatementOfFactsViewGeneratorTest.kt`

Use immutableList() or listOf() instead of mutableListOf() since the list is not modified after creation. This follows immutability best practices.
```suggestion
        val visit = createNewVisit(approachAreaActivities = listOf(approachActivity))
```

### Copilot — 2025-10-02 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PortReporterStatementOfFactsViewGeneratorTest.kt`

Use JUnit assertions like assertEquals() and assertTrue() instead of assert() for better test failure messages and consistency with the rest of the test class.
```suggestion
        assertTrue(result.approachAreas.any { it.area != null })
```

### Darius-Wattimena — 2025-10-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PortReporterStatementOfFactsMapper.kt`

Seems indeed to be the case? Probably good to check what we did here for the PTO one and do something similar?
