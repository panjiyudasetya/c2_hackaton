---
id: github:teqplay/vesselvoyage-backend:pr:663
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 663
title: TTC-526 Priority field population
author: TeqJoostD
state: closed
date: '2025-11-11'
merged_at: '2025-11-11'
base_branch: develop
head_branch: TTC-526
url: https://github.com/teqplay/vesselvoyage-backend/pull/663
labels: []
linked_issues: []
explicit_links: []
---
# PR #663: TTC-526 Priority field population

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/663  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TTC-526`  
**Created:** 2025-11-11  
**Merged:** 2025-11-11  

## Description

_No description._

## Commits

- `c11588fc` **TeqJoostD** (2025-11-10): add logic for supporting and populating priority field for post-processable items
- `9c9960e5` **TeqJoostD** (2025-11-10): add more logging
- `0bcc9dd2` **TeqJoostD** (2025-11-10): add profile processing
- `c0a80c0e` **TeqJoostD** (2025-11-10): Added priority logic
- `9c1a3a3f` **TeqJoostD** (2025-11-10): change direction
- `c4ba2570` **TeqJoostD** (2025-11-10): fix wrong collection import statement
- `30e51142` **TeqJoostD** (2025-11-11): Make populate service applicationTest safe
- `f3377d19` **TeqJoostD** (2025-11-11): Create controller support
- `c34f0e69` **TeqJoostD** (2025-11-11): Add ordering in datasource, add batched processing
- `2908cee9` **TeqJoostD** (2025-11-11): Add error handling
- `7be52949` **TeqJoostD** (2025-11-11): Fix indexing, add more ports to ARA list
- `985ee746` **TeqJoostD** (2025-11-11): Catch collection bulkwrite error

## Reviews

### github-actions[bot] — COMMENTED (2025-11-11)

Review completed with several suggestions for improvement. The priority field population implementation looks solid overall, but there are some important issues to address around null safety, sorting logic, and error handling.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-11)

## Pull Request Overview

This PR implements a priority field for post-processing to allow certain visits/voyages (specifically those associated with ARA and USCRP ports) to be processed before others. The feature is controlled by a configuration flag `post-processing.priority.enabled`.

Key changes:
- Added a `priority` boolean field to the `PostProcessable` model
- Created services to determine priority based on port locations and populate the priority field
- Modified the post-processing logic to sort entries by priority before processing

### Reviewed Changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated 7 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/resources/application.properties | Added `post-processing.priority.enabled` configuration flag (disabled by default) |
| src/test/resources/application.properties | Added same configuration flag for test environment |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessable.kt | Added `priority` boolean field with default value `false` |
| src/main/kotlin/nl/teqplay/vesselvoyage/properties/PostProcessingProperties.kt | Added nested `Priority` class to hold priority-related configuration |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessingPriorityService.kt | New service to determine if an entry should have priority based on port locations |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingPriorityPopulationService.kt | New service to populate the priority field for existing entries |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/PostProcessableDataSource.kt | Added index on the `priority` field for query optimization |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt | Modified to sort entries by priority before processing |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingPostProcessingController.kt | Added new endpoint to trigger priority population |
</details>

### TeqJoostD — COMMENTED (2025-11-11)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-11)

Code review completed. Found several areas for improvement related to error handling, batch processing logic, and null safety. Please see inline comments for specific suggestions.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-11-11)

Review completed. The priority field population implementation looks solid overall with good separation of concerns and efficient batch processing. A few suggestions for improvements have been provided in the inline comments.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-11-11)

Review completed. The priority field population implementation looks solid overall with good separation of concerns and proper configuration management. A few suggestions for improvements have been provided in the inline comments.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2025-11-11)

The priority field population implementation looks solid overall. The batched processing approach and proper error handling are well implemented. A few suggestions for improvement have been provided in the inline comments.

### Darius-Wattimena — APPROVED (2025-11-11)

_No comment._

## Review Comments

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingPriorityPopulationService.kt`

The filter logic is inverted. `Filters.exists('priority')` will only select documents that already have the priority field. To populate missing priority fields, use `Filters.not(Filters.exists('priority'))` or remove the filter entirely to update all documents.
```suggestion
        val filter = Filters.not(Filters.exists("priority"))
```

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingPriorityPopulationService.kt`

This implementation performs individual database updates for each document (N+1 pattern). For a backfill operation processing potentially thousands of documents, consider batching updates using `bulkWrite` to significantly improve performance.

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The sorting logic is inverted. `sortedBy { it.priority }` sorts boolean values with `false` before `true`, meaning non-priority entries will be processed first. Use `sortedByDescending { it.priority }` to process priority entries first.
```suggestion
            // Sort by priority descending so priority entries are processed first
            val allPostProcessableSortedByPriority = allPostProcessable.sortedByDescending { it.priority }
```

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessingPriorityService.kt`

Hard-coded port list should be externalized to configuration to allow modification without code changes. Consider moving this to `PostProcessingProperties.Priority` class or a separate configuration property.

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingPriorityPopulationService.kt`

This method performs individual database lookups for each entry. Since the operation processes entries in batches of 1000, consider fetching all visits and voyages in bulk using batch queries to reduce database round-trips.
```suggestion
        val batchSize = 1000
        val docsBatch = mutableListOf<PostProcessable>()
        for (doc in cursor) {
            docsBatch.add(doc)
            if (docsBatch.size == batchSize) {
                processBatch(docsBatch, ppCollection)
                seen += docsBatch.size
                priorityCount += docsBatch.count { it.priority == true }
                log.info { "Processed $seen documents so far (priority=$priorityCount)..." }
                docsBatch.clear()
            }
        }
        // Process any remaining docs
        if (docsBatch.isNotEmpty()) {
            processBatch(docsBatch, ppCollection)
            seen += docsBatch.size
            priorityCount += docsBatch.count { it.priority == true }
        }

        log.info { "BackfillPostProcessablePriority complete: scanned=$seen, priority=$priorityCount" }
    }

    /**
     * Processes a batch of PostProcessable documents by performing bulk lookups for visits and voyages,
     * updating the priority field efficiently.
     */
    private fun processBatch(
        docsBatch: List<PostProcessable>,
        ppCollection: com.mongodb.kotlin.client.MongoCollection<PostProcessable>
    ) {
        val entryIds = docsBatch.map { it.entryId }
        val visitIds = entryIds.filter { it.endsWith("VISIT") }
        val voyageIds = entryIds.filterNot { it.endsWith("VISIT") }

        // Bulk fetch visits and voyages
        val visits = visitDataSource.findByIds(visitIds)
        val voyages = voyageDataSource.findByIds(voyageIds)

        // Build lookup map
        val entryMap = mutableMapOf<String, NewEntry>()
        visits.forEach { entryMap[it.entryId] = it }
        voyages.forEach { entryMap[it.entryId] = it }

        for (doc in docsBatch) {
            val entry = entryMap[doc.entryId]
            val priority = entry?.let { postProcessingPriorityService?.isARAorUSCRPEntry(entry) } ?: false

            // Update only the current document by its _id
            val idFilter = Filters.eq("_id", doc.entryId)
            val update = Updates.combine(
                Updates.set("priority", priority),
            )
            ppCollection.updateOne(idFilter, update)
```

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessingPriorityService.kt`

The `priorityAreaIds` initialization happens once at service construction. If `infraService.getPortByUnlocode()` returns null for any port at startup (e.g., database not ready), those ports will be silently excluded from priority checking. Consider lazy initialization or validation that all expected ports are found.
```suggestion
    private val priorityAreaIds: List<String>

    init {
        val foundAreaIds = mutableListOf<String>()
        val missingPorts = mutableListOf<String>()
        for (unlocode in priorityPorts) {
            val port = infraService.getPortByUnlocode(unlocode)
            if (port != null) {
                foundAreaIds.add(port._id)
            } else {
                missingPorts.add(unlocode)
            }
        }
        if (missingPorts.isNotEmpty()) {
            log.error { "PostProcessingPriorityService: Missing priority ports at startup: $missingPorts. Service will not start." }
            throw IllegalStateException("Missing priority ports: $missingPorts")
        }
        priorityAreaIds = foundAreaIds
```

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingPriorityPopulationService.kt`

The log message references 'BackfillPostProcessablePriority' which appears to be a legacy name. The service is named 'PostProcessingPriorityPopulationService'. Update the message to reflect the current service name.
```suggestion
        log.info { "PostProcessingPriorityPopulationService complete: scanned=$seen, priority=$priorityCount" }
```

### TeqJoostD — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingPriorityPopulationService.kt`

ehhh
