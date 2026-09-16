---
id: github:teqplay/vesselvoyage-backend:pr:387
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 387
title: 'PTO SOF: Pilot fallbacks (also expose fallback type)'
author: leonjoosse
state: closed
date: '2024-12-24'
merged_at: '2025-01-20'
base_branch: develop
head_branch: SPV-2410-locationtime-fallback-reason
url: https://github.com/teqplay/vesselvoyage-backend/pull/387
labels: []
linked_issues: []
explicit_links: []
---
# PR #387: PTO SOF: Pilot fallbacks (also expose fallback type)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/387  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2410-locationtime-fallback-reason`  
**Created:** 2024-12-24  
**Merged:** 2025-01-20  

## Description

_No description._

## Commits

- `8ad39a2e` **leonj** (2024-12-02): Add endpoint for front-end ports page, to combine all calls in one
- `f1b2ab12` **leonj** (2024-12-02): Rework the pilot info class, it was too complicated. Now accepts both encounter and areaActivity, and uses nullability to figure out which one to use.
- `6938c15e` **leonj** (2024-12-19): Merge branch 'refs/heads/develop' into SPV-2410-locationtime-fallback-reason
- `17bba948` **leonj** (2024-12-24): Add fallback detection type for PTO SOF view. Expose LocationTime fallback to the API.
  Note that these fallbacks are different: (1) for pilot detection (encounter events, fallback sailing through pilot area) and (2) fallback for pilot detection end locationtime. The latter case may occur with the pilot area fallback, where the area.end event is not there. Another (encompassing) area event may then serve as the area.end event.
- `65baa361` **leonj** (2024-12-24): Merge branch 'refs/heads/develop' into SPV-2410-locationtime-fallback-reason
- `1b21f01f` **leonj** (2025-01-17): Merge branch 'develop' into SPV-2410-locationtime-fallback-reason
- `ab688422` **leonj** (2025-01-17): Clarify find inbound/outbound pilot by area names that it's a fallback method
- `8bad8bb5` **leonj** (2025-01-17): Add tests for PTO sof fallback inbound/outbound pilot

## Reviews

### TeqJoostD — APPROVED (2025-01-06)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-01-06)

Looks mostly fine. Left some small comments.
I also miss any tests covering the new usecase of pilot fallbacks?

### leonjoosse — COMMENTED (2025-01-17)

_No comment._

### Darius-Wattimena — APPROVED (2025-01-17)

_No comment._

### Darius-Wattimena — COMMENTED (2025-01-17)

_No comment._

## Review Comments

### Darius-Wattimena — 2025-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/ptoview/PilotInfo.kt`

If we are going this way then I would rather create 2 extra constructors where you can create a `PilotInfo` based on those inputs as we are not really doing something with the static functions then create a `PilotInfo`?

### Darius-Wattimena — 2025-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

Would rename to `fallbackInboundPilotByArea` to explicitly indicated that this is a fallback

### Darius-Wattimena — 2025-01-06 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

Would do same here explicitly say that this is a fallback

### leonjoosse — 2025-01-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/ptoview/PilotInfo.kt`

What do you mean with 'this way'? Pointing at collecting all variables in one class, or having the static methods?
In case of the static methods, I wanted to use the method name to clarify what we are expecting. 
I'm fine with implementing it in another way, so let's discuss if you'd like to see it different than the current implementation.

### Darius-Wattimena — 2025-01-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/esof/ptoview/PilotInfo.kt`

What I meant is just have this as a constructor.

So for example:
```
data class PilotInfo(...) {
    constructor(encounter: NewEncounter, pilotArea: PilotBoardingPlace?): this(...)
    constructor(pilotAreaActivity: AreaActivity, pilotArea: PilotBoardingPlace?): this(...)
}
```

This way you avoid the need for static functions. As that is not really that clean for a data class in my mind. Besides us never using a structure like that in the VesselVoyage backend.

## Comments

### leonjoosse — 2025-01-17

Added tests, this actually helped to find a case with the fallback outbound pilot: before writing tests it was selecting the **first pilot** after last berth, where it needs to be **last pilot** after last berth.
Good point Darius to still implement the tests.
