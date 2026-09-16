---
id: github:teqplay/vesselvoyage-backend:issue:55
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 55
title: Speed Up Startup Time By Caching Ships/Ports/Anchorages On Disk
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/55
labels: []
explicit_links: []
---
# Issue #55: Speed Up Startup Time By Caching Ships/Ports/Anchorages On Disk

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/55  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8a186cca4f02...cdaaef10df23](https://github.com/teqplay/vesselvoyage-backend/compare/8a186cca4f02...cdaaef10df23)
**Merge commit:** [cdaaef10df23](https://github.com/teqplay/vesselvoyage-backend/commit/cdaaef10df23)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/cache_on_disk](https://github.com/teqplay/vesselvoyage-backend/tree/feat/cache_on_disk)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-14T13:05:33.802015+00:00
**Status:** MERGED

Before, VesselVoyage would fetch all ships, ports, anchorages on startup and refresh them once every 24h. Especially during local development a slow startup is frustrating.

This PR implements the following logic:

* Once every 24h and right _after_ startup, all the ships/ports/anchorages are fetched and stored in a temp file on disk
* During startup, the ships/ports/anchorages will be loaded from disk if present \(very fast\), and if not, will be fetched.

The gist:

* Implemented a `TempFileDataSource` to read/write files from disk
* Implemented a helper class `DiskCache` to model the \(fast\) loading from disk with fallback on fetching, and the refreshing.
* Use these classes to load ships \(from platform and CSI\), ports, anchorages during startup and refresh right after startup and once every 24h.
* Send a slack message when refreshing of data failed \(introduced a new util function `sendMessage` for that and use it everywhere in the application\)


