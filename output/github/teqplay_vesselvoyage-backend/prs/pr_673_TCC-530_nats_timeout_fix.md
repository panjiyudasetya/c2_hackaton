---
id: github:teqplay/vesselvoyage-backend:pr:673
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 673
title: TCC-530 nats timeout fix
author: Darius-Wattimena
state: closed
date: '2025-11-28'
merged_at: '2025-12-01'
base_branch: develop
head_branch: TCC-530-nats-timeout-fix
url: https://github.com/teqplay/vesselvoyage-backend/pull/673
labels: []
linked_issues: []
explicit_links: []
---
# PR #673: TCC-530 nats timeout fix

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/673  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-530-nats-timeout-fix`  
**Created:** 2025-11-28  
**Merged:** 2025-12-01  

## Description

_No description._

## Commits

- `0587a847` **Darius Wattimena** (2025-11-24): Update skeleton version to 2.10.0 and add NATS dependency
- `5b228b67` **Darius Wattimena** (2025-11-24): Fix NATS consumer timeout by adding drain duration so it doesn't get stuck indefinitely
- `933736a6` **Darius Wattimena** (2025-11-27): Merge branch 'develop' into TCC-530-nats-timeout-fix

## Reviews

### github-actions[bot] — COMMENTED (2025-11-28)

Review completed. The changes look good overall - the timeout additions to NATS drain operations and dependency updates are appropriate improvements. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-28)

## Pull request overview

This PR addresses NATS timeout issues by adding explicit timeout parameters to consumer drain operations and improving observability through additional logging. The changes upgrade the skeleton library to support the new drain API with timeout configuration.

- Adds timeout parameters to all NATS consumer `drain()` calls (10s for shutdown, 1s for refresh)
- Introduces informative logging after drain operations to indicate consumer state
- Updates skeleton library dependency to version 2.10.0-b162.1 and adds explicit NATS module dependency

### Reviewed changes

Copilot reviewed 2 out of 3 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/EventsMessageHandler.kt | Adds 10-second timeout to drain operation in shutdown method and logs drain completion |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt | Adds timeouts to drain operations (1s for refresh, 10s for shutdown) and adds logging for drain completion and shutdown status |
| build.gradle | Updates skeleton library to version 2.10.0-b162.1 and adds explicit nats module dependency to support new drain API |

### TeqJoostD — APPROVED (2025-12-01)

_No comment._

### TeqJoostD — COMMENTED (2025-12-01)

_No comment._

### Darius-Wattimena — COMMENTED (2025-12-01)

_No comment._

## Review Comments

### TeqJoostD — 2025-12-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Would add parameter name here to make it more clear but that is really NIT PICKY

### Darius-Wattimena — 2025-12-01 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

no
