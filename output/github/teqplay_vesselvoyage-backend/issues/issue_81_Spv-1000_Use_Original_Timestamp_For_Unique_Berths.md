---
id: github:teqplay/vesselvoyage-backend:issue:81
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 81
title: Spv-1000 Use Original Timestamp For Unique Berths
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/81
labels: []
explicit_links: []
---
# Issue #81: Spv-1000 Use Original Timestamp For Unique Berths

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/81  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [c32213a56568...e47195c9b9ec](https://github.com/teqplay/vesselvoyage-backend/compare/c32213a56568...e47195c9b9ec)
**Merge commit:** [e47195c9b9ec](https://github.com/teqplay/vesselvoyage-backend/commit/e47195c9b9ec)
**Author:** Darius Wattimena
**Reviewers:** Joost Dambrink
**Approvers:** Joost Dambrink
**Source Branch:** [SPV-1000_use_original_timestamp_for_unique_berths](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1000_use_original_timestamp_for_unique_berths)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-07-12T15:37:21.563385+00:00
**Status:** MERGED

* Use the originalTimestamp instead when parsing a UniqueBerthEvent
* Fixed the UnitTests that use the UniqueBerthEvent eventTime to instead use the originalTimestamp
Change is rather small so feel free to take a look @{5f4cda8d3e9e2e004d5edf39} if you want

