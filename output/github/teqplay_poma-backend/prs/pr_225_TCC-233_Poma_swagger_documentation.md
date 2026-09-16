---
id: github:teqplay/poma-backend:pr:225
source: github
type: pull_request
repo: teqplay/poma-backend
number: 225
title: TCC-233 Poma swagger documentation
author: TeqJoostD
state: closed
date: '2026-01-30'
merged_at: '2026-02-04'
base_branch: develop
head_branch: TCC-233
url: https://github.com/teqplay/poma-backend/pull/225
labels: []
linked_issues: []
explicit_links: []
---
# PR #225: TCC-233 Poma swagger documentation

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/225  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-233`  
**Created:** 2026-01-30  
**Merged:** 2026-02-04  

## Description

_No description._

## Commits

- `ab37a756` **TeqJoostD** (2026-01-29): Add swagger documentation
- `1ec8fc3b` **TeqJoostD** (2026-01-29): request
- `c79f4151` **TeqJoostD** (2026-01-30): formatting
- `96c51ea5` **TeqJoostD** (2026-01-30): Formatting

## Reviews

### github-actions[bot] — COMMENTED (2026-01-30)

Review completed. Found one critical bug that needs to be fixed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — COMMENTED (2026-01-30)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-30)

## Pull request overview

This PR adds comprehensive Swagger/OpenAPI documentation to the POMA infrastructure controllers, improving API discoverability and documentation. The changes introduce a new `ApiRequestBody` type alias to avoid naming conflicts between Spring's `@RequestBody` and Swagger's `RequestBody` annotations, and systematically adds `@Operation`, `@Parameter`, `@ApiResponse`, and tag descriptions across all infrastructure controllers.

**Changes:**
- Created `ApiRequestBody` type alias for Swagger's RequestBody annotation
- Added detailed Swagger documentation to the base `InfrastructureController` covering CRUD operations
- Enhanced 11 infrastructure controllers with comprehensive API documentation including operations summaries, parameter descriptions, and response codes

### Reviewed changes

Copilot reviewed 13 out of 13 changed files in this pull request and generated 21 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/poma/common/ApiRequestBody.kt | Introduces type alias to resolve annotation naming conflicts |
| src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt | Adds comprehensive Swagger documentation for base CRUD operations |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt | Documents terminal management endpoints with search, filtering, and administrative operations |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt | Documents port management endpoints with extensive filtering and data maintenance operations |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/pilotboardingplace/PilotBoardingPlaceController.kt | Documents pilot boarding place endpoints with filtering and import capabilities |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/lock/LockController.kt | Documents lock management endpoints with comprehensive filtering |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customarea/CustomAreaController.kt | Documents custom area endpoints with import from VesselMatcher |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/breakwater/BreakWaterAreaController.kt | Documents breakwater area endpoints with platform import |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt | Documents berth management endpoints with import and maintenance operations |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/basin/BasinController.kt | Documents basin endpoints with filtering and import capabilities |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/approachroute/ApproachRouteController.kt | Documents approach route endpoints with data science import |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/approacharea/ApproachAreaController.kt | Documents approach area endpoints with platform import |
| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/anchorage/AnchorageController.kt | Documents anchorage endpoints with multiple import sources |
</details>






---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### TeqJoostD — COMMENTED (2026-02-04)

_No comment._

### michel-teqplay — APPROVED (2026-02-04)

_No comment._

## Review Comments

### TeqJoostD — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt`

not my problem

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. Other similar methods in this file have this annotation (e.g., getByUnLoCodeList at line 127, getBerthMappedPorts at line 139). The success response should be documented for API consistency.
```suggestion
    )
    @ApiResponse(
        responseCode = "200",
        description = "Successful retrieval of known UN/LOCODEs",
        content = [Content(mediaType = MediaType.APPLICATION_JSON_VALUE)],
    )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. Data maintenance operations in this file should document their success response for API consistency, especially since similar operations at lines 198, 209, 220, and 231 document access control failures but not success responses.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. The operation documents the 403 response but not the success case, which is inconsistent with the pattern used in other administrative operations.
```suggestion
    )
    @ApiResponse(responseCode = "200", description = "Display names filled successfully", content = [Content()])
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt`

Missing @ApiResponse annotation for the 200 success response. Other methods in this file document their success responses (e.g., lines 50, 94, 118, 132), so this should be consistent.
```suggestion
    )
    @ApiResponse(responseCode = "200", description = "Successfully retrieved all terminal group names")
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. All similar data maintenance operations should document their success response for consistency.
```suggestion
    )
    @ApiResponse(
        responseCode = "200",
        description = "EOS areas fixed successfully",
    )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt`

The @PathVariable annotation is incorrect here. The parameter 'overwrite' should be annotated with @RequestParam since it's defined as a query parameter with a default value, not a path variable. The endpoint path '/script/recalculate/ports' doesn't contain an 'overwrite' path segment.
```suggestion
        @RequestParam(name = "overwrite", required = false, defaultValue = "false") overwrite: Boolean,
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt`

The Parameter annotations are placed on the method instead of on the actual parameters. In Swagger annotations, @Parameter should be placed directly on each @RequestParam parameter. This is inconsistent with the pattern used in other methods in the same file (e.g., lines 182-184) where @Parameter is correctly placed on the parameters themselves.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt`

The description incorrectly states "Sets display names to empty for all berths". Based on the method name 'setEmptyDisplayNames' and the pattern from similar methods in PortController (line 217), this operation should "set display names for berths that have empty display names", not set them to empty.
```suggestion
        description = "Sets display names for berths that have empty display names in the system",
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. The operation documents the 403 response but not the success case, which is inconsistent with the pattern used in other administrative operations.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. The operation documents the 403 response but not the success case, which is inconsistent with the pattern used in other administrative operations.
```suggestion
    )
    @ApiResponse(responseCode = "200", description = "Main port links fixed successfully")
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt`

Inconsistent capitalization in description. "ID" should be "id" to match the pattern used in other descriptions throughout the file (e.g., lines 144, 180, 212 which use "external ID").
```suggestion
    @ApiResponse(responseCode = "409", description = "A model with this external id already exists in the database", content = [Content()])
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. The operation documents the 403 response but not the success case, which is inconsistent with the pattern used in other administrative operations.
```suggestion
    )
    @ApiResponse(responseCode = "200", description = "Display names set successfully", content = [Content()])
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. All similar data maintenance operations should document their success response for consistency.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt`

Spelling error: "Conscious" should be "consciousness" or more appropriately, this should be "confirmation" or "acknowledgment". The phrase "conscious flag" is not idiomatic in English for API parameters. Consider using "confirmationFlag" or simply describing it as "Flag to confirm the operation".
```suggestion
        @Parameter(description = "Flag to confirm the operation")
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt`

Inconsistent spacing in multi-line description. There's a missing space after the comma in "if false,". All other multi-line parameter descriptions in this file have consistent spacing after punctuation (e.g., lines 85, 105, 125).
```suggestion
                "Filter by validation status. If true, counts only validated objects; if false, " +
                    "counts only non-validated objects; if null, counts all objects",
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/approacharea/ApproachAreaController.kt`

Missing @ApiResponse annotation for the 200 success response. All other getAll methods in the controllers have this annotation (e.g., AnchorageController line 37, BasinController line 39, BreakWaterAreaController line 39). This is inconsistent with the pattern established in this PR.
```suggestion
    )
    @ApiResponse(responseCode = "200", description = "Successfully retrieved approach areas")
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. All other getAll methods with pagination parameters in the controllers have this annotation (e.g., TerminalController line 50, BerthController line 49). This is inconsistent with the documentation pattern established in this PR.
```suggestion
    )
    @ApiResponse(
        responseCode = "200",
        description = "Successfully retrieved list of ports matching the provided filters",
    )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. This is inconsistent with the pattern used in other similar methods in this file (e.g., getAll at line 85, getBerthMappedPorts at line 139). The success response should be documented for consistency.
```suggestion
    )
    @ApiResponse(
        responseCode = "200",
        description = "Ports retrieved successfully",
        content = [Content(mediaType = MediaType.APPLICATION_JSON_VALUE)],
    )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. All similar data maintenance operations should document their success response for consistency.
```suggestion
    )
    @ApiResponse(
        responseCode = "200",
        description = "Main ports within sub-ports successfully defined",
        content = [Content()],
    )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing @ApiResponse annotation for the 200 success response. The operation documents the 403 response but not the success case, which is inconsistent with the pattern used in other administrative operations.
```suggestion
    )
    @ApiResponse(responseCode = "200", description = "Display names capitalization started", content = [Content()])
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/lock/LockController.kt`

The Parameter annotations are placed on the method instead of on the actual parameters. In Swagger annotations, @Parameter should be placed directly on each @RequestParam parameter, not as separate method-level annotations. This prevents proper OpenAPI documentation generation for these parameters.

### TeqJoostD — 2026-02-04 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/lock/LockController.kt`

Makes it more readable IMO this way
