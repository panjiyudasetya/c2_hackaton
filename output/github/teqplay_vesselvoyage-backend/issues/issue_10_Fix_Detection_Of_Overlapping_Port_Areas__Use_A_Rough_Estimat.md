---
id: github:teqplay/vesselvoyage-backend:issue:10
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 10
title: 'Fix Detection Of Overlapping Port Areas: Use A Rough Estimate Of The Distance
  Between Two Areas Instead Of The (Inner) Area Polygons'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/10
labels: []
explicit_links: []
---
# Issue #10: Fix Detection Of Overlapping Port Areas: Use A Rough Estimate Of The Distance Between Two Areas Instead Of The (Inner) Area Polygons

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/10  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [025f7fb576a2...e8526fd3f312](https://github.com/teqplay/vesselvoyage-backend/compare/025f7fb576a2...e8526fd3f312)
**Merge commit:** [e8526fd3f312](https://github.com/teqplay/vesselvoyage-backend/commit/e8526fd3f312)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/overlapping_port_areas](https://github.com/teqplay/vesselvoyage-backend/tree/fix/overlapping_port_areas)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-03T09:30:21.692070+00:00
**Status:** MERGED

So the underlying difficulty here is: VesselVoyage needs the outer area polygon of all port areas, but this is currently calculated in platform on the fly with certain logic, so that’s not really possible.  
  
@{5c57efac4912b735b9e0646c} can you have a look to see whether the solution I made makes sense to you. It’s not an ideal solution but I’m afraid that making a really perfect solution costs a lot of effort and still isn’t guaranteed to keep working in the future \(the logic used by platform to calculate the outer port areas must be copied into VesselVoyage and kept in sync or something like that\).  
  
@{5d7f358247b4570c41cc30b0} maybe interesting to be aware of this issue too from a PoMa perspective. In the long term, a proper solution \(I think\) would be if platform no longer calculates the port outer area itself, but when it is fully defined and stored in PoMa. Then both platform and VesselVoyage could use the same outer area polygon and all would be roze wolkjes and sunshine.

