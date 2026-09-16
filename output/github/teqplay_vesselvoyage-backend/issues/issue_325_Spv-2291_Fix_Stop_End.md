---
id: github:teqplay/vesselvoyage-backend:issue:325
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 325
title: Spv-2291 Fix Stop End
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/325
labels: []
explicit_links: []
---
# Issue #325: Spv-2291 Fix Stop End

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/325  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [257fb669213e...7f9e1dcba12c](https://github.com/teqplay/vesselvoyage-backend/compare/257fb669213e...7f9e1dcba12c)
**Merge commit:** [7f9e1dcba12c](https://github.com/teqplay/vesselvoyage-backend/commit/7f9e1dcba12c)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-2291-fix-stop-end](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2291-fix-stop-end)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-15T13:38:56.440707+00:00
**Status:** MERGED

* Temporary fix an issue where the stops of a visit could potentially not have an end time and location
* Changed settings of the fallback location to use the berth location of the closest one if available and our ship fits inside the berth

