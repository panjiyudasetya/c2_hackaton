---
id: github:teqplay/vesselvoyage-backend:issue:294
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 294
title: Fix Event Consuming Threads
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/294
labels: []
explicit_links: []
---
# Issue #294: Fix Event Consuming Threads

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/294  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [391bd3411a49...aa7050424955](https://github.com/teqplay/vesselvoyage-backend/compare/391bd3411a49...aa7050424955)
**Merge commit:** [aa7050424955](https://github.com/teqplay/vesselvoyage-backend/commit/aa7050424955)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix-event-consuming-threads](https://github.com/teqplay/vesselvoyage-backend/tree/fix-event-consuming-threads)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-24T13:16:34.379699+00:00
**Status:** MERGED

* Adjusted event processing so it is done in parallel
* Added some more comments
* Acknowledge messages after instead

