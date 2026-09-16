---
id: github:teqplay/vesselvoyage-backend:pr:546
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 546
title: Release 1 July
author: leonjoosse
state: closed
date: '2025-07-01'
merged_at: '2025-07-01'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/546
labels: []
linked_issues: []
explicit_links: []
---
# PR #546: Release 1 July

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/546  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-07-01  
**Merged:** 2025-07-01  

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
- `8b8477a1` **leonj** (2025-06-18): Publish PortReporter SOFView via RabbitMQ in the ChangesPublisherService.
- `0dc98465` **leonj** (2025-06-20): Give our RabbitMQ outgoing change sender a more descriptive name
- `bc1f6a67` **leonj** (2025-06-20): Merge branch 'develop' into TCC-138-prp-sof-rabbitmq
- `254abf3b` **Leon Joosse** (2025-06-20): Merge branch 'develop' into TCC-138-prp-sof-rabbitmq
- `f5c6f5a0` **Darius Wattimena** (2025-06-20): Merge branch 'develop' into TCC-147-catch-write-exceptions
- `64d46804` **Darius Wattimena** (2025-06-20): Catch exceptions during old definition processing to prevent failures for V2
- `843698e2` **Darius Wattimena** (2025-06-20): Added some extra comments
- `ecd05f4b` **Darius Wattimena** (2025-06-20): Adjusted some of the naming and rewrite persisting of the changes so we avoid having to cast
- `1a88f033` **Darius Wattimena** (2025-06-20): ktlint
- `d8bcb2aa` **Leon Joosse** (2025-06-25): Merge branch 'develop' into TCC-138-prp-sof-rabbitmq
- `81571ada` **Darius Wattimena** (2025-06-27): Merge branch 'develop' into TCC-147-catch-write-exceptions
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewEntryDataSource.kt
- `5c1f5cbd` **Darius Wattimena** (2025-06-27): Removed unneeded extra replacing of entries when fixing stops
- `29df398e` **Darius Wattimena** (2025-06-27): Merge pull request #527 from teqplay/TCC-147-catch-write-exceptions
  TCC-147 catch write exceptions
- `c4055f64` **Darius Wattimena** (2025-06-27): Merge pull request #540 from teqplay/TCC-138-prp-sof-rabbitmq
  TCC-138: Publish PortReporter SOF via RabbitMQ
- `eb901f49` **Darius Wattimena** (2025-06-27): Fix an issue where the batch call for traces wasn't correctly mapped to how the client would expect it
- `be60bdf5` **Darius Wattimena** (2025-06-27): Merge pull request #544 from teqplay/fix-api-endpoint
  Fix traces batch call endpoint
- `9b55fd97` **Darius Wattimena** (2025-06-30): Fix the selected pilot inbound to match desired timestamp
- `44405ca3` **Darius Wattimena** (2025-06-30): Merge pull request #545 from teqplay/fix-pilot-on-board
  Fix the selected pilot inbound to be the last before the first berth

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-01)

## Pull Request Overview

This release adds RabbitMQ support alongside NATS for outgoing change publishing, optimizes persistence via bulk database writes, and enhances multi-view StatementOfFacts handling and related logic.

- Introduced `RabbitMqOutgoingChangeSender` and updated `ChangesPublisherService` and tests to send to RabbitMQ with new routing keys and both PTO/PortReporter views.
- Added `bulkWriteChanges` utility and refactored `PersistChangesService`, data sources, and entry/trace services to batch-persist changes.
- Updated pilot selection in `PtoStatementOfFactsViewGenerator`, improved exception handling in `EventsDefaultMessageProcessor`, and adjusted `ProcessingTraceService` insert logic.

### Reviewed Changes

Copilot reviewed 22 out of 22 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File                                                                                 | Description                                                       |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| src/test/kotlin/.../ChangesPublisherServiceTest.kt                                    | Split parameterized tests for NATS and RabbitMQ publishing       |
| src/test/kotlin/.../PtoStatementOfFactsViewGeneratorTest.kt                           | Corrected test comments and expected pilot-selection behavior     |
| src/test/kotlin/.../ProcessingTraceServiceTest.kt                                     | Updated verifications to use `insertOrUpdate` instead of `insert`|
| src/test/kotlin/.../PersistChangesServiceTest.kt                                      | Removed obsolete tests for individual persisted changes           |
| src/test/kotlin/.../ApplicationTest.kt                                               | Injected `RabbitMqOutgoingChangeSender` into `ApplicationTestConfig` |
| src/main/kotlin/.../ProcessingTraceService.kt                                        | Switched from `insert` to `insertOrUpdate` for trace persistence  |
| src/main/kotlin/.../ReventsRecalculationService.kt                                    | Moved `forEach` inside `imoLockService.executeBlocking`           |
| src/main/kotlin/.../EventsDefaultMessageProcessor.kt                                  | Wrapped old-definition processing in try/catch to log and continue |
| src/main/kotlin/.../publisher/RabbitMqOutgoingChangeSender.kt                         | New RabbitMQ sender component                                    |
| src/main/kotlin/.../publisher/ChangesPublisherService.kt                              | Wire up RabbitMQ sender, update routing key format, add multi-SOF views |
| src/main/kotlin/.../api/PtoStatementOfFactsViewGenerator.kt                           | Changed pilot encounter selection from first to last before berth |
| src/main/kotlin/.../PostProcessingService.kt                                          | Updated call from `persistChange` to `persistChanges`             |
| src/main/kotlin/.../PersistChangesService.kt                                         | Refactored to batch-persist changes via `bulkWriteChanges`        |
| src/main/kotlin/.../EntryProcessingService.kt                                        | Call `persistChanges` once before iterating change-by-change      |
| src/main/kotlin/.../datasource/util/BulkWriteUtils.kt                                 | New bulk-write utility with sorted operations                    |
| src/main/kotlin/.../datasource/NewTraceDataSource.kt                                  | Removed raw `insert`, added `insertOrUpdate`                      |
| src/main/kotlin/.../datasource/NewEntryDataSource.kt                                  | Added `bulkWriteChanges`, removed individual create/replace methods |
| src/main/kotlin/.../datasource/NewESoFDataSource.kt                                   | Exposed collection and added `bulkWriteChanges`                   |
| src/main/kotlin/.../controller/api/ApiTraceV2Controller.kt                            | Changed POST path to `/ids`                                       |
| api/src/main/kotlin/.../model/v2/NewEntry.kt                                         | Made `NewEntry` extend `EntryDatabaseObject`                      |
| api/src/main/kotlin/.../model/v2/NewESoF.kt                                           | Made `NewESoF` extend `EntryDatabaseObject`                       |
| api/src/main/kotlin/.../model/v2/EntryDatabaseObject.kt                               | New interface for entries with `_id`                              |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>

**src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiTraceV2Controller.kt:64**
* [nitpick] Changing the POST endpoint path from the default mapping to `/ids` is a breaking change for API consumers; consider deprecating the old path or adding a versioned alias.
```
    @PostMapping("/ids")
```

</details>

### leonjoosse — COMMENTED (2025-07-01)

_No comment._

## Review Comments

### Copilot — 2025-07-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/util/BulkWriteUtils.kt`

The sort predicate `sortedBy { action is DeleteOneModel }` places delete operations last, opposite the intended comment. To process deletes first, use `sortedByDescending { it is DeleteOneModel }` or invert the predicate.
```suggestion
    val sortedWrites = preparedWrites.sortedByDescending { action -> action is DeleteOneModel }
```

### leonjoosse — 2025-07-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/util/BulkWriteUtils.kt`

Coordinated, so not an issue at the moment.
