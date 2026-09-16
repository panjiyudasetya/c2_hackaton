---
id: github:teqplay/vesselvoyage-backend:issue:266
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 266
title: Spv-2050 Sof Api Portareas (2/9)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/266
labels: []
explicit_links:
- jira:SPV-2050
---
# Issue #266: Spv-2050 Sof Api Portareas (2/9)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/266  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d70ebca66d65...50ba0a87396c](https://github.com/teqplay/vesselvoyage-backend/compare/d70ebca66d65...50ba0a87396c)
**Merge commit:** [50ba0a87396c](https://github.com/teqplay/vesselvoyage-backend/commit/50ba0a87396c)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena, Former user
**Source Branch:** [SPV-2050-sof-api-portareas](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2050-sof-api-portareas)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-09T07:54:43.042473+00:00
**Status:** MERGED

This PR adds the `eosp.start` and `eosp.end` and `portAreas` to the `PtoStatementOfFactsView`.
Also adds an interface for objects having a `start` and `end`: `StartEnd`, to make comparing them easier. For now only on `AreaActivity` and `NewStop`.

