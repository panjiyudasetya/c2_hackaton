---
id: github:teqplay/vesselvoyage-backend:pr:687
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 687
title: TCC-570 Make ShipId internal ship identifier instead of the IMO number
author: Darius-Wattimena
state: closed
date: '2025-12-22'
merged_at: '2026-01-05'
base_branch: develop
head_branch: TCC-570-internal-csi-id
url: https://github.com/teqplay/vesselvoyage-backend/pull/687
labels: []
linked_issues: []
explicit_links: []
---
# PR #687: TCC-570 Make ShipId internal ship identifier instead of the IMO number

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/687  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-570-internal-csi-id`  
**Created:** 2025-12-22  
**Merged:** 2026-01-05  

## Description

_No description._

## Commits

- `06382334` **Darius Wattimena** (2025-12-16): Add CSI id to internal models, processing and all underlying components using them
- `91f8c5f0` **Darius Wattimena** (2025-12-18): Refactor shipId handling in NewVisit and NewVoyage models to be nullable, update related processing logic, and implement lazy loading for shipId resolution and added migration support
- `7a44a220` **Darius Wattimena** (2025-12-19): Merge branch 'refs/heads/develop' into TCC-570-internal-csi-id
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageEndProcessor.kt
- `56805b1b` **Darius Wattimena** (2025-12-19): Reverted back the change where imo would not be set anymore, but for now always set the field if we have any, otherwise the imo 0 will be provided for ships without an IMO
- `3f449883` **Darius Wattimena** (2025-12-19): Adjusted all tests so they work again with all changes made with ship ids
- `d12285b8` **Darius Wattimena** (2025-12-19): code cleanup and renaming
- `c3cb0ece` **Darius Wattimena** (2025-12-19): Added a toggle and some tests to ensure barges are handled correctly
- `1dbcc755` **Darius Wattimena** (2025-12-19): Adjusted database queries so we never return visits and voyages by imo 0 when requesting by port
- `0f867a68` **Darius Wattimena** (2025-12-19): Revert back to correctly load in only 1 day of ship state
- `0b6ac546` **Darius Wattimena** (2025-12-19): Adjusted frontend logic so we never display barges
- `064ea7f6` **Darius Wattimena** (2025-12-19): Added missing index to speedup startup
- `439d6629` **Darius Wattimena** (2025-12-19): Fallback existing entries to make use of imo to get the shipId
- `058bc8c6` **Darius Wattimena** (2025-12-19): Fix broken tests
- `3b8e68ca` **Darius Wattimena** (2025-12-19): Adjusted shipId migration to keep the progress in mongo to survive a restart
- `138e131d` **Darius Wattimena** (2025-12-22): Add remaining IMOs calculation for visit and voyage collections in migration stats
- `eca95d4a` **Darius Wattimena** (2025-12-22): Merge branch 'develop' into TCC-570-internal-csi-id
- `c51c9a26` **Darius Wattimena** (2025-12-22): PR feedback
- `f2bee220` **Darius Wattimena** (2025-12-22): Remove post-processing entry when the ship ID can't be resolved
- `3ae27f5f` **Darius Wattimena** (2025-12-24): pr feedback + allow processing AIS of non-imo vessels

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-22)

## Pull request overview

This PR implements a significant refactoring to change the ship identifier from IMO number to an internal CSI Ship ID throughout the codebase. The change enables support for non-sea vessels (barges) that don't have IMO numbers.

**Key Changes:**
- Replaced IMO-based ship identification with shipId throughout the processing pipeline
- Renamed `ImoLockService` to `ShipLockService` and updated locking mechanism to use shipId
- Added `shipId` field to `NewVisit` and `NewVoyage` data models
- Introduced `ShipIdBackgroundMigrationService` for gradual data migration
- Updated all event processors to accept `shipId` instead of `imo` parameter

### Reviewed changes

Copilot reviewed 112 out of 112 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| StaticShipInfoService.kt | Added methods to resolve shipId from IMO/MMSI and vice versa; introduced MISSING_IMO constant |
| ShipLockService.kt | Renamed from ImoLockService; now uses shipId.hashCode() for lock striping |
| ShipStatusService.kt | Updated to use shipId for status retrieval and storage; added fallback to IMO during migration |
| ProcessingShipStatusService.kt | Changed internal cache from IMO to shipId; updated startup to load ships by shipId |
| EventProcessingService.kt | Added shipId parameter to all event processing methods |
| EntryProcessingService.kt | Updated to resolve and pass shipId through processing pipeline |
| Various Processors | Updated all processor interfaces to accept shipId instead of imo |
| Migration Service | New background service to gradually migrate existing data to include shipId |
| Test Files | Updated test utilities and mocks to provide shipId; added DEFAULT_TEST_SHIP_ID constant |
| Application Properties | Added shipid-migration and enable-barges configuration properties |
</details>

### github-actions[bot] — COMMENTED (2025-12-22)

This is a substantial refactoring that migrates from IMO-based ship identification to an internal shipId system. The migration strategy with lazy loading and background migration is well-designed. I've identified a few potential bugs that should be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-12-22)

Review completed. The existing automated review has already identified the critical issues in this PR. No additional suggestions at this time.

### github-actions[bot] — COMMENTED (2025-12-22)

Review completed. The migration from IMO-based to shipId-based identifiers is well-structured with proper lazy loading and background migration support. I've identified a couple of minor improvements that could enhance robustness during the migration period.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — CHANGES_REQUESTED (2025-12-22)

_No comment._

### Darius-Wattimena — COMMENTED (2025-12-24)

_No comment._

### github-actions[bot] — COMMENTED (2025-12-24)

Review completed. Found one critical bug related to sequence consumption that would cause processing failures.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — APPROVED (2026-01-05)

_No comment._

## Review Comments

### michel-teqplay — 2025-12-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

`null` is also a distinct result so I believe this needs to be addressed.

### michel-teqplay — 2025-12-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Incorrect: also process barge ais data here :)

### michel-teqplay — 2025-12-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Routing should be done on ship ip instead of IMO

### michel-teqplay — 2025-12-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Same here

### Darius-Wattimena — 2025-12-24 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt`

Actually testing this out locally, this is not the case. Given that the field doesn't exist in old data, it means `null` will never be returned.

Also there will always be a value in the field when processing real-time, so it can never be `null`.
