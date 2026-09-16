---
id: github:teqplay/vesselvoyage-backend:issue:157
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 157
title: Spv-1889 Single Platform Url
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/157
labels: []
explicit_links:
- jira:SPV-1889
---
# Issue #157: Spv-1889 Single Platform Url

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/157  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [958d934b39df...7d9dacee952e](https://github.com/teqplay/vesselvoyage-backend/compare/958d934b39df...7d9dacee952e)
**Merge commit:** [7d9dacee952e](https://github.com/teqplay/vesselvoyage-backend/commit/7d9dacee952e)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1889-single-platform-url](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1889-single-platform-url)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-01-30T13:35:31.740471+00:00
**Status:** MERGED

* Updated the VesselVoyage default properties to instead use a single platform url which is the internalapi dev
* Adjusted the code removing any use of multiple platform connections
* adjusted test as it only requests a single event history
* Updated bean names to not mention anything about global or pronto

