---
id: github:teqplay/vesselvoyage-backend:pr:525
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 525
title: TCC-147 reflection fix
author: Darius-Wattimena
state: closed
date: '2025-06-04'
merged_at: '2025-06-04'
base_branch: develop
head_branch: TCC-147-reflection-issue
url: https://github.com/teqplay/vesselvoyage-backend/pull/525
labels: []
linked_issues: []
explicit_links: []
---
# PR #525: TCC-147 reflection fix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/525  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-147-reflection-issue`  
**Created:** 2025-06-04  
**Merged:** 2025-06-04  

## Description

_No description._

## Commits

- `8179e638` **Darius Wattimena** (2025-06-04): Adjusted code so we avoid using generics for overwriting a private final field and instead make use of mutable lists

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-04)

## Pull Request Overview

This pull request fixes reflection issues and enforces mutability for area activity collections throughout the code and tests. The key changes are:
- Replacing immutable list creations (listOf) with mutable list creations (mutableListOf) in tests, processing services, and utility functions.
- Updating the NewVisit API model to use mutable lists for all area activity properties.
- Removing reflection-based modifications in favor of direct updates on mutable collection objects.

### Reviewed Changes

Copilot reviewed 14 out of 14 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/TestUtil.kt | Updated createNewVisit to add a new parameter and changed list creations to mutable lists. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/dsl/EntriesBuilder.kt | Modified build() to return a mutable list. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt | Adjusted list assignments to use mutableListOf for area activity fields. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2ServiceTest.kt | Updated NewVisit creation to use createNewVisit and mutable lists. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt | Changed berthAreaActivities to a mutable list in test case. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PortReporterStatementOfFactsViewGeneratorTest.kt | Converted berthAreaActivities to a mutable list. |
| src/test/kotlin/nl/teqplay/vesselvoyage/mapper/EntryV2MapperTest.kt | Updated portAreaActivities list creation to mutable list. |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/AreaActivityUtils.kt | Modified functions to return mutable lists instead of immutable ones. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/terminalmooring/TerminalMooringAreaEndProcessor.kt | Converted terminalMooringAreaActivities to a mutable list. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/port/PortEndProcessor.kt | Updated portAreaActivities assignment to use toMutableList(). |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt | Changed portAreaActivities to a mutable list. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt | Replaced javaField reflection update with direct mutable list modifications. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt | Updated portAreaActivities conversion to mutable list. |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewVisit.kt | Changed all area activity properties from immutable to mutable collections. |
</details>

### TeqJoostD — APPROVED (2025-06-04)

![image](https://github.com/user-attachments/assets/74290069-61e5-4ab5-9335-1597d8e71489)
