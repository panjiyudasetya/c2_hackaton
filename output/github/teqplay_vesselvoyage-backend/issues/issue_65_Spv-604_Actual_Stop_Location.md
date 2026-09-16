---
id: github:teqplay/vesselvoyage-backend:issue:65
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 65
title: Spv-604 Actual Stop Location
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/65
labels: []
explicit_links: []
---
# Issue #65: Spv-604 Actual Stop Location

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/65  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [f1c97802b568...c863634ea2da](https://github.com/teqplay/vesselvoyage-backend/compare/f1c97802b568...c863634ea2da)
**Merge commit:** [c863634ea2da](https://github.com/teqplay/vesselvoyage-backend/commit/c863634ea2da)
**Author:** Darius Wattimena
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [SPV-604_actual-stop-location](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-604_actual-stop-location)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-24T13:37:03.825525+00:00
**Status:** MERGED

* Add the ability to store the actual location of a stop to somewhat represent the middle of a stop
* Added a fallback of setting the actual stop location by using the historical trace, and otherwise it will ask global if not found in both the ongoing and historical
* Fixed broken unit tests \+ added a new one to cover the setting of the actual location logic
* Fixed an issue where the historic trace wouldn't be received correctly
* Please ktlint


