---
id: github:teqplay/vesselvoyage-backend:pr:536
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 536
title: TCC-209 fix sof ids
author: Darius-Wattimena
state: closed
date: '2025-06-16'
merged_at: '2025-06-17'
base_branch: master
head_branch: TCC-209-fix-sof-ids
url: https://github.com/teqplay/vesselvoyage-backend/pull/536
labels: []
linked_issues: []
explicit_links: []
---
# PR #536: TCC-209 fix sof ids

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/536  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `TCC-209-fix-sof-ids`  
**Created:** 2025-06-16  
**Merged:** 2025-06-17  

## Description

_No description._

## Commits

- `e93f8950` **Darius Wattimena** (2025-06-16): Adjusted ID generation for all stops and encounters to be based on visit id + the id of said activity to avoid id duplication on split stops or encounters
- `060a314b` **Darius Wattimena** (2025-06-16): Adjusted existing test cases to ensure the ids are generated as expected
- `29ba3248` **Darius Wattimena** (2025-06-16): code cleanup
- `f138f81b` **Darius Wattimena** (2025-06-16): Merge branch 'master' into TCC-209-fix-sof-ids

## Reviews

### TeqJoostD — APPROVED (2025-06-16)

_No comment._
