---
id: github:teqplay/vesselvoyage-backend:issue:289
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 289
title: 'Fix: Ensure Origin And Destination Port Is Set'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/289
labels: []
explicit_links: []
---
# Issue #289: Fix: Ensure Origin And Destination Port Is Set

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/289  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [4dfbab39c78c...ec164fffb8a5](https://github.com/teqplay/vesselvoyage-backend/compare/4dfbab39c78c...ec164fffb8a5)
**Merge commit:** [ec164fffb8a5](https://github.com/teqplay/vesselvoyage-backend/commit/ec164fffb8a5)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2104-update-v2-merging-code-to-not-be-lossy](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2104-update-v2-merging-code-to-not-be-lossy)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-26T07:04:28.500048+00:00
**Status:** MERGED

When merging back the `voyage.originPort` and `voyage.destinationPort` need to be aligned with newly merged visits.

