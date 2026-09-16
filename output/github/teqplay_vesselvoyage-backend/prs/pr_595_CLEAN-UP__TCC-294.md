---
id: github:teqplay/vesselvoyage-backend:pr:595
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 595
title: '[CLEAN-UP] TCC-294 '
author: TeqJoostD
state: closed
date: '2025-08-18'
merged_at: '2025-08-22'
base_branch: develop
head_branch: TCC-294-cleanup
url: https://github.com/teqplay/vesselvoyage-backend/pull/595
labels: []
linked_issues: []
explicit_links: []
---
# PR #595: [CLEAN-UP] TCC-294 

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/595  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-294-cleanup`  
**Created:** 2025-08-18  
**Merged:** 2025-08-22  

## Description

_No description._

## Commits

- `d11a2435` **TeqJoostD** (2025-08-18): cleanup: backfill cleanup
- `a8ca6e8f` **TeqJoostD** (2025-08-18): cleanup: remove unused countAllEntries method and related documentation
- `26c9c156` **TeqJoostD** (2025-08-19): cleanup: remove unused AutoTimeoutHealthIndicator from health configurations
- `0f4ad895` **TeqJoostD** (2025-08-19): cleanup: add AutoTimeoutHealthIndicator to health configurations

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-18)

## Pull Request Overview

This PR removes unused pagination functionality from the codebase, specifically the paginated endpoints for retrieving all data without filtering. The changes clean up code that was likely introduced for data backfill purposes but is no longer needed.

Key changes:
- Removed the entire `ApiPaginatedDataController` that provided paginated access to all visits and statement of facts
- Eliminated the `countAllEntries()` method from the data access layer since it's no longer referenced
- Removed client-side support for the paginated endpoints

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| BaseApiV2Service.kt | Removed `countAllEntries()` method from the service layer |
| NewEntryDataSource.kt | Removed `countAllEntries()` implementation from the data source |
| BaseApiDataSource.kt | Removed `countAllEntries()` method from the interface definition |
| ApiPaginatedDataController.kt | Complete removal of the pagination controller |
| VesselVoyageClient.kt | Removed pagination client support and related documentation |
| PaginatedResponse.kt | Removed pagination response models |
</details>

### Darius-Wattimena — DISMISSED (2025-08-19)

_No comment._

### Darius-Wattimena — APPROVED (2025-08-22)

_No comment._
