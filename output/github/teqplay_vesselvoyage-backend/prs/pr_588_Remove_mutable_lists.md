---
id: github:teqplay/vesselvoyage-backend:pr:588
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 588
title: Remove mutable lists
author: Darius-Wattimena
state: closed
date: '2025-08-13'
merged_at: '2025-08-13'
base_branch: develop
head_branch: fix-revents
url: https://github.com/teqplay/vesselvoyage-backend/pull/588
labels: []
linked_issues: []
explicit_links: []
---
# PR #588: Remove mutable lists

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/588  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-revents`  
**Created:** 2025-08-13  
**Merged:** 2025-08-13  

## Description

_No description._

## Commits

- `a2a46a13` **Darius Wattimena** (2025-08-13): Revent back the usa of mutable lists and instead update the visit directly with a copy function

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-13)

## Pull Request Overview

This PR refactors the codebase to remove mutable lists by replacing `MutableList<AreaActivity>` with immutable `List<AreaActivity>` throughout the activity processing system. The change promotes immutability and functional programming practices while maintaining the same functionality.

Key changes:
- Replaced mutable list operations with immutable list operations in utility functions
- Updated all activity fields in `NewVisit` model from `MutableList` to `List`
- Added explicit `updateVisitWithActivities` implementations to each processor class

### Reviewed Changes

Copilot reviewed 11 out of 11 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| AreaActivityUtils.kt | Refactored `replaceFirst` extension function to work with immutable lists and return new list instances |
| NewVisit.kt | Changed all activity list fields from `MutableList` to `List` with empty list defaults |
| ActivityEventProcessor.kt | Updated abstract class to use immutable lists and made `updateVisitWithActivities` abstract |
| Multiple processor files | Added concrete implementations of `updateVisitWithActivities` using data class copy operations |

### TeqJoostD — APPROVED (2025-08-13)

_No comment._

### Darius-Wattimena — COMMENTED (2025-08-13)

_No comment._

### TeqJoostD — COMMENTED (2025-08-13)

_No comment._

## Review Comments

### Copilot — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/AreaActivityUtils.kt`

The call to `toList()` is unnecessary here. Both `newList.sortedBy()` and `newList` already return immutable List instances, so this operation creates an unnecessary copy.
```suggestion
        newList.toList()
    }

    // Make sure the list is back to an immutable list
    return sortedList
```

### Darius-Wattimena — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/AreaActivityUtils.kt`

No you are wrong! 😠 

### TeqJoostD — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/AreaActivityUtils.kt`

Stupid clanker
