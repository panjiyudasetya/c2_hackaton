---
id: github:teqplay/vesselvoyage-backend:pr:874
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 874
title: Let every revents recalculation state its amount of parallel jobs, and grow
  the develop Mongo claim
author: TeqJoostD
state: open
date: '2026-09-03'
merged_at: null
base_branch: develop
head_branch: claude/parallel-jobs-config-delay-hvvlty
url: https://github.com/teqplay/vesselvoyage-backend/pull/874
labels: []
linked_issues: []
explicit_links: []
---
# PR #874: Let every revents recalculation state its amount of parallel jobs, and grow the develop Mongo claim

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/874  
**State:** open | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `claude/parallel-jobs-config-delay-hvvlty`  
**Created:** 2026-09-03  

## Description

## What

Every recalculation that creates a revents scenario now takes an optional `parallelJobs`, passed on as the `parallelJobs` scenario setting: how many parallel revents jobs the resolved ships are spread over.

| Endpoint | Effect |
|:---------|:-------|
| `POST /v2/recalculate/port/{unlocode}` | spreads the port's resolved ships over that many jobs |
| `POST /v2/recalculate/ship/batch` | spreads the requested ships over that many jobs |
| `POST /v2/recalculate/ship/{shipId}` | accepted, but a single ship always replays on one job (see below) |

- **Leaving it out keeps each flow exactly as it is today.** The parameter is optional-with-no-value rather than defaulting to 1, so a port still auto-distributes (as develop now does) and a ship batch is still distributed by revents based on how many ships it resolves. Defaulting it to 1 would have silently switched that automatic distribution off.
- Rejected with a 400 outside `1..25`, validated once for all three endpoints.
- Re-running a scenario (`POST /v2/recalculate/scenario/{id}`) copies the original request, so it keeps the amount it was created with.

### Why a single ship is always one job

revents groups resolved interests per ship and never uses more jobs than there are ships, because a ship's story has to be replayed in one place to merge back. So `parallelJobs` on `/ship/{shipId}` is a no-op; it is accepted for consistency and documented as such in the KDoc and the Swagger description rather than silently ignored.

Automatic recalculation is left alone: its batches are scheduler-driven with no caller to state a value, so revents keeps deriving the amount.

## Also in here: the develop Mongo volume claim

`helm/values.processing-dev.yaml` raises `mongodb.persistence.size` from `430Gi` to `500Gi`, because the deploy failed on the claim in the chart no longer matching the volume actually provisioned for the develop environment. Unrelated to the rest of this PR, but carried here by request rather than as its own PR. `processing-prod` (430Gi) and `processing-data` (400Gi) are untouched.

## Changes

- `ProcessingRecalculateV2Controller` — `parallelJobs` on the port, ship-batch and single-ship endpoints, documented for Swagger.
- `ReventsRecalculationService` — `recalculateByPort` / `recalculateByShips` / `recalculateByShip` take it, with one shared `validateParallelJobs`.
- `ReventsConversionService` — all three `createScenarioRequestFor…` functions set `Scenario.Settings.parallelJobs`.
- Tests for the bounds and the pass-through on each path; existing port/ship tests updated for the added argument, which is matched with `anyOrNull()` since it is nullable and `any()` does not match null.
- `helm/values.processing-dev.yaml` — the volume claim above.

## ⚠️ The ais-engine version is a temporary snapshot

`aisengine_version` points at `20260909-SNAPSHOT`, published from the branch of teqplay/ais-engine#1587 so this branch compiles and can be reviewed. A dated snapshot is the same coordinate for every non-master ais-engine build that day, so **this must become a released version before merging**:

1. teqplay/ais-engine#1587
2. release ais-engine
3. re-point `aisengine_version` at that release
4. merge this

## CI

`Test & build` is green: compiles against the snapshot, all 2418 tests pass, ktlint clean. The SonarCloud quality gate reports *B Maintainability Rating on New Code* — no defects; the likely cause is that adding a parameter tipped six recalculation functions from 7 to 8-9 parameters (`kotlin:S107`). Grouping the optional flags into an options object is the fix, deliberately left out of this PR.

The UI control lives in teqplay/vesselvoyage#170, the scenario setting in teqplay/ais-engine#1587.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM

## Commits

- `6238c42e` **Claude** (2026-09-03): Let a port recalculation state its amount of parallel jobs
  `POST /v2/recalculate/port/{unlocode}` takes an optional `parallelJobs`,
  which is passed to revents as the `parallelJobs` scenario setting: the
  amount of parallel jobs the port's ships are spread over. It defaults to 1
  (everything on a single job, the current behaviour) and is rejected with a
  400 outside of 1..25.
  
  Spreading a port over multiple jobs is opted in to explicitly, as the
  interest distribution it uses reintroduces the duplicate visits that
  `useInterestDistribution = false` guards against for ports with S2S ports.
  
  Note this needs the ais-engine version carrying the `parallelJobs` setting.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `156f58b6` **Claude** (2026-09-09): Let every revents recalculation state its amount of parallel jobs
  The parallel jobs setting was only reachable through the port recalculation.
  Every recalculation that creates a revents scenario now takes it:
  
  - POST /v2/recalculate/port/{unlocode}
  - POST /v2/recalculate/ship/batch
  - POST /v2/recalculate/ship/{shipId}
  
  The parameter became optional-with-no-value instead of defaulting to 1, so
  leaving it out keeps whatever each flow did before: a port still runs on a
  single job, while a ship batch is still distributed by revents based on the
  amount of resolved ships. That avoids turning off the automatic distribution
  of large batches. Validation of the 1..25 bounds is shared by all three.
  
  Note that a single-ship recalculation always replays on one job: revents
  groups interests per ship and never uses more jobs than there are ships.
  The parameter is accepted there for consistency, and documented as such.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `7ed2b5ab` **Claude** (2026-09-09): Merge remote-tracking branch 'origin/develop' into claude/parallel-jobs-config-delay-hvvlty
- `5f981992` **Claude** (2026-09-09): Merge develop and drop the stale note about opting in to distribution
  develop turned on the interest distribution for port recalculations, so
  requesting parallel jobs no longer opts in to anything the port did not
  already do: it only states how many jobs to use instead of letting revents
  derive the amount.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `8c7462c3` **Claude** (2026-09-09): Point at the ais-engine snapshot carrying the parallelJobs setting
  Scenario.Settings.parallelJobs does not exist in 20260819-b1593.1, so this
  branch did not compile. teqplay/ais-engine#1587 published 20260909-SNAPSHOT
  from its branch, which carries it.
  
  Marked temporary on purpose: a dated snapshot is the same coordinate for every
  non-master ais-engine build that day, so this needs to become the released
  version before it merges.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `a1a8730d` **Claude** (2026-09-09): Match the nullable parallelJobs argument with anyOrNull
  With the version bump in place the build got as far as the tests, where 8 of
  them failed on the argument I added: mockito-kotlin's any() does not match
  null, and every existing test calls these conversions without stating an
  amount of parallel jobs. The stubs therefore stopped matching (returning null
  into the service, hence the NPEs) and the verifications reported
  ArgumentsAreDifferent.
  
  Switched that argument to anyOrNull() everywhere, as this file already does
  for other nullable arguments. The three verifications that assert a requested
  amount keep their eq(...).
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `40c9808e` **Claude** (2026-09-09): Grow the develop Mongo volume claim to 500Gi
  The deploy failed because the claim in this chart no longer matches the
  volume that is actually provisioned for the develop environment. Raising the
  requested size realigns them.
  
  Only the develop environment is changed; processing-prod (430Gi) and
  processing-data (400Gi) keep their current sizes.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `5089afe4` **Claude** (2026-09-09): Follow the parallel jobs ceiling of 50
  The validation already reads Scenario.Settings.MAX_PARALLEL_JOBS, so raising
  it in ais-engine is enough for the enforced bound; only the constant that
  names it in the Swagger description had to move to 50, since annotations take
  compile-time constants.
  
  The bounds tests now derive their out-of-range value from that constant
  instead of hardcoding 26, so they follow whichever ais-engine version is
  pinned rather than needing an edit each time the ceiling moves.
  
  Note the enforced bound is whatever the pinned ais-engine carries: the current
  20260909-SNAPSHOT still stops at 25 until a build with 50 is published.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `a38d16fa` **Claude** (2026-09-09): Keep the documented parallel jobs bounds tied to the enforced ones
  The Swagger description names the bounds through local constants, because
  annotations only take compile-time constants, which means the numbers exist
  twice: once here and once in the ais-engine model that actually enforces them.
  
  A test now asserts the two agree, so bumping the ais-engine version can no
  longer leave this endpoint documenting a range it does not have. The constants
  became internal so the test can read them.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01ACbShcRKXRY3NL39zoPfjM
- `f3880239` **Claude** (2026-09-10): Clear the SonarCloud findings on the recalculation service
  Two of these come from this branch, the rest were already in the file -
  SonarCloud reports on the whole changed file, not only the changed lines.
  
  From this branch:
  
  - Adding parallelJobs tipped recalculateByPort/ByShip/ByShips to 8-9
    parameters (kotlin:S107, 7 allowed). Their optional knobs move into a
    RecalculationOptions, passed as a defaulted last parameter, which leaves
    every positional call of the required arguments compiling as it was.
  
  Already in the file:
  
  - mergeWindowsOfShip and deleteOrphanPortVisits both took 8 parameters. The
    four values identifying what a ship's merge is working on - ship, scenario,
    requested port and recalculated window - become a ShipMergeContext, since
    they always travelled together anyway.
  - mergeWindowsOfShip scored 17 cognitive complexity against the 15 allowed.
    Merging one window is now its own function, and the guard on whether an
    orphan sweep applies at all moved into the sweep itself, so the caller no
    longer has to know when one is due.
  - Two "useless null-safe access" reports on reading a recalculation's window.
    Both bounds really are nullable, so the ?. is not redundant; Sonar appears
    to resolve the property named `to` as the infix function. The two places
    that build a TimeWindow out of from/to now share one helper that checks each
    bound on its own, which drops the ?. without dropping a real null guard.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_0151DNvqRuYh8zAvtPvZoib5

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-03)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-03)

### 🟡 Changes recommended

There are small but concrete issues to address (notably a weakened default-path assertion in a unit test) and the PR is explicitly not buildable until the ais-engine version bump is applied.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

Adds an optional `parallelJobs` query parameter to the port recalculation endpoint (`POST /v2/recalculate/port/{unlocode}`) and threads it through to the revents scenario settings so a port recalculation can distribute work across multiple parallel revents jobs (within revents’ allowed bounds).

**Changes:**
- Extend `ProcessingRecalculateV2Controller.recalculatePort` with `parallelJobs` request parameter (Swagger-documented) and pass it into the service layer.
- Validate `parallelJobs` in `ReventsRecalculationService.recalculateByPort` and forward it to scenario creation.
- Set `Scenario.Settings.parallelJobs` in `ReventsConversionService.createScenarioRequestForPort` and add/adjust unit tests for defaulting and validation.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt | Adds `parallelJobs` query param (with Swagger description) and forwards it to the recalculation service. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationService.kt | Adds `parallelJobs` argument, enforces bounds, and passes it into scenario creation. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionService.kt | Extends port scenario request creation to populate `Scenario.Settings.parallelJobs`. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt | Updates stubbing/verification for the new argument and adds tests for invalid values + forwarding. |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionServiceTest.kt | Updates expected settings and adds tests for default and explicit `parallelJobs` propagation. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 5/5 changed files
- **Comments generated:** 2
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/vesselvoyage-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

## Review Comments

### Copilot — 2026-09-03 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsRecalculationServiceTest.kt`

This test no longer asserts what value is passed for the new `parallelJobs` argument in the default-path call; using `any()` means a regression (e.g., passing 0) would still pass. It should verify the default value is forwarded.

### Copilot — 2026-09-03 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/processing/ProcessingRecalculateV2Controller.kt`

The KDoc claims the default is tied to `Scenario.Settings.MIN_PARALLEL_JOBS`, but the actual `@RequestParam` default is hardcoded to "1". If `MIN_PARALLEL_JOBS` ever changes, this comment becomes incorrect/misleading.

## Comments

### TeqJoostD — 2026-09-09

CI is red here and I am deliberately not fixing it on this branch.

**What fails:** `Test & build` / `Kover + Codecov Upload` on `:compileKotlin`:

```
ReventsConversionService.kt:101:47 Unresolved reference: MIN_PARALLEL_JOBS
ReventsConversionService.kt:128:13 Cannot find a parameter with this name: parallelJobs
ReventsRecalculationService.kt:444:47 Unresolved reference: MIN_PARALLEL_JOBS
...
```

**Why:** `Scenario.Settings.parallelJobs` does not exist yet in the pinned `aisengine_version = '20260819-b1593.1'`. It is added by teqplay/ais-engine#1587, which is not merged or released yet. SonarCloud is red for the same reason — it has no successful analysis to report on.

**What unblocks it:** merge teqplay/ais-engine#1587, release ais-engine, then bump `aisengine_version` in `build.gradle` here. I have left the version alone rather than guessing at an unreleased one. Happy to push the bump the moment there is a version to point at.

Nothing else on this branch is failing: develop is merged in and the existing recalculation tests were updated for the added argument.

---
_Generated by [Claude Code](https://claude.ai/code)_
