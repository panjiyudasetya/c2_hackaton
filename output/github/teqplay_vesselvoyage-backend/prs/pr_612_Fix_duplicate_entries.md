---
id: github:teqplay/vesselvoyage-backend:pr:612
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 612
title: Fix duplicate entries
author: Darius-Wattimena
state: closed
date: '2025-09-22'
merged_at: '2025-09-22'
base_branch: develop
head_branch: fix-duplicate-entries
url: https://github.com/teqplay/vesselvoyage-backend/pull/612
labels: []
linked_issues: []
explicit_links: []
---
# PR #612: Fix duplicate entries

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/612  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-duplicate-entries`  
**Created:** 2025-09-22  
**Merged:** 2025-09-22  

## Description

_No description._

## Commits

- `33b6c579` **Darius Wattimena** (2025-09-22): Add test for merging duplicate visits into a single visit
- `b8074ef1` **Darius Wattimena** (2025-09-22): Implement duplicate entry pruning in EntriesMergeService

## Reviews

### michel-teqplay — APPROVED (2025-09-22)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-22)

## Pull Request Overview

Adds de-duplication of incoming new entries (by start/end timestamps) before merge to prevent creating duplicate visits, plus a test validating the behavior.
- Introduces pruneDuplicateNewEntries to strip duplicates (retaining first) prior to merge logic.
- Adds test ensuring two identical new visits collapse into a single merged visit.
- Adjusts merge flow to invoke pruning early.

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt | Adds duplicate-pruning helper and wires it into merge pipeline. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeV2ServiceTest.kt | Adds test case validating duplicate new visits are merged into a single visit. |

## Review Comments

### Copilot — 2025-09-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt`

This helper is now part of the public interface surface (all interface functions are public), potentially leaking an internal mutation utility to API consumers. If not intended as part of the contract, move it to a private/top-level internal function in the implementation, or mark it internal (and keep it out of the interface) to avoid accidental external use.

### Copilot — 2025-09-22 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/merge/EntriesMergeService.kt`

Document that this function mutates the passed list in place and that duplicates are determined solely by (startTime, endTime) ignoring other distinguishing fields (e.g., IDs, port info). Clarifying these side effects and criteria will prevent misuse or incorrect assumptions by future maintainers.
```suggestion
     * Removes duplicate entries from [newEntries] in place, based solely on identical start and end times.
     *
     * This function mutates the passed [newEntries] list directly by removing elements.
     * Duplicates are determined only by the pair (startTime, endTime), ignoring all other fields
     * (such as IDs, port information, etc). Only the first occurrence of each unique (startTime, endTime)
     * pair is kept; subsequent duplicates are removed.
```
