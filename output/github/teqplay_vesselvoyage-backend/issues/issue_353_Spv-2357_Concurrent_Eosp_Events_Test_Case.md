---
id: github:teqplay/vesselvoyage-backend:issue:353
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 353
title: Spv-2357 Concurrent Eosp Events Test Case
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/353
labels: []
explicit_links:
- jira:SPV-2357
---
# Issue #353: Spv-2357 Concurrent Eosp Events Test Case

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/353  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [2d53e0f604a6...fb62cf07159d](https://github.com/teqplay/vesselvoyage-backend/compare/2d53e0f604a6...fb62cf07159d)
**Merge commit:** [fb62cf07159d](https://github.com/teqplay/vesselvoyage-backend/commit/fb62cf07159d)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse, Joost Dambrink
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2357-fix-concurrent-eosp-events](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2357-fix-concurrent-eosp-events)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-10-25T09:34:44.491895+00:00
**Status:** MERGED

I first thought that the behaviour was broken. But after thoroughly debugging it turned out that the current flow works, however the existing tests were looking at a wrong timestamp. Still something is broken with broken visit/voyage structures, so will continue in a new branch to try to reproduce and fix it

