---
id: github:teqplay/portreporter-backend:issue:1382
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1382
title: 'Cherrypick For Of Prp-2432: Create Admin Patch Portcall Endpoint (Pull Request
  #760)'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1382
labels: []
explicit_links: []
---
# Issue #1382: Cherrypick For Of Prp-2432: Create Admin Patch Portcall Endpoint (Pull Request #760)

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1382  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [4babaffcff15...ac255f96d24e](https://github.com/teqplay/portreporter-backend/compare/4babaffcff15...ac255f96d24e)
**Merge commit:** [ac255f96d24e](https://github.com/teqplay/portreporter-backend/commit/ac255f96d24e)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Leon Joosse, Gavin den Hollander
**Approvers:** Leon Joosse
**Source Branch:** [feat/PRP-2432/cherrypick/patch_portcall_fields](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2432/cherrypick/patch_portcall_fields)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-08-22T13:38:30.838794+00:00
**Status:** MERGED

PR of a master-forked branch where the commit 3fa338bbadc5dddc15d3852c81cd6ae900c37e3c of the PR for the feature.
---
Create admin patch portcall endpoint
* PRP-2413, PRP-2432 : Enabling portcall patch endpoint for admins to update agent, startTime, endTime and portATA.
* PRP-2413, PRP-2432 : Setting only PATCH as a valid endpoint's method.
* PRP-2413, PRP-2432 : send slack message when new agent is not a valid one.
* PRP-2413, PRP-2432 : logging full change for traceability.
* PRP-2413, PRP-2432 : change endpoint kdoc description.
Approved-by: Gavin den Hollander

