---
id: github:teqplay/vesselvoyage-backend:issue:320
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 320
title: Spv-2241 Encounters
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/320
labels: []
explicit_links:
- jira:SPV-2241
---
# Issue #320: Spv-2241 Encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/320  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [c3099dec459e...257fb669213e](https://github.com/teqplay/vesselvoyage-backend/compare/c3099dec459e...257fb669213e)
**Merge commit:** [257fb669213e](https://github.com/teqplay/vesselvoyage-backend/commit/257fb669213e)
**Author:** Leon Joosse
**Reviewers:** Michel Wilson, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2241-encounters](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2241-encounters)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-08-15T10:21:27.589286+00:00
**Status:** MERGED

* Extend NewEncounter from StartEnd
* Add EncounterInfo and API Encounter model, plus mapper toApi method
* Add test helpers for BerthVisitInfo and TerminalVisitInfo
* Add test for StartEnd.overlaps\(\)
* Add generate encounters to PTO SOF, include tests

