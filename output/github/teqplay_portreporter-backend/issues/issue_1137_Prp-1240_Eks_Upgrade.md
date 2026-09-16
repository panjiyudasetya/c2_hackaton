---
id: github:teqplay/portreporter-backend:issue:1137
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1137
title: Prp-1240/Eks Upgrade
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1137
labels: []
explicit_links:
- jira:PRP-1240
---
# Issue #1137: Prp-1240/Eks Upgrade

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1137  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [bf6f4f0bc94f...f0a6a42d0d7e](https://github.com/teqplay/portreporter-backend/compare/bf6f4f0bc94f...f0a6a42d0d7e)
**Merge commit:** [f0a6a42d0d7e](https://github.com/teqplay/portreporter-backend/commit/f0a6a42d0d7e)
**Author:** Wouter Naloop
**Reviewers:** Darius Wattimena, Joaquin Marquez Bugella
**Approvers:** Darius Wattimena
**Source Branch:** [PRP-1240/eks_upgrade](https://github.com/teqplay/portreporter-backend/tree/PRP-1240/eks_upgrade)
**Destination Branch:** [feat/upgrade_spring_boot](https://github.com/teqplay/portreporter-backend/tree/feat/upgrade_spring_boot)
**Closed On:** 2022-08-25T13:22:22.009695+00:00
**Status:** MERGED

* PRP-1240: eks upgrade

* PRP-1240: change the docker image name to what is in ecr

* PRP-1240: make the error level slack logging configurable and default to ERROR

* PRP-1240: set default actuator settings, remove the repo name info from the circle ci and hardcode it

* PRP-1240: hard hard code it

* PRP-1240: locally disable the slack webhook, disable the default rabbitmq health check of spring

* PRP-1240: remove the exclude by default config of the actuator and include the liveness and readiness states in the actuator

* PRP-1240: allow access without auth to every actuator endpoint

* PRP-1240: remove ebs folders, apply the liveness and readiness as group when locally using portreporter

* PRP-1240: add the publish library step to circleCi

* PRP-1240: test publish library when this branch is pushed

* PRP-1240: revert test setup for portcall library publish, upgrade gradle wrapper to 7.4.1, remove git properties

