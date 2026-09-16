---
id: github:teqplay/vesselvoyage-backend:issue:30
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 30
title: 'Feat: Implement Limits On All Relevant Requests To Make Sure The Server Cannot
  Run Out Of Memory'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/30
labels: []
explicit_links: []
---
# Issue #30: Feat: Implement Limits On All Relevant Requests To Make Sure The Server Cannot Run Out Of Memory

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/30  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [641fff366137...ce22fe51b72b](https://github.com/teqplay/vesselvoyage-backend/compare/641fff366137...ce22fe51b72b)
**Merge commit:** [ce22fe51b72b](https://github.com/teqplay/vesselvoyage-backend/commit/ce22fe51b72b)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/SPV-306_limit_requests](https://github.com/teqplay/vesselvoyage-backend/tree/feat/SPV-306_limit_requests)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-12-09T09:02:11.809908+00:00
**Status:** MERGED

Instead of just limiting the maximum amount of traces, I went through _all_ of the endpoints to add limits, so I made the scope of the Jira card a bit bigger :sweat_smile: .

* I added a `limit` parameter to all of the relevant queries in the data sources, but do not throw exceptions in the data sources

    In the controllers, I pass this `limit` and validate whether the limit is reached. If so, an exception is thrown. This way, it cannot happen that the user gets truncated, incomplete data without knowing it.


* I experimented on the DEV server with what a “suitable“ maximum is for the number of visits/voyages/traces. With a max of 10\_000 visits/voyages, and 1000 traces, all keeps running smoothly. 10x those amounts works but lets the server have a hard time.
* @{5c57efac4912b735b9e0646c} do you see issues in activating those limits? Any requests from SmartFleet for example that are on the edge or over these limits?

\(in the future, if we want to be able to do bigger requests, we can implement a streaming solution for those queries\)

