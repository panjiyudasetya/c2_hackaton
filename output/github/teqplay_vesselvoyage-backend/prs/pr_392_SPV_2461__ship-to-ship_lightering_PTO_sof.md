---
id: github:teqplay/vesselvoyage-backend:pr:392
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 392
title: 'SPV 2461: ship-to-ship lightering PTO sof'
author: leonjoosse
state: closed
date: '2025-01-16'
merged_at: '2025-01-17'
base_branch: develop
head_branch: SPV-2461-lightering-sof
url: https://github.com/teqplay/vesselvoyage-backend/pull/392
labels: []
linked_issues: []
explicit_links: []
---
# PR #392: SPV 2461: ship-to-ship lightering PTO sof

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/392  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2461-lightering-sof`  
**Created:** 2025-01-16  
**Merged:** 2025-01-17  

## Description

This adds ship-to-ship data to the PTO SOF.
POMA dependency is upgraded to include details of the ship-to-ship areas.

## Commits

- `fe7a4a4b` **leonj** (2025-01-13): Add ship-to-ship to PTO sof
- `0aaa7883` **leonj** (2025-01-16): Merge branch 'SPV-2460-lightering-encounters' into SPV-2461-lightering-sof
- `bdc221c6` **leonj** (2025-01-16): Fix tests
- `6e62c5cd` **leonj** (2025-01-16): Upgrade POMA 20240510-b1743 -> 20250110-b2514 to use the ShipToShip lightering area. Fix tests because of added property Berth.displayName
- `f3cde481` **leonj** (2025-01-16): Merge branch 'SPV-2460-lightering-encounters' into SPV-2461-lightering-sof
- `00a09ff4` **leonj** (2025-01-16): Add ShipToShip to InfraService and PomaClient
- `4dd0a261` **leonj** (2025-01-16): Add ShipToShip area details to PtoStatementOfFacts, instead of just returning the area id
- `c5df2f69` **leonj** (2025-01-16): Tests for PtoStatementOfFactsMapper
- `d1e9c0e1` **leonj** (2025-01-16): Amend tests for PtoStatementOfFactsViewGenerator
- `c5cf6a69` **leonj** (2025-01-17): Rename shipToShip to ShipToShipTransfer
  Allow nullability of ShipToShipTransfer.end
- `ee1e7706` **leonj** (2025-01-17): Ship details function in PtoStatementOfFactsViewGenerator

## Reviews

### leonjoosse — COMMENTED (2025-01-16)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2025-01-16)

_No comment._

### leonjoosse — COMMENTED (2025-01-17)

_No comment._

### leonjoosse — COMMENTED (2025-01-17)

_No comment._

### Darius-Wattimena — APPROVED (2025-01-17)

_No comment._

## Review Comments

### leonjoosse — 2025-01-16 on `src/test/kotlin/nl/teqplay/vesselvoyage/util/PomaUtilsTest.kt`

customArea.ports changed to non-nullable, so this test can be removed

### Darius-Wattimena — 2025-01-16 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/PtoStatementOfFactsView.kt`

Should be nullable as they can be ongoing

### Darius-Wattimena — 2025-01-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt`

`toShipToShip` sounds a bit weird for a function name. Might be nicer to refer that this is a transfer?

### Darius-Wattimena — 2025-01-16 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/PtoStatementOfFactsView.kt`

Would call this `ShipToShipTransfer` instead of `ShipToShip`?

### Darius-Wattimena — 2025-01-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

Not sure how you use this but it might be nice to have a combined function that does first try to find the ship details by IMO and if not found then it tries by MMSI?

### leonjoosse — 2025-01-17 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/sof/PtoStatementOfFactsView.kt`

Oef, good catch. That would have bitten us quite annoyingly

### leonjoosse — 2025-01-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/mapper/PtoStatementOfFactsMapper.kt`

Agree, will add `Transfer` to the name
