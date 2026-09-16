---
id: github:teqplay/vesselvoyage-backend:issue:255
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 255
title: Spv-2124 Add Port Pass Through Support
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/255
labels: []
explicit_links: []
---
# Issue #255: Spv-2124 Add Port Pass Through Support

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/255  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [2faa7cf085b9...79e348bd0cf0](https://github.com/teqplay/vesselvoyage-backend/compare/2faa7cf085b9...79e348bd0cf0)
**Merge commit:** [79e348bd0cf0](https://github.com/teqplay/vesselvoyage-backend/commit/79e348bd0cf0)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2124-add-port-pass-through-support](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2124-add-port-pass-through-support)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-24T08:14:03.350435+00:00
**Status:** MERGED

* Adjusted port processing to support pass-through ports when not stopping inside the port
* Aligned existing port event test cases to contain stops so they don't get marked as pass-through ports
* Adjusted scenario testing to have stops as well
* Adjust marking of overlapping port times to actually work
* Adjusted story dry run so it also load in all pass through ports
* code cleanup
* Adjusted scenario tests to again test on every permutation possible
* Adjusted logic to actually be testing correctly for ongoing stops
* Added more test cases to ensure stops are correctly covered
* Code cleanup

