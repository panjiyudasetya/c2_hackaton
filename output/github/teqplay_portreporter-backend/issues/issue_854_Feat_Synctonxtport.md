---
id: github:teqplay/portreporter-backend:issue:854
source: github
type: issue
repo: teqplay/portreporter-backend
number: 854
title: Feat/Synctonxtport
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/854
labels: []
explicit_links: []
---
# Issue #854: Feat/Synctonxtport

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/854  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4e2b5d7ce9c6...ee11b23762a7](https://github.com/teqplay/portreporter-backend/compare/4e2b5d7ce9c6...ee11b23762a7)
**Merge commit:** [ee11b23762a7](https://github.com/teqplay/portreporter-backend/commit/ee11b23762a7)
**Author:** Shravan Shetty
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feat/syncToNxtPort](https://github.com/teqplay/portreporter-backend/tree/feat/syncToNxtPort)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:40.952146+00:00
**Status:** MERGED

* moved all company related logics/services to separate package
* removed rootLogic moved to userProfileLogic. Moved exact logic to 'external' package
* moved all reporting: communication, subscription, notification, daily ship reporting logics to separate package
* moved all portcall related logic to separate package
* moved all company and reporting controllers to separate packages
* moved portcall related controllers to separate packages
* update: added nxtport ingestion endpoint. some cleanup of multiple authToken/credentials models


