---
id: github:teqplay/vesselvoyage-backend:issue:319
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 319
title: Spv-2287 Update Recalculation State On Finish
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/319
labels: []
explicit_links:
- jira:SPV-2287
---
# Issue #319: Spv-2287 Update Recalculation State On Finish

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/319  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [9826b184bafe...42d4a48ca131](https://github.com/teqplay/vesselvoyage-backend/compare/9826b184bafe...42d4a48ca131)
**Merge commit:** [42d4a48ca131](https://github.com/teqplay/vesselvoyage-backend/commit/42d4a48ca131)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse, Wouter Naloop
**Approvers:** Leon Joosse
**Source Branch:** [SPV-2287-update-recalculation-state-on-finish](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2287-update-recalculation-state-on-finish)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-21T14:18:31.611142+00:00
**Status:** MERGED

* Extended automatic recalculation to update state to finished or error when the scenario is done
* Updated existing tests and added a new test case to ensure ships are correctly updated to the new state
* Also cover the case where errors are handled as well updating the state to ERROR
* Adjusted implementation to handle general errors as well that are not tied to an IMO
* Code cleanup
* Removed unused function
* ktlint

