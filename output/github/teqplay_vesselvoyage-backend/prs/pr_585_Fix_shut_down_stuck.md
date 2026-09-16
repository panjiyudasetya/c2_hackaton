---
id: github:teqplay/vesselvoyage-backend:pr:585
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 585
title: Fix shut down stuck
author: Darius-Wattimena
state: closed
date: '2025-08-08'
merged_at: '2025-08-08'
base_branch: develop
head_branch: fix-shut-down-stuck
url: https://github.com/teqplay/vesselvoyage-backend/pull/585
labels: []
linked_issues: []
explicit_links: []
---
# PR #585: Fix shut down stuck

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/585  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-shut-down-stuck`  
**Created:** 2025-08-08  
**Merged:** 2025-08-08  

## Description

_No description._

## Commits

- `d6a6529c` **Darius Wattimena** (2025-07-14): Merge pull request #565 from teqplay/develop
  Release 2025-07-14
- `c7f5bc68` **Darius Wattimena** (2025-07-15): Merge pull request #570 from teqplay/develop
  Release 2025-07-15
- `b34f398f` **Darius Wattimena** (2025-07-15): Merge pull request #574 from teqplay/develop
  Release 2025-07-15 #2
- `c1d204c7` **Darius Wattimena** (2025-07-17): Merge pull request #576 from teqplay/develop
  Release 2025-07-17
- `80953b37` **Darius Wattimena** (2025-08-06): Merge pull request #584 from teqplay/develop
  Release 2025-08-06
- `071ea848` **Darius Wattimena** (2025-08-08): Adjusted how we shut down so we only stop the background processing on close and also stop the PostProcessingService which was missing

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-08)

## Pull Request Overview

This PR fixes an issue where the application shutdown process was getting stuck by improving the shutdown sequence of various processing services. The fix reorganizes the shutdown logic to ensure all background services are properly terminated during application shutdown.

Key changes:
- Separates regular processing shutdown from background processing shutdown
- Adds proper shutdown method to PostProcessingService
- Ensures all services including PostProcessingService and V1TraceService are shutdown during application termination

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| ProcessingService.kt | Refactors shutdown logic by adding PostProcessingService dependency and creating separate methods for different shutdown phases |
| PostProcessingService.kt | Adds missing shutdown method to properly terminate the executor service |

### TeqJoostD — APPROVED (2025-08-08)

_No comment._

## Review Comments

### Copilot — 2025-08-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The shutdown method only calls executor.shutdown() which initiates an orderly shutdown but doesn't wait for completion. Consider using executor.awaitTermination() with a timeout to ensure tasks complete before proceeding, or use shutdownNow() if immediate termination is required.
```suggestion
        executor.shutdown()
        try {
            if (!executor.getThreadPoolExecutor().awaitTermination(60, TimeUnit.SECONDS)) {
                executor.shutdownNow()
                if (!executor.getThreadPoolExecutor().awaitTermination(60, TimeUnit.SECONDS)) {
                    log.warn { "Executor did not terminate" }
                }
            }
        } catch (ie: InterruptedException) {
            executor.shutdownNow()
            Thread.currentThread().interrupt()
        }
```
