---
id: github:teqplay/vesselvoyage-backend:pr:643
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 643
title: Shuffle post-processing to prevent locking on recurring same imo visi…
author: TeqJoostD
state: closed
date: '2025-10-21'
merged_at: '2025-10-21'
base_branch: master
head_branch: master-post-processing-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/643
labels: []
linked_issues: []
explicit_links: []
---
# PR #643: Shuffle post-processing to prevent locking on recurring same imo visi…

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/643  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `master-post-processing-hotfix`  
**Created:** 2025-10-21  
**Merged:** 2025-10-21  

## Description

…ts/voyages

## Commits

- `429d0a9e` **TeqJoostD** (2025-10-21): Shuffle post-processing to prevent locking on recurring same imo visits/voyages

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-21)

## Pull Request Overview

This PR addresses a locking issue in the post-processing service by introducing randomization. The changes increase the batch size and shuffle the order of post-processable entries to prevent the system from repeatedly attempting to process the same IMO visits/voyages in sequence, which was causing locking problems.

**Key Changes:**
- Increased maximum post-processing batch size from 1,000 to 5,000 entries
- Added shuffling of post-processable entries before processing to randomize the order

### TeqJoostD — COMMENTED (2025-10-21)

_No comment._

### michel-teqplay — APPROVED (2025-10-21)

_No comment._

## Review Comments

### Copilot — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The `shuffled()` operation creates a new shuffled list, which has O(n) time and space complexity. With the batch size increased to 5,000, this could impact performance on every cycle. Consider whether the shuffling is necessary for the entire batch or if a more targeted approach (e.g., randomizing the order at the database level or shuffling only when contention is detected) would be more efficient.
```suggestion
            // Fetch entries in random order to prevent locking mechanism
            val allPostProcessable = dataSource.getBatch(batchSize = MAX_POST_PROCESSING_PER_CYCLE, randomOrder = true)
```

### TeqJoostD — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

shush
