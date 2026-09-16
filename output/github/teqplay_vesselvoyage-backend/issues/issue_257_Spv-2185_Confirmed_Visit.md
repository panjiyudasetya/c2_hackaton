---
id: github:teqplay/vesselvoyage-backend:issue:257
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 257
title: Spv-2185 Confirmed Visit
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/257
labels: []
explicit_links: []
---
# Issue #257: Spv-2185 Confirmed Visit

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/257  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [366e90970481...647da79d0d23](https://github.com/teqplay/vesselvoyage-backend/compare/366e90970481...647da79d0d23)
**Merge commit:** [647da79d0d23](https://github.com/teqplay/vesselvoyage-backend/commit/647da79d0d23)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2185-confirmed-visit](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2185-confirmed-visit)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-25T14:42:57.316902+00:00
**Status:** MERGED

* Adjusted stop processing to confirm a visit when stopped inside a berth inside the port
* Changed dropping of ongoing EOSP area activities, so they are added as pass-through EOSP areas instead
* Moved stop visit confirming logic to the base processor so it can be used on end events as well
* Fixed an issue where an anchorage stop could be happening inside the previous visit when having a 0-second voyage
* Adjusted the logic so the current visit is replaced with a new one if we had an anchorage stop that was used by for more than the current visit port
* Changed logic so visits are finished when existing the confirmed port
* Adjusted the order of creating and deleting so we never end up with no visit when we have duplicate events
* code cleanup

