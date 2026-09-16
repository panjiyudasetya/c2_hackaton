---
id: github:teqplay/vesselvoyage-backend:issue:362
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 362
title: Spv-2387 Fix Recalculation Status
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/362
labels: []
explicit_links: []
---
# Issue #362: Spv-2387 Fix Recalculation Status

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/362  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [316856558237...93a3442915c3](https://github.com/teqplay/vesselvoyage-backend/compare/316856558237...93a3442915c3)
**Merge commit:** [93a3442915c3](https://github.com/teqplay/vesselvoyage-backend/commit/93a3442915c3)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Joost Dambrink
**Approvers:** Joost Dambrink
**Source Branch:** [SPV-2387-fix-recalculation-status](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2387-fix-recalculation-status)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-10-29T13:27:38.527475+00:00
**Status:** MERGED

* Added a gauge to also track the ships that ended up in the error state
* Added some logic to automatically cleanup scenarios that were stuck on restart of the backend

