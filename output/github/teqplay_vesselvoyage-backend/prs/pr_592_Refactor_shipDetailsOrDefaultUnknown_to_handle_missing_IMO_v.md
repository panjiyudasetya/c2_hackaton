---
id: github:teqplay/vesselvoyage-backend:pr:592
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 592
title: Refactor shipDetailsOrDefaultUnknown to handle missing IMO values
author: TeqJoostD
state: closed
date: '2025-08-18'
merged_at: '2025-08-18'
base_branch: develop
head_branch: develop-cache-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/592
labels: []
linked_issues: []
explicit_links: []
---
# PR #592: Refactor shipDetailsOrDefaultUnknown to handle missing IMO values

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/592  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `develop-cache-hotfix`  
**Created:** 2025-08-18  
**Merged:** 2025-08-18  

## Description

_No description._

## Commits

- `0db00c43` **TeqJoostD** (2025-08-18): Refactor shipDetailsOrDefaultUnknown to handle missing IMO values

## Reviews

### Darius-Wattimena — APPROVED (2025-08-18)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-18)

## Pull Request Overview

This PR refactors the `shipDetailsOrDefaultUnknown` method to ensure that ship details always include an IMO value when one is provided, even if the retrieved ship details don't contain it.

- Extracts ship details retrieval into a variable for better code organization
- Adds logic to set the IMO field from the input parameter when it's missing in the retrieved details

## Review Comments

### Copilot — 2025-08-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

The code attempts to call `toString()` on a nullable `Int?` parameter. This will fail with a NullPointerException if `imo` is null. The condition should check if `imo` is not null before calling `toString()`.
```suggestion
            details.copy(imo = imo?.toString() ?: "")
```

### Copilot — 2025-08-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

There's a typo in the method name `getCachyByMmsi`. It should be `getCacheByMmsi` to match the naming pattern used in the line above.
```suggestion
            ?: mmsi?.let { shipCacheService.getCacheByMmsi(it.toString())?.csi?.register?.toShipDetails() }
```
