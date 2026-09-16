---
id: github:teqplay/vesselvoyage-backend:issue:114
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 114
title: Spv-1246 Skeleton Request Logging
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/114
labels: []
explicit_links: []
---
# Issue #114: Spv-1246 Skeleton Request Logging

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/114  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [4d3242e4f26a...4927d58723da](https://github.com/teqplay/vesselvoyage-backend/compare/4d3242e4f26a...4927d58723da)
**Merge commit:** [4927d58723da](https://github.com/teqplay/vesselvoyage-backend/commit/4927d58723da)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson
**Approvers:** Michel Wilson
**Source Branch:** [SPV-1246_skeleton_request_logging](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1246_skeleton_request_logging)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-01-17T16:32:32.685748+00:00
**Status:** MERGED

* Updated skeleton to the latest version and made changes where needed
* Removed the project logback file, so it uses the skeleton one instead
* Added log file sidecar
* Updated a bunch of logging to debug
* Test out using the ContextClosedEvent instead of the @PreDestroy annotation
* ktlint
* Downgrade skeleton to see if it shutsdowns correctly in Kubernetes
* Revert skeleton version as it seems to be related to the log file sidecar not being terminated correctly

