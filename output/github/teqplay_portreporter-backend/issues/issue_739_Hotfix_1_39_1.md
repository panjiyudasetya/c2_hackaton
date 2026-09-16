---
id: github:teqplay/portreporter-backend:issue:739
source: github
type: issue
repo: teqplay/portreporter-backend
number: 739
title: Hotfix 1.39.1
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/739
labels: []
explicit_links: []
---
# Issue #739: Hotfix 1.39.1

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/739  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [c0404f4b1a36...88a4e4617731](https://github.com/teqplay/portreporter-backend/compare/c0404f4b1a36...88a4e4617731)
**Merge commit:** [88a4e4617731](https://github.com/teqplay/portreporter-backend/commit/88a4e4617731)
**Author:** Shravan Shetty
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [hotfix_1.39.1](https://github.com/teqplay/portreporter-backend/tree/hotfix_1.39.1)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2020-02-25T14:53:15.616090+00:00
**Status:** MERGED

There are two issues seen: 

* Enddate was not used in the query
* `limit` of 1000 was added to fetching the portcalls. 

This made sure only the most recent 1000 portcalls was fetched. So the filtering in the frontend was not good enough

