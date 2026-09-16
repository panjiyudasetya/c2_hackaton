---
id: github:teqplay/vesselvoyage-backend:pr:551
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 551
title: Temp joost
author: TeqJoostD
state: closed
date: '2025-07-03'
merged_at: '2025-07-03'
base_branch: develop
head_branch: temp-joost
url: https://github.com/teqplay/vesselvoyage-backend/pull/551
labels: []
linked_issues: []
explicit_links: []
---
# PR #551: Temp joost

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/551  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `temp-joost`  
**Created:** 2025-07-03  
**Merged:** 2025-07-03  

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
- `1d8bf089` **TeqJoostD** (2025-07-03): Merge branch 'develop'
  # Conflicts:
  #	api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-03)

## Pull Request Overview

This PR adds JSON alias mappings to several `EncounterType` enum constants to support legacy or alternative JSON values for barge-related events.

- Introduces `@JsonAlias` annotations for various barge encounter types.
- Ensures incoming JSON values like `"BARGE_SUPPLY"` map to `SUPPLY_BARGE`.


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt:19**
* Add unit tests to verify JSON serialization and deserialization for the new @JsonAlias annotations to ensure they map correctly to the enum constants.
```
    @JsonAlias("BARGE_SUPPLY")
```
</details>

### Darius-Wattimena — APPROVED (2025-07-03)

_No comment._
