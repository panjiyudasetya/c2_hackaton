---
id: github:teqplay/vesselvoyage-backend:issue:314
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 314
title: Spv-2275 Lock Stops
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/314
labels: []
explicit_links:
- jira:SPV-2275
---
# Issue #314: Spv-2275 Lock Stops

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/314  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [f87673e43134...e818037b510e](https://github.com/teqplay/vesselvoyage-backend/compare/f87673e43134...e818037b510e)
**Merge commit:** [e818037b510e](https://github.com/teqplay/vesselvoyage-backend/commit/e818037b510e)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse
**Approvers:** Michel Wilson
**Source Branch:** [SPV-2275-lock-stops](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2275-lock-stops)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-09T08:26:07.071985+00:00
**Status:** MERGED

* Created `NewStopType` enum to avoid issues with V1.
* Reworked stop classification logic used by V2.
* Added locks to the classification logic.
* Adjust confirming of Visits to ignore lock stops.

