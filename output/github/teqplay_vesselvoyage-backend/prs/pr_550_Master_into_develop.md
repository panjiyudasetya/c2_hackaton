---
id: github:teqplay/vesselvoyage-backend:pr:550
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 550
title: Master into develop
author: TeqJoostD
state: closed
date: '2025-07-03'
merged_at: null
base_branch: develop
head_branch: master
url: https://github.com/teqplay/vesselvoyage-backend/pull/550
labels: []
linked_issues: []
explicit_links: []
---
# PR #550: Master into develop

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/550  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `master`  
**Created:** 2025-07-03  

## Description

_No description._

## Commits

- `0f7e3c35` **Darius Wattimena** (2025-06-25): Merge pull request #543 from teqplay/develop
  Release 25 Jun 2025
- `48b8dd8b` **Leon Joosse** (2025-07-01): Merge pull request #546 from teqplay/develop
  Release 1 July 2025
- `1e88fc5c` **TeqJoostD** (2025-07-03): fix
- `06206b08` **Joost Dambrink** (2025-07-03): Merge pull request #549 from teqplay/Fixer-branch
  Preparations Branch

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-03)

## Pull Request Overview

This PR merges updates from `master` into `develop` and adds Jackson `@JsonAlias` annotations to the `EncounterType` enum to support new JSON field names for various barge and tug encounter types.

- Added `@JsonAlias` annotations for all `BARGE_*` variants and the tug departure type.
- Imported `JsonAlias` from Jackson.


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt:18**
* Add unit tests to verify that Jackson correctly deserializes the new JSON alias values into the corresponding enum constants.
```
    @JsonAlias("BARGE_SUPPLY")
```
</details>

### Darius-Wattimena — APPROVED (2025-07-03)

_No comment._
