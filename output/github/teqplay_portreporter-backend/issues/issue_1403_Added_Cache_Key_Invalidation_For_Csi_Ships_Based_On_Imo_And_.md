---
id: github:teqplay/portreporter-backend:issue:1403
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1403
title: Added Cache Key Invalidation For Csi Ships Based On Imo And Mmsi
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1403
labels: []
explicit_links: []
---
# Issue #1403: Added Cache Key Invalidation For Csi Ships Based On Imo And Mmsi

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1403  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [10fc8b3c0d8a...a6e699989941](https://github.com/teqplay/portreporter-backend/compare/10fc8b3c0d8a...a6e699989941)
**Merge commit:** [a6e699989941](https://github.com/teqplay/portreporter-backend/commit/a6e699989941)
**Author:** Shan Minh Nguyen
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/PRP-2473_invalidating_csi_cache_keys_upon_update](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2473_invalidating_csi_cache_keys_upon_update)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-10-30T07:52:02.815626+00:00
**Status:** MERGED

Added an invalidation of caches based on the ship imo/mmsi after a portcall update is performed.

