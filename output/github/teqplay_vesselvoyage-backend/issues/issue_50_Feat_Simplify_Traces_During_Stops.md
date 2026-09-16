---
id: github:teqplay/vesselvoyage-backend:issue:50
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 50
title: Feat/Simplify Traces During Stops
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/50
labels: []
explicit_links: []
---
# Issue #50: Feat/Simplify Traces During Stops

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/50  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [a43c3e42dc84...b62b761d0a94](https://github.com/teqplay/vesselvoyage-backend/compare/a43c3e42dc84...b62b761d0a94)
**Merge commit:** [b62b761d0a94](https://github.com/teqplay/vesselvoyage-backend/commit/b62b761d0a94)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/simplify_traces_during_stops](https://github.com/teqplay/vesselvoyage-backend/tree/feat/simplify_traces_during_stops)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-01T11:15:48.882285+00:00
**Status:** MERGED

Especially anchorages cause a lot of noise, see picture below. During stops, we can simplify the trace and reduce it to a single, averaged point.

* Implement a new function `simplifyTraceAtStops`
* Use this function together with the existing `simplifyTrace` in `TraceService`
* Unit tests

Example: [https://vesselvoyage.teqplay.nl/#/ships/9291602/story](https://vesselvoyage.teqplay.nl/#/ships/9291602/story)



![](https://bitbucket.org/repo/k5G8e7j/images/736932503-image.png)

