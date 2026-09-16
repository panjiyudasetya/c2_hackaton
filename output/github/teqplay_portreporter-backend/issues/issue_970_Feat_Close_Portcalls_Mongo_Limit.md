---
id: github:teqplay/portreporter-backend:issue:970
source: github
type: issue
repo: teqplay/portreporter-backend
number: 970
title: Feat/Close Portcalls Mongo Limit
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/970
labels: []
explicit_links: []
---
# Issue #970: Feat/Close Portcalls Mongo Limit

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/970  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b96c5045f171...ab8ff2834e77](https://github.com/teqplay/portreporter-backend/compare/b96c5045f171...ab8ff2834e77)
**Merge commit:** [ab8ff2834e77](https://github.com/teqplay/portreporter-backend/commit/ab8ff2834e77)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/close_portcalls_mongo_limit](https://github.com/teqplay/portreporter-backend/tree/feat/close_portcalls_mongo_limit)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-10-19T14:28:44.184610+00:00
**Status:** MERGED

* use mongo limit and skip to ensure we don't have too much portcalls in memory to cause out of memory exception

* `fix tests`

