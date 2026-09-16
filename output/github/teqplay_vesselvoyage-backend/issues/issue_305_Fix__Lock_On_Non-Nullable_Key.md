---
id: github:teqplay/vesselvoyage-backend:issue:305
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 305
title: 'Fix: Lock On Non-Nullable Key'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/305
labels: []
explicit_links: []
---
# Issue #305: Fix: Lock On Non-Nullable Key

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/305  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3c78d8dd363b...a2611902dafb](https://github.com/teqplay/vesselvoyage-backend/compare/3c78d8dd363b...a2611902dafb)
**Merge commit:** [a2611902dafb](https://github.com/teqplay/vesselvoyage-backend/commit/a2611902dafb)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [fix/lock-on-non-nullable-key](https://github.com/teqplay/vesselvoyage-backend/tree/fix/lock-on-non-nullable-key)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-31T09:54:58.778371+00:00
**Status:** MERGED

`event.ship.imo` and `event.ship.mmsi` are nullable fields, and you’re not allowed to lock on `null`.
Need to use defaults in those cases.

