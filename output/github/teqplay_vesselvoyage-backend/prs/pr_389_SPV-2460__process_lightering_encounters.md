---
id: github:teqplay/vesselvoyage-backend:pr:389
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 389
title: 'SPV-2460: process lightering encounters'
author: leonjoosse
state: closed
date: '2025-01-13'
merged_at: '2025-01-17'
base_branch: develop
head_branch: SPV-2460-lightering-encounters
url: https://github.com/teqplay/vesselvoyage-backend/pull/389
labels: []
linked_issues: []
explicit_links: []
---
# PR #389: SPV-2460: process lightering encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/389  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2460-lightering-encounters`  
**Created:** 2025-01-13  
**Merged:** 2025-01-17  

## Description

This PR adds ship-to-ship events to the SOF

Data flow:

- `EncounterMonitor` posts an EncounterEvent on the message bus, with `type=SHIP_TO_SHIP`
- The event is received by VesselVoyage in `EventsDefaultMessageProcessor.processEvent()`
- The event is _not_ converted to an EncounterEvent, but rather to a `ShipToShipTransferEvent`
- The event flows through the `EntryProcessingService.insertNew()`, then `EventProcessingService.onEvent()`
- The `ShipToShipTransferEventProcessor` processes the event and adds it to the `NewESof` object.


## Commits

- `e381512c` **leonj** (2025-01-10): Add ShipToShipEncounter, this is actually an Encounter but with specific information (areaId) for a ship-to-ship encounter (for a lightering scenario).
  The Encounter and ShipToShipEncounter have almost all properties in common, therefore add an interface with the shared fields.
- `87f99904` **leonj** (2025-01-10): Add ShipToShip event processor. For now, this is almost the same as EncounterProcessor, therefore allow ShipToShipEncounterProcessor to extend from EncounterProcessor
- `89fa2b2f` **leonj** (2025-01-10): Incorporate the ShipToShipProcessor into the EventProcessingService
- `122a084b` **leonj** (2025-01-13): Rename ShipToShipEncounter to ShipToShipTransfer.
  Remove parent interface for EncounterEvent and ShipToShipTransfer, as we will treat it as a fully separate encounter (service vessel vs non service vessel)
- `f9734747` **leonj** (2025-01-13): Add ShipToShipTransfers to NewESoF
- `e8910803` **leonj** (2025-01-13): Add test for convertAisEngineEvent for ShipToShip events
- `368ff634` **leonj** (2025-01-14): Upgrade aisengine dependency 0.27.1 -> 0.29.0, to incorporate EncounterType and ship-to-ship metadata changes
- `318e99b8` **leonj** (2025-01-14): Update ShipToShipTransfer processors to extend from EventProcessor instead of EsofEventProcessor, the ShipToShipTransfer processors don't need the extensive detail of the EsofEventProcessor
- `8514542e` **leonj** (2025-01-14): When converting an AISEngine event for ship to ship, use the STSEncounterMetadata to retrieve the areaId
- `c269c974` **leonj** (2025-01-14): Add tests for the event processing, this also tests the ShipToShipTransfer processors
- `5505f37b` **leonj** (2025-01-14): Upgrade skeleton-plugins: 1.3.0 -> 1.9.7, as skeleton-plugins dependency in ais-engine causes a conflict (is already at 1.9.7)
- `31acd0f7` **leonj** (2025-01-14): Merge branch 'develop' into SPV-2460-lightering-encounters
- `76781acd` **leonj** (2025-01-14): Make NewEsof.shipToShipTransfers nullable, to allow serialization from earlier NewEsof objects from the database
- `29c47546` **leonj** (2025-01-14): Make NewEsof.shipToShipTransfers empty list by default, to allow serialization from earlier NewEsof objects from the database
- `6ff12b7a` **leonj** (2025-01-14): Merge remote-tracking branch 'origin/SPV-2460-lightering-encounters' into SPV-2460-lightering-encounters
  # Conflicts:
  #	api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewESoF.kt
- `5d717dc0` **TeqJoostD** (2025-01-15): feat: add logging
- `750f0b9c` **TeqJoostD** (2025-01-15): Merge remote-tracking branch 'origin/develop' into SPV-2460-lightering-encounters
  # Conflicts:
  #	api/src/main/kotlin/nl/teqplay/vesselvoyage/model/v2/NewESoF.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingService.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/util/esofUtils.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/util/TestUtil.kt
- `b64062aa` **TeqJoostD** (2025-01-15): fix: merge conflict
- `661f2b4c` **TeqJoostD** (2025-01-15): fix: merge conflict
- `06ea747a` **leonj** (2025-01-16): Fix last test
- `58d6e3a0` **leonj** (2025-01-16): Merge remote-tracking branch 'origin/SPV-2460-lightering-encounters' into SPV-2460-lightering-encounters
- `6e238b1c` **leonj** (2025-01-16): Fix tests
- `6298c3a5` **TeqJoostD** (2025-01-16): fix: add logging
- `e190cd59` **TeqJoostD** (2025-01-16): Merge remote-tracking branch 'origin/SPV-2460-lightering-encounters' into SPV-2460-lightering-encounters
- `032e16d1` **leonj** (2025-01-16): Merge remote-tracking branch 'origin/SPV-2460-lightering-encounters' into SPV-2460-lightering-encounters
- `5998afb3` **TeqJoostD** (2025-01-16): fix: add logging
- `42bc3239` **TeqJoostD** (2025-01-16): Merge remote-tracking branch 'origin/SPV-2460-lightering-encounters' into SPV-2460-lightering-encounters
- `d3a865da` **TeqJoostD** (2025-01-16): fix: ktlint
- `ec89ab64` **TeqJoostD** (2025-01-16): feat: dont check rabbitMQ health when not configured
- `1b862551` **TeqJoostD** (2025-01-17): fix: remove redundant logging
- `9da89d56` **leonj** (2025-01-17): Fix metric registry for ShipToShipTransferProcessor

## Reviews

### TeqJoostD — APPROVED (2025-01-14)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-01-17)

_No comment._

## Review Comments

### Darius-Wattimena — 2025-01-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsSchedulerService.kt`

Please don't forget to remove this before merging

## Comments

### leonjoosse — 2025-01-14

The upgrade of `aisengine` 0.27.1 --> 0.29.0 introduced some change in the configuration behavior, still checking that. The build fails, but the place where is fails is unrelated, so stuff can still be reviewed already.

### TeqJoostD — 2025-01-14

I have started 20 minutes ago.
