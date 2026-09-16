---
id: github:teqplay/vesselvoyage-backend:issue:6
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 6
title: Send Latest Ship Status Over The Queue After A Recalculate
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/6
labels: []
explicit_links: []
---
# Issue #6: Send Latest Ship Status Over The Queue After A Recalculate

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/6  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [0aa55e031a6f...72f8e7d4781a](https://github.com/teqplay/vesselvoyage-backend/compare/0aa55e031a6f...72f8e7d4781a)
**Merge commit:** [72f8e7d4781a](https://github.com/teqplay/vesselvoyage-backend/commit/72f8e7d4781a)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/send_latest_update_after_recalculate](https://github.com/teqplay/vesselvoyage-backend/tree/feat/send_latest_update_after_recalculate)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-07-19T14:40:57.458826+00:00
**Status:** MERGED

@{5c57efac4912b735b9e0646c}  can you have a look at this small PR? It addresses a concern of you from some time ago. 

The new `REVISE` action type is breaking for SmartFleet, but I see that right now SmartFleet would simply log an exception and continue when receiving such an event, so it’s robust against it.

