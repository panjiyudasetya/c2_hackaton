---
id: github:teqplay/csi-backend:issue:45
source: github
type: issue
repo: teqplay/csi-backend
number: 45
title: Csi Ha Init
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/45
labels: []
explicit_links:
- jira:PRA-324
---
# Issue #45: Csi Ha Init

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/45  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [b1e8abec6e96...f52316f6b499](https://github.com/teqplay/csi-backend/compare/b1e8abec6e96...f52316f6b499)
**Merge commit:** [f52316f6b499](https://github.com/teqplay/csi-backend/commit/f52316f6b499)
**Author:** Former user
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Michel Wilson
**Source Branch:** [PRA-324-HA](https://github.com/teqplay/csi-backend/tree/PRA-324-HA)
**Destination Branch:** [CSI-HA-pre-release](https://github.com/teqplay/csi-backend/tree/CSI-HA-pre-release)
**Closed On:** 2023-03-03T09:09:09.303385+00:00
**Status:** MERGED

Summary of changes:

* upgraded gradle wrapper
* upgraded skeleton-plugins
* updated CircleCI config to use the new multi-project setup
* using gradle convention plugins \(can be found in `buildSrc`, contains `api`, `lib` and `app` conventions for CSI\)
* move common logic into `:lib:utils`
* split CSI into three:

    * `:app:base`, contains the base app logic for CSI
    * `:app:query`, uses `:app:base`, only implements some interfaces to resolve where data comes from, where it’s stored and how it’s updated
    * `:app:internal`, uses `:app:base`, implements the same interfaces as above, and:
    
        * added specific endpoints only for internal use; like tickets
        * add “extension” endpoints, which contain CRUD functionality for the basic endpoints exposed by `:app:base`
        
    


