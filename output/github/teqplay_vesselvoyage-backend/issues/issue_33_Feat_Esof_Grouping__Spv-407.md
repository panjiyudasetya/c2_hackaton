---
id: github:teqplay/vesselvoyage-backend:issue:33
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 33
title: Feat/Esof Grouping (Spv-407)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/33
labels: []
explicit_links: []
---
# Issue #33: Feat/Esof Grouping (Spv-407)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/33  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ce22fe51b72b...69be85dc840c](https://github.com/teqplay/vesselvoyage-backend/compare/ce22fe51b72b...69be85dc840c)
**Merge commit:** [69be85dc840c](https://github.com/teqplay/vesselvoyage-backend/commit/69be85dc840c)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/esof_grouping](https://github.com/teqplay/vesselvoyage-backend/tree/feat/esof_grouping)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-12-30T08:17:00.111122+00:00
**Status:** MERGED

This is big PR, sorry for that. Halfway implementation it turned out a refactor was needed.

This PR implements grouping encounters and stops in the right e-sof. That can be the current visit but also the previous visit or the voyage in between. Determining on which visit an event belongs can only \(partly\) be determined afterwards, depending on the voyage duration. This means that in the code we no longer make changes in the current Visit/Voyage only, but also in the previous. We need to pass around the ShipStatus consisting of current visit and previous voyage and previous visit.

Overview of the changes:

* Refactor visitUtils and voyageUtils into entryUtils, where we pass `VisitShipStatus` and `VoyageShipStatus` around \(instead of just the current Visit/Voyage\). The actual logic isn't changed.
* Now that all functions pass `ShipStatus`, and every visit/voyage inside this status may have changed, it becomes hard to determine the list with changes returned by the `processEvent` functions. But the new structure of working with `ShipStatus` everywhere also makes it easy to _automate_ generation of the list with `changes`. This is what the new util function `createChangeList` does: take the original status, and one or multiple state changes, and determine the minimal list with what is changed.  
  Remark: the function cannot detect deletions right now, only creates and updates.
* Implement new esofUtils functions to split \(partition\) and regroup ESof's. Most importantly `regroupESof`, which can regroup the ESof's of a series: `visitBefore - voyage - visitAfter`. The logic currently is the following \(can be refined in the future\):

    * events within 4 hours of the start of the end of the first visit are grouped in that visit
    * events within 24 hours before the start of the last visit are grouped there
    * the rest of the events is grouped in the voyage
    
* The `regroupESof` function is called when a new visit or a new voyage is started, and when an update is made in the e-sof \(after an encounter, movement, or status changed event comes in\)
* The functions `processEncounterEvent`, `processMovementEvent`, and `processStatusChangedEvent` now need to take care that a new event can be part of one of multiple e-sofs \(current visit/voyage, previous vsit/voyage. They now use the “trick“ to first merge all esofs, add the new event to the merged esof, and after that split the esof again.


