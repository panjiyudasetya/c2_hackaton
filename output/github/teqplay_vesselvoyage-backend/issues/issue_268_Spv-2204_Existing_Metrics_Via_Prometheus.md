---
id: github:teqplay/vesselvoyage-backend:issue:268
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 268
title: Spv-2204 Existing Metrics Via Prometheus
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/268
labels: []
explicit_links:
- jira:SPV-2204
---
# Issue #268: Spv-2204 Existing Metrics Via Prometheus

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/268  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [9f98acae72b1...3a0a63f2b238](https://github.com/teqplay/vesselvoyage-backend/compare/9f98acae72b1...3a0a63f2b238)
**Merge commit:** [3a0a63f2b238](https://github.com/teqplay/vesselvoyage-backend/commit/3a0a63f2b238)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2204-existing-metrics-via-prometheus](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2204-existing-metrics-via-prometheus)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-08T09:47:07.021444+00:00
**Status:** MERGED

* Upgraded skeleton plugins version and load in the metrics library
* Replaced the existing metrics to use the metric registry
* adjusted tag key to match prometheus naming conventions
* Made the old insert function testable
* Added tests to ensure the counters are working as expected
* Removed unused imports
* Removed wildcard import
* Adjusted metric type of changes to output as we would expect

