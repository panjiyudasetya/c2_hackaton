---
id: github:teqplay/poma-backend:pr:185
source: github
type: pull_request
repo: teqplay/poma-backend
number: 185
title: Added functionType to terminal and made CARGOOPS the default in the apiModel
author: PimTeqplay
state: closed
date: '2025-02-21'
merged_at: '2025-02-27'
base_branch: develop
head_branch: CC-123-function-types-terminals
url: https://github.com/teqplay/poma-backend/pull/185
labels: []
linked_issues: []
explicit_links:
- jira:CC-123
---
# PR #185: Added functionType to terminal and made CARGOOPS the default in the apiModel

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/185  
**State:** closed | **Author:** PimTeqplay  
**Base ← Head:** `develop` ← `CC-123-function-types-terminals`  
**Created:** 2025-02-21  
**Merged:** 2025-02-27  

## Description

_No description._

## Commits

- `ff5b4b7f` **Pim van den Toorn** (2025-02-21): Added functionType to terminal and made CARGOOPS the default in the apiModel
- `393e127b` **Pim van den Toorn** (2025-02-21): Removing SHIP2SHIP and CARDROPOFF from functionType when converting an apiModel to a db model, as those should not be possible for terminals
- `5317cb87` **Pim van den Toorn** (2025-02-27): Added comment on terminal function type

## Reviews

### TeqJoostD — COMMENTED (2025-02-26)

_No comment._

### TeqJoostD — CHANGES_REQUESTED (2025-02-26)

minor feedback

### PimTeqplay — COMMENTED (2025-02-27)

_No comment._

### TeqJoostD — APPROVED (2025-02-27)

_No comment._

## Review Comments

### TeqJoostD — 2025-02-26 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalService.kt`

Can you add a comment why these get removed

### PimTeqplay — 2025-02-27 on `src/main/kotlin/nl/teqplay/poma/feature/infrastructure/terminal/TerminalService.kt`

Done
