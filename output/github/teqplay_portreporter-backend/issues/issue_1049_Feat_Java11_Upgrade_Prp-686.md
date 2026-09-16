---
id: github:teqplay/portreporter-backend:issue:1049
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1049
title: Feat/Java11 Upgrade Prp-686
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1049
labels: []
explicit_links: []
---
# Issue #1049: Feat/Java11 Upgrade Prp-686

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1049  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b45a23592a85...250729d6582d](https://github.com/teqplay/portreporter-backend/compare/b45a23592a85...250729d6582d)
**Merge commit:** [250729d6582d](https://github.com/teqplay/portreporter-backend/commit/250729d6582d)
**Author:** Wouter Naloop
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/java11_upgrade_PRP-686](https://github.com/teqplay/portreporter-backend/tree/feat/java11_upgrade_PRP-686)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-02-24T15:33:38.795250+00:00
**Status:** MERGED

* The neccesary changes to go from a linux 1 eb instance to linux 2

* add the janino library

* add the nginx https config

* python27-boto3 is not available on amazon linux 2 so using python2-boto3

* remove unneccesary cloudwatch eb extension

* add the log config from vesselvoyage

* tomcat8 to tomcat

* make the log group name tomcat8 like before

