---
id: github:teqplay/vesselvoyage-backend:issue:206
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 206
title: Spv-2069 Support New Stop Events
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/206
labels: []
explicit_links: []
---
# Issue #206: Spv-2069 Support New Stop Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/206  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e5f278e463d3...8334d0ee31b1](https://github.com/teqplay/vesselvoyage-backend/compare/e5f278e463d3...8334d0ee31b1)
**Merge commit:** [8334d0ee31b1](https://github.com/teqplay/vesselvoyage-backend/commit/8334d0ee31b1)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2069-support-new-stop-events](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2069-support-new-stop-events)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-15T13:50:09.486288+00:00
**Status:** MERGED

Adding support for:
* converting ais-engine’s `StopStartEvent` and `StopEndEvent` to VesselVoyage’s `StopEvent`
* storing the `StopEndEvent.actualLocation` in the `NewStop` \(was not done before\)

