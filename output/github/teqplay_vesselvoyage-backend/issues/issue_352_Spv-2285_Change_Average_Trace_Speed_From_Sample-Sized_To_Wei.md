---
id: github:teqplay/vesselvoyage-backend:issue:352
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 352
title: Spv-2285 Change Average Trace Speed From Sample-Sized To Weighted Average Calculation
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/352
labels: []
explicit_links: []
---
# Issue #352: Spv-2285 Change Average Trace Speed From Sample-Sized To Weighted Average Calculation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/352  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [5a89c40e6fe3...5494d21252ce](https://github.com/teqplay/vesselvoyage-backend/compare/5a89c40e6fe3...5494d21252ce)
**Merge commit:** [5494d21252ce](https://github.com/teqplay/vesselvoyage-backend/commit/5494d21252ce)
**Author:** Leon Joosse
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Michel Wilson
**Source Branch:** [SPV-2285-trace-speed-weighted-average](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2285-trace-speed-weighted-average)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-10-23T09:31:50.895730+00:00
**Status:** MERGED

A trace contains an average speed, using a sample-size based calculation. This PR changes it to a weighted average calculation.

