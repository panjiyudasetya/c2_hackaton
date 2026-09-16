---
id: github:teqplay/vesselvoyage-backend:pr:590
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 590
title: Infra missing error
author: Darius-Wattimena
state: closed
date: '2025-08-13'
merged_at: '2025-08-13'
base_branch: develop
head_branch: infra-missing-error
url: https://github.com/teqplay/vesselvoyage-backend/pull/590
labels: []
linked_issues: []
explicit_links: []
---
# PR #590: Infra missing error

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/590  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `infra-missing-error`  
**Created:** 2025-08-13  
**Merged:** 2025-08-13  

## Description

_No description._

## Commits

- `e2508c34` **Darius Wattimena** (2025-08-12): Added test to check if getting the port by id can result in a concurrency issue
- `a3b27d1e` **Darius Wattimena** (2025-08-12): Adjusted in memory maps to be ConcurrentHashMap instead to ensure read and write operations to be consistent
- `544ced08` **Darius Wattimena** (2025-08-12): Adjusted some extra code so we don't have to do additional casting
- `5b45af18` **Darius Wattimena** (2025-08-12): Adjusted some more to avoid additional casting
- `35341aab` **Darius Wattimena** (2025-08-12): Removed unused import
- `aaf28153` **Darius Wattimena** (2025-08-13): Removed unused volatile annotation
- `12968e2b` **Darius Wattimena** (2025-08-13): Fix test

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-13)

## Pull Request Overview

This PR adds an infrastructure error handling improvement by introducing a dedicated method for port retrieval and implementing thread-safe concurrent access to the infrastructure cache. The changes focus on improving the robustness of port lookups and ensuring thread safety in concurrent scenarios.

Key changes:
- Introduction of a new `getPortByAreaId` method to simplify port retrieval
- Conversion of cache maps to `ConcurrentHashMap` for thread-safe access
- Addition of concurrency testing for infrastructure service operations

### Reviewed Changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| InfraServiceTest.kt | Adds concurrency test and imports for new infrastructure area type |
| EntryV2MapperTest.kt | Updates test mocks to use new `getPortByAreaId` method |
| InfraCacheService.kt | Converts cache maps to `ConcurrentHashMap` for thread safety |
| EntryV2Mapper.kt | Simplifies port retrieval by using new `getPortByAreaId` method |

### TeqJoostD — DISMISSED (2025-08-13)

_No comment._

### TeqJoostD — APPROVED (2025-08-13)

_No comment._

## Review Comments

### Copilot — 2025-08-13 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/InfraServiceTest.kt`

Calling `thread.join()` immediately after `thread.start()` defeats the purpose of concurrent testing. All threads will execute sequentially instead of concurrently. Move all `start()` calls before any `join()` calls to ensure proper concurrent execution.
```suggestion
            thread.start()
        }
        threads.forEach { thread ->
```

### Copilot — 2025-08-13 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/InfraServiceTest.kt`

Using `ReentrantLock` for thread-safe list access is unnecessary overhead. Consider using `Collections.synchronizedList()` or a concurrent collection like `ConcurrentLinkedQueue` for better performance in this test scenario.
```suggestion

```

### Copilot — 2025-08-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/InfraCacheService.kt`

The `@Volatile` annotation on `itemsById` is redundant since `ConcurrentHashMap` already provides thread-safe access. The volatile keyword is unnecessary and may cause confusion about the synchronization strategy.
```suggestion
        
```
