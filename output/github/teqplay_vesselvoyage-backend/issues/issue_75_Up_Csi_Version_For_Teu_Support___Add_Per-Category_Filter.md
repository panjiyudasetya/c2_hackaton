---
id: github:teqplay/vesselvoyage-backend:issue:75
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 75
title: Up Csi Version For Teu Support & Add Per-Category Filter
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/75
labels: []
explicit_links:
- jira:SPV-1010
---
# Issue #75: Up Csi Version For Teu Support & Add Per-Category Filter

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/75  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [a08392e2078f...6ef7440ba92b](https://github.com/teqplay/vesselvoyage-backend/compare/a08392e2078f...6ef7440ba92b)
**Merge commit:** [6ef7440ba92b](https://github.com/teqplay/vesselvoyage-backend/commit/6ef7440ba92b)
**Author:** Former user
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feature/SPV-1010-per-category-filter](https://github.com/teqplay/vesselvoyage-backend/tree/feature/SPV-1010-per-category-filter)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-07-04T07:32:07.670201+00:00
**Status:** MERGED

In SmartFleet a feature is needed to be able to filter on categories, but also on DWT/TEU within those categories.

For example filtering on `TANKER` categories with DWT between A-B and `CARGO` categories with DWT between C-D.

VesselVoyage needs to be extended so SmartFleet can query based on this filter.

