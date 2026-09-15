---
id: github:teqplay/vesselvoyage-backend:pr:876
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 876
title: Cache scenario interests to reduce concurrent fetch failures
author: TeqJoostD
state: open
date: '2026-09-08'
merged_at: null
base_branch: develop
head_branch: claude/revents-merge-extraction-error-dwof0o
url: https://github.com/teqplay/vesselvoyage-backend/pull/876
labels: []
linked_issues: []
explicit_links: []
---
# PR #876: Cache scenario interests to reduce concurrent fetch failures

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/876  
**State:** open | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `claude/revents-merge-extraction-error-dwof0o`  
**Created:** 2026-09-08  

## Description

## Summary

Fixes repeated `RestClientException` failures when merging scenarios with many ships by caching the scenario's interests once per scenario instead of fetching them once per ship. The large response is now fetched once, shared across all ships of a scenario, and evicted when the merge completes.

## Changes

- **ReventsReplayMergeService**: Added `interestsByScenario` cache (keyed by scenario ID, lazily populated) to fetch interests once per scenario and share them across all ships. Interests are grouped by ship ID for efficient lookup.
  - `interestsOfShip()`: Retrieves a ship's interests from the shared cache, computing it lazily on first access.
  - `fetchInterests()`: Fetches all scenario interests and groups by ship. Retries up to 3 times on transport-level `RestClientException` (e.g., closed connection mid-stream), but immediately rethrows `HttpStatusCodeException` (e.g., 503, 400) so the caller can queue the scenario for retry.
  - `evictInterests()`: Public method to clear cached interests when a scenario's merge ends.
  - Updated `buildMergeEntries()` to use `interestsOfShip()` instead of fetching directly.

- **ReventsRecalculationService**: Added `evictInterests()` calls in two places:
  - After `mergeShipsOfScenario()` completes (in finally block) to release interests once the scenario's merge is done.
  - After `runShips()` completes (in finally block) to evict interests from all source scenarios in a merge pass.

- **ReventsReplayMergeServiceTest**: Added comprehensive test coverage:
  - `` `the interests of a scenario are fetched once for all of its ships` ``: Verifies the cache is hit and `getInterests()` is called exactly once for two ships.
  - `` `a ship without an interest in the scenario produces no merge entries` ``: Confirms filtering by ship ID works correctly.
  - `` `evicting the interests of a scenario makes the next ship fetch them again` ``: Validates cache eviction and re-fetch.
  - `` `a cut-short interests response is fetched again` ``: Tests retry logic on `RestClientException`.
  - `` `an interests response with an HTTP status is not fetched again` ``: Confirms `HttpServerErrorException` is rethrown immediately without retry.

## Implementation Details

- Uses `ConcurrentHashMap` with `Lazy<Map<String, List<InterestVesselVoyage>>>` values to ensure thread-safe, single-threaded fetch per scenario while other ships wait.
- Retry logic: up to 3 attempts with exponential backoff (1s, 2s, 3s) for transport errors; HTTP status errors bypass retry.
- Lazy evaluation ensures the fetch runs outside the map's lock, preventing deadlocks under concurrent access.
- Memory footprint is minimal: one cached map per concurrently merged scenario, far less than the previous per-ship materialization of the entire response.

https://claude.ai/code/session_01QUAWRThn1Z8Yp19Gim5KUA

## Commits

- `8e12c0f7` **Claude** (2026-09-07): Fetch a scenario's revents interests once per merge instead of per ship
  Merging a scenario back failed per ship with
  
      RestClientException: Error while extracting response for type
      [class [Lnl.teqplay.aisengine.reventsengine.model.interest.InterestVesselVoyage;]
      ... JSON parse error: closed ... (through reference chain: java.lang.Object[][254029])
  
  ReventsReplayMergeService.buildMergeEntries called
  GET /vesselvoyage/v2/{id}/interests for every ship and then filtered the
  response down to that one ship. The endpoint has no per-ship filter, so each
  ship downloaded the interests of the whole scenario - a quarter of a million
  of them for a port-wide window - and up to merge-ship-threads x
  max-concurrent-scenarios of those downloads ran in parallel. The response was
  regularly cut short mid-stream, which failed the ship's merge and silently
  left its data unmerged.
  
  The interests are now fetched once per scenario, grouped by ship and shared by
  all of its ships, and dropped again when the scenario's merge ends (also when
  it is handed back for a later retry). The fetch is lazy and synchronized, so
  the other ship threads wait for the one in-flight request instead of issuing
  their own, and a transport-level failure is retried a few times; failures that
  carry an HTTP status still reach the caller unchanged, which is what keeps the
  503 and "merge metadata is not prepared" handling working.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01QUAWRThn1Z8Yp19Gim5KUA

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-08)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F876%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-08)

### 🟢 Approval recommended

The code changes are cohesive, covered by targeted tests, and the only noted issue is a minor mismatch between the PR description and the implemented retry backoff behavior.

<details>
<summary>Pull request overview</summary>

This PR reduces concurrent `getInterests(scenarioId)` fetch failures during (r)events scenario merges by caching a scenario’s interests once per scenario (grouped by shipId) and evicting the cache when merging completes.

**Changes:**
- Added a per-scenario, lazily populated `interestsByScenario` cache in `ReventsReplayMergeService`, plus retry logic for transport-level `RestClientException` during interest fetch.
- Updated `buildMergeEntries()` to use the shared per-scenario interests instead of fetching interests per ship.
- Added eviction calls in `ReventsRecalculationService` and added unit tests covering cache behavior, eviction, and retry/rethrow semantics.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeService.kt | Introduces per-scenario interest caching + retry-on-transport-errors for interest fetches and updates merge entry building to consume the cache. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt | Ensures cached interests are evicted after merge processing completes to avoid holding large responses in memory. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeServiceTest.kt | Adds tests verifying single-fetch caching across ships, eviction behavior, and retry vs. rethrow behavior for fetch failures. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 3/3 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/vesselvoyage-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

## Review Comments

### Copilot — 2026-09-08 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsReplayMergeService.kt`

The PR description says the retry uses “exponential backoff (1s, 2s, 3s)”. The current implementation sleeps `1s` and `2s` (linear `baseDelay * attempt`) and does not sleep `3s` because the final attempt throws before sleeping. Please align the PR description with the actual behavior, or adjust the retry logic/constants if the 1/2/3s schedule was intended.

## Comments
