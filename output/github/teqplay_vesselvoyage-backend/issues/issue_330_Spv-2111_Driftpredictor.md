---
id: github:teqplay/vesselvoyage-backend:issue:330
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 330
title: Spv-2111 Driftpredictor
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/330
labels: []
explicit_links:
- jira:SPV-2111
---
# Issue #330: Spv-2111 Driftpredictor

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/330  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [1a90aa97cacf...85c74c61e87f](https://github.com/teqplay/vesselvoyage-backend/compare/1a90aa97cacf...85c74c61e87f)
**Merge commit:** [85c74c61e87f](https://github.com/teqplay/vesselvoyage-backend/commit/85c74c61e87f)
**Author:** Rowdey Goos
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2111-driftpredictor](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2111-driftpredictor)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-09-06T09:53:47.212525+00:00
**Status:** MERGED

* Added drift segment data class \(from drift predictor\)
* Added drift segment prediction item data class \(from drift predictor\)
* Added drift segment response body data class \(from drift predictor\)
* Added rest template configuration for drift predictor api
* Added drift predictor client
* Created post-processing service for determining slow moving segments
* Added Speed calculation for slow moving period
* Added test to validate slow moving period calculated by the PostProcessingService
* Changed expression label
* Added test for no slow moving period case & cleared up timestamps
* Refactored speed functions into separate util functions.
* Refactored service to make use of speed util functions.
* Refactored service to make use of speed util functions.
* Fixed ktlint error

