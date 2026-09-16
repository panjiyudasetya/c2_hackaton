---
id: github:teqplay/vesselvoyage-backend:pr:717
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 717
title: 'Release PR: docker build fix + bunker encounters'
author: michel-teqplay
state: closed
date: '2026-02-18'
merged_at: null
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/717
labels: []
linked_issues: []
explicit_links: []
---
# PR #717: Release PR: docker build fix + bunker encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/717  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-02-18  

## Description

_No description._

## Commits

- `69919f31` **Jamie de Leest** (2026-02-13): chore: update Spring Boot version to 3.4.12 and add Docker builder configuration
- `8e2a2378` **Darius Wattimena** (2026-02-16): Remove unneeded builder
- `85df82b2` **Darius Wattimena** (2026-02-17): fix: prevent inverted stops when event time is before ongoing stop start
  Agent-Id: agent-b7c0ab31-3977-4209-aeb7-fa0b979952ef
  Linked-Note-Id: 36d157bb-bc43-47ef-be5c-a78c6a5a28ef
- `b50dcdd1` **Darius Wattimena** (2026-02-17): Add inverted stop validation to StopStartProcessor.getUpdatedStops()
  Agent-Id: agent-b7c0ab31-3977-4209-aeb7-fa0b979952ef
- `59f680d1` **Darius Wattimena** (2026-02-17): Merge pull request #712 from teqplay/fix-deployment
  Fix deployment
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
- `edc762ac` **Darius Wattimena** (2026-02-17): Fix negative PTO SOF terminal times by preventing inverted stops (#714)
  Fix negative PTO SOF terminal times by preventing inverted stops

## Reviews

### github-actions[bot] — COMMENTED (2026-02-18)

Review completed. No suggestions at this time.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-18)

## Pull request overview

This PR hardens stop processing against “inverted” stop durations caused by out-of-order timestamps (seen in CSV imports), and aligns Spring Boot patch versions across modules (likely related to release/docker build stability).

**Changes:**
- Prevent inverted stop durations by clamping fallback/split end times so they never precede the stop start time.
- Add regression tests covering multiple real-world inversion patterns (small/large time offsets, voyage + previous-entry split).
- Bump `spring_boot_version` from `3.4.4` to `3.4.12` in root/api/client Gradle builds.

### Reviewed changes

Copilot reviewed 5 out of 6 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt` | Clamp fallback end time when a stop-start event’s `actualTime` predates the ongoing stop start (prevents inverted stop). |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopEndProcessor.kt` | Clamp previous-entry stop end to its own start when `currentEntry.start` predates the stop start (prevents inverted stop during split). |
| `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt` | Adds regression tests for inverted-stop prevention across several timestamp-offset scenarios. |
| `build.gradle` | Updates Spring Boot patch version to `3.4.12`. |
| `api/build.gradle` | Updates Spring Boot patch version to `3.4.12`. |
| `client/build.gradle` | Updates Spring Boot patch version to `3.4.12`. |
</details>

## Review Comments

### Copilot — 2026-02-18 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopEndProcessor.kt`

The new warn log for inverted previous-entry stop splitting doesn’t include the stop end event id (or related start event id / entry ids), which makes it hard to trace back to the source data when this triggers in production. Consider including `event._id` (and ideally the related start event id and current/previous entry ids) in the log message so it’s actionable.

### Copilot — 2026-02-18 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/processing/EventProcessingServiceTest.kt`

These inverted-stop scenarios are covered with several near-identical tests that differ only in the time offsets (e.g., 28 hours vs 10 minutes). To reduce duplication (and make it easier to add more cases), consider converting these to a single `@ParameterizedTest` (or a small helper that runs a table of offsets + expected assertions).
