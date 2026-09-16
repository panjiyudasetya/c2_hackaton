---
id: github:teqplay/vesselvoyage-backend:issue:146
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 146
title: Spv-1806 Rework Ship Cache
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/146
labels: []
explicit_links: []
---
# Issue #146: Spv-1806 Rework Ship Cache

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/146  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [03f40d28bd02...1d8e9eda99d1](https://github.com/teqplay/vesselvoyage-backend/compare/03f40d28bd02...1d8e9eda99d1)
**Merge commit:** [1d8e9eda99d1](https://github.com/teqplay/vesselvoyage-backend/commit/1d8e9eda99d1)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1806_rework_ship_cache](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1806_rework_ship_cache)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-09-27T09:05:33.279993+00:00
**Status:** MERGED

* Reduced the platform dependency and rely more on CSI
* Removed any calls to the platform or csi ship clients and instead fully rely on the local cache to be consistent with the provided result
* Removed unused imports
* Adjusted tests to also only make use of the CSI cache and ignore the result from platform
* Removed platform dependency on startup
* Make sure only valid ships with mmsi and imo get loaded in any caches
* Changed logging on how many CSI ships are being loaded
* removed the use of the cached ship client in tests
* removed any remaining traces of using platform directly instead of using the ship cache
* removed unused configuration properties
* ktlint

