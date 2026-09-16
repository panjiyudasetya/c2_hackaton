---
id: github:teqplay/csi-backend:issue:3
source: github
type: issue
repo: teqplay/csi-backend
number: 3
title: Shipcontroller
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/3
labels: []
explicit_links: []
---
# Issue #3: Shipcontroller

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/3  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [2dcaf7bd0d2b...977371cd6183](https://github.com/teqplay/csi-backend/compare/2dcaf7bd0d2b...977371cd6183)
**Merge commit:** [977371cd6183](https://github.com/teqplay/csi-backend/commit/977371cd6183)
**Author:** Former user
**Reviewers:** Michel Wilson
**Approvers:** Michel Wilson
**Source Branch:** [shipController](https://github.com/teqplay/csi-backend/tree/shipController)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2019-05-21T11:05:47.640751+00:00
**Status:** MERGED

* Added initial version of ship controller

    Search for ships including a search query option


* Sort ship search query results
* Add test for ship controller

Endpoints are created for getting the ship, either single or multiple, with: id, mmsi, imo and eni. Also the ship search endpoint from the platform is implemented.

The object that’s returned can’t be made compatible with the current platform endpoints, most of the data exists \(on another json path\) but there is no dynamic data like location or speed \(which is also returned with the platform endpoints\). For now the CSI model is used as returned object in these new endpoints.

