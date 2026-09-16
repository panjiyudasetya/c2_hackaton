---
id: github:teqplay/vesselvoyage-backend:pr:810
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 810
title: Add CLAUDE.md with AI agent rules
author: michel-teqplay
state: closed
date: '2026-07-06'
merged_at: '2026-07-08'
base_branch: develop
head_branch: TC-840-ai-rules
url: https://github.com/teqplay/vesselvoyage-backend/pull/810
labels: []
linked_issues: []
explicit_links: []
---
# PR #810: Add CLAUDE.md with AI agent rules

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/810  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TC-840-ai-rules`  
**Created:** 2026-07-06  
**Merged:** 2026-07-08  

## Description

## Summary
- Adds a `CLAUDE.md` at the repo root with AI-agent coding rules for VesselVoyage.
- Based on the earlier ruleset drafted for Augment (`~/teqplay-augment-rules.md`), but verified against the actual codebase and trimmed/corrected:
  - Fixed the mocking library: this repo uses `com.nhaarman.mockitokotlin2`, not `org.mockito.kotlin`.
  - Replaced the elaborate module-level `BaseTest` Spring integration test guidance with a short note — only `ApplicationTest.kt` actually uses `@SpringBootTest`; the rest of the ~800 tests are plain JUnit 5 + manual mocks.
  - Added sections not previously covered: module orientation (root/`api`/`client`), error handling (skeleton exceptions, no `@ControllerAdvice`), and auth (`@PreAuthorize` + `AuthResource`/`AuthOperation`).
  - Trimmed the generic skeleton-plugin catalog and Kubernetes/Redis/RabbitMQ subsections down to what's actually used here.

## Test plan
- [x] Read through the file for accuracy against sampled source/test files.
- N/A for automated tests — this is a documentation-only change (no code paths affected).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `041860c7` **Michel Wilson** (2026-07-06): Add CLAUDE.md with AI agent rules for this repo
  Derived from the earlier Augment ruleset, corrected against the actual
  codebase (e.g. mockito-kotlin package, Spring test usage) and trimmed to
  what's actually used here.
  
  Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
- `8cf6a542` **Michel Wilson** (2026-07-08): Merge remote-tracking branch 'origin/develop' into TC-840-ai-rules

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-06)

Review completed. 5 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F810%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-08)

_No comment._

## Review Comments

## Comments
