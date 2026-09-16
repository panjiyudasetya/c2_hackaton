---
id: github:teqplay/vesselvoyage-backend:pr:804
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 804
title: 'feat(recalculation): add excludeBarges option to port recalculation'
author: TeqJoostD
state: closed
date: '2026-06-29'
merged_at: '2026-07-01'
base_branch: develop
head_branch: TCC-1012
url: https://github.com/teqplay/vesselvoyage-backend/pull/804
labels: []
linked_issues: []
explicit_links: []
---
# PR #804: feat(recalculation): add excludeBarges option to port recalculation

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/804  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TCC-1012`  
**Created:** 2026-06-29  
**Merged:** 2026-07-01  

## Description

## What
Adds an `excludeBarges` option to port recalculation so a port-wide recalc can drop barge data.

- `POST /v2/recalculate/port/{unlocode}` gains `?excludeBarges=true` (default `false`).
- Threaded through `recalculateByPort` → `createScenarioRequestForPort` → revents `Scenario.Settings.excludeBarges`.

This targets the **port** flow specifically: revents resolves which ships are in the port, so only revents can drop the barges among them (vesselvoyage never sees those ship IDs). Explicit ship/batch recalcs already select their ships, so they are intentionally left untouched.

## Dependency
Relies on the revents `Scenario.Settings.excludeBarges` field from ais-engine (PR #1527, merged to develop), published in `20260630-SNAPSHOT`. `aisengine_version` is bumped accordingly. A ship is treated as a barge when it has **no IMO and no role**.

## Tests
- `ReventsConversionServiceTest` covers excludes-barges-when-requested and keeps-barges-by-default.
- Compiles and tests pass against the bumped dependency.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `03433534` **TeqJoostD** (2026-06-29): feat(recalculation): add excludeBarges option to port recalculation
  Expose `excludeBarges` on POST /v2/recalculate/port/{unlocode} and thread
  it through to the revents `Scenario.Settings.excludeBarges` flag, so a
  port recalculation can drop barge data. Revents resolves the port's ships
  and applies the filter.
  
  Requires bumping `aisengine_version` to a build containing the revents
  `Scenario.Settings.excludeBarges` field (see TODO in build.gradle); it
  does not compile until then.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `f884ec63` **TeqJoostD** (2026-06-30): chore(deps): bump aisengine_version to 20260630-SNAPSHOT for excludeBarges
  The revents Scenario.Settings.excludeBarges field (ais-engine PR #1527,
  merged to develop) is published in 20260630-SNAPSHOT. Bumping unblocks the
  port recalculation excludeBarges option, which now compiles and tests pass.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `e50b5c1e` **TeqJoostD** (2026-06-30): test: fix createScenarioRequestForPort matcher count in recalculateByPort test
  Add the missing matcher for the new excludeBarges parameter in the stub and
  verify of ReventsRecalculationServiceTest, fixing InvalidUseOfMatchersException.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `c05b10d1` **TeqJoostD** (2026-07-01): chore(deps): bump aisengine_version to 20260701-b1433.1
  Pin the released ais-engine build containing the revents
  Scenario.Settings.excludeBarges field.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-06-30)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F804%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### michel-teqplay — APPROVED (2026-07-01)

_No comment._

## Review Comments

## Comments
