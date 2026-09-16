---
id: github:teqplay/vesselvoyage-backend:pr:742
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 742
title: Ensure Redis connects only when enabled
author: michel-teqplay
state: closed
date: '2026-03-19'
merged_at: '2026-03-26'
base_branch: develop
head_branch: TCC-823_conditional-redis
url: https://github.com/teqplay/vesselvoyage-backend/pull/742
labels: []
linked_issues: []
explicit_links: []
---
# PR #742: Ensure Redis connects only when enabled

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/742  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-823_conditional-redis`  
**Created:** 2026-03-19  
**Merged:** 2026-03-26  

## Description

_No description._

## Commits

- `e00e02be` **Michel Wilson** (2026-03-19): Only connect to Redis when we enable it, disable Spring magic
- `e0a42974` **Michel Wilson** (2026-03-19): Fix keyspace events

## Reviews

### michel-teqplay — COMMENTED (2026-03-19)

_No comment._

### augmentcode[bot] — COMMENTED (2026-03-19)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F742%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — APPROVED (2026-03-25)

_No comment._

## Review Comments

### michel-teqplay — 2026-03-19 on `src/main/resources/application.properties`

This change is kinda unrelated but helps with local testing: when the sentinel keys are present but empty the application won't start if you don't supply any actual values if Redis is enabled.

## Comments
