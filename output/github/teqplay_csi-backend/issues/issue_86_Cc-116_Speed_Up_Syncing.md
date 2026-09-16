---
id: github:teqplay/csi-backend:issue:86
source: github
type: issue
repo: teqplay/csi-backend
number: 86
title: Cc-116 Speed Up Syncing
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/86
labels: []
explicit_links: []
---
# Issue #86: Cc-116 Speed Up Syncing

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/86  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [a599c3b91cfb...3613b67c88b2](https://github.com/teqplay/csi-backend/compare/a599c3b91cfb...3613b67c88b2)
**Merge commit:** [3613b67c88b2](https://github.com/teqplay/csi-backend/commit/3613b67c88b2)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [CC-116-speed-up-syncing](https://github.com/teqplay/csi-backend/tree/CC-116-speed-up-syncing)
**Destination Branch:** [develop](https://github.com/teqplay/csi-backend/tree/develop)
**Closed On:** 2024-12-16T10:00:43.884133+00:00
**Status:** MERGED

* Synchronize now run async \(diff threads\), changed syncedAt to an Instant
* Added not equals check between local and external model, faster than going through all \(sub\)properties per model
* added some logging

