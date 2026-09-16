---
id: github:teqplay/vesselvoyage-backend:pr:637
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 637
title: Release 14 October
author: TeqJoostD
state: closed
date: '2025-10-14'
merged_at: '2025-10-14'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/637
labels: []
linked_issues: []
explicit_links: []
---
# PR #637: Release 14 October

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/637  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-10-14  
**Merged:** 2025-10-14  

## Description

_No description._

## Commits

- `2383c7ac` **TeqJoostD** (2025-10-14): fix: make sure STS gets merged back when it occurs in voyage
- `313dff25` **Joost Dambrink** (2025-10-14): Merge pull request #636 from teqplay/TCC-438-1
  TCC-438 make sure STS gets merged back when it occurs in voyage

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-14)

## Pull Request Overview

This is a merge PR bringing changes from master into develop branch. The changes enhance the End of Sea Passage (EOSP) processing logic to properly handle ESoF (End of Sea of Flanders) changes when resuming visits.

- Captures the `isNewEsof` flag from the `mergeESoF` function instead of discarding it
- Conditionally creates ESoF changes based on whether the ESoF is new or updated
- Adds deletion of the current voyage's ESoF when resuming a previous visit

## Review Comments

### Copilot — 2025-10-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

[nitpick] The logic for determining ESoF action type could be extracted into a helper function to improve readability and reduce nesting within the listOfNotNull call.
