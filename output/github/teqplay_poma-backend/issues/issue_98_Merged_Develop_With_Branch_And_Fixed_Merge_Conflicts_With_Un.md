---
id: github:teqplay/poma-backend:issue:98
source: github
type: issue
repo: teqplay/poma-backend
number: 98
title: Merged Develop With Branch And Fixed Merge Conflicts With Unit Tests. First
  Version Of Triggers For Setting Main Port Of Berths And Terminals.
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/98
labels: []
explicit_links: []
---
# Issue #98: Merged Develop With Branch And Fixed Merge Conflicts With Unit Tests. First Version Of Triggers For Setting Main Port Of Berths And Terminals.

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/98  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [5e66be4869ca...083c8cd4db10](https://github.com/teqplay/poma-backend/compare/5e66be4869ca...083c8cd4db10)
**Merge commit:** [083c8cd4db10](https://github.com/teqplay/poma-backend/commit/083c8cd4db10)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Wouter Naloop
**Source Branch:** [feature/PRP-2254_determine_main_port_for_berths_and_terminals](https://github.com/teqplay/poma-backend/tree/feature/PRP-2254_determine_main_port_for_berths_and_terminals)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2023-10-12T07:41:00.035369+00:00
**Status:** MERGED

Had some troubles with the unit tests running into errors after merging develop onto branch. I think I started from a branch of master as I was getting a lot of conflicts and like application.properties wasn’t present anymore making me miss the application context.  
I shouldn’t be deleting anything from the develop as I should only be adding so it should be good to go now.

