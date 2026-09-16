---
id: github:teqplay/portreporter-backend:issue:1355
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1355
title: Release Candidate V5.29.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1355
labels: []
explicit_links:
- jira:PRP-2274
---
# Issue #1355: Release Candidate V5.29.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1355  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [6d0504773e4f...39b01e1439a8](https://github.com/teqplay/portreporter-backend/compare/6d0504773e4f...39b01e1439a8)
**Merge commit:** [39b01e1439a8](https://github.com/teqplay/portreporter-backend/commit/39b01e1439a8)
**Author:** Shan Minh Nguyen
**Reviewers:** 
**Approvers:** 
**Source Branch:** [feature/release_candidate_v5.29.0](https://github.com/teqplay/portreporter-backend/tree/feature/release_candidate_v5.29.0)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-01-08T11:44:37.587731+00:00
**Status:** MERGED

* Removed nortendering packages and config
* Merged in feature/PRP-2274\_extend\_health\_actuator\_setup \(pull request #707\)
    Feature/PRP-2274 extend health actuator setup

    * Setup health actuator checks and error handling for several services.
    * Removed some secrets and properties
    * Changed file names and status of external service connections when fetch
    * Merged develop into feature/PRP-2274\_extend\_health\_actuator\_setup
    * Reworked some code from feedback.
    * Fixed conflicts for merging develop onto branch.
    
    Approved-by: Darius Wattimena

* Changed Helm installation to different namespace
* Added two CSI caches based on imos and mmsis in shiplogic to reduce some duplicate calls being made right now with a configurable cache timer.
* Updated the nomination cron task to also check for updates and report this back.
* Enabled caffeine cache on shiplogic csi calls.
* Added threading during init and fixed a bug in the startAllScheduledTasks
* Added logging at login to check for responsiveness endpoint request.
* Added vesselvoyage annotations for service health check.
* Added some VesselVoyage health service annotations and added defaults to config so that a developer doesn't send notifications by accident without having some identifications from the user sending in notifications

