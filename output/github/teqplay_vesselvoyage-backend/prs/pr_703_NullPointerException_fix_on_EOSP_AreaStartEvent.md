---
id: github:teqplay/vesselvoyage-backend:pr:703
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 703
title: NullPointerException fix on EOSP AreaStartEvent
author: Darius-Wattimena
state: closed
date: '2026-01-23'
merged_at: '2026-01-29'
base_branch: develop
head_branch: npe-fix
url: https://github.com/teqplay/vesselvoyage-backend/pull/703
labels: []
linked_issues: []
explicit_links: []
---
# PR #703: NullPointerException fix on EOSP AreaStartEvent

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/703  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `npe-fix`  
**Created:** 2026-01-23  
**Merged:** 2026-01-29  

## Description

Voyage start and Visit end are the same timestamp so we can just take the Voyage start as that is non-nullable.

Exception would be thrown at Duration.between(visitEnd, voyageEnd) as the first param was nullable but Kotlin didn't complain about it given that it was calling a Java function.

Do note that this only triggers on DEV right now given that the data is corrupted around the time I was experimenting with barges, resulting in Visits without an end time.

## Commits

- `25af4902` **Darius Wattimena** (2026-01-23): Fix potential NPE
- `cd47bf34` **Darius Wattimena** (2026-01-23): Remove unneeded

## Reviews

### github-actions[bot] — COMMENTED (2026-01-23)

Review completed. The changes correctly fix the NullPointerException by using the voyage start time (which should equal the visit end time by design) and remove an unnecessary null assertion operator. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-23)

## Pull request overview

Fixes a NullPointerException during EOSP (End Of Sea Passage) start processing when DEV data contains a previous visit without an end time, and removes an unnecessary non-null assertion in API port mapping.

**Changes:**
- Avoid passing a nullable visit end time into `Duration.between(...)` in `EndOfSeaPassageStartProcessor`.
- Remove `!!` on `port.unlocode` when mapping visit port info to the API model.

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt` | Prevents NPE in EOSP start drift/resume logic by using a non-null timestamp for duration calculation. |
| `src/main/kotlin/nl/teqplay/vesselvoyage/mapper/EntryV2Mapper.kt` | Simplifies port mapping by dropping an unnecessary non-null assertion on `unlocode`. |

### michel-teqplay — APPROVED (2026-01-26)

_No comment._

## Review Comments

### Copilot — 2026-01-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

`visitEnd` is now derived from `currentVoyage.start.time`, so the variable name no longer reflects what it contains and it also ignores `previousVisit.entry.end` when it is present. To keep the original semantics (and only fall back when the visit end is missing), consider using `previousVisit.entry.end?.time` with a fallback to `currentVoyage.start.time`, and rename the variable to something like `previousVisitEndTime`/`voyageStartTime` for clarity.
```suggestion
            // Prefer the recorded end time of the previous visit; fall back to the current voyage start
            // when the previous visit end is not available.
            val previousVisitEndTime = previousVisit.entry.end?.time ?: currentVoyage.start.time
            val voyageEnd = event.actualTime

            val voyageDuration = Duration.between(previousVisitEndTime, voyageEnd)
```

### Copilot — 2026-01-23 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

This change fixes a production crash path (nullable `previousVisit.entry.end?.time` being passed into `Duration.between` via Java interop). Please add a regression test that reproduces the DEV-corrupted-data scenario (voyage status with a `previousVisit` that has a null `end`) and verifies EOSP start processing no longer throws and still takes the intended branch (resume vs. create new visit) based on the duration.
