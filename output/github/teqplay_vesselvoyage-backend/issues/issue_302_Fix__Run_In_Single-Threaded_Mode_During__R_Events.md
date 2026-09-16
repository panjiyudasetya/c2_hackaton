---
id: github:teqplay/vesselvoyage-backend:issue:302
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 302
title: 'Fix: Run In Single-Threaded Mode During (R)Events'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/302
labels: []
explicit_links: []
---
# Issue #302: Fix: Run In Single-Threaded Mode During (R)Events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/302  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e29e600d0f73...f458d767a492](https://github.com/teqplay/vesselvoyage-backend/compare/e29e600d0f73...f458d767a492)
**Merge commit:** [f458d767a492](https://github.com/teqplay/vesselvoyage-backend/commit/f458d767a492)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena, Leon Joosse
**Source Branch:** [fix/revents-requires-single-threaded](https://github.com/teqplay/vesselvoyage-backend/tree/fix/revents-requires-single-threaded)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-30T09:21:00.764604+00:00
**Status:** MERGED

\(r\)events needs to be run single-threaded.
It uses status messages like poison pills and batch timestamps to indicate when respectively the process is finished and which batch it has processed. When the processing is done in other threads than the main one, these status events are sent out-of-sync with the processing logic.

