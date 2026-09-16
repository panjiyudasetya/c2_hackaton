---
id: github:teqplay/vesselvoyage-backend:pr:824
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 824
title: Use globalObjectMapper in slackError to support Instant serialization
author: Darius-Wattimena
state: closed
date: '2026-07-21'
merged_at: '2026-07-23'
base_branch: develop
head_branch: fix/slack-error-jackson-instant
url: https://github.com/teqplay/vesselvoyage-backend/pull/824
labels: []
linked_issues: []
explicit_links: []
---
# PR #824: Use globalObjectMapper in slackError to support Instant serialization

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/824  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix/slack-error-jackson-instant`  
**Created:** 2026-07-21  
**Merged:** 2026-07-23  

## Description

## Problem
Processing a `UniqueBerthEndEvent` whose berth end precedes the start triggered the Slack error notification path, which serialized the event with a bare `jacksonObjectMapper()`. That mapper has no JSR-310 module, so serializing `actualTime: Instant` threw `InvalidDefinitionException` — and because this happens inside event processing, the whole message was dropped instead of just failing the Slack notification.

## Fix
Use the already-configured `globalObjectMapper` (registers `JavaTimeModule`) instead of constructing a bare mapper per call. This was the only bare `jacksonObjectMapper()` left in the codebase.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `0d52bea2` **Darius Wattimena** (2026-07-21): Use globalObjectMapper in slackError to support Instant serialization
  The bare jacksonObjectMapper() lacked the JSR-310 module, so serializing
  the event's actualTime threw InvalidDefinitionException and the whole
  message was dropped during event processing.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `9256bd45` **Darius Wattimena** (2026-07-21): Make the berth-end Slack notification best-effort
  Review feedback: serialization or Slack failures in slackError could
  still bubble up and drop the message being processed. Wrap the whole
  notification in a try/catch and log a warning instead.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-21)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F824%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-22)

_No comment._

## Review Comments

## Comments
