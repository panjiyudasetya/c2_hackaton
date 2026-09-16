---
id: github:teqplay/vesselvoyage-backend:pr:527
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 527
title: TCC-147 catch write exceptions
author: Darius-Wattimena
state: closed
date: '2025-06-04'
merged_at: '2025-06-27'
base_branch: develop
head_branch: TCC-147-catch-write-exceptions
url: https://github.com/teqplay/vesselvoyage-backend/pull/527
labels: []
linked_issues: []
explicit_links: []
---
# PR #527: TCC-147 catch write exceptions

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/527  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-147-catch-write-exceptions`  
**Created:** 2025-06-04  
**Merged:** 2025-06-27  

## Description

_No description._

## Commits

- `f4e98545` **Darius Wattimena** (2025-06-04): Make sure to also persist other changes when an insert exception happened
- `07e3f1c1` **Darius Wattimena** (2025-06-04): Adjusted trace inserting to be an upsert instead
- `614cc18f` **Darius Wattimena** (2025-06-06): Adjust persisting of changes to be bulk writes instead
- `21a8ba1c` **Darius Wattimena** (2025-06-11): Update log level to debug
- `6f156f5e` **Darius Wattimena** (2025-06-11): Added some more explanation why we do a replace after the insert fails
- `0cbe382f` **Darius Wattimena** (2025-06-11): Merge branch 'develop' into TCC-147-catch-write-exceptions
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt
- `b9ef4a10` **Darius Wattimena** (2025-06-11): Merge branch 'master' into TCC-147-catch-write-exceptions
- `31ff00ac` **Darius Wattimena** (2025-06-12): Merge branch 'develop' into TCC-147-catch-write-exceptions
- `f74d7095` **Darius Wattimena** (2025-06-16): Lock the full ship once instead of doing multiple lockings
- `f5c6f5a0` **Darius Wattimena** (2025-06-20): Merge branch 'develop' into TCC-147-catch-write-exceptions
- `64d46804` **Darius Wattimena** (2025-06-20): Catch exceptions during old definition processing to prevent failures for V2
- `843698e2` **Darius Wattimena** (2025-06-20): Added some extra comments
- `ecd05f4b` **Darius Wattimena** (2025-06-20): Adjusted some of the naming and rewrite persisting of the changes so we avoid having to cast
- `1a88f033` **Darius Wattimena** (2025-06-20): ktlint
- `81571ada` **Darius Wattimena** (2025-06-27): Merge branch 'develop' into TCC-147-catch-write-exceptions
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt
- `5c1f5cbd` **Darius Wattimena** (2025-06-27): Removed unneeded extra replacing of entries when fixing stops

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-06-10)

## Pull Request Overview

This PR modifies the data persistence and testing strategies to better handle write exceptions and to consolidate insert and update operations. Key changes include:
- Replacing direct insert calls with insertOrUpdate throughout the code, including tests.
- Refactoring PersistChangesService to group changes by type and using bulkWrite instead of individual create/replace methods.
- Removing PersistChangesServiceTest and updating related tests to work with the new persistence API.

### Reviewed Changes

Copilot reviewed 13 out of 13 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| ProcessingTraceServiceTest.kt | Updated verification to use insertOrUpdate calls. |
| PersistChangesServiceTest.kt | Entire file removed; tests are expected to be covered elsewhere. |
| ProcessingTraceService.kt | Modified insertion calls to use insertOrUpdate with an accompanying comment for rationale. |
| PostProcessingService.kt | Adjusted call from persistChange to persistChanges with a list parameter. |
| PersistChangesService.kt | Refactored persistence logic to group changes and use bulkWrite rather than individual operations. |
| EntryProcessingService.kt | Updated to persist all changes in bulk before processing trace changes. |
| BulkWriteUtils.kt | Added new helper for bulk write operations, sorting deletions first. |
| NewTraceDataSource.kt, NewEntryDataSource.kt, NewESoFDataSource.kt | Updated data source methods to support bulk write and insertOrUpdate. |
| NewEntry.kt, NewESoF.kt, EntryDatabaseObject.kt | Updated model interfaces to align with new persistence strategy. |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/service/PersistChangesServiceTest.kt:1**
* The removal of PersistChangesServiceTest reduces the direct test coverage for the persistChange(s) logic. Please ensure that the new bulkWrite grouping functionality in PersistChangesService is adequately covered by other tests.
```
Entire file removed
```
**src/main/kotlin/nl/teqplay/vesselvoyage/service/PersistChangesService.kt:24**
* Grouping changes by their runtime class and throwing an IllegalArgumentException for unsupported change classes may lead to unexpected runtime errors if a new change type is introduced. Consider adding a more graceful handling mechanism or logging a detailed error before throwing.
```
val changesGroupedByChangeClass = changes.groupBy { it::class }
```
</details>

### leonjoosse — CHANGES_REQUESTED (2025-06-10)

Small thingy that can be removed

### Darius-Wattimena — COMMENTED (2025-06-11)

_No comment._

### TeqJoostD — COMMENTED (2025-06-11)

_No comment._

### TeqJoostD — COMMENTED (2025-06-11)

_No comment._

### leonjoosse — COMMENTED (2025-06-12)

_No comment._

### leonjoosse — APPROVED (2025-06-27)

_No comment._

## Review Comments

### leonjoosse — 2025-06-10 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt`

You may as well remove the `dataSource.replace(newTrace)` below, that's never going to be run again because of the upsert

### Darius-Wattimena — 2025-06-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt`

Not really, here replace is not doing an upsert, while in the save it does the following:
```kotlin
fun <T : Any> MongoCollection<T>.save(document: T) {
    val id = MongoIdUtil.getIdValue(document)
    if (id != null) {
        replaceOneById(id, document, ReplaceOptions().upsert(true))
    } else {
        insertOne(document)
    }
}
```

This means we have to do the replace still if we decided to do an insert, but end up with a insert error. As it can happen that meanwhile we got a trace for this ship by generating it by ShipHistory which can happen in concurrent.

### TeqJoostD — 2025-06-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/util/BulkWriteUtils.kt`

Please add comment 
🙏

### TeqJoostD — 2025-06-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/util/BulkWriteUtils.kt`

![image](https://github.com/user-attachments/assets/bf0da54c-ef4a-4587-9470-39d917e4c75d)


### leonjoosse — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceService.kt`

Ah good point! Never mind then 
