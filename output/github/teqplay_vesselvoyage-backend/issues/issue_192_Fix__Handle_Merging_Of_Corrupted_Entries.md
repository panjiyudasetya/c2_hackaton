---
id: github:teqplay/vesselvoyage-backend:issue:192
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 192
title: 'Fix: Handle Merging Of Corrupted Entries'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/192
labels: []
explicit_links:
- jira:SPV-1994
---
# Issue #192: Fix: Handle Merging Of Corrupted Entries

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/192  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d85403cf7767...8110fb54fafb](https://github.com/teqplay/vesselvoyage-backend/compare/d85403cf7767...8110fb54fafb)
**Merge commit:** [8110fb54fafb](https://github.com/teqplay/vesselvoyage-backend/commit/8110fb54fafb)
**Author:** Former user
**Reviewers:** Wouter Naloop, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-1994-support-merging-with-corrupted-data](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1994-support-merging-with-corrupted-data)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-15T08:17:03.246267+00:00
**Status:** MERGED

VesselVoyage might get a corrupted view of the world, having visits or voyages that don’t end / are not finished, or other issues.
For example a visit that doesn’t have an `endTime`, missing voyages, things being misaligned:
![](https://bitbucket.org/repo/k5G8e7j/images/4153861782-image.png)
Or an extension to this, with multiple visits being incorrect, one with an `endTime` that’s equal to the `startTime`, one with no `endTime` at all. A missing voyage and a voyage that doesn’t have an `endTime`.
![](https://bitbucket.org/repo/k5G8e7j/images/870778033-image.png)

This PR adds support for merging back cleanly in these cases, by:
* identifying corrupted visits/voyages and removing them pre-emptively
* enlarging the time window when regenerating by ship to ensure these issues are captured and eliminated

