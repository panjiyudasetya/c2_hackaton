---
id: github:teqplay/vesselvoyage-backend:issue:116
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 116
title: Spv-1187 Fix Stops Being Put On Future Voyage
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/116
labels: []
explicit_links: []
---
# Issue #116: Spv-1187 Fix Stops Being Put On Future Voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/116  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [2ea5b6607a37...ef0673008581](https://github.com/teqplay/vesselvoyage-backend/compare/2ea5b6607a37...ef0673008581)
**Merge commit:** [ef0673008581](https://github.com/teqplay/vesselvoyage-backend/commit/ef0673008581)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop, Former user
**Source Branch:** [SPV-1187_fix_stops_being_put_on_future_voyage](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1187_fix_stops_being_put_on_future_voyage)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2023-02-16T12:29:48.224108+00:00
**Status:** MERGED

* Fixed an issue where the regrouping of the esof would result in weird behaviour
* Changed the logic when the actual stop location is used for trace generation
* Commented out running of a test used to see the working of the trace simplification in geojson

