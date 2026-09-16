---
id: github:teqplay/vesselvoyage-backend:pr:618
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 618
title: TCC-424 Journey ETAs
author: Darius-Wattimena
state: closed
date: '2025-09-29'
merged_at: '2025-10-03'
base_branch: develop
head_branch: TCC-424-journey-etas
url: https://github.com/teqplay/vesselvoyage-backend/pull/618
labels: []
linked_issues: []
explicit_links: []
---
# PR #618: TCC-424 Journey ETAs

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/618  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-424-journey-etas`  
**Created:** 2025-09-29  
**Merged:** 2025-10-03  

## Description

_No description._

## Commits

- `e959d35e` **Darius Wattimena** (2025-09-18): Adjusted journey service to include the new ETA predictions
- `10f5e032` **Darius Wattimena** (2025-09-26): Added Voyage ID as well to the journey model when Voyage is known
- `d9a70b82` **Darius Wattimena** (2025-09-26): Merge branch 'develop' into TCC-424-journey-etas
- `0ec4fbe0` **Darius Wattimena** (2025-09-29): Merge branch 'TCC-422-eta-predictions' into TCC-424-journey-etas
- `425716ff` **Darius Wattimena** (2025-10-02): Add API docs for the voyageId field
- `734cc628` **Darius Wattimena** (2025-10-02): Merge branch 'develop' into TCC-424-journey-etas

## Reviews

### TeqJoostD — COMMENTED (2025-09-30)

_No comment._

### TeqJoostD — DISMISSED (2025-09-30)

NTH comment

### Darius-Wattimena — COMMENTED (2025-10-02)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-02)

## Pull Request Overview

Adds ETA (Estimated Time of Arrival) functionality to journey tracking by integrating ESoF (Electronic Statement of Facts) data and implementing travel time calculations.

- Integrates ESoF data to provide ETAs for arrival ports
- Adds travel time calculation based on current time and destination ETA
- Includes voyageId field to track voyage entries for journey legs

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| JourneyService.kt | Implements ETA calculation logic, integrates ESoF data, and adds voyageId tracking |
| Journey.kt | Adds voyageId field to the Journey data model with proper schema documentation |

### TeqJoostD — APPROVED (2025-10-02)

_No comment._

## Review Comments

### TeqJoostD — 2025-09-30 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Journey.kt`

No docs?

### Darius-Wattimena — 2025-10-02 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Journey.kt`

Oh good point, let me add those

### Copilot — 2025-10-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyService.kt`

The function name `calculateTravelTime` is misleading as it calculates remaining time to destination rather than actual travel time. Consider renaming to `calculateRemainingTravelTime` or `calculateTimeToDestination` to better reflect its purpose.
