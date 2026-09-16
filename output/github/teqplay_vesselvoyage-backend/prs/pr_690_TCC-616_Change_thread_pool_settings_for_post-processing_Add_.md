---
id: github:teqplay/vesselvoyage-backend:pr:690
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 690
title: TCC-616 Change thread pool settings for post-processing Add max timeout for
  thread pool
author: TeqJoostD
state: closed
date: '2026-01-07'
merged_at: null
base_branch: develop
head_branch: TCC-616
url: https://github.com/teqplay/vesselvoyage-backend/pull/690
labels: []
linked_issues: []
explicit_links: []
---
# PR #690: TCC-616 Change thread pool settings for post-processing Add max timeout for thread pool

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/690  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-616`  
**Created:** 2026-01-07  

## Description

_No description._

## Commits

- `367f6153` **TeqJoostD** (2026-01-07): Change thread pool settings for post-processing
  Add max timeout for thread pool
- `48d78169` **TeqJoostD** (2026-01-07): Revert some of the thread pool settings
- `bdd2d38f` **TeqJoostD** (2026-01-07): Introduce bounded queue with error message and slack notification again
- `ba3993eb` **TeqJoostD** (2026-01-07): Add test coverage for timeout mechanism

## Reviews

### github-actions[bot] — COMMENTED (2026-01-07)

Review completed. The changes look solid overall - the timeout mechanism and improved thread pool configuration will help prevent indefinite hangs. No critical issues found.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-07)

## Pull request overview

This PR enhances the post-processing service's thread pool management by adding timeout protection, improved configuration, and better monitoring capabilities to prevent the scheduled task from hanging indefinitely.

**Key Changes:**
- Added configurable timeout for thread pool waiting (default 1 hour) with timeout detection and Slack notifications
- Enhanced thread pool configuration with maxPoolSize (2x totalThreads), queueCapacity (10,000), and CallerRunsPolicy for rejection handling
- Improved observability with cycle duration logging and elapsed time tracking in wait loops

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 6 comments.

| File | Description |
| ---- | ----------- |
| PostProcessingService.kt | Added thread pool timeout mechanism, enhanced executor configuration with queue capacity and rejection policy, improved logging with duration tracking |
| PostProcessingProperties.kt | Added two new configurable properties: threadPoolWaitTimeout (Duration) and queueCapacity (Int) with sensible defaults |

### github-actions[bot] — COMMENTED (2026-01-07)

Review completed. The changes add timeout protection for the thread pool wait operation and revert to a simpler thread pool configuration. The implementation looks correct and the timeout mechanism provides a safety net against indefinite hangs.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-07)

The PR introduces bounded queue capacity and timeout settings for the post-processing thread pool. However, there is a critical issue with task rejection handling that could lead to data loss.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — COMMENTED (2026-01-07)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-07)

## Pull request overview

Copilot reviewed 2 out of 2 changed files in this pull request and generated 5 comments.

### TeqJoostD — COMMENTED (2026-01-07)

_No comment._

### github-actions[bot] — COMMENTED (2026-01-07)

Review completed. The implementation adds important timeout and queue management features to prevent indefinite hangs. However, there is a critical issue with the rejection handler that could lead to silent data loss.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

## Review Comments

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The new thread pool timeout functionality, including the timeout check, error logging, and Slack notification, is not covered by tests. Since PostProcessingServiceTest already has comprehensive test coverage for other features, this new critical functionality should have corresponding tests to verify timeout behavior.

### TeqJoostD — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

Not true, entries will stay in the datasource if not processed

### Copilot — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

The timeout check uses elapsed time greater than maxWaitMillis, which means if elapsed equals maxWaitMillis exactly, it won't trigger. This could lead to waiting slightly longer than intended. Change the condition to use greater than or equal to for more precise timeout enforcement.
```suggestion
            if (elapsed >= maxWaitMillis) {
```

### TeqJoostD — 2026-01-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/PostProcessingService.kt`

oh no imagine the consequences
