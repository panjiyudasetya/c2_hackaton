---
id: github:teqplay/portreporter-backend:issue:1310
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1310
title: 'Prp-1895 : Add Othership To Encounter Class.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1310
labels: []
explicit_links: []
---
# Issue #1310: Prp-1895 : Add Othership To Encounter Class.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1310  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [11f8850fa0e4...fa1b38b558af](https://github.com/teqplay/portreporter-backend/compare/11f8850fa0e4...fa1b38b558af)
**Merge commit:** [fa1b38b558af](https://github.com/teqplay/portreporter-backend/commit/fa1b38b558af)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/extend_vessel_voyage_encounter_class_with_ship_info](https://github.com/teqplay/portreporter-backend/tree/feat/extend_vessel_voyage_encounter_class_with_ship_info)
**Destination Branch:** [release/5.26.0](https://github.com/teqplay/portreporter-backend/tree/release/5.26.0)
**Closed On:** 2023-07-11T11:29:00.832912+00:00
**Status:** MERGED

The Encounter mirror model \(from VesselVoyage\) didn’t include the SFShip that SFEncounter had, and Damon expected it.

This PR:

1. extends the Encounter class with SFShip
2. uses same logic as SmartFleetLogic for getting the object
3. moves that logic to the ShipLogic so both, SmartFleetLogic and VesselVoyageLogic can access it, keeping things separated.
4. adapts \(doesn’t change\) SmartFleetUnitTest to mock the Ship get-methods according to the new logic location.


