---
id: github:teqplay/portreporter-backend:issue:928
source: github
type: issue
repo: teqplay/portreporter-backend
number: 928
title: 'Cleanup: Https://Trello.Com/C/Nr3Hidvj/8782-20-Clean-Up-Portreporter'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/928
labels: []
explicit_links: []
---
# Issue #928: Cleanup: Https://Trello.Com/C/Nr3Hidvj/8782-20-Clean-Up-Portreporter

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/928  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ac4e27f89135...d43a266fa3b5](https://github.com/teqplay/portreporter-backend/compare/ac4e27f89135...d43a266fa3b5)
**Merge commit:** [d43a266fa3b5](https://github.com/teqplay/portreporter-backend/commit/d43a266fa3b5)
**Author:** Shravan Shetty
**Reviewers:** Wouter Naloop, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/testBuilders](https://github.com/teqplay/portreporter-backend/tree/feat/testBuilders)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-08-27T14:21:48.496047+00:00
**Status:** MERGED

* update: added TestBuilder a single point of entry for all builders and mocks
* update: removed TestHelper from library. all in builders now. Included library tests in gradle build
* update: cleanup of test builders and the use of them in tests
* removed portcall, subscription and notification mock/builders. Others can follow similar template in the future
* update: removed all datasource dependency in the controller level
* update: removed all not directly related datasource dependency at logic level


