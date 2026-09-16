---
id: github:teqplay/vesselvoyage-backend:issue:44
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 44
title: Implement Endpoint To Get Berth Details From Poma
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/44
labels: []
explicit_links: []
---
# Issue #44: Implement Endpoint To Get Berth Details From Poma

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/44  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [9a6e86c7d9a1...7791c9900354](https://github.com/teqplay/vesselvoyage-backend/compare/9a6e86c7d9a1...7791c9900354)
**Merge commit:** [7791c9900354](https://github.com/teqplay/vesselvoyage-backend/commit/7791c9900354)
**Author:** Jos de Jong
**Reviewers:** Wouter Naloop
**Approvers:** Former user, Wouter Naloop
**Source Branch:** [feat/berth_details_endpoint](https://github.com/teqplay/vesselvoyage-backend/tree/feat/berth_details_endpoint)
**Destination Branch:** [feat/berth_events](https://github.com/teqplay/vesselvoyage-backend/tree/feat/berth_events)
**Closed On:** 2022-01-21T13:39:32.632017+00:00
**Status:** MERGED



* Fix using the VesselVoyage `Location` instead of the PoMa `Location` in PoMa models
* Implement endpoint to get the `Berth` from PoMa by the berthId that is stored in the platform's `UniqueBerthEvent.berthId` \(this is _not_ the unique id of the berth in PoMa\)

@{5d7f358247b4570c41cc30b0} questions: 

1. currently I use the search endpoint because I didn’t see a way to search by the platform's berthId, is that the best way right now?
2. It would be nice if I could import the data models of PoMa instead of copy/pasting :grin: , is that something we can put in the backlog?


