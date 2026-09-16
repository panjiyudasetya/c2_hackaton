---
id: github:teqplay/vesselvoyage-backend:issue:229
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 229
title: Spv-1983 Api V2 Voyages By Port Fix Merge Conflicts
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/229
labels: []
explicit_links: []
---
# Issue #229: Spv-1983 Api V2 Voyages By Port Fix Merge Conflicts

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/229  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [05d160a8e7f1...55c33418f97a](https://github.com/teqplay/vesselvoyage-backend/compare/05d160a8e7f1...55c33418f97a)
**Merge commit:** [55c33418f97a](https://github.com/teqplay/vesselvoyage-backend/commit/55c33418f97a)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [SPV-1983-api-v2-voyages-by-port-fix-merge-conflicts](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1983-api-v2-voyages-by-port-fix-merge-conflicts)
**Destination Branch:** [SPV-1983-api-v2-voyages-by-port](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1983-api-v2-voyages-by-port)
**Closed On:** 2024-05-07T08:44:38.536745+00:00
**Status:** MERGED

Fixes for PR #232
* Rename `NewVoyage.origin` to `originPort` and `NewVoyage.destination` to `destinationPort`. to not conflict with `destination` added by Maurice
* Add v2 voyage by ais destination endpoint

