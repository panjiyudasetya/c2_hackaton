---
id: github:teqplay/vesselvoyage-backend:pr:522
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 522
title: 'TCC-137: extend byPort API endpoints with DWT / TEU filter (only when category
  present)'
author: leonjoosse
state: closed
date: '2025-06-02'
merged_at: '2025-06-05'
base_branch: develop
head_branch: TCC-137-filter-category-and-dwt-teu
url: https://github.com/teqplay/vesselvoyage-backend/pull/522
labels: []
linked_issues: []
explicit_links: []
---
# PR #522: TCC-137: extend byPort API endpoints with DWT / TEU filter (only when category present)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/522  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `TCC-137-filter-category-and-dwt-teu`  
**Created:** 2025-06-02  
**Merged:** 2025-06-05  

## Description

This pull request refactors the API model and controller classes to introduce a new interface, `ShipPropertyFilterRequest`, which standardizes filtering by ship properties such as categories, DWT, and TEU. It also updates various request and response classes to implement this interface, ensuring consistent handling of ship-related filters across the application. Additionally, it replaces the previous filtering logic with a new utility function, `filterByShipCategoryAndRange`, to improve maintainability and readability.

The filter is added to the following endpoints:

```
/v2/sof/byPort
/v2/visits/byPort
/v2/voyages/byPort
```

and works together with the already existing `categories` parameter:
- The `TEU` range is used for ships with category `CONTAINER`.
- The `DWT` range is used for ships with other categories.

## Commits

- `12f5a3fc` **leonj** (2025-05-28): Pass finished property for voyage by port call to underlying service/database layer
- `139bbff9` **leonj** (2025-06-02): Add support for filtering by minTeu-maxTeu / minDwt-maxDwt to byPort requests in the V2 visits / voyages / sof APIs
- `4d72cf75` **leonj** (2025-06-02): Merge branch 'develop' into TCC-135-visit-by-ais-destination
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt
- `5e348268` **leonj** (2025-06-03): Remove unrelated byAisTrueDestination implementation
- `c08a85c0` **leonj** (2025-06-03): Remove too aggressive CONTAINER + minTeu/maxTeu check
- `1ba48f87` **leonj** (2025-06-03): Also validate dwt/teu in ApiStatementOfFactsV2Controller.byPort()
- `4d54b157` **leonj** (2025-06-03): Extend visit and SOF byPort with aisTrueDestination (NewEntry.destination.actual), which is the resolved unlocode of the AIS destination entered by the captain
- `c779aa7d` **leonj** (2025-06-03): Tighten when DWT/TEU can be used
- `da0879aa` **leonj** (2025-06-04): Remove duplicate validation
- `ed7f8358` **Leon Joosse** (2025-06-04): Merge pull request #523 from teqplay/TCC-134-visits-ais-destination
  TCC-134: Extend visit and SOF byPort with aisTrueDestination filter
- `d6bbcd08` **leonj** (2025-06-04): Fix a bug in querying start/end times in the NewEntryDataSource
- `07cf7303` **leonj** (2025-06-04): Fix a bug in querying start/end times in the NewEntryDataSource (update method docs)
- `88ecb4ee` **leonj** (2025-06-05): Add dwt/teu filters to VesselVoyageClient

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-02)

Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting a review.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-02)

## Pull Request Overview

This PR extends the byPort endpoints to support optional DWT/TEU filtering alongside existing category filters by introducing a new `ShipPropertyFilterRequest`, updating models/controllers, and centralizing logic in a utility function.

- Introduce `ShipPropertyFilterRequest` and add `minDwt`/`maxDwt`/`minTeu`/`maxTeu` to request DTOs  
- Replace old per-category IMO filtering with `filterByShipCategoryAndRange` in controllers  
- Add `findByAisTrueDestination` to `EntryV2Service` and controllers, plus corresponding data source methods

### Reviewed Changes

Copilot reviewed 13 out of 13 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File                                                        | Description                                                             |
| ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/EntryUtilsTest.kt      | Add parameterized tests for TEU/DWT filtering permutations              |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt          | Implement and document `filterByShipCategoryAndRange` utility          |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/EntryV2Service.kt | Add `findByAisTrueDestination` combining visits and voyages            |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt | Query voyages by AIS true destination (`.eq("aisTrueDestination.unlocode")`) |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt  | Query visits by AIS true destination                                   |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt | Wire in `ShipPropertyFilterRequest`, add validation and filtering helper |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt | Add DWT/TEU params and apply new filter in voyage endpoint            |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt  | Add DWT/TEU params and apply new filter in visit endpoint             |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt | Add DWT/TEU params and apply new filter in SOF endpoint               |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt | Add `/byAisTrueDestination` endpoint                                   |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VoyagesByPortRequest.kt | Extend voyages request interface with DWT/TEU fields                   |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/ShipPropertyFilterRequest.kt | Introduce new filter interface                                         |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/ByPortRequest.kt | Update ByPortRequest to implement `ShipPropertyFilterRequest`           |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt:915**
* The Javadoc tag uses `@param maxDwd` for the TEU description but should reference `@param maxTeu`. Update the tag and description accordingly.
```
* @param maxDwd Maximum TEU of the ship. When [minTeu] is set, but [maxTeu] not, it becomes Int.MAX_VALUE.
```
</details>

### leonjoosse — COMMENTED (2025-06-03)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-06-03)

_No comment._

### Darius-Wattimena — DISMISSED (2025-06-03)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-06-04)

_No comment._

### Darius-Wattimena — DISMISSED (2025-06-04)

_No comment._

### Darius-Wattimena — APPROVED (2025-06-05)

_No comment._

## Review Comments

### Copilot — 2025-06-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt`

The TEU validation logic is inverted: it throws when TEU filters are provided for CONTAINER instead of when they are missing. It should throw only if category CONTAINER is selected and both minTeu and maxTeu are null.
```suggestion
        if (categories != null && categories.contains(CONTAINER) && minTeu == null && maxTeu == null) {
            throw BadRequestException("minTeu and maxTeu must be set when category CONTAINER is selected")
```

### Copilot — 2025-06-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

The DWT filter branch also applies to CONTAINER ships when dwtRange is set. Change the condition to exclude CONTAINER, e.g., `shipCategory != CONTAINER && dwtRange != null`.
```suggestion
            shipCategory != CONTAINER && dwtRange != null -> categoryMatches && ship.dwt() in dwtRange
```

### Copilot — 2025-06-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

Unlike other endpoints, this controller does not call `validateDwtTeu(request)` before filtering. Add a validation call to ensure DWT/TEU parameters are checked consistently.

### leonjoosse — 2025-06-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

Nice catch, added it.

### Darius-Wattimena — 2025-06-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt`

Don't we also have to check if both DWT and TEU are not provided? like I would expect to only have DWT for non-containers, and TEU for containers?

### Darius-Wattimena — 2025-06-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

remove this

## Comments

### leonjoosse — 2025-06-03

Okay, I made some improvements, its now really ready for review.
