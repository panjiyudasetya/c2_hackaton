---
id: github:teqplay/vesselvoyage-backend:pr:701
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 701
title: TCC-635 barge testing paginated response
author: Darius-Wattimena
state: closed
date: '2026-01-21'
merged_at: '2026-01-22'
base_branch: develop
head_branch: TCC-635-vesselvoyage-barges-testing
url: https://github.com/teqplay/vesselvoyage-backend/pull/701
labels: []
linked_issues: []
explicit_links: []
---
# PR #701: TCC-635 barge testing paginated response

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/701  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-635-vesselvoyage-barges-testing`  
**Created:** 2026-01-21  
**Merged:** 2026-01-22  

## Description

Adjusted the endpoint used by the VesselVoyage completeness testing backend so backfilling can also happen for barges.

## Commits

- `3c7c552f` **Darius Wattimena** (2026-01-20): Adjusted paginated response to instead return the base ApiVisit class to support barges
- `e5a0cc54` **Darius Wattimena** (2026-01-20): ktlint
- `52f2fa6a` **Darius Wattimena** (2026-01-20): Handle BadRequestException when mapping visits to ApiVisit, ensuring missing IMO values are ignored

## Reviews

### github-actions[bot] — COMMENTED (2026-01-21)

Review completed. The changes correctly generalize the type from `ImoVisit` to `ApiVisit` to support both IMO vessels and barges. The exception handling approach is reasonable for filtering out entries with unresolvable ship IDs.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-21)

## Pull request overview

This PR extends the paginated backfill endpoint to support both IMO vessels and barges by changing the type from `ImoVisit` to the more general `ApiVisit` interface. Error handling was added to gracefully skip entries where the shipId cannot be resolved.

**Changes:**
- Changed response type from `ImoVisit` to `ApiVisit` to support both IMO vessels and barges
- Added try-catch block to handle `BadRequestException` when shipId resolution fails

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| ApiPaginatedDataController.kt | Updated to use `ApiVisit` type and added error handling for unresolvable shipIds during backfilling |
| PaginatedResponse.kt | Changed visits field type from `List<ImoVisit>` to `List<ApiVisit>` to support both vessel types |

### michel-teqplay — APPROVED (2026-01-21)

_No comment._

## Review Comments

### Copilot — 2026-01-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

The new error handling logic and type changes in this controller lack test coverage. Other controllers in this package (ApiVisitV2Controller, ApiVoyageV2Controller, ApiStatementOfFactsV2Controller) have comprehensive test coverage. Consider adding tests to cover: 1) successful handling of both ImoVisit and BargeVisit types, 2) the BadRequestException catch scenario when shipId cannot be resolved, and 3) the pagination behavior with the new type.

### Copilot — 2026-01-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiPaginatedDataController.kt`

The comment is inaccurate. Based on the EntryV2Mapper code, the BadRequestException is thrown when the shipId cannot be resolved for an entry, not specifically when "the IMO can't be converted to a ShipID". The comment should be updated to reflect the actual condition: "Happens when the shipId cannot be resolved for this entry, which means the vessel is missing in CSI".
```suggestion
                // Happens when the shipId cannot be resolved for this entry, which means the vessel is missing in CSI so we can just ignore
```
