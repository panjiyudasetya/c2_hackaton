---
id: github:teqplay/vesselvoyage-backend:issue:186
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 186
title: Spv-2020 New Definitions Berth Event Processing Impl
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/186
labels: []
explicit_links:
- jira:SPV-2019
- jira:SPV-1985
---
# Issue #186: Spv-2020 New Definitions Berth Event Processing Impl

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/186  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [23a672ff4905...41b6aba485ad](https://github.com/teqplay/vesselvoyage-backend/compare/23a672ff4905...41b6aba485ad)
**Merge commit:** [41b6aba485ad](https://github.com/teqplay/vesselvoyage-backend/commit/41b6aba485ad)
**Author:** Darius Wattimena
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-2019-new-definitions-berth-event-processing-impl](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2019-new-definitions-berth-event-processing-impl)
**Destination Branch:** [SPV-1985-new-definitions](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1985-new-definitions)
**Closed On:** 2024-03-25T08:50:54.067742+00:00
**Status:** MERGED

* Added support for unique berth event processing
* Changed the anchor event processor to also use the ActivityEventProcessor
* Added test cases to ensure we don't do anything with the berth start and end event when in voyage or initial status
* Added unique berth event tests to ensure they work as expected
* ktlint

