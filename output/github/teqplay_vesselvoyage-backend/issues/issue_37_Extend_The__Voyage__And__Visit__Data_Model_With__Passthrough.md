---
id: github:teqplay/vesselvoyage-backend:issue:37
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 37
title: Extend The `Voyage` And `Visit` Data Model With `Passthroughareas`, And Move
  Pass-Through Visits There Instead Of Losing Them
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/37
labels: []
explicit_links: []
---
# Issue #37: Extend The `Voyage` And `Visit` Data Model With `Passthroughareas`, And Move Pass-Through Visits There Instead Of Losing Them

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/37  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d6cd06c550e0...97db8e257ce6](https://github.com/teqplay/vesselvoyage-backend/compare/d6cd06c550e0...97db8e257ce6)
**Merge commit:** [97db8e257ce6](https://github.com/teqplay/vesselvoyage-backend/commit/97db8e257ce6)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/SPV-479_store_pass-through_visits_in_previous_voyage](https://github.com/teqplay/vesselvoyage-backend/tree/feat/SPV-479_store_pass-through_visits_in_previous_voyage)
**Destination Branch:** [feat/SPV-481_store_non-matching_anchorages_in_previous_voyage](https://github.com/teqplay/vesselvoyage-backend/tree/feat/SPV-481_store_non-matching_anchorages_in_previous_voyage)
**Closed On:** 2022-01-03T12:32:25.348373+00:00
**Status:** MERGED

* Add a new property `passThroughAreas` to the `Voyage` and `Visit` data models
* Move pass-through areas from the updated visit \(when there are still other port areas left\) to `visit.passThroughAreas`
* Move pass-through areas from a deleted visit \(when no port areas area left\) to the previous `voyage.passThroughAreas`
* The changed unit tests cover the changed behavior.

