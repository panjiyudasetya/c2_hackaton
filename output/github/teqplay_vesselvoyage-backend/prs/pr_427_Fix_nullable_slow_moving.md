---
id: github:teqplay/vesselvoyage-backend:pr:427
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 427
title: Fix nullable slow moving
author: Darius-Wattimena
state: closed
date: '2025-02-20'
merged_at: '2025-02-20'
base_branch: develop
head_branch: fix-nullable-slow-moving
url: https://github.com/teqplay/vesselvoyage-backend/pull/427
labels: []
linked_issues: []
explicit_links: []
---
# PR #427: Fix nullable slow moving

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/427  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-nullable-slow-moving`  
**Created:** 2025-02-20  
**Merged:** 2025-02-20  

## Description

_No description._

## Commits

- `6034ef26` **Darius Wattimena** (2025-02-20): Adjusted the slow moving periods so they are nullable when not determined yet
- `d4343e2d` **Darius Wattimena** (2025-02-20): rewritten the code to be easier to test
- `30738811` **Darius Wattimena** (2025-02-20): Added 2 test cases to ensure we correctly generate the slow moving periods when we didn't generate anything yet or when we generated but had an empty result

## Reviews

### TeqJoostD — APPROVED (2025-02-20)

_No comment._
