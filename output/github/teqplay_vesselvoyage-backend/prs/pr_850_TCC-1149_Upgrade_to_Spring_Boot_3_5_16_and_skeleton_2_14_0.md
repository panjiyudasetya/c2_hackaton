---
id: github:teqplay/vesselvoyage-backend:pr:850
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 850
title: TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0
author: Darius-Wattimena
state: closed
date: '2026-08-07'
merged_at: '2026-08-18'
base_branch: develop
head_branch: TCC-1149-upgrade-spring-boot-3-5-16
url: https://github.com/teqplay/vesselvoyage-backend/pull/850
labels: []
linked_issues: []
explicit_links: []
---
# PR #850: TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/850  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-1149-upgrade-spring-boot-3-5-16`  
**Created:** 2026-08-07  
**Merged:** 2026-08-18  

## Description

## Summary
- Spring Boot **3.4.12 → 3.5.16** in root, `api`, and `client` builds; spring-cloud-kubernetes starter **3.2.1 → 3.3.3**
- skeleton **2.12.2-b220.1 → 2.14.0-b237.1**
- poma **20250304-b34.1 → 20260810-b287.1**
- csi **20250305-b38.1 → 20260811-b242.1**
- ais-engine **20260729-b1494.1 → 20260814-b1581.1**
- springdoc **2.8.6 → 2.8.17**
- MongoDB driver **4.11.0 → 5.5.2** ⚠️ — forced: Boot 3.5 imports `mongodb-driver-bom`, which has no 4.x line
- Test mock adapted to driver 5.x (`listCollectionNames()` returns `ListCollectionNamesIterable`)
- Added `junit-platform-launcher` to test runtime (JUnit platform 1.12 discovery fails against Gradle's bundled launcher)

## Test plan
- [x] `./gradlew test ktlintCheck` — green

Part of TCC-1149 (Spring Boot 3.5.16 rollout).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `5113c8b7` **Darius Wattimena** (2026-08-07): TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0-SNAPSHOT
  - Spring Boot 3.4.12 -> 3.5.16 (root, api, client), spring-cloud-kubernetes 3.2.1 -> 3.3.3
  - skeleton 2.12.2-b220.1 -> 2.14.0-SNAPSHOT (Boot 3.5 based)
  - springdoc 2.8.6 -> 2.8.17
  - MongoDB driver 4.11.0 -> 5.5.2 (Boot 3.5 imports mongodb-driver-bom, no 4.x line)
  - Adapt test mock to driver 5.x ListCollectionNamesIterable
  - Add junit-platform-launcher to test runtime (required by JUnit platform 1.12)
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `8e3f1bef` **Darius Wattimena** (2026-08-10): TCC-1149 Pin skeleton release 2.14.0-b237.1
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `3d0cb551` **Darius Wattimena** (2026-08-10): TCC-1149 Bump poma api to 20260810-b287.1 (Boot 3.5 based)
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `9aa25ffd` **Darius Wattimena** (2026-08-11): TCC-1149 Bump csi to 20260811-b242.1 (Boot 3.5 based)
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `046b25a7` **Darius Wattimena** (2026-08-14): TCC-1149 Bump ais-engine to 20260814-b1581.1 (Boot 3.5 based)
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-07)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F850%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-08-14)

_No comment._

## Review Comments

## Comments
