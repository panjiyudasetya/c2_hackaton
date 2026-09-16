---
id: github:teqplay/vesselvoyage-backend:pr:699
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 699
title: Release 20 Jan 2026
author: Darius-Wattimena
state: closed
date: '2026-01-19'
merged_at: '2026-01-20'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/699
labels: []
linked_issues: []
explicit_links: []
---
# PR #699: Release 20 Jan 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/699  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-01-19  
**Merged:** 2026-01-20  

## Description

_No description._

## Commits

- _… 48 earlier commits not shown_
- `2967f067` **Darius Wattimena** (2026-01-05): Refactor NewEntryDataSource to require ShipIdLazyLoader and make it impossible to get a null pointer
- `8e11566c` **Darius Wattimena** (2026-01-05): Made sure shipId is not null when we process events
- `94e7773d` **Darius Wattimena** (2026-01-05): ktlint
- `4275f7f9` **Darius Wattimena** (2026-01-05): flip check to actually work as intended
- `e1289b6e` **Darius Wattimena** (2026-01-05): Merge pull request #687 from teqplay/TCC-570-internal-csi-id
  TCC-570 Make ShipId internal ship identifier instead of the IMO number
- `abe2fbff` **Darius Wattimena** (2026-01-05): Merge pull request #688 from teqplay/TCC-548-api-adjustments
  TCC-548 api adjustments
- `49cf0b3c` **Darius Wattimena** (2026-01-06): PR feedback
- `8c2038a7` **Darius Wattimena** (2026-01-06): Merge pull request #689 from teqplay/TCC-546-real-time-recalculate-capabilities
  TCC-546 real time recalculate capabilities
- `d8c47132` **Darius Wattimena** (2026-01-06): Improve lane hashing
- `367f6153` **TeqJoostD** (2026-01-07): Change thread pool settings for post-processing
  Add max timeout for thread pool
- `41e82c7a` **Darius Wattimena** (2026-01-07): Fix flipped feature toggle
- `48d78169` **TeqJoostD** (2026-01-07): Revert some of the thread pool settings
- `bdd2d38f` **TeqJoostD** (2026-01-07): Introduce bounded queue with error message and slack notification again
- `ba3993eb` **TeqJoostD** (2026-01-07): Add test coverage for timeout mechanism
- `8630e763` **TeqJoostD** (2026-01-07): Introduce mechanism for cancelling task when taking too long
- `9ff0de67` **TeqJoostD** (2026-01-07): Increase queue size to 10000
- `4aa41fe0` **Darius Wattimena** (2026-01-07): Adjusted ports frontend endpoint to return barges as well
- `8ddb1c89` **Darius Wattimena** (2026-01-07): Revert back amount of data we load in on start up
- `c2d9ce13` **Darius Wattimena** (2026-01-07): Update tests to not be flaky
- `6424a66b` **Darius Wattimena** (2026-01-07): Fixed an issue where barges would be loaded in multiple times in the in-memory state under IMO 0
- `2afda862` **Darius Wattimena** (2026-01-07): Added temporary endpoints to get back the current internal state of the processing pod
- `137e11fd` **Darius Wattimena** (2026-01-07): Fixed an issue where barge data of 1 vessel would be loaded for the same ship on all states
- `ba0f36ba` **Darius Wattimena** (2026-01-08): Replace IllegalArgumentException with BadRequestException for shipId resolution errors
- `9a2b0035` **Darius Wattimena** (2026-01-08): Remove temporary testing endpoints
- `f7856cd0` **Darius Wattimena** (2026-01-08): Merge pull request #692 from teqplay/TCC-627-broken-traces
  TCC-627 barges fix
- `65706f91` **Joost Dambrink** (2026-01-09): Merge pull request #691 from teqplay/TCC-616
  TCC-616 PostProcessing thread pool stuck fix
- `7f1ed86b` **Darius Wattimena** (2026-01-09): Enhance ship ID resolution by adding support for IMO lookup when MMSI is not found
- `adb751b9` **Darius Wattimena** (2026-01-09): Merge branch 'develop' into TCC-638-etas-not-applied
- `7bd8911d` **Darius Wattimena** (2026-01-09): Make comment more clear
- `99234684` **Darius Wattimena** (2026-01-09): Refactor assertions in StaticShipInfoServiceTest to use assertNotNull for clarity
- `98a844cb` **Darius Wattimena** (2026-01-09): Adjusted all places where assert was used to use junit methods
- `e0411b27` **Darius Wattimena** (2026-01-09): Refactor StaticShipInfoServiceTest to reduce mock declarations
- `2a3723e2` **Darius Wattimena** (2026-01-09): Refactor StaticShipInfoServiceTest to use parameterized tests for ship ID retrieval
- `51fe48ef` **Darius Wattimena** (2026-01-12): Merge pull request #693 from teqplay/TCC-638-etas-not-applied
  TCC-638 etas not applied
- `657d3232` **Darius Wattimena** (2026-01-12): Introduce VesselType enum and update endpoints to filter by vessel type when requesting by port
- `370339fa` **Darius Wattimena** (2026-01-12): Updated client to support the new vesselType parameter
- `1f7a5395` **Darius Wattimena** (2026-01-12): Made the vesselType field non-nullable to make things easier
- `71cea704` **Darius Wattimena** (2026-01-12): Update client to reflect non-nullable changes
- `0620da90` **Darius Wattimena** (2026-01-12): PR feedback
- `c55a8e5a` **Darius Wattimena** (2026-01-13): Merge pull request #694 from teqplay/TCC-643-api-adjustments
  TCC-643 api adjustments for `byPort` endpoints
- `20b7873f` **Darius Wattimena** (2026-01-16): Adjust ship search to work with barges and refactor qualifying IMOs to qualifying ship IDs across controllers and services
- `85ab2010` **Darius Wattimena** (2026-01-16): Adjusted existing test to reflect changes in ship cache
- `2341a32d` **Darius Wattimena** (2026-01-16): Adjusted event processing endpoint to work with both IMOs and Ship IDs
- `ed8ee08e` **Darius Wattimena** (2026-01-16): ktlint
- `d86a7ca5` **Darius Wattimena** (2026-01-16): Refactor MMSI retrieval logic to handle barges
- `2a7d1f22` **Darius Wattimena** (2026-01-19): Merge pull request #696 from teqplay/TCC-650-ship-search-barges
  TCC-650 ship search barges
- `6d6b29bb` **Darius Wattimena** (2026-01-19): Merge pull request #697 from teqplay/TCC-636-event-dry-run
  TCC-636 support event processing dry run by Ship ID
- `6911705f` **Darius Wattimena** (2026-01-19): Merge pull request #698 from teqplay/TCC-654-barges-story
  TCC-654 barges story fix missing MMSI
- `3f6f34b9` **Darius Wattimena** (2026-01-19): Merge remote-tracking branch 'origin/master' into fix-merge-conflicts
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt
- `459829ed` **Darius Wattimena** (2026-01-20): Merge pull request #700 from teqplay/fix-merge-conflicts
  Fix merge conflicts

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-19)

## Pull request overview

This PR introduces a major architectural change to support ships without IMO numbers (barges) by introducing a `shipId` field alongside the existing `imo` field. The changes migrate core services from IMO-based locking and identification to shipId-based operations.

**Changes:**
- Introduces `shipId` field to voyage/visit models and throughout the processing pipeline
- Refactors `ImoLockService` to `ShipLockService` with shipId-based locking
- Adds lane routing utilities for distributing ships across processing lanes
- Updates test fixtures and adds comprehensive test coverage for new functionality

### Reviewed changes

Copilot reviewed 194 out of 195 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| Test data (JSON) | Adds shipId field to test event fixtures |
| Test utilities | Adds shipId constants and updates helper functions |
| LaneRoutingUtilsTest.kt | New comprehensive tests for lane distribution algorithm |
| Service tests | Updates mocking to use shipId and ShipLockService |
| Main utilities | Adds shipId support to entry creation and ship status utilities |
| Service layer | Refactors services to use shipId for locking and identification |
| Processors | Updates event processors to accept shipId parameter |
| Configuration | Adds barge enablement flags |
</details>

### michel-teqplay — APPROVED (2026-01-20)

_No comment._

## Comments
