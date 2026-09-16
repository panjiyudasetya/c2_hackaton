---
id: github:teqplay/vesselvoyage-backend:pr:692
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 692
title: TCC-627 barges fix
author: Darius-Wattimena
state: closed
date: '2026-01-08'
merged_at: '2026-01-08'
base_branch: develop
head_branch: TCC-627-broken-traces
url: https://github.com/teqplay/vesselvoyage-backend/pull/692
labels: []
linked_issues: []
explicit_links: []
---
# PR #692: TCC-627 barges fix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/692  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-627-broken-traces`  
**Created:** 2026-01-08  
**Merged:** 2026-01-08  

## Description

Running quite stable so far, having ~2600 ongoing barge visits after only running for like 12 hours!

## Commits

- `d8c47132` **Darius Wattimena** (2026-01-06): Improve lane hashing
- `41e82c7a` **Darius Wattimena** (2026-01-07): Fix flipped feature toggle
- `4aa41fe0` **Darius Wattimena** (2026-01-07): Adjusted ports frontend endpoint to return barges as well
- `8ddb1c89` **Darius Wattimena** (2026-01-07): Revert back amount of data we load in on start up
- `c2d9ce13` **Darius Wattimena** (2026-01-07): Update tests to not be flaky
- `6424a66b` **Darius Wattimena** (2026-01-07): Fixed an issue where barges would be loaded in multiple times in the in-memory state under IMO 0
- `2afda862` **Darius Wattimena** (2026-01-07): Added temporary endpoints to get back the current internal state of the processing pod
- `137e11fd` **Darius Wattimena** (2026-01-07): Fixed an issue where barge data of 1 vessel would be loaded for the same ship on all states
- `ba0f36ba` **Darius Wattimena** (2026-01-08): Replace IllegalArgumentException with BadRequestException for shipId resolution errors
- `9a2b0035` **Darius Wattimena** (2026-01-08): Remove temporary testing endpoints

## Reviews

### github-actions[bot] — COMMENTED (2026-01-08)

Review completed. No suggestions at this time.

### github-actions[bot] — COMMENTED (2026-01-08)

Review completed. The PR includes important improvements for barge handling and lane routing optimization. I've identified one critical issue with the lane routing function that needs to be addressed.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-08)

## Pull request overview

This PR fixes critical issues with barge (vessels without IMO numbers) processing and improves message distribution across processing lanes.

**Key Changes:**
- Fixed inverted logic in `EventsDefaultMessageProcessor` that was incorrectly filtering barges when they were enabled
- Introduced new `LaneRoutingUtils` to replace hashCode-based distribution with a more reliable UUID-segment-based approach
- Updated exception handling to use `BadRequestException` instead of `IllegalArgumentException` for better HTTP status code mapping
- Extended frontend API to support ship lookups by shipId (for barges) in addition to IMO numbers

### Reviewed changes

Copilot reviewed 14 out of 14 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `LaneRoutingUtils.kt` | New utility for deterministic lane distribution using UUID last segment instead of hashCode |
| `LaneRoutingUtilsTest.kt` | Comprehensive test suite for lane routing with distribution, consistency, and edge case tests |
| `EventsDefaultMessageProcessor.kt` | **Critical fix**: Inverted enableBarges condition from `enableBarges &&` to `!enableBarges &&` |
| `AisStreamingMessageHandler.kt` | Migrated to use new `calculateLaneIndex()` function, moved LANE_COUNT constant to utility |
| `ShipStatusService.kt` | Added filtering to prevent loading barges via IMO fallback path |
| `ProcessingFrontendViewV2Service.kt` | Removed barge exclusion, added shipById lookup support, new debug endpoints |
| `ProcessingFrontendViewV2Controller.kt` | Added shipById field to response, deprecated shipByImo, added internal state endpoints |
| `NewEntryDataSource.kt` | Excluded MISSING_IMO sentinel value from distinctImos query |
| `ChangesPublisherService.kt` | Changed exception type to BadRequestException |
| `StoryService.kt` | Changed exception type to BadRequestException (2 locations) |
| `EntryProcessingService.kt` | Changed exception type to BadRequestException |
| `EntryV2Mapper.kt` | Changed exception type to BadRequestException (3 locations) |
| `ProcessingV2EventController.kt` | Changed exception type to BadRequestException |
| `ProcessingRecalculateV2Controller.kt` | Changed exception type to BadRequestException |
</details>



<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingFrontendViewV2Controller.kt:61**
* The @Deprecated annotation uses ReplaceWith("shipById"), but this is not a straightforward replacement since shipByImo is Map<Int, ShipDetails> while shipById is Map<String, ShipDetails>. The ReplaceWith suggestion may mislead developers as it suggests a simple rename, when in fact code changes are needed to handle the different key types (Int vs String). Consider either removing the ReplaceWith or clarifying the migration path in the deprecation message.
```
    )
}

```
</details>

### michel-teqplay — APPROVED (2026-01-08)

_No comment._

## Review Comments

### Copilot — 2026-01-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

The critical logic change from `enableBarges` to `!enableBarges` is not covered by tests. This inverted condition determines whether events for ships without IMO numbers (barges) are processed or dropped. Given the significance of this change, test coverage should be added to verify the behavior when enableBarges is true (barges should be processed) and when it's false (barges should be dropped).
