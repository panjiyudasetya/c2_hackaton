---
id: github:teqplay/vesselvoyage-backend:issue:360
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 360
title: Spv-2284 Trace Draught
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/360
labels: []
explicit_links:
- jira:SPV-2284
---
# Issue #360: Spv-2284 Trace Draught

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/360  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [7be15a65fa74...03eadfd62c74](https://github.com/teqplay/vesselvoyage-backend/compare/7be15a65fa74...03eadfd62c74)
**Merge commit:** [03eadfd62c74](https://github.com/teqplay/vesselvoyage-backend/commit/03eadfd62c74)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena, Joost Dambrink
**Approvers:** Joost Dambrink
**Source Branch:** [SPV-2284-trace-draught](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2284-trace-draught)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-11-11T09:19:42.084652+00:00
**Status:** MERGED

Adds draught stats to the NewTrace class. Draught information is passed on from AIS messages, just as with the speed over ground property.
Added a TraceStatistic class that resembles the draught. Would be nice if we convert average Speed object as well to this, as both properties use the exact same logic for calculating the weighted average.

