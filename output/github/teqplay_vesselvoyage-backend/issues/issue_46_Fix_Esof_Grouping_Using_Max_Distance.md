---
id: github:teqplay/vesselvoyage-backend:issue:46
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 46
title: Fix/Esof Grouping Using Max Distance
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/46
labels: []
explicit_links: []
---
# Issue #46: Fix/Esof Grouping Using Max Distance

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/46  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [fc3407e08cf6...3c1e6314b4d2](https://github.com/teqplay/vesselvoyage-backend/compare/fc3407e08cf6...3c1e6314b4d2)
**Merge commit:** [3c1e6314b4d2](https://github.com/teqplay/vesselvoyage-backend/commit/3c1e6314b4d2)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/esof_grouping_using_max_distance](https://github.com/teqplay/vesselvoyage-backend/tree/fix/esof_grouping_using_max_distance)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:38.793994+00:00
**Status:** MERGED

Improve e-sof grouping: should not group when the distance is to far from the port. For example in the following case, a ship anchored near hamburg at 2022-01-06, sailed to Rotterdam, anchored before Rotterdam, and then entered Rotterdam: [https://vesselvoyagedev.teqplay.nl/#/ships/9130432/story](https://vesselvoyagedev.teqplay.nl/#/ships/9130432/story) . The anchorage at hamburg was grouped as part of the Rotterdam visit, but that should not be the case.
* Extracted the logic to determine whether a stop/encounter is part of a visit into a function `isPartOfVisit`, and extended this logic to also recon with the distance. A stop/encounter is part of a visit when:
    * It took place during the visit
    * It took place shortly before or after the visit AND is in the neighborhood of the visit
    
* To be able to utilize the new function `isPartOfVisit`, I refactored the regrouping logic:
    * Implemented `ESof.groupBy` \(replacing the need for `ESof.partition`\)
    
        Refactored `VisitShipStatus.regroupESof` and `VoyageShipStatus.regroupESof` from splitting the esofs into three by partitioning twice into calling `ESof.groupBy` once.
    
    

