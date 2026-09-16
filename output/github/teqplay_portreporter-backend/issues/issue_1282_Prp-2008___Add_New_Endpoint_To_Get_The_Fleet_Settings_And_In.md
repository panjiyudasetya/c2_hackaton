---
id: github:teqplay/portreporter-backend:issue:1282
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1282
title: 'Prp-2008 : Add New Endpoint To Get The Fleet Settings And Internally Rename
  Getfleet To Getfleetvoyages For Consistency.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1282
labels: []
explicit_links: []
---
# Issue #1282: Prp-2008 : Add New Endpoint To Get The Fleet Settings And Internally Rename Getfleet To Getfleetvoyages For Consistency.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1282  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [bea6dd74cf04...9456336c60f8](https://github.com/teqplay/portreporter-backend/compare/bea6dd74cf04...9456336c60f8)
**Merge commit:** [9456336c60f8](https://github.com/teqplay/portreporter-backend/commit/9456336c60f8)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [feat/PRP-2008/add_optional_flag_to_get_only_SFfleet_settings](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-2008/add_optional_flag_to_get_only_SFfleet_settings)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-05-31T15:26:19.146633+00:00
**Status:** MERGED

This PR consists in two things:
1. The core is just exposing a new endpoint to retrieve the `SFFleet` by its `id` \(only the fleet settings\) from SmartFleet.
2. The second \(and less important\) is naming things as they should:
    * the old method `getFleet(...): FleetVoyages` to `getFleetVoyages(...): SFFleetVoyages`
    * the new method to be called as it should `getFleet(...): SFFleet`
    

