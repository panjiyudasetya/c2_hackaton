---
id: github:teqplay/vesselvoyage-backend:issue:115
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 115
title: Spv-1313 Fix Stop Combining
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/115
labels: []
explicit_links: []
---
# Issue #115: Spv-1313 Fix Stop Combining

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/115  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [be883afdb18d...3cc1d9bd5a98](https://github.com/teqplay/vesselvoyage-backend/compare/be883afdb18d...3cc1d9bd5a98)
**Merge commit:** [3cc1d9bd5a98](https://github.com/teqplay/vesselvoyage-backend/commit/3cc1d9bd5a98)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1313_fix_stop_combining](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1313_fix_stop_combining)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-01-26T12:32:02.996737+00:00
**Status:** MERGED

* Fixed an issue where combining of stops would never contain the starting stop except for the first stop it tries to combine
* Added a test case to cover combining of stops is done correctly when having more than 2 stops

