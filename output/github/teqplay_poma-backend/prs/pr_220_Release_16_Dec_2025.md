---
id: github:teqplay/poma-backend:pr:220
source: github
type: pull_request
repo: teqplay/poma-backend
number: 220
title: Release 16 Dec 2025
author: TeqJoostD
state: closed
date: '2025-12-10'
merged_at: '2025-12-16'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/poma-backend/pull/220
labels: []
linked_issues: []
explicit_links: []
---
# PR #220: Release 16 Dec 2025

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/220  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-12-10  
**Merged:** 2025-12-16  

## Description

_No description._

## Commits

- `dc602b8e` **Pim van den Toorn** (2025-11-03): Added Slack deployment notifications
- `4cbc7c3d` **PimTeqplay** (2025-11-20): Merge pull request #216 from teqplay/slack-deploy-notification
  Added Slack deployment notifications
- `eed98c4d` **Jamie de Leest** (2025-11-21): DEV-1282: Add pr-review workflow
- `4db9d148` **jamie-teqplay** (2025-11-21): Merge pull request #217 from teqplay/DEV-1282-add-augment-pr-review
  DEV-1282: Add augment PR review workflow
- `c5087b58` **TeqJoostD** (2025-12-10): Introduce customer area implementation
- `35e1f21a` **TeqJoostD** (2025-12-10): formatting
- `c5ed9031` **TeqJoostD** (2025-12-10): Add support for customerId and controller endpoint
- `64db6bda` **TeqJoostD** (2025-12-10): formatting
- `69ca1dec` **Michel Wilson** (2025-12-10): Increase CPU requests to reflect actual usage
- `0a55613f` **Michel Wilson** (2025-12-10): Merge pull request #219 from teqplay/increase-requests
  Increase CPU requests to reflect actual usage
- `e6d4f1db` **TeqJoostD** (2025-12-10): add index
- `ff668862` **Joost Dambrink** (2025-12-10): Merge pull request #218 from teqplay/TCC-552
  TCC-552 Customer Area

## Reviews

### github-actions[bot] — COMMENTED (2025-12-10)

Review completed. The implementation follows established patterns and appears well-structured. The customer area feature is properly integrated across all layers of the application.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-10)

## Pull request overview

This PR introduces a new `CustomerArea` infrastructure model to the POMA backend system, allowing customers to have dedicated geographical areas. The implementation follows the existing infrastructure model pattern used for other area types like CustomArea and ShipToShipArea.

**Key Changes:**
- Added CustomerArea domain and API models with full CRUD support
- Integrated CustomerArea into synchronization, global search, and all infrastructure management workflows
- Updated deployment configuration (CPU resource requests increased from 0.01 to 0.1)
- Added PR review workflow automation

### Reviewed changes

Copilot reviewed 17 out of 17 changed files in this pull request and generated 7 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/poma/model/basemodels/CustomerArea.kt` | New domain model for customer areas with location, area boundaries, and customer association |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaService.kt` | Service layer implementing business logic for customer area CRUD operations |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaController.kt` | REST controller exposing customer area endpoints with search and filtering capabilities |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/AbstractCustomerAreaDatasource.kt` | Base datasource with MongoDB indexes and query filters for customer areas |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaDatasource.kt` | Teqplay database implementation for customer areas |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaMergedDatasource.kt` | Merged database implementation for customer areas |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaExternalDatasource.kt` | External database implementation for customer areas |
| `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/Config.kt` | Type aliases and configuration constants for customer area feature |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/CustomerArea.kt` | API model for customer area with serialization support |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/InfrastructureModelType.kt` | Added CUSTOMER enum value to infrastructure model types |
| `api/src/main/kotlin/nl/teqplay/poma/api/v1/ApiModel.kt` | Registered CustomerArea in JsonSubTypes for polymorphic deserialization |
| `src/main/kotlin/nl/teqplay/poma/feature/synchronize/SyncService.kt` | Integrated CustomerAreaService into infrastructure synchronization system |
| `src/test/kotlin/nl/teqplay/poma/feature/synchronize/SyncServiceTest.kt` | Updated sync service tests to mock CustomerAreaService |
| `src/main/kotlin/nl/teqplay/poma/feature/combined/GlobalController.kt` | Added customer area support to global infrastructure search |
| `helm/values.yaml` | Increased CPU request from 0.01 to 0.1 for better resource allocation |
| `.github/workflows/pr-review.yml` | New workflow for automated PR reviews |
| `.github/workflows/main.yml` | Added Slack notification configuration for deployment pipelines |
</details>






---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### Darius-Wattimena — APPROVED (2025-12-16)

_No comment._

## Review Comments

### Copilot — 2025-12-10 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/CustomerArea.kt`

The comment refers to "region" but this is a CustomerArea. The comment should be updated to say "the ports that are in the customer area, set of unlocodes" for consistency with the model name and the comment at line 4.
```suggestion
    /** the ports that are in the customer area, set of unlocodes */
```

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/model/basemodels/CustomerArea.kt`

The comment refers to "region" but this is a CustomerArea data class. The comment should be updated to say "The name of the customer area" for consistency with the model name.
```suggestion
    /** The name of the customer area */
```

### Copilot — 2025-12-10 on `.github/workflows/pr-review.yml`

The file appears to contain a BOM (Byte Order Mark) character at the beginning (the invisible character before "name"). This can cause issues with some YAML parsers and should be removed. Save the file with UTF-8 encoding without BOM.
```suggestion
name: pr-review
```

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaService.kt`

The documentation comment is inaccurate for CustomerArea. It mentions "region object", "unlocode and countryCode" which don't apply to this model. The comment should describe what this sanitize function actually does for CustomerArea, which is transforming the name and ports to uppercase.
```suggestion
     * Sanitizes the CustomerArea by transforming the name and all ports to uppercase,
     * and updates the updatedAt timestamp.
```

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/CustomerAreaController.kt`

The endpoint path `/{customerId}` conflicts with the inherited `getById` endpoint at `/{id}` from InfrastructureController. When a request is made to `/v1/customerarea/someValue`, Spring will be unable to differentiate whether `someValue` is an `id` or a `customerId`. Consider using a more specific path like `/customer/{customerId}` or `/by-customer-id/{customerId}` to avoid this ambiguity.
```suggestion
    @GetMapping("/customer/{customerId}")
```

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/AbstractCustomerAreaDatasource.kt`

Using `ensureUniqueIndex` for `customerId` will prevent a customer from having multiple customer areas, which conflicts with the `getByCustomerId` method that returns a list. This should be `ensureIndex` instead of `ensureUniqueIndex` to allow multiple customer areas per customer, following the pattern used in similar infrastructure datasources like CustomAreaDatasource and ShipToShipAreaDatasource.
```suggestion
            ensureIndex(Model::customerId)
```

### Copilot — 2025-12-10 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/customerarea/AbstractCustomerAreaDatasource.kt`

Using `ensureUniqueIndex` for `name` is overly restrictive. Different customers should be able to have customer areas with the same name. This should be `ensureIndex` instead, following the pattern used in similar infrastructure datasources like CustomAreaDatasource and ShipToShipAreaDatasource.
```suggestion
            ensureIndex(Model::name)
```
