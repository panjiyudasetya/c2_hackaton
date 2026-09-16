---
id: github:teqplay/vesselvoyage-backend:pr:754
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 754
title: Replace revents NATS flows with RabbitMQ
author: TeqJoostD
state: closed
date: '2026-04-01'
merged_at: null
base_branch: develop
head_branch: revents-rabbitmq-pr
url: https://github.com/teqplay/vesselvoyage-backend/pull/754
labels: []
linked_issues: []
explicit_links: []
---
# PR #754: Replace revents NATS flows with RabbitMQ

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/754  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `revents-rabbitmq-pr`  
**Created:** 2026-04-01  

## Description

## Summary
- switch revents event intake from the deprecated NATS path to RabbitMQ
- switch revents change publishing from `nats.change-stream` to RabbitMQ
- clean up stale shared revents change-stream config/test references

## Verification
- JDK 17 `ReventsApplicationTest`
- `service.queue.*`
- `service.queue.events.*`
- `service.publisher.*`


---
Pull Request opened by [Augment Code](https://www.augmentcode.com/) with guidance from the PR author

## Commits

- `d3f84069` **Augment Test** (2026-04-01): Replace revents NATS flows with RabbitMQ
  Agent-Id: agent-4ad4c40b-ac03-462c-bd87-3401a86678fc
- `13265784` **Augment Test** (2026-04-01): Run ktlint format
  Agent-Id: agent-4ad4c40b-ac03-462c-bd87-3401a86678fc
- `2af680dc` **TeqJoostD** (2026-04-10): fix
- `ef0bed38` **TeqJoostD** (2026-04-10): fix
- `8c54286f` **TeqJoostD** (2026-04-10): fix
- `0a892c0e` **TeqJoostD** (2026-04-10): fix
- `e57f967d` **TeqJoostD** (2026-04-10): fix
- `1eff8296` **TeqJoostD** (2026-04-15): fix
- `f76d0f0e` **TeqJoostD** (2026-04-15): fix
- `efe8a87f` **TeqJoostD** (2026-04-15): fix
- `53b87440` **TeqJoostD** (2026-04-15): fix
- `e29c40b3` **TeqJoostD** (2026-04-17): fix

## Reviews

### augmentcode[bot] — COMMENTED (2026-04-01)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F754%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments
