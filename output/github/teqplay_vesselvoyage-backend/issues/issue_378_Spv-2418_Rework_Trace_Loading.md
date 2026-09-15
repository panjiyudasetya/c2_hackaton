---
id: github:teqplay/vesselvoyage-backend:issue:378
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 378
title: Spv-2418 Rework Trace Loading
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/378
labels: []
explicit_links: []
---
# Issue #378: Spv-2418 Rework Trace Loading

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/378  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [0cf9b33a772c...c161a02ed21f](https://github.com/teqplay/vesselvoyage-backend/compare/0cf9b33a772c...c161a02ed21f)
**Merge commit:** [c161a02ed21f](https://github.com/teqplay/vesselvoyage-backend/commit/c161a02ed21f)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2418-rework-trace-loading](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2418-rework-trace-loading)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-12-04T16:07:03.272412+00:00
**Status:** MERGED

* Moved existing trace services to their corresponding package
* Made trace generation schedulable when missing
* Added a test to ensure traces are correctly generated when scheduling a finished visit
* Added a test case where we also include the last info of a previous entry to create the new trace
* Fixed an issue where the draught isn't correctly processed when providing multiple trace items

