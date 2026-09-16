---
id: github:teqplay/vesselvoyage-backend:issue:297
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 297
title: Spv-2251 Adjust Endpoint To Frontend Needs
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/297
labels: []
explicit_links: []
---
# Issue #297: Spv-2251 Adjust Endpoint To Frontend Needs

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/297  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ec164fffb8a5...bf835e52501e](https://github.com/teqplay/vesselvoyage-backend/compare/ec164fffb8a5...bf835e52501e)
**Merge commit:** [bf835e52501e](https://github.com/teqplay/vesselvoyage-backend/commit/bf835e52501e)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2251-adjust-endpoint-to-frontend-needs](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2251-adjust-endpoint-to-frontend-needs)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-26T10:23:13.369163+00:00
**Status:** MERGED

Fixing some things synced with David today:
* Time range optional in `/byPort` visit/voyage endpoints
* `voyage/byPort` provided port lists are now not all required but instead only one of them should be sufficient
* You can now filter by `ShipCategoriesV2` like you can do currently in the VesselVoyage frontend
* Add logic to fill in the `previous.port` and `next.port` in the mappers
* Add logic to determine the `finished` flag in the mappers

