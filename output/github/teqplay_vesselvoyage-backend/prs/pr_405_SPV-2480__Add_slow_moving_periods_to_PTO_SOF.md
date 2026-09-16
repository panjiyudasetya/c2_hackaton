---
id: github:teqplay/vesselvoyage-backend:pr:405
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 405
title: 'SPV-2480: Add slow moving periods to PTO SOF'
author: leonjoosse
state: closed
date: '2025-01-31'
merged_at: '2025-02-03'
base_branch: develop
head_branch: SPV-2480-pto-sof-slowsteaming
url: https://github.com/teqplay/vesselvoyage-backend/pull/405
labels: []
linked_issues: []
explicit_links: []
---
# PR #405: SPV-2480: Add slow moving periods to PTO SOF

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/405  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2480-pto-sof-slowsteaming`  
**Created:** 2025-01-31  
**Merged:** 2025-02-03  

## Description

When creating the PTO statement of facts we will group the drifting moments in 3 different groups with the in-between edges between the 3 groups:

- Arrival drifting
- Boundary: Pilot inbound start / Fallback first visit port start
- In-port drifting
- Boundary: Pilot outbound start / Fallback last visit port end
- Departure drifting

## Commits

- `b4c9536a` **leonj** (2025-01-31): Add slow moving periods to PTO SOF

## Reviews

### leonjoosse — COMMENTED (2025-01-31)

_No comment._

### TeqJoostD — COMMENTED (2025-02-03)

_No comment._

### TeqJoostD — APPROVED (2025-02-03)

_No comment._

## Review Comments

### leonjoosse — 2025-01-31 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGeneratorTest.kt`

Found an empty test, let's clean it up...

### TeqJoostD — 2025-02-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt`

Do you only look at start time when determining the segments. What happens when a slow moving period falls in before and afther the port end/start?
