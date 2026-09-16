---
id: github:teqplay/vesselvoyage-backend:issue:175
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 175
title: 'Fix: Disable Trace Calculations When Performing Ais-Engine Dry-Run'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/175
labels: []
explicit_links: []
---
# Issue #175: Fix: Disable Trace Calculations When Performing Ais-Engine Dry-Run

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/175  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [058d0ea8b4d9...0ea49faa85ee](https://github.com/teqplay/vesselvoyage-backend/compare/058d0ea8b4d9...0ea49faa85ee)
**Merge commit:** [0ea49faa85ee](https://github.com/teqplay/vesselvoyage-backend/commit/0ea49faa85ee)
**Author:** Former user
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/disable-trace-calculations-for-aisengine-processing](https://github.com/teqplay/vesselvoyage-backend/tree/fix/disable-trace-calculations-for-aisengine-processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-03-12T09:49:16.931006+00:00
**Status:** MERGED

My assumption was adding this to the config would fix it:
```
event-processing.enable-trace-calculations=false
```
But it turned out to not be the case. Due to it being always overwritten:
```kotlin
    /**
     * Process an [Event] resulting in a [EventProcessingResult].
     *
     * @param shipStatus The current status of the ship at the time when the [event] was received.
     * @param event The [Event] we want to process.
     * @param enableTraceCalculations When true the visit and voyages will be enhanced by requesting ship traces.
     */
    fun onEvent(
        shipStatus: ShipStatus,
        event: Event,
        enableTraceCalculations: Boolean = true
    ): EventProcessingResult {
```
Not sure what the reason behind that is, but have disabled that for dry-running in ais-engine.
But even then not all trace calculations are stopped.. so need to add the config property as well.

In the context of PTO, stops will still be generated since they are done separately and it doesn’t look at this config property.

