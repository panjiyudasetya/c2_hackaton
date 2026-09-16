---
id: github:teqplay/vesselvoyage-backend:pr:748
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 748
title: Release 25 Mar 2026
author: Darius-Wattimena
state: closed
date: '2026-03-25'
merged_at: '2026-03-25'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/748
labels: []
linked_issues: []
explicit_links: []
---
# PR #748: Release 25 Mar 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/748  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-03-25  
**Merged:** 2026-03-25  

## Description

_No description._

## Commits

- `b586b9e7` **Darius Wattimena** (2026-03-09): Add support for event processing via RabbitMQ
- `3786b532` **Darius Wattimena** (2026-03-10): ktlint
- `caf6059b` **Darius Wattimena** (2026-03-10): Adjusted ais and event processing to not use a ready latch but instead create the listener only when ready to process using a custom configuration class
- `70ead8d5` **Darius Wattimena** (2026-03-11): Clean up code
- `5b4bdddb` **Darius Wattimena** (2026-03-11): Update default refresh time to no be aligned with other applications
- `9924fa00` **Darius Wattimena** (2026-03-16): Merge branch 'develop' into TCC-783-rabbitmq-event-consuming
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/ProcessingService.kt
- `ce5fc34b` **Darius Wattimena** (2026-03-16): Merge pull request #730 from teqplay/TCC-783-rabbitmq-event-consuming
  TCC-783 rabbitmq event consuming
- `5a63caf8` **Darius Wattimena** (2026-03-18): Merge pull request #741 from teqplay/master
  Sync hotfix changes back to develop branch
- `f011c91d` **Jamie de Leest** (2026-03-20): update codecov badge
- `ab2cb343` **jamie-teqplay** (2026-03-20): Merge pull request #747 from teqplay/DEV-1444-update-codecov
  DEV-1444 update codecov

## Reviews

### michel-teqplay — APPROVED (2026-03-25)

_No comment._

### augmentcode[bot] — COMMENTED (2026-03-25)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F748%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments
