---
id: github:teqplay/vesselvoyage-backend:issue:136
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 136
title: Spv-1668 Stop Berth Event Fields
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/136
labels: []
explicit_links: []
---
# Issue #136: Spv-1668 Stop Berth Event Fields

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/136  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [5662a6d48fee...e51a4c188481](https://github.com/teqplay/vesselvoyage-backend/compare/5662a6d48fee...e51a4c188481)
**Merge commit:** [e51a4c188481](https://github.com/teqplay/vesselvoyage-backend/commit/e51a4c188481)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Former user
**Source Branch:** [SPV-1668_stop_berth_event_fields](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1668_stop_berth_event_fields)
**Destination Branch:** [SPV-1656_stop_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1656_stop_improvements)
**Closed On:** 2023-09-01T11:43:47.887134+00:00
**Status:** MERGED

* Added new fields on the Stop model to later be used for the matching berth event
* Set the berthStart and berthEnd fields to null on places where Stops are being created

