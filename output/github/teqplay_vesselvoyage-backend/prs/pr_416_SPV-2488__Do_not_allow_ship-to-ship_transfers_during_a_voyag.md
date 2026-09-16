---
id: github:teqplay/vesselvoyage-backend:pr:416
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 416
title: 'SPV-2488: Do not allow ship-to-ship transfers during a voyage'
author: leonjoosse
state: closed
date: '2025-02-13'
merged_at: '2025-02-18'
base_branch: develop
head_branch: SPV-2488-shiptoship-only-in-visits
url: https://github.com/teqplay/vesselvoyage-backend/pull/416
labels: []
linked_issues: []
explicit_links: []
---
# PR #416: SPV-2488: Do not allow ship-to-ship transfers during a voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/416  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2488-shiptoship-only-in-visits`  
**Created:** 2025-02-13  
**Merged:** 2025-02-18  

## Description

 Ship-to-ship end encounters during a voyage are applied to the previous visit, if that event was ended by a fallback mechanism (e.g. sailing out of the EOSP).

Processing of the ship-to-ship encounter events:
- start event processor:
  - on visit: added to esof
  - on voyage: discard and mark as ignored
- end event processor:
  - on visit: end matching item, otherwise discard and mark as ignored
  - on voyage: end matching item in previous visit, otherwise discard and mark as ignored

## Commits

- `b73d7fad` **leonj** (2025-02-12): Do not allow ship-to-ship transfers during a voyage. Ship-to-ship end encounters during a voyage are applied to the previous visit, if that event was ended by a fallback mechanism (e.g. sailing out of the EOSP).

## Reviews

### Darius-Wattimena — CHANGES_REQUESTED (2025-02-13)

_No comment._

### leonjoosse — COMMENTED (2025-02-17)

_No comment._

### Darius-Wattimena — COMMENTED (2025-02-17)

_No comment._

### Darius-Wattimena — APPROVED (2025-02-17)

_No comment._

## Review Comments

### Darius-Wattimena — 2025-02-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/shiptoship/ShipToShipTransferBaseProcessor.kt`

We still want this behaviour to be here, as you still want to override end times when the sts starts in the visit but ends in the voyage?

### leonjoosse — 2025-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/shiptoship/ShipToShipTransferBaseProcessor.kt`

Yes, that happens in the end processor on line 30. Am I missing something?

### Darius-Wattimena — 2025-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/shiptoship/ShipToShipTransferBaseProcessor.kt`

Oh good point, I went over it too quickly I assume when checking the PR
