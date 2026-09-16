---
id: github:teqplay/portreporter-backend:issue:1130
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1130
title: Feat/Upgrade Spring Boot
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1130
labels: []
explicit_links: []
---
# Issue #1130: Feat/Upgrade Spring Boot

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1130  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [27de4be4e5b7...2b2118e42692](https://github.com/teqplay/portreporter-backend/compare/27de4be4e5b7...2b2118e42692)
**Merge commit:** [2b2118e42692](https://github.com/teqplay/portreporter-backend/commit/2b2118e42692)
**Author:** Wouter Naloop
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feat/upgrade_spring_boot](https://github.com/teqplay/portreporter-backend/tree/feat/upgrade_spring_boot)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-09-20T08:27:58.414448+00:00
**Status:** MERGED

* PRP-1240: start of eks changes

* PRP-1240: date to instant start but does not work yet

* PRP-1240: make instants work by removing the kmongo configuration, cleanup, remove portcallplus Date converter, remove all DateTimeFormat annotations

* PRP-1240: I know this still fails, but fixed the date to long bug

* PRP-1240: resolve merge conflicts and make sure it can run on beanstalk again

* PRP-1240: downgrade gradle

* PRP-1240: trying to get portreporter to build on circleCi

* PRP-1240: re add git properties

* PRP-1240: override mongo client instead of settings only



Kept these commit changes in here so you can see the process

