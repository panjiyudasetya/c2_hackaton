---
id: github:teqplay/vesselvoyage-backend:pr:523
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 523
title: 'TCC-134: Extend visit and SOF byPort with aisTrueDestination filter'
author: leonjoosse
state: closed
date: '2025-06-03'
merged_at: '2025-06-04'
base_branch: TCC-137-filter-category-and-dwt-teu
head_branch: TCC-134-visits-ais-destination
url: https://github.com/teqplay/vesselvoyage-backend/pull/523
labels: []
linked_issues: []
explicit_links: []
---
# PR #523: TCC-134: Extend visit and SOF byPort with aisTrueDestination filter

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/523  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `TCC-137-filter-category-and-dwt-teu` ← `TCC-134-visits-ais-destination`  
**Created:** 2025-06-03  
**Merged:** 2025-06-04  

## Description

This pull request introduces support for filtering by `aisTrueDestination` in various API endpoints and services. The changes include modifications to request models, controllers, data sources, and service classes to handle the new filter parameter. Below is a summary of the most important changes grouped by theme.

### API Enhancements

* Added `aisTrueDestination` as a new request parameter in the `byPort` and `findByPort` methods of `ApiStatementOfFactsV2Controller` and `ApiVisitV2Controller`. This allows users to filter results based on the actual AIS destination. 

* Updated the `ByPortRequest` model to include the `aisTrueDestination` field, ensuring the parameter is passed through the request object.


## Commits

- `4d54b157` **leonj** (2025-06-03): Extend visit and SOF byPort with aisTrueDestination (NewEntry.destination.actual), which is the resolved unlocode of the AIS destination entered by the captain

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-03)

## Pull Request Overview

This PR adds support for filtering by aisTrueDestination across various endpoints and services.  
- Updated service methods (VisitV2Service.kt) to propagate the aisTrueDestination parameter.  
- Modified data source queries (NewVisitDataSource.kt and NewEntryDataSource.kt) to include filtering based on aisTrueDestination.  
- Enhanced API controllers (ApiVisitV2Controller.kt and ApiStatementOfFactsV2Controller.kt) and the ByPortRequest model to accept the new parameter.

### Reviewed Changes

Copilot reviewed 6 out of 6 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt | Added aisTrueDestination parameter to service calls for visit queries. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt | Updated the query filters to include aisTrueDestination. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt | Introduced a new helper function to build the aisTrueDestination query filter. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt | Added request parameter aisTrueDestination to the visit endpoint. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt | Integrated the aisTrueDestination parameter into the statement-of-facts endpoint. |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/ByPortRequest.kt | Extended ByPortRequest to include aisTrueDestination. |
</details>

### Darius-Wattimena — APPROVED (2025-06-03)

_No comment._

## Review Comments

### Copilot — 2025-06-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt`

[nitpick] Consider adding a brief comment to explain the expected format or behavior of 'aisTrueDestination', as its transformation may affect filtering.

### Copilot — 2025-06-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

[nitpick] Consider adding a comment clarifying why the 'aisTrueDestination' value is converted to uppercase, which will aid future maintenance and ensure clarity on data expectations.
