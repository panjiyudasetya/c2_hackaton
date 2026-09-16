---
id: github:teqplay/vesselvoyage-backend:issue:27
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 27
title: Feat/Spv-152 E-Sof
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/27
labels: []
explicit_links:
- jira:SPV-152
---
# Issue #27: Feat/Spv-152 E-Sof

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/27  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d81773690752...51ebe125a950](https://github.com/teqplay/vesselvoyage-backend/compare/d81773690752...51ebe125a950)
**Merge commit:** [51ebe125a950](https://github.com/teqplay/vesselvoyage-backend/commit/51ebe125a950)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/SPV-152-e-sof](https://github.com/teqplay/vesselvoyage-backend/tree/feat/SPV-152-e-sof)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:38.999995+00:00
**Status:** MERGED

In the frontend on DEV you can see what is in the e-sof: [https://vesselvoyagedev.teqplay.nl](https://vesselvoyagedev.teqplay.nl) . On the story page of a ship, you can expand every visit/voyage with the arrow on the right to see the e-sof. To see e-sof events longer ago you’ll need to recalculate the ship. Events like StatusChangedEvent exist only recently and movement events is enabled only recently on BACKENDGLOBAL, so you’ll not see these in the past.

In short:

* VesselVoyage now processed three new TeqplayEvents: `ShipMovingEvent`, `StatusChangedEvent`, and  `TeqplayLocationBasedEvent` for encounters
* The `Visit` and `Voyage` models are extended with a property `ESof`. The `ESof` contains:

    * stops based on `MovementEvent` and enriched with `StatusChangedEvent` to determine whether dealing with an anchorage or berth stop\)
    * encounters based on EncounterEvent\)
    
* Some refactoring in `processEtaEvent` and `processDestinationChangedEvent` to simplify the code
* I’ve extended `VisitShipStatus` and `VoyageShipStatus` to keep track on the previousVoyage and previousVisit. This extra information is needed in the future to be able to put ESof events in the right visit \(current or previous\). But not yet used right now.
* Unit tests for all the new stuff

Most important limitation right now is that the e-sof events are currently added to the visit/voyage that is ongoing at the moment of the event. In a following step we’ll attach it to the corresponding visit. For example pilot events typically happen when the visit is not yet started, but we consider them part of the visit and not the voyage. And the frontend needs some polishing.


