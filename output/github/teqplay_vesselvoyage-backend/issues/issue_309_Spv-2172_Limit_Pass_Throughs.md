---
id: github:teqplay/vesselvoyage-backend:issue:309
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 309
title: Spv-2172 Limit Pass Throughs
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/309
labels: []
explicit_links: []
---
# Issue #309: Spv-2172 Limit Pass Throughs

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/309  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d6c0604489d9...419e9f9bd0eb](https://github.com/teqplay/vesselvoyage-backend/compare/d6c0604489d9...419e9f9bd0eb)
**Merge commit:** [419e9f9bd0eb](https://github.com/teqplay/vesselvoyage-backend/commit/419e9f9bd0eb)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2172-limit-pass-throughs](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2172-limit-pass-throughs)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-09T08:26:09.793781+00:00
**Status:** MERGED

Ships such as [https://vesselvoyagedev.teqplay.nl/#/ships/1005693/story/bb2dafad-d1ea-4bcd-bd94-dfdd707c1a44.VISIT](https://vesselvoyagedev.teqplay.nl/#/ships/1005693/story/bb2dafad-d1ea-4bcd-bd94-dfdd707c1a44.VISIT)  could have unlimited pass throughs, this is bound to go wrong with those special vessels, so instead we now limit at 100, like is done for other fields as well \(e.g. stops\)

