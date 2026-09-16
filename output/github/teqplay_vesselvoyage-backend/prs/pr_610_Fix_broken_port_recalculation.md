---
id: github:teqplay/vesselvoyage-backend:pr:610
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 610
title: Fix broken port recalculation
author: Darius-Wattimena
state: closed
date: '2025-09-19'
merged_at: '2025-09-19'
base_branch: develop
head_branch: fix-broken-port-recalculation
url: https://github.com/teqplay/vesselvoyage-backend/pull/610
labels: []
linked_issues: []
explicit_links: []
---
# PR #610: Fix broken port recalculation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/610  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-broken-port-recalculation`  
**Created:** 2025-09-19  
**Merged:** 2025-09-19  

## Description

_No description._

## Commits

- `b62e9fe9` **Darius Wattimena** (2025-09-19): Disable interest distribution for port requests to prevent duplicate visits in S2S scenarios
- `40d6590b` **Darius Wattimena** (2025-09-19): Added a test case to ensure that when a merge happens when the existing data contains duplicate visits that one of the duplicates gets deleted
- `64baeb56` **Darius Wattimena** (2025-09-19): Disable interest distribution in test scenarios to align with recent changes

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-19)

## Pull Request Overview

Purpose: Adjust recalculation to disable interest distribution for port-related scenarios to prevent duplicate visit generation and add test coverage for merging identical overlapping entries.
- Add useInterestDistribution = false to Scenario.Settings in production and corresponding test.
- Introduce a new merge test validating consolidation of identical overlapping visits.
- Minor test setup adjustments adding helper imports.

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionService.kt | Adds useInterestDistribution = false with explanatory comment to prevent duplicate visits. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionServiceTest.kt | Updates scenario settings in test to match new parameter. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2ServiceTest.kt | Adds new test for merging identical overlapping visits and necessary helper imports. |

### Jamie-de-Leest — APPROVED (2025-09-19)

_No comment._

## Review Comments

### Copilot — 2025-09-19 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2ServiceTest.kt`

Test name is grammatically awkward and a bit unclear. Consider a clearer phrasing such as `merge identical overlapping visits results in single visit` to better convey the intent.
