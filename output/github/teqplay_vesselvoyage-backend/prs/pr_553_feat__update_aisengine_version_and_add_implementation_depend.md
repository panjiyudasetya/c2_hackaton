---
id: github:teqplay/vesselvoyage-backend:pr:553
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 553
title: 'feat: update aisengine version and add implementation dependency'
author: TeqJoostD
state: closed
date: '2025-07-04'
merged_at: null
base_branch: master
head_branch: master-ais-increase
url: https://github.com/teqplay/vesselvoyage-backend/pull/553
labels: []
linked_issues: []
explicit_links: []
---
# PR #553: feat: update aisengine version and add implementation dependency

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/553  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `master-ais-increase`  
**Created:** 2025-07-04  

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
- `5ab0ef7e` **Joost Dambrink** (2025-07-02): Merge branch 'develop' into SPV-1948
- `6c6023e4` **Joost Dambrink** (2025-07-03): Merge pull request #519 from teqplay/SPV-1948
  SPV-1948 Change VV models to AisEngine models
- `1d8bf089` **TeqJoostD** (2025-07-03): Merge branch 'develop'
  # Conflicts:
  #	api/src/main/kotlin/nl/teqplay/vesselvoyage/model/event/EncounterType.kt
- `91eb1f23` **Joost Dambrink** (2025-07-03): Merge pull request #551 from teqplay/temp-joost
  Temp joost
- `43cc3fd4` **TeqJoostD** (2025-07-04): feat: update aisengine version and add implementation dependency
- `1dab1761` **TeqJoostD** (2025-07-04): Merge branch 'develop' into master-ais-increase
  # Conflicts:
  #	api/build.gradle

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-07-04)

## Pull Request Overview

This PR updates the AIS engine version and adds a model dependency with an exclusion to the API module.

- Introduces `aisengine_version` property
- Adds `nl.teqplay.aisengine:models` implementation dependency with an exclude for `nl.teqplay.vesselvoyage:api`

## Review Comments

### Copilot — 2025-07-04 on `api/build.gradle`

[nitpick] Use single quotes for version literals to match existing style (e.g., change \"master-2.3.0\" to 'master-2.3.0').
```suggestion
        aisengine_version = 'master-2.3.0'
```

### Copilot — 2025-07-04 on `api/build.gradle`

[nitpick] Remove the space between the method name and parentheses for consistency with other declarations: use `implementation("...")` instead of `implementation ("...")`.
```suggestion
    implementation("nl.teqplay.aisengine:models:$aisengine_version") {
```
