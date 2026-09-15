---
id: github:teqplay/vesselvoyage-backend:pr:856
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 856
title: Split revents recalculation phases and add merge and post-processing progress
author: TeqJoostD
state: closed
date: '2026-08-18'
merged_at: '2026-08-25'
base_branch: develop
head_branch: revents-phase-progress
url: https://github.com/teqplay/vesselvoyage-backend/pull/856
labels: []
linked_issues: []
explicit_links: []
---
# PR #856: Split revents recalculation phases and add merge and post-processing progress

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/856  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `revents-phase-progress`  
**Created:** 2026-08-18  
**Merged:** 2026-08-25  

## Description

## Why

A revents recalculation used to jump from `PROGRESSING` straight to its final phase. Everything after the revents run itself — merging the generated events back, and post-processing the merged entries — was invisible, and the scenario was already reported as `FINISHED` while its entries were still being post-processed.

## The phases

```
QUEUED → RUNNING_REVENTS → MERGING → POST_PROCESSING → { FINISHED | PARTIALLY_FAILED | STOPPED }
```

The three phases a scenario can end in carry `final = true` on the enum, which now drives `findAllRunning()` and `finishedRecalculationStatus` instead of hand-maintained sets. `QUEUED` already existed. `PROGRESSING` was renamed to `RUNNING_REVENTS`, because "progressing" no longer says which part is meant.

Note the two `POST_PROCESSING`s are different things and are deliberately not mapped onto each other: ais-engine's is the in-run `VESSEL_VOYAGE_V2` step and still collapses into `RUNNING_REVENTS`; ours is the later phase where the merged Visit/Voyage entries go through `PostProcessingService`.

## One progress bar, never two

Merging counts ships, post-processing counts entries, and both are persisted while they run:

| phase | `merge` | `postProcessing` | `progress` |
|:--|:--|:--|:--|
| `QUEUED` | – | – | `0` |
| `RUNNING_REVENTS` | – | – | cursor vs window (unchanged) |
| `MERGING` | ships | – | `merge.percentage` |
| `POST_PROCESSING` | – | entries | `postProcessing.percentage` |
| final | – | entries | `100` |

The phases run one after the other, so only the counters of the current phase are kept — **at most one of `merge` / `postProcessing` is ever set**. The front-end keeps rendering a single bar bound to `progress` and takes its caption ("132 / 480 ships") from whichever counter object is present. Post-processing counters are only written once merging is done, so that bar can't jump backwards while entries are still being scheduled per merged ship.

Post-processing progress comes from `ScenarioMeasurement` (`measures`), which gained `totalPostProcessingTasks`, a derived `completedPostProcessingTasks` and `lastPostProcessedTime`. Merge progress is written per ship from inside both merge loops.

## Behaviour changes worth reviewing

- A scenario **stays tracked** after merging and gets its final phase from the existing one-minute tick once its entries are post-processed. The outcome is re-derived from the persisted errors and merge-failure summary, so no pending-outcome state is stored.
- `finishAutomaticRecalculation` **moved** to that terminal transition. Left at merge-end it would silently no-op on `POST_PROCESSING` and automatic-recalculation ships would never leave `RUNNING`.
- Entries that keep failing to post-process would otherwise park a scenario outside a final phase forever, so after `recalculation.post-processing-stall-timeout` (default `PT30M`) without a single entry finishing, the scenario finishes anyway and logs + Slacks it. Deliberately **no** error is recorded for this, so a clean merge still ends `FINISHED` instead of being demoted to `PARTIALLY_FAILED`.
- `persistMergeResultV2` only announces post-processing when `postProcessingService` is actually wired. Without that guard a deployment with `post-processing.enabled=false` would wait out the full stall timeout on every scenario.
- Merge-only scenarios (`.MERGE`) get no post-processing phase: their entries are scheduled under the *source* scenario's id, so they finish right after merging exactly as they do today. Aggregating the source measurements would read as already-drained from that source's earlier merge and finish early, which is worse than the gap.

## Migration and compatibility

- `Migration20260817` (Mongock) rewrites stored `revents.phase: "PROGRESSING"` to `"RUNNING_REVENTS"`; a `@JsonAlias` on the enum constant covers anything read before or outside it.
- **Breaking for the front-end**: `PROGRESSING` disappears from the API and `MERGING` / `POST_PROCESSING` appear. Needs a coordinated release. `progress` keeps its meaning as "percentage of the current phase", so the existing bar keeps working through all phases untouched.

## Testing

`./gradlew ktlintCheck test` green. New coverage for per-phase `progress` and `PhaseProgress` bounds, the phase enum (alias, finality, order), the post-processing counters in `MeasuringService`, and the phase lifecycle in `ReventsRecalculationService`: per-ship merge counters, waiting for post-processing, finishing right away when there is nothing to post-process, refreshing progress without re-merging, finishing on drain, keeping a `PARTIALLY_FAILED` outcome across post-processing, and the stall guard.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `0c3b2cdb` **TeqJoostD** (2026-08-18): Split revents recalculation phases and add merge and post-processing progress
  A recalculation used to jump from PROGRESSING straight to its final phase, so
  everything after the revents run itself — merging the generated events back and
  post-processing the merged entries — was invisible, and the scenario was already
  reported as FINISHED while its entries were still being post-processed.
  
  The phases are now QUEUED, RUNNING_REVENTS (was PROGRESSING), MERGING,
  POST_PROCESSING and the three phases a scenario can end in: FINISHED,
  PARTIALLY_FAILED and STOPPED, which are marked as final on the enum itself.
  
  Merging counts the ships it merged, post-processing counts the entries it
  post-processed, and both are persisted while they run. The phases follow each
  other, so only the counters of the current phase are kept and `progress` reports
  that single phase: the front-end renders one progress bar that follows the
  scenario, never a merge and a post-processing bar at the same time.
  
  A scenario stays tracked until its merged entries are post-processed, and gets
  its final phase from what the merge ran into. Entries that keep failing to
  post-process no longer keep it out of a final phase forever: after
  `recalculation.post-processing-stall-timeout` it finishes anyway and reports it.
  
  Recalculations stored with the old PROGRESSING phase are migrated, and the phase
  also reads back through a Jackson alias.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `32100195` **Joost Dambrink** (2026-08-19): Merge branch 'develop' into revents-phase-progress
- `bc1bde9f` **TeqJoostD** (2026-08-21): Drop the phase-rename migration, the Jackson alias already covers it
  The recalculations are read through mongojack's JacksonCodecRegistry, so the
  @JsonAlias on RUNNING_REVENTS is enough to keep documents stored as PROGRESSING
  readable - rewriting the stored value bought nothing. Same approach as the
  pendingDrifting alias on ShipChangeStatistics.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
- `64660c65` **Joost Dambrink** (2026-08-21): Merge branch 'claude/port-recalc-polygon-size-v6ceyb' into revents-phase-progress
  Combines the split recalculation phases with the port-visit deletion and
  follow-up recalculation work.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01S7ZWS51673Y7UuDiB5HAyj
- `79d1f5b4` **Joost Dambrink** (2026-08-21): Fix test compilation after merging the port-recalc branch
  The merged branches crossed two renames: the recalculation phase PROGRESSING
  became RUNNING_REVENTS, and buildMergeEntries now returns ShipMergeData
  instead of a plain list of merge entries.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01S7ZWS51673Y7UuDiB5HAyj
- `df89bdda` **Joost Dambrink** (2026-08-25): Merge branch 'develop' into revents-phase-progress
- `2e54619f` **Claude** (2026-08-25): Merge remote-tracking branch 'origin/develop' into revents-phase-progress
- `37906d3d` **TeqJoostD** (2026-08-25): Drop the post-processing stall timeout
  Waiting for post-processing no longer gives up after a while: the timeout, its
  property and the lastPostProcessedTime it needed are gone. A scenario now stays
  in POST_PROCESSING until every merged entry is post-processed.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-18)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F856%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### Darius-Wattimena — APPROVED (2026-08-25)

_No comment._

## Review Comments

## Comments
