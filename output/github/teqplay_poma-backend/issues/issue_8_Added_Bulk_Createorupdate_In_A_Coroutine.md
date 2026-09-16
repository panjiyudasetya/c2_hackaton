---
id: github:teqplay/poma-backend:issue:8
source: github
type: issue
repo: teqplay/poma-backend
number: 8
title: Added Bulk Createorupdate In A Coroutine
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/8
labels: []
explicit_links: []
---
# Issue #8: Added Bulk Createorupdate In A Coroutine

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/8  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [f8dc1ed35752...d9aab50a66c5](https://github.com/teqplay/poma-backend/compare/f8dc1ed35752...d9aab50a66c5)
**Merge commit:** [d9aab50a66c5](https://github.com/teqplay/poma-backend/commit/d9aab50a66c5)
**Author:** Wouter Naloop
**Reviewers:** Leon Joosse, Vasyl Pidlisniak
**Approvers:** 
**Source Branch:** [feat/bulk_update](https://github.com/teqplay/poma-backend/tree/feat/bulk_update)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2020-10-01T06:55:20.994715+00:00
**Status:** MERGED

Hi,   
The bulkwrite is a bit stupid because i still need to fetch the items individually to do the merge step.   
If someone knows a solution to this problem it is very welcome.   
I have seen that in the aggregation stuff of mongo there is a merge possibility which might be useful here to lift that logic up into the db level.   
  
For now this seems to work good enough except for that i need to do the update in a coroutine so the resource can already return a result. If i don’t do that the request will timeout because it takes too long

