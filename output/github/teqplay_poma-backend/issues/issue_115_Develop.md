---
id: github:teqplay/poma-backend:issue:115
source: github
type: issue
repo: teqplay/poma-backend
number: 115
title: Develop
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/115
labels: []
explicit_links: []
---
# Issue #115: Develop

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/115  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [6380e82449e9...389c49b6a7fc](https://github.com/teqplay/poma-backend/compare/6380e82449e9...389c49b6a7fc)
**Merge commit:** [389c49b6a7fc](https://github.com/teqplay/poma-backend/commit/389c49b6a7fc)
**Author:** Wouter Naloop
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2023-11-06T16:13:55.576165+00:00
**Status:** MERGED

* make ports a list instead of a set so that order is preserved, add a sort function for all items that can be in a port based on the area size, introduce an interface which covers all models which is linked to a port
* fix tests after ports set to list
* add a list of unlocodes instead of ports

