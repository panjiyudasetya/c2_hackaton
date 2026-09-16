---
id: github:teqplay/vesselvoyage-backend:issue:58
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 58
title: Fix/Fetch Events In Chunks
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/58
labels: []
explicit_links: []
---
# Issue #58: Fix/Fetch Events In Chunks

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/58  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [382fdfd9ead1...8a186cca4f02](https://github.com/teqplay/vesselvoyage-backend/compare/382fdfd9ead1...8a186cca4f02)
**Merge commit:** [8a186cca4f02](https://github.com/teqplay/vesselvoyage-backend/commit/8a186cca4f02)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/fetch_events_in_chunks](https://github.com/teqplay/vesselvoyage-backend/tree/fix/fetch_events_in_chunks)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-14T12:58:12.750426+00:00
**Status:** MERGED

In some cases, there are ships that have many events. I’ve seen up to 40k events for a single ship, and this will only grow in the future.

Instead of fetching all events at once and holding them in memory, this PR fetches events in chunks and processes them via a stream, to prevent the application from running out of memory for “extreme“ ships.

