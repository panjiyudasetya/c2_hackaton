---
id: github:teqplay/vesselvoyage-backend:pr:611
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 611
title: Release 19 Sep 2025
author: Darius-Wattimena
state: closed
date: '2025-09-19'
merged_at: '2025-09-19'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/611
labels: []
linked_issues: []
explicit_links: []
---
# PR #611: Release 19 Sep 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/611  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-09-19  
**Merged:** 2025-09-19  

## Description

_No description._

## Commits

- `b62e9fe9` **Darius Wattimena** (2025-09-19): Disable interest distribution for port requests to prevent duplicate visits in S2S scenarios
- `40d6590b` **Darius Wattimena** (2025-09-19): Added a test case to ensure that when a merge happens when the existing data contains duplicate visits that one of the duplicates gets deleted
- `64baeb56` **Darius Wattimena** (2025-09-19): Disable interest distribution in test scenarios to align with recent changes
- `ae2eacad` **Darius Wattimena** (2025-09-19): Merge pull request #610 from teqplay/fix-broken-port-recalculation
  Fix broken port recalculation

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-19)

## Pull Request Overview

This release includes updates to the vessel voyage recalculation system, specifically disabling interest distribution for port requests to prevent duplicate visits in ship-to-ship scenarios. The change ensures consistent behavior in both production code and test scenarios.

- Disabled interest distribution in scenario settings to prevent duplicate visits for ship-to-ship ports
- Updated test configurations to reflect the new default behavior
- Added comprehensive test coverage for merging overlapping entries

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| ReventsConversionService.kt | Added useInterestDistribution = false to scenario settings with explanatory comment |
| ReventsConversionServiceTest.kt | Updated test scenario settings to include useInterestDistribution = false |
| EntriesMergeV2ServiceTest.kt | Added new test case and utility imports for testing merge behavior of overlapping entries |
