---
id: github:teqplay/vesselvoyage-backend:issue:16
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 16
title: Feat/Query By Ship Type
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/16
labels: []
explicit_links: []
---
# Issue #16: Feat/Query By Ship Type

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/16  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [09142b597253...1c0adee93622](https://github.com/teqplay/vesselvoyage-backend/compare/09142b597253...1c0adee93622)
**Merge commit:** [1c0adee93622](https://github.com/teqplay/vesselvoyage-backend/commit/1c0adee93622)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/query_by_ship_type](https://github.com/teqplay/vesselvoyage-backend/tree/feat/query_by_ship_type)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-23T12:30:16.340231+00:00
**Status:** MERGED

The two commits in this PR are not really related, maybe it helps to look at them separate from each other.  
  
Changes:

* Small refactor: move the logic related to keeping/loading a map with current ship statuses into ShipStatusCache to keep EntryService focused
* New feature: Extend the VisitQuery and VoyageQuery with an optional set with ship types. 

Querying now goes in two steps:

* first determine the list with matching ships. Currently only filtered on shipType or explicitly entered imo, later we can extend with other ship properties like size
* second: execute the query to find matching visits/voyages


