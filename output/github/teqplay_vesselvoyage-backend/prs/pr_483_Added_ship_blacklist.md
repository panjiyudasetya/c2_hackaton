---
id: github:teqplay/vesselvoyage-backend:pr:483
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 483
title: Added ship blacklist
author: TeqJoostD
state: closed
date: '2025-04-23'
merged_at: '2025-04-30'
base_branch: develop
head_branch: blacklist
url: https://github.com/teqplay/vesselvoyage-backend/pull/483
labels: []
linked_issues: []
explicit_links: []
---
# PR #483: Added ship blacklist

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/483  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `blacklist`  
**Created:** 2025-04-23  
**Merged:** 2025-04-30  

## Description

_No description._

## Commits

- `700ba6cc` **TeqJoostD** (2025-04-23): feat: add tolerance to qualification of arrival/departure tugs
- `da20e9ec` **TeqJoostD** (2025-04-23): fix: ktlint
- `d1314bb0` **TeqJoostD** (2025-04-23): fix: add missing annotation
- `4be80324` **TeqJoostD** (2025-04-23): fix: add missing annotation
- `1d8d493d` **TeqJoostD** (2025-04-23): fix: fix test
- `29ddd47b` **TeqJoostD** (2025-04-30): fix: change feedback

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-04-23)

## Pull Request Overview

This pull request adds support for a ship blacklist to prevent processing events from specific ships.  
- Injects a datasource for retrieving a list of blacklisted ship IMO numbers.  
- Updates event processing logic to terminate messages for ships with null or blacklisted IMO values.  
- Introduces a new data class and datasource to manage blacklisted ships.

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt | Integrated blacklist check and dependency injection for blacklist datasource. |
| src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/ShipBlacklist.kt | Added data class representing a blacklisted ship. |
| src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ShipBlacklistDatasource.kt | Provided a datasource that retrieves all blacklisted ship IMO numbers. |

### Darius-Wattimena — CHANGES_REQUESTED (2025-04-28)

_No comment._

### Darius-Wattimena — APPROVED (2025-04-30)

_No comment._

## Review Comments

### Copilot — 2025-04-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt`

The blacklisted ships list is loaded once during processor initialization, which may lead to stale data if the blacklist changes during runtime. Consider implementing a mechanism to refresh this list periodically.

### Darius-Wattimena — 2025-04-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/ShipBlacklistDatasource.kt`

This is only needed for the processing profile? Event processing is only done on that level, not on the API level.

### Darius-Wattimena — 2025-04-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/model/internal/ShipBlacklist.kt`

Do we need an `_id` field? We can just use the `imo` as the `BsonId` I think?
