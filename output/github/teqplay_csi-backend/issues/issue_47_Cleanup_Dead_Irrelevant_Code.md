---
id: github:teqplay/csi-backend:issue:47
source: github
type: issue
repo: teqplay/csi-backend
number: 47
title: Cleanup Dead/Irrelevant Code
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/47
labels: []
explicit_links:
- jira:PRA-284
---
# Issue #47: Cleanup Dead/Irrelevant Code

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/47  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [77065fedee22...8a66c62f49f4](https://github.com/teqplay/csi-backend/compare/77065fedee22...8a66c62f49f4)
**Merge commit:** [8a66c62f49f4](https://github.com/teqplay/csi-backend/commit/8a66c62f49f4)
**Author:** Former user
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Michel Wilson
**Source Branch:** [PRA-284/cleanup](https://github.com/teqplay/csi-backend/tree/PRA-284/cleanup)
**Destination Branch:** [CSI-HA-pre-release](https://github.com/teqplay/csi-backend/tree/CSI-HA-pre-release)
**Closed On:** 2023-03-03T09:36:29.365041+00:00
**Status:** MERGED

This PR removes dead code, like `ImportService` and `ImportController`, which were only used once for the transition to CSI mid-2019.
It also removes irrelevant/dangerous code for `createMany`, which only was used for importing, and `delete`. Instead of deleting data, keep the data and mark as deleted \(or as ghost ship, both of which are already supported\). This will also help in the future, with CSI having a more stable identifier.

