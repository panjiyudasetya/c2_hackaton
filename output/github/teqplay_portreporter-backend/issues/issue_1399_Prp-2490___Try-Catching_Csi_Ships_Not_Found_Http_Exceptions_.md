---
id: github:teqplay/portreporter-backend:issue:1399
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1399
title: 'Prp-2490 : Try-Catching Csi Ships Not Found Http Exceptions And Returning
  Null. Adding A Schduled Report In Slack Of These Missing Ships Detected By Portreporter.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1399
labels: []
explicit_links: []
---
# Issue #1399: Prp-2490 : Try-Catching Csi Ships Not Found Http Exceptions And Returning Null. Adding A Schduled Report In Slack Of These Missing Ships Detected By Portreporter.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1399  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e6f800eae5aa...10fc8b3c0d8a](https://github.com/teqplay/portreporter-backend/compare/e6f800eae5aa...10fc8b3c0d8a)
**Merge commit:** [10fc8b3c0d8a](https://github.com/teqplay/portreporter-backend/commit/10fc8b3c0d8a)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Leon Joosse
**Approvers:** Joost Laurman, Leon Joosse
**Source Branch:** [feat/PRP-2490/handle_missing_ship_in_csi](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2490/handle_missing_ship_in_csi)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-10-24T12:30:54.913769+00:00
**Status:** MERGED

Don’t be scared of the amount of files. The relevant changes are in the following points 1,2 and 3:
1. **New _by-passed_ CSI Client** \(`CsiShipClient.kt`\) that extends the skeleton one, overrides `getShipRegisterByIMO` and `getShipRegisterByMMSI`.  
  They try-catch their respective super methods for **NotFoundExceptions** \(in two _flavours_\), reporting when catching, the missing ship and returning null .
2. **New module MissingCsiShip**, consisting of:
    1. **Datasource:** `MissingCsiShipDataSource.kt`
    2. **Logic:** `MissingCsiShipLogic.kt`
    
        1. A configurable scheduled task to report in Slack on a regular bases the reporter missing ships in CSI.
        2. A method to report a missing ship in CSI \(used in point 1\).
        
    3. **Model:** `MissingCsiShip.kt` and enum for the ship type `ShipIdType.kt`.
    
3. **UnitTests** for the newly introduced CsiShipClient and MissingCsiShipLogic:
    1. `CsiShipClientTest.kt`
    2. `MissingCsiShipLogicTest.kt`
    
4. **Rest of files** is the **import replacement** of the CsiShipClient.

