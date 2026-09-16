---
id: github:teqplay/vesselvoyage-backend:issue:160
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 160
title: Fix Movement Stop Processing
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/160
labels: []
explicit_links: []
---
# Issue #160: Fix Movement Stop Processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/160  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [1fd87959424b...958d934b39df](https://github.com/teqplay/vesselvoyage-backend/compare/1fd87959424b...958d934b39df)
**Merge commit:** [958d934b39df](https://github.com/teqplay/vesselvoyage-backend/commit/958d934b39df)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [fix-movement-stop-processing](https://github.com/teqplay/vesselvoyage-backend/tree/fix-movement-stop-processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-01-30T12:26:17.936017+00:00
**Status:** MERGED

* Clarified the check being done when we have a movement stop
* Removed the unneeded code that never triggered as it would already been covered with the check above

Noticed the code didn’t make much sense when I was writing down the definitions about the movement stop

