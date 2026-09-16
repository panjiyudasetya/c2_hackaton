---
id: github:teqplay/vesselvoyage-backend:issue:251
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 251
title: Spv-2046 Fallback Encounters
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/251
labels: []
explicit_links: []
---
# Issue #251: Spv-2046 Fallback Encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/251  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [f217be3b9b9a...45b3a13837a3](https://github.com/teqplay/vesselvoyage-backend/compare/f217be3b9b9a...45b3a13837a3)
**Merge commit:** [45b3a13837a3](https://github.com/teqplay/vesselvoyage-backend/commit/45b3a13837a3)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2046-fallback-encounters](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2046-fallback-encounters)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-06-07T12:16:28.980557+00:00
**Status:** MERGED

* Added logic to end encounters as well when setting a fallback on receiving an EOSP end event
* Adjusted existing test cases to include an ongoing encounter that will be ended with a fallback as well
* Fixed an issue where the updated esof wouldn't be set correctly when providing the result
* Added logic to be able to override the encounter fallback end when we eventually get the encounter event

