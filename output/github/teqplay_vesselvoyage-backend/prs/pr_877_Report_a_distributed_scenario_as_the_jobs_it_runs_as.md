---
id: github:teqplay/vesselvoyage-backend:pr:877
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 877
title: Report a distributed scenario as the jobs it runs as
author: TeqJoostD
state: open
date: '2026-09-09'
merged_at: null
base_branch: develop
head_branch: claude/nice-cannon-bt7pfm
url: https://github.com/teqplay/vesselvoyage-backend/pull/877
labels: []
linked_issues: []
explicit_links: []
---
# PR #877: Report a distributed scenario as the jobs it runs as

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/877  
**State:** open | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `claude/nice-cannon-bt7pfm`  
**Created:** 2026-09-09  

## Description

Progress stopped working for port recalculations once `useInterestDistribution` was turned on for them. This fixes that, and exposes the jobs themselves so the front-end can list them.

## Problem

A port recalculation distributes its interests over multiple revents jobs, which forks the scenario into child scenarios. In `ais-engine`, a forked parent explicitly reports no cursor of its own:

```kotlin
// can't have a progressing cursor on the parent, since it's forked, but can have child statuses
progressingCursor = null,
```

`ReventsConversionService` read `response.status?.progressingCursor` straight off the parent, so `cursor` came back null and `reventsProgress()` fell back to `cursor ?: windowStart` — **0% for the whole `RUNNING_REVENTS` phase**.

## Change

Two commits.

**1. Follow the slowest job for the progress of a forked scenario.** Take the cursor of the job lagging behind the most instead of the parent's, so the bar never claims more progress than the slowest job actually made.

**2. Report a distributed scenario as the jobs it runs as.** `ReventsRecalculationStatus.jobs: List<JobProgress>` — every job reported on its own with its `name`, `progress`, `jobId`, `cursor`, `monitors` and `aisReplay`, so the front-end can list them and open one. Empty for a scenario that runs as a single job, which keeps reporting its replay data on `monitors`/`aisReplay` directly and is unaffected by all of this.

Details worth flagging in review:

- **Ordering and naming.** Revents names a child `<parent id>.<index>`; that suffix is the only thing that ties a job to the same position on every poll, since the order the children come back in is not guaranteed. Jobs are sorted and numbered by it, falling back to wire order for an id that does not follow the shape.
- **Job progress comes from revents' own `percentage`,** not from recomputing the cursor: a job that finished reports 100% even though its cursor stopped short of the end of the window.
- **The scenario's `progress` is `jobs.minOf { progress }`** when there are jobs, and its `cursor` is that same job's cursor — one job is "the lagging one" and both numbers come from it. A single-job scenario keeps the old cursor-versus-window path exactly.
- The window-to-cursor maths moved to a private top-level `windowProgress`, so there is one implementation of it.

## Depends on

**This does not compile against the currently pinned `aisengine_version = '20260819-b1593.1'`.** It reads `ScenarioResponse.Status.scenarioId`, which teqplay/ais-engine#1589 adds. That PR needs to be merged and published, and `aisengine_version` in `build.gradle` bumped to that build, before this one is green. I left the version untouched rather than guessing a build number.

That PR also makes a forked scenario report the children that have not started yet, which matters here: without it a job still waiting for capacity is absent from `children`, and the lagging job would be picked from the started ones only — reporting more progress than the scenario has really made.

## Related

The front-end side is teqplay/vesselvoyage#171. It tolerates a backend without `jobs`, so it is independent of the merge order.

## Testing

- `ReventsConversionServiceTest` — jobs are listed, ordered and numbered by their id suffix; the scenario follows the lagging job for both progress and cursor; a job that has not started stays in the list and holds the scenario at 0%; replay data is reported per job; a single-job scenario reports no jobs.
- `ReventsRecalculationStatusProgressTest` — progress follows the lowest job, a job at 0% holds the scenario there, and a scenario with jobs no longer needs a parent window.

I could not run the build in this environment — `s3://repo.teqplay.nl` uses `AwsImAuthentication` and no AWS credentials are available here (`InvalidAccessKeyId`, 403), so `./gradlew test ktlintCheck` still needs a real run on CI, after the version bump above.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_0151DNvqRuYh8zAvtPvZoib5

## Commits

- `ad3e51a9` **Claude** (2026-09-09): Follow the slowest job for the progress of a forked scenario
  A port recalculation now distributes its interests over multiple (r)events
  jobs, which forks the scenario into child scenarios. A forked parent reports
  no progressing cursor of its own - only its children do, each walking the
  same window at its own pace - so reading the cursor straight off the parent
  yielded null and left the RUNNING_REVENTS progress stuck at 0%.
  
  Take the cursor of the job lagging behind the most instead: the scenario as a
  whole is only as far as its slowest job, so the bar never claims more progress
  than that job actually made. A job that started but has yet to report a cursor
  has not walked its window at all and holds the scenario at the start.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_0151DNvqRuYh8zAvtPvZoib5
- `ca7720d7` **Claude** (2026-09-09): Report a distributed scenario as the jobs it runs as
  Building on the previous commit, which only recovered a single cursor for a
  forked scenario: expose the jobs themselves, so the front-end can list them
  and open one.
  
  Every job of a scenario whose interests are distributed is reported on its own
  - named after the position it was forked off in, with its own progress, cursor,
  monitor timings and replay throughput. The scenario's own progress follows the
  job lagging behind the most, so the bar never claims more than the slowest job
  actually made, and the scenario cursor is that same job's cursor.
  
  Job progress comes from (r)events' own percentage rather than being recomputed
  from the cursor: a job that finished reports 100% even though its cursor
  stopped short of the end of the window.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_0151DNvqRuYh8zAvtPvZoib5

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-09)

### 🟡 Changes recommended

It depends on an AIS Engine client model change (`ScenarioResponse.Status.scenarioId`) and needs the pinned `aisengine_version` bumped to a published build that includes it to compile and pass CI.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

Fixes stalled progress reporting for distributed (forked) (r)events scenarios by deriving overall progress/cursor from the slowest-running child job, and exposes per-job progress details so the front-end can list and link to individual jobs.

**Changes:**
- Convert forked scenarios into `ReventsRecalculationStatus.jobs` entries (stable ordering by child id suffix), each with its own progress/cursor/monitoring/replay data.
- Compute scenario-level `progress`/`cursor` from the lagging job when jobs are present; otherwise keep the existing single-job window/cursor logic.
- Add unit tests covering job listing/ordering, lagging-job selection, and progress behavior with not-yet-started jobs.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionService.kt` | Builds per-job status from forked children and uses the slowest job for scenario-level cursor/progress inputs. |
| `api/src/main/kotlin/nl/teqplay/vesselvoyage/model/ReventsRecalculationStatus.kt` | Adds `jobs` to the API model and updates progress calculation to follow the slowest job when present. |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionServiceTest.kt` | Adds coverage for job listing/ordering, lagging-job selection, and per-job replay/monitor reporting. |
| `src/test/kotlin/nl/teqplay/vesselvoyage/model/ReventsRecalculationStatusProgressTest.kt` | Adds progress-calculation tests for multi-job scenarios (min progress) and window-less job-reported scenarios. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 4/4 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/vesselvoyage-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F877%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

### Copilot — 2026-09-09 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/recalculation/ReventsConversionService.kt`

This code now relies on `ScenarioResponse.Status.scenarioId`, but the repo is pinned to `aisengine_version = 20260819-b1593.1` (build.gradle:14), which (per PR description) doesn’t include that property yet. To keep this PR compiling and CI-green, bump the AIS Engine dependency to a published build that contains `scenarioId` (and the child-reporting behavior this logic depends on) before merging.

## Comments
