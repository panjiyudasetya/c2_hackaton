---
id: github:teqplay/vesselvoyage-backend:issue:288
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 288
title: 'Fix: Non-Confirmed To Confirmed Visit Moves Backward In Time'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/288
labels: []
explicit_links: []
---
# Issue #288: Fix: Non-Confirmed To Confirmed Visit Moves Backward In Time

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/288  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [a97fd5d223d4...b7cdead8ab95](https://github.com/teqplay/vesselvoyage-backend/compare/a97fd5d223d4...b7cdead8ab95)
**Merge commit:** [b7cdead8ab95](https://github.com/teqplay/vesselvoyage-backend/commit/b7cdead8ab95)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/non-confirmed-to-confirmed-visit-moves-backward-in-time](https://github.com/teqplay/vesselvoyage-backend/tree/fix/non-confirmed-to-confirmed-visit-moves-backward-in-time)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-23T11:53:25.203577+00:00
**Status:** MERGED

Once a non-confirmed visit became confirmed due to a stop classified as berth. It could move visits/voyages backward in time.
![](https://bitbucket.org/repo/k5G8e7j/images/97087738-image.png)

