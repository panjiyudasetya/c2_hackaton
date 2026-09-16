---
id: github:teqplay/poma-backend:issue:99
source: github
type: issue
repo: teqplay/poma-backend
number: 99
title: Spv-1807 Calculate The Eos Automatically
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/99
labels: []
explicit_links: []
---
# Issue #99: Spv-1807 Calculate The Eos Automatically

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/99  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [fcf97f60acb7...bc2af02155ca](https://github.com/teqplay/poma-backend/compare/fcf97f60acb7...bc2af02155ca)
**Merge commit:** [bc2af02155ca](https://github.com/teqplay/poma-backend/commit/bc2af02155ca)
**Author:** Former user
**Reviewers:** Wouter Naloop, Maryam Tavakoli
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1807-calculate-the-eos-automatically](https://github.com/teqplay/poma-backend/tree/SPV-1807-calculate-the-eos-automatically)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2023-09-27T09:24:41.571806+00:00
**Status:** MERGED

* feat\(port\): calculate EOS automatically
* fix: use 'convertToApiModels' everywhere where there's a list

This PR implements the same automatic area generation that the terminal mooring areas have \([https://github.com/teqplay/poma-backend/issues/79](https://github.com/teqplay/poma-backend/issues/79) \)
Important things before this PR can be merged:
* frontend needs to be aware/changed to be able to set and unset if the EOS was created manually \([https://github.com/teqplay/poma-backend/issues/99](https://github.com/teqplay/poma-backend/issues/99) \)
* based on the above, the \(two\) ports that have manual EOS' set also need the `manualOverriddenEosArea` field to be set to `true`

In general this PR changes all usages of `result.map { service.convertToApiModel(it) }` to `service.convertToApiModels(result).` Which ensures more optimal code can be used when requesting terminal mooring areas or port EOS.
Also, the logic that was used to automatically generate the terminal mooring area is now extracted in a separate file, and reused to automatically generate the EOS.
Tested the performance impact by calculating this automatically as well \(on POMA sandbox\):
* for normal calls like “get by id / get one” and “get all within bounding box” \(as used by the frontend\) only become some milliseconds slower, not noticeable at all
* for a call like `/v1/port?validated=true` that returns all validated ports, it is <100 ms slower. Taking ~450 ms after this change and ~350 ms before this change \(on average\).

