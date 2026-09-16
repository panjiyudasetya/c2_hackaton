---
id: github:teqplay/vesselvoyage-backend:issue:31
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 31
title: 'Fix: Return Ongoing Visits/Voyages When They Start Before The Queried Period'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/31
labels: []
explicit_links: []
---
# Issue #31: Fix: Return Ongoing Visits/Voyages When They Start Before The Queried Period

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/31  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [20fdebb3405f...95af082344c1](https://github.com/teqplay/vesselvoyage-backend/compare/20fdebb3405f...95af082344c1)
**Merge commit:** [95af082344c1](https://github.com/teqplay/vesselvoyage-backend/commit/95af082344c1)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/SPV-440_filter_ongoing_visits](https://github.com/teqplay/vesselvoyage-backend/tree/fix/SPV-440_filter_ongoing_visits)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-12-09T07:38:43.864159+00:00
**Status:** MERGED

Small PR @{5c57efac4912b735b9e0646c} , this solves for example the following case:

[https://vesselvoyagedev.teqplay.nl/#/ships/8014409/story](https://vesselvoyagedev.teqplay.nl/#/ships/8014409/story)

of a ship having an ongoing visit of more than three months old. This should be returned when you query the last three months only. 

\(of course, this visit should maybe be marked as finished/invalid or so, it doesn’t make sense, but that is another story\)

