---
id: github:teqplay/vesselvoyage-backend:issue:11
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 11
title: Fix/Recalculate History Using All Ship'S Mmsis Instead Of The Imo
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/11
labels: []
explicit_links: []
---
# Issue #11: Fix/Recalculate History Using All Ship'S Mmsis Instead Of The Imo

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/11  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [9cfba26ad4b6...02a8ab347a05](https://github.com/teqplay/vesselvoyage-backend/compare/9cfba26ad4b6...02a8ab347a05)
**Merge commit:** [02a8ab347a05](https://github.com/teqplay/vesselvoyage-backend/commit/02a8ab347a05)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/recalculate_history_using_historic_mmsis](https://github.com/teqplay/vesselvoyage-backend/tree/fix/recalculate_history_using_historic_mmsis)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-09-03T14:58:37.692485+00:00
**Status:** MERGED

For recalculation, fetch the events and AIS based on all MMSI's that a ship has had instead of IMO, else you will only fetch the data corresponding to the latest MMSI normally

In a future step, I hope we can get this mapping \(IMO and all MMSI’s that a ship has had in the past\) from CSI instead.  
  
Thinking aloud: maybe we should solve this in the platform instead, the current queries are misleading when you use IMO.

