---
id: github:teqplay/portreporter-backend:issue:1332
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1332
title: Prp-2266 Removed Nortendering Packages And Config
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1332
labels: []
explicit_links:
- github:teqplay/portreporter-backend:issue:704
---
# Issue #1332: Prp-2266 Removed Nortendering Packages And Config

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1332  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [dfa2f39a0ae7...ab8789fdab6e](https://github.com/teqplay/portreporter-backend/compare/dfa2f39a0ae7...ab8789fdab6e)
**Merge commit:** [ab8789fdab6e](https://github.com/teqplay/portreporter-backend/commit/ab8789fdab6e)
**Author:** Shan Minh Nguyen
**Reviewers:** Wouter Naloop, Darius Wattimena, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/PRP-2266_removed_nortendering_packages](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2266_removed_nortendering_packages)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2023-11-20T15:30:07.100956+00:00
**Status:** MERGED

Only remarks are:
* TerminalLogic can be removed from the RestructureLogic constructor [\(here\)](https://github.com/teqplay/portreporter-backend/issues/704#comment-446163469).
* being coordinated with the FE so it doesn’t should error when calling the removed endpoints.

