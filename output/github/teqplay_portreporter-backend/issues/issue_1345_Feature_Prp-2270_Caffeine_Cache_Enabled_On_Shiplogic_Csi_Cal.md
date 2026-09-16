---
id: github:teqplay/portreporter-backend:issue:1345
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1345
title: Feature/Prp-2270 Caffeine Cache Enabled On Shiplogic Csi Calls
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1345
labels: []
explicit_links: []
---
# Issue #1345: Feature/Prp-2270 Caffeine Cache Enabled On Shiplogic Csi Calls

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1345  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [817b7088ca2b...0b8740374797](https://github.com/teqplay/portreporter-backend/compare/817b7088ca2b...0b8740374797)
**Merge commit:** [0b8740374797](https://github.com/teqplay/portreporter-backend/commit/0b8740374797)
**Author:** Shan Minh Nguyen
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [feature/PRP-2270_caffeine_cache_enabled_on_shiplogic_csi_calls](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2270_caffeine_cache_enabled_on_shiplogic_csi_calls)
**Destination Branch:** [feature/PRP-2281_create_annotation_to_check_services_health_before_handling_endpoint](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2281_create_annotation_to_check_services_health_before_handling_endpoint)
**Closed On:** 2023-11-23T10:53:42.708347+00:00
**Status:** MERGED

* Added two CSI caches based on imos and mmsis in shiplogic to reduce some duplicate calls being made right now with a configurable cache timer.
* Enabled caffeine cache on shiplogic csi calls.

