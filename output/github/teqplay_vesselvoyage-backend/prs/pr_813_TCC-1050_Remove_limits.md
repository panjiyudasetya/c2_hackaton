---
id: github:teqplay/vesselvoyage-backend:pr:813
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 813
title: TCC-1050 Remove limits
author: Darius-Wattimena
state: closed
date: '2026-07-07'
merged_at: '2026-07-10'
base_branch: develop
head_branch: remove-limits
url: https://github.com/teqplay/vesselvoyage-backend/pull/813
labels: []
linked_issues: []
explicit_links: []
---
# PR #813: TCC-1050 Remove limits

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/813  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `remove-limits`  
**Created:** 2026-07-07  
**Merged:** 2026-07-10  

## Description

_No description._

## Commits

- `2d98f498` **Darius Wattimena** (2026-07-07): Remove limiting of visit and voyages in VesselVoyage
- `f559bd7e` **Darius Wattimena** (2026-07-07): Update tests to reflect the removal of limiting
- `38a491d3` **Darius Wattimena** (2026-07-07): Fix outdated documentation about removed limiting
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-07)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F813%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — COMMENTED (2026-07-07)

_No comment._

### Darius-Wattimena — COMMENTED (2026-07-07)

_No comment._

### michel-teqplay — APPROVED (2026-07-07)

_No comment._

### TeqJoostD — APPROVED (2026-07-07)

_No comment._

## Review Comments

### Darius-Wattimena — 2026-07-07 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/Entry.kt`

Reworded the KDoc to "50 or more activities" to match the historical `>= 50` threshold (commit 38a491d3).

_🤖 Addressed by [Claude Code](https://claude.com/claude-code)_

### Darius-Wattimena — 2026-07-07 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt`

Removed the outdated step 4 about limiting the voyage from the `getResultOnVoyage` KDoc (commit 38a491d3).

_🤖 Addressed by [Claude Code](https://claude.com/claude-code)_

## Comments
