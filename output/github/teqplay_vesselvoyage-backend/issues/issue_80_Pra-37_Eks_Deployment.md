---
id: github:teqplay/vesselvoyage-backend:issue:80
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 80
title: Pra-37 Eks Deployment
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/80
labels: []
explicit_links: []
---
# Issue #80: Pra-37 Eks Deployment

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/80  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [ee9929f9dbb7...c32213a56568](https://github.com/teqplay/vesselvoyage-backend/compare/ee9929f9dbb7...c32213a56568)
**Merge commit:** [c32213a56568](https://github.com/teqplay/vesselvoyage-backend/commit/c32213a56568)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [PRA-37_eks_deployment](https://github.com/teqplay/vesselvoyage-backend/tree/PRA-37_eks_deployment)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-07-07T09:04:28.159825+00:00
**Status:** MERGED

* Did first steps to make VesselVoyage EKS ready
* ktlint format
* Added helm value files and updated cirlcleci script
* Added needed gradle tasks to publish to ECR
* Removed all old Elastic Beanstalk configuration
* Added setting the version
* Add support for gracefully terminating on EKS by giving it 2 minutes
* Updated default Kubernetes resources needed for VesselVoyage


