---
id: github:teqplay/portreporter-backend:issue:1410
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1410
title: Dev-448 Updating To Spring 3.1
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1410
labels: []
explicit_links:
- jira:DEV-448
---
# Issue #1410: Dev-448 Updating To Spring 3.1

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1410  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [204ede34eecd...66d56f2fdb7f](https://github.com/teqplay/portreporter-backend/compare/204ede34eecd...66d56f2fdb7f)
**Merge commit:** [66d56f2fdb7f](https://github.com/teqplay/portreporter-backend/commit/66d56f2fdb7f)
**Author:** Jamie de Leest
**Reviewers:** Darius Wattimena, Joaquin Marquez Bugella, Shan Minh Nguyen
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [DEV-448-updating-to-spring-3.1](https://github.com/teqplay/portreporter-backend/tree/DEV-448-updating-to-spring-3.1)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2025-01-13T14:02:59.364818+00:00
**Status:** MERGED

* refactor: move application properties from Konfig to Property classes
* refactor: implement konfig changes
* refactor: implement spring 3.1 changes
* Ktlint upgrade to 11.5.0 and ktlint formatting.
* testing: add properties for tests with a test secret
* fix: add application-kubernetes
* fix: update jackson version
* fix: change jackson configuration
* fix: changed test to the write object mapper
* fix: revert jackson changes
* fix: remove unused importers
* fix: changed import for objectmapper
* fix: update skeleton version for poma client fixes
* fix: swagger fixes and unauthorized login url
* fix: save security context
* chore: ktlint format
* fix: replaced the custom security filter chain with the skeleton filter chain with bean configuration

