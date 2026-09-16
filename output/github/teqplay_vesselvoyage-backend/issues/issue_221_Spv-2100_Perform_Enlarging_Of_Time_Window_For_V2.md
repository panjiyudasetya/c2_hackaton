---
id: github:teqplay/vesselvoyage-backend:issue:221
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 221
title: Spv-2100 Perform Enlarging Of Time Window For V2
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/221
labels: []
explicit_links: []
---
# Issue #221: Spv-2100 Perform Enlarging Of Time Window For V2

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/221  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [f2d5672e78ee...56f0b2cb23fe](https://github.com/teqplay/vesselvoyage-backend/compare/f2d5672e78ee...56f0b2cb23fe)
**Merge commit:** [56f0b2cb23fe](https://github.com/teqplay/vesselvoyage-backend/commit/56f0b2cb23fe)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2100-perform-enlarging-of-time-window-for-v2](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2100-perform-enlarging-of-time-window-for-v2)
**Destination Branch:** [SPV-2076-merging-v2-logic](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2076-merging-v2-logic)
**Closed On:** 2024-05-01T13:53:34.078141+00:00
**Status:** MERGED

* chore: only allow running one guarantee from the API
* feat: enlarge V2 TimeWindow separately & consolidate skeleton TimeWindow and Instant usage
  
When recalculating by ship we need to check if the `TimeWindow` needs to be enlarged.
For example when a `TimeWindow` that is inside a `Visit` is provided, we need to enlarge it to be the `previousVoyage.startTime` and `nextVoyage.endTime`. This ensures merging back will have all data available.

To enable this, it’s now required to supply recalculating either `V1` OR `V2`, not both. Depending on that setting we enlarge the `TimeWindow` based on `V1` or `V2`.  
_\(Do note though, that VesselVoyage internally still supports updating both V1 and V2 at the same time, but this enlarging check will not be done at that level\)_
```kotlin
        val window = when (guarantee) {
            Guarantee.V1 -> recalculationEnlargeTimeWindowService.enlargeTimeWindowBasedOnVoyagesV1(imo, start, end)
            Guarantee.V2 -> recalculationEnlargeTimeWindowService.enlargeTimeWindowBasedOnVoyagesV2(imo, start, end)
        }
```

Also took the time to pro-actively migrate some places in the merging code to use `Instant` instead of `ZonedDateTime`.

