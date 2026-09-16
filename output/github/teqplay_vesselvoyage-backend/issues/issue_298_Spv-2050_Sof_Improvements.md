---
id: github:teqplay/vesselvoyage-backend:issue:298
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 298
title: Spv-2050 Sof Improvements
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/298
labels: []
explicit_links:
- jira:SPV-2050
---
# Issue #298: Spv-2050 Sof Improvements

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/298  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [58f777a77f8d...e776c8d4135e](https://github.com/teqplay/vesselvoyage-backend/compare/58f777a77f8d...e776c8d4135e)
**Merge commit:** [e776c8d4135e](https://github.com/teqplay/vesselvoyage-backend/commit/e776c8d4135e)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Former user
**Source Branch:** [SPV-2050-sof-improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2050-sof-improvements)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-14T10:27:21.899381+00:00
**Status:** MERGED

A couple of improvements:
* SOF `PortArea.end` must be nullable, otherwise ongoing visit breaks the SOF
* PTO SOF: allow esof to be null \(ongoing visits may not have an esof object yet, would be silly to just not generate any SOF, as there is other information to be published\)
* SOF: When matching port area to `berth.ports`, match on `port._id` AND `port.unlocode`. `berth.ports` is apparently \_id and unlocode mixed?
* Simplify `mapWithSurrounding` and add test

Changes to loading caches. For the SOF, the system needs the infra and ship objects. Both services need to load for all profiles, so loading them now as part of the class init instead of the `ApplicationReadyEvent`. 
* Execute blocking load of InfraCacheService, it needs to be ready before the application can serve content
* Execute blocking load of StaticShipInfoService, it needs to be ready before the application can serve content

