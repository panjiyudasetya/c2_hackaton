---
id: github:teqplay/vesselvoyage-backend:pr:665
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 665
title: Remove filter for retrieving batches wrongfully
author: TeqJoostD
state: closed
date: '2025-11-11'
merged_at: '2025-11-11'
base_branch: develop
head_branch: TTC-526
url: https://github.com/teqplay/vesselvoyage-backend/pull/665
labels: []
linked_issues: []
explicit_links: []
---
# PR #665: Remove filter for retrieving batches wrongfully

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/665  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TTC-526`  
**Created:** 2025-11-11  
**Merged:** 2025-11-11  

## Description

_No description._

## Commits

- `491adfbc` **TeqJoostD** (2025-11-11): Remove filter for retrieving batches wrongfully

## Reviews

### Darius-Wattimena — APPROVED (2025-11-11)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-11)

Review completed. The change removes the filter that prevented re-processing entries with existing priority fields, which may have performance implications.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-11)

## Pull Request Overview

This PR removes a MongoDB filter that was limiting document retrieval to only those without a `priority` field. The service now processes all documents in the `postProcessable` collection instead of just those missing the priority field.

- Removes the filter `Filters.not(exists("priority"))` from the priority population query
- Cleans up unused imports (`Filters` and `Filters.exists`)
- Changes behavior from selective backfill to full collection processing

## Review Comments

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingPriorityPopulationService.kt`

Removing the filter means this function will now process and update **all** documents in the collection, regardless of whether they already have a priority value set. While the PR title suggests this is intentional, this could have significant performance implications:

1. The function will unnecessarily recalculate priority for documents that already have it set
2. Bulk updates will be performed on all documents every time this endpoint is called

Consider:
- If the intent is to recalculate priority for all documents (e.g., because the priority logic changed), the current implementation is correct but the method name and documentation should clarify this is a full recalculation, not just population of missing values
- If the intent is only to populate missing priority values, the filter should be restored or a conditional check should be added to skip documents that already have priority set (e.g., `if (doc.priority == null)`)
