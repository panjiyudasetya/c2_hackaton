---
id: github:teqplay/vesselvoyage-backend:issue:59
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 59
title: Fix/Improve Locking And Memory Of Recalculation
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/59
labels: []
explicit_links: []
---
# Issue #59: Fix/Improve Locking And Memory Of Recalculation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/59  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b2adffd3fb10...49d6f42c668f](https://github.com/teqplay/vesselvoyage-backend/compare/b2adffd3fb10...49d6f42c668f)
**Merge commit:** [49d6f42c668f](https://github.com/teqplay/vesselvoyage-backend/commit/49d6f42c668f)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/improve_locking_and_memory_of_recalculation](https://github.com/teqplay/vesselvoyage-backend/tree/fix/improve_locking_and_memory_of_recalculation)
**Destination Branch:** [fix/fetch_events_in_chunks](https://github.com/teqplay/vesselvoyage-backend/tree/fix/fetch_events_in_chunks)
**Closed On:** 2022-02-14T12:57:00.046945+00:00
**Status:** MERGED

During recalculation of a ship:
* Do not keep all entries \(visits/voyages\) of a single ship in memory but only a tiny summary \(an entry can grow large when having many encounters, stops, etc\)
* Do not lock a ship whilst recalculating its traces \(that can take a long time\)

