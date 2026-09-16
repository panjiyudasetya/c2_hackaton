---
id: github:teqplay/vesselvoyage-backend:issue:54
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 54
title: Replace Recalculating Ships In Parallel Using `@Async` With Running It In A
  Separate Thread Pool
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/54
labels: []
explicit_links: []
---
# Issue #54: Replace Recalculating Ships In Parallel Using `@Async` With Running It In A Separate Thread Pool

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/54  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d322717b8bd7...67d65d0d13e8](https://github.com/teqplay/vesselvoyage-backend/compare/d322717b8bd7...67d65d0d13e8)
**Merge commit:** [67d65d0d13e8](https://github.com/teqplay/vesselvoyage-backend/commit/67d65d0d13e8)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/recalculation_threading](https://github.com/teqplay/vesselvoyage-backend/tree/fix/recalculation_threading)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-08T09:12:28.259445+00:00
**Status:** MERGED

So, using `@Async` can easily cause thread starvation, blocking the complete application when using the default thread of Spring. \(this happens when calculating too many ships in parallel\).

This PR let the recalculations run in a separate thread so it cannot occupy the threads of the main application, and in the worst case just queue recalculation of the following scheduled ships.

