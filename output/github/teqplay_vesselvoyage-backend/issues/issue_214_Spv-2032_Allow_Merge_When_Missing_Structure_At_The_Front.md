---
id: github:teqplay/vesselvoyage-backend:issue:214
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 214
title: Spv-2032 Allow Merge When Missing Structure At The Front
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/214
labels: []
explicit_links:
- jira:SPV-2032
- jira:SPV-2076
---
# Issue #214: Spv-2032 Allow Merge When Missing Structure At The Front

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/214  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [13ac5c7b33db...68681a0dc605](https://github.com/teqplay/vesselvoyage-backend/compare/13ac5c7b33db...68681a0dc605)
**Merge commit:** [68681a0dc605](https://github.com/teqplay/vesselvoyage-backend/commit/68681a0dc605)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2032-allow-merge-when-missing-structure](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2032-allow-merge-when-missing-structure)
**Destination Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Closed On:** 2024-08-26T07:49:35.784492+00:00
**Status:** MERGED

* feat: allow merging when data is missing on the left of the visit/voyage structure
* fix: don't allow merging when missing data at the end for now
* chore: remove redundant notes
* chore: cleanup

Previously when merging it was a requirement for VesselVoyage to have voyages to merge with at both ends. Meaning we needed a `firstOldVoyage` and a `lastOldVoyage`, within this period we could merge `newEntries` coming from \(r\)events \(not to be confused with the V2 `NewEntry`, merging works for both V1 and V2, naming in this file is `oldEntries=current VesselVoyage entries,` `newEntries=new entries coming from (r)events`\).
This change allows for merging data when there is no `firstOldVoyage` available. This could happen when:
* We didn’t have any context data, like ports, mapped in POMA until 2022.
* We do have data for the ship from 2019 to 2022 \(even up to now\), but it was not included in VesselVoyage due to missing data in POMA.
* Now that data is mapped in POMA \(2022\), we do get visits and voyages for this ship.
This PR allows regenerating this ship from 2019 to 2022, and then allowing it to do a “merge at the start” with the data from 2022 and onwards.

The above is represented in a check which determines `missesStart` and `missesEnd`, which checks if VesselVoyage data is returned within our time frame, and if data at the start or end misses. And if data misses, we know that VesselVoyage should not have more data either at the start or end.
Currently `missesEnd` is not implemented yet, the reasoning described by this TODO:
```kotlin
    // TODO: for now only allowing merge if data is available at the end
    //  We have lots of freedom at the start, since we will not need to interact with the real-time processing.
    //  Allowing interacting with the (moving) end would require locking the real-time access and ensure in-memory state is updated.
    require(!missesEnd) { "Old entries are required to have overlap at the end, data is missing." }
    // require(!missesStart || !missesEnd) { "Old entries are required to overlap either at the start or end, but none did." }
```
Will need to think about that one a bit more, to see if and how we could achieve to do that. So that will be done separately, if it turns out to be possible.

