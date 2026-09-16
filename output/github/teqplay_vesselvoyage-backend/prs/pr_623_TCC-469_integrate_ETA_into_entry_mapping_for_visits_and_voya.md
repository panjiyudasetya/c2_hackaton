---
id: github:teqplay/vesselvoyage-backend:pr:623
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 623
title: TCC-469 integrate ETA into entry mapping for visits and voyages
author: Jamie-de-Leest
state: closed
date: '2025-10-03'
merged_at: '2025-10-03'
base_branch: develop
head_branch: TCC-469-add-eta-to-entry-mapper
url: https://github.com/teqplay/vesselvoyage-backend/pull/623
labels: []
linked_issues: []
explicit_links: []
---
# PR #623: TCC-469 integrate ETA into entry mapping for visits and voyages

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/623  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `TCC-469-add-eta-to-entry-mapper`  
**Created:** 2025-10-03  
**Merged:** 2025-10-03  

## Description

_No description._

## Commits

- `24ee777d` **Jamie de Leest** (2025-10-03): feat: integrate ETA into entry mapping for visits and voyages
- `a5d23f5d` **Jamie de Leest** (2025-10-03): test: fix wrong tests
- `dab600cb` **Jamie de Leest** (2025-10-03): refactor: change database calls to batch calls when possible
- `157df2c3` **Jamie de Leest** (2025-10-03): refactor: rename and add missing batch calls
- `ee97f871` **Jamie de Leest** (2025-10-03): chore: ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-03)

## Pull Request Overview

This PR integrates ETA information into entry mapping for visits and voyages by introducing a new wrapper approach that combines entries with their ESoF (Electronic Statement of Facts) data to include destination port ETA information.

- Replaced direct entry-to-API mapping with wrapper-based mapping that includes ESoF data
- Added destination port ETA field to API models using ESoF's trueDestinationEta
- Removed journal-related code as part of the refactoring

### Reviewed Changes

Copilot reviewed 14 out of 14 changed files in this pull request and generated 9 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| ChangesPublisherServiceTest.kt | Updated test calls to use new wrapper-based mapper method |
| EntryV2MapperTest.kt | Added comprehensive tests for both visit and voyage mapping with and without ESoF data |
| ChangesPublisherService.kt | Updated to use new wrapper-based entry mapping method |
| ProcessingFrontendViewV2Service.kt | Modified to create ESoF wrappers for all entry mappings |
| EntryV2Mapper.kt | Refactored mapping methods to accept ESoF wrapper instead of direct entries |
| ApiVoyageV2Controller.kt | Updated to fetch ESoF data and create wrappers before mapping |
| ApiVisitV2Controller.kt | Updated to fetch ESoF data and create wrappers before mapping |
| ApiJournalV2Controller.kt | Removed entire journal controller as part of refactoring |
| ApiEntryV2Controller.kt | Updated to use wrapper-based mapping approach |
| JournalItem.kt | Removed journal item model |
| JournalItemByImoResponse.kt | Removed journal response model |
| JournalItemByImoRequest.kt | Removed journal request model |
| JournalItem.kt (api) | Removed API journal item model |
</details>

### Darius-Wattimena — APPROVED (2025-10-03)

_No comment._

## Review Comments

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt`

Multiple database calls to fetch ESoF data in a loop could create an N+1 query problem. Consider batching the ESoF lookups by collecting all entry IDs first, then fetching them in a single query.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt`

Multiple database calls to fetch ESoF data in a loop could create an N+1 query problem. Consider batching the ESoF lookups by collecting all entry IDs first, then fetching them in a single query.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingFrontendViewV2Service.kt`

Multiple database calls to fetch ESoF data in a loop could create an N+1 query problem. Consider batching the ESoF lookups by collecting all entry IDs first, then fetching them in a single query.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

Multiple database calls to fetch ESoF data in mapping functions could create an N+1 query problem. Consider batching the ESoF lookups for all voyages before mapping.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

Multiple database calls to fetch ESoF data in mapping functions could create an N+1 query problem. Consider batching the ESoF lookups for all voyages before mapping.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

Multiple database calls to fetch ESoF data in mapping functions could create an N+1 query problem. Consider batching the ESoF lookups for all voyages before mapping.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

Multiple database calls to fetch ESoF data in mapping functions could create an N+1 query problem. Consider batching the ESoF lookups for all visits before mapping.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

Multiple database calls to fetch ESoF data in mapping functions could create an N+1 query problem. Consider batching the ESoF lookups for all visits before mapping.

### Copilot — 2025-10-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

Multiple database calls to fetch ESoF data in mapping functions could create an N+1 query problem. Consider batching the ESoF lookups for all entries before mapping.
