---
id: github:teqplay/vesselvoyage-backend:issue:78
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 78
title: Pra-37 Eks Improve Cache
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/78
labels: []
explicit_links: []
---
# Issue #78: Pra-37 Eks Improve Cache

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/78  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [cac65d61d92a...a08392e2078f](https://github.com/teqplay/vesselvoyage-backend/compare/cac65d61d92a...a08392e2078f)
**Merge commit:** [a08392e2078f](https://github.com/teqplay/vesselvoyage-backend/commit/a08392e2078f)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [PRA-37_eks_improve_cache](https://github.com/teqplay/vesselvoyage-backend/tree/PRA-37_eks_improve_cache)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-07-01T15:32:30.460134+00:00
**Status:** MERGED

* Added an enabled boolean for diskcache, so you can keep the old behaviour of always loading in fresh data
* Added missing value for testing the diskcache
* Changed loading in platform and csi data to be done in parallel
* Changed the flow a bit so it blocks the main thread so we can ensure everything is loaded in before the application starts processing events
* ktlint
* Fixed unittest not properly working when using coroutines


