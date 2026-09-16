---
id: github:teqplay/vesselvoyage-backend:issue:210
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 210
title: 'Chore: Extract V1 Definition From Merging Logic'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/210
labels: []
explicit_links: []
---
# Issue #210: Chore: Extract V1 Definition From Merging Logic

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/210  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d0438190dfcb...7086b3e63ad4](https://github.com/teqplay/vesselvoyage-backend/compare/d0438190dfcb...7086b3e63ad4)
**Merge commit:** [7086b3e63ad4](https://github.com/teqplay/vesselvoyage-backend/commit/7086b3e63ad4)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2076-merging-v2-logic-extract-v1](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic-extract-v1)
**Destination Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Closed On:** 2024-04-17T09:56:18.168623+00:00
**Status:** MERGED

The `EntriesMergeService` was previously built to work with the V1 definitions. Now that the V2 definitions are introduced, this service will not work with these of course.
This PR makes an interface out of `EntriesMergeService` and introduces an `EntriesMergeV1Service` that can handle merging V1 definition data.
The changes:
* `EntriesMergeService` is turned into an interface, containing abstract functions for returning the ID, previous/next entry ID, etc.
* `correctESofAtEdge()` is moved to `EntriesMergeV1Service` since it is specific to the V1 definition
* Change to using `Instant` over `ZonedDateTime`, and using skeleton-plugins' `TimeWindow` over VesselVoyage’s `TimeWindow`
Apart from the above, there are no other introduced changes.

Later on an `EntriesMergeV2Service` can be added to support merging V2 definition data.

