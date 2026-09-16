---
id: github:teqplay/vesselvoyage-backend:issue:213
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 213
title: Spv-2076 Merging V2 Logic Perform Merge
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/213
labels: []
explicit_links: []
---
# Issue #213: Spv-2076 Merging V2 Logic Perform Merge

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/213  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [369785c1b121...13ac5c7b33db](https://github.com/teqplay/vesselvoyage-backend/compare/369785c1b121...13ac5c7b33db)
**Merge commit:** [13ac5c7b33db](https://github.com/teqplay/vesselvoyage-backend/commit/13ac5c7b33db)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2076-merging-v2-logic-perform-merge](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic-perform-merge)
**Destination Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Closed On:** 2024-08-26T07:49:35.798838+00:00
**Status:** MERGED

* feat: use V2 merging upon scenario completion
* feat: allow running V1/V2/V1&V2 when creating a scenario

This PR introduces the ability to regenerate V1 data, V2 data or both. Enabling to send this via the API, but defaulting to only recalculating V2 data.
For persisting the merging the exact same logic is copied from V1 to V2. The only difference being which data sources are used. Also, there is currently no `NewTraceService`, so the deletion of traces after merging is not implemented yet.

