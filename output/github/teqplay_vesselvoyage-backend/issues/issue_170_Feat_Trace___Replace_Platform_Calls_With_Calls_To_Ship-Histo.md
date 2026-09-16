---
id: github:teqplay/vesselvoyage-backend:issue:170
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 170
title: 'Feat(Trace): Replace Platform Calls With Calls To Ship-History'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/170
labels: []
explicit_links:
- jira:SPV-1991
- jira:SPV-1992
---
# Issue #170: Feat(Trace): Replace Platform Calls With Calls To Ship-History

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/170  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3ad0393a31d4...6985dc39aba4](https://github.com/teqplay/vesselvoyage-backend/compare/3ad0393a31d4...6985dc39aba4)
**Merge commit:** [6985dc39aba4](https://github.com/teqplay/vesselvoyage-backend/commit/6985dc39aba4)
**Author:** Former user
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-1991-make-use-of-the-v-1-endpoints-to-get-ship-history](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1991-make-use-of-the-v-1-endpoints-to-get-ship-history)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-04T13:01:03.301704+00:00
**Status:** MERGED

Swapping the use of platform for AIS traces with calls to ship-history.
This doesn’t yet change where the real-time-received AIS traces come from, that will be done in:  
[https://teqplaybv.atlassian.net/browse/SPV-1992](https://teqplaybv.atlassian.net/browse/SPV-1992)

