---
id: github:teqplay/vesselvoyage-backend:issue:98
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 98
title: Spv-1174 Improve Startup Mechanism
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/98
labels: []
explicit_links: []
---
# Issue #98: Spv-1174 Improve Startup Mechanism

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/98  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b12ad31f1dcf...a33acc879907](https://github.com/teqplay/vesselvoyage-backend/compare/b12ad31f1dcf...a33acc879907)
**Merge commit:** [a33acc879907](https://github.com/teqplay/vesselvoyage-backend/commit/a33acc879907)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Gavin den Hollander
**Approvers:** Gavin den Hollander, Wouter Naloop
**Source Branch:** [SPV-1174_improve_startup_mechanism](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1174_improve_startup_mechanism)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-11-15T10:27:03.171713+00:00
**Status:** MERGED

* Added a retry and shutdown mechanism when the needed caches can't be loaded in correctly
* Fixed a bunch of unit tests that didn't like the shutdown of the spring context when empty lists were returned
* ktlint
* Changed logic to not shut down and instead don't process rabbitmq
* Attempt to fix unit tests that don't run in CI
* Fixed broken unit test


