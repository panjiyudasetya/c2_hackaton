---
id: github:teqplay/portreporter-backend:issue:1365
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1365
title: Remove Calls Into Platform To Get Portcalls
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1365
labels: []
explicit_links: []
---
# Issue #1365: Remove Calls Into Platform To Get Portcalls

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1365  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [76089b38b1f2...6c5e0f6d3d0f](https://github.com/teqplay/portreporter-backend/compare/76089b38b1f2...6c5e0f6d3d0f)
**Merge commit:** [6c5e0f6d3d0f](https://github.com/teqplay/portreporter-backend/commit/6c5e0f6d3d0f)
**Author:** Michel Wilson
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [remove-platform-portcall-call](https://github.com/teqplay/portreporter-backend/tree/remove-platform-portcall-call)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-03-19T15:37:20.137190+00:00
**Status:** MERGED

This PR removes all calls into platform to get portcalls, because we no longer want to support this in platform. This prepares the way ahead for pointint PortReporter to backend\(dev\) instead of to backendpronto\(dev\).

