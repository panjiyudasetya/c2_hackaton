---
id: github:teqplay/vesselvoyage-backend:issue:66
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 66
title: Feat/Show Non Parsed Teqplayevents
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/66
labels: []
explicit_links: []
---
# Issue #66: Feat/Show Non Parsed Teqplayevents

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/66  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [15adf256daa2...f1c97802b568](https://github.com/teqplay/vesselvoyage-backend/compare/15adf256daa2...f1c97802b568)
**Merge commit:** [f1c97802b568](https://github.com/teqplay/vesselvoyage-backend/commit/f1c97802b568)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/show_non_parsed_teqplayevents](https://github.com/teqplay/vesselvoyage-backend/tree/feat/show_non_parsed_teqplayevents)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-24T13:25:28.536573+00:00
**Status:** MERGED

* Introduce a new method `fetchTeqplayEventsByIMO` to get the original, unconverted TeqplayEvents
* Let `convertTeqplayEvent` return a Success/failure `Result`, and use the error message in the dry-run ProcessedEvent results
* Use TeqplayEvents in the `processEventsDryRun` method

