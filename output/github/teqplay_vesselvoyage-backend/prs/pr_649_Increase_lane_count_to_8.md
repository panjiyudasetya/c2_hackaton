---
id: github:teqplay/vesselvoyage-backend:pr:649
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 649
title: Increase lane count to 8
author: TeqJoostD
state: closed
date: '2025-10-23'
merged_at: '2025-10-23'
base_branch: master
head_branch: trace-processing-fix
url: https://github.com/teqplay/vesselvoyage-backend/pull/649
labels: []
linked_issues: []
explicit_links: []
---
# PR #649: Increase lane count to 8

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/649  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `trace-processing-fix`  
**Created:** 2025-10-23  
**Merged:** 2025-10-23  

## Description

_No description._

## Commits

- `99605797` **TeqJoostD** (2025-10-23): Increase lane count to 8
- `6334cfb1` **Joost Dambrink** (2025-10-23): Update src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-23)

## Pull Request Overview

This PR increases the lane count configuration from 4 to 8 lanes in the AIS streaming message handler, likely to improve throughput and parallel processing capacity for handling AIS streaming messages.

## Review Comments

### Copilot — 2025-10-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/AisStreamingMessageHandler.kt`

Increasing LANE_COUNT from 4 to 8 while keeping MAX_IN_FLIGHT at 800 reduces perLaneCapacity from 200 to 100. This change may impact throughput and should be accompanied by performance testing to verify the system can handle the increased concurrency without degrading per-lane processing efficiency.
```suggestion
        private const val MAX_IN_FLIGHT = 1600
```
