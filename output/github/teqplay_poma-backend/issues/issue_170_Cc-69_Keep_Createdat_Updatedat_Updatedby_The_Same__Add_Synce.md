---
id: github:teqplay/poma-backend:issue:170
source: github
type: issue
repo: teqplay/poma-backend
number: 170
title: Cc-69 Keep Createdat/Updatedat/Updatedby The Same, Add Syncedat Timestamp
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/170
labels: []
explicit_links: []
---
# Issue #170: Cc-69 Keep Createdat/Updatedat/Updatedby The Same, Add Syncedat Timestamp

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/170  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [b37fe5be0eba...ac9a5be7032b](https://github.com/teqplay/poma-backend/compare/b37fe5be0eba...ac9a5be7032b)
**Merge commit:** [ac9a5be7032b](https://github.com/teqplay/poma-backend/commit/ac9a5be7032b)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [CC-69-sync-same-created-and-updated-add-syncedAt](https://github.com/teqplay/poma-backend/tree/CC-69-sync-same-created-and-updated-add-syncedAt)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-11-18T16:24:52.518379+00:00
**Status:** MERGED

* Changed responseType from ApiModel to Model, changed responseModels to externalModels for clarity
* Added syncedAt to all InfrastructureModels
* Changed ApiModel to Model in ModelDifference

