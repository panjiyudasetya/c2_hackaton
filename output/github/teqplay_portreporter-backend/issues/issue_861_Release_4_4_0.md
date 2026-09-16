---
id: github:teqplay/portreporter-backend:issue:861
source: github
type: issue
repo: teqplay/portreporter-backend
number: 861
title: Release 4.4.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/861
labels: []
explicit_links: []
---
# Issue #861: Release 4.4.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/861  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [c7872fbfba38...13d21d4f1fac](https://github.com/teqplay/portreporter-backend/compare/c7872fbfba38...13d21d4f1fac)
**Merge commit:** [13d21d4f1fac](https://github.com/teqplay/portreporter-backend/commit/13d21d4f1fac)
**Author:** Shravan Shetty
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2021-03-08T13:38:16.245339+00:00
**Status:** MERGED

* Generic:

    * PortCallEventUtils: cancel berth eta with source cancel
    * Package restructure
    * adding pbp eta, berth ata,atd,eta,etd to the timestamps of anchorreporter
    * do not show cancelled events in the sof
    * fixes and updates for official reporting configurable. Multiple subscriptions on 12h, 24h can now be triggered
    
* USHOU related:

    * update: added nxtport ingestion endpoint. some cleanup of multiple authToken/credentials models
    * fix: fetch any vopak nomination for subscriptions
    * fix: do not add empty draught
    
* Invoice related:

    * fix: issue with invoice grouping when invoiceOptions are disabled
    * update: making invoice grouping/csv export more efficient
    


