---
id: github:teqplay/vesselvoyage-backend:pr:589
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 589
title: Add paginated endpoints for retrieving all data without filtering
author: TeqJoostD
state: closed
date: '2025-08-13'
merged_at: '2025-08-13'
base_branch: develop
head_branch: TCC-294
url: https://github.com/teqplay/vesselvoyage-backend/pull/589
labels: []
linked_issues: []
explicit_links: []
---
# PR #589: Add paginated endpoints for retrieving all data without filtering

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/589  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-294`  
**Created:** 2025-08-13  
**Merged:** 2025-08-13  

## Description

_No description._

## Commits

- `a7f17f05` **TeqJoostD** (2025-08-13): Add paginated endpoints for retrieving all data without filtering
- `cbb784e1` **Joost Dambrink** (2025-08-13): Merge branch 'develop' into TCC-294
- `3bac04cb` **Joost Dambrink** (2025-08-13): Update src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-13)

## Pull Request Overview

This PR adds paginated endpoints for retrieving all data from the database without any filtering. The implementation bypasses the existing limited status filtering and other constraints to provide access to the complete dataset.

Key changes:
- Added pagination methods to base service and data source layers
- Created a new controller with paginated endpoints for visits and statement of facts
- Extended the client library with paginated API support

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| BaseApiV2Service.kt | Added service methods for paginated data retrieval without filtering |
| NewEntryDataSource.kt | Implemented data source methods for unfiltered pagination queries |
| BaseApiDataSource.kt | Added interface methods for pagination support |
| ApiPaginatedDataController.kt | New controller providing paginated endpoints for visits and statement of facts |
| VesselVoyageClient.kt | Extended client with paginated API methods |
| PaginatedResponse.kt | New data models for paginated API responses |
</details>

### Darius-Wattimena — DISMISSED (2025-08-13)

_No comment._

### Darius-Wattimena — APPROVED (2025-08-13)

_No comment._

## Review Comments

### Copilot — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/BaseApiV2Service.kt`

The skip calculation logic is duplicated from the existing getLimitedEntries method. Consider extracting this calculation into a private helper method to avoid code duplication.
```suggestion
        val skip = calculateSkip(page, pageSize)
```

### Copilot — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

Using `Any` as the first generic type parameter seems inappropriate. This should be a more specific type that represents the API model for this controller.
```suggestion
) : BaseApiV2Controller<Visit, NewVisit, NewVisitDataSource, VisitV2Service>(visitV2Service, shipService) {
```

### Copilot — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

[nitpick] The total pages calculation logic could be extracted to a utility class or made part of PaginationMetadata itself, as this is a common calculation that might be reused elsewhere.
```suggestion
/**
 * Calculates the total number of pages based on total elements and page size.
 */
fun calculateTotalPages(totalElements: Long, pageSize: Int): Long {
    return if (totalElements == 0L) 0L else (totalElements + pageSize - 1) / pageSize
}
}
```

### Copilot — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

The documentation mentions 'finished and confirmed parameters' but these parameters are not present in the actual endpoint methods. This documentation is misleading and should be corrected.
```suggestion
 * Note: There are no 'finished' or 'confirmed' parameters in these endpoints; all entries are returned.
```
