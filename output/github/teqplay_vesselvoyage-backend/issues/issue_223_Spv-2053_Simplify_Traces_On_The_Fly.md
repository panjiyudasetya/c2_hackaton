---
id: github:teqplay/vesselvoyage-backend:issue:223
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 223
title: Spv-2053 Simplify Traces On The Fly
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/223
labels: []
explicit_links: []
---
# Issue #223: Spv-2053 Simplify Traces On The Fly

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/223  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [7ba4aea8ecf5...89dcb9de9248](https://github.com/teqplay/vesselvoyage-backend/compare/7ba4aea8ecf5...89dcb9de9248)
**Merge commit:** [89dcb9de9248](https://github.com/teqplay/vesselvoyage-backend/commit/89dcb9de9248)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2053-simplify-traces-on-the-fly](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2053-simplify-traces-on-the-fly)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-29T09:12:37.525457+00:00
**Status:** MERGED

This PR adds the following functionality:
* Real-time trace simplification \(no create and update\)
    * After having more than 100 trace points in the ongoing trace, simplify all points and use the last location for the new ongoing trace
    * Adds the simplification logic of the already used library in V1
    * Adds location deduping as the library doesn’t clean up if you provide multiple times the same location.
    
* Debug endpoint to get an ongoing trace and simplified trace stitched together

