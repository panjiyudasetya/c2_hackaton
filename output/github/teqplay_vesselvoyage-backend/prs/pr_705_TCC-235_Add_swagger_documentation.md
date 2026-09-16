---
id: github:teqplay/vesselvoyage-backend:pr:705
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 705
title: TCC-235 Add swagger documentation
author: TeqJoostD
state: closed
date: '2026-01-30'
merged_at: '2026-02-04'
base_branch: develop
head_branch: TCC-235
url: https://github.com/teqplay/vesselvoyage-backend/pull/705
labels: []
linked_issues: []
explicit_links: []
---
# PR #705: TCC-235 Add swagger documentation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/705  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-235`  
**Created:** 2026-01-30  
**Merged:** 2026-02-04  

## Description

_No description._

## Commits

- `47e46f1e` **TeqJoostD** (2026-01-30): Add swagger documentation
- `6b9d7baa` **Joost Dambrink** (2026-01-30): Merge branch 'develop' into TCC-235
- `f9f2e1e8` **TeqJoostD** (2026-01-30): add missing endpoints
- `efe1155b` **TeqJoostD** (2026-01-30): Merge remote-tracking branch 'origin/TCC-235' into TCC-235
- `1f445ba3` **TeqJoostD** (2026-02-04): Merge branch 'develop' into TCC-235

## Reviews

### github-actions[bot] — COMMENTED (2026-01-30)

This PR adds comprehensive Swagger/OpenAPI documentation to the V2 API controllers, which will improve API discoverability and usability. However, there's a significant breaking change (removal of `/byShipId` endpoints from visits) that should be highlighted in the PR description.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-30)

This PR adds comprehensive Swagger/OpenAPI documentation to the V2 API controllers. The documentation is generally well-structured and provides clear descriptions for endpoints and parameters. I have a few suggestions for improvement.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-30)

## Pull request overview

Adds Swagger/OpenAPI annotations (tags, operations, parameters, and response docs) to several V2 API controllers to improve generated API documentation.

**Changes:**
- Annotated V2 controllers with `@Tag`, `@Operation`, `@Parameter`, and `@ApiResponses`.
- Added request-body descriptions for batch endpoints via Swagger `@RequestBody` (aliased).
- Modified `ApiVisitV2Controller` endpoints (notably, `/byShipId` mappings appear removed).

### Reviewed changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 8 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt | Adds Swagger metadata for voyage endpoints and query parameters. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt | Adds Swagger metadata, but also removes public `/byShipId` visit endpoints. |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt | Adds Swagger metadata for SOF endpoints (visit/IMO/port variants). |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt | Adds Swagger metadata for entry endpoints and batch request bodies. |

### github-actions[bot] — COMMENTED (2026-01-30)

Review completed. No suggestions at this time.

### TeqJoostD — COMMENTED (2026-02-04)

_No comment._

### TeqJoostD — COMMENTED (2026-02-04)

_No comment._

### TeqJoostD — COMMENTED (2026-02-04)

_No comment._

### TeqJoostD — COMMENTED (2026-02-04)

_No comment._

### TeqJoostD — COMMENTED (2026-02-04)

_No comment._

### TeqJoostD — COMMENTED (2026-02-04)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-04)

Review completed. The Swagger documentation additions are comprehensive and well-structured across all four controllers. However, I noticed that the `ApiStatementOfFactsV2Controller` has two endpoints that were not documented in this PR:

**Missing Documentation:**
- `GET /v2/sof/byShipId/{shipId}` (line 96)
- `POST /v2/sof/byShipId` (line 120)

For consistency with the rest of this PR, these endpoints should also receive `@Operation`, `@Parameter`, and `@ApiResponses` annotations similar to the other documented endpoints.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — APPROVED (2026-02-04)

_No comment._

## Review Comments

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

The PR title indicates Swagger documentation changes, but this controller removes the public /byShipId/{shipId} and POST /byShipId endpoints for visits. This is a breaking API change and also leaves the existing private findByShipId(VisitByShipIdRequest) helper unused. If the endpoints should remain supported, restore the mappings; if the removal is intentional, update the PR description/changelog and remove now-dead code paths to avoid confusion.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

This endpoint returns null when an entry is not found (because it just returns entryV2Service.findEntry(...)?). Other controllers in v2 throw NotFoundException for missing resources, and v1 entries return 404. Consider returning 404 here as well (e.g., throw NotFoundException or return ResponseEntity.notFound()) so clients don’t get a 200 with an empty body.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

The Swagger description implies clients must choose either start+end or last, but the current implementation accepts start+end+last and silently ignores last (time-range branch wins). Either enforce mutual exclusivity with a 400 (consistent with BaseApiV2Controller.findByImoBase/findByShipIdBase) or update the documentation to describe the precedence behavior.

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

These parameters are nullable; when omitted they are treated as “no filter” (finished=both, confirmed=all). The current descriptions only document true/false cases, which is misleading for Swagger consumers. Update the descriptions to explicitly document the null semantics (as done in ApiVisitV2Controller).
```suggestion
        @Parameter(
            description = "Filter by entry completion status. True for finished entries only, false for ongoing only. When omitted or null, no filter is applied (both finished and ongoing entries are returned)."
        )
        @RequestParam("finished") finished: Boolean?,
        @Parameter(
            description = "Filter by confirmation status. True for confirmed entries only, false for unconfirmed only. When omitted or null, no filter is applied (both confirmed and unconfirmed entries are returned)."
        )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The finished query parameter is nullable and maps to NewEntryFinishedFilter.ofBoolean(finished), where null means “both finished and ongoing”. The current description only mentions true/false, so Swagger consumers won’t know how to request both. Please update the description to include the null behavior (and consider aligning wording with ApiVisitV2Controller).
```suggestion
        @Parameter(description = "Filter by voyage completion status. True for finished voyages only, false for ongoing only, omit or null for both finished and ongoing voyages.")
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The finished query parameter is nullable (null = no finished filter / both states). The description currently only documents true/false; please include the null behavior for Swagger accuracy.
```suggestion
        @Parameter(
            description = "Filter by voyage completion status. True for finished voyages only, false for ongoing only, null or omitted for no filter (both finished and ongoing)."
        )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The finished query parameter is nullable and treated as “no filter” when omitted (NewEntryFinishedFilter.ofBoolean). The description should mention null=both finished+ongoing to avoid implying it’s required to choose a boolean.
```suggestion
        @Parameter(
            description = "Filter by voyage completion status: true for finished voyages only, false for ongoing only, null or omitted for both finished and ongoing (no completion-status filter)"
        )
```

### Copilot — 2026-01-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

This endpoint can also throw NotFoundException when the visit doesn’t exist ("Could not generate SOF, visit not found"), but the documented responses only include 400. Add a 404 ApiResponse so the Swagger contract matches runtime behavior.
```suggestion
            ApiResponse(responseCode = "400", description = "Provided ID is not a valid Visit ID"),
            ApiResponse(responseCode = "404", description = "Could not generate SOF, visit not found"),
```

### TeqJoostD — 2026-02-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

Only endpoints exposed in the internal api get annotation so no

### TeqJoostD — 2026-02-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

It clearly is in the code

### TeqJoostD — 2026-02-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVisitV2Controller.kt`

fixed again

### TeqJoostD — 2026-02-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

no

### TeqJoostD — 2026-02-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiEntryV2Controller.kt`

I mean, it clearly says you can either use start or end or last not both

### TeqJoostD — 2026-02-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiStatementOfFactsV2Controller.kt`

False
