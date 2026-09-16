---
id: github:teqplay/vesselvoyage-backend:issue:203
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 203
title: 'Fix: After Splitting Voyage At Front/End, Ensure Esof Entries Are Filtered
  To Still Be Overlapping With The Voyage'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/203
labels: []
explicit_links: []
---
# Issue #203: Fix: After Splitting Voyage At Front/End, Ensure Esof Entries Are Filtered To Still Be Overlapping With The Voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/203  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [117a2be469ac...507b7dd6a6f8](https://github.com/teqplay/vesselvoyage-backend/compare/117a2be469ac...507b7dd6a6f8)
**Merge commit:** [507b7dd6a6f8](https://github.com/teqplay/vesselvoyage-backend/commit/507b7dd6a6f8)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2031-when-splitting-voyage-filter-overlapping-esof-entries](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2031-when-splitting-voyage-filter-overlapping-esof-entries)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-12T07:14:01.071020+00:00
**Status:** MERGED

For a case where VesselVoyage has one voyage and it needs to be merged with a visit, it should result in the voyage being split into two interleaved with the visit.
```none
Original/current voyage
|-------------------------------------|
    New visit coming from (r)events
              ___________
             |___________|
Should result in: voyage > visit > voyage
              ___________
|------------|___________|------------|
```
However, let’s say that voyage has two stops \(or encounters, any ESof entry will do\). One stop might be just before the visit, and one might be just after the visit. Since the voyage is split/duplicated into two, to allow inserting the new visit, the ESof data is also duplicated.
If there would be no filter on the ESof data, that would mean that the stops and encounters are duplicated and exist both in the voyage on the left and on the voyage on the right.
This PR fixes that, by checking that any stops and encounters are still overlapping with the `Voyage.startTime` and `Voyage.endTime` bounds. If not, they are removed.

NOTE: This will only work for the V1 definitions. Currently there is no support for V2 definitions yet, but there this logic will be different to not check if stops\(/encounters\) are overlapping, but instead check if they are exactly inside.

