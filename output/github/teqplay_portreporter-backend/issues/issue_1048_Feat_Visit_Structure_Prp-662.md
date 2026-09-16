---
id: github:teqplay/portreporter-backend:issue:1048
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1048
title: Feat/Visit Structure Prp-662
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1048
labels: []
explicit_links: []
---
# Issue #1048: Feat/Visit Structure Prp-662

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1048  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [848283876fe0...345574d2f87c](https://github.com/teqplay/portreporter-backend/compare/848283876fe0...345574d2f87c)
**Merge commit:** [345574d2f87c](https://github.com/teqplay/portreporter-backend/commit/345574d2f87c)
**Author:** Wouter Naloop
**Reviewers:** Joost Laurman, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/visit_structure_PRP-662](https://github.com/teqplay/portreporter-backend/tree/feat/visit_structure_PRP-662)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-05-12T13:27:11.924792+00:00
**Status:** MERGED

This is a big visit refactor of portreporter. with alot of minor changes. 

Tried to saveguard all changes inside the unittests and as extra on top of it added a confluence page with the decisions we have made in the process.

https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/92667905/Portreporter+Visit+structure+rules

* do not remove the estimations when a visit gets cancelled, so that when it gets added again we have the best guess available

