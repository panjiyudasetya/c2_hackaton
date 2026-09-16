---
id: github:teqplay/vesselvoyage-backend:issue:245
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 245
title: Spv-2141 Fix Trace Gap
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/245
labels: []
explicit_links: []
---
# Issue #245: Spv-2141 Fix Trace Gap

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/245  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [237848d0f899...31975af5c4f2](https://github.com/teqplay/vesselvoyage-backend/compare/237848d0f899...31975af5c4f2)
**Merge commit:** [31975af5c4f2](https://github.com/teqplay/vesselvoyage-backend/commit/31975af5c4f2)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-2141-fix-trace-gap](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2141-fix-trace-gap)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-27T09:05:15.033284+00:00
**Status:** MERGED

* Fixed an issue where the ship trace would not be stitched together
* Added a test case to ensure the previous location is always added when creating a new trace
* Code cleanup

