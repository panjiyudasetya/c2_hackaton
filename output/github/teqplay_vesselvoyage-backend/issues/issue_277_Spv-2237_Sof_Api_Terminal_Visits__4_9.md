---
id: github:teqplay/vesselvoyage-backend:issue:277
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 277
title: Spv-2237 Sof Api Terminal Visits (4/9)
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/277
labels: []
explicit_links:
- jira:SPV-2237
---
# Issue #277: Spv-2237 Sof Api Terminal Visits (4/9)

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/277  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [00815e4d9a2f...353429c66949](https://github.com/teqplay/vesselvoyage-backend/compare/00815e4d9a2f...353429c66949)
**Merge commit:** [353429c66949](https://github.com/teqplay/vesselvoyage-backend/commit/353429c66949)
**Author:** Leon Joosse
**Reviewers:** Darius Wattimena
**Approvers:** Former user
**Source Branch:** [SPV-2237-sof-api-terminal-visits](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2237-sof-api-terminal-visits)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-18T08:22:46.380885+00:00
**Status:** MERGED

This adds the terminal visit to the SOF model.
Couple of things to note / keep in mind:
* A terminal visit is derived from berth stops \(berth stops → berth visits → terminal visits\)
* A terminal visit is derived from a berth visit that has a `berth.terminalId`. Adjacent terminal visits with the same terminal id are merged into the same terminal visit. See the documentation in the code for a full explanation.
* A terminal may occur multiple times in the terminal visit list, when the ship visits the terminal multiple times. For example, ship goes to Vopak Europoort Terminal, then Koole Terminals, then Vopak Europoort Terminal again. That results in 2 terminal visits for Vopak and 1 for Koole.

