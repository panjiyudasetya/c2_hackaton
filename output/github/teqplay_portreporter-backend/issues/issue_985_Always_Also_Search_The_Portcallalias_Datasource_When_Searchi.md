---
id: github:teqplay/portreporter-backend:issue:985
source: github
type: issue
repo: teqplay/portreporter-backend
number: 985
title: Always Also Search The Portcallalias Datasource When Searching For Portcalls,
  Small Refactor To Make Sure We Request Each Portcall From The Database In 1 Calls
  Instead Of Separately
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/985
labels: []
explicit_links:
- jira:CV-5800
---
# Issue #985: Always Also Search The Portcallalias Datasource When Searching For Portcalls, Small Refactor To Make Sure We Request Each Portcall From The Database In 1 Calls Instead Of Separately

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/985  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4c4fc9cb892d...8e512ca38d07](https://github.com/teqplay/portreporter-backend/compare/4c4fc9cb892d...8e512ca38d07)
**Merge commit:** [8e512ca38d07](https://github.com/teqplay/portreporter-backend/commit/8e512ca38d07)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Former user
**Source Branch:** [fix/search_alias](https://github.com/teqplay/portreporter-backend/tree/fix/search_alias)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-11-11T12:33:41.444236+00:00
**Status:** MERGED

It came forward that when searching for CV-5800 it did not show any recent portcalls. I believe it is due to it not trying anymore because it had some results when searching the normal portcall database for it.

