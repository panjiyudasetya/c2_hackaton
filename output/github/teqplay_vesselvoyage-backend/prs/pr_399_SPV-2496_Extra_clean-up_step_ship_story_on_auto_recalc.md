---
id: github:teqplay/vesselvoyage-backend:pr:399
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 399
title: SPV-2496 Extra clean-up step ship story on auto recalc
author: Darius-Wattimena
state: closed
date: '2025-01-24'
merged_at: '2025-01-28'
base_branch: develop
head_branch: SPV-2496-additional-clean-up-step-auto-recalc
url: https://github.com/teqplay/vesselvoyage-backend/pull/399
labels: []
linked_issues: []
explicit_links: []
---
# PR #399: SPV-2496 Extra clean-up step ship story on auto recalc

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/399  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2496-additional-clean-up-step-auto-recalc`  
**Created:** 2025-01-24  
**Merged:** 2025-01-28  

## Description

Without this when running auto recalculations we ended up triggering quite a lot of cases where merging was impossible because there was a random `Visit -> Visit -> Voyage` structure, instead of the expected `Visit -> Voyage -> Visit` structure that was expected.

This change makes it so we first run the logic of the "manual" recalculation, ensuring the ship story is in the expected structure.

## Commits

- `8a515249` **Darius Wattimena** (2025-01-24): Made it so we also trigger a story clean-up before we automatically recalculate via revents to ensure we can merge everything back
- `9458b232` **Darius Wattimena** (2025-01-28): Instead recalculate one by one instead of in parallel to avoid the backend exploding when using big batches

## Reviews

### leonjoosse — CHANGES_REQUESTED (2025-01-27)

_No comment._

### Darius-Wattimena — COMMENTED (2025-01-28)

_No comment._

### leonjoosse — APPROVED (2025-01-28)

_No comment._

## Review Comments

### leonjoosse — 2025-01-27 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/AutomaticRecalculationService.kt`

Are you sure about using a `parallelStream`? Should we use another system to control the amount of threads?

### Darius-Wattimena — 2025-01-28 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/AutomaticRecalculationService.kt`

Actually after testing, this does speed it up a bit, but is most likely not needed as recalculating via events is rather fast. Will remove
