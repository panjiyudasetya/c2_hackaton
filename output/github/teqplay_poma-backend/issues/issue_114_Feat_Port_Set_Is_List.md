---
id: github:teqplay/poma-backend:issue:114
source: github
type: issue
repo: teqplay/poma-backend
number: 114
title: Feat/Port Set Is List
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/114
labels: []
explicit_links: []
---
# Issue #114: Feat/Port Set Is List

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/114  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [5193bd422fe6...c83e7ce2f01e](https://github.com/teqplay/poma-backend/compare/5193bd422fe6...c83e7ce2f01e)
**Merge commit:** [c83e7ce2f01e](https://github.com/teqplay/poma-backend/commit/c83e7ce2f01e)
**Author:** Wouter Naloop
**Reviewers:** Darius Wattimena, Shan Minh Nguyen
**Approvers:** Shan Minh Nguyen
**Source Branch:** [feat/port_set_is_list](https://github.com/teqplay/poma-backend/tree/feat/port_set_is_list)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2023-11-06T15:03:34.292432+00:00
**Status:** MERGED

* make ports a list instead of a set so that order is preserved, add a sort function for all items that can be in a port based on the area size, introduce an interface which covers all models which is linked to a port
* fix tests after ports set to list

