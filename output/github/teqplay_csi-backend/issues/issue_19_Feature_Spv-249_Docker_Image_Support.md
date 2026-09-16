---
id: github:teqplay/csi-backend:issue:19
source: github
type: issue
repo: teqplay/csi-backend
number: 19
title: Feature/Spv-249 Docker Image Support
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/19
labels: []
explicit_links: []
---
# Issue #19: Feature/Spv-249 Docker Image Support

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/19  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [6a4b2595a81e...2d1f174b463e](https://github.com/teqplay/csi-backend/compare/6a4b2595a81e...2d1f174b463e)
**Merge commit:** [2d1f174b463e](https://github.com/teqplay/csi-backend/commit/2d1f174b463e)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feature/SPV-249_docker_image_support](https://github.com/teqplay/csi-backend/tree/feature/SPV-249_docker_image_support)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2021-10-20T13:01:59.157357+00:00
**Status:** MERGED

* Added support for jib to create a docker image
* Fixed entry point of docker container to be the Application class of csi
* Changed the dependencies to be v3, so it also gets back the set S3 config
* Set source compatibility to 11, so tests don't complain
* Attempt to fix an issue where the image name is not lowercase
* Attempt to fix statup problem of docker image
* Removed the log4j library from keycloak
* Updated skeleton to resolve the issue with multiple log4j libraries


