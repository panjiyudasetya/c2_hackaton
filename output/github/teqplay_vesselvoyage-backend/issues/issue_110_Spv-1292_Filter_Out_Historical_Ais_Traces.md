---
id: github:teqplay/vesselvoyage-backend:issue:110
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 110
title: Spv-1292 Filter Out Historical Ais Traces
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/110
labels: []
explicit_links: []
---
# Issue #110: Spv-1292 Filter Out Historical Ais Traces

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/110  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [56a4e373609f...44315301a5d8](https://github.com/teqplay/vesselvoyage-backend/compare/56a4e373609f...44315301a5d8)
**Merge commit:** [44315301a5d8](https://github.com/teqplay/vesselvoyage-backend/commit/44315301a5d8)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1292_filter_out_historical_ais_traces](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1292_filter_out_historical_ais_traces)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-01-09T15:10:00.073323+00:00
**Status:** MERGED

* Filtered out all use of historical ais data when receiving new data point from the queue
* Filtered out historical ais data when retrieving them from the /ship/history/query endpoint
* Changed unit test to reflect ignoring of historic traces

