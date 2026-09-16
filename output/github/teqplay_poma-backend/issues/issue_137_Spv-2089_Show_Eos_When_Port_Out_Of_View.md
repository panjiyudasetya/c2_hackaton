---
id: github:teqplay/poma-backend:issue:137
source: github
type: issue
repo: teqplay/poma-backend
number: 137
title: Spv-2089 Show Eos When Port Out Of View
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/137
labels: []
explicit_links: []
---
# Issue #137: Spv-2089 Show Eos When Port Out Of View

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/137  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [99a1a696f56e...1f6b85525868](https://github.com/teqplay/poma-backend/compare/99a1a696f56e...1f6b85525868)
**Merge commit:** [1f6b85525868](https://github.com/teqplay/poma-backend/commit/1f6b85525868)
**Author:** Pim van den Toorn
**Reviewers:** Darius Wattimena, Maryam Tavakoli
**Approvers:** Darius Wattimena, Maryam Tavakoli
**Source Branch:** [SPV-2089-show-eos-when-port-out-of-view](https://github.com/teqplay/poma-backend/tree/SPV-2089-show-eos-when-port-out-of-view)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2024-08-05T08:53:34.765631+00:00
**Status:** MERGED

This update adds the option to include the eos area when looking for ports within some area. This is done by adding an eos bounding box to every port, which gets updated anytime an anchorage, pilot boarding, approach area or break water area gets created or updated.

* Port search bounding box uses eos bound when available
* Port search added eosAreaFilter flag
* Added EosAreaService, EOS area and its bounding box are now updated whenever an anchorage, pilot boarding, approach area or break water area gets created or updated, added a fixEosAreas endpoint to update all ports,

