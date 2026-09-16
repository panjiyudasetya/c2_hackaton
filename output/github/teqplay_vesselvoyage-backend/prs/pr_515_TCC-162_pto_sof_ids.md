---
id: github:teqplay/vesselvoyage-backend:pr:515
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 515
title: TCC-162 pto sof ids
author: Darius-Wattimena
state: closed
date: '2025-05-27'
merged_at: '2025-05-27'
base_branch: develop
head_branch: TCC-162-pto-sof-ids
url: https://github.com/teqplay/vesselvoyage-backend/pull/515
labels: []
linked_issues: []
explicit_links: []
---
# PR #515: TCC-162 pto sof ids

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/515  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-162-pto-sof-ids`  
**Created:** 2025-05-27  
**Merged:** 2025-05-27  

## Description

_No description._

## Commits

- `1a3ae708` **Darius Wattimena** (2025-05-26): Add id field to all classes exposed to PTO
- `22b04b09` **Darius Wattimena** (2025-05-26): Adjusted test that wasn't adjusted
- `d443e557` **Darius Wattimena** (2025-05-26): Deprecated ref fields and added missing replacement fields
- `f653c908` **Darius Wattimena** (2025-05-27): ktlint
- `23ad5231` **Darius Wattimena** (2025-05-27): Deprecated ref field in berth visit and updated places where we used this ref with the id field

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-27)

## Pull Request Overview

This PR refactors the statement of facts identifiers by introducing explicit id parameters throughout the codebase, replacing derived reference strings. Key changes include:
- Adding an explicit id parameter to helper functions and data classes (e.g. BerthVisitInfo, PilotInfo) in both production and test code.
- Updating test cases and mapper configurations to use the new id values and deprecate old ref fields.
- Adjusting mapping annotations in MapStruct configuration to route id fields appropriately.

### Reviewed Changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/PtoSofHelperFunctions.kt | Added explicit id parameter to createBerthVisitInfo. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt | Updated test helper functions and calls to include explicit id values. |
| src/test/kotlin/nl/teqplay/vesselvoyage/model/esof/ptoview/PilotInfoTest.kt | Adjusted pilot info tests to validate new id usage. |
| src/test/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapperTest.kt | Enhanced assertions to check id mappings in various scenarios. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt | Updated view generation logic to set id fields from event ids. |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/ptoview/PilotInfo.kt | Modified PilotInfo to include an id field populated from encounter data. |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/ptoview/BerthVisitInfo.kt | Introduced an id field to improve clarity of visit identifiers. |
| src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt | Updated mapping definitions to use id and deprecate old ref fields (one mapping for area is incomplete). |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/pto/PtoStatementOfFactsView.kt | Revised API models to include id fields and deprecate legacy ref fields. |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt:178**
* The mapping for the 'area' field in toApproachAreaVisit is missing a source attribute. Please update the annotation to explicitly map 'area' from the appropriate source field.
```
@Mapping(target = "area",)
```
</details>

### TeqJoostD — COMMENTED (2025-05-27)

_No comment._

### TeqJoostD — DISMISSED (2025-05-27)

_No comment._

### TeqJoostD — APPROVED (2025-05-27)

_No comment._

## Review Comments

### TeqJoostD — 2025-05-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/ptoview/BerthVisitInfo.kt`

```suggestion
    @Deprecated("Use id instead", ReplaceWith("id"))
    val ref: Int,
```
