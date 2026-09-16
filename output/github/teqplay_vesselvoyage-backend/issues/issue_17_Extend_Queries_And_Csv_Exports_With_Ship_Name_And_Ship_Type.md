---
id: github:teqplay/vesselvoyage-backend:issue:17
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 17
title: Extend Queries And Csv Exports With Ship Name And Ship Type
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/17
labels: []
explicit_links: []
---
# Issue #17: Extend Queries And Csv Exports With Ship Name And Ship Type

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/17  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [1399e1e7f29d...9d320ff3c844](https://github.com/teqplay/vesselvoyage-backend/compare/1399e1e7f29d...9d320ff3c844)
**Merge commit:** [9d320ff3c844](https://github.com/teqplay/vesselvoyage-backend/commit/9d320ff3c844)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/extend_query_with_ship_name](https://github.com/teqplay/vesselvoyage-backend/tree/feat/extend_query_with_ship_name)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-30T09:20:24.807969+00:00
**Status:** MERGED

* Create two new query endpoints for visits/voyages, returning ExtendedVisit and ExtendedVoyage: a wrapper holding both the entry and the ship details
* Extend the CSV exports with two new columns: ship name, ship type
* Unify ShipDetails in the application, use this instead of StaticShipInfo. We may want to change this to the CSI model as soon as VesselVoyage gets it’s data directly from CSI.
* Cache the StaticShipInfo fetched from CSI \(via the platform proxy\)

This backend PR and corresponding frontend PR are deployed on DEV,  [https://vesselvoyagedev.teqplay.nl/#/visits](https://vesselvoyagedev.teqplay.nl/#/visits) , you can try it out there

