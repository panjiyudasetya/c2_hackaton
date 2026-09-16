---
id: github:teqplay/vesselvoyage-backend:pr:573
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 573
title: Fix valid event type check
author: Darius-Wattimena
state: closed
date: '2025-07-15'
merged_at: '2025-07-17'
base_branch: develop
head_branch: fix-missing-encounters
url: https://github.com/teqplay/vesselvoyage-backend/pull/573
labels: []
linked_issues: []
explicit_links: []
---
# PR #573: Fix valid event type check

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/573  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix-missing-encounters`  
**Created:** 2025-07-15  
**Merged:** 2025-07-17  

## Description

_No description._

## Commits

- `a2b606c9` **Darius Wattimena** (2025-07-15): Added test cases ensuring we process the correct event types and ignore all events we don't support
- `e9103dee` **Darius Wattimena** (2025-07-15): Adjusted logic to match expected event coverage
- `7cf46910` **Darius Wattimena** (2025-07-15): code cleanup
- `bf037a1d` **Darius Wattimena** (2025-07-15): Update src/main/kotlin/nl/teqplay/vesselvoyage/logic/EventTypeValidator.kt
  Co-authored-by: Copilot <175728472+Copilot@users.noreply.github.com>

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-15)

## Pull Request Overview

This PR updates the `EventTypeValidator` to accept all encounter events and refines area event validation to only consider start/end events, and adds a broad suite of parameterized tests to cover valid and invalid `Event` types.

- Changed `isValid` to always accept any `EncounterEvent` and to explicitly filter `AreaEvent` to only `AreaStartEvent` and `AreaEndEvent` with allowed types.
- Introduced a new `EventTypeValidatorTest` with parameterized tests covering each `EncounterType`, valid and invalid `AreaType`, and unsupported events.

### Reviewed Changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated 1 comment.

| File                                                              | Description                                          |
| ----------------------------------------------------------------- | ---------------------------------------------------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/logic/EventTypeValidator.kt | Refined `isValid` logic for `EncounterEvent` and `AreaEvent` |
| src/test/kotlin/nl/teqplay/vesselvoyage/logic/EventTypeValidatorTest.kt | Added comprehensive parameterized tests for `isValid` |


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**src/test/kotlin/nl/teqplay/vesselvoyage/logic/EventTypeValidatorTest.kt:117**
* Add test cases for `AreaEndEvent` alongside `AreaStartEvent` for both valid and invalid `AreaType` values to ensure the validator correctly handles end events as well as start events.
```
        Arguments.of(mockAreaEvent(AreaType.PORT), true),
```
</details>

### TeqJoostD — APPROVED (2025-07-17)

_No comment._

## Review Comments

### Copilot — 2025-07-15 on `src/main/kotlin/nl/teqplay/vesselvoyage/logic/EventTypeValidator.kt`

[nitpick] Use `true` instead of `return true` in the `when` branch so that the entire `when` expression consistently returns a Boolean, improving readability and avoiding mixing expression and statement style.
```suggestion
            is EncounterEvent -> true
```
