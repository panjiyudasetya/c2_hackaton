---
id: github:teqplay/portreporter-backend:issue:1088
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1088
title: Feat/Auto Fix Duplicate Planned Berths
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1088
labels: []
explicit_links: []
---
# Issue #1088: Feat/Auto Fix Duplicate Planned Berths

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1088  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [17af594a7e47...591177110e21](https://github.com/teqplay/portreporter-backend/compare/17af594a7e47...591177110e21)
**Merge commit:** [591177110e21](https://github.com/teqplay/portreporter-backend/commit/591177110e21)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/auto_fix_duplicate_planned_berths](https://github.com/teqplay/portreporter-backend/tree/feat/auto_fix_duplicate_planned_berths)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-05-17T12:49:56.535322+00:00
**Status:** MERGED

* Attempt to fix the duplicate berths in the planning

* add the berth owner id from platform to portreporter


Sometimes the id ends up in the name, that may cause unwanted duplicates so this should dedupe that part

