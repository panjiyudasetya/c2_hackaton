---
id: github:teqplay/vesselvoyage-backend:pr:685
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 685
title: Release 17 Dec 2025
author: Darius-Wattimena
state: closed
date: '2025-12-16'
merged_at: '2025-12-17'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/685
labels: []
linked_issues: []
explicit_links: []
---
# PR #685: Release 17 Dec 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/685  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-12-16  
**Merged:** 2025-12-17  

## Description

_No description._

## Commits

- `40228bd5` **Darius Wattimena** (2025-12-08): Add support for querying visits by AIS true destination only when doing a byPort request
- `92063d89` **Darius Wattimena** (2025-12-08): Add unit tests for ApiVisitV2Controller to validate visit retrieval by ID, IMO or port
- `c5ab9b65` **Darius Wattimena** (2025-12-08): Adjusted existing controllers to validate the provided ports for visit and sof and timerange for all
- `5ac8d76b` **Darius Wattimena** (2025-12-08): code cleanup
- `18f308b6` **Darius Wattimena** (2025-12-11): Merge branch 'develop' into TCC-563-fix-visit-by-port-api
- `68a3847e` **Darius Wattimena** (2025-12-11): Add unit tests for ApiVoyageV2Controller to validate voyage retrieval by ID, IMO and port
- `cde540af` **Darius Wattimena** (2025-12-11): Add unit tests for ApiStatementOfFactsV2Controller to validate SOF retrieval by ID, IMO and port as well
- `0f31edc6` **Darius Wattimena** (2025-12-11): ktlint
- `99e446f4` **Darius Wattimena** (2025-12-11): Validate port identifier input in ApiVisitV2Controller to ensure only one is provided and improve error message
- `a987e92d` **Darius Wattimena** (2025-12-11): Make consistent with Visit API byPort
- `0903aa56` **Darius Wattimena** (2025-12-11): Remove unreachable else branch and instead return an empty response
- `485aa3b9` **Darius Wattimena** (2025-12-11): Removed unneeded duplicate filter
- `b59e28f0` **Darius Wattimena** (2025-12-11): Remove unneeded checks as they are done in the validatePortIdentifiers from the BaseApiV2Controller
- `c336eece` **Darius Wattimena** (2025-12-11): ktlint
- `0a4511f0` **Darius Wattimena** (2025-12-15): Added an extra index for getting ongoing by destination faster
- `d3763f68` **Darius Wattimena** (2025-12-15): Refactor API controllers to include EsofV2Service and improve ongoing result filtering to be done by ship instead of all ships
- `88ca5bde` **Darius Wattimena** (2025-12-15): Clarify documentation for filterMultipleOngoing parameter in VisitByPortRequest and VoyagesByPortRequest
- `51d56838` **Darius Wattimena** (2025-12-16): ktlint
- `140b65dc` **Darius Wattimena** (2025-12-16): Merge pull request #683 from teqplay/TCC-563-fix-visit-by-port-api
  TCC-563 fix visit by port api
- `d7a372e5` **Darius Wattimena** (2025-12-16): Bump aisengine_version to master-2.8.0
- `7a5cca7f` **Darius Wattimena** (2025-12-16): Merge pull request #684 from teqplay/ais-engine-version
  Bump AisEngine version to master-2.8.0

## Reviews

### michel-teqplay — APPROVED (2025-12-16)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-16)

## Pull request overview

This PR introduces comprehensive API endpoints for querying voyages, visits, and statement of facts by AIS true destination, along with improved validation and code organization. The changes refactor shared filtering logic into a base controller and add extensive test coverage for the new API v2 endpoints.

Key changes:
- Added support for querying visits by AIS true destination
- Refactored duplicate filtering and validation logic into `BaseApiV2Controller`
- Added comprehensive test suites for three API controllers

### Reviewed changes

Copilot reviewed 15 out of 16 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2ControllerTest.kt` | New comprehensive test suite for voyage API endpoints covering various query scenarios and authorization |
| `src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2ControllerTest.kt` | New comprehensive test suite for visit API endpoints including AIS true destination queries |
| `src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2ControllerTest.kt` | New comprehensive test suite for statement of facts API endpoints |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt` | Added `findByAisTrueDestination` method to support AIS destination queries |
| `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt` | Added database indexes and `findByAisTrueDestination` query method |
| `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt` | Refactored AIS destination query methods to support both optional and required usage |
| `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt` | Extracted shared validation and filtering logic from controllers into reusable base methods |
| `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt` | Refactored to use base controller methods and added validation calls |
| `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt` | Refactored to use base controller methods and added AIS true destination support |
| `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt` | Refactored to use base controller methods and added AIS true destination support |
| `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt` | Updated constructor to pass esofV2Service to base controller |
| `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt` | Updated documentation for `filterMultipleOngoing` parameter |
| `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VoyagesByPortRequest.kt` | Improved documentation for `filterMultipleOngoing` parameter |
| `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VisitByPortRequest.kt` | Improved documentation for `filterMultipleOngoing` parameter |
| `api/build.gradle` | Updated aisengine_version from master-2.7.0 to master-2.8.0 |
</details>

### github-actions[bot] — COMMENTED (2025-12-16)

Review completed with several suggestions for improvement. The code changes look functionally correct but there are some inconsistencies and debugging code that should be addressed.

## Review Comments

### Copilot — 2025-12-16 on `src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2ControllerTest.kt`

Debug println statement should be removed before merging to production. This appears to be leftover debugging code that adds unnecessary console output.
```suggestion

```

### Copilot — 2025-12-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt`

The error message incorrectly refers to 'visits' specifically, but this validation method is used in a base controller that handles both visits and voyages. Consider using a more generic term like 'entries' or 'results'.
```suggestion
            0 -> throw BadRequestException("Missing port identifier. A port identifier is required to find entries, this can be an unlocode, areaId or aisTrueDestination")
```

### Copilot — 2025-12-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt`

The documentation should clarify that `sortedAscending` only affects sorting when `filterMultipleOngoing` is true and there are multiple IMO groups. The current description doesn't explain this conditional behavior.
