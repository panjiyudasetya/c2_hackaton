---
id: github:teqplay/vesselvoyage-backend:issue:243
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 243
title: Spv-2118 Event Converting
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/243
labels: []
explicit_links:
- jira:SPV-2118
---
# Issue #243: Spv-2118 Event Converting

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/243  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [a18329ad3a23...41696e25bec8](https://github.com/teqplay/vesselvoyage-backend/compare/a18329ad3a23...41696e25bec8)
**Merge commit:** [41696e25bec8](https://github.com/teqplay/vesselvoyage-backend/commit/41696e25bec8)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [SPV-2118-event-converting](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2118-event-converting)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-23T09:27:33.945841+00:00
**Status:** MERGED

Added logic to convert AisEngine area events into the VesselVoyage equivalent.
NOTE: This does not include Breakwater, as when checking with Richard it makes more sense to have them all under the “approach area” times \(like we have in the AreaMonitor\).  
So soon a PR will follow that renames breakwater → approach in the models, converters, etc.

