---
id: github:teqplay/vesselvoyage-backend:issue:141
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 141
title: Spv-1738 Fix/Ongoing Ship Trace Imo Referencing A Different Vessel
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/141
labels: []
explicit_links: []
---
# Issue #141: Spv-1738 Fix/Ongoing Ship Trace Imo Referencing A Different Vessel

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/141  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [4b3895e3cac4...e6c960b1e3de](https://github.com/teqplay/vesselvoyage-backend/compare/4b3895e3cac4...e6c960b1e3de)
**Merge commit:** [e6c960b1e3de](https://github.com/teqplay/vesselvoyage-backend/commit/e6c960b1e3de)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Shan Minh Nguyen
**Approvers:** Shan Minh Nguyen
**Source Branch:** [fix/ongoing_ship_trace_imo_mmsi_mapping](https://github.com/teqplay/vesselvoyage-backend/tree/fix/ongoing_ship_trace_imo_mmsi_mapping)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-08-14T15:15:14.754550+00:00
**Status:** MERGED

Currently, this bug is being triggered on [https://vesselvoyage.teqplay.nl/#/ships/9545053/story/c125de36-0cb1-4cec-84e2-29ce1b7d3311.VOYAGE](https://vesselvoyage.teqplay.nl/#/ships/9545053/story/c125de36-0cb1-4cec-84e2-29ce1b7d3311.VOYAGE)
There are 2 vessels using the IMO number of `9545053`:
* The BUTTERFLY with MMSI `538070979` -> [https://onthemap.teqplay.nl/#/ship/538070979](https://onthemap.teqplay.nl/#/ship/538070979)
* The one we are interested in is the HOPE with MMSI `636019333` -> [https://onthemap.teqplay.nl/#/ship/636019333](https://onthemap.teqplay.nl/#/ship/636019333)
This PR makes sure we only insert ongoing ais traces of the vessels where we know the MMSI is the same as the one we know in CSI. When we don’t know the MMSI, we just insert the trace.

