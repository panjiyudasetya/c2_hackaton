---
id: github:teqplay/vesselvoyage-backend:issue:189
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 189
title: 'Fix: When Splitting And Creating A New Voyage, Ensure The Next Entry Properly
  Links To The New Identifier'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/189
labels: []
explicit_links:
- jira:SPV-2015
---
# Issue #189: Fix: When Splitting And Creating A New Voyage, Ensure The Next Entry Properly Links To The New Identifier

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/189  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ebe0757cc1a7...116d1a763a9c](https://github.com/teqplay/vesselvoyage-backend/compare/ebe0757cc1a7...116d1a763a9c)
**Merge commit:** [116d1a763a9c](https://github.com/teqplay/vesselvoyage-backend/commit/116d1a763a9c)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-2015-bug-splitting-voyage-in-two-should-link-correctly](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2015-bug-splitting-voyage-in-two-should-link-correctly)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-29T11:15:58.961756+00:00
**Status:** MERGED

When merging and a voyage gets split into two, we need to get the next entry to fix the `previousEntryId` of the next entry.
This ensures the entry previous<>next ID links stay correct even if a new voyage identifier gets introduced in-between.
Otherwise you could have the issue of:
* old situation only has a voyage
* new situation introduces a visit
* to the left of the visit will be the original voyage, shortened, and with its identifier staying the same
* to the right of the visit we’ll need to create a new voyage based on the original one, but adding a new identifier
* if we don’t link the `previousEntryId` of that \(presumably\) visit to the new voyage we’ve created, it would still link to the voyage before the new visit..

