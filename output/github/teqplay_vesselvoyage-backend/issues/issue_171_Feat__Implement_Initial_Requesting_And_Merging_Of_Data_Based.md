---
id: github:teqplay/vesselvoyage-backend:issue:171
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 171
title: 'Feat: Implement Initial Requesting And Merging Of Data Based On (R)Events'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/171
labels: []
explicit_links: []
---
# Issue #171: Feat: Implement Initial Requesting And Merging Of Data Based On (R)Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/171  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [0ea49faa85ee...4514dace343f](https://github.com/teqplay/vesselvoyage-backend/compare/0ea49faa85ee...4514dace343f)
**Merge commit:** [4514dace343f](https://github.com/teqplay/vesselvoyage-backend/commit/4514dace343f)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-1986-replace-vessel-voyage-recalculation-mechanism-using-revents](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1986-replace-vessel-voyage-recalculation-mechanism-using-revents)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-13T08:53:18.732929+00:00
**Status:** MERGED

This is an initial implementation for recalculating VesselVoyage.
Currently only supporting recalculating a ship within a time frame, creating a \(r\)events scenario for that, tracking its progress, as well as merging that back into VesselVoyage itself.
The full “VesselVoyage recalculation based on \(r\)events” feature will not be finished within just this PR, there is more work to be done. To spend sufficient time on those tasks, would like to have this initial PR reviewed and merged beforehand. Continuing those tasks in separate and subsequent PRs, to ensure this one doesn’t grow too large, as well as maintaining proper focus.
The TODOs within this PR \(and some that don’t have an explicit TODO\) have tasks associated with them on the sprint backlog:
* [https://teqplaybv.atlassian.net/browse/SPV-2002](https://teqplaybv.atlassian.net/browse/SPV-2002) 
* [https://teqplaybv.atlassian.net/browse/SPV-2003](https://teqplaybv.atlassian.net/browse/SPV-2003) 
* [https://teqplaybv.atlassian.net/browse/SPV-2004](https://teqplaybv.atlassian.net/browse/SPV-2004) 
* [https://teqplaybv.atlassian.net/browse/SPV-2005](https://teqplaybv.atlassian.net/browse/SPV-2005) 
* [https://teqplaybv.atlassian.net/browse/SPV-2006](https://teqplaybv.atlassian.net/browse/SPV-2006) 
* [https://teqplaybv.atlassian.net/browse/SPV-2007](https://teqplaybv.atlassian.net/browse/SPV-2007) 

Would like to know what you think about this initial setup, and about next steps to get this merged and afterward continue working on the above-mentioned tasks.

