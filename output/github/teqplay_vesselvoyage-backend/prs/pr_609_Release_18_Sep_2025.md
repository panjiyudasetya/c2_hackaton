---
id: github:teqplay/vesselvoyage-backend:pr:609
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 609
title: Release 18 Sep 2025
author: Darius-Wattimena
state: closed
date: '2025-09-18'
merged_at: '2025-09-18'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/609
labels: []
linked_issues: []
explicit_links: []
---
# PR #609: Release 18 Sep 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/609  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-09-18  
**Merged:** 2025-09-18  

## Description

_No description._

## Commits

- `3f0273f7` **Darius Wattimena** (2025-09-18): Fix null handling for IMO in PtoStatementOfFactsViewGenerator and add test for shipToShip transfer
- `e8d32749` **Darius Wattimena** (2025-09-18): Merge pull request #608 from teqplay/fix-broken-api
  Fix broken API call when ship-to-ship vessel doesn't have an IMO

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-18)

## Pull Request Overview

This release includes a bug fix for ship-to-ship transfer generation when ships have null IMO values. The change prevents a potential NullPointerException by safely handling null IMO values in the `PtoStatementOfFactsViewGenerator`.

- Fixed null pointer exception when processing ship details with null IMO values
- Added test coverage to verify the fix handles null IMO scenarios correctly

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| PtoStatementOfFactsViewGenerator.kt | Fixed null pointer exception by adding safe null handling for IMO values |
| PtoStatementOfFactsViewGeneratorTest.kt | Added test case to verify null IMO handling doesn't throw exceptions |

## Review Comments

### Copilot — 2025-09-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

The condition checks if `details.imo` is null or equals \"null\", but then assigns `imo?.toString()` which could still result in a null value. This creates inconsistent behavior where the condition suggests we want to replace null/\"null\" values, but the assignment might still produce null. Consider using `imo?.toString() ?: \"\"` or handle the null case explicitly.
```suggestion
            details.copy(imo = imo?.toString() ?: "")
```
