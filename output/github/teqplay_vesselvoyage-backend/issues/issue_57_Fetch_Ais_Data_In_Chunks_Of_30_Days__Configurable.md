---
id: github:teqplay/vesselvoyage-backend:issue:57
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 57
title: Fetch Ais Data In Chunks Of 30 Days (Configurable)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/57
labels: []
explicit_links: []
---
# Issue #57: Fetch Ais Data In Chunks Of 30 Days (Configurable)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/57  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [202fb0390ade...382fdfd9ead1](https://github.com/teqplay/vesselvoyage-backend/compare/202fb0390ade...382fdfd9ead1)
**Merge commit:** [382fdfd9ead1](https://github.com/teqplay/vesselvoyage-backend/commit/382fdfd9ead1)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/fetch_ais_in_chunks](https://github.com/teqplay/vesselvoyage-backend/tree/fix/fetch_ais_in_chunks)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-11T13:55:47.966883+00:00
**Status:** MERGED

In some cases, there are ships like tugs which have a visit with a duration of years. Generating an AIS trace for such a long visit/voyage can result in timeouts or running out of memory. 

This PR solves this by fetching AIS history in chunks of 30 days using a new method `queryAisHistoryInChunks`, and applying `simplifyTraceWithStops` on each of the individual chunks.

