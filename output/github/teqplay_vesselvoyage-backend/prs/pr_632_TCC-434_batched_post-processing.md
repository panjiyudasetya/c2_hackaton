---
id: github:teqplay/vesselvoyage-backend:pr:632
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 632
title: TCC-434 batched post-processing
author: Darius-Wattimena
state: closed
date: '2025-10-13'
merged_at: '2025-10-13'
base_branch: develop
head_branch: TCC-434-batched-post-processing
url: https://github.com/teqplay/vesselvoyage-backend/pull/632
labels: []
linked_issues: []
explicit_links: []
---
# PR #632: TCC-434 batched post-processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/632  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-434-batched-post-processing`  
**Created:** 2025-10-13  
**Merged:** 2025-10-13  

## Description

_No description._

## Commits

- `ee020504` **Darius Wattimena** (2025-10-13): Implement batched post-processing so we always keep up-to-date with real-time entries
- `fdcace27` **Darius Wattimena** (2025-10-13): Update src/main/kotlin/nl/teqplay/vesselvoyage/datasource/PostProcessableDataSource.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>
- `82591baa` **Darius Wattimena** (2025-10-13): First sort before limiting
- `18ac9a34` **Darius Wattimena** (2025-10-13): Merge remote-tracking branch 'origin/TCC-434-batched-post-processing' into TCC-434-batched-post-processing

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-13)

## Pull Request Overview

This PR implements batched post-processing to improve performance by limiting the number of entries processed per cycle. The change introduces a configurable batch size limit to prevent overwhelming the system when processing large backlogs while maintaining real-time processing capabilities.

Key changes:
- Introduces a maximum batch size of 1000 entries per post-processing cycle
- Replaces `getAll()` with `getBatch()` method that includes pagination and sorting
- Adds database indexing on the sorting field for performance optimization

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File | Description |
| ---- | ----------- |
| PostProcessingService.kt | Adds batch size constant and updates cycle logic to use batched processing |
| PostProcessableDataSource.kt | Implements getBatch method with limit, sorting, and database indexing |

### michel-teqplay — APPROVED (2025-10-13)

_No comment._

## Review Comments

### Copilot — 2025-10-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/PostProcessableDataSource.kt`

The parameter documentation uses incorrect KDoc syntax. Should use `@param batchSize` instead of `@batchSize`.
```suggestion
     * @param batchSize The maximum amount of post-processing we want to do per cycle. This is to ensure we keep post-processing real-time entries and slowly work away our backlog.
```
