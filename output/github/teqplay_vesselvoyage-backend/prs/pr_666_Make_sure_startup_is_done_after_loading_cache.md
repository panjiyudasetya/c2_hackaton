---
id: github:teqplay/vesselvoyage-backend:pr:666
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 666
title: Make sure startup is done after loading cache
author: TeqJoostD
state: closed
date: '2025-11-11'
merged_at: '2025-11-11'
base_branch: develop
head_branch: TTC-526
url: https://github.com/teqplay/vesselvoyage-backend/pull/666
labels: []
linked_issues: []
explicit_links: []
---
# PR #666: Make sure startup is done after loading cache

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/666  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TTC-526`  
**Created:** 2025-11-11  
**Merged:** 2025-11-11  

## Description

_No description._

## Commits

- `508a2755` **TeqJoostD** (2025-11-11): Make sure startup is done after loading cache
- `9e19c38d` **TeqJoostD** (2025-11-11): remove eosp suffix
- `37603f89` **Joost Dambrink** (2025-11-11): Merge branch 'develop' into TTC-526
- `11e03db3` **TeqJoostD** (2025-11-11): Fix darius added tests

## Reviews

### Darius-Wattimena — DISMISSED (2025-11-11)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-11)

The changes correctly address the startup timing issue by ensuring priority area IDs are initialized after cache loading. The implementation follows the established pattern used by other services in the codebase.

🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-11)

## Pull Request Overview

This PR refactors the `PostProcessingPriorityService` to defer initialization of priority area IDs until after the cache (specifically `InfraService`) is loaded. Previously, the priority area IDs were initialized immediately during bean construction, which could fail if the infrastructure cache wasn't ready.

**Key Changes:**
- Moved priority area ID initialization from class initialization to a new `startup()` method
- Added `postProcessingPriorityService.startup()` call to the `ProcessingService.onStartProcessing()` lifecycle method
- Used `lateinit` to defer initialization of the `priorityAreaIds` field

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessingPriorityService.kt | Refactored to use `lateinit` for `priorityAreaIds` and moved initialization logic to a new `startup()` method that fetches area IDs from `InfraService` |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingService.kt | Added `PostProcessingPriorityService` dependency and called its `startup()` method during the processing startup sequence |

### github-actions[bot] — COMMENTED (2025-11-11)

The changes properly address the startup ordering issue and improve area ID consistency. The lazy initialization approach ensures the priority service starts after cache loading is complete.

### Darius-Wattimena — DISMISSED (2025-11-11)

_No comment._

### github-actions[bot] — COMMENTED (2025-11-11)

The changes look good overall - moving the priority area initialization to a startup method ensures it happens after the cache is loaded. However, there's one potential issue with the lateinit property that should be addressed.

### github-actions[bot] — COMMENTED (2025-11-11)

The changes properly address the startup ordering issue by ensuring cache loading completes before priority service initialization. The implementation is clean and follows good practices.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — APPROVED (2025-11-11)

_No comment._

## Review Comments

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessingPriorityService.kt`

The `startup()` method should include logging similar to other services in the codebase (e.g., `AisStreamingMessageHandler.startup()`, `AutomaticRecalculationService.startup()`). This helps with debugging and monitoring service initialization. 

Add a log statement like:
```kotlin
fun startup() {
    log.info { "Starting PostProcessingPriorityService" }
    // ARA Region Ports
    val ports = setOf("USCRP", "NLRTM", "NLAMS", "BEANR", "NLVLI", "BEGNE", "NLTNZ")
    
    priorityAreaIds = ports.mapNotNull { unlocode ->
        fetchAreaId(unlocode)
    }
    log.info { "Loaded ${priorityAreaIds.size} priority area IDs" }
}
```
```suggestion
    fun startup() {
        log.info { "Starting PostProcessingPriorityService" }
        // ARA Region Ports
        val ports = setOf("USCRP", "NLRTM", "NLAMS", "BEANR", "NLVLI", "BEGNE", "NLTNZ")

        priorityAreaIds = ports.mapNotNull { unlocode ->
            fetchAreaId(unlocode)
        }
        log.info { "Loaded ${priorityAreaIds.size} priority area IDs" }
```

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessingPriorityService.kt`

[nitpick] The list of priority ports is hardcoded in the `startup()` method. This reduces flexibility and maintainability. Consider moving this configuration to application properties so it can be changed without code modifications.

For example:
```kotlin
// In application.properties:
// post-processing.priority.ports=USCRP,NLRTM,NLAMS,BEANR,NLVLI,BEGNE,NLTNZ

// In a properties class:
@ConfigurationProperties(prefix = "post-processing.priority")
data class PostProcessingPriorityProperties(
    val enabled: Boolean = false,
    val ports: Set<String> = emptySet()
)
```

This follows the pattern already established in the codebase with other configuration properties.

### Copilot — 2025-11-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/PostProcessingPriorityService.kt`

The `priorityAreaIds` field is declared as `lateinit` and can be accessed before `startup()` is called, which will throw a `UninitializedPropertyAccessException`. This can happen if `PostProcessingPriorityPopulationService.execute()` is called via the `/v2/post-processing/populate/priority` endpoint before the startup completes.

Consider one of these solutions:
1. Initialize `priorityAreaIds` as an empty list and add a check in `isARAorUSCRPEntry` to ensure it's been populated
2. Use a nullable type with a check: `private var priorityAreaIds: List<String>? = null`
3. Add documentation that `startup()` must be called before using this service
