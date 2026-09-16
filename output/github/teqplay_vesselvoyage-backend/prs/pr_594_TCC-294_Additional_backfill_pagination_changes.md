---
id: github:teqplay/vesselvoyage-backend:pr:594
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 594
title: TCC-294 Additional backfill pagination changes
author: TeqJoostD
state: closed
date: '2025-08-18'
merged_at: '2025-08-19'
base_branch: develop
head_branch: TCC-294
url: https://github.com/teqplay/vesselvoyage-backend/pull/594
labels: []
linked_issues: []
explicit_links: []
---
# PR #594: TCC-294 Additional backfill pagination changes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/594  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-294`  
**Created:** 2025-08-18  
**Merged:** 2025-08-19  

## Description

_No description._

## Commits

- `c448325a` **TeqJoostD** (2025-08-14): Remove sorting
- `3ac4c93c` **TeqJoostD** (2025-08-14): Remove total count and total pages from pagination metadata
- `46dbe4eb` **TeqJoostD** (2025-08-14): Refactor paginated methods to support generic response types
- `f85101af` **TeqJoostD** (2025-08-14): Increase maximum page size to 1,000,000 for paginated data retrieval
- `c7f8d658` **TeqJoostD** (2025-08-15): Refactor pagination endpoints to use afterId and limit parameters for data retrieval
- `6bab837c` **TeqJoostD** (2025-08-18): Merge branch 'develop' into TCC-294
- `f20071c8` **TeqJoostD** (2025-08-18): Merge branch 'develop' into TCC-294
- `e24d020b` **TeqJoostD** (2025-08-18): Merge remote-tracking branch 'origin/develop' into TCC-294
- `fa993994` **TeqJoostD** (2025-08-18): Update documentation for pagination endpoints to reflect accurate object types

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-18)

## Pull Request Overview

This PR implements cursor-based pagination for backfill data endpoints, replacing the traditional page/size-based pagination with afterId/limit parameters. This change improves performance for large datasets by avoiding expensive skip operations in MongoDB.

- Replaces offset-based pagination with cursor-based pagination using MongoDB document IDs
- Consolidates two separate endpoints (`/pto-statement-of-facts` and `/visits`) into a single `/backfill-data` endpoint
- Updates pagination metadata to use cursor information instead of page counts

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| BaseApiV2Service.kt | Updates service method signature to use afterId/limit instead of page/pageSize parameters |
| NewEntryDataSource.kt | Implements cursor-based filtering using MongoDB _id field with proper sorting |
| BaseApiDataSource.kt | Updates interface to match new pagination method signature |
| ApiPaginatedDataController.kt | Consolidates endpoints and removes page-based validation logic |
| VesselVoyageClient.kt | Updates client method to match new API contract |
| PaginatedResponse.kt | Changes response structure to include specific visit/sof fields instead of generic data |
</details>

### Darius-Wattimena — APPROVED (2025-08-19)

_No comment._

## Review Comments

### Copilot — 2025-08-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

The filter logic could be simplified. When afterId is null, you can use an empty filter (Filters.empty()) instead of Filters.exists("_id"), since all MongoDB documents have an _id field by default.
```suggestion
        val filter = if (afterId == null) Filters.empty()
```

### Copilot — 2025-08-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

The afterId parameter should have input validation to ensure it's a valid MongoDB ObjectId format when provided, to prevent potential errors in the database query.

### Copilot — 2025-08-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

The limit parameter lacks validation constraints. Consider adding validation to ensure limit is positive and within reasonable bounds (e.g., max 1000) to prevent performance issues.
```suggestion
        @RequestParam @Min(1) @Max(1000) limit: Int,
```

### Copilot — 2025-08-18 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/PaginatedResponse.kt`

The PaginatedResponse is no longer generic but hardcoded to specific types (Visit and StatementOfFactsView). This breaks the reusability of the response class for other paginated endpoints that might exist or be added in the future.
```suggestion
data class PaginatedResponse<T>(
    val items: List<T>,
```

## Comments

### TeqJoostD — 2025-08-18

Please NOTE: All of this we be deleted
