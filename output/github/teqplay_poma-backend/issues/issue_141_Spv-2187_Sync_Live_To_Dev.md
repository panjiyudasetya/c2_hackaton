---
id: github:teqplay/poma-backend:issue:141
source: github
type: issue
repo: teqplay/poma-backend
number: 141
title: Spv-2187 Sync Live To Dev
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/141
labels: []
explicit_links: []
---
# Issue #141: Spv-2187 Sync Live To Dev

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/141  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [1f6b85525868...67009aca9941](https://github.com/teqplay/poma-backend/compare/1f6b85525868...67009aca9941)
**Merge commit:** [67009aca9941](https://github.com/teqplay/poma-backend/commit/67009aca9941)
**Author:** Pim van den Toorn
**Reviewers:** Wouter Naloop, Joost Dambrink
**Approvers:** Joost Dambrink, Wouter Naloop
**Source Branch:** [SPV-2187-sync-live-to-dev](https://github.com/teqplay/poma-backend/tree/SPV-2187-sync-live-to-dev)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-08-05T09:33:57.215822+00:00
**Status:** MERGED

Added a syncing mechanism for dev, so that weekly de database gets replaced by the prod version

* Added liveSyncRestTemplate, added synchronize to the InfrastructureService and -controller, added scheduled to all infrastructures
* Added mock for RestTemplate in tests
* Moved the liveSyncRestTemplate to the body of InfrastructureService
* Only gets and syncs the Teqplay db, then call mergeDatabases to update the merged db,
* Added mergeWOPCron to live sync and removed merge after sync from terminal and berth, due to incompatibility, also added replaceCollection to DataSource for a safe and total replacement

