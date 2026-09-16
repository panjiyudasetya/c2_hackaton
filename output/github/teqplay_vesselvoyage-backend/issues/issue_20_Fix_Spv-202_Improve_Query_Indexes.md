---
id: github:teqplay/vesselvoyage-backend:issue:20
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 20
title: Fix/Spv-202 Improve Query Indexes
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/20
labels: []
explicit_links: []
---
# Issue #20: Fix/Spv-202 Improve Query Indexes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/20  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [25a0f71f0b81...670c1da585b4](https://github.com/teqplay/vesselvoyage-backend/compare/25a0f71f0b81...670c1da585b4)
**Merge commit:** [670c1da585b4](https://github.com/teqplay/vesselvoyage-backend/commit/670c1da585b4)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/SPV-202-improve-query-indexes](https://github.com/teqplay/vesselvoyage-backend/tree/fix/SPV-202-improve-query-indexes)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-10-14T12:20:37.413240+00:00
**Status:** MERGED

Currently deployed on VesselVoyage DEV, works nicely, though sometimes requests are just slow and need a warm up, as if Mongo doesn’t have the indexes in it’s cache anymore or so.

* Added some indexes
* Simplify querying on a period with start/end \(not looking at `finished` anymore\)
* Added comments explaining which index serves which method

I didn’t manage to create compound indexes having for example the startTime descending, seems to be a limitation in kmongo. I didn’t look into this indepth. I added some TODO’s to maybe retry some day when we have time or the need to improve this further.


