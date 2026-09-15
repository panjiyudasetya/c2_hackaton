---
id: github:teqplay/vesselvoyage-backend:issue:377
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 377
title: Hotfix Ports Page
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/377
labels: []
explicit_links: []
---
# Issue #377: Hotfix Ports Page

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/377  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [72da02e673cf...63c07d0f37da](https://github.com/teqplay/vesselvoyage-backend/compare/72da02e673cf...63c07d0f37da)
**Merge commit:** [63c07d0f37da](https://github.com/teqplay/vesselvoyage-backend/commit/63c07d0f37da)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [hotfix-ports-page](https://github.com/teqplay/vesselvoyage-backend/tree/hotfix-ports-page)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-12-02T13:24:51.294723+00:00
**Status:** MERGED

* Attempt to fix an issue where the wrong data is returned when loading in the sailing towards and just left data
* Adjusted how we load in ports and ships when starting the backend
* Actually fix sailing towards and just left
* Remove sparse index that doesn't work

