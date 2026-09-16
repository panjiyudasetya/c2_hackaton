---
id: github:teqplay/portreporter-backend:issue:987
source: github
type: issue
repo: teqplay/portreporter-backend
number: 987
title: Feat/Upgrade Dependencies Prp-326
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/987
labels: []
explicit_links: []
---
# Issue #987: Feat/Upgrade Dependencies Prp-326

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/987  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [c96f2f1e9da3...3d994af67c87](https://github.com/teqplay/portreporter-backend/compare/c96f2f1e9da3...3d994af67c87)
**Merge commit:** [3d994af67c87](https://github.com/teqplay/portreporter-backend/commit/3d994af67c87)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Former user
**Source Branch:** [feat/upgrade_dependencies_PRP-326](https://github.com/teqplay/portreporter-backend/tree/feat/upgrade_dependencies_PRP-326)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:39.174902+00:00
**Status:** MERGED

* upgrading portreporter depencies, includes a big refactor of everything I had to refactor

* use the gradle wrapper in circleci

* downgraded the dependency that enforced using java 11, removed some warnings

* upgraded the okhttp and retrofit dependencies and related code

* replaced the deprecated compile for implementation, use 1 style of defining the dependencies, upgrade some more dependencies

