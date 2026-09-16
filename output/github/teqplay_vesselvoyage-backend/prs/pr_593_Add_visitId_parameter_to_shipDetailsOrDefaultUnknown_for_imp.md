---
id: github:teqplay/vesselvoyage-backend:pr:593
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 593
title: Add visitId parameter to shipDetailsOrDefaultUnknown for improved log
author: TeqJoostD
state: closed
date: '2025-08-18'
merged_at: '2025-08-18'
base_branch: develop
head_branch: develop-cache-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/593
labels: []
linked_issues: []
explicit_links: []
---
# PR #593: Add visitId parameter to shipDetailsOrDefaultUnknown for improved log

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/593  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `develop-cache-hotfix`  
**Created:** 2025-08-18  
**Merged:** 2025-08-18  

## Description

…ging

## Commits

- `0491e302` **TeqJoostD** (2025-08-18): Add visitId parameter to shipDetailsOrDefaultUnknown for improved logging

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-18)

## Pull Request Overview

This PR enhances logging capability by adding a `visitId` parameter to the `shipDetailsOrDefaultUnknown` method. This allows for better traceability when ship details cannot be retrieved properly.

- Added `visitId` parameter to `shipDetailsOrDefaultUnknown` method for improved logging context
- Updated all method calls to include the `visitId` parameter
- Added warning log when IMO is null to help with debugging

### Darius-Wattimena — APPROVED (2025-08-18)

_No comment._

## Review Comments

### Copilot — 2025-08-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

Method name 'getCachyByMmsi' appears to have a typo. Should this be 'getCacheByMmsi'?
```suggestion
            ?: mmsi?.let { shipCacheService.getCacheByMmsi(it.toString())?.csi?.register?.toShipDetails() }
```

### Copilot — 2025-08-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

The string comparison with "null" suggests potential data quality issues. Consider using a more explicit check or validating the data source to prevent string "null" values.
```suggestion
        return if (details.imo == null) {
```
