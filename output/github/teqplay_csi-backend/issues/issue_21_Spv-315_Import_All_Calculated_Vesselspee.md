---
id: github:teqplay/csi-backend:issue:21
source: github
type: issue
repo: teqplay/csi-backend
number: 21
title: Spv-315 Import All Calculated Vesselspee
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/21
labels: []
explicit_links:
- jira:SPV-315
- jira:SPV-344
---
# Issue #21: Spv-315 Import All Calculated Vesselspee

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/21  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [064f13900239...84a1ed6b802f](https://github.com/teqplay/csi-backend/compare/064f13900239...84a1ed6b802f)
**Merge commit:** [84a1ed6b802f](https://github.com/teqplay/csi-backend/commit/84a1ed6b802f)
**Author:** Former user
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [SPV-315-import-all-calculated-vesselspee](https://github.com/teqplay/csi-backend/tree/SPV-315-import-all-calculated-vesselspee)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2021-11-22T16:43:38.206920+00:00
**Status:** MERGED

Ship characteristics are converted from the `shipModels` collection from Data Science and are stored inside the `shipRegisterCharacteristics` collection. These contain the average speed and loading conditions of a vessel. Some new endpoints have been added to be able to request these through the API.

Outside of the scope of this PR:

* creating/updating \(endpoints\) for the ship characteristics \(will be picked up as part of [SPV-344](https://teqplaybv.atlassian.net/browse/SPV-344)\)
* adding support in the CSI frontend to display \(and edit\) these



[SPV-344]: https://teqplaybv.atlassian.net/browse/SPV-344?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
