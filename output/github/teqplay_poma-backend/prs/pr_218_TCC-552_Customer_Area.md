---
id: github:teqplay/poma-backend:pr:218
source: github
type: pull_request
repo: teqplay/poma-backend
number: 218
title: TCC-552 Customer Area
author: TeqJoostD
state: closed
date: '2025-12-10'
merged_at: '2025-12-10'
base_branch: develop
head_branch: TCC-552
url: https://github.com/teqplay/poma-backend/pull/218
labels: []
linked_issues: []
explicit_links: []
---
# PR #218: TCC-552 Customer Area

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/218  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-552`  
**Created:** 2025-12-10  
**Merged:** 2025-12-10  

## Description

_No description._

## Commits

- `c5087b58` **TeqJoostD** (2025-12-10): Introduce customer area implementation
- `35e1f21a` **TeqJoostD** (2025-12-10): formatting
- `c5ed9031` **TeqJoostD** (2025-12-10): Add support for customerId and controller endpoint
- `64db6bda` **TeqJoostD** (2025-12-10): formatting
- `e6d4f1db` **TeqJoostD** (2025-12-10): add index

## Reviews

### github-actions[bot] — COMMENTED (2025-12-10)

The CustomerArea implementation follows established patterns well and integrates properly with the existing infrastructure. I found one potential bug in the service layer that should be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-10)

## Pull request overview

This PR adds support for a new infrastructure model type called "Customer Area" (TCC-552). The implementation follows the established pattern for infrastructure models in the codebase, similar to existing models like CustomArea and ShipToShipArea.

- Introduces a new `CustomerArea` model with associated service, datasources, and controller
- Integrates the new model type into the sync service and global controller
- Adds comprehensive API definitions and enum values for the CUSTOMER infrastructure type

### Reviewed changes

Copilot reviewed 14 out of 14 changed files in this pull request and generated 3 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/poma/model/basemodels/CustomerArea.kt` | Defines the database model for CustomerArea with location, area, and port properties |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaService.kt` | Implements service layer with CRUD operations and model conversion logic |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/AbstractCustomerAreaDatasource.kt` | Abstract datasource with MongoDB indexing and search query implementations |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaDatasource.kt` | Teqplay database datasource implementation |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaMergedDatasource.kt` | Merged database datasource implementation |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaExternalDatasource.kt` | External database datasource implementation |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaController.kt` | REST controller for CustomerArea endpoints with validation logic |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/Config.kt` | Type aliases and collection name configuration |
| `src/main/kotlin/nl/teqplay/poma/feature/synchronize/SyncService.kt` | Adds CustomerAreaService integration to sync service routing |
| `src/main/kotlin/nl/teqplay/poma/feature/combined/GlobalController.kt` | Adds CustomerArea handling to global infrastructure controller |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/CustomerArea.kt` | API model definition for CustomerArea |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/InfrastructureModelType.kt` | Adds CUSTOMER enum value to infrastructure model types |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/ApiModel.kt` | Adds JSON subtype mapping for CustomerArea |
| `src/test/kotlin/nl/teqplay/poma/feature/synchronize/SyncServiceTest.kt` | Updates test to include CustomerAreaService mock in SyncService constructor |
</details>






---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### github-actions[bot] — COMMENTED (2025-12-10)

Review completed. The CustomerArea implementation follows established patterns and integrates well with the existing infrastructure. The code is well-structured and consistent with the codebase conventions.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-10)

Review completed. The CustomerArea implementation follows established patterns well and integrates properly with the existing infrastructure. One potential issue identified around synchronization service integration.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — APPROVED (2025-12-10)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-10)

Review completed. The Customer Area implementation follows established patterns well and integrates properly with the existing infrastructure. The code is well-structured and consistent with the codebase conventions.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

## Review Comments

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaService.kt`

The documentation comment is inaccurate. It mentions "unlocode and countryCode" but CustomerArea does not have these fields. The comment should reflect what is actually being sanitized: the name and ports are transformed to uppercase.
```suggestion
     * Clean up the region object.
     * The name and ports are transformed to uppercase to enable faster searching.
     * The updatedAt field is set to the current time.
```

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaService.kt`

The `ports` field is not being mapped from `apiModel` to the infrastructure model. This will result in an empty list being used instead of the ports from the API model. Add `ports = apiModel.ports,` to the Model constructor.
```suggestion
            sourceType = getSourceType(apiModel.sourceType),
            ports = apiModel.ports,
```

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/CustomerArea.kt`

The comment says "The name of the region" but should say "The name of the customer area" to be consistent with the API model and the actual purpose of this class.
```suggestion
    /** The name of the customer area */
```
