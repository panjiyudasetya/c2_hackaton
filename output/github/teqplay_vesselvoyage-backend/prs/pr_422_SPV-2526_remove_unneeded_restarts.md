---
id: github:teqplay/vesselvoyage-backend:pr:422
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 422
title: SPV-2526 remove unneeded restarts
author: Darius-Wattimena
state: closed
date: '2025-02-14'
merged_at: '2025-02-17'
base_branch: develop
head_branch: SPV-2526-remove-unneeded-restarts
url: https://github.com/teqplay/vesselvoyage-backend/pull/422
labels: []
linked_issues: []
explicit_links: []
---
# PR #422: SPV-2526 remove unneeded restarts

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/422  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2526-remove-unneeded-restarts`  
**Created:** 2025-02-14  
**Merged:** 2025-02-17  

## Description

This PR:
1. Removes the Platform client, as we can use AisEngine clients for all of that + no way to exclude the health indicator without adjusting the skeleton-plugins code.
2. Remove the auto loading of the `AutoTimeoutHealthIndicator` made by Shan from skeleton-plugins. This was exposed in the health actuator, even though it wasn't used at all by VesselVoyage.

With those changes I hope that we will see even less restarts, as both those health checks could bring the system down.


## Commits

- `2c238a0c` **Darius Wattimena** (2025-02-14): Replaced all things that still used the old platform events with ais engine events
- `0ff5d25c` **Darius Wattimena** (2025-02-14): Exclude skeleton plugin health checks which are not needed for VesselVoyage
- `48ec1080` **Darius Wattimena** (2025-02-14): Some more code clean up
- `598d0e27` **Darius Wattimena** (2025-02-14): ktlint

## Reviews

### leonjoosse — CHANGES_REQUESTED (2025-02-17)

_No comment._

### Darius-Wattimena — COMMENTED (2025-02-17)

_No comment._

### leonjoosse — COMMENTED (2025-02-17)

_No comment._

### leonjoosse — DISMISSED (2025-02-17)

_No comment._

### leonjoosse — APPROVED (2025-02-17)

_No comment._

## Review Comments

### leonjoosse — 2025-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/EventFetchingService.kt`

Would it make sense to convert `ZonedDateTime` already to `Instant` here? Not sure what the impact would be, but as we're touching this method anyway...

### Darius-Wattimena — 2025-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/EventFetchingService.kt`

I was thinking that first as well. I tried it at first, but ended up having to change 5+ places and also controllers that we then have to adjust to use `Instant` which is not very nice ...

For now just calling `toInstant()` on both start and end seems to me the fastest and easiest way

### leonjoosse — 2025-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/EventFetchingService.kt`

Ah okay, too much stuff to change, no problemo 😉 
