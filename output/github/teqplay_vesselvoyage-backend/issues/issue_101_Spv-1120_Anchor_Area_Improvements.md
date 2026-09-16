---
id: github:teqplay/vesselvoyage-backend:issue:101
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 101
title: Spv-1120 Anchor Area Improvements
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/101
labels: []
explicit_links: []
---
# Issue #101: Spv-1120 Anchor Area Improvements

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/101  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [e919d667ae9d...98bd19a2edba](https://github.com/teqplay/vesselvoyage-backend/compare/e919d667ae9d...98bd19a2edba)
**Merge commit:** [98bd19a2edba](https://github.com/teqplay/vesselvoyage-backend/commit/98bd19a2edba)
**Author:** Darius Wattimena
**Reviewers:** Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [SPV-1120_anchor_area_improvements](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-1120_anchor_area_improvements)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-12-01T14:19:32.327754+00:00
**Status:** MERGED

* Increased the short duration to merge stops to improve anchor area detection
* Increased range to improve anchor area detection and changed fallback clause to not trigger for berths and only allow 1 anchor area stop per movement end-start
* Changed the logic how the actual location of a stop is determined to be based on the trace of the stop
* Made detection a bit more aggressive again, fixed some unit tests and added some documentation to the helper functions
* ktlint

