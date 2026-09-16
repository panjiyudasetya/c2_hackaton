---
id: github:teqplay/vesselvoyage-backend:pr:809
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 809
title: Merge back-to-back bunker encounters with the same vessel during live processing
author: michel-teqplay
state: closed
date: '2026-07-06'
merged_at: '2026-07-08'
base_branch: develop
head_branch: TCC-975-merge-encounters
url: https://github.com/teqplay/vesselvoyage-backend/pull/809
labels: []
linked_issues: []
explicit_links: []
---
# PR #809: Merge back-to-back bunker encounters with the same vessel during live processing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/809  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-975-merge-encounters`  
**Created:** 2026-07-06  
**Merged:** 2026-07-08  

## Description

## Summary
- `EncounterStartProcessor` now resumes a recently closed (<1h) BUNKER encounter with the same vessel instead of always starting a new one
- Prevents a bunkering operation that's briefly interrupted from being split into separate encounters during live processing

## Test plan
- [x] Added `EncounterStartProcessorTest` covering merge and non-merge scenarios

## Commits

- `ac6d015e` **Michel Wilson** (2026-07-01): Merge back-to-back bunker encounters with the same vessel during live processing
  EncounterStartProcessor now resumes a recently closed (<1h) BUNKER encounter
  with the same vessel instead of always creating a new one, so a bunkering
  operation that's briefly interrupted isn't split into separate encounters.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-06)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F809%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-08)

_No comment._

## Review Comments

## Comments
