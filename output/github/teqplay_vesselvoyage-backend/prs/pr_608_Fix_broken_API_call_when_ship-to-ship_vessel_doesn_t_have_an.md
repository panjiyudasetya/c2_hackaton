---
id: github:teqplay/vesselvoyage-backend:pr:608
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 608
title: Fix broken API call when ship-to-ship vessel doesn't have an IMO
author: Darius-Wattimena
state: closed
date: '2025-09-18'
merged_at: '2025-09-18'
base_branch: develop
head_branch: fix-broken-api
url: https://github.com/teqplay/vesselvoyage-backend/pull/608
labels: []
linked_issues: []
explicit_links: []
---
# PR #608: Fix broken API call when ship-to-ship vessel doesn't have an IMO

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/608  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-broken-api`  
**Created:** 2025-09-18  
**Merged:** 2025-09-18  

## Description

_No description._

## Commits

- `3f0273f7` **Darius Wattimena** (2025-09-18): Fix null handling for IMO in PtoStatementOfFactsViewGenerator and add test for shipToShip transfer

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-18)

## Pull Request Overview

This PR fixes a bug where an API call failed when a ship-to-ship vessel doesn't have an IMO number. The fix ensures null IMO values are properly handled instead of causing exceptions.

- Changes nullable IMO handling to use safe call operator instead of direct toString()
- Adds test coverage for the ship-to-ship transfer scenario with null IMO

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| PtoStatementOfFactsViewGenerator.kt | Fixed null IMO handling by using safe call operator |
| PtoStatementOfFactsViewGeneratorTest.kt | Added test case to verify no exception is thrown when ship has null IMO |

### michel-teqplay — APPROVED (2025-09-18)

_No comment._

## Review Comments

### Copilot — 2025-09-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

The fix handles the case where `imo` is null, but the condition check on line 1031 already handles null IMO by checking `details.imo == null || details.imo == "null"`. If `imo` parameter is null here, calling `imo?.toString()` will result in `null`, which means the condition will be true again on the next call, potentially causing an infinite loop or unexpected behavior. Consider clarifying the logic or ensuring `imo` parameter validation.
