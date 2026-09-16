---
id: github:teqplay/portreporter-backend:issue:1273
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1273
title: 'Prp-1895 + Prp-1898 : Add Vesselvoyage Endpoints To Get Visit Or Voyage By
  Their Id. Portreporter Mirrored Classes For Vesselvoyage.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1273
labels: []
explicit_links: []
---
# Issue #1273: Prp-1895 + Prp-1898 : Add Vesselvoyage Endpoints To Get Visit Or Voyage By Their Id. Portreporter Mirrored Classes For Vesselvoyage.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1273  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [673d11a5e25d...46e700f50595](https://github.com/teqplay/portreporter-backend/compare/673d11a5e25d...46e700f50595)
**Merge commit:** [46e700f50595](https://github.com/teqplay/portreporter-backend/commit/46e700f50595)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Joost Laurman
**Source Branch:** [feat/PRP-1895/PRP-1898/extend_vessel_voyage_endpoints](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1895/PRP-1898/extend_vessel_voyage_endpoints)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-16T15:15:38.625348+00:00
**Status:** MERGED

1. Adding endpoints `[GET] /v1/vesselvoyage/visit/{id}` and `[GET] /v1/vesselvoyage/voyaget/{id}`
2. Adding also internal mirror data models of VesselVoyage \(all of them included in the package `import nl.teqplay.portreporter.model.internal.vesselvoyage`\).
3. Include the imo in the `VesselVoyageVisit` for `VesselVoyageVisitBucket`

