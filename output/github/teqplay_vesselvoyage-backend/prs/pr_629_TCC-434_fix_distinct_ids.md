---
id: github:teqplay/vesselvoyage-backend:pr:629
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 629
title: TCC-434 fix distinct ids
author: Darius-Wattimena
state: closed
date: '2025-10-08'
merged_at: '2025-10-08'
base_branch: develop
head_branch: TCC-434-fix-distinct-ids
url: https://github.com/teqplay/vesselvoyage-backend/pull/629
labels: []
linked_issues: []
explicit_links: []
---
# PR #629: TCC-434 fix distinct ids

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/629  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-434-fix-distinct-ids`  
**Created:** 2025-10-08  
**Merged:** 2025-10-08  

## Description

_No description._

## Commits

- `a0e760c4` **jamie-teqplay** (2025-10-03): Release 03-10-2025 Merge pull request #626 from teqplay/develop
  Release 03-10-2025
- `3e9e5843` **Darius Wattimena** (2025-10-08): Merge pull request #628 from teqplay/develop
  Release 8 Oct 2025
- `b4c0ce18` **Darius Wattimena** (2025-10-08): Refactor distinctIdsFinished to use find with projection to avoid the mongo 16MB limit

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-08)

## Pull Request Overview

This PR fixes an issue with retrieving distinct IDs from the database when the combined size of all IDs exceeds MongoDB's 16MB limit for distinct operations. The solution replaces the `distinct` query with a `find` query using projection to retrieve only the `_id` field.

- Replaced MongoDB `distinct` operation with `find` and projection to handle large result sets
- Added a private data class `IdOnly` to support type-safe projection
- Added necessary import for the `include` projection function

### michel-teqplay — APPROVED (2025-10-08)

_No comment._

## Review Comments

### Copilot — 2025-10-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

[nitpick] Consider moving the `IdOnly` data class outside the function or to a companion object to improve code organization and potential reusability.
