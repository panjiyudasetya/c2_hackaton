---
id: github:teqplay/portreporter-backend:issue:1046
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1046
title: Pilot Fallback Explicit
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1046
labels: []
explicit_links: []
---
# Issue #1046: Pilot Fallback Explicit

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1046  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [680a6f3343dc...dc7c2113c62d](https://github.com/teqplay/portreporter-backend/compare/680a6f3343dc...dc7c2113c62d)
**Merge commit:** [dc7c2113c62d](https://github.com/teqplay/portreporter-backend/commit/dc7c2113c62d)
**Author:** Wouter Naloop
**Reviewers:** Joost Laurman, Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella, Joost Laurman
**Source Branch:** [feat/pilot_fallback_event](https://github.com/teqplay/portreporter-backend/tree/feat/pilot_fallback_event)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-02-18T12:57:12.325642+00:00
**Status:** MERGED

Rename the pilotboarding place atae to pilotonboard fallback, this is how it is always used inside portreporter.
This is not in line with the intentions of platform. 
Added a probably sea pilot on board message if it is based on the fallback

