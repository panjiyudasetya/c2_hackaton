---
id: github:teqplay/vesselvoyage-backend:issue:276
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 276
title: Spv-2259 Fix Multiple Visit Issues
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/276
labels: []
explicit_links: []
---
# Issue #276: Spv-2259 Fix Multiple Visit Issues

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/276  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [351a28426edc...1b743d7c09a1](https://github.com/teqplay/vesselvoyage-backend/compare/351a28426edc...1b743d7c09a1)
**Merge commit:** [1b743d7c09a1](https://github.com/teqplay/vesselvoyage-backend/commit/1b743d7c09a1)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Former user
**Source Branch:** [SPV-2259-fix-first-visit-issue](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2259-fix-first-visit-issue)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-12T12:25:06.219776+00:00
**Status:** MERGED

* Fix multiple issues where visits wouldn't be handled correctly when it was a pass-through
* Fix an issue where when switching main port the new main port wouldn't be removed from the other ongoing EOSP area activities
* Fixed an issue where the current visit eosp activity would be marked as a pass through eosp when still ongoing

