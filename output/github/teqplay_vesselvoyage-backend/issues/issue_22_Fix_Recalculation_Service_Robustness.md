---
id: github:teqplay/vesselvoyage-backend:issue:22
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 22
title: Fix/Recalculation Service Robustness
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/22
labels: []
explicit_links: []
---
# Issue #22: Fix/Recalculation Service Robustness

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/22  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [7c94013a80eb...2d201152419c](https://github.com/teqplay/vesselvoyage-backend/compare/7c94013a80eb...2d201152419c)
**Merge commit:** [2d201152419c](https://github.com/teqplay/vesselvoyage-backend/commit/2d201152419c)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [fix/recalculation_service_robustness](https://github.com/teqplay/vesselvoyage-backend/tree/fix/recalculation_service_robustness)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-10-21T15:35:19.002851+00:00
**Status:** MERGED

* Fix the RecalculationService retrying the same ship every 60 seconds: remove ship from the list when starting to recalculate, put it back at the end in case of failure
* Configure larger read and connection timeouts for BACKENDGLOBAL and BACKENDPRONTO


