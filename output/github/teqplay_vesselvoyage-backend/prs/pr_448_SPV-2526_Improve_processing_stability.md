---
id: github:teqplay/vesselvoyage-backend:pr:448
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 448
title: SPV-2526 Improve processing stability
author: Darius-Wattimena
state: closed
date: '2025-03-11'
merged_at: '2025-03-14'
base_branch: develop
head_branch: improve-memory
url: https://github.com/teqplay/vesselvoyage-backend/pull/448
labels: []
linked_issues: []
explicit_links: []
---
# PR #448: SPV-2526 Improve processing stability

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/448  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `improve-memory`  
**Created:** 2025-03-11  
**Merged:** 2025-03-14  

## Description

_No description._

## Commits

- `8314dc02` **Darius Wattimena** (2025-03-10): Adjust auto-recalculation refresh performance + GC tweaks
- `50ebfcd3` **Darius Wattimena** (2025-03-11): Improved how we check the automatic recalculation refresh and made the service optional
- `233af841` **Darius Wattimena** (2025-03-11): Added an extra database query that just counts the first voyage before our time without pulling it out of the database
- `13933dd9` **Darius Wattimena** (2025-03-11): Added a comment what the function should do and renamed it to be more clear
- `eafb67eb` **Darius Wattimena** (2025-03-12): Rework event buffer logic
- `ae1d406e` **Darius Wattimena** (2025-03-12): Added logging how long it takes to process an AIS message
- `a752c477` **Darius Wattimena** (2025-03-12): ktlint please
- `6dd76b97` **Darius Wattimena** (2025-03-12): Added a caching layer for traces to reduce the strain on the database and speed up processing
- `fd736d53` **Darius Wattimena** (2025-03-12): Correctly log duration + add try catch around trace processing
- `a2a8ad09` **Darius Wattimena** (2025-03-12): Adjusted how we calculate statistics so it makes sense
- `4c0786fe` **Darius Wattimena** (2025-03-12): Make sure we don't do any processing if the AIS message is older than the previous entry end
- `2c016cdc` **Darius Wattimena** (2025-03-12): Added a try catch in the task to ensure we don't fully crash a threadpool when consuming AIS
- `9f777a07` **Darius Wattimena** (2025-03-12): Added try-catch also for event processing
- `f99ab3a8` **Darius Wattimena** (2025-03-12): Disabled tests for now that expected much different behaviour
- `dce4934f` **Darius Wattimena** (2025-03-12): ktlint
- `81c19154` **Darius Wattimena** (2025-03-13): Fixed null pointers and make sure traces are correctly generated
- `ea960101` **Darius Wattimena** (2025-03-13): Fix an issue where the distance wasn't calculated correctly and enabled trace tests again
- `a835183f` **Darius Wattimena** (2025-03-13): code cleanup
- `bcf04301` **Darius Wattimena** (2025-03-13): ktlint
- `c893f7cd` **Darius Wattimena** (2025-03-13): Removed the unneeded synchronized list logic
- `7a13e5a4` **Darius Wattimena** (2025-03-13): Merge branch 'refs/heads/develop' into improve-memory
- `0491f9eb` **Darius Wattimena** (2025-03-14): Excluded packages so gradle build doesn't fail
- `15055a23` **Darius Wattimena** (2025-03-14): Give 2 percentage of head room to both prod and dev processing

## Reviews

### Darius-Wattimena — COMMENTED (2025-03-11)

_No comment._

### TeqJoostD — COMMENTED (2025-03-11)

_No comment._

### TeqJoostD — COMMENTED (2025-03-11)

minor COMMENT

### TeqJoostD — DISMISSED (2025-03-13)

_No comment._

### Darius-Wattimena — COMMENTED (2025-03-13)

_No comment._

### TeqJoostD — APPROVED (2025-03-14)

_No comment._

## Review Comments

### Darius-Wattimena — 2025-03-11 on `helm/values.processing-dev.yaml`

TODO:
- Can we go back to the default GC?
- Check if we can run without any experimental VM options?
- Also make use of this for PROD processing if keeping.

### TeqJoostD — 2025-03-11 on `src/main/kotlin/nl/teqplay/vesselvoyage/datasource/NewVoyageDataSource.kt`

function name is a bit unclear to me

### TeqJoostD — 2025-03-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceCacheService.kt`

Just wondering if this still is the preferred option now that we know that it was not causing the delay? Or is this meant for the memory issues.

### Darius-Wattimena — 2025-03-13 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/trace/ProcessingTraceCacheService.kt`

Good point, I'll check how much this improves performance & memory because it does avoid us having to look up any traces from the DB when inserting a new AIS point.
