---
id: github:teqplay/vesselvoyage-backend:pr:534
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 534
title: TTC-163 Remove ref fields
author: TeqJoostD
state: closed
date: '2025-06-11'
merged_at: null
base_branch: develop
head_branch: TCC-163
url: https://github.com/teqplay/vesselvoyage-backend/pull/534
labels: []
linked_issues: []
explicit_links: []
---
# PR #534: TTC-163 Remove ref fields

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/534  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-163`  
**Created:** 2025-06-11  

## Description

test

## Commits

- `08989d36` **TeqJoostD** (2025-06-11): Refactor PtoStatementOfFactsMapper and related tests to remove deprecated fields and align with new ID structure
- `7b7df80d` **TeqJoostD** (2025-06-17): fix: adjusted tests

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-11)

## Pull Request Overview

This PR refactors the PtoStatementOfFactsMapper and its related tests to remove deprecated fields and update the ID structure to align with recent changes.  
- Removed deprecated "ref", "terminalVisitRef", and "portAreaRef" fields.  
- Updated test assertions in both view generator and mapper tests to reflect the new ID structure.  
- Adjusted mapping definitions in the main mapper and API view model accordingly.

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt | Removed deprecated "ref" usages from test helper functions and calls. |
| src/test/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapperTest.kt | Updated test assertions to use new ID fields while removing assertions for deprecated fields. |
| src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt | Excluded mappings for deprecated fields from various mapping functions. |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/pto/PtoStatementOfFactsView.kt | Removed deprecated fields from the data classes to match the new ID structure. |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt:168**
* The mapping for 'area' in toApproachAreaVisit is incomplete; please specify a source field or remove the trailing comma to ensure proper mapping functionality.
```
@Mapping(target = "area",)
```
</details>

### Darius-Wattimena — APPROVED (2025-06-27)

_No comment._

## Comments

### TeqJoostD — 2025-06-11

![image](https://github.com/user-attachments/assets/96c49bed-90cc-400b-8aed-4a3a65a2bbda)


### Darius-Wattimena — 2025-06-27

Changes look fine, please fix the merge conflict. Probably have to check when we merge this into develop, given that this needs the PTO team to be fully moved away from the ref fields
