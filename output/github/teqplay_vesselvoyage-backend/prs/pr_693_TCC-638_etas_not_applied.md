---
id: github:teqplay/vesselvoyage-backend:pr:693
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 693
title: TCC-638 etas not applied
author: Darius-Wattimena
state: closed
date: '2026-01-09'
merged_at: '2026-01-12'
base_branch: develop
head_branch: TCC-638-etas-not-applied
url: https://github.com/teqplay/vesselvoyage-backend/pull/693
labels: []
linked_issues: []
explicit_links: []
---
# PR #693: TCC-638 etas not applied

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/693  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-638-etas-not-applied`  
**Created:** 2026-01-09  
**Merged:** 2026-01-12  

## Description

_No description._

## Commits

- `7f1ed86b` **Darius Wattimena** (2026-01-09): Enhance ship ID resolution by adding support for IMO lookup when MMSI is not found
- `adb751b9` **Darius Wattimena** (2026-01-09): Merge branch 'develop' into TCC-638-etas-not-applied
- `7bd8911d` **Darius Wattimena** (2026-01-09): Make comment more clear
- `99234684` **Darius Wattimena** (2026-01-09): Refactor assertions in StaticShipInfoServiceTest to use assertNotNull for clarity
- `98a844cb` **Darius Wattimena** (2026-01-09): Adjusted all places where assert was used to use junit methods
- `e0411b27` **Darius Wattimena** (2026-01-09): Refactor StaticShipInfoServiceTest to reduce mock declarations
- `2a3723e2` **Darius Wattimena** (2026-01-09): Refactor StaticShipInfoServiceTest to use parameterized tests for ship ID retrieval

## Reviews

### github-actions[bot] — COMMENTED (2026-01-09)

Review completed. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-09)

## Pull request overview

This pull request addresses TCC-638 by adding fallback logic to the `getShipIdByMmsi` method to handle sea vessels that have IMO numbers but are not in the MMSI cache. The change enables the system to find ship IDs for sea vessels by looking up their IMO via MMSI mapping when a direct MMSI lookup fails.

Key changes:
- Enhanced `getShipIdByMmsi` to fall back to IMO-based lookup when MMSI lookup returns null
- Added comprehensive test coverage for `getShipIdByImo` and `getShipIdByMmsi` methods with both positive and negative test cases

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 4 comments.

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoService.kt | Added fallback logic in `getShipIdByMmsi` to query by IMO when MMSI lookup fails, handling sea vessels not in the MMSI cache |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt | Added five new test methods covering ship ID lookup by IMO and MMSI for different vessel types (barges vs sea vessels) and edge cases |

### github-actions[bot] — COMMENTED (2026-01-09)

Review completed. No suggestions at this time.

### augmentcode[bot] — COMMENTED (2026-01-09)

Review completed. 1 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F693%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-01-09)

_No comment._

### github-actions[bot] — COMMENTED (2026-01-09)

Review completed. No suggestions at this time.

### TeqJoostD — APPROVED (2026-01-09)

_No comment._

### github-actions[bot] — COMMENTED (2026-01-09)

Review completed. No suggestions at this time.

## Review Comments

### Copilot — 2026-01-09 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt`

There is significant code duplication across all five new test methods. Each test repeats the same setup code for creating mocks and initializing the StaticShipInfoService. Consider extracting this common setup into a helper method or using a @BeforeEach method to reduce duplication and improve maintainability.

### Copilot — 2026-01-09 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt`

Use `assertNotNull()` instead of `assert()` for better test readability and more descriptive failure messages. The standard JUnit assertion provides clearer error messages when tests fail.

### Copilot — 2026-01-09 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt`

Use `assertNotNull()` instead of `assert()` for better test readability and more descriptive failure messages. The standard JUnit assertion provides clearer error messages when tests fail.

### Copilot — 2026-01-09 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt`

Use `assertNotNull()` instead of `assert()` for better test readability and more descriptive failure messages. The standard JUnit assertion provides clearer error messages when tests fail.

### TeqJoostD — 2026-01-09 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/StaticShipInfoServiceTest.kt`

please do the following:

val imos = listOf(IMO_1, IMO_2)

list.forEach { imo ->
    assert(staticShipInfoService.getShipIdByImo(imo)
}

I cannot approve otherwise sorry.

## Comments

### TeqJoostD — 2026-01-09

augment review
