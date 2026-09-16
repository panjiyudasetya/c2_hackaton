---
id: github:teqplay/vesselvoyage-backend:issue:318
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 318
title: Fix Scenario Status
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/318
labels: []
explicit_links: []
---
# Issue #318: Fix Scenario Status

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/318  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [54c708f60202...fe37e7c431b9](https://github.com/teqplay/vesselvoyage-backend/compare/54c708f60202...fe37e7c431b9)
**Merge commit:** [fe37e7c431b9](https://github.com/teqplay/vesselvoyage-backend/commit/fe37e7c431b9)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Wouter Naloop
**Approvers:** Leon Joosse
**Source Branch:** [fix-scenario-status](https://github.com/teqplay/vesselvoyage-backend/tree/fix-scenario-status)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-15T09:18:51.391350+00:00
**Status:** MERGED

This code/endpoint is only triggered by revents. It always overridden the existing result, meaning we would lose any info about who, what and how the scenario was triggered.
The top one is with the fix, while the other two, that got triggered by VesselVoyage itself did get overriden by a non database one
![](https://bitbucket.org/repo/k5G8e7j/images/422260640-Screenshot%202024-08-09%20at%2017.12.39.png)

