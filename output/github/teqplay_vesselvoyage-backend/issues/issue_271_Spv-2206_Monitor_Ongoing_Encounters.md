---
id: github:teqplay/vesselvoyage-backend:issue:271
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 271
title: Spv-2206 Monitor Ongoing Encounters
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/271
labels: []
explicit_links:
- jira:SPV-2206
---
# Issue #271: Spv-2206 Monitor Ongoing Encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/271  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [44cf36ac30aa...01c5f1dcbf0d](https://github.com/teqplay/vesselvoyage-backend/compare/44cf36ac30aa...01c5f1dcbf0d)
**Merge commit:** [01c5f1dcbf0d](https://github.com/teqplay/vesselvoyage-backend/commit/01c5f1dcbf0d)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [SPV-2206-monitor-ongoing-encounters](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2206-monitor-ongoing-encounters)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-11T14:48:44.030381+00:00
**Status:** MERGED

* Extended the StartEndEventProcessor to count processed start and end events when a metric registry is provided
* Overwritten the default gauges by specific ones for tracking the ongoing encounters
* Adjusted tests to compile with the new MeterRegistry in the EncounterProcessor
* Changed creating of the gauges to actually work for all encounter types
* Adjusted MetricRegistry class to be the EncounterProcessor and not the companion on it
* Changed metrics to instead count processed start and end status of encounters

