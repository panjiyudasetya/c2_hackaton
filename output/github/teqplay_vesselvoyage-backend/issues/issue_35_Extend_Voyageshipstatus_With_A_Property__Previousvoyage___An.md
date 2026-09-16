---
id: github:teqplay/vesselvoyage-backend:issue:35
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 35
title: Extend Voyageshipstatus With A Property `Previousvoyage`, And Utilize This
  By Cleaning An Ugly Special Case In The Code
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/35
labels: []
explicit_links: []
---
# Issue #35: Extend Voyageshipstatus With A Property `Previousvoyage`, And Utilize This By Cleaning An Ugly Special Case In The Code

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/35  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ad0e6c32526b...a0e5017d4323](https://github.com/teqplay/vesselvoyage-backend/compare/ad0e6c32526b...a0e5017d4323)
**Merge commit:** [a0e5017d4323](https://github.com/teqplay/vesselvoyage-backend/commit/a0e5017d4323)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [chore/SPV-480_extend_VoyageShipStatus_with_previousVoyage](https://github.com/teqplay/vesselvoyage-backend/tree/chore/SPV-480_extend_VoyageShipStatus_with_previousVoyage)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-01-03T12:42:25.112761+00:00
**Status:** MERGED

* Extend the data model `VoyageShipStatus` with a property `previousVoyage`
* Cleanup an ugly special case in the function `startVoyage()` that is no longer needed now
* This is preparation for future PR’s which will store pass-through visits and non-matching anchorages in the previous voyage instead of throwing them away. After that, we can visualize them in the frontend to get a better view of what a ship did.
* No new unit tests where needed: the existing unit tests cover the old special case already, which is now handled more neatly with the new `.previousVoyage` property.

