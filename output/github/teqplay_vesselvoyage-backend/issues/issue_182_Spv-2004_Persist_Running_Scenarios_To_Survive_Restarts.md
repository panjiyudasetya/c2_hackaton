---
id: github:teqplay/vesselvoyage-backend:issue:182
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 182
title: Spv-2004 Persist Running Scenarios To Survive Restarts
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/182
labels: []
explicit_links: []
---
# Issue #182: Spv-2004 Persist Running Scenarios To Survive Restarts

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/182  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [725233a275af...ebe0757cc1a7](https://github.com/teqplay/vesselvoyage-backend/compare/725233a275af...ebe0757cc1a7)
**Merge commit:** [ebe0757cc1a7](https://github.com/teqplay/vesselvoyage-backend/commit/ebe0757cc1a7)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2004-persist-running-scenarios-to-survive-restarts](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2004-persist-running-scenarios-to-survive-restarts)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-26T08:43:27.315855+00:00
**Status:** MERGED

This PR fixes the issue of a restart clearing the `runningScenarios` list. Now that’s persisted in the `revents.recalculations` collection.
The model is also changed a little to contain both the `revents.scenarioId` as well as the `revents.phase`, which is one of `QUEUED, PROGRESSING, FINISHED, STOPPED`.
```json
{
    "startedAt": "2024-03-15T12:46:00.177+01:00",
    "imo": 9803704,
    "revents": {
        "scenarioId": "1fb60e00-1148-401d-90f2-dbeb26a4be46",
        "phase": "QUEUED"
    },
    "_id": "1fb60e00-1148-401d-90f2-dbeb26a4be46"
}
```
Also some endpoints have been added to get recalculations:
* listing all, `GET /v2/recalculation`
* listing all for a specific IMO, `GET /v2/recalculation/ship/{imo}`
* listing a specific one, `GET /v2/recalculation/{id}`
This would allow us to add a page in the frontend, akin to CircleCI, showing the \(r\)events “jobs” and their progress of being merged back into VesselVoyage. Currently the model is very simple, it contains the bare-minimum, so it’s missing some values that could be useful to a user, like `start` and `end` times. That can be added later when thinking about how the frontend would look and what it would need.

