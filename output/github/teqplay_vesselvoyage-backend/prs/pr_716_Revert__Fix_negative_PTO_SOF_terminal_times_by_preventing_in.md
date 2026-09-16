---
id: github:teqplay/vesselvoyage-backend:pr:716
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 716
title: Revert "Fix negative PTO SOF terminal times by preventing inverted stops"
author: Darius-Wattimena
state: closed
date: '2026-02-18'
merged_at: '2026-02-18'
base_branch: develop
head_branch: revert-714-fix-negative-pto-sof-times
url: https://github.com/teqplay/vesselvoyage-backend/pull/716
labels: []
linked_issues: []
explicit_links: []
---
# PR #716: Revert "Fix negative PTO SOF terminal times by preventing inverted stops"

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/716  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `revert-714-fix-negative-pto-sof-times`  
**Created:** 2026-02-18  
**Merged:** 2026-02-18  

## Description

Reverts teqplay/vesselvoyage-backend#714

## Commits

- `6fe2b18a` **Darius Wattimena** (2026-02-18): Revert "Fix negative PTO SOF terminal times by preventing inverted stops"

## Reviews

### michel-teqplay — APPROVED (2026-02-18)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-18)

This revert removes important data integrity protections that prevent inverted stops (end time before start time). Reverting without an alternative fix will re-introduce negative terminal times in the PTO Statement of Facts API. Consider whether the original fix had unintended side effects that necessitate this revert, and if so, plan for an alternative solution to maintain data integrity.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-18)

## Pull request overview

This PR reverts the changes from teqplay/vesselvoyage-backend#714, restoring the previous stop start/end processing behavior (including removing the inverted-stop prevention logic) and removing the corresponding regression tests.

**Changes:**
- Removed inverted-stop prevention/clamping logic from `StopStartProcessor` and `StopEndProcessor`.
- Removed KotlinLogging usage that was introduced to warn when inverted-stop situations occur.
- Removed regression tests that asserted stop end times are never before stop start times for out-of-order timestamps.

### Reviewed changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 3 comments.

| File | Description |
| ---- | ----------- |
| src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt | Removes inverted-stop regression tests that were added with the reverted behavior. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt | Reverts fallback stop-end timestamp clamping; now always uses `event.actualTime`. |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopEndProcessor.kt | Reverts clamping when splitting stops across entries; now always uses `currentEntry.start` as the previous stop’s end. |

## Review Comments

### Copilot — 2026-02-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt`

`fallbackEndedCurrentlyOngoingStop.end.time` is set to `event.actualTime` even if that timestamp is before `currentlyOngoingStop.start.time`, which can produce an inverted stop (negative duration). Consider clamping the fallback end time to `max(event.actualTime, currentlyOngoingStop.start.time)` (or using the stop start time when the event is earlier) so `end >= start` is always guaranteed.

### Copilot — 2026-02-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopEndProcessor.kt`

When splitting a stop that started in the previous entry, `finishedPreviousEntryStop.end` is always set to `currentEntry.start`. If `currentEntry.start.time` is earlier than `matchingPreviousEntryStop.start.time`, this creates an inverted stop (negative duration). Please guard against this by ensuring the end is not before the stop start (e.g., clamp to the stop start time in that case).

### Copilot — 2026-02-18 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt`

This change removes the only tests covering the inverted-stop edge cases (stop end/start timestamps arriving out-of-order), so regressions like negative terminal/anchorage durations won’t be caught by CI anymore. Consider keeping/rewriting a minimal regression test that asserts `stop.end.time >= stop.start.time` for these scenarios, even if the implementation is being changed/reverted.
