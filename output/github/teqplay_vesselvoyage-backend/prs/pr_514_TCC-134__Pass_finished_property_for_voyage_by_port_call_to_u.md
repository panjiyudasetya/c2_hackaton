---
id: github:teqplay/vesselvoyage-backend:pr:514
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 514
title: 'TCC-134: Pass finished property for voyage by port call to underlying service/database'
author: leonjoosse
state: closed
date: '2025-05-26'
merged_at: '2025-06-02'
base_branch: develop
head_branch: TCC-134-api-fix-finished-flag
url: https://github.com/teqplay/vesselvoyage-backend/pull/514
labels: []
linked_issues: []
explicit_links: []
---
# PR #514: TCC-134: Pass finished property for voyage by port call to underlying service/database

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/514  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `TCC-134-api-fix-finished-flag`  
**Created:** 2025-05-26  
**Merged:** 2025-06-02  

## Description

_No description._

## Commits

- `afe13e06` **leonj** (2025-05-26): Pass finished property for voyage by port call to underlying service/database layer

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-26)

## Pull Request Overview

This PR extends the voyage-by-port-call endpoints to forward the new `finished` filter parameter through to the service/database layer.

- Adds `finished` to all three `VoyagesBy…` request constructors
- Ensures the controller methods accept and pass through the `finished` flag
- Supports filtering voyages by completion status


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt:117**
* Add or update unit/integration tests to verify that the `finished` flag correctly filters voyage results in the controller and underlying service.
```
finished = finished
```
</details>

### Darius-Wattimena — APPROVED (2025-06-02)

_No comment._

## Review Comments

### Copilot — 2025-05-26 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

The new `finished` query parameter should be documented (e.g. OpenAPI annotations or KDoc) so API consumers know how to filter by finished status.

### Copilot — 2025-05-26 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt`

[nitpick] The repetitive addition of `finished` across multiple request constructors could be refactored into a shared helper or builder to reduce duplication.
