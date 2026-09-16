---
id: github:teqplay/vesselvoyage-backend:issue:41
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 41
title: Remove Ignoring Ships With Types Like Tug Or Fishing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/41
labels: []
explicit_links: []
---
# Issue #41: Remove Ignoring Ships With Types Like Tug Or Fishing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/41  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [5f8289238566...e263cddf4550](https://github.com/teqplay/vesselvoyage-backend/compare/5f8289238566...e263cddf4550)
**Merge commit:** [e263cddf4550](https://github.com/teqplay/vesselvoyage-backend/commit/e263cddf4550)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/filter_ship_types](https://github.com/teqplay/vesselvoyage-backend/tree/feat/filter_ship_types)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-01-11T07:27:22.314064+00:00
**Status:** MERGED

Instead of ignoring ships, the frontend page “Ports“ of VesselVoyage will implement a filter on ship type, utilizing the CSI ship types in `Filter.categoriesV1` that you \(@{5c57efac4912b735b9e0646c} \) recently implemented on all relevant endpoints. 

And also separately, the visit/voyage queries will be refactored to use the CSI ship types instead of the platform ship types.

