---
id: github:teqplay/vesselvoyage-backend:issue:224
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 224
title: 'Fix: Ensure Merge Consistency On Missing Start And Beginning With A Visit'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/224
labels: []
explicit_links:
- jira:SPV-2059
- jira:SPV-2076
---
# Issue #224: Fix: Ensure Merge Consistency On Missing Start And Beginning With A Visit

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/224  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [56f0b2cb23fe...9608d538db13](https://github.com/teqplay/vesselvoyage-backend/compare/56f0b2cb23fe...9608d538db13)
**Merge commit:** [9608d538db13](https://github.com/teqplay/vesselvoyage-backend/commit/9608d538db13)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2059-ensure-merge-consistency-on-missing-start-and-begins-with-visit](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2059-ensure-merge-consistency-on-missing-start-and-begins-with-visit)
**Destination Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Closed On:** 2024-05-13T07:51:07.911080+00:00
**Status:** MERGED

Merging was not fully consistent when data was missing at the start, for example when VesselVoyage’s knowledge starts in 2022, but we want to generate and add data prior to 2022.
If the new data would start with a visit, it would somewhat corrupt the old voyage and it would lead into inconsistencies when merging again.
So, this PR fixes that by removing a visit at the start if the data is new, making the result after merge always start and end with a voyage which ensures that merging again will be idempotent. And also ensuring the `previousEntryId` link gets reset in that case, since we don’t have data prior.

