---
id: github:teqplay/vesselvoyage-backend:issue:211
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 211
title: Spv-2073 Ais Trace Processing For V2
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/211
labels: []
explicit_links:
- jira:SPV-2073
---
# Issue #211: Spv-2073 Ais Trace Processing For V2

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/211  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d0438190dfcb...650231041d47](https://github.com/teqplay/vesselvoyage-backend/compare/d0438190dfcb...650231041d47)
**Merge commit:** [650231041d47](https://github.com/teqplay/vesselvoyage-backend/commit/650231041d47)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [SPV-2073-ais-diff-trace-processing](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2073-ais-diff-trace-processing)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-04-19T10:00:28.262073+00:00
**Status:** MERGED

* Changed trace logic so both V1 as V2 traces can be inserted
* Fix an issue where the message wouldn't be acknowledged when the new definition is enabled
* Added a test case covering the new definition
* Adjusted verification to actually check if the mocked ship status is used
* Changed processing trace service tests to reflect the new boolean result

