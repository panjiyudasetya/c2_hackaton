---
id: github:teqplay/vesselvoyage-backend:issue:356
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 356
title: Spv-2357 Fix Out Of Order State
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/356
labels: []
explicit_links: []
---
# Issue #356: Spv-2357 Fix Out Of Order State

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/356  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [eca03de21a06...72c1b5f0b73e](https://github.com/teqplay/vesselvoyage-backend/compare/eca03de21a06...72c1b5f0b73e)
**Merge commit:** [72c1b5f0b73e](https://github.com/teqplay/vesselvoyage-backend/commit/72c1b5f0b73e)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Joost Dambrink
**Source Branch:** [fix-out-of-order-state](https://github.com/teqplay/vesselvoyage-backend/tree/fix-out-of-order-state)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-10-23T09:30:27.182627+00:00
**Status:** MERGED

* Added a test case of a ship state where the vessel would go out of order when having a zero-second voyage
* Fixed an issue where with a zero-second voyage you would always load in the ship state incorrectly resulting in creating of multiple visit

