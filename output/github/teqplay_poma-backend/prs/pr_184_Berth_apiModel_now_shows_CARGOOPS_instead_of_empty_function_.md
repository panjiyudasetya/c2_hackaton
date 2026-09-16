---
id: github:teqplay/poma-backend:pr:184
source: github
type: pull_request
repo: teqplay/poma-backend
number: 184
title: Berth apiModel now shows CARGOOPS instead of empty function type sets…
author: PimTeqplay
state: closed
date: '2025-02-21'
merged_at: '2025-02-27'
base_branch: develop
head_branch: CC-122-function-types-for-berth
url: https://github.com/teqplay/poma-backend/pull/184
labels: []
linked_issues: []
explicit_links:
- jira:CC-122
---
# PR #184: Berth apiModel now shows CARGOOPS instead of empty function type sets…

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/184  
**State:** closed | **Author:** PimTeqplay  
**Base ← Head:** `develop` ← `CC-122-function-types-for-berth`  
**Created:** 2025-02-21  
**Merged:** 2025-02-27  

## Description

…, changed enum typo: REPARE->REPAIR (Change DB!)

## Commits

- `169fa96b` **Pim van den Toorn** (2025-02-21): Berth apiModel now shows CARGOOPS instead of empty function type sets, changed enum typo: REPARE->REPAIR (Change DB!)
- `61ca854d` **Pim van den Toorn** (2025-02-27): Added JsonAlias REPARE to deserialize it to the new REPAIR and added UNKNOWN as default

## Reviews

### TeqJoostD — COMMENTED (2025-02-26)

_No comment._

### TeqJoostD — APPROVED (2025-02-27)

_No comment._

## Review Comments

### TeqJoostD — 2025-02-26 on `api/src/main/kotlin/nl/teqplay/poma/api/v1/FunctionType.kt`

Lol, Wouter English

## Comments

### TeqJoostD — 2025-02-26

> …, changed enum typo: REPARE->REPAIR (Change DB!)



How would you see this working in a deployment? Maybe better to deprecate `REPARE` and add `REPAIR` and when the migration is done remove the old field?



Or a solution where we add some sort of @JsonProperty annotation so repare gets deserialized to repair to avoid downtime of the system. And we can do the migration after the deployment. What are your thoughts on this?

### PimTeqplay — 2025-02-27

@TeqJoostD I looked into an annotation to des. repare to repair, but that isn't available and it needs some bulkier code to get that working. I was thinking of running a query over the db, as that takes less than a second. It would have to be done at the same time as deployment, which is easy, but it would also have to be synced with the FE deployment, which might be a bit more of a hassle
