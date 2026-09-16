---
id: github:teqplay/csi-backend:issue:20
source: github
type: issue
repo: teqplay/csi-backend
number: 20
title: Spv-250 Kubernetes
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/20
labels: []
explicit_links: []
---
# Issue #20: Spv-250 Kubernetes

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/20  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [ca46bad540dc...8a109cf8bb20](https://github.com/teqplay/csi-backend/compare/ca46bad540dc...8a109cf8bb20)
**Merge commit:** [8a109cf8bb20](https://github.com/teqplay/csi-backend/commit/8a109cf8bb20)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [kubernetes](https://github.com/teqplay/csi-backend/tree/kubernetes)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2021-12-08T14:50:57.027494+00:00
**Status:** MERGED

* Started adding helm support to CSI
* Updated helm to be supporting every environment variable and add the java version to the prepared tags for jib in circleci
* Removed putting the version as tag as it doesn't seem to work properly
* Updated ConfigMap to be correct
* Added an okay way of managing config variables via configmaps
* got CSI working in kubernetes and started exposing it via a load balancer
* Tried getting ingress to work
* Last small updates for helm so it properly makes the needed resources in our kubernetes cluster
* Renamed the csi helm helper includes to be more generic and can easily be reused


