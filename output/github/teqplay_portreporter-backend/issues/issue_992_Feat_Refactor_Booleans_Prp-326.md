---
id: github:teqplay/portreporter-backend:issue:992
source: github
type: issue
repo: teqplay/portreporter-backend
number: 992
title: Feat/Refactor Booleans Prp-326
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/992
labels: []
explicit_links: []
---
# Issue #992: Feat/Refactor Booleans Prp-326

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/992  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [da12f284b767...d76354f0051c](https://github.com/teqplay/portreporter-backend/compare/da12f284b767...d76354f0051c)
**Merge commit:** [d76354f0051c](https://github.com/teqplay/portreporter-backend/commit/d76354f0051c)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/refactor_booleans_PRP-326](https://github.com/teqplay/portreporter-backend/tree/feat/refactor_booleans_PRP-326)
**Destination Branch:** [feat/upgrade_dependencies_PRP-326](https://github.com/teqplay/portreporter-backend/tree/feat/upgrade_dependencies_PRP-326)
**Closed On:** 2021-12-27T16:53:10.454867+00:00
**Status:** MERGED

* refactored all booleans related to database operations or returned from controllers from isBoolean -> boolean

* fix mail template variable that was needed to be in the isBoolean format

