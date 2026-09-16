---
id: github:teqplay/vesselvoyage-backend:issue:45
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 45
title: When Getting The Ongoing Trace Of An Entry That Is More Than 30 Days Long,
  Fallback On Fetching Ais History From Platform
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/45
labels: []
explicit_links: []
---
# Issue #45: When Getting The Ongoing Trace Of An Entry That Is More Than 30 Days Long, Fallback On Fetching Ais History From Platform

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/45  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d58d8fe99e19...fc3407e08cf6](https://github.com/teqplay/vesselvoyage-backend/compare/d58d8fe99e19...fc3407e08cf6)
**Merge commit:** [fc3407e08cf6](https://github.com/teqplay/vesselvoyage-backend/commit/fc3407e08cf6)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/long_ongoing_voyages](https://github.com/teqplay/vesselvoyage-backend/tree/fix/long_ongoing_voyages)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-01-24T09:54:29.331475+00:00
**Status:** MERGED

When requesting the trace of an ongoing visit/voyage, VesselVoyage uses it’s ongoingTraceDataSource. This datasource keeps simplified traces for the last 30 days. 

When an ongoing visit/voyage is longer than 30 days, you did get a partial trace: only the last 30 days. This PR fixes this by falling back on fetching trace from platform instead in such cases.

Example of the issue: [https://vesselvoyage.teqplay.nl/#/ships/9723514/story](https://vesselvoyage.teqplay.nl/#/ships/9723514/story)

