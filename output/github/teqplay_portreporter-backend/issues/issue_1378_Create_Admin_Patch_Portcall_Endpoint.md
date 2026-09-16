---
id: github:teqplay/portreporter-backend:issue:1378
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1378
title: Create Admin Patch Portcall Endpoint
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1378
labels: []
explicit_links: []
---
# Issue #1378: Create Admin Patch Portcall Endpoint

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1378  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [cc41f45d6a58...3fa338bbadc5](https://github.com/teqplay/portreporter-backend/compare/cc41f45d6a58...3fa338bbadc5)
**Merge commit:** [3fa338bbadc5](https://github.com/teqplay/portreporter-backend/commit/3fa338bbadc5)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Gavin den Hollander
**Approvers:** Gavin den Hollander
**Source Branch:** [feat/PRP-2413/PRP-2432/create_admin_patch_portcall_endpoint](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2413/PRP-2432/create_admin_patch_portcall_endpoint)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-05T10:22:57.324614+00:00
**Status:** MERGED

Enabling portcall patch endpoint for admins to update `agent`, `startTime`, `endTime` and `portATA`.
It also sends slack messages when:
* portATA changed \(as it creates a data discrepancy with the portATA event\)
* agent is changed, and the new one doesn’t exist as an agency.

