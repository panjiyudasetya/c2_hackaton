---
id: github:teqplay/csi-backend:issue:48
source: github
type: issue
repo: teqplay/csi-backend
number: 48
title: On Update To Any Ship/Characteristics/Mapping, Publish Event
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/48
labels: []
explicit_links:
- jira:PRA-284
---
# Issue #48: On Update To Any Ship/Characteristics/Mapping, Publish Event

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/48  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [8a66c62f49f4...c01a5c2435a2](https://github.com/teqplay/csi-backend/compare/8a66c62f49f4...c01a5c2435a2)
**Merge commit:** [c01a5c2435a2](https://github.com/teqplay/csi-backend/commit/c01a5c2435a2)
**Author:** Former user
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Michel Wilson
**Source Branch:** [PRA-284/publish](https://github.com/teqplay/csi-backend/tree/PRA-284/publish)
**Destination Branch:** [CSI-HA-pre-release](https://github.com/teqplay/csi-backend/tree/CSI-HA-pre-release)
**Closed On:** 2023-03-03T10:09:32.160718+00:00
**Status:** MERGED

Whenever an update in the database takes place \(`.insert`, `.save`, etc.\), also publish an update to a stream.

