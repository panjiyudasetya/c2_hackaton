---
id: github:teqplay/vesselvoyage-backend:issue:285
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 285
title: Spv-2256 Api Missing Imo
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/285
labels: []
explicit_links:
- jira:SPV-2256
---
# Issue #285: Spv-2256 Api Missing Imo

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/285  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [d721fe69aee4...3e52af3c3950](https://github.com/teqplay/vesselvoyage-backend/compare/d721fe69aee4...3e52af3c3950)
**Merge commit:** [3e52af3c3950](https://github.com/teqplay/vesselvoyage-backend/commit/3e52af3c3950)
**Author:** Darius Wattimena
**Reviewers:** Leon Joosse
**Approvers:** Leon Joosse, Former user
**Source Branch:** [SPV-2256-api-missing-imo](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2256-api-missing-imo)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-24T08:03:25.303754+00:00
**Status:** MERGED

When getting the visits/voyages by port, then there is currently now way of knowing for which vessel this is part of. This PR adds the imo field to the exposed ones. No special mappers were needed as mapstruct solved this for us already.

