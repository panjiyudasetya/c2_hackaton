---
id: github:teqplay/vesselvoyage-backend:issue:95
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 95
title: Spv-1184 Daily Recalculate Mechanism
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/95
labels: []
explicit_links: []
---
# Issue #95: Spv-1184 Daily Recalculate Mechanism

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/95  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [185fca23ce0b...38956559d138](https://github.com/teqplay/vesselvoyage-backend/compare/185fca23ce0b...38956559d138)
**Merge commit:** [38956559d138](https://github.com/teqplay/vesselvoyage-backend/commit/38956559d138)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop, Gavin den Hollander
**Approvers:** Gavin den Hollander
**Source Branch:** [SPV-1184_daily_recalculate_mechanism](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1184_daily_recalculate_mechanism)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-11-15T10:25:58.506292+00:00
**Status:** MERGED

* Renamed model for recalculating vessels
* Added preparations to recalculate events via an endpoint
* Added the functionality to recalculate via a snapshot mechanism
* Finalized the snapshot recalculation mechanism
* Code formatting
* Added a test to recalculate by snapshot
* Added comments how the new properties work and fixed the failing spring context test
* Changed mongo id annotation to properly work


