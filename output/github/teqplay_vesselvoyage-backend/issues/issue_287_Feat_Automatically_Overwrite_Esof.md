---
id: github:teqplay/vesselvoyage-backend:issue:287
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 287
title: Feat/Automatically Overwrite Esof
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/287
labels: []
explicit_links: []
---
# Issue #287: Feat/Automatically Overwrite Esof

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/287  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [480177f7d7ab...a97fd5d223d4](https://github.com/teqplay/vesselvoyage-backend/compare/480177f7d7ab...a97fd5d223d4)
**Merge commit:** [a97fd5d223d4](https://github.com/teqplay/vesselvoyage-backend/commit/a97fd5d223d4)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/automatically-overwrite-esof](https://github.com/teqplay/vesselvoyage-backend/tree/feat/automatically-overwrite-esof)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-07-23T11:52:35.847293+00:00
**Status:** MERGED

Previously once \(r\)events had run without encounters, you’d need to request `POST /v2/recalculate/ship/{imo}/overwriteESoFsForEncounters` for every ship, overwriting their ESOFs.
This endpoint is kept, but now the overwrite is also automatically called after the merge is performed. This makes it a lot easier to “just” run \(r\)events and VesselVoyage will make sure the merge happens, and if encounters are missing the ESOF is also overwritten based on encounters from event-history.

