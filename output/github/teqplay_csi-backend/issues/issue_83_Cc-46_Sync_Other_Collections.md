---
id: github:teqplay/csi-backend:issue:83
source: github
type: issue
repo: teqplay/csi-backend
number: 83
title: Cc-46 Sync Other Collections
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/83
labels: []
explicit_links: []
---
# Issue #83: Cc-46 Sync Other Collections

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/83  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [a03d738fd8a8...b46b1dce1777](https://github.com/teqplay/csi-backend/compare/a03d738fd8a8...b46b1dce1777)
**Merge commit:** [b46b1dce1777](https://github.com/teqplay/csi-backend/commit/b46b1dce1777)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [CC-46-sync-other-collections](https://github.com/teqplay/csi-backend/tree/CC-46-sync-other-collections)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-12-02T17:36:09.512629+00:00
**Status:** MERGED

* WIP: Added a ShipAllData object for comparing and grouping by ship, started the integration of the other collections in SyncService and made a difference checking function
* Fixed rest template timeout
* Changed difference checking from all at once in big objects to checking per collection and remade the ShipAllData into an object that holds all differences grouped by ship
* Added syncing of other collections by replacing the full collections, added syncedAt to ShipRegisterInfo and ShipRegisterMapping, added ignored fields for differences
* Jackson setting only send non-null fields

