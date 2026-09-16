---
id: github:teqplay/poma-backend:pr:224
source: github
type: pull_request
repo: teqplay/poma-backend
number: 224
title: TCC-233 Poma swagger documentation
author: TeqJoostD
state: closed
date: '2026-01-30'
merged_at: null
base_branch: develop
head_branch: TCC-233
url: https://github.com/teqplay/poma-backend/pull/224
labels: []
linked_issues: []
explicit_links:
- jira:TCC-233
---
# PR #224: TCC-233 Poma swagger documentation

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/224  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-233`  
**Created:** 2026-01-30  

## Description

_No description._

## Commits

- `ab37a756` **TeqJoostD** (2026-01-29): Add swagger documentation
- `1ec8fc3b` **TeqJoostD** (2026-01-29): request
- `c79f4151` **TeqJoostD** (2026-01-30): formatting
- `96c51ea5` **TeqJoostD** (2026-01-30): Formatting

## Reviews

### github-actions[bot] — COMMENTED (2026-01-30)

The PR adds comprehensive Swagger/OpenAPI documentation to infrastructure controllers. The documentation is well-structured and consistent across most controllers.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-30)

## Pull request overview

This pull request adds comprehensive Swagger/OpenAPI documentation to infrastructure controllers in the POMA application to improve API documentation and developer experience.

**Changes:**
- Created a new `ApiRequestBody` type alias to avoid conflicts between Swagger and Spring annotations
- Added detailed `@Operation`, `@Parameter`, and `@ApiResponse` annotations to all infrastructure controller endpoints
- Enhanced `@Tag` descriptions for better API categorization

### Reviewed changes

Copilot reviewed 13 out of 13 changed files in this pull request and generated 10 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |

| ---- | ----------- |

| src/main/kotlin/nl/teqplay/poma/common/ApiRequestBody.kt | New type alias for Swagger's RequestBody annotation to prevent naming conflicts with Spring's annotation |

| src/main/kotlin/nl/teqplay/poma/generics/InfrastructureController.kt | Added comprehensive Swagger annotations including operation summaries, parameter descriptions, and response codes for the base infrastructure controller |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt | Added Swagger documentation for terminal management endpoints including CRUD operations, imports, and maintenance scripts |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt | Added Swagger documentation for port management endpoints with detailed parameter descriptions and enhanced tag description |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/pilotboardingplace/PilotBoardingPlaceController.kt | Added Swagger documentation for pilot boarding place endpoints with enhanced tag description |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/lock/LockController.kt | Added Swagger documentation for lock management endpoints |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customarea/CustomAreaController.kt | Added Swagger documentation for custom area endpoints with enhanced tag description |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/breakwater/BreakWaterAreaController.kt | Added Swagger documentation for breakwater area endpoints with enhanced tag description |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt | Added Swagger documentation for berth management endpoints including import and maintenance operations |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/basin/BasinController.kt | Added Swagger documentation for basin management endpoints with enhanced tag description |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/approachroute/ApproachRouteController.kt | Added Swagger documentation for approach route endpoints |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/approacharea/ApproachAreaController.kt | Added Swagger documentation for approach area endpoints |

| src/main/kotlin/nl/teqplay/poma/feature/infrastructure/anchorage/AnchorageController.kt | Added Swagger documentation for anchorage endpoints with import functionality |
</details>






---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### github-actions[bot] — COMMENTED (2026-01-30)

Review completed. Found two issues that need to be addressed: incorrect annotation usage in TerminalController and LockController.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-30)

Review completed. Found one critical bug that needs to be fixed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

## Review Comments

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalController.kt`

The annotation `@PathVariable` is incorrect for this parameter. Since this is a GET request and the parameter is not part of the URL path, it should use `@RequestParam` instead. The endpoint mapping is `/script/recalculate/ports` with no path variable placeholder.
```suggestion
        @RequestParam overwrite: Boolean = false,
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/lock/LockController.kt`

Inconsistent request body documentation style. The `@ApiRequestBody` annotation is placed at the method level, while all other infrastructure controllers in this PR place it directly on the parameter (along with Spring's `@RequestBody` annotation). For consistency with the rest of the codebase, move this annotation to the parameter level and add the `required = true` attribute like in other controllers.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/approacharea/ApproachAreaController.kt`

Missing `required` attribute in `@ApiRequestBody` annotation. For consistency with InfrastructureController and other parts of this PR, add `required = true` to this annotation since the request body is mandatory for import operations.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/approachroute/ApproachRouteController.kt`

Missing `required` attribute in `@ApiRequestBody` annotation. For consistency with InfrastructureController and other parts of this PR, add `required = true` to this annotation since the request body is mandatory for import operations.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/berth/BerthController.kt`

Missing `required` attribute in `@ApiRequestBody` annotations. For consistency with InfrastructureController and other parts of this PR, add `required = true` to these annotations since the request bodies are mandatory for import operations.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/port/PortController.kt`

Missing `required` attribute in `@ApiRequestBody` annotation. For consistency with InfrastructureController and other parts of this PR, add `required = true` to this annotation since the request body is mandatory.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/lock/LockController.kt`

Inconsistent parameter documentation style. This controller uses method-level `@Parameter` annotations with the `name` attribute, while all other infrastructure controllers in this PR use parameter-level annotations (placed directly on the parameter, without the `name` attribute). For consistency with the rest of the codebase, consider using parameter-level annotations like in TerminalController, PortController, and other controllers.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customarea/CustomAreaController.kt`

Missing `required` attribute in `@ApiRequestBody` annotation. For consistency with InfrastructureController and other parts of this PR (e.g., TerminalController, PilotBoardingPlaceController, BreakWaterAreaController, BasinController), add `required = true` to this annotation since the request body is mandatory for import operations.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/anchorage/AnchorageController.kt`

Missing `required` attribute in `@ApiRequestBody` annotations. For consistency with InfrastructureController and other parts of this PR, add `required = true` to these annotations since the request bodies are mandatory for import operations.
