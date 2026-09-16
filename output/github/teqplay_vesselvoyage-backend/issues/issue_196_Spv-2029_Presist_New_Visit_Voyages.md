---
id: github:teqplay/vesselvoyage-backend:issue:196
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 196
title: Spv-2029 Presist New Visit Voyages
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/196
labels: []
explicit_links:
- jira:SPV-2029
---
# Issue #196: Spv-2029 Presist New Visit Voyages

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/196  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [241ff866b7f7...16288b263265](https://github.com/teqplay/vesselvoyage-backend/compare/241ff866b7f7...16288b263265)
**Merge commit:** [16288b263265](https://github.com/teqplay/vesselvoyage-backend/commit/16288b263265)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [SPV-2029-presist-new-visit-voyages](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2029-presist-new-visit-voyages)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-04T07:36:36.500991+00:00
**Status:** MERGED

* Added a feature flag so we can enable processing of the new definition
* Added event processing when the feature flag is enabled
* Adjusted tests to have the new future flag set

