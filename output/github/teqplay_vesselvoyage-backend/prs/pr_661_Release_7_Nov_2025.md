---
id: github:teqplay/vesselvoyage-backend:pr:661
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 661
title: Release 7 Nov 2025
author: Darius-Wattimena
state: closed
date: '2025-11-07'
merged_at: '2025-11-07'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/661
labels: []
linked_issues: []
explicit_links: []
---
# PR #661: Release 7 Nov 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/661  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-11-07  
**Merged:** 2025-11-07  

## Description

_No description._

## Commits

- `d282c797` **TeqJoostD** (2025-10-28): add augment pr review workflow
- `89392deb` **Joost Dambrink** (2025-10-28): Merge branch 'develop' into augment-pr-review
- `d4080b8a` **Joost Dambrink** (2025-11-03): Merge pull request #654 from teqplay/augment-pr-review
  add augment pr review workflow
- `c866aac3` **Darius Wattimena** (2025-11-04): Added back backfill endpoint
- `d0ed34ba` **Darius Wattimena** (2025-11-05): Merge pull request #658 from teqplay/reintroduce-backfill
  TCC-504 Added back backfill endpoint
- `f5462b54` **TeqJoostD** (2025-11-06): publish changes from eta update result
- `73a6f09f` **TeqJoostD** (2025-11-07): fix comment
- `c86ab078` **Joost Dambrink** (2025-11-07): Merge pull request #659 from teqplay/TCC-524
  publish changes from eta update result
- `e7c0bda6` **Darius Wattimena** (2025-11-07): Updated PTO sof model so it implements the ApiStartEnd for all fields
- `544edc10` **Darius Wattimena** (2025-11-07): Merge pull request #660 from teqplay/TCC-504-fix-api-models
  TCC-504 Updated PTO sof model so it implements the ApiStartEnd for all fields

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-07)

## Pull Request Overview

This PR integrates change publishing into the ETA prediction message handler, adds a new paginated data endpoint for backfill operations, implements the `ApiStartEnd` interface for several data classes, and adds a GitHub workflow for automated PR reviews.

- Adds change publishing functionality to `EtaPredictionMessageHandler` when prediction results contain changes
- Introduces a new `/v2/paginated/backfillData` endpoint with corresponding client method for retrieving all visits and SOFs without filtering
- Updates three data classes (`UnclassifiedStop`, `ApproachAreaVisit`, `ShipToShipTransfer`) to implement the `ApiStartEnd` interface

### Reviewed Changes

Copilot reviewed 8 out of 8 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandler.kt` | Adds `ChangesPublisherService` dependency and publishes changes when present |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandlerTest.kt` | Adds test coverage for change publishing behavior |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/EntryProcessingService.kt` | Updates comment to be consistent with similar publishing logic |
| `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt` | Adds new controller with paginated endpoint for retrieving all visits and SOFs |
| `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt` | Adds client method for calling the new paginated endpoint |
| `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/pto/PtoStatementOfFactsView.kt` | Makes three data classes implement `ApiStartEnd` interface |
| `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/PaginatedResponse.kt` | Adds new response models for pagination |
| `.github/workflows/basic-pr-review.yml` | Adds GitHub Actions workflow for automated PR reviews |
</details>

### github-actions[bot] — COMMENTED (2025-11-07)

Review completed. The code changes look good overall with proper Kotlin practices and adequate test coverage. I have one minor suggestion for improvement.

### TeqJoostD — APPROVED (2025-11-07)

_No comment._

## Review Comments

### Copilot — 2025-11-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EtaPredictionMessageHandler.kt`

[nitpick] The `changesPublisherService` is nullable but used with safe-call operators only when changes are present. This nullable design could hide missing configuration issues. Consider making it non-nullable with `@ConditionalOnProperty` or `@Autowired(required = false)` to make the dependency clearer, or add logging when the service is null but changes exist.

### Copilot — 2025-11-07 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

The KDoc return statement mentions 'PTOStatementOfFactsView' specifically, but the endpoint returns a generic `StatementOfFactsView` based on the `view` parameter which could be any view type. The documentation should reflect that the return type depends on the `view` parameter.
```suggestion
         * @return Paginated response containing ALL StatementOfFactsView objects of the type specified by the [view] parameter.
```

## Comments

### TeqJoostD — 2025-11-07

You make so much good code Darius, thank you!
