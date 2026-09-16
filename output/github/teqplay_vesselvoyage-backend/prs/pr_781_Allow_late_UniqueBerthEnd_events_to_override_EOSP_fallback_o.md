---
id: github:teqplay/vesselvoyage-backend:pr:781
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 781
title: Allow late UniqueBerthEnd events to override EOSP fallback on previous visit
author: TeqJoostD
state: closed
date: '2026-06-02'
merged_at: null
base_branch: develop
head_branch: TeqJoostD/berth-end-override-previous-visit-fallback
url: https://github.com/teqplay/vesselvoyage-backend/pull/781
labels: []
linked_issues: []
explicit_links: []
---
# PR #781: Allow late UniqueBerthEnd events to override EOSP fallback on previous visit

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/781  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `develop` ← `TeqJoostD/berth-end-override-previous-visit-fallback`  
**Created:** 2026-06-02  

## Description

## Problem

When revents recalculation produces a `UniqueBerthEndEvent` after the visit has already been closed, multiple checks in the V2 processing pipeline blocked it from updating the original visit:

1. `EventProcessor.isValidEventTime` rejected any event older than the latest event on the current entry.
2. When the ship had already moved on to a new visit, `ActivityEventProcessor.getResultOnVisitAtEndEvent` could only match activities on the *current* visit and silently dropped events that targeted a closed visit.

The net result: an `ACTIVITY_END_BY_EOSP` fallback set on a closed visit's berth activity could never be overridden by the actual berth end event, even when revents made it available.

## Changes

- Drop `isValidEventTime` from the V2 validation pipeline (`EventProcessor.isValid`). Late events from revents are now allowed through; the V1 check stays intact for the deprecated path.
- Extract the previous-visit fallback application into a shared private helper on `ActivityEventProcessor` and expose a sibling `getResultForPreviousVisitOnVisit` alongside the existing `getResultForPreviousVisitOnVoyage` so it can be called from a `NewVisitShipStatus`.
- Override `getResultOnVisitAtEndEvent` in `UniqueBerthEndProcessor` so when an end event doesn't match any ongoing activity on the current visit but there is a previous visit, it falls through and tries to override an EOSP fallback on that previous visit. Scope is intentionally limited to berth-end events as agreed.

`NewInitialShipStatus` is unaffected — there is no previous visit to fall back to. The ship-ID validation is preserved.

## Tests

Added `should process late berth end event by overriding EOSP fallback on previous visit when ship is at new visit` to `EventProcessingServiceTest`. Existing tests for the visit-only and voyage-only paths continue to assert the same behavior.

I could not run the test suite locally (no JDK in the sandbox); please rely on CI.

---
Pull Request opened by [Augment Code](https://www.augmentcode.com/) | [View session](https://cosmos.augmentcode.com/session?agentId=01KT3J3B6ABG8VC19MZAFP2CN5&panel=chat)

## Commits

- `d1784a3a` **TeqJoostD** (2026-06-02): Allow late UniqueBerthEnd events to override EOSP fallback on previous visit
  When revents recalculation produces a UniqueBerthEndEvent after the visit
  has already been closed, the event was previously blocked by the V2
  isValidEventTime check, or silently ignored when the ship had already
  moved to a new visit. This made it impossible to override an EOSP
  fallback that was set as the activity end time on the closed visit.
  
  - Drop isValidEventTime from the V2 validation pipeline so late events
    are no longer rejected for being older than the latest known event.
  - Extract the previous-visit fallback application into a shared helper
    on ActivityEventProcessor and add getResultForPreviousVisitOnVisit
    for use from a NewVisitShipStatus.
  - Override getResultOnVisitAtEndEvent in UniqueBerthEndProcessor so
    end events that don't match any ongoing activity on the current visit
    fall through to the previous visit's EOSP-fallback activity.

## Comments

### TeqJoostD — 2026-06-02

<sup>[**PR Author Agent**](https://cosmos.augmentcode.com/session?agentId=01KT3J3B6ABG8VC19MZAFP2CN5)⚡</sup>

👋 I've got this PR — here's what I'll handle for you:

- **Review feedback** — implement suggestions, answer questions, fix what comes up
- **CI failures** — I get pinged when checks fail and try to fix them
- **Merge conflicts** — bring the PR back up to date when it falls behind
- **Merge gates** — watch CI, reviews, and verification
- **Ping you the moment it's ready to merge**

Marking it ready and picking reviewers are your call — I'll leave both alone.

Drop a comment anytime!

### TeqJoostD — 2026-06-08

<sup>[**PR Author Agent**](https://cosmos.augmentcode.com/session?agentId=01KT3J3B6ABG8VC19MZAFP2CN5)⚡</sup>

This PR appears to be inactive. The agent will stop monitoring until a new comment is posted.
