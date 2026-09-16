---
id: github:teqplay/vesselvoyage-backend:pr:487
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 487
title: 'fix: add try catch'
author: TeqJoostD
state: closed
date: '2025-04-30'
merged_at: '2025-04-30'
base_branch: develop
head_branch: SPV-2612
url: https://github.com/teqplay/vesselvoyage-backend/pull/487
labels: []
linked_issues: []
explicit_links: []
---
# PR #487: fix: add try catch

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/487  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `SPV-2612`  
**Created:** 2025-04-30  
**Merged:** 2025-04-30  

## Description

_No description._

## Commits

- `2b69598b` **TeqJoostD** (2025-04-30): fix: add try catch
- `ea597cc0` **TeqJoostD** (2025-04-30): fix: add stacktrace
- `740e4253` **TeqJoostD** (2025-04-30): fix: add stacktrace

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-30)

## Pull Request Overview

This PR adds a try-catch block around the asynchronous publishing of events to ensure any exceptions during the publish process are caught and logged.  
- Added an import for KotlinLogging and initialized a logger.  
- Wrapped the producer.publishAsync call in a try-catch block to log errors during message processing.

### Darius-Wattimena — CHANGES_REQUESTED (2025-04-30)

_No comment._

### Darius-Wattimena — APPROVED (2025-04-30)

_No comment._

## Review Comments

### Copilot — 2025-04-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsReventsMessageProcessor.kt`

Consider logging the complete exception (e.g., using log.error(e) { ... }) to capture the full stack trace rather than only logging the error message.
```suggestion
                    // log error with full stack trace
                    log.error(e) { "Error publishing message" }
```

### Darius-Wattimena — 2025-04-30 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsReventsMessageProcessor.kt`

```suggestion
                    log.error(e) { "Error publishing message" }
```
Doing it this way we at least know the stacktrace that is being thrown?
