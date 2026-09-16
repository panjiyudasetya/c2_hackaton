---
id: github:teqplay/vesselvoyage-backend:issue:262
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 262
title: 'Feat: Remove Stops <5 Minutes & Merge Stops Within <5 Minutes'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/262
labels: []
explicit_links: []
---
# Issue #262: Feat: Remove Stops <5 Minutes & Merge Stops Within <5 Minutes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/262  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [96d294f599c3...e0e5c22d66db](https://github.com/teqplay/vesselvoyage-backend/compare/96d294f599c3...e0e5c22d66db)
**Merge commit:** [e0e5c22d66db](https://github.com/teqplay/vesselvoyage-backend/commit/e0e5c22d66db)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2180-remove-and-merge-stops](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2180-remove-and-merge-stops)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-03T10:11:15.607879+00:00
**Status:** MERGED

Stops are merged if they are within <5 minutes of each other. Ensuring that if the ship is speeding and slowing down often, the stops can get merged.
As well as removing stops if they only took <5 minutes.

