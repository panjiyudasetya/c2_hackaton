---
id: github:teqplay/vesselvoyage-backend:pr:582
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 582
title: TCC-295 fix overlapping eosp
author: Darius-Wattimena
state: closed
date: '2025-08-05'
merged_at: '2025-08-05'
base_branch: develop
head_branch: TCC-295-fix-overlapping-eosp
url: https://github.com/teqplay/vesselvoyage-backend/pull/582
labels: []
linked_issues: []
explicit_links: []
---
# PR #582: TCC-295 fix overlapping eosp

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/582  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-295-fix-overlapping-eosp`  
**Created:** 2025-08-05  
**Merged:** 2025-08-05  

## Description

Things to note:
- Logic has been tested with all the 150~ or so ships that got provided by the projects team. Fixing issues such as https://vesselvoyagedev.teqplay.nl/#/ships/9359260/story/32b4da15-522d-40f7-82d8-7235a0c49f4d.VISIT?mode=period&months=50 which were completely broken.
- I did not add test yet given the amount of additional time it would take me, given that the scenario is super complex. There will be a followup branch TCC-295-fix-overlapping-eosp-test which contains a bunch of testing to cover the adjusted code

## Commits

- `51044785` **Darius Wattimena** (2025-08-04): Adjusted logic so we don't create fallbacks when we left the EOSP but didn't receive the needed EOSP events as this resulted in a lot more incorrect cases
- `b4d9e561` **Darius Wattimena** (2025-08-04): Fix an issue where stops in new ports can result in incorrect visit structures when we have main ports overlapping fully when at berths
- `e40c7f88` **Darius Wattimena** (2025-08-04): ktlint
- `069932e3` **Darius Wattimena** (2025-08-04): Removed unused code

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-05)

## Pull Request Overview

This PR fixes issues related to overlapping End of Sea Passage (EOSP) processing in the vessel voyage tracking system. The changes aim to resolve broken ship voyage tracking scenarios where ships move between multiple EOSP areas simultaneously.

Key changes:
- Removed complex missed end event handling logic from EOSP start processing
- Added utility functions for splitting visit activities based on time boundaries
- Enhanced stop processors to handle port switching when ships stop in different main port areas
- Refactored constructor calls to use named parameters for better maintainability

### Reviewed Changes

Copilot reviewed 10 out of 10 changed files in this pull request and generated 4 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| EventProcessingServiceTest.kt | Removed obsolete test imports and complex test cases for missed EOSP end events |
| BaseEventProcessingTest.kt | Updated service constructor to use named parameters instead of positional |
| entryUtils.kt | Added utility functions for visit splitting and pass-through activity creation |
| StopStartProcessor.kt | Enhanced with logic to detect and handle port switching during stops |
| StopEndProcessor.kt | Removed unused import for actualTime utility |
| EndOfSeaPassageStartProcessor.kt | Significantly simplified by removing missed end event handling logic |
| EventProcessor.kt | Added TODO comment for validation check relocation |
| InfraService.kt | Added location-in-area checking and updated main port detection |
| EventFetchingService.kt | Reduced log verbosity for event fetching operations |
| Port.kt | Added convenience method to check if port is a main port |
</details>

### leonjoosse — DISMISSED (2025-08-05)

_No comment._

### leonjoosse — APPROVED (2025-08-05)

_No comment._

## Review Comments

### Copilot — 2025-08-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

The import `kotlin.collections.plus` is unnecessary as the plus operator for collections is available by default in Kotlin.
```suggestion

```

### Copilot — 2025-08-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt`

This complex conditional logic spanning multiple concerns should be extracted into a well-named private method to improve readability and maintainability.

### Copilot — 2025-08-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/util/entryUtils.kt`

[nitpick] Using `buildList` with `addAll` operations is less efficient than using the `+` operator for list concatenation, especially for small lists.
```suggestion
    val mergedPassThrough = previousVoyage.passThroughEosp +
        currentVisit.passThroughEosp +
        listOfNotNull(visitPassThrough)
```

### Copilot — 2025-08-05 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/stop/StopStartProcessor.kt`

[nitpick] The comment on line 169-170 mentions this scenario but the logic handling could be more explicit. Consider adding a more descriptive comment explaining why returning null is the correct behavior here.
