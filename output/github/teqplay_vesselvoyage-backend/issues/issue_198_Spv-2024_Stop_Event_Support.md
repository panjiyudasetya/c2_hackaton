---
id: github:teqplay/vesselvoyage-backend:issue:198
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 198
title: Spv-2024 Stop Event Support
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/198
labels: []
explicit_links:
- jira:SPV-2024
---
# Issue #198: Spv-2024 Stop Event Support

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/198  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [33867cc5bef2...5be65e2a8cf6](https://github.com/teqplay/vesselvoyage-backend/compare/33867cc5bef2...5be65e2a8cf6)
**Merge commit:** [5be65e2a8cf6](https://github.com/teqplay/vesselvoyage-backend/commit/5be65e2a8cf6)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2024-stop-event-support](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2024-stop-event-support)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:35.843422+00:00
**Status:** MERGED

* Added internal event model
* Added basic stop event processing classes
* Added logic how stop events should be handled
* Added tests to ensure stop start events are handled correctly for all expected cases
* Added tests to ensure stop end events are processed as expected
* Fix an issue where it would always find finished stops instead of ongoing ones to match on
* Code cleanup

