---
id: github:teqplay/vesselvoyage-backend:pr:508
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 508
title: 'SPV-2617: Extend StatementOfFacts in the VesselVoyageClient, allowing to retrieve
  SOFs by imo and port, including batch calls'
author: leonjoosse
state: closed
date: '2025-05-21'
merged_at: '2025-05-22'
base_branch: develop
head_branch: SPV-2617-portreporter-sof-view-extend-sof-client-methods
url: https://github.com/teqplay/vesselvoyage-backend/pull/508
labels: []
linked_issues: []
explicit_links: []
---
# PR #508: SPV-2617: Extend StatementOfFacts in the VesselVoyageClient, allowing to retrieve SOFs by imo and port, including batch calls

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/508  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2617-portreporter-sof-view-extend-sof-client-methods`  
**Created:** 2025-05-21  
**Merged:** 2025-05-22  

## Description

This pull request adds new methods to the `VesselVoyageClient` class to support querying statement of facts (SOF) for ships by IMO or port, with additional batch request capabilities. These changes enhance the client’s functionality by introducing flexible querying options and support for filtering results based on various parameters.

### New Methods for SOF Queries:

* **Query by IMO**:
  - Added `findByImo` method to retrieve SOF for a specific ship by IMO, with support for filtering by time range, recent items, and flags like `finished` or `confirmed`.
  - Added `findByImoBatch` method to handle batch requests for multiple IMO-based queries.

* **Query by Port**:
  - Added `findByPort` method to retrieve SOF for ships in a specific port or area, with filtering options for time range, recent items, categories, and flags like `finished` or `confirmed`.
  - Added `findByPortBatch` method to handle batch requests for multiple port-based queries.

## Commits

- `a0e89fcf` **leonj** (2025-05-20): Extend StatementOfFacts in the VesselVoyageClient, allowing to retrieve SOFs by imo and port, including batch calls
- `da708bdf` **Leon Joosse** (2025-05-22): Fix wrong parameter type ByPortRequest, should be ByImoRequest
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-21)

## Pull Request Overview

This PR extends the VesselVoyageClient with methods to retrieve Statement of Facts (SOF) for ships by IMO or port, including support for batch queries.  
- Introduces findByImo and findByImoBatch methods for IMO-based queries.  
- Adds findByPort and findByPortBatch methods for port-based queries.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-21)

## Pull Request Overview

This PR extends the VesselVoyageClient functionality by adding methods for retrieving Statement of Facts (SOF) data by IMO and port, including support for batch queries.  
- Added new query methods: findByImo, findByImoBatch, findByPort, and findByPortBatch  
- Enhances filtering options such as time ranges, finished/confirmed states, and ship categories

### TeqJoostD — COMMENTED (2025-05-21)

_No comment._

### Darius-Wattimena — APPROVED (2025-05-22)

_No comment._

## Review Comments

### Copilot — 2025-05-21 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

The body parameter type in the findByImoBatch method appears to be incorrect; consider using a request type specific to IMO queries (e.g., ByImoRequest) for consistency with the method's intent.
```suggestion
            body: List<ByImoRequest>
```

### TeqJoostD — 2025-05-21 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

Good catch
