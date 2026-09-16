---
id: github:teqplay/vesselvoyage-backend:issue:215
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 215
title: Spv-2080 Fix Overlapping Eosp
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/215
labels: []
explicit_links:
- jira:SPV-2080
---
# Issue #215: Spv-2080 Fix Overlapping Eosp

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/215  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [650231041d47...4b857f887603](https://github.com/teqplay/vesselvoyage-backend/compare/650231041d47...4b857f887603)
**Merge commit:** [4b857f887603](https://github.com/teqplay/vesselvoyage-backend/commit/4b857f887603)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2080-fix-overlapping-eosp](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2080-fix-overlapping-eosp)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:35.812759+00:00
**Status:** MERGED

* Added new test cases to cover the special scenarios where we are in multiple main port EOSP at the same time
* Adjusted logic so only main ports are supported when entering a EOSP and that you can be in multiple EOSP at the same time
* Changed logic to create 0-second voyages when still having an ongoing eosp when we finish the visit
* Adjusted EOSP end event processing when having a pass-through but having other ongoing EOSP activities

