---
id: github:teqplay/poma-backend:pr:277
source: github
type: pull_request
repo: teqplay/poma-backend
number: 277
title: Release 10 Aug 2026
author: Darius-Wattimena
state: closed
date: '2026-08-10'
merged_at: '2026-08-10'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/poma-backend/pull/277
labels: []
linked_issues: []
explicit_links: []
---
# PR #277: Release 10 Aug 2026

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/277  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-08-10  
**Merged:** 2026-08-10  

## Description

_No description._

## Commits

- `6e5907a0` **Darius Wattimena** (2026-08-07): TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0-SNAPSHOT
  - Spring Boot 3.4.12 -> 3.5.16, spring-cloud-kubernetes 3.2.1 -> 3.3.3
  - skeleton 2.12.0-b212.1 -> 2.14.0-SNAPSHOT (Boot 3.5 based)
  - MongoDB driver 4.11.2 -> 5.5.2 (Boot 3.5 imports mongodb-driver-bom, no 4.x line)
  - springdoc 2.8.5 -> 2.8.17, Jackson 2.18.3 -> 2.21.4 (BOM-aligned), JUnit 5.12.2/1.12.2
  - api module keeps Jackson 2.18.3: no Boot BOM there, and Jackson 2.21 pulls Kotlin 2.x metadata incompatible with Kotlin 1.9.25
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `d666e420` **Darius Wattimena** (2026-08-10): TCC-1149 Pin skeleton release 2.14.0-b237.1
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `3ab59d30` **Darius Wattimena** (2026-08-10): Merge pull request #276 from teqplay/TCC-1149-upgrade-spring-boot-3-5-16
  TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0

## Reviews

### michel-teqplay — APPROVED (2026-08-10)

_No comment._

### augmentcode[bot] — COMMENTED (2026-08-10)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Comments
