---
id: github:teqplay/vesselvoyage-backend:pr:507
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 507
title: SPV-2617 Support PortReporter SOF view for API and vesselvoyageclient
author: leonjoosse
state: closed
date: '2025-05-19'
merged_at: '2025-05-22'
base_branch: develop
head_branch: SPV-2617-portreporter-sof-view-api-and-client
url: https://github.com/teqplay/vesselvoyage-backend/pull/507
labels: []
linked_issues: []
explicit_links: []
---
# PR #507: SPV-2617 Support PortReporter SOF view for API and vesselvoyageclient

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/507  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2617-portreporter-sof-view-api-and-client`  
**Created:** 2025-05-19  
**Merged:** 2025-05-22  

## Description

(summary by copilot)

Key updates include extending the `StatementOfFactsViewName` enum, adding detailed documentation for methods in the `VesselVoyageClient`, and refactoring API controllers to improve reusability and remove hardcoded constraints.

### Enum and Model Updates:
* Added a new `PORTREPORTER` value to the `StatementOfFactsViewName` enum to support additional view types. (`api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/StatementOfFactsViewName.kt`)

### Client Enhancements:
* Introduced comprehensive documentation for the `VesselVoyageClient` class, detailing its purpose and available methods. (`client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`)

### API Controller Refactoring:
* Updated `ApiStatementOfFactsV2Controller` to remove hardcoded constraints for the `PTO` view, enabling support for additional view types like `PORTREPORTER`. (`src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`) [[1]](diffhunk://#diff-8d1217e4600ad9dfd25716e37f8eba360bdb7fec55c8335bdfc4d7f82ca8727aL54-R57) [[2]](diffhunk://#diff-8d1217e4600ad9dfd25716e37f8eba360bdb7fec55c8335bdfc4d7f82ca8727aL76-R73) [[3]](diffhunk://#diff-8d1217e4600ad9dfd25716e37f8eba360bdb7fec55c8335bdfc4d7f82ca8727aL109-R100)
* Refactored `findByImo` and `findByPort` methods in `BaseApiV2Controller` to use a mapper function, improving reusability across API controllers. (`src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt`) [[1]](diffhunk://#diff-5763eb3a5705baf9aa457caf3631a0bfe7b792c71e725815db82492da9b6cd38L20-R20) [[2]](diffhunk://#diff-5763eb3a5705baf9aa457caf3631a0bfe7b792c71e725815db82492da9b6cd38L62-L66)

### Other Improvements:
* Simplified mapping logic in `ApiVisitV2Controller` and `ApiVoyageV2Controller` by delegating to mapper functions, reducing redundancy. (`src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`, `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`) [[1]](diffhunk://#diff-0aca2b5dab78f145f984842e0d3db8c3a8bfa6f615063068a45b9eac0df50535L75-R84) [[2]](diffhunk://#diff-c16c3cb94479ab886acc9d7fdfdd32770d00bab3384e1f26334ec0054b0b89e3L80-R88)

## Commits

- `223a8083` **leonj** (2025-05-16): Add documentation for VesselVoyageClient
- `1fe4ab47` **leonj** (2025-05-19): Merge branch 'SPV-2616-portreporter-sof-view' into SPV-2617-portreporter-sof-view-api-and-client
- `c603f8f1` **leonj** (2025-05-19): Extend API with portreporter SOF
- `de1666c7` **leonj** (2025-05-19): Generalize produce methods for SOF views. Change BaseApiV2Controller to better accommodate mapping the result.
- `a963fd09` **leonj** (2025-05-19): For now, only publish PTO SOF. Publishing the portreporter SOF via rabbitmq will be addressed later in a separate PR, as it includes a breaking change.
- `da8692ca` **Leon Joosse** (2025-05-19): Merge branch 'develop' into SPV-2617-portreporter-sof-view-api-and-client
- `d1b0a918` **Leon Joosse** (2025-05-20): Merge branch 'develop' into SPV-2617-portreporter-sof-view-api-and-client

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-19)

## Pull Request Overview

This PR introduces support for the PortReporter SOF view and refactors methods to handle a generic StatementOfFacts view, allowing for both PTO and PORTREPORTER use cases. Key changes include:  
- Updating EsofV2Service methods to accept a StatementOfFactsViewName parameter and delegate to the correct generator.  
- Adjusting tests and mocks in ChangesPublisherServiceTest to reflect new argument order and method names.  
- Modifying API controllers and client documentation to use mapper lambdas and support the extended view functionality.

### Reviewed Changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherServiceTest.kt | Updated test mocks to use the new produce method with reordered parameters. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherService.kt | Replaced producePtoView calls with produce(PTO, …) to publish PTO SOFs. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/api/EsofV2Service.kt | Refactored production of SOF views to support both PTO and PORTREPORTER and introduced findPreviousPortAreaId. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt, ApiVoyageV2Controller.kt, ApiVisitV2Controller.kt, ApiStatementOfFactsV2Controller.kt | Adjusted mapping functions and endpoint responses to accommodate lambda-based mapping and generic view production. |
| client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt | Expanded documentation in the client for improved clarity on service methods and parameters. |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/StatementOfFactsViewName.kt | Added the PORTREPORTER view option alongside PTO. |
</details>



<details>
<summary>Comments suppressed due to low confidence (3)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/service/publisher/ChangesPublisherServiceTest.kt:57**
* Verify that the reordering of parameters in the produce method is correctly handled in the test's invocation answer. Ensure that the indices used in invocation.getArgument() reflect the new argument order.
```
whenever(esofV2Service.produce(eq(PTO), any<NewVisit>(), anyOrNull<NewESoF>())).thenAnswer { invocation ->
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/api/EsofV2Service.kt:53**
* [nitpick] Confirm that using findPreviousPortAreaId within the produce method for the PTO view meets the generator's requirements, and verify that no additional parameters are needed if further view types are introduced in the future.
```
fun produce(view: StatementOfFactsViewName, visit: NewVisit, esof: NewESoF?): StatementOfFactsView {
```
**src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt:57**
* [nitpick] Ensure that the removal of the strict PTO check is intentional. If the endpoint is now meant to support multiple views, update the documentation accordingly.
```
return esofV2Service.produce(view, visitId)
```
</details>

### Darius-Wattimena — APPROVED (2025-05-20)

_No comment._
