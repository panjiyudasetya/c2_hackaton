---
id: github:teqplay/vesselvoyage-backend:issue:219
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 219
title: Spv-2074 Merge Traces On Visit Cancel
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/219
labels: []
explicit_links:
- jira:SPV-2074
---
# Issue #219: Spv-2074 Merge Traces On Visit Cancel

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/219  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8f3bfe9ccf71...c3cc4c3c7ceb](https://github.com/teqplay/vesselvoyage-backend/compare/8f3bfe9ccf71...c3cc4c3c7ceb)
**Merge commit:** [c3cc4c3c7ceb](https://github.com/teqplay/vesselvoyage-backend/commit/c3cc4c3c7ceb)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2074-merge-traces-on-visit-cancel](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2074-merge-traces-on-visit-cancel)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-24T13:15:15.061741+00:00
**Status:** MERGED

Adjust event processing to merge the traces of a visit and a voyage when the visit is canceled and voyage resumed.
  
NOTE: The merging is done when we get the event processing result to make trace merging not entangled with the processing logic.

