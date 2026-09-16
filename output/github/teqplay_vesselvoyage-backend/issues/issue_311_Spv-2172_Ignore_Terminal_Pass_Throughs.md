---
id: github:teqplay/vesselvoyage-backend:issue:311
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 311
title: Spv-2172 Ignore Terminal Pass Throughs
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/311
labels: []
explicit_links: []
---
# Issue #311: Spv-2172 Ignore Terminal Pass Throughs

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/311  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [419e9f9bd0eb...e7f0180ec0f1](https://github.com/teqplay/vesselvoyage-backend/compare/419e9f9bd0eb...e7f0180ec0f1)
**Merge commit:** [e7f0180ec0f1](https://github.com/teqplay/vesselvoyage-backend/commit/e7f0180ec0f1)
**Author:** Darius Wattimena
**Reviewers:** Michel Wilson, Leon Joosse
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2172-ignore-terminal-pass-throughs](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2172-ignore-terminal-pass-throughs)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-09T08:26:27.194307+00:00
**Status:** MERGED

* Adjusted terminal mooring end event processing to only keep the ones where we stopped
* Changed existing tests to match the new behaviour

