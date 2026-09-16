---
id: github:teqplay/vesselvoyage-backend:pr:709
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 709
title: Process bunker encounters both ways
author: michel-teqplay
state: closed
date: '2026-02-11'
merged_at: '2026-02-12'
base_branch: develop
head_branch: TCC-710_bunker-encounters
url: https://github.com/teqplay/vesselvoyage-backend/pull/709
labels: []
linked_issues: []
explicit_links: []
---
# PR #709: Process bunker encounters both ways

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/709  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-710_bunker-encounters`  
**Created:** 2026-02-11  
**Merged:** 2026-02-12  

## Description

_No description._

## Commits

- `5cecb5bd` **Michel Wilson** (2026-02-11): Process bunker encounters both ways
- `e3f828d4` **Michel Wilson** (2026-02-11): Also honor blacklist and barges property for other vessel

## Reviews

### github-actions[bot] — COMMENTED (2026-02-11)

Review completed. Found one potential bug related to blacklist checking for bunker vessels.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-11)

## Pull request overview

Updates the events queue processor to record bunker encounter events for both the “main” ship and the bunker vessel, with accompanying tests to validate the new behavior.

**Changes:**
- Extend `EventsDefaultMessageProcessor.processMessage` to additionally process `EncounterType.BUNKER` for `event.otherShip`.
- Add unit tests covering: bunker processed for both ships, non-bunker processed for main ship only, and bunker processed when only the other ship resolves.

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt | Adds “process both ways” behavior for bunker encounters. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessorTest.kt | Adds tests validating bunker vs non-bunker processing paths. |

### github-actions[bot] — COMMENTED (2026-02-11)

Review completed. I've identified one critical potential deadlock issue that should be addressed. The implementation correctly handles bunker encounters for both ships, but the locking strategy needs adjustment to prevent deadlocks.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — COMMENTED (2026-02-11)

_No comment._

### TeqJoostD — APPROVED (2026-02-11)

_No comment._

## Review Comments

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

`ShipBlacklistDatasource` is documented as “events will not be processed for these ships”, but the new bunker “both ways” path can still process `event.otherShip` even when its IMO is blacklisted. Consider filtering out `otherShipId` when `event.otherShip.imo in blacklistedShips` (and/or when resolving the ID) so blacklisted bunker vessels don’t get voyage updates via another ship’s event.
```suggestion
            val otherShipImo = event.otherShip.imo

            // Do not process bunker encounters for blacklisted bunker vessels.
            // This enforces the ShipBlacklistDatasource contract that blacklisted ships
            // should not receive event-based voyage updates, even indirectly as "otherShip".
            if (otherShipImo != null && otherShipImo in blacklistedShips) {
                log.trace { "Skipping bunker 'otherShip' processing for blacklisted IMO $otherShipImo" }
                null
            } else {
                otherShipImo?.let { staticShipInfoService.getShipIdByImo(it) }
                    ?: event.otherShip.mmsi.let { staticShipInfoService.getShipIdByMmsi(it) }
            }
```

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

`listOfNotNull(shipId, otherShipId)` can contain the same ID twice (e.g., if the encounter is malformed/self-referential or both identifiers resolve to the same canonical shipId). That would double-process the same event for one ship and inflate metrics/changes. Consider de-duplicating before iterating (e.g., `distinct()`) and/or explicitly guarding against `shipId == otherShipId`.

### Copilot — 2026-02-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

The `enableBarges` gate (“only process events for ships with an IMO”) is currently applied only to `event.ship`. With the new bunker “both ways” logic, `otherShipId` can still be resolved via MMSI even when `enableBarges` is false and `event.otherShip.imo` is null, which would process a barge/service vessel contrary to the configuration. Consider applying the same IMO-only restriction when deciding whether to include `otherShipId`.
```suggestion
            val otherImo = event.otherShip.imo
            val otherMmsi = event.otherShip.mmsi

            // When barges are disabled, only process the other ship if it has an IMO.
            if (!processingProperties.enableBarges && otherImo == null) {
                null
            } else {
                otherImo?.let { staticShipInfoService.getShipIdByImo(it) }
                    ?: otherMmsi?.let { staticShipInfoService.getShipIdByMmsi(it) }
            }
```

### TeqJoostD — 2026-02-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

its also possible that a meteor will hit the amazon servers running this code, do we have enough protection for that?
