---
id: github:teqplay/vesselvoyage-backend:pr:714
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 714
title: Fix negative PTO SOF terminal times by preventing inverted stops
author: Darius-Wattimena
state: closed
date: '2026-02-17'
merged_at: '2026-02-17'
base_branch: develop
head_branch: fix-negative-pto-sof-times
url: https://github.com/teqplay/vesselvoyage-backend/pull/714
labels: []
linked_issues:
- github:teqplay/vesselvoyage-backend:issue:713
explicit_links:
- github:teqplay/vesselvoyage-backend:issue:713
---
# PR #714: Fix negative PTO SOF terminal times by preventing inverted stops

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/714  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-negative-pto-sof-times`  
**Created:** 2026-02-17  
**Merged:** 2026-02-17  

## Description

## Summary

Fixes #713 — VesselVoyage PTO SOF terminal times can be negative.

Adds validation in `StopStartProcessor` and `StopEndProcessor` to prevent creating stops with inverted times (`end < start`), which caused negative terminal and berth visit durations in the PTO Statement of Facts API.

## Changes

### `StopStartProcessor.kt`
- Added validation in `getUpdatedStops()`: when creating a fallback-ended stop, if `event.actualTime < currentlyOngoingStop.start.time`, clamps the end time to the stop's start time (zero-duration) instead of creating an inverted stop
- Logs a warning when this occurs

### `StopEndProcessor.kt`
- Added validation in `getResultOnVisitOrVoyage()`: when finishing a previous-entry stop with `end = currentEntry.start`, if `currentEntry.start.time < matchingPreviousEntryStop.start.time`, clamps the end to the stop's own start time (zero-duration)
- Logs a warning when this occurs

### `EventProcessingServiceTest.kt`
- Added test: stop start event with time before ongoing stop's start does not create an inverted stop
- Added test: stop end with entry start before the stop's start does not create an inverted stop

## Testing

- All existing `EventProcessingServiceTest` tests pass (no regressions)
- 2 new tests cover both inverted-stop edge cases

## Notes

This prevents **future** inverted stops from being created. Existing corrupt data in the database (as reported in the CSV attached to the issue) will need a separate data fix or reprocessing.

---
Pull Request opened by [Augment Code](https://www.augmentcode.com/) with guidance from the PR author

## Commits

- `85df82b2` **Darius Wattimena** (2026-02-17): fix: prevent inverted stops when event time is before ongoing stop start
  Agent-Id: agent-b7c0ab31-3977-4209-aeb7-fa0b979952ef
  Linked-Note-Id: 36d157bb-bc43-47ef-be5c-a78c6a5a28ef
- `b50dcdd1` **Darius Wattimena** (2026-02-17): Add inverted stop validation to StopStartProcessor.getUpdatedStops()
  Agent-Id: agent-b7c0ab31-3977-4209-aeb7-fa0b979952ef
- `037d444b` **Darius Wattimena** (2026-02-17): Merge remote-tracking branch 'origin/develop' into fix-negative-pto-sof-times
- `a5008fb2` **Darius Wattimena** (2026-02-17): Add CSV-based inverted stop test cases from real production data
  Added 4 new test cases to EventProcessingServiceTest based on the actual
  negative terminal stay data from the CSV attached to issue #713:
  
  - StopStartProcessor: large inversion (~28 hours, matching NLRTM visit)
  - StopStartProcessor: small inversion (~10 minutes, matching USHOU visit)
  - StopEndProcessor: large inversion (~17 hours, matching BEANR visit)
  - StopEndProcessor: small inversion (~10 minutes)
  
  All tests verify that inverted stops are clamped to zero-duration.
  
  Agent-Id: agent-240ff93b-4126-401f-a92a-225499b53395

## Reviews

### github-actions[bot] — COMMENTED (2026-02-17)

Review completed. I found one potential logic issue in the StopEndProcessor that should be addressed.

### github-actions[bot] — COMMENTED (2026-02-17)

Review completed. The validation logic successfully prevents inverted stops in the previous entry, and the tests confirm the expected behavior.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-17)

## Pull request overview

Fixes negative PTO SOF terminal times by preventing creation of inverted stops (`end < start`) during stop start/end event processing in the VesselVoyage processing pipeline.

**Changes:**
- Clamp fallback stop end times to the stop’s start time when an event timestamp would otherwise invert the stop (StopStartProcessor, StopEndProcessor).
- Add regression tests covering both inverted-stop edge cases (EventProcessingServiceTest).
- Bump Spring Boot version from `3.4.4` to `3.4.12` across modules.

### Reviewed changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 1 comment.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt` | Adds validation + warning log to prevent inverted fallback-ended stops on stop start events. |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopEndProcessor.kt` | Adds validation + warning log to prevent inverted previous-entry stop end when splitting across entries. |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt` | Adds 2 tests verifying inverted stops are not created in both scenarios. |
| `build.gradle` | Updates `spring_boot_version` to `3.4.12`. |
| `api/build.gradle` | Updates `spring_boot_version` to `3.4.12`. |
| `client/build.gradle` | Updates `spring_boot_version` to `3.4.12`. |
</details>

### TeqJoostD — CHANGES_REQUESTED (2026-02-17)

Can you add test cases for the cases where it acutally went wrong which are defined in the csv in the github issue.

### michel-teqplay — DISMISSED (2026-02-17)

_No comment._

### github-actions[bot] — COMMENTED (2026-02-17)

Review completed. No suggestions at this time.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### TeqJoostD — APPROVED (2026-02-17)

LGTM! Could you please tell Darius that im very proud of him!

## Review Comments

### Copilot — 2026-02-17 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt`

The KDoc for `getUpdatedStops()` states the ongoing stop is ended with a fallback time matching the new stop’s start time, but this new clamping logic can set the fallback end to the ongoing stop’s own start time instead. Please update the documentation/comment so it reflects the new behavior (end time is clamped to be >= ongoing stop start).

## Comments

### Darius-Wattimena — 2026-02-17

Added 4 new test cases based on the real failure data from the CSV attached to #713:

- **StopStartProcessor — large inversion (~28 hours):** Reproduces the NLRTM visit (`397b0b2f`) where terminal stay was -28.02h
- **StopStartProcessor — small inversion (~10 minutes):** Reproduces the USHOU visit (`fd7145fe`) where terminal stay was -0.17h
- **StopEndProcessor — large inversion (~17 hours):** Reproduces the BEANR visit (`99b5d643`) where terminal stay was -17.67h
- **StopEndProcessor — small inversion (~10 minutes):** Covers small inversion edge case

All 6 tests pass (2 original + 4 new CSV-based). Ready for re-review. @TeqJoostD
