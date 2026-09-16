---
id: github:teqplay/vesselvoyage-backend:issue:274
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 274
title: Spv-2247 Non Blocking Event Consuming When On Limit
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/274
labels: []
explicit_links:
- jira:SPV-2247
---
# Issue #274: Spv-2247 Non Blocking Event Consuming When On Limit

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/274  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [0347dcee5dfe...9c82c9dc24b7](https://github.com/teqplay/vesselvoyage-backend/compare/0347dcee5dfe...9c82c9dc24b7)
**Merge commit:** [9c82c9dc24b7](https://github.com/teqplay/vesselvoyage-backend/commit/9c82c9dc24b7)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2247-non-blocking-event-consuming-when-on-limit](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2247-non-blocking-event-consuming-when-on-limit)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-10T13:03:34.431776+00:00
**Status:** MERGED

Adjusts the visit and voyage persisting to not crash when a the mongo exception is thrown for having items bigger than the 16 MB max of mongo

