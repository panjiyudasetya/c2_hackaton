---
id: github:teqplay/vesselvoyage-backend:pr:658
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 658
title: TCC-504 Added back backfill endpoint
author: Darius-Wattimena
state: closed
date: '2025-11-04'
merged_at: '2025-11-05'
base_branch: develop
head_branch: reintroduce-backfill
url: https://github.com/teqplay/vesselvoyage-backend/pull/658
labels: []
linked_issues: []
explicit_links: []
---
# PR #658: TCC-504 Added back backfill endpoint

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/658  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `reintroduce-backfill`  
**Created:** 2025-11-04  
**Merged:** 2025-11-05  

## Description

_No description._

## Commits

- `c866aac3` **Darius Wattimena** (2025-11-04): Added back backfill endpoint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-04)

## Pull Request Overview

This PR introduces paginated endpoints for retrieving all visits and statement of facts (SOFs) data without filtering. The implementation adds support for cursor-based pagination to facilitate data backfilling operations.

- Adds a new `ApiPaginatedDataController` with a `/v2/paginated/backfillData` endpoint
- Introduces `PaginatedResponse` and `PaginationMetadata` models for structured pagination responses
- Extends the client SDK with a new `Paginated` class to consume the pagination endpoint

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| `ApiPaginatedDataController.kt` | Implements controller with paginated endpoint for retrieving all visits and SOFs |
| `VesselVoyageClient.kt` | Adds client-side support for accessing the paginated endpoint |
| `PaginatedResponse.kt` | Defines data models for pagination response and metadata |

### github-actions[bot] — COMMENTED (2025-11-04)

Review completed. The backfill endpoint implementation looks solid overall with proper authentication and clean structure. A few suggestions for improvement have been provided in the inline comments.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — APPROVED (2025-11-05)

_No comment._

## Review Comments

### Copilot — 2025-11-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

The code iterates over `result` twice (lines 69-70) to extract visits and SOFs. This creates unnecessary iterations and allocations. Consider using `unzip()` or collecting into separate lists in a single pass.
```suggestion
        val (visitsList, sofsList) = result.unzip()
        return PaginatedResponse(
            visits = visitsList,
            sofs = sofsList,
```

### Copilot — 2025-11-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

The `limit` parameter lacks input validation. Without constraints, clients could request extremely large page sizes that could cause memory issues or performance degradation. Consider adding validation to enforce a maximum limit (e.g., `@Max(1000)` annotation or explicit validation).
