---
id: github:teqplay/vesselvoyage-backend:issue:234
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 234
title: Spv-2139 Dry Run Endpoints
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/234
labels: []
explicit_links: []
---
# Issue #234: Spv-2139 Dry Run Endpoints

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/234  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [67c78b684686...8c0060089ae5](https://github.com/teqplay/vesselvoyage-backend/compare/67c78b684686...8c0060089ae5)
**Merge commit:** [8c0060089ae5](https://github.com/teqplay/vesselvoyage-backend/commit/8c0060089ae5)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [dry-run-endpoints](https://github.com/teqplay/vesselvoyage-backend/tree/dry-run-endpoints)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-17T12:00:25.783971+00:00
**Status:** MERGED

* Added the `/v2/story/dryRun` endpoint to get something similar to the Story page in the frontend
    * Added support to load in all Poma entities for a ship story
    
* Cleaned up Poma entities, removing unneeded fields and added EOSP for port
* Added an `enableRealTime` flag so you can start with the processing profile locally without having to consume events and ais

