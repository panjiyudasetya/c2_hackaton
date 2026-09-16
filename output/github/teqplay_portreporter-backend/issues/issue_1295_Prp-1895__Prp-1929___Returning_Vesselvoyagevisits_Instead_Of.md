---
id: github:teqplay/portreporter-backend:issue:1295
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1295
title: 'Prp-1895, Prp-1929 : Returning Vesselvoyagevisits Instead Of Vesselvoyage''S
  Visits In Two Endpoints.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1295
labels: []
explicit_links: []
---
# Issue #1295: Prp-1895, Prp-1929 : Returning Vesselvoyagevisits Instead Of Vesselvoyage'S Visits In Two Endpoints.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1295  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [aa2b93e6d1e7...01011d1f335a](https://github.com/teqplay/portreporter-backend/compare/aa2b93e6d1e7...01011d1f335a)
**Merge commit:** [01011d1f335a](https://github.com/teqplay/portreporter-backend/commit/01011d1f335a)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop, Darius Wattimena, Shan Minh Nguyen
**Approvers:** Wouter Naloop
**Source Branch:** [fix/PRP-1985/PRP-1929/returning_VesselVoyageVisits_instead_of_VesselVoyage_Visits](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1985/PRP-1929/returning_VesselVoyageVisits_instead_of_VesselVoyage_Visits)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-23T07:17:05.131064+00:00
**Status:** MERGED

Damon needed the PortReporter’s `VesselVoyageVisit` model, not the VesselVoyage’s `Visit` model.

