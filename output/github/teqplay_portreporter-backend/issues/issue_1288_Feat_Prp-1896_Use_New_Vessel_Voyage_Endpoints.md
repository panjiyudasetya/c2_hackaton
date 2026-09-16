---
id: github:teqplay/portreporter-backend:issue:1288
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1288
title: Feat/Prp-1896/Use New Vessel Voyage Endpoints
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1288
labels: []
explicit_links: []
---
# Issue #1288: Feat/Prp-1896/Use New Vessel Voyage Endpoints

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1288  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [5757dd42daaa...1232256a7338](https://github.com/teqplay/portreporter-backend/compare/5757dd42daaa...1232256a7338)
**Merge commit:** [1232256a7338](https://github.com/teqplay/portreporter-backend/commit/1232256a7338)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Leon Joosse, Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop
**Source Branch:** [feat/PRP-1896/use_new_vessel_voyage_endpoints](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1896/use_new_vessel_voyage_endpoints)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-06-14T08:24:20.790733+00:00
**Status:** MERGED

Hi there,
This change consist on:
1. **\[Core content from line** [**83**](https://github.com/teqplay/portreporter-backend/issues/654#Lsrc/main/kotlin/nl/teqplay/portreporter/logic/external/VesselVoyageLogic.ktT83) **to 160\]** New logic to combine Visits and Voyages from VesselVoyage into the VesselVoyageVisit object, using the new VesselVoyage endpoints. I tried to follow the 5-lines of code paradigm for easy reading
2. Adding the missing mirror classes from VesselVoyage and amending existing ones \(under `src/main/kotlin/nl/teqplay/portreporter/model/internal/vesselvoyage`\)
3. Marking as deprecated the logic to be replaced \(in case it’s still in place in the FE\).
4. Renaming some classes aliases in VesselVoyageLogic \(so the external VesselVoyage models will be called **V2**\*\).

