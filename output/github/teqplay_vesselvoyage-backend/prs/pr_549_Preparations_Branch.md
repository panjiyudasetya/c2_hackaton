---
id: github:teqplay/vesselvoyage-backend:pr:549
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 549
title: Preparations Branch
author: TeqJoostD
state: closed
date: '2025-07-03'
merged_at: '2025-07-03'
base_branch: master
head_branch: Fixer-branch
url: https://github.com/teqplay/vesselvoyage-backend/pull/549
labels: []
linked_issues: []
explicit_links: []
---
# PR #549: Preparations Branch

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/549  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `Fixer-branch`  
**Created:** 2025-07-03  
**Merged:** 2025-07-03  

## Description

Before the SPV-1948 merge

## Commits

- `62fb3221` **TeqJoostD** (2025-07-02): feat: add copilot instructions
- `7df6a48b` **TeqJoostD** (2025-07-02): Merge remote-tracking branch 'origin/develop' into develop
- `5289683a` **Joost Dambrink** (2025-07-02): Merge pull request #547 from teqplay/github-instructions
  GitHub instructions
- `1e88fc5c` **TeqJoostD** (2025-07-03): fix

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-03)

## Pull Request Overview

This PR prepares for the SPV-1948 merge by adding JSON alias mappings to the `EncounterType` enum and introducing a new Copilot Code Review Guidelines document.

- Added `@JsonAlias` annotations to map legacy JSON values to the appropriate enum constants.
- Created `.github/copilot-instructions.md` to outline internal code review standards.

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated no comments.

| File                                                          | Description                                                                  |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt | Added `@JsonAlias` annotations for various barge and tug encounter types.     |
| .github/copilot-instructions.md                               | Introduced Copilot Code Review Guidelines in the repository.                 |


<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt:18**
* Add unit tests to verify that deserializing JSON with each new alias (e.g., "BARGE_SUPPLY", "BARGE_PUSH", etc.) correctly maps to the intended enum constant.
```
    @JsonAlias("BARGE_SUPPLY")
```
**.github/copilot-instructions.md:1**
* [nitpick] Reference this new guidelines document from the project's main README or CONTRIBUTING.md so that all contributors can easily find and follow these standards.
```
# Copilot Code Review Guidelines
```
</details>

### Darius-Wattimena — APPROVED (2025-07-03)

Seems fine, but why the preparation?
