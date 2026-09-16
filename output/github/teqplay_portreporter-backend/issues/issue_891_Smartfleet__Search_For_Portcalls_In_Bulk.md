---
id: github:teqplay/portreporter-backend:issue:891
source: github
type: issue
repo: teqplay/portreporter-backend
number: 891
title: 'Smartfleet: Search For Portcalls In Bulk'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/891
labels: []
explicit_links: []
---
# Issue #891: Smartfleet: Search For Portcalls In Bulk

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/891  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ae7f5e9f2108...2b88f677ad08](https://github.com/teqplay/portreporter-backend/compare/ae7f5e9f2108...2b88f677ad08)
**Merge commit:** [2b88f677ad08](https://github.com/teqplay/portreporter-backend/commit/2b88f677ad08)
**Author:** Former user
**Reviewers:** Shravan Shetty, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [smartfleet/fine-tune-portcall-search](https://github.com/teqplay/portreporter-backend/tree/smartfleet/fine-tune-portcall-search)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-05-17T08:19:27.043606+00:00
**Status:** MERGED

Related card:  
[https://trello.com/c/QdMo888y/8581-43-fine-tune-improve-speed-of-portcall-search-for-a-visit-by-providing-from-and-to-times](https://trello.com/c/QdMo888y/8581-43-fine-tune-improve-speed-of-portcall-search-for-a-visit-by-providing-from-and-to-times)

The calls for SmartFleet to get the fleet and a specific ship voyage within a fleet used to take around 8 seconds, because for all visits times the amount of voyages the portcalls were requested.

Now it’s done in bulk, so the request is done only once and the data is just filtered after. Now the request are decreased to around ~150-200ms.

