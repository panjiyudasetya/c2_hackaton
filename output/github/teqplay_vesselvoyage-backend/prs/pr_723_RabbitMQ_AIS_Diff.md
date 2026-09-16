---
id: github:teqplay/vesselvoyage-backend:pr:723
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 723
title: RabbitMQ AIS Diff
author: TeqJoostD
state: closed
date: '2026-03-04'
merged_at: '2026-03-06'
base_branch: develop
head_branch: TCC-720
url: https://github.com/teqplay/vesselvoyage-backend/pull/723
labels: []
linked_issues: []
explicit_links: []
---
# PR #723: RabbitMQ AIS Diff

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/723  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-720`  
**Created:** 2026-03-04  
**Merged:** 2026-03-06  

## Description

_No description._

## Commits

- `219ef17b` **TeqJoostD** (2026-03-04): Rabbitmq ais diff consumer
- `57ec5840` **TeqJoostD** (2026-03-04): Merge branch 'develop' into TCC-720
  # Conflicts:
  #	build.gradle
- `d00b219e` **TeqJoostD** (2026-03-04): RabbitMQ FIX
- `1ea469c4` **Joost Dambrink** (2026-03-05): Merge branch 'develop' into TCC-720
- `5cec0c9c` **TeqJoostD** (2026-03-05): Add lane mechanism for better consumption
- `2997fb97` **TeqJoostD** (2026-03-05): Merge remote-tracking branch 'origin/TCC-720' into TCC-720
- `92a66ab3` **TeqJoostD** (2026-03-05): Improve speed
- `03aaa8b1` **TeqJoostD** (2026-03-05): Improve speed even more
- `d1d23c3a` **TeqJoostD** (2026-03-05): Fix dropping messages issue
- `4179dfc6` **TeqJoostD** (2026-03-06): Stop dropping messages

## Reviews

### Darius-Wattimena — CHANGES_REQUESTED (2026-03-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-03-04)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F723%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — DISMISSED (2026-03-05)

_No comment._

### Darius-Wattimena — CHANGES_REQUESTED (2026-03-05)

_No comment._

### Darius-Wattimena — APPROVED (2026-03-06)

_No comment._

## Review Comments

### Darius-Wattimena — 2026-03-04 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/RabbitMqAisStreamingConsumerService.kt`

This is not what we want? Don't consume anything until it is ready? Dropping means losing data

### Darius-Wattimena — 2026-03-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/RabbitMqAisStreamingConsumerService.kt`

Doesn't this just drop the message if we are not ready yet? This will basically mean data lose the first 2/3 minutes until the application is ready?

Because `return` at this point will just ack the message later.

## Comments
