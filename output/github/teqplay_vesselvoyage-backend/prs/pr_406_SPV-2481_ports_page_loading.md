---
id: github:teqplay/vesselvoyage-backend:pr:406
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 406
title: SPV-2481 ports page loading
author: Darius-Wattimena
state: closed
date: '2025-01-31'
merged_at: '2025-02-04'
base_branch: develop
head_branch: SPV-2481-ports-page-loading
url: https://github.com/teqplay/vesselvoyage-backend/pull/406
labels: []
linked_issues: []
explicit_links: []
---
# PR #406: SPV-2481 ports page loading

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/406  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2481-ports-page-loading`  
**Created:** 2025-01-31  
**Merged:** 2025-02-04  

## Description

This PR cuts in half the amount of time we need to wait when loading the ports page. Going from 60+ seconds for NLRTM to like 30~ seconds and even less when you also select a ship category.

## Commits

- `28a3387a` **Darius Wattimena** (2025-01-28): Moved logic of retrieving the port page to its own service and made it so we get all data using coroutines async jobs
- `d096bf50` **Darius Wattimena** (2025-01-30): Added some custom queries adding projections as well so we only have to load in a fraction of the data for the ports page
- `01a6adee` **Darius Wattimena** (2025-01-31): Code cleanup
- `3c2c428c` **Darius Wattimena** (2025-01-31): Set logging to debug to avoid spamming the logs when people load in the ports page
- `94c858b0` **Darius Wattimena** (2025-02-03): Merge branch 'refs/heads/develop' into SPV-2481-ports-page-loading
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingFrontendViewV2Controller.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVisitDataSource.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt
- `b49e64a4` **Darius Wattimena** (2025-02-03): Merge branch 'refs/heads/develop' into SPV-2481-ports-page-loading
- `95097f14` **Darius Wattimena** (2025-02-03): Move logic of minimal visits and voyages to the frontend service instead
- `badca63b` **Darius Wattimena** (2025-02-03): ktlint

## Reviews

### leonjoosse — CHANGES_REQUESTED (2025-02-03)

As discussed offline, in the Visit/VoyageV2Service, please return the fully populated object instead of half the information. Also placed some comments to indicate the places.

### leonjoosse — APPROVED (2025-02-04)

_No comment._

## Review Comments

### leonjoosse — 2025-02-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VisitV2Service.kt`

Please return the minimal visit instead, as other functions in this class do return the full visit with all information 

### leonjoosse — 2025-02-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VoyageV2Service.kt`

Please return the minimal visit instead, as other functions in this class do return the full visit with all information

### leonjoosse — 2025-02-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/api/VoyageV2Service.kt`

Please return the minimal visit instead, as other functions in this class do return the full visit with all information
