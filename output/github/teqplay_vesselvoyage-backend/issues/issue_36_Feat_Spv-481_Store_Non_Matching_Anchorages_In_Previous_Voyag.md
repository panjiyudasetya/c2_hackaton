---
id: github:teqplay/vesselvoyage-backend:issue:36
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 36
title: Feat/Spv-481 Store Non Matching Anchorages In Previous Voyage
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/36
labels: []
explicit_links: []
---
# Issue #36: Feat/Spv-481 Store Non Matching Anchorages In Previous Voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/36  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [05b54194e595...a97dd3f451bc](https://github.com/teqplay/vesselvoyage-backend/compare/05b54194e595...a97dd3f451bc)
**Merge commit:** [a97dd3f451bc](https://github.com/teqplay/vesselvoyage-backend/commit/a97dd3f451bc)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/SPV-481_store_non-matching_anchorages_in_previous_voyage](https://github.com/teqplay/vesselvoyage-backend/tree/feat/SPV-481_store_non-matching_anchorages_in_previous_voyage)
**Destination Branch:** [chore/SPV-480_extend_VoyageShipStatus_with_previousVoyage](https://github.com/teqplay/vesselvoyage-backend/tree/chore/SPV-480_extend_VoyageShipStatus_with_previousVoyage)
**Closed On:** 2022-01-03T12:34:44.807088+00:00
**Status:** MERGED

* Move data classes `AnchorAreaVisit` and `PortAreaVisit` in their own file
* Extend the `Voyage` data model with a property `anchorAreas`
* When finishing a visit \(and starting a voyage\), move non-matching anchor areas to the previous voyage instead of deleting them
* when deleting a visit because of being a pass-through, move all it’s anchor areas to the previous voyage instead of losing them

