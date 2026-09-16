---
id: github:teqplay/vesselvoyage-backend:pr:517
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 517
title: Release 28 May 2025
author: Darius-Wattimena
state: closed
date: '2025-05-28'
merged_at: '2025-05-28'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/517
labels: []
linked_issues: []
explicit_links: []
---
# PR #517: Release 28 May 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/517  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-05-28  
**Merged:** 2025-05-28  

## Description

_No description._

## Commits

- `cf7fbfa0` **TeqJoostD** (2025-05-13): fix: create fix for terminal mooring area not taking absolute duration
- `28cf7689` **leonj** (2025-05-15): Move PtoStatementOfFactsView to its own sub package, to later add another subpackage for PortReporterStatementOfFactsView
  Move all internal SOF info objects for PTO to their own subpackage, as we'll duplicate them later on for PortReporter in another subpackage
- `5d8f5f52` **leonj** (2025-05-15): Add DTO objects to collect info to build the PortReporterStatementOfFactsView
- `dcb4f203` **leonj** (2025-05-15): Add PortReporterStatementOfFactsView
- `cfa8d457` **leonj** (2025-05-15): Add PortReporterStatementOfFactsViewGenerator. Add test. Separate test helper functions for PTO and PortReporter SOF view
- `2d68b059` **leonj** (2025-05-15): Fix PtoStatementOfFactsMapperTest
- `d7c15446` **leonj** (2025-05-15): Enhance documentation on PortReporterStatementOfFactsView and its underlying models
- `223a8083` **leonj** (2025-05-16): Add documentation for VesselVoyageClient
- `f6cd18a0` **leonj** (2025-05-16): Do not expose ShipDetails model (which is internal to VV), instead use the Ship model
- `b98430d1` **Leon Joosse** (2025-05-19): Merge pull request #501 from teqplay/SPV-2616-sof-view-prepare-for-portreporter
  SPV-2616: better package separation for PTO and PRP StatementOfFactsView
- `af2f31bb` **Leon Joosse** (2025-05-19): Merge branch 'develop' into SPV-2616-portreporter-sof-view
- `1fe4ab47` **leonj** (2025-05-19): Merge branch 'SPV-2616-portreporter-sof-view' into SPV-2617-portreporter-sof-view-api-and-client
- `6b431f79` **Darius Wattimena** (2025-05-19): Added an endpoint to see the automatic recalculation status per ship category
- `5a67fed2` **Darius Wattimena** (2025-05-19): Code cleanup
- `c603f8f1` **leonj** (2025-05-19): Extend API with portreporter SOF
- `de1666c7` **leonj** (2025-05-19): Generalize produce methods for SOF views. Change BaseApiV2Controller to better accommodate mapping the result.
- `a963fd09` **leonj** (2025-05-19): For now, only publish PTO SOF. Publishing the portreporter SOF via rabbitmq will be addressed later in a separate PR, as it includes a breaking change.
- `bc508345` **Leon Joosse** (2025-05-19): Merge pull request #502 from teqplay/SPV-2616-portreporter-sof-view
  SPV-2616 PortReporter StatementOfFacts view + generator
- `da8692ca` **Leon Joosse** (2025-05-19): Merge branch 'develop' into SPV-2617-portreporter-sof-view-api-and-client
- `9c562f65` **Darius Wattimena** (2025-05-20): Merge pull request #506 from teqplay/explain-recalc-ship-types
  Automatic recalculation more stats
- `839e6638` **Joost Dambrink** (2025-05-20): Merge pull request #497 from teqplay/SPV-2581
  SPV-2581: Create fix for terminal mooring area not taking absolute duration
- `d1b0a918` **Leon Joosse** (2025-05-20): Merge branch 'develop' into SPV-2617-portreporter-sof-view-api-and-client
- `a0e89fcf` **leonj** (2025-05-20): Extend StatementOfFacts in the VesselVoyageClient, allowing to retrieve SOFs by imo and port, including batch calls
- `13a9e341` **leonj** (2025-05-21): Add methods to retrieve multiple traces by entry ids
- `ea7fa81f` **leonj** (2025-05-21): Move Trace endpoints from the PROCESSING to API, so it can be returned through the api, and used by the client
- `da708bdf` **Leon Joosse** (2025-05-22): Fix wrong parameter type ByPortRequest, should be ByImoRequest
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `a777715e` **leonj** (2025-05-22): Add endpoint to look up SOFs around a timestamp, and a positive/negative limit to return items after/before the timestamp respectively
- `fec8d6e6` **leonj** (2025-05-22): Fix query
- `c19b1e2c` **Leon Joosse** (2025-05-22): Fix required timestamp and limit
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `625fd78b` **Leon Joosse** (2025-05-22): Update docs
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `6dc0c417` **Leon Joosse** (2025-05-22): Merge pull request #507 from teqplay/SPV-2617-portreporter-sof-view-api-and-client
  SPV-2617 Support PortReporter SOF view for API and vesselvoyageclient
- `2ece9f83` **Leon Joosse** (2025-05-22): Merge pull request #508 from teqplay/SPV-2617-portreporter-sof-view-extend-sof-client-methods
  SPV-2617: Extend StatementOfFacts in the VesselVoyageClient, allowing to retrieve SOFs by imo and port, including batch calls
- `fdbcb57b` **leonj** (2025-05-22): Add test
- `22a3d3dd` **Leon Joosse** (2025-05-23): Merge pull request #509 from teqplay/SPV-2619-trace-api-and-client
  SPV-2619: Trace api and client
- `e7aecb7b` **leonj** (2025-05-23): Remove commented code from a test, remove qualifier for mock function
- `5e9c42ff` **leonj** (2025-05-23): Send slack message when a @Scheduled task fails. This only happens when the processing profile is enabled (because the SlackMessageService is only available under the processing profile
- `bd1b9c59` **Leon Joosse** (2025-05-23): Merge pull request #511 from teqplay/SPV-2645-sof-endpoint-lookaround
  SPV-2645 Add endpoint to look up SOFs around a timestamp
- `97233548` **leonj** (2025-05-26): Add traces variable to access it via the client
- `5fa80358` **Leon Joosse** (2025-05-26): Merge pull request #513 from teqplay/TCC-133-fixclient
  TCC-133: Add traces variable to access it via the client
- `f8f2642a` **Leon Joosse** (2025-05-26): Merge pull request #512 from teqplay/TCC-99-notify-on-failing-scheduled-tasks
  TCC-99: Send slack message when a @Scheduled task fails
- `1a3ae708` **Darius Wattimena** (2025-05-26): Add id field to all classes exposed to PTO
- `22b04b09` **Darius Wattimena** (2025-05-26): Adjusted test that wasn't adjusted
- `d443e557` **Darius Wattimena** (2025-05-26): Deprecated ref fields and added missing replacement fields
- `f653c908` **Darius Wattimena** (2025-05-27): ktlint
- `23ad5231` **Darius Wattimena** (2025-05-27): Deprecated ref field in berth visit and updated places where we used this ref with the id field
- `629dbe33` **Darius Wattimena** (2025-05-27): Merge pull request #515 from teqplay/TCC-162-pto-sof-ids
  TCC-162 pto sof ids
- `29d495c5` **Jamie de Leest** (2025-05-27): feat: add atlas actuator endpoint
- `f3228539` **jamie-teqplay** (2025-05-27): Merge pull request #516 from teqplay/DEV-872-deploy-vesselvoyage-with-actuator-endpoint
  DEV-872 add atlas actuator endpoint
- `83273474` **Darius Wattimena** (2025-05-28): Fix an issue where we didn't select the correct id
- `a89397a1` **Darius Wattimena** (2025-05-28): Merge pull request #518 from teqplay/TCC-162-fix
  TCC-162 Fix wrong id PTO SOF
