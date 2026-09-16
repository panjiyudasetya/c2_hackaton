---
id: github:teqplay/vesselvoyage-backend:issue:86
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 86
title: Spv-1045 Improve Csi Cache Use
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/86
labels: []
explicit_links: []
---
# Issue #86: Spv-1045 Improve Csi Cache Use

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/86  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [083ee243f4b7...038b8c60df50](https://github.com/teqplay/vesselvoyage-backend/compare/083ee243f4b7...038b8c60df50)
**Merge commit:** [038b8c60df50](https://github.com/teqplay/vesselvoyage-backend/commit/038b8c60df50)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [SPV-1045_improve_csi_cache_use](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1045_improve_csi_cache_use)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-08-18T08:44:46.784375+00:00
**Status:** MERGED

* Changed the CSI caches to instead make use of only 1 cache that keeps track of the full ShipRegisterInfoCache for each IMO
* ktlint format


