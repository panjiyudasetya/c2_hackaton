---
id: github:teqplay/portreporter-backend:issue:1305
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1305
title: Fix/Prp-2109/Fix Impersonation In Method Getuserprofiles Controller
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1305
labels: []
explicit_links: []
---
# Issue #1305: Fix/Prp-2109/Fix Impersonation In Method Getuserprofiles Controller

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1305  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [f5d795ae560b...d1f8c3ca9838](https://github.com/teqplay/portreporter-backend/compare/f5d795ae560b...d1f8c3ca9838)
**Merge commit:** [d1f8c3ca9838](https://github.com/teqplay/portreporter-backend/commit/d1f8c3ca9838)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Leon Joosse, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [fix/PRP-2109/fix_impersonation_in_method_getUserProfiles_controller](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-2109/fix_impersonation_in_method_getUserProfiles_controller)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-07-04T14:03:18.211675+00:00
**Status:** MERGED

This pull request address the creation of personal fleets for smartfleet users by Teqplay admins or SmartFleet admins by:
* PRP-2109 : Fix impersonation in GET /v1/userProfile \(and add it to GET /v1/userProfile/current\).
* PRP-2109 : allow Teqplay admins and SmartFleet admins to create fleets for them.

