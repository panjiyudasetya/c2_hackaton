---
id: github:teqplay/poma-backend:issue:144
source: github
type: issue
repo: teqplay/poma-backend
number: 144
title: Cc-2 Sync A To B Cc-3 Sync Per Port
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/144
labels: []
explicit_links: []
---
# Issue #144: Cc-2 Sync A To B Cc-3 Sync Per Port

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/144  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [188ecafb9d00...8bc17b418009](https://github.com/teqplay/poma-backend/compare/188ecafb9d00...8bc17b418009)
**Merge commit:** [8bc17b418009](https://github.com/teqplay/poma-backend/commit/8bc17b418009)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena, Joost Dambrink
**Approvers:** Joost Dambrink, Darius Wattimena, Pim van den Toorn
**Source Branch:** [CC-2-sync-A-to-B-CC-3-sync-per-port](https://github.com/teqplay/poma-backend/tree/CC-2-sync-A-to-B-CC-3-sync-per-port)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-08-26T15:38:36.323805+00:00
**Status:** MERGED

Created SyncService to sync from other instances, with ability to choose the source, sync specific infrastructure types like berth, sync everything and sync all models linked to a port or ports. Also moved the scheduled synchronization to the SyncService

* Added SyncService and -Controller with ability to synchronize from prod, dev or sandbox and the option to sync everything or a single infrastructure type
* Added synchronizePort\(s\), added PortInfraDataSource and -service as support,
* Added scheduled autoSync to SyncService and removed the scheduled syncing from all infra services
* Restored resolveTimeZone for Port
* Replaced autoMerge bool from InfrastructureService and replaced with try catch in SyncService, removed missed scheduled merge

