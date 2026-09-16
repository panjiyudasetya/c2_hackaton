---
id: github:teqplay/vesselvoyage-backend:pr:599
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 599
title: Infra cache improvements
author: Darius-Wattimena
state: closed
date: '2025-08-26'
merged_at: '2025-08-27'
base_branch: develop
head_branch: infra-cache-improvements
url: https://github.com/teqplay/vesselvoyage-backend/pull/599
labels: []
linked_issues: []
explicit_links: []
---
# PR #599: Infra cache improvements

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/599  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `infra-cache-improvements`  
**Created:** 2025-08-26  
**Merged:** 2025-08-27  

## Description

Tried out augment, see if it produced any good code and it actually did pretty well.
Given that this cleans up the code quite nicely + it might fix the weird edge case that occurred when you ask for infra but instead get an empty result (because of the missing Volatile annotations)

## Commits

- `3def8c50` **Darius Wattimena** (2025-08-26): Refactor infra cache to be better thread-safe, use less casting and generics where possible and remove nullable fields where possible
- `a200c4bd` **Darius Wattimena** (2025-08-26): ktlint
- `ffc29981` **Darius Wattimena** (2025-08-26): Fix test helper functions where a nullable poma entity was possible

## Reviews

### TeqJoostD — APPROVED (2025-08-26)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-26)

Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting a review.

## Comments

### TeqJoostD — 2025-08-26

@Copilot what the sigma?
