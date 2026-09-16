---
id: github:teqplay/vesselvoyage-backend:issue:269
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 269
title: Spv-2205 Track Ongoing Visits
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/269
labels: []
explicit_links:
- jira:SPV-2205
---
# Issue #269: Spv-2205 Track Ongoing Visits

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/269  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3a0a63f2b238...b21302512223](https://github.com/teqplay/vesselvoyage-backend/compare/3a0a63f2b238...b21302512223)
**Merge commit:** [b21302512223](https://github.com/teqplay/vesselvoyage-backend/commit/b21302512223)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2205-track-ongoing-visits](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2205-track-ongoing-visits)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-08T09:47:59.359518+00:00
**Status:** MERGED

Track the total amount of active visits, voyages and initial ship statuses.
You can already see the stats working at [https://grafanadev.teqplay.nl/d/NdlJ2Zn4z/vesselvoyage?orgId=1](https://grafanadev.teqplay.nl/d/NdlJ2Zn4z/vesselvoyage?orgId=1) ~~I’m still a bit clueless why there are so many spikes on the side of loading visits/voyages but have to do some deep diving to understand that~~
Okay I ended up using a wrong function to query what I wanted, which was showing the derivative

