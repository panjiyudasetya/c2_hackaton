---
id: github:teqplay/portreporter-backend:issue:1091
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1091
title: 'Prp-1003 : Consider Also Updating Nominations By The Queue.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1091
labels: []
explicit_links: []
---
# Issue #1091: Prp-1003 : Consider Also Updating Nominations By The Queue.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1091  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [d2af8da235d5...5a9428ed1c66](https://github.com/teqplay/portreporter-backend/compare/d2af8da235d5...5a9428ed1c66)
**Merge commit:** [5a9428ed1c66](https://github.com/teqplay/portreporter-backend/commit/5a9428ed1c66)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop, Berend
**Approvers:** Berend
**Source Branch:** [PRP-1003/feat/match_nomination_by_ext_ref](https://github.com/teqplay/portreporter-backend/tree/PRP-1003/feat/match_nomination_by_ext_ref)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-05-18T13:43:09.413779+00:00
**Status:** MERGED

This PR enables the Nomination Message Handler to decide whether creating or updating nominations based on the nomination’s reference or eta margin \(±10 days - configurable\).

Also, I took the opportunity to make the handling more simple: easier to read and extend.

