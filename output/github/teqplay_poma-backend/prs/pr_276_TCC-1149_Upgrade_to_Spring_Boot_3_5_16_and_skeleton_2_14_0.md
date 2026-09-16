---
id: github:teqplay/poma-backend:pr:276
source: github
type: pull_request
repo: teqplay/poma-backend
number: 276
title: TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0
author: Darius-Wattimena
state: closed
date: '2026-08-07'
merged_at: '2026-08-10'
base_branch: develop
head_branch: TCC-1149-upgrade-spring-boot-3-5-16
url: https://github.com/teqplay/poma-backend/pull/276
labels: []
linked_issues: []
explicit_links: []
---
# PR #276: TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/276  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1149-upgrade-spring-boot-3-5-16`  
**Created:** 2026-08-07  
**Merged:** 2026-08-10  

## Description

## Summary
- Spring Boot **3.4.12 → 3.5.16**, spring-cloud-kubernetes starter **3.2.1 → 3.3.3** (pairs with Spring Cloud 2025.0.x)
- skeleton **2.12.0-b212.1 → 2.14.0-SNAPSHOT** (Boot 3.5-based; release pin to follow)
- MongoDB driver **4.11.2 → 5.5.2** — Boot 3.5 imports `mongodb-driver-bom`, which has no 4.x line. This also supersedes the old comment about `ArrayCodecProvider` ClassNotFoundException on 4.11.3+.
- springdoc **2.8.5 → 2.8.17**, Jackson **2.18.3 → 2.21.4**, JUnit **5.12.2** / platform **1.12.2** (all aligned with the Boot 3.5.16 BOM)
- `api` module deliberately stays on Jackson 2.18.3: it has no Boot BOM to pin `kotlin.version`, and jackson-module-kotlin 2.21 drags in Kotlin 2.x jars that break the Kotlin 1.9.25 compile

## Test plan
- [x] `./gradlew test ktlintCheck` — green

Part of TCC-1149 (Spring Boot 3.5.16 rollout). Depends on skeleton-plugins 2.14.0 (teqplay/skeleton-plugins#438).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

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

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-07)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — APPROVED (2026-08-10)

_No comment._

## Comments
