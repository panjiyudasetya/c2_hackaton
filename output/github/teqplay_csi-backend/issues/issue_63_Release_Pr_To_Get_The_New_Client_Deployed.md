---
id: github:teqplay/csi-backend:issue:63
source: github
type: issue
repo: teqplay/csi-backend
number: 63
title: Release Pr To Get The New Client Deployed
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/63
labels: []
explicit_links: []
---
# Issue #63: Release Pr To Get The New Client Deployed

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/63  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [612e6be493ad...421f784fe896](https://github.com/teqplay/csi-backend/compare/612e6be493ad...421f784fe896)
**Merge commit:** [421f784fe896](https://github.com/teqplay/csi-backend/commit/421f784fe896)
**Author:** Michel Wilson
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/csi-backend/tree/master)
**Closed On:** 2024-02-12T13:05:41.170346+00:00
**Status:** MERGED

* Merged in new\_namespace \(pull request #60\)
    Moved CSI to new namespace

    * Moved CSI to new namespace
    
    Approved-by: Maurice van Veen

* Adjust script so it doesn't break when merging to master
* Changed Helm installation to namespace core-service
* Enable prometheus for csi query and internal
* Add internal-api RestTemplate client
* review comments
* Also publish client

