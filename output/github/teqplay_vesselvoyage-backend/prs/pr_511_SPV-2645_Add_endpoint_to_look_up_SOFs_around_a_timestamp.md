---
id: github:teqplay/vesselvoyage-backend:pr:511
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 511
title: SPV-2645 Add endpoint to look up SOFs around a timestamp
author: leonjoosse
state: closed
date: '2025-05-22'
merged_at: '2025-05-23'
base_branch: develop
head_branch: SPV-2645-sof-endpoint-lookaround
url: https://github.com/teqplay/vesselvoyage-backend/pull/511
labels: []
linked_issues: []
explicit_links: []
---
# PR #511: SPV-2645 Add endpoint to look up SOFs around a timestamp

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/511  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2645-sof-endpoint-lookaround`  
**Created:** 2025-05-22  
**Merged:** 2025-05-23  

## Description

This pull request introduces a new feature to support querying ship-related data by IMO (International Maritime Organization number) with a "look around" functionality. It includes changes to define request and response models, update the client and controller logic, and implement the necessary database query methods. Below is a summary of the most important changes grouped by theme.

### New Models for Request and Response

* Added `ByImoLookAroundRequest` data class to represent the request parameters for querying ship data by IMO, including fields for `timestamp`, `limit`, `finished`, and `confirmed` filters. 
* Added `ByImoLookAroundResponse` generic data class to encapsulate the request and the resulting data list. 

### Client Enhancements

* Updated `VesselVoyageClient` to include a new method `findByImoLookAround` for making requests to the "look around" API endpoint. This method supports filtering by timestamp, limit, finished state, and confirmation status. 

### Controller Updates

* Added a new API endpoint `/byImo/{imo}/lookaround` in `ApiStatementOfFactsV2Controller` to handle "look around" requests. This endpoint validates the request, queries the service layer, and returns the response. 

### Database Query Implementation

* Implemented the `findByImoLookAround` method in `NewVisitDataSource` to query the database based on IMO, timestamp, limit, finished state, and confirmation status. The method dynamically adjusts filters and sorting based on the direction of the query (past or future).

### Service Layer Support

* Added `findByImoLookAround` method in `VisitV2Service` to bridge the controller and data source layers, passing the query parameters and returning the results. 

## Commits

- `a777715e` **leonj** (2025-05-22): Add endpoint to look up SOFs around a timestamp, and a positive/negative limit to return items after/before the timestamp respectively
- `fec8d6e6` **leonj** (2025-05-22): Fix query
- `c19b1e2c` **Leon Joosse** (2025-05-22): Fix required timestamp and limit
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `625fd78b` **Leon Joosse** (2025-05-22): Update docs
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `fdbcb57b` **leonj** (2025-05-22): Add test
- `e7aecb7b` **leonj** (2025-05-23): Remove commented code from a test, remove qualifier for mock function

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-22)

## Pull Request Overview

Adds a “look around” endpoint for fetching SOFs by IMO around a given timestamp.

- Introduces `ByImoLookAroundRequest`/`Response` models  
- Exposes `/byImo/{imo}/lookaround` in the controller and client  
- Implements service and data‐source logic with time‐based filtering

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File                                                     | Description                                                        |
| -------------------------------------------------------- | ------------------------------------------------------------------ |
| service/api/VisitV2Service.kt                            | Added `findByImoLookAround` service method                         |
| datasource/NewVisitDataSource.kt                         | Implemented DB query with timestamp filters and limit handling     |
| controller/api/ApiStatementOfFactsV2Controller.kt        | Exposed new GET `/byImo/{imo}/lookaround` endpoint                 |
| client/src/.../VesselVoyageClient.kt                     | Added client method for lookaround endpoint                        |
| apiv2/model/requestresponse/ByImoLookAroundRequest.kt    | New request data class                                             |
| apiv2/model/requestresponse/ByImoLookAroundResponse.kt   | New response data class                                            |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/ByImoLookAroundRequest.kt:11**
* [nitpick] The request model does not include the `view` parameter even though the controller accepts it. Consider adding `view: StatementOfFactsViewName` to the request so the response reflects all input parameters consistently.
```
data class ByImoLookAroundRequest(
```
</details>

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-22)

## Pull Request Overview

Adds a “look around” feature for querying SOFs by IMO at a given timestamp, allowing retrieval of entries before or after that time.  
- Introduced request/response models (`ByImoLookAroundRequest`/`ByImoLookAroundResponse`).  
- Exposed new controller endpoint and client method for look-around queries.  
- Implemented service and datasource logic with dynamic filters and sorting.

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| VisitV2Service.kt | Added `findByImoLookAround` service method delegating to the datasource |
| NewVisitDataSource.kt | Implemented database query and sorting logic in `findByImoLookAround` |
| ApiStatementOfFactsV2Controller.kt | Added `/byImo/{imo}/lookaround` endpoint and mapping logic |
| VesselVoyageClient.kt | Added client wrapper `findByImoLookAround` method |
| ByImoLookAroundRequest.kt | Defined request data class with timestamp, limit, finished, confirmed |
| ByImoLookAroundResponse.kt | Defined response data class wrapping request and result list |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/ByImoLookAroundRequest.kt:28**
* [nitpick] The description for `finished` is confusing: change 'ongoing finished' to 'finished entries' and 'ongoing entries' to 'unfinished entries' for clarity.
```
*     * Pass `true` for only ongoing finished, `false` for only ongoing entries, or `null` for both.
```
**src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt:88**
* New endpoint added; consider adding unit and integration tests for the `findByImoLookAround` controller action to ensure parameter validation and response mapping.
```
@GetMapping("/byImo/{imo}/lookaround")
```
</details>

### Darius-Wattimena — CHANGES_REQUESTED (2025-05-22)

_No comment._

### leonjoosse — COMMENTED (2025-05-22)

_No comment._

### leonjoosse — COMMENTED (2025-05-23)

_No comment._

### Darius-Wattimena — APPROVED (2025-05-23)

_No comment._

## Review Comments

### Copilot — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

Using a negative `limit` directly in `.limit(limit)` may cause runtime errors or unexpected behavior. Use `Math.abs(limit)` when `limit` is negative.

### Copilot — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

The sort direction is always descending, so future queries (limit > 0) will return newest first. Consider using ascending sort when `limit > 0` to preserve chronological order for upcoming entries.
```suggestion
            .let { query ->
                if (limit > 0) {
                    query.ascendingSort(NewEntry::start / LocationTime::time)
                } else {
                    query.descendingSort(NewEntry::start / LocationTime::time)
                }
            }
```

### Copilot — 2025-05-22 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/ByImoLookAroundRequest.kt`

[nitpick] The description for `finished` is confusing and contains a typo. Clarify that `true` filters only finished visits, `false` filters only ongoing visits, and `null` returns both.
```suggestion
     * - `true` = only finished entries
     * - `false` = only ongoing entries
     * - `null` = both finished and ongoing entries
```

### Copilot — 2025-05-22 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

The `timestamp` and `limit` parameters are optional in the client but are required by the API endpoint. Change them to non-nullable to match the controller contract.
```suggestion
            timestamp: Instant,
            limit: Int,
```

### Copilot — 2025-05-22 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

[nitpick] The method parameters `timestamp: Instant? = null` and `limit: Int? = null` are declared nullable, but the controller requires them. Consider making these non-nullable to enforce required parameters at compile time.
```suggestion
            timestamp: Instant,
            limit: Int,
```

### Copilot — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

[nitpick] Sorting uses `NewEntry::start` while filters use `NewVisit::start`. For consistency and clarity, use the same model reference (`NewVisit::start`) in both filter and sort expressions.
```suggestion
            query.ascendingSort(NewVisit::start / LocationTime::time)
        } else {
            // looking back (past), so sort the result set descending to get the items closest to the timestamp
            query.descendingSort(NewVisit::start / LocationTime::time)
```

### Darius-Wattimena — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

Would be nice to cover this by a test. Feels a bit hard for me to now know if this sorting is actually working as intended.

### Darius-Wattimena — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

This build list isn't even needed as all filters are all non-nullable? You can just do:
```kotlin
val filters = and(
   NewVisit::imo eq imo,
   timestampFilter,
   ..
)
```

### leonjoosse — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

Yeah, indeed. I had an if-else statement inside the buildList, but then decided to change it.

### leonjoosse — 2025-05-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

You're right. Now thinking about it, this would be commentary I would give as well 😛 

### leonjoosse — 2025-05-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

Can't of course test the sorting behavior of Mongo in a unit test, but can at least test that the function is using the right operator
