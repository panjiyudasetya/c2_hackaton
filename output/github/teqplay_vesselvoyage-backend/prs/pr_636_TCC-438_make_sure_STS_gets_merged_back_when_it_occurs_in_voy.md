---
id: github:teqplay/vesselvoyage-backend:pr:636
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 636
title: TCC-438 make sure STS gets merged back when it occurs in voyage
author: TeqJoostD
state: closed
date: '2025-10-14'
merged_at: '2025-10-14'
base_branch: develop
head_branch: TCC-438-1
url: https://github.com/teqplay/vesselvoyage-backend/pull/636
labels: []
linked_issues: []
explicit_links: []
---
# PR #636: TCC-438 make sure STS gets merged back when it occurs in voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/636  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-438-1`  
**Created:** 2025-10-14  
**Merged:** 2025-10-14  

## Description

_No description._

## Commits

- `2383c7ac` **TeqJoostD** (2025-10-14): fix: make sure STS gets merged back when it occurs in voyage

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-14)

## Pull Request Overview

This PR fixes an issue where STS (Ship-to-Ship) transfers were not being properly merged back when they occurred during a voyage, specifically in the End of Sea Passage (EOSP) processing logic.

Key changes:
- Modified the merging logic to capture and use the `isNewEsof` flag from the `mergeESoF` function
- Updated the changes list to properly handle ESoF (End of Sea Passage File) creation, updates, and deletions based on the merge result
- Added deletion of the current voyage's ESoF when resuming a previous visit

### Darius-Wattimena — APPROVED (2025-10-14)

_No comment._

## Review Comments

### Copilot — 2025-10-14 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

[nitpick] The ESoF action logic is duplicated within the `listOfNotNull` call. Consider extracting this into a separate function or variable to improve readability and reduce complexity.
