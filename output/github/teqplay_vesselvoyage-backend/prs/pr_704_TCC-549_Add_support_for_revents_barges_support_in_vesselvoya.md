---
id: github:teqplay/vesselvoyage-backend:pr:704
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 704
title: TCC-549 Add support for revents barges support in vesselvoyage
author: TeqJoostD
state: closed
date: '2026-01-27'
merged_at: '2026-02-10'
base_branch: develop
head_branch: TCC-549
url: https://github.com/teqplay/vesselvoyage-backend/pull/704
labels: []
linked_issues: []
explicit_links: []
---
# PR #704: TCC-549 Add support for revents barges support in vesselvoyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/704  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-549`  
**Created:** 2026-01-27  
**Merged:** 2026-02-10  

## Description

- Removed V1 revents stuff
- Added support for shipId and new revents endpoints

## Commits

- `3eeaedaf` **TeqJoostD** (2026-01-27): Add support for revents barges support in vesselvoyage
  - Removed V1 revents stuff
  - Added support for shipId and new revents endpoints
- `6775d8a6` **TeqJoostD** (2026-01-27): remove 7
- `db255cd4` **TeqJoostD** (2026-01-27): remove unused mock
- `a77bcb81` **TeqJoostD** (2026-01-29): add mmsi to RecalculationResult.kt
- `744c30f1` **TeqJoostD** (2026-01-29): fix tests
- `68964ceb` **Joost Dambrink** (2026-02-04): Merge branch 'develop' into TCC-549
- `23aeea0f` **TeqJoostD** (2026-02-05): Revents barges fix
- `624ad44c` **TeqJoostD** (2026-02-06): some feedback
- `e1817924` **Joost Dambrink** (2026-02-10): Merge pull request #708 from teqplay/revents-barges-fix
  Revents barges fix
- `7ae939a9` **Joost Dambrink** (2026-02-10): Merge branch 'develop' into TCC-549
- `afbf5438` **TeqJoostD** (2026-02-10): Upgrade to stable version
- `43e25f2e` **TeqJoostD** (2026-02-10): Merge remote-tracking branch 'origin/TCC-549' into TCC-549

## Reviews

### github-actions[bot] — COMMENTED (2026-01-27)

Review completed. Found one critical syntax error that will prevent compilation.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — COMMENTED (2026-01-27)

_No comment._

### TeqJoostD — COMMENTED (2026-01-27)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-27)

## Pull request overview

This pull request removes support for V1 revents processing and migrates the vesselvoyage recalculation system from IMO-based to shipId-based identification to support barges. This is a significant architectural change that enables better handling of vessels that may not have IMO numbers, such as barges.

**Changes:**
- Removed all V1 revents code including `EntriesMergeV1Service`, `ReventsVesselVoyageMergingClient`, and V1 test infrastructure
- Migrated from IMO (Integer) to shipId (String) throughout the recalculation and automatic recalculation flows
- Updated API endpoints to use `shipId` instead of `imo` as path parameters, introducing breaking changes
- Updated database queries and data source methods to work with shipId instead of IMO
- Updated the aisengine dependency version to support the new V2-only revents endpoints

### Reviewed changes

Copilot reviewed 24 out of 25 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| ReventsRecalculationServiceTest.kt | Removed V1 test cases and updated all test mocks/verifications to use shipId instead of IMO |
| ReventsConversionServiceTest.kt | Updated scenario creation tests to use shipId instead of IMO |
| RecalculationEnlargeTimeWindowServiceTest.kt | Removed V1 time window enlargement tests and updated V2 tests for shipId |
| EntriesMergeV2ServiceTest.kt | Updated merge service tests to use shipId parameters |
| EntriesMergeV1ServiceTest.kt | Deleted entire file containing V1 merge tests |
| EntriesMergeBaseServiceTest.kt | Updated base test class to use shipId in merge operations |
| RecalculationMergeResultTest.kt | Updated test data to use shipId strings |
| ReventsRecalculationService.kt | Major refactoring removing V1 logic, updating all methods to use shipId, and removing IMO-to-shipId resolution |
| ReventsConversionService.kt | Updated scenario creation to use shipId and removed V1 guarantee handling |
| RecalculationEnlargeTimeWindowService.kt | Removed V1 time window enlargement method |
| AutomaticRecalculationService.kt | Updated automatic recalculation to work with shipIds throughout |
| EntriesMergeV2Service.kt | Updated to use shipId-based entry queries |
| EntriesMergeV1Service.kt | Deleted entire file |
| EntriesMergeService.kt | Updated interface to use shipId instead of IMO |
| EntryV2Service.kt | Added new `findByShipIdAndTimeRange` method |
| StaticShipInfoService.kt | Added new shipId-based lookup methods |
| ShipCacheService.kt | Added `getAllShipIds` method |
| AutomaticRecalculationShip.kt | Changed primary key from `imo: Int` to `shipId: String` |
| ReventsRecalculationsDataSource.kt | Updated all queries to use shipId |
| NewVoyageDataSource.kt | Updated voyage lookup methods to use shipId |
| AutomaticRecalculationShipDataSource.kt | Updated to use shipId as identifier |
| ProcessingRecalculateV2Controller.kt | Updated API endpoints from `/ship/{imo}` to `/ship/{shipId}` |
| ReventsRecalculationStatus.kt | Removed V1 guarantee enum value and updated error model to use shipId |
| RecalculationResult.kt | Updated models to use shipId instead of imo fields |
| build.gradle | Updated aisengine dependency to new version with V2-only support |
</details>

### github-actions[bot] — COMMENTED (2026-01-27)

Review completed. Found one potential issue with the guarantee conversion logic that could cause runtime errors.

### TeqJoostD — COMMENTED (2026-01-27)

_No comment._

### github-actions[bot] — COMMENTED (2026-01-27)

Review completed. I found one potential issue related to non-exhaustive pattern matching that could lead to runtime errors if new guarantee types are added in the future.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — COMMENTED (2026-01-27)

_No comment._

### github-actions[bot] — COMMENTED (2026-01-29)

Review completed. No suggestions at this time.

### github-actions[bot] — COMMENTED (2026-01-29)

I've reviewed the PR changes for adding revents barges support. The migration from IMO-based identifiers to shipId-based identifiers appears to be comprehensive and well-executed. The removal of V1 revents code is clean, and the changes are consistent throughout the codebase including tests.

The refactoring maintains the existing logic while updating the data model, and I don't see any high-confidence issues that need to be addressed at this time.

### Darius-Wattimena — CHANGES_REQUESTED (2026-01-30)

Please apply the open feedback, then its good to go for me

### github-actions[bot] — COMMENTED (2026-02-04)

Review completed. Found one potential null safety issue that should be addressed.

### github-actions[bot] — COMMENTED (2026-02-10)

This PR successfully migrates from IMO-based to shipId-based identification and removes V1 revents support. The changes are comprehensive and well-structured. I've identified a few potential issues that should be addressed.

### github-actions[bot] — COMMENTED (2026-02-10)

Review completed. The migration from IMO-based to shipId-based processing appears well-structured overall. I've identified a few potential issues related to null handling and edge cases that should be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — DISMISSED (2026-02-10)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-10)

Review completed. I found one potential issue related to event processing logic when barges are enabled.

### Darius-Wattimena — APPROVED (2026-02-10)

_No comment._

## Review Comments

### Darius-Wattimena — 2026-01-27 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/ReventsRecalculationStatus.kt`

Just delete the 7

### TeqJoostD — 2026-01-27 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/ReventsRecalculationStatus.kt`

luckily this critical bug was found before deploying to production, thanks Augment!

### Copilot — 2026-01-27 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/ReventsRecalculationStatus.kt`

There's a typo in the comment marker. The line shows "46: 7" instead of just the line number. This should be cleaned up to maintain code readability.
```suggestion
     * A scenario could have one or more guarantees to merge V2 data back into VesselVoyage.
```

### Copilot — 2026-01-27 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt`

This mock for `staticShipInfoService.getShipIdByImo(eq(1))` is no longer used. After the migration to shipId-based processing, the V2 flow no longer calls `getShipIdByImo` since shipIds are returned directly from `getShipIdsForMerging`. This mock should be removed to keep tests clean and avoid confusion.
```suggestion

```

### TeqJoostD — 2026-01-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionService.kt`

zip it

### TeqJoostD — 2026-01-27 on `build.gradle`

upgrade version
