---
id: github:teqplay/poma-backend:pr:199
source: github
type: pull_request
repo: teqplay/poma-backend
number: 199
title: TCC-285 fix syncing
author: Darius-Wattimena
state: closed
date: '2025-07-24'
merged_at: '2025-08-07'
base_branch: develop
head_branch: TCC-285-fix-syncing
url: https://github.com/teqplay/poma-backend/pull/199
labels: []
linked_issues: []
explicit_links:
- jira:TCC-285
---
# PR #199: TCC-285 fix syncing

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/199  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-285-fix-syncing`  
**Created:** 2025-07-24  
**Merged:** 2025-08-07  

## Description

_No description._

## Commits

- `dc188ced` **Darius Wattimena** (2025-07-24): Refactor sync logic to improve readability
- `19b3e239` **Darius Wattimena** (2025-07-24): Added better error handling for syncing mechanism
- `82db4453` **Darius Wattimena** (2025-07-24): Add unit tests to ensure replacing of collections behave as expected
- `89d268fc` **Darius Wattimena** (2025-07-24): Adjusted code so we instead always clear the collection instead of dropping it
- `a0ab1449` **Darius Wattimena** (2025-07-24): ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-24)

## Pull Request Overview

This PR improves the robustness of the syncing functionality by adding comprehensive error handling and logging to the collection replacement process. The changes focus on making the `replaceCollection` method more resilient to failures and providing better observability.

- Adds extensive error handling with try-catch blocks around critical database operations
- Implements proper cleanup of temporary collections when operations fail
- Enhances logging to track sync operations and failures

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| DataSource.kt | Adds error handling, logging, and temporary collection cleanup to `replaceCollection` method |
| SyncService.kt | Refactors sync call to use named parameters and extract sync time to a variable |

### TeqJoostD — CHANGES_REQUESTED (2025-07-24)

Please add tests, this is very important code

### TeqJoostD — COMMENTED (2025-07-24)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-24)

## Pull Request Overview

This PR improves the reliability of the synchronization process by adding comprehensive error handling to the `replaceCollection` method in the DataSource class. The changes ensure that collection replacement operations fail gracefully without breaking the entire sync process.

- Enhanced error handling with try-catch blocks around critical MongoDB operations
- Added explicit clearing of temporary collections before inserting new data
- Improved code readability in the sync service with extracted variables

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt | Added error handling, logging, and explicit temp collection clearing to replaceCollection method |
| src/main/kotlin/nl/teqplay/poma/feature/synchronize/SyncService.kt | Extracted variables for better readability and added named parameter |
| src/test/kotlin/nl/teqplay/poma/generics/DataSourceTest.kt | Added comprehensive test coverage for error scenarios in replaceCollection method |


<details>
<summary>Comments suppressed due to low confidence (3)</summary>

**src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt:98**
* [nitpick] The error message could be more specific about the actual failure. Consider including the exception type or a brief description of what operation failed (e.g., 'Failed to insert items into temporary collection' vs 'Failed to clear temporary collection').
```
            logger.error(ex) { "Failed to insert items into temporary collection $tempCollectionName, dropping collection" }
```
**src/test/kotlin/nl/teqplay/poma/generics/DataSourceTest.kt:88**
* The test only verifies that no exception is thrown, but doesn't assert that the error was handled properly (e.g., logged or that the original collection remains unchanged). Consider adding assertions to verify the expected error handling behavior.
```
        // Should not throw
```
**src/test/kotlin/nl/teqplay/poma/generics/DataSourceTest.kt:101**
* Similar to other error handling tests, this only verifies no exception is thrown but doesn't verify that the temporary collection is properly cleaned up or that appropriate logging occurs.
```
        // Should not throw
```
</details>

### TeqJoostD — APPROVED (2025-07-24)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-24)

Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting a review.

## Review Comments

### Copilot — 2025-07-24 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

After dropping the temporary collection, calling `ensureIndexes()` on the dropped collection reference will fail. You need to get a fresh collection reference from the database before calling `ensureIndexes()`.
```suggestion
                    val freshTempCollection = database.getCollection(tempCollectionName, modelClass).ensureIndexes()
```

### Copilot — 2025-07-24 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

Using `findOne()` to check if a collection exists is inefficient. Consider using `countDocuments()` with a limit of 1, or check if the collection exists using database metadata operations.
```suggestion
                if (tempCollection.countDocuments() > 0) {
```

### Copilot — 2025-07-24 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

[nitpick] The logic for checking and dropping an existing temporary collection should be extracted to a separate method to improve readability and reduce complexity in the main method.
```suggestion
                handleExistingTempCollection(tempCollection, tempCollectionName)
```

### TeqJoostD — 2025-07-24 on `src/main/kotlin/nl/teqplay/poma/generics/DataSource.kt`

This will break
