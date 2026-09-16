---
id: github:teqplay/poma-backend:pr:206
source: github
type: pull_request
repo: teqplay/poma-backend
number: 206
title: Fix syncing
author: Darius-Wattimena
state: closed
date: '2025-09-04'
merged_at: '2025-09-04'
base_branch: develop
head_branch: speed-up-sync
url: https://github.com/teqplay/poma-backend/pull/206
labels: []
linked_issues: []
explicit_links: []
---
# PR #206: Fix syncing

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/206  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `speed-up-sync`  
**Created:** 2025-09-04  
**Merged:** 2025-09-04  

## Description

_No description._

## Commits

- `c509ee55` **Darius Wattimena** (2025-09-02): Adjust the way how we check if items are the same by doing all the id checks before doing any area overlap check
- `5590e231` **Darius Wattimena** (2025-09-02): ktlint
- `407abddc` **Darius Wattimena** (2025-09-04): Adjusted replace collection code so it can't crash
- `9dde0415` **Darius Wattimena** (2025-09-04): Adjusted override of collection so they compile again
- `5da1e08d` **Darius Wattimena** (2025-09-04): ktlint
- `c0e997bc` **Darius Wattimena** (2025-09-04): fix broken tests
- `e186ec9a` **Darius Wattimena** (2025-09-04): ktlint
- `22963bb3` **Darius Wattimena** (2025-09-04): Refactor collection property to be immutable in datasource again
- `23d00d70` **Darius Wattimena** (2025-09-04): Fixed tests to the mocking is done correctly
- `e5f0a3f7` **Darius Wattimena** (2025-09-04): Test clean up
- `d174047c` **Darius Wattimena** (2025-09-04): ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-04)

## Pull Request Overview

This PR fixes issues with the syncing mechanism by improving the model comparison logic and refactoring collection handling. The changes optimize the duplicate detection process and make the temporary collection management more reliable.

- Adds early-exit checks for ID and uniqueId matching to improve performance
- Refactors temporary collection creation to use a centralized helper method
- Updates collection reference management during the rename operation

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| InfrastructureService.kt | Optimizes the `hasSameItem` method with early returns and improved parameter passing |
| DataSource.kt | Refactors temporary collection handling and fixes collection reference updating |





---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

### Jamie-de-Leest — APPROVED (2025-09-04)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-04)

## Pull Request Overview

This PR refactors the synchronization logic for data models to fix issues with collection replacement and improve duplicate detection during sync operations.

- Optimizes duplicate detection by checking `_id` and `uniqueId` matches before expensive overlap calculations
- Removes lazy initialization from collection properties to fix collection reference issues during rename operations
- Refactors test setup to use shared mock configuration and improve test isolation

### Reviewed Changes

Copilot reviewed 16 out of 16 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/poma/generics/InfrastructureService.kt | Optimizes `hasSameItem` method by checking ID matches before overlap calculations |
| src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt | Fixes collection reference issues in `replaceCollection` by using fresh collection instances |
| src/test/kotlin/nl/teqplay/poma/generics/DataSourceTest.kt | Refactors test setup to use shared mock configuration and proper initialization |
| src/test/kotlin/nl/teqplay/poma/Mocks.kt | Adds namespace mock to MongoDB collection mock |
| Multiple AbstractDatasource files | Removes lazy initialization from collection properties |
</details>






---

<sub>**Tip:** Customize your code reviews with copilot-instructions.md. <a href="/teqplay/poma-backend/new/develop/.github?filename=copilot-instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Create the file</a> or <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">learn how to get started</a>.</sub>

## Review Comments

### Copilot — 2025-09-04 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

Changing the collection property from `val` to `var` breaks immutability and could lead to unexpected behavior if the collection reference is modified externally. Consider using a private backing field with a public getter or a method to update the collection reference instead.
```suggestion
    abstract val collection: MongoCollection<T>
```

### Copilot — 2025-09-04 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

The `getTempCollection()` method should handle potential exceptions when creating the collection, similar to the original try-catch block that was removed. This could cause failures that were previously handled gracefully.
```suggestion
        try {
            val currentNamespace = collection.namespace
            val tempCollectionName = currentNamespace.collectionName + "_temp"
            return database.getCollection(tempCollectionName, modelClass)
        } catch (ex: Exception) {
            logger.error(ex) { "Failed to get temporary collection for ${collection.namespace.collectionName}" }
            throw ex
        }
```

### Copilot — 2025-09-04 on `src/main/kotlin/nl/teqplay/poma/generics/InfrastructureService.kt`

[nitpick] Consider using positional arguments instead of named arguments for this function call since the parameter names are clear from the function signature and this would reduce verbosity.
```suggestion
                    externalModel,
                    teqplayModels,
                    teqplayModelsIds,
                    teqplayModelsUniqueIds,
```

### Copilot — 2025-09-04 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

[nitpick] The chained method calls should be formatted consistently. Either put all methods on the same line or consistently break each method call to a new line.
