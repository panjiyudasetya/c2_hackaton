---
id: github:teqplay/vesselvoyage-backend:issue:237
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 237
title: Spv-2118 More Area Support Improve Area Activity Generics
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/237
labels: []
explicit_links: []
---
# Issue #237: Spv-2118 More Area Support Improve Area Activity Generics

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/237  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [6586c477fc97...ab70ec24f119](https://github.com/teqplay/vesselvoyage-backend/compare/6586c477fc97...ab70ec24f119)
**Merge commit:** [ab70ec24f119](https://github.com/teqplay/vesselvoyage-backend/commit/ab70ec24f119)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [SPV-2118-more-area-support-improve-area-activity-generics](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2118-more-area-support-improve-area-activity-generics)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-17T12:37:49.594531+00:00
**Status:** MERGED

This change became way bigger then I wanted it to be :confused:
* Made all `location` fields in all VesselVoyage events use the Skeleton `Location` model.
* Adjusted the `ActivityEventProcessor` so it doesn't need any abstract functions.

