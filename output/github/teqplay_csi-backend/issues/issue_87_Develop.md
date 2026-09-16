---
id: github:teqplay/csi-backend:issue:87
source: github
type: issue
repo: teqplay/csi-backend
number: 87
title: Develop
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/87
labels: []
explicit_links: []
---
# Issue #87: Develop

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/87  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [08e6242b2dbd...f74aba5a572c](https://github.com/teqplay/csi-backend/compare/08e6242b2dbd...f74aba5a572c)
**Merge commit:** [f74aba5a572c](https://github.com/teqplay/csi-backend/commit/f74aba5a572c)
**Author:** Pim van den Toorn
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/csi-backend/tree/master)
**Closed On:** 2024-12-16T13:39:51.158217+00:00
**Status:** MERGED

* Added checking for differences
* Added recursive to fun name propertyDifferences for clarity
* Changed comparing the objects to comparing JSON
* WIP: Added a ShipAllData object for comparing and grouping by ship, started the integration of the other collections in SyncService and made a difference checking function
* Fixed rest template timeout
* Changed difference checking from all at once in big objects to checking per collection and remade the ShipAllData into an object that holds all differences grouped by ship
* Added syncing of other collections by replacing the full collections, added syncedAt to ShipRegisterInfo and ShipRegisterMapping, added ignored fields for differences
* Jackson setting only send non-null fields
* Scheduled syncing
* getExternal back to inline fun, get all ids/imos with no shipRegister changes to sets with buildSet, Rest Template timeout to val, removed all RawImoMapping syncing functions
* Added ship name to ShipAllChanges, also search ships from all ids and imos and build the main ShipAllData list from that
* Synchronize now run async \(diff threads\), changed syncedAt to an Instant
* Added not equals check between local and external model, faster than going through all \(sub\)properties per model
* CC-113 counting tickets by distinct imo
* added some logging
* Memory from 3Gi to 4Gi

