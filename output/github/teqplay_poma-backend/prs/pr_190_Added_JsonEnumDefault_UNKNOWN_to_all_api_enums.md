---
id: github:teqplay/poma-backend:pr:190
source: github
type: pull_request
repo: teqplay/poma-backend
number: 190
title: Added JsonEnumDefault UNKNOWN to all api enums
author: PimTeqplay
state: closed
date: '2025-02-27'
merged_at: '2025-03-03'
base_branch: develop
head_branch: Default-unknown-api-enums
url: https://github.com/teqplay/poma-backend/pull/190
labels: []
linked_issues: []
explicit_links:
- jira:CC-122
---
# PR #190: Added JsonEnumDefault UNKNOWN to all api enums

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/190  
**State:** closed | **Author:** PimTeqplay  
**Base ← Head:** `develop` ← `Default-unknown-api-enums`  
**Created:** 2025-02-27  
**Merged:** 2025-03-03  

## Description

Will merge to dev once CC-122/PR 189 has been merged

## Commits

- `950835fa` **Pim van den Toorn** (2025-02-27): Put REPARE back, fix when all projects have this update
- `2e189621` **Pim van den Toorn** (2025-02-27): Added JsonEnumDefault UNKNOWN to all api enums

## Reviews

### TeqJoostD — COMMENTED (2025-02-28)

_No comment._

### TeqJoostD — APPROVED (2025-02-28)

_No comment._

## Review Comments

### TeqJoostD — 2025-02-28 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/DatabaseAccessRole.kt`

Why would someone make a database access role an api available model???? When would someone ever need this
