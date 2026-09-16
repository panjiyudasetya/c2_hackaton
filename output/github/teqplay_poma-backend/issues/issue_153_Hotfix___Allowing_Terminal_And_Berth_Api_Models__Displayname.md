---
id: github:teqplay/poma-backend:issue:153
source: github
type: issue
repo: teqplay/poma-backend
number: 153
title: 'Hotfix : Allowing Terminal And Berth Api Models'' Displayname Field Nullable.'
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/153
labels: []
explicit_links: []
---
# Issue #153: Hotfix : Allowing Terminal And Berth Api Models' Displayname Field Nullable.

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/153  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [cf407b2d7120...05d105cda056](https://github.com/teqplay/poma-backend/compare/cf407b2d7120...05d105cda056)
**Merge commit:** [05d105cda056](https://github.com/teqplay/poma-backend/commit/05d105cda056)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Dambrink
**Approvers:** Joost Dambrink
**Source Branch:** [hotfix/allow_terminal_and_berth_api_models_displayName_to_be_nullable](https://github.com/teqplay/poma-backend/tree/hotfix/allow_terminal_and_berth_api_models_displayName_to_be_nullable)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2024-09-03T12:27:35.165558+00:00
**Status:** MERGED

A hotfix to allow the FE to update Terminals and Berths without breaking for the lack of `displayName`.
It should be temporal until FE adapts to provides it.

