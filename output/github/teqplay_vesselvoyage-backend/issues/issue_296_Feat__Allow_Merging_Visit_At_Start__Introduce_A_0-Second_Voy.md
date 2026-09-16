---
id: github:teqplay/vesselvoyage-backend:issue:296
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 296
title: 'Feat: Allow Merging Visit At Start, Introduce A 0-Second Voyage'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/296
labels: []
explicit_links: []
---
# Issue #296: Feat: Allow Merging Visit At Start, Introduce A 0-Second Voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/296  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b70f7c7974bc...4dfbab39c78c](https://github.com/teqplay/vesselvoyage-backend/compare/b70f7c7974bc...4dfbab39c78c)
**Merge commit:** [4dfbab39c78c](https://github.com/teqplay/vesselvoyage-backend/commit/4dfbab39c78c)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/allow-merging-visit-at-start](https://github.com/teqplay/vesselvoyage-backend/tree/feat/allow-merging-visit-at-start)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-26T06:53:01.859828+00:00
**Status:** MERGED

Previously when merging back data, the first visit would be completely removed to maintain consistency of having a voyage at the start and end of the merge.
By allowing this first visit to be kept, it means a 0-second voyage at the start is required. Which allows to maintain merge consistency, and ensures merging back multiple times still yields the same \(idempotent\) result.

