---
id: github:teqplay/vesselvoyage-backend:pr:537
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 537
title: Release 16 Jun 2025
author: Darius-Wattimena
state: closed
date: '2025-06-16'
merged_at: '2025-06-16'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/537
labels: []
linked_issues: []
explicit_links: []
---
# PR #537: Release 16 Jun 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/537  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-06-16  
**Merged:** 2025-06-16  

## Description

_No description._

## Commits

- `8f713816` **leonj** (2025-06-05): Filtering visit/voyage/sof results by DWT/TEU filters is too slow. Instead of filtering afterwards, select the list of IMOs upfront and use it in the database query
- `f017503b` **leonj** (2025-06-10): Test indexes for voyages
- `4caff79f` **leonj** (2025-06-10): Fix json sub types for VoyagesByPortRequest
- `dfbdb6de` **leonj** (2025-06-10): Make return types explicit in the VesselVoyageClient when calling the restTemplate methods, hopefully helps in resolving the mapping issues on the callers end
- `5f7ac07d` **Joost Dambrink** (2025-06-11): Merge pull request #535 from teqplay/master
  Master into develop
- `828197bb` **leonj** (2025-06-13): Rework the request and response data classes
- `3789e9f7` **leonj** (2025-06-13): Remove unused interface
- `9e6b9a3c` **Darius Wattimena** (2025-06-16): Merge pull request #529 from teqplay/TCC-191-dwt-teu-performance
  TCC-191: Filtering visit/voyage/sof results by DWT/TEU filters is too slow
