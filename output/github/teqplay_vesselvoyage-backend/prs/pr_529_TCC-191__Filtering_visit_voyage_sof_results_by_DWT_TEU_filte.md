---
id: github:teqplay/vesselvoyage-backend:pr:529
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 529
title: 'TCC-191: Filtering visit/voyage/sof results by DWT/TEU filters is too slow'
author: leonjoosse
state: closed
date: '2025-06-05'
merged_at: '2025-06-16'
base_branch: develop
head_branch: TCC-191-dwt-teu-performance
url: https://github.com/teqplay/vesselvoyage-backend/pull/529
labels: []
linked_issues: []
explicit_links: []
---
# PR #529: TCC-191: Filtering visit/voyage/sof results by DWT/TEU filters is too slow

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/529  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `TCC-191-dwt-teu-performance`  
**Created:** 2025-06-05  
**Merged:** 2025-06-16  

## Description

Instead of filtering afterwards, select the list of IMOs upfront and use it in the database query.

## Commits

- `8f713816` **leonj** (2025-06-05): Filtering visit/voyage/sof results by DWT/TEU filters is too slow. Instead of filtering afterwards, select the list of IMOs upfront and use it in the database query
- `f017503b` **leonj** (2025-06-10): Test indexes for voyages
- `4caff79f` **leonj** (2025-06-10): Fix json sub types for VoyagesByPortRequest
- `dfbdb6de` **leonj** (2025-06-10): Make return types explicit in the VesselVoyageClient when calling the restTemplate methods, hopefully helps in resolving the mapping issues on the callers end
- `828197bb` **leonj** (2025-06-13): Rework the request and response data classes
- `3789e9f7` **leonj** (2025-06-13): Remove unused interface

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-05)

## Pull Request Overview

This PR optimizes the filtering of visit, voyage, and statement-of-facts results by selecting the list of qualifying IMOs upfront so that the database query handles TEU and DWT filtering rather than filtering after retrieval.
- Introduces a new parameter “qualifyingImos” to various service, datasource, and controller methods.
- Renames and refactors the filtering method from filterByShipCategoryAndRange (which returned a list) to shipMatchesCategoryAndOptionalRange (now a boolean predicate).
- Updates tests and controller logic to leverage the new pre-filtering mechanism.

### Reviewed Changes

Copilot reviewed 10 out of 10 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/EntryUtilsTest.kt | Adjusts test cases to verify boolean-based filtering logic. |
| src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt | Replaces the list filter method with a boolean evaluator for ship matching. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VoyageV2Service.kt | Adds the qualifyingImos parameter to voyage query methods. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt | Introduces qualifyingImos in visit query methods. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt | Incorporates the qualifyingImos filter into voyage datasource queries. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt | Integrates the qualifyingImos filter into visit datasource queries. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/*.kt | Updates controllers to utilize the new pre-filtering mechanism via qualifyingImos. |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt:87**
* [nitpick] The method name 'appenedEospSuffixIfNeeded' may contain a typo; consider renaming it to 'appendEospSuffixIfNeeded' for clarity.
```
add(NewVoyage::destinationPort `in` destinationPortAreaIds.appenedEospSuffixIfNeeded())
```
</details>

### leonjoosse — COMMENTED (2025-06-05)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-13)

## Pull Request Overview

This PR refactors the request and response models for port- and IMO-based queries to support a new filtering approach that selects the list of IMOs upfront for database queries. Key changes include renaming request/response classes (e.g. ByPortRequest → VisitByPortRequest, ByImoRequest → EntryByImoRequest), the introduction of new generic response types for StatementOfFacts views, and the removal of the old By*-prefixed classes.

### Reviewed Changes

Copilot reviewed 37 out of 37 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| VisitByPortResponse.kt | New response class for port-based visit queries |
| VisitByPortRequest.kt | Renamed from ByPortRequest; updated request model for port queries |
| VisitByImoResponse.kt | New response class for IMO-based visit queries |
| VisitByImoRequest.kt | New request model for IMO-based visit queries |
| VisitByImoLookAroundResponse.kt | New response class for look-around queries by IMO |
| VisitByImoLookAroundRequest.kt | Renamed from ByImoLookAroundRequest; updated request model for look-around queries |
| StatementOfFactsViewByPortResponse.kt | New generic response for port-based SOF view queries |
| StatementOfFactsViewByPortRequest.kt | New request model for port-based SOF view queries with ship filter properties |
| StatementOfFactsViewByImoResponse.kt | New generic response for IMO-based SOF view queries |
| StatementOfFactsViewByImoRequest.kt | New request model for IMO-based SOF view queries |
| StatementOfFactsViewByImoLookAroundResponse.kt | New generic response for IMO look-around queries for SOF views |
| StatementOfFactsViewByImoLookAroundRequest.kt | New request model for IMO look-around queries for SOF views |
| JournalItemByImoResponse.kt | New response for IMO-based journal item queries |
| JournalItemByImoRequest.kt | New request model for IMO-based journal item queries |
| EntryByImoResponse.kt | New response for IMO-based entry queries |
| EntryByImoRequest.kt | Renamed from ByImoRequest; updated request model for entry queries |
| EntryBasedRequest.kt | New interfaces defining common request properties based on entry filtering |
| ByPortResponse.kt, ByImoResponse.kt, ByImoLookAroundResponse.kt | Removed deprecated classes |
</details>

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-16)

## Pull Request Overview

This PR aims to improve performance by filtering results upstream in the database query rather than post-filtering, thereby reducing the overhead associated with DWT/TEU filters. Key changes include:
- Addition of new request/response data classes for Voyage, Visit, Entry, and StatementOfFacts endpoints.
- Renaming of previously generic endpoints (e.g. ByPort/ByImo) to more descriptive names.
- Removal of outdated generic response classes.

### Reviewed Changes

Copilot reviewed 36 out of 36 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| VoyageByImoRequest.kt | Introduces a new request model for voyages filtered by IMO. |
| VisitByPortResponse.kt, VisitByPortRequest.kt | Updates and renames port-related endpoints for clarity. |
| VisitByImoResponse.kt, VisitByImoRequest.kt, VisitByImoLookAroundResponse.kt, VisitByImoLookAroundRequest.kt | Defines request/response models for visit endpoints, including look-around capabilities. |
| StatementOfFactsViewByPort*.kt, StatementOfFactsViewByImo*.kt, StatementOfFactsViewByImoLookAround*.kt | Introduces request/response models for Statement of Facts views with filtering parameters. |
| JournalItemByImo*.kt | Implements request/response models for journal item retrieval by IMO. |
| EntryByImoResponse.kt, EntryByImoRequest.kt | Renames and clarifies IMO endpoints for entry data. |
| ByPortResponse.kt, ByImoResponse.kt, ByImoLookAroundResponse.kt | Removes outdated generic response classes. |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/EntryByImoRequest.kt:10**
* [nitpick] Consider clarifying the naming distinction between 'EntryByImoRequest' and similar classes such as 'VisitByImoRequest' if they serve different purposes, to ensure consistency and reduce potential confusion.
```
data class EntryByImoRequest(
```
</details>

### TeqJoostD — APPROVED (2025-06-16)

_No comment._

## Review Comments

### leonjoosse — 2025-06-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt`

Had to move this to the controllers, because this service should not start selecting qualifying IMOs...
