---
id: github:teqplay/csi-backend:issue:40
source: github
type: issue
repo: teqplay/csi-backend
number: 40
title: Dev-98 Changed Ci Script To Always Take The Latest Changes From The Helm Values
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/40
labels: []
explicit_links: []
---
# Issue #40: Dev-98 Changed Ci Script To Always Take The Latest Changes From The Helm Values

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/40  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [b499d1041c16...5d12741dbfda](https://github.com/teqplay/csi-backend/compare/b499d1041c16...5d12741dbfda)
**Merge commit:** [5d12741dbfda](https://github.com/teqplay/csi-backend/commit/5d12741dbfda)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [DEV-98_EKS_resources](https://github.com/teqplay/csi-backend/tree/DEV-98_EKS_resources)
**Destination Branch:** [master](https://github.com/teqplay/csi-backend/tree/master)
**Closed On:** 2022-09-13T15:26:31.629656+00:00
**Status:** MERGED

Needed resources are specified in [https://docs.google.com/spreadsheets/d/17eIugacGRznKaH8wfuSCo9xE21ACMFG\_WmVvsfJVrNA/edit#gid=0](https://docs.google.com/spreadsheets/d/17eIugacGRznKaH8wfuSCo9xE21ACMFG_WmVvsfJVrNA/edit#gid=0)

Note: This change will affect all environments that will be deployed. Meaning that production will be changing its needed resources when merging this change to the master branch

