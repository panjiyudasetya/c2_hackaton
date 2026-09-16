---
id: github:teqplay/vesselvoyage-backend:issue:334
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 334
title: Spv-2257 Clean-Up Sof V2
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/334
labels: []
explicit_links:
- jira:SPV-2257
---
# Issue #334: Spv-2257 Clean-Up Sof V2

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/334  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [04b544421187...1a90aa97cacf](https://github.com/teqplay/vesselvoyage-backend/compare/04b544421187...1a90aa97cacf)
**Merge commit:** [1a90aa97cacf](https://github.com/teqplay/vesselvoyage-backend/commit/1a90aa97cacf)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2257-cleanup-generify](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2257-cleanup-generify)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-09-06T09:27:52.765656+00:00
**Status:** MERGED

Removes Port statement of facts view, along with the `Areametadata` annotation in `NewVisit`
For now, there is not much else to optimize or make generic, as there are no other sof generators.

