---
id: github:teqplay/vesselvoyage-backend:pr:683
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 683
title: TCC-563 fix visit by port api
author: Darius-Wattimena
state: closed
date: '2025-12-11'
merged_at: '2025-12-16'
base_branch: develop
head_branch: TCC-563-fix-visit-by-port-api
url: https://github.com/teqplay/vesselvoyage-backend/pull/683
labels: []
linked_issues: []
explicit_links: []
---
# PR #683: TCC-563 fix visit by port api

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/683  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-563-fix-visit-by-port-api`  
**Created:** 2025-12-11  
**Merged:** 2025-12-16  

## Description

1. Adds functionality for finding Visit by AIS destination which is needed for SmartFleet.
2. Added a new index for the VisitV2 collection to make this call possible.
3. Add controller unit testing for Visit, Voyage and SOF endpoints (which should cover all important V2 endpoints).
4. Added some missing validation in all 3 controllers to match expected behaviour.

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

## Reviews

### github-actions[bot] — COMMENTED (2025-12-11)

Review completed. Found several potential issues that should be addressed.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-11)

## Pull request overview

This pull request adds functionality to find visits by AIS true destination (required for SmartFleet integration), introduces comprehensive controller unit testing for V2 API endpoints, and adds validation logic to ensure consistent error handling across Visit, Voyage, and Statement of Facts controllers.

**Key Changes:**
- Added `findByAisTrueDestination` method with corresponding database index for efficient queries on the VisitV2 collection
- Introduced comprehensive unit tests for ApiVoyageV2Controller, ApiVisitV2Controller, and ApiStatementOfFactsV2Controller with 2,234 lines of test coverage
- Added centralized validation methods in BaseApiV2Controller for time range and port identifier validation

### Reviewed changes

Copilot reviewed 10 out of 10 changed files in this pull request and generated 6 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| ApiVoyageV2ControllerTest.kt | New test file with 667 lines covering all voyage endpoints including GET/POST by ID, IMO, and port |
| ApiVisitV2ControllerTest.kt | New test file with 910 lines covering all visit endpoints including new AIS true destination functionality |
| ApiStatementOfFactsV2ControllerTest.kt | New test file with 657 lines covering SOF endpoints with various filtering options |
| VisitV2Service.kt | Added findByAisTrueDestination service method delegating to data source |
| NewVisitDataSource.kt | Added findByAisTrueDestination query method and new compound index on destination.actual field |
| NewEntryDataSource.kt | Refactored AIS true destination query logic into reusable methods |
| BaseApiV2Controller.kt | Added validateTimeRange and validatePortIdentifiers helper methods for consistent validation |
| ApiVoyageV2Controller.kt | Integrated time range validation calls in byImo and byPort endpoints |
| ApiVisitV2Controller.kt | Added AIS true destination support with validation in byPort endpoints |
| ApiStatementOfFactsV2Controller.kt | Added AIS true destination support with validation in byPort endpoints |
</details>

### github-actions[bot] — COMMENTED (2025-12-11)

Review completed. Found several potential issues that should be addressed.

### github-actions[bot] — COMMENTED (2025-12-11)

Review completed. I found one potential bug in the data source implementation that could cause incorrect query results.

### github-actions[bot] — COMMENTED (2025-12-11)

Review completed. Found one potential bug in the data source implementation that could cause incorrect query results.

### github-actions[bot] — COMMENTED (2025-12-11)

## Code Review Summary

I've completed a comprehensive review of this PR. The implementation looks solid overall with good test coverage and proper validation. I found one inconsistency in sorting logic between the Visit and Voyage controllers that should be addressed for consistency.

### Key Findings:

✅ **Good practices observed:**
- Comprehensive unit test coverage for all new functionality
- Proper validation of input parameters
- Consistent error handling and messaging
- Well-structured MongoDB index for AIS destination queries
- Security annotations properly applied

⚠️ **Issue found:**
- Inconsistent sorting implementation between ApiVisitV2Controller and ApiVoyageV2Controller

The new AIS destination functionality is well-implemented and follows the existing patterns in the codebase. The MongoDB index addition is appropriate for the new query pattern.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-11)

Review completed. No suggestions at this time.

### github-actions[bot] — COMMENTED (2025-12-11)

Review completed. No suggestions at this time.

### michel-teqplay — DISMISSED (2025-12-11)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-15)

Review completed. The code changes look solid overall with good test coverage and proper validation. The new AIS destination functionality is well-implemented with appropriate database indexes.

### github-actions[bot] — COMMENTED (2025-12-15)

Review completed. The PR demonstrates solid engineering practices with comprehensive testing, proper validation, and good code organization. The new AIS destination functionality is well-implemented with appropriate database indexing for performance.

### github-actions[bot] — COMMENTED (2025-12-15)

Review completed. The PR successfully adds AIS true destination functionality with comprehensive test coverage and proper validation. The implementation follows established patterns and maintains consistency across the codebase.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — DISMISSED (2025-12-16)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-16)

Review completed. The PR adds comprehensive functionality for AIS destination filtering and includes thorough unit testing. The implementation follows established patterns and includes proper validation. No suggestions at this time.

### michel-teqplay — APPROVED (2025-12-16)

_No comment._

## Review Comments

### Copilot — 2025-12-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

The query filter for AIS true destination is being added twice. Line 90 already adds the filter via `queryAisTrueDestination(aisTrueDestination)`, which internally creates `NewEntry::destination / Destination::actual eq aisTrueDestination.uppercase()`. Line 91 then duplicates this exact same filter. Remove line 91 to avoid adding duplicate filters to the query.
```suggestion
            // Removed duplicate AIS true destination filter
```

### Copilot — 2025-12-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt`

Missing the call to `add()` before `queryFinishedFilter(finished)` on line 93. The filter is being created but not added to the list. It should be wrapped with `?.let(::add)` or use `add()` directly like line 69 does. Similarly, line 94 should also use `add()` for consistency with line 70.
```suggestion
            add(queryFinishedFilter(finished))
            add(queryConfirmedFilter(confirmed))
```

### Copilot — 2025-12-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/BaseApiV2Controller.kt`

The error message contains grammatically incorrect text. "Provide at least 1 identifier is required" should be "At least 1 identifier is required" or "Provide at least 1 identifier". Remove the redundant "Provide" or "is required".
```suggestion
            throw BadRequestException("At least 1 identifier is required to find visits. Provide an unlocode, areaId or trueDestination")
```

### Copilot — 2025-12-11 on `src/test/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2ControllerTest.kt`

This test contains debug code that should be removed. Lines 312-322 appear to be debugging code with a println statement, and the actual test is duplicated in lines 324-333. Remove the debug section (lines 312-322) and keep only the actual test assertions.
```suggestion

```

## Comments
