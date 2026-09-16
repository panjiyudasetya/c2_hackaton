---
id: github:teqplay/vesselvoyage-backend:pr:530
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 530
title: Added Model, dataSource, Service and Controller for correct timestamps
author: Francisco-teqplay
state: closed
date: '2025-06-08'
merged_at: '2025-08-08'
base_branch: develop
head_branch: TCC-110-Set-up-database-of-correct-timestamps
url: https://github.com/teqplay/vesselvoyage-backend/pull/530
labels: []
linked_issues: []
explicit_links: []
---
# PR #530: Added Model, dataSource, Service and Controller for correct timestamps

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/530  
**State:** closed | **Author:** Francisco-teqplay  
**Base ← Head:** `develop` ← `TCC-110-Set-up-database-of-correct-timestamps`  
**Created:** 2025-06-08  
**Merged:** 2025-08-08  

## Description

Added Model, DataSource, Service and Controller for correct timestamps.

Delete an specific entry is giving a 401 error but getting the same entry is a 200, don't know if it is a configuration problem or not.

## Commits

- `e1826a61` **Francisco** (2025-06-08): Added Model, dataSource, Service and Controller for correct timestamps
- `4f9207dc` **Francisco** (2025-06-11): Updated model with random _id
- `47ca11d0` **Francisco** (2025-06-11): Format and removed unused imports
- `1c2cc97f` **Francisco-teqplay** (2025-06-17): Merge branch 'develop' into TCC-110-Set-up-database-of-correct-timestamps
- `46a6839b` **Francisco** (2025-07-16): Code review request changes applied
- `d1e1e12d` **Francisco** (2025-07-16): Removed unused imports
- `20fb31ea` **Francisco-teqplay** (2025-07-16): Merge branch 'develop' into TCC-110-Set-up-database-of-correct-timestamps
- `b1620133` **Francisco** (2025-07-25): Code review changes
- `f5714d19` **Francisco** (2025-07-31): Added @ProfileProcessing and removed unused imports
- `e319c6fd` **Francisco-teqplay** (2025-07-31): Merge branch 'develop' into TCC-110-Set-up-database-of-correct-timestamps
- `d67d57ef` **Francisco** (2025-08-01): Merge branch 'TCC-110-Set-up-database-of-correct-timestamps' of https://github.com/teqplay/vesselvoyage-backend into TCC-110-Set-up-database-of-correct-timestamps
- `2cf61601` **Darius Wattimena** (2025-08-07): Adjustments in code to reflect decided model and minor code clean up

## Reviews

### leonjoosse — CHANGES_REQUESTED (2025-06-23)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-16)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-16)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-16)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-16)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-16)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-21)

## Pull Request Overview

This PR introduces a complete CRUD implementation for managing correct timestamps in a vessel voyage system. The implementation follows a standard layered architecture pattern with model, data source, service, and controller components.

Key changes:
- Adds a new `CorrectTimestamps` data model with UUID-based identification and timestamp management
- Implements MongoDB data access layer with basic CRUD operations
- Creates a service layer that delegates to the data source
- Provides REST API endpoints for creating, reading, and deleting timestamp entries

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 6 comments.

| File | Description |
| ---- | ----------- |
| CorrectTimestamps.kt | Defines the data model with ID, visit ID, event type, and expected timestamps |
| CorrectTimestampsDataSource.kt | Implements MongoDB operations for CRUD functionality |
| CorrectTimestampsService.kt | Service layer that delegates operations to the data source |
| ProcessingCorrectTimestampsController.kt | REST controller providing HTTP endpoints for timestamp management |

### leonjoosse — CHANGES_REQUESTED (2025-07-21)

_No comment._

### leonjoosse — CHANGES_REQUESTED (2025-07-29)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-31)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-31)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-31)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-31)

_No comment._

### Francisco-teqplay — COMMENTED (2025-07-31)

_No comment._

### leonjoosse — DISMISSED (2025-08-05)

_No comment._

### Darius-Wattimena — APPROVED (2025-08-07)

_No comment._

## Review Comments

### leonjoosse — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

For a POST endpoint, we usually return the created object fully. An object usually has an `_id` or `id` field, which is then populated in the response, allowing the endpoint caller to do something with it.
Also, a String with an explanation should not be needed, returning 200 OK already indicates the action succeeded.

### leonjoosse — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Could also use  `throw NotFoundException()` here, Spring framework will translate that to a 404 Not Found response.
Additionally, the code can then look a bit cleaner:

```
@GetMapping("/{id}")
fun getEntryById(@PathVariable id: String): CorrectTimestamps { // <-- also note the return type changing
    timestampsService.getEntryById(id)
        ?: throw NotFoundException("Entry with this id does not exist")
}
```

### leonjoosse — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

A String with an explanation should not be needed, returning `200 OK` already indicates the action succeeded. 
Additionally for "Entry deleted", when applications are communicating with each other, we should use things that they understand. This String tells something useful to a human, but not to a machine. (although you could program it to expect this exact String, but the 200 OK already covers it).

### leonjoosse — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/CorrectTimestamps.kt`

What kind of category is this? A ship? Would be nice to place a comment, or add a bit more context to the variable name.
```
/** Ship category */
val category: String,
```

### leonjoosse — 2025-06-12 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/CorrectTimestampsService.kt`

The `@Profile...` annotations are different from the other classes, please check which one you need.

### leonjoosse — 2025-06-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/CorrectTimestamps.kt`

What does this class actually mean? And how is it related to 'A minimal version of NewVisit'? It would be helpful to the next reader to explain what is meant here and what it's used for.

### Francisco-teqplay — 2025-07-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Changed, now it returns the created object.

### Francisco-teqplay — 2025-07-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Used the code you added to the comment

### Francisco-teqplay — 2025-07-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Removed the string, now it just returns a 200

### Francisco-teqplay — 2025-07-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/CorrectTimestamps.kt`

Changed a bit the naming of the fields, now they are:
visitId instead of entryId
eventType instead of category

### Francisco-teqplay — 2025-07-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/CorrectTimestamps.kt`

This was a remnant of the class where I had a few different options, I removed this as it doesnt make sense anymore

### Copilot — 2025-07-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/CorrectTimestampsService.kt`

The service class lacks documentation explaining its purpose and responsibility. Add a class-level comment or KDoc describing what this service does and how it relates to the correct timestamps functionality.

### Copilot — 2025-07-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/CorrectTimestamps.kt`

The data class lacks documentation explaining the purpose of the model and the meaning of its fields, especially the relationship between visitId, eventType, and expectedTimestamps.

### Copilot — 2025-07-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/CorrectTimestampsDataSource.kt`

The data source class lacks documentation explaining its responsibility as the data access layer for correct timestamps and the MongoDB collection it manages.

### Copilot — 2025-07-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

The controller class lacks documentation explaining its purpose as the REST API for managing correct timestamps and the endpoints it provides.

### Copilot — 2025-07-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

The return type ResponseEntity<Any> is too generic. For a delete operation, it should be ResponseEntity<Unit> or ResponseEntity<Void> to clearly indicate no content is returned.
```suggestion
    fun deleteEntry(@PathVariable id: String): ResponseEntity<Void> {
```

### leonjoosse — 2025-07-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Looking good, we could improve it even further:

`ResponseEntity` is mostly used when we need to do other than just returning the object. For instance, we need to stream the data instead of giving it back in one go.

So for this method, we could just return the item:

```
    @PostMapping
    fun createEntry(@RequestBody entry: CorrectTimestamps): CorrectTimestamps {
        return timestampsService.createEntry(entry)
    }
```

### leonjoosse — 2025-07-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

I would suggest to remove the `ResponseEntity` entirely:

```
fun deleteEntry(@PathVariable id: String) {
    val deleted = timestampsService.deleteEntry(id)
    if (!deleted) {
        throw NotFoundException(...)
    }
}
```

### leonjoosse — 2025-07-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Which backend should this run on? On the `processing` or the `api` backend? 
I'm asking because the controllers on the `processing` backend are in this `nl.teqplay.vesselvoyage.controller.processing` package (folder), but the class now got the `@ProfileApi` annotation?

### leonjoosse — 2025-07-29 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/CorrectTimestampsService.kt`

Looks like an unnecessary import, should be removed.

IntelliJ can help here by automating it: when committing code, there is a checkbox 'Optimize imports'. If enabled, IntelliJ will remove any unused imports of the classes that are touched by the commit.

### Francisco-teqplay — 2025-07-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Changed to @ProfileProcessing

### Francisco-teqplay — 2025-07-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/CorrectTimestampsService.kt`

Removed unused imports

### Francisco-teqplay — 2025-07-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Used the proposed code

### Francisco-teqplay — 2025-07-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingCorrectTimestampsController.kt`

Used the proposed code

### Francisco-teqplay — 2025-07-31 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/CorrectTimestampsService.kt`

Used @ProfileProcessing as discussed
