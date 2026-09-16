---
id: github:teqplay/portreporter-backend:issue:1420
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1420
title: Fix/Circle Ci Deploy Wait For Images
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1420
labels: []
explicit_links: []
---
# Issue #1420: Fix/Circle Ci Deploy Wait For Images

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1420  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [44a468ede8a1...64effd8b38fd](https://github.com/teqplay/portreporter-backend/compare/44a468ede8a1...64effd8b38fd)
**Merge commit:** [64effd8b38fd](https://github.com/teqplay/portreporter-backend/commit/64effd8b38fd)
**Author:** Joaquin Marquez Bugella
**Reviewers:** 
**Approvers:** 
**Source Branch:** [fix/circle_ci_deploy_wait_for_images](https://github.com/teqplay/portreporter-backend/tree/fix/circle_ci_deploy_wait_for_images)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2025-01-15T18:03:40.007837+00:00
**Status:** MERGED

* alter order of images for deploy so the primary image is jdk and will be loaded before aws \(according to the deploy order\).
* Removing custom docker images from deploy and adding a step in deploy\_to\_kubernetes to download and install the aws client.

