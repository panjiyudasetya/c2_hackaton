---
id: github:teqplay/vesselvoyage-backend:pr:630
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 630
title: Hotfix 8 Oct 2025
author: Darius-Wattimena
state: closed
date: '2025-10-08'
merged_at: '2025-10-08'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/630
labels: []
linked_issues: []
explicit_links: []
---
# PR #630: Hotfix 8 Oct 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/630  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-10-08  
**Merged:** 2025-10-08  

## Description

_No description._

## Commits

- `b4c0ce18` **Darius Wattimena** (2025-10-08): Refactor distinctIdsFinished to use find with projection to avoid the mongo 16MB limit
- `a050edc8` **Darius Wattimena** (2025-10-08): Merge pull request #629 from teqplay/TCC-434-fix-distinct-ids
  TCC-434 fix distinct ids

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-08)

## Pull Request Overview

This hotfix addresses a MongoDB limitation by replacing a `distinct` query with a `find` query to avoid the 16MB result size limit when retrieving finished entry IDs.

- Replaced `distinct` operation with `find` and projection to handle large result sets
- Added `IdOnly` data class for type-safe projection results
- Added necessary import for the `include` projection function

## Review Comments

### Copilot — 2025-10-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

[nitpick] The `IdOnly` data class is only used within the `distinctIdsFinished()` method. Consider moving it inside the method as a local data class to better encapsulate its usage and reduce the class scope.
