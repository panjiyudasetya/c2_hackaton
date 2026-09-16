---
id: github:teqplay/poma-backend:pr:203
source: github
type: pull_request
repo: teqplay/poma-backend
number: 203
title: Fix broken Poma sync
author: Darius-Wattimena
state: closed
date: '2025-09-02'
merged_at: '2025-09-02'
base_branch: develop
head_branch: fix-sync
url: https://github.com/teqplay/poma-backend/pull/203
labels: []
linked_issues: []
explicit_links: []
---
# PR #203: Fix broken Poma sync

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/203  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-sync`  
**Created:** 2025-09-02  
**Merged:** 2025-09-02  

## Description

_No description._

## Commits

- `f552649b` **Darius Wattimena** (2025-09-02): Fixed issue where we potentially could crash the syncing mechanism when corrupt data is provided by a different source
- `b836e05e` **Darius Wattimena** (2025-09-02): Fix confusing comment

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-02)

## Pull Request Overview

This PR fixes synchronization issues in the Poma system by improving the collection replacement mechanism and handling potential race conditions with other Poma backends.

- Refactored the `replaceCollection` method to use collection dropping instead of `deleteMany` for better error handling
- Enhanced duplicate detection in synchronization by deduplicating external models and improving the `hasSameItem` logic
- Improved error handling during collection operations with better exception catching and rollback mechanisms

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| DataSource.kt | Refactored collection replacement to use drop operations and improved error handling with rollback capability |
| DataSourceTest.kt | Updated test to verify drop operations instead of deleteMany and improved test assertion structure |
| InfrastructureService.kt | Enhanced merge logic with performance optimization and improved duplicate detection using ID sets |
| SyncService.kt | Added deduplication of external models to prevent conflicts from other Poma backends |





---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### michel-teqplay — APPROVED (2025-09-02)

_No comment._

## Review Comments

### Copilot — 2025-09-02 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

This line attempts to rename the collection back to the current namespace, but the collection is already at the old namespace. It should rename from oldNamespace to currentNamespace: `database.getCollection(oldNamespace.collectionName, modelClass).renameCollection(currentNamespace)`
```suggestion
            database.getCollection(oldNamespace.collectionName, modelClass).renameCollection(currentNamespace)
```

### Copilot — 2025-09-02 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureService.kt`

The logic is inverted. The method should return true if the item exists in teqplay models, but this returns true when the external model's ID is found in teqplay IDs, which means the item already exists and should be filtered out. The return value should be negated or the logic should be: `return externalModel._id !in teqplayModelsIds`
```suggestion
        return externalModel._id !in teqplayModelsIds
```
