---
id: github:teqplay/portreporter-backend:issue:1317
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1317
title: Prp-2180 Refactored Some Platform Ship Info Objects In Sf Endpoints To Retrieve
  Csi Static Ship Info As A Base With Platform For Dynamic Info.
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1317
labels: []
explicit_links: []
---
# Issue #1317: Prp-2180 Refactored Some Platform Ship Info Objects In Sf Endpoints To Retrieve Csi Static Ship Info As A Base With Platform For Dynamic Info.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1317  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [981e368f7b00...efb394d8f8bb](https://github.com/teqplay/portreporter-backend/compare/981e368f7b00...efb394d8f8bb)
**Merge commit:** [efb394d8f8bb](https://github.com/teqplay/portreporter-backend/commit/efb394d8f8bb)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Wouter Naloop
**Source Branch:** [feature/PRP-2180_refactor_platform_to_csi_part_2](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2180_refactor_platform_to_csi_part_2)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-07-31T10:08:31.024180+00:00
**Status:** MERGED

Updated endpoints where Platform’s static ship info is being called to be replaced partly by CSI static info.  
  
Update:  
After talk with Joaquin, will try to replace all static ship info from platform by CSI. So will continue to modify other endpoints of static ship info to static info from csi.

