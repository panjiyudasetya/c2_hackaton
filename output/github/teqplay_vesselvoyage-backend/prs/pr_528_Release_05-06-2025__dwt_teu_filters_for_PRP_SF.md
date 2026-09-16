---
id: github:teqplay/vesselvoyage-backend:pr:528
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 528
title: Release 05-06-2025 (dwt/teu filters for PRP/SF)
author: leonjoosse
state: closed
date: '2025-06-05'
merged_at: '2025-06-05'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/528
labels: []
linked_issues: []
explicit_links: []
---
# PR #528: Release 05-06-2025 (dwt/teu filters for PRP/SF)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/528  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-06-05  
**Merged:** 2025-06-05  

## Description

_No description._

## Commits

- `12f5a3fc` **leonj** (2025-05-28): Pass finished property for voyage by port call to underlying service/database layer
- `139bbff9` **leonj** (2025-06-02): Add support for filtering by minTeu-maxTeu / minDwt-maxDwt to byPort requests in the V2 visits / voyages / sof APIs
- `4d72cf75` **leonj** (2025-06-02): Merge branch 'develop' into TCC-135-visit-by-ais-destination
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiVoyageV2Controller.kt
- `5e348268` **leonj** (2025-06-03): Remove unrelated byAisTrueDestination implementation
- `c08a85c0` **leonj** (2025-06-03): Remove too aggressive CONTAINER + minTeu/maxTeu check
- `1ba48f87` **leonj** (2025-06-03): Also validate dwt/teu in ApiStatementOfFactsV2Controller.byPort()
- `4d54b157` **leonj** (2025-06-03): Extend visit and SOF byPort with aisTrueDestination (NewEntry.destination.actual), which is the resolved unlocode of the AIS destination entered by the captain
- `c779aa7d` **leonj** (2025-06-03): Tighten when DWT/TEU can be used
- `da0879aa` **leonj** (2025-06-04): Remove duplicate validation
- `ed7f8358` **Leon Joosse** (2025-06-04): Merge pull request #523 from teqplay/TCC-134-visits-ais-destination
  TCC-134: Extend visit and SOF byPort with aisTrueDestination filter
- `d6bbcd08` **leonj** (2025-06-04): Fix a bug in querying start/end times in the NewEntryDataSource
- `07cf7303` **leonj** (2025-06-04): Fix a bug in querying start/end times in the NewEntryDataSource (update method docs)
- `88ecb4ee` **leonj** (2025-06-05): Add dwt/teu filters to VesselVoyageClient
- `c8a29a58` **Leon Joosse** (2025-06-05): Merge pull request #522 from teqplay/TCC-137-filter-category-and-dwt-teu
  TCC-137: extend byPort API endpoints with DWT / TEU filter (only when category present)
