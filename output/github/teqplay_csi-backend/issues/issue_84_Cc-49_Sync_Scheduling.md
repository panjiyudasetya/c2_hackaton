---
id: github:teqplay/csi-backend:issue:84
source: github
type: issue
repo: teqplay/csi-backend
number: 84
title: Cc-49 Sync Scheduling
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/84
labels: []
explicit_links:
- jira:CC-49
---
# Issue #84: Cc-49 Sync Scheduling

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/84  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [b46b1dce1777...a599c3b91cfb](https://github.com/teqplay/csi-backend/compare/b46b1dce1777...a599c3b91cfb)
**Merge commit:** [a599c3b91cfb](https://github.com/teqplay/csi-backend/commit/a599c3b91cfb)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [CC-49-sync-scheduling](https://github.com/teqplay/csi-backend/tree/CC-49-sync-scheduling)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-12-02T17:31:00.072094+00:00
**Status:** MERGED

Includes all collections changes, so only check line 60-67 in SyncService:  
  
```kotlin
    @Scheduled(cron = "\${sync.auto-sync-cron}")
    fun autoSync() {
        if (syncProperties.autoSyncEnabled) {
            logger.info("Starting scheduled syncing from ${syncProperties.autoSyncSource}")
            synchronize(syncProperties.autoSyncSource, true)
            logger.info("Finished scheduled syncing from ${syncProperties.autoSyncSource}")
        }
    }
```
* Scheduled syncing

