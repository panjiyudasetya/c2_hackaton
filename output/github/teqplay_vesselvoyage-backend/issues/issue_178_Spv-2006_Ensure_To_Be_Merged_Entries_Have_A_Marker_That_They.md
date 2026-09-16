---
id: github:teqplay/vesselvoyage-backend:issue:178
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 178
title: Spv-2006 Ensure To Be Merged Entries Have A Marker That They Have Been Recalculated
  Are Coming From R Events
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/178
labels: []
explicit_links:
- jira:SPV-2006
---
# Issue #178: Spv-2006 Ensure To Be Merged Entries Have A Marker That They Have Been Recalculated Are Coming From R Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/178  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [9e974a821171...3f688a7fe00a](https://github.com/teqplay/vesselvoyage-backend/compare/9e974a821171...3f688a7fe00a)
**Merge commit:** [3f688a7fe00a](https://github.com/teqplay/vesselvoyage-backend/commit/3f688a7fe00a)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2006-ensure-to-be-merged-entries-have-a-marker-that-they-have-been-recalculated-are-coming-from-r-events](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2006-ensure-to-be-merged-entries-have-a-marker-that-they-have-been-recalculated-are-coming-from-r-events)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-25T09:12:16.001792+00:00
**Status:** MERGED

* feat: add Entry.regenerated flag
* feat: all regenerated entries should have their regenerated flag set
This PR ensures that all merged entries have a `regenerated=true` flag set, allowing us to identify what was merged from the outside. Could also add a way to identify them in the VesselVoyage frontend.

