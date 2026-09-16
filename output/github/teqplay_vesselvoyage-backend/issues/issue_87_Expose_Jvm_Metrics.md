---
id: github:teqplay/vesselvoyage-backend:issue:87
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 87
title: Expose Jvm Metrics
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/87
labels: []
explicit_links: []
---
# Issue #87: Expose Jvm Metrics

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/87  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [bc2828c2b12b...eb1752ac1b70](https://github.com/teqplay/vesselvoyage-backend/compare/bc2828c2b12b...eb1752ac1b70)
**Merge commit:** [eb1752ac1b70](https://github.com/teqplay/vesselvoyage-backend/commit/eb1752ac1b70)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [expose_jvm_metrics](https://github.com/teqplay/vesselvoyage-backend/tree/expose_jvm_metrics)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-09-19T07:40:17.103918+00:00
**Status:** MERGED

* Added JVM metrics to be exposed to prometheus
* Set production memory limit to 11Gi
* Changed CI to always provide the helm values when doing a deploy
* Added prometheus to allowed endpoints to access without any authorization


