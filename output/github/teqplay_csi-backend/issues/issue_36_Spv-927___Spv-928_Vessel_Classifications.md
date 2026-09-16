---
id: github:teqplay/csi-backend:issue:36
source: github
type: issue
repo: teqplay/csi-backend
number: 36
title: Spv-927 / Spv-928 Vessel Classifications
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/36
labels: []
explicit_links: []
---
# Issue #36: Spv-927 / Spv-928 Vessel Classifications

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/36  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [f106278489db...7fa7a222fb46](https://github.com/teqplay/csi-backend/compare/f106278489db...7fa7a222fb46)
**Merge commit:** [7fa7a222fb46](https://github.com/teqplay/csi-backend/commit/7fa7a222fb46)
**Author:** Berend
**Reviewers:** Darius Wattimena
**Approvers:** Former user
**Source Branch:** [feat/SPV-927-and-SPV-928-vessel-classification](https://github.com/teqplay/csi-backend/tree/feat/SPV-927-and-SPV-928-vessel-classification)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:38.142900+00:00
**Status:** MERGED

* Added an additional classification field to ShipCalculated which is determined through checking the range which the DWT or TEU is inside of.
* Added enum values for classifications.
* Added an endpoint for searching by classification.

