---
id: github:teqplay/portreporter-backend:issue:1373
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1373
title: Develop > Master
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1373
labels: []
explicit_links: []
---
# Issue #1373: Develop > Master

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1373  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [e19dc46a288e...0a2537dc94a5](https://github.com/teqplay/portreporter-backend/compare/e19dc46a288e...0a2537dc94a5)
**Merge commit:** [0a2537dc94a5](https://github.com/teqplay/portreporter-backend/commit/0a2537dc94a5)
**Author:** Shan Minh Nguyen
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-07-10T09:07:13.472614+00:00
**Status:** MERGED

* Updated version to snapshots.
* Removing kmongo
* fixed multiple instances of mongo beans
* Merged in feat/PRP-2397/smartfleet\_event\_pilotboardingplace\_3h\_before\_happening \(pull request #754\)
    PRP-2397 : SmartFleet PilotBoardingPlace's scheduled notification.

    * PRP-2397 : SmartFleet PilotBoardingPlace's scheduled notification.
    * PRP-2397 : adapt unitTests to new functionality.
    * PRP-2397 : Adding logs and calling action and postAction and call them properly.
    * PRP-2397 : executeIn getting its correct value. Set some safety margins when scheduling. Setting a SmartFleet prefix to sheculedTask to avoid key collisions in the scheduler's map. Improving logs.
    * PRP-2397 : remove some logs.
    * PRP-2397 : Including the unlocode to the uniqueness of the SmartFleetScheduledTaskDetails.
    * PRP-2397 : Change wording of SmartFleet ETA -3h PilotBorardingPlace message notification.
    * PRP-2397 : adapt unitTest for the new message wording.
    
    Approved-by: Joost Laurman

* Removing kmongo out of the new SmartFleetScheduledTaskDetailsDataSource

