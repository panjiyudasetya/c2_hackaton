---
id: github:teqplay/vesselvoyage-backend:issue:113
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 113
title: Spv-1249 Anchorage Destination Changes
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/113
labels: []
explicit_links: []
---
# Issue #113: Spv-1249 Anchorage Destination Changes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/113  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [8d86a3d81eb8...70d740fb5b78](https://github.com/teqplay/vesselvoyage-backend/compare/8d86a3d81eb8...70d740fb5b78)
**Merge commit:** [70d740fb5b78](https://github.com/teqplay/vesselvoyage-backend/commit/70d740fb5b78)
**Author:** Darius Wattimena
**Reviewers:** Gavin den Hollander
**Approvers:** Gavin den Hollander
**Source Branch:** [SPV-1249_anchorage_destination_changes](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1249_anchorage_destination_changes)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-01-12T10:20:25.009356+00:00
**Status:** MERGED

* Fixed an issue where the destination would be cleared when the provided set of destinations is empty
* Moved clearing of the destination to be done when exiting of the anchorage of the port instead on first entering
* Updated test cases to reflect the new way of handling the destination when entering or exiting the anchor area

