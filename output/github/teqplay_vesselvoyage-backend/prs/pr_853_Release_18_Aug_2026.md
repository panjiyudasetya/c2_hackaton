---
id: github:teqplay/vesselvoyage-backend:pr:853
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 853
title: Release 18 Aug 2026
author: Darius-Wattimena
state: closed
date: '2026-08-18'
merged_at: '2026-08-18'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/853
labels: []
linked_issues: []
explicit_links:
- jira:TCC-1149
---
# PR #853: Release 18 Aug 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/853  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-08-18  
**Merged:** 2026-08-18  

## Description

_No description._

## Commits

- `5113c8b7` **Darius Wattimena** (2026-08-07): TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0-SNAPSHOT
  - Spring Boot 3.4.12 -> 3.5.16 (root, api, client), spring-cloud-kubernetes 3.2.1 -> 3.3.3
  - skeleton 2.12.2-b220.1 -> 2.14.0-SNAPSHOT (Boot 3.5 based)
  - springdoc 2.8.6 -> 2.8.17
  - MongoDB driver 4.11.0 -> 5.5.2 (Boot 3.5 imports mongodb-driver-bom, no 4.x line)
  - Adapt test mock to driver 5.x ListCollectionNamesIterable
  - Add junit-platform-launcher to test runtime (required by JUnit platform 1.12)
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `8e3f1bef` **Darius Wattimena** (2026-08-10): TCC-1149 Pin skeleton release 2.14.0-b237.1
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `3d0cb551` **Darius Wattimena** (2026-08-10): TCC-1149 Bump poma api to 20260810-b287.1 (Boot 3.5 based)
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `0a46151a` **Claude** (2026-08-11): Split berth stops at the berths they moved to in post-processing
  A stop's berth is decided once, from its start location, and never
  revisited. A ship that shifts along the quay without producing a stop end
  event keeps one stop carrying the first berth for the whole stay, while
  the visit's berth activities correctly record both calls.
  
  The second berth call is then lost entirely rather than just mislabelled:
  the SoF generators only keep berth activities matching the stop's own
  berth, so it never becomes a berth visit, terminal visit, or ATB/ATD.
  
  Add BerthStopSplitter, run as a post-processing step: if another berth
  happens during a berth-classified stop, split the stop there, unless that
  berth already has a stop of its own. Two properties it holds on to:
  
  - The stop's own start and end never move. A split only adds boundaries
    inside them, so the original span stays partitioned exactly, with no
    gaps and no overlaps.
  - "Already has a stop" is matched per berth call, not per berth, so a ship
    returning to a berth later in the visit still gets a second stop for
    that second call.
  
  Segments carry derived start event ids because a stop's document id is
  built from its start event id with no uniqueness guard, and derived
  boundaries are marked with a new STOP_SPLIT_BY_BERTH fallback type so
  consumers can tell them from real stop events.
  
  This is the first post-processing step that rewrites the entry itself
  rather than only the ESoF, so PostProcessingService now emits a
  VisitChange and refreshes the entry cached on the ship status - without
  that, resuming the visit would restore the pre-split stops. Guarded by
  post-processing.split-berth-stops as a kill switch.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01TLDWmWxCC92V5sQDdf7AFw
- `08a31f05` **Claude** (2026-08-11): Drop the berth stop split feature flag
  The flag was not asked for and the splitter needs no configuration: it
  either finds an unaccounted berth call inside a stop or leaves the stop
  alone.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01TLDWmWxCC92V5sQDdf7AFw
- `9aa25ffd` **Darius Wattimena** (2026-08-11): TCC-1149 Bump csi to 20260811-b242.1 (Boot 3.5 based)
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `789eac3d` **Claude** (2026-08-14): Reconsider new segments so a return to the stop's own berth is split
  Splitting advanced the index past every segment it had just created, so a
  new segment was never itself considered for further cuts. Combined with
  the first pass only looking at berth calls foreign to the stop's own
  berth, a stop covering A -> B -> A lost the return to berth A: the cut at
  B was made, but the berth B segment that would expose the return to A was
  skipped.
  
  That reproduced exactly the data loss this splitter exists to prevent. The
  existing three berth test did not catch it because A -> B -> C are all
  foreign to A and so are collected in a single pass; the hole only opens
  when a berth repeats inside one stop.
  
  Leave the index in place after a split instead. This terminates because a
  berth call that produced a cut opens a segment carrying that same berth,
  so it is no longer foreign to it and can never cut again.
  
  The segment needing the extra cut is not always the last one, so
  re-checking only the final segment would have been incomplete - covered by
  a test for A -> B -> A -> C, where the un-cut return sits in the middle.
  
  Reported by augmentcode on PR #852.
  
  Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_01TLDWmWxCC92V5sQDdf7AFw
- `046b25a7` **Darius Wattimena** (2026-08-14): TCC-1149 Bump ais-engine to 20260814-b1581.1 (Boot 3.5 based)
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `b3eb4496` **Darius Wattimena** (2026-08-18): Merge pull request #850 from teqplay/TCC-1149-upgrade-spring-boot-3-5-16
  TCC-1149 Upgrade to Spring Boot 3.5.16 and skeleton 2.14.0
- `50fd5ed9` **Joost Dambrink** (2026-08-18): Merge pull request #852 from teqplay/claude/stop-berth-matching-ml8o3y
  Split berth stops at the berths they moved to in post-processing

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-18)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F853%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-08-18)

_No comment._

## Review Comments

## Comments
