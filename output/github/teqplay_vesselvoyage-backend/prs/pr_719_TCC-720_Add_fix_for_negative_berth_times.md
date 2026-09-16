---
id: github:teqplay/vesselvoyage-backend:pr:719
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 719
title: TCC-720 Add fix for negative berth times
author: TeqJoostD
state: closed
date: '2026-02-19'
merged_at: '2026-03-02'
base_branch: develop
head_branch: TCC-720
url: https://github.com/teqplay/vesselvoyage-backend/pull/719
labels: []
linked_issues: []
explicit_links: []
---
# PR #719: TCC-720 Add fix for negative berth times

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/719  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-720`  
**Created:** 2026-02-19  
**Merged:** 2026-03-02  

## Description

_No description._

## Commits

- `13069a17` **TeqJoostD** (2026-02-19): Add fix for negative berth times
- `0b2bf866` **TeqJoostD** (2026-02-19): ktlint
- `0584417c` **TeqJoostD** (2026-03-02): Change of logic and adjusting test
- `008e826f` **TeqJoostD** (2026-03-02): Small feedback

## Reviews

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. I found one potential logic issue in the duplicate detection that could cause valid events to be incorrectly ignored.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-02-19)

Review completed. The implementation correctly handles duplicate stop start events and out-of-order events. The logic is well-tested with comprehensive test coverage.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### augmentcode[bot] — COMMENTED (2026-02-19)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F719%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-19)

## Pull request overview

This PR addresses incorrect stop/berth timelines (notably negative durations) by improving how stop start/end events are handled when events arrive out-of-order or are duplicated.

**Changes:**
- Add logic to StopStartProcessor to (a) ignore certain duplicate stop start events and (b) create a bounded stop when a stop start arrives before the currently ongoing stop’s start time.
- Allow StopEndProcessor to match and override stops that were fallback-ended by a later stop start (in addition to EOSP fallback).
- Add test coverage for duplicate stop start handling, out-of-order stop start bounding, and overriding fallback-ended stops with real end events.

### Reviewed changes

Copilot reviewed 4 out of 4 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt | Adds tests for duplicate/out-of-order stop start behavior and fallback-end override behavior. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt | Implements duplicate detection + out-of-order bounding to prevent negative stop durations. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopEndProcessor.kt | Expands match logic so real end events can override STOP_START fallback-ended stops. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopBaseProcessor.kt | Allows stop update lambda to return null so callers can short-circuit (e.g., duplicates). |

### augmentcode[bot] — COMMENTED (2026-03-02)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### augmentcode[bot] — COMMENTED (2026-03-02)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F719%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-03-02)

_No comment._

### augmentcode[bot] — COMMENTED (2026-03-02)

Review completed. 1 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F719%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — COMMENTED (2026-03-02)

_No comment._

### Darius-Wattimena — APPROVED (2026-03-02)

_No comment._

## Review Comments

### TeqJoostD — 2026-03-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopEndProcessor.kt`

Should not be possible

### TeqJoostD — 2026-03-02 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt`

it does copy the location?


## Comments

### TeqJoostD — 2026-03-02

augment review

### TeqJoostD — 2026-03-02

augment review
