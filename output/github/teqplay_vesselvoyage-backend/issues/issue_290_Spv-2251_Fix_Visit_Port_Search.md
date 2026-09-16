---
id: github:teqplay/vesselvoyage-backend:issue:290
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 290
title: Spv-2251 Fix Visit Port Search
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/290
labels: []
explicit_links: []
---
# Issue #290: Spv-2251 Fix Visit Port Search

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/290  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3e52af3c3950...360d5caba8be](https://github.com/teqplay/vesselvoyage-backend/compare/3e52af3c3950...360d5caba8be)
**Merge commit:** [360d5caba8be](https://github.com/teqplay/vesselvoyage-backend/commit/360d5caba8be)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [SPV-2251-make-visit-search-more-flexable](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2251-make-visit-search-more-flexable)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-24T08:03:15.947198+00:00
**Status:** MERGED

Turned out searching by unlocode or portid search the following:
```
NewVisit::eospAreaActivity / AreaActivity::areaId eq areaId
```
This however does only work when you add `.eosp` to the `areaId` as you will otherwise never match on a port.

