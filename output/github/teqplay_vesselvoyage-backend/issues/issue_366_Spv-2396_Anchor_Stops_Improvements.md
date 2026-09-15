---
id: github:teqplay/vesselvoyage-backend:issue:366
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 366
title: Spv-2396 Anchor Stops Improvements
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/366
labels: []
explicit_links: []
---
# Issue #366: Spv-2396 Anchor Stops Improvements

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/366  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3ea77c10b0bd...e30d8c14fe5b](https://github.com/teqplay/vesselvoyage-backend/compare/3ea77c10b0bd...e30d8c14fe5b)
**Merge commit:** [e30d8c14fe5b](https://github.com/teqplay/vesselvoyage-backend/commit/e30d8c14fe5b)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Joost Dambrink, Leon Joosse
**Source Branch:** [SPV-2396-anchor-stops-improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2396-anchor-stops-improvements)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-11-14T10:13:24.952373+00:00
**Status:** MERGED

* Added a new test case where multiple anchor stops should be merged when having a drifting like pattern in the same anchorage
* Adjusted how the anchor merging tactic works to group together anchor moments when they are close enough and of the same anchorage
* Changed comment why we use a more aggressive max distance
* ktlint

