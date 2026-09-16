---
id: github:teqplay/vesselvoyage-backend:pr:560
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 560
title: Release 😃👍 -  🌸 ８．０８．２０２５ 🌸
author: TeqJoostD
state: closed
date: '2025-07-08'
merged_at: '2025-07-08'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/560
labels: []
linked_issues: []
explicit_links: []
---
# PR #560: Release 😃👍 -  🌸 ８．０８．２０２５ 🌸

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/560  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-07-08  
**Merged:** 2025-07-08  

## Description

_No description._

## Commits

- `616c8334` **TeqJoostD** (2025-05-28): refactor: update event imports and deprecate old event types
- `0bf58932` **TeqJoostD** (2025-05-28): delete todo
- `de896ef4` **Darius Wattimena** (2025-05-28): Fix broken dependency loading
- `88de5814` **TeqJoostD** (2025-06-10): fix: merge conflicts
  fix: failing tests
  fix: apply feedback from PR session
- `e58105f4` **TeqJoostD** (2025-06-24): fix: resolve feedback
- `4d2afe78` **TeqJoostD** (2025-06-27): Merge branch 'develop' into SPV-1948
  # Conflicts:
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/api/PtoStatementOfFactsViewGenerator.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/ActivityEventProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/service/queue/events/EventsDefaultMessageProcessor.kt
  #	src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt
  #	src/test/kotlin/nl/teqplay/vesselvoyage/util/EntryUtilsTest.kt
- `e987a5f6` **TeqJoostD** (2025-06-27): fix merge conflicts
- `f7e978f3` **Darius Wattimena** (2025-07-02): Adjusted getting of the trace to be always being scheduled on both API and processing + added a blocking argument to ensure you always get a trace
- `2a6ba78a` **Darius Wattimena** (2025-07-02): Fix an issue where the TraceService bean wouldn't be loaded in and renamed the old TraceService so they don't clash with naming
- `5ab0ef7e` **Joost Dambrink** (2025-07-02): Merge branch 'develop' into SPV-1948
- `6c6023e4` **Joost Dambrink** (2025-07-03): Merge pull request #519 from teqplay/SPV-1948
  SPV-1948 Change VV models to AisEngine models
- `7aa78113` **Darius Wattimena** (2025-07-03): Fix existing StoryService tests and removed unused parameter for trace generation
- `a699e675` **Darius Wattimena** (2025-07-03): Fix incorrectly mocked trace service and adjusted test name to match controller name
- `773a505c` **Darius Wattimena** (2025-07-03): ktlint
- `98ce2760` **Darius Wattimena** (2025-07-03): copilot feedback
- `a8bff051` **Darius Wattimena** (2025-07-03): Merge branch 'develop' into TCC-248-fix-trace-missing
- `1d8bf089` **TeqJoostD** (2025-07-03): Merge branch 'develop'
  # Conflicts:
  #	api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt
- `91eb1f23` **Joost Dambrink** (2025-07-03): Merge pull request #551 from teqplay/temp-joost
  Temp joost
- `79a04eb3` **Darius Wattimena** (2025-07-03): Merge branch 'develop' into TCC-248-fix-trace-missing
- `3d5e0043` **Darius Wattimena** (2025-07-03): PR feedback
- `ced28f48` **Darius Wattimena** (2025-07-03): ktlint
- `8f264cd6` **Darius Wattimena** (2025-07-04): Merge pull request #548 from teqplay/TCC-248-fix-trace-missing
  TCC-248 fix trace missing
- `8f3578e3` **TeqJoostD** (2025-07-04): increase ais engine version
- `57d01fd6` **Joost Dambrink** (2025-07-04): Merge pull request #555 from teqplay/develop-ais-incrase
  Increase ais-engine version
- `f987afa1` **Darius Wattimena** (2025-07-04): Increase disk
- `540e909f` **Darius Wattimena** (2025-07-04): Merge pull request #556 from teqplay/Increase-disk-size
  Increase disk
- `fdd2330b` **Darius Wattimena** (2025-07-07): Fix batch call of traces breaking
- `75984391` **Darius Wattimena** (2025-07-07): Merge pull request #557 from teqplay/fix-batch-trace-call
  Fix batch call of traces breaking
- `d3d85843` **Darius Wattimena** (2025-07-07): Moved all existing batch calls to avoid a typing issue
- `b84c6488` **Darius Wattimena** (2025-07-07): Merge pull request #558 from teqplay/batch-calls
  Fix other broken batch calls
- `8b66fb1e` **TeqJoostD** (2025-07-08): Merge branch 'master' into merge-coflict-resolver-branch
- `fbf46df9` **TeqJoostD** (2025-07-08): Merge branch 'develop' into merge-coflict-resolver-branch
- `4026953f` **Joost Dambrink** (2025-07-08): Merge pull request #561 from teqplay/merge-coflict-resolver-branch
  Merge coflict resolver branch

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-08)

## Pull Request Overview

This PR updates tests and test utilities to use the new AIS Engine event interfaces and models, removes deprecated tests, and adjusts JSON fixtures to the new event schema.

- Migrate tests from `vesselvoyage.model.event.*` types to `nl.teqplay.aisengine.event.*`
- Remove legacy conversion tests (`EventUtilsTest.kt`, `AisEngineEventUtilsTest.kt`)
- Update JSON fixture (`eventbuffer-removal-events.json`) to use `"type"` discriminator and nested identifiers

### Reviewed Changes

Copilot reviewed 156 out of 157 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File                                                                                       | Description                                               |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| src/test/resources/events/eventbuffer-removal-events.json                                 | Replaced `_type` with `type`, updated event structure     |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/TestUtil.kt                                   | Swapped imports to AIS Engine interfaces                  |
| **(deleted)** src/test/kotlin/nl/teqplay/vesselvoyage/util/EventUtilsTest.kt              | Removed outdated conversion tests                         |
| src/test/kotlin/nl/teqplay/vesselvoyage/util/EntryUtilsTest.kt                             | Adapted calls to include new parameters for port ID       |
| src/test/kotlin/... _(many test files)_                                                   | Updated imports, constructors, and date/time handling     |
</details>



<details>
<summary>Comments suppressed due to low confidence (2)</summary>


**src/test/resources/events/eventbuffer-removal-events.json:18**
* The second event in this fixture still uses "AreaStartEvent" but originally represented an EndOfSeaPassageEvent. Confirm that the JSON discriminator and deserialization logic correctly interpret this as a start-type event for an End-of-Sea Passage, or adjust to a more precise type if needed.
```
    "type": "AreaStartEvent",
```
</details>
