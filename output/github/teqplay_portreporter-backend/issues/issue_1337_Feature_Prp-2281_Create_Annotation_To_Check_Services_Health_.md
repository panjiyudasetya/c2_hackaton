---
id: github:teqplay/portreporter-backend:issue:1337
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1337
title: Feature/Prp-2281 Create Annotation To Check Services Health Before Handling
  Endpoint
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1337
labels: []
explicit_links: []
---
# Issue #1337: Feature/Prp-2281 Create Annotation To Check Services Health Before Handling Endpoint

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1337  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ab8789fdab6e...366f434803ec](https://github.com/teqplay/portreporter-backend/compare/ab8789fdab6e...366f434803ec)
**Merge commit:** [366f434803ec](https://github.com/teqplay/portreporter-backend/commit/366f434803ec)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Darius Wattimena, Joaquin Marquez Bugella
**Approvers:** Wouter Naloop, Shan Minh Nguyen
**Source Branch:** [feature/PRP-2281_create_annotation_to_check_services_health_before_handling_endpoint](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2281_create_annotation_to_check_services_health_before_handling_endpoint)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-11-23T12:42:29.920121+00:00
**Status:** MERGED

* Setup health actuator checks and error handling for several services.
* KTLint commit of shame.
* Removed some secrets and properties
* Changed file names and status of external service connections when fetch
* Added a in memory mapping of endpoints and it's latest status related to endpoints with the specific health services annotations.

