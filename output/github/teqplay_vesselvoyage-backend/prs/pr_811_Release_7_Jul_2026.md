---
id: github:teqplay/vesselvoyage-backend:pr:811
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 811
title: Release 7 Jul 2026
author: Darius-Wattimena
state: closed
date: '2026-07-07'
merged_at: '2026-07-07'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/811
labels: []
linked_issues: []
explicit_links: []
---
# PR #811: Release 7 Jul 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/811  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-07-07  
**Merged:** 2026-07-07  

## Description

_No description._

## Commits

- `5f8e00ea` **Darius Wattimena** (2026-06-25): Remove all V1 code
- `255e0c7f` **Darius Wattimena** (2026-06-25): Adjusted tests to also work with V1 removed
- `f857069e` **Darius Wattimena** (2026-06-25): Correct all broken tests
- `9e3b5631` **Darius Wattimena** (2026-06-25): ktlint please
- `770c4e0b` **Darius Wattimena** (2026-06-25): Remove unused properties
- `03433534` **TeqJoostD** (2026-06-29): feat(recalculation): add excludeBarges option to port recalculation
  Expose `excludeBarges` on POST /v2/recalculate/port/{unlocode} and thread
  it through to the revents `Scenario.Settings.excludeBarges` flag, so a
  port recalculation can drop barge data. Revents resolves the port's ships
  and applies the filter.
  
  Requires bumping `aisengine_version` to a build containing the revents
  `Scenario.Settings.excludeBarges` field (see TODO in build.gradle); it
  does not compile until then.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `1b195517` **Michel Wilson** (2026-06-30): Add role to ShipDetails
- `f884ec63` **TeqJoostD** (2026-06-30): chore(deps): bump aisengine_version to 20260630-SNAPSHOT for excludeBarges
  The revents Scenario.Settings.excludeBarges field (ais-engine PR #1527,
  merged to develop) is published in 20260630-SNAPSHOT. Bumping unblocks the
  port recalculation excludeBarges option, which now compiles and tests pass.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `e50b5c1e` **TeqJoostD** (2026-06-30): test: fix createScenarioRequestForPort matcher count in recalculateByPort test
  Add the missing matcher for the new excludeBarges parameter in the stub and
  verify of ReventsRecalculationServiceTest, fixing InvalidUseOfMatchersException.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `c69d9aa1` **Darius Wattimena** (2026-07-01): Merge pull request #801 from teqplay/v1-purge
  V1 purge
- `c05b10d1` **TeqJoostD** (2026-07-01): chore(deps): bump aisengine_version to 20260701-b1433.1
  Pin the released ais-engine build containing the revents
  Scenario.Settings.excludeBarges field.
  
  Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
- `e4681176` **Joost Dambrink** (2026-07-01): Merge pull request #804 from teqplay/TCC-1012
  feat(recalculation): add excludeBarges option to port recalculation
- `b98a6b76` **Darius Wattimena** (2026-07-01): feat(encounter): add encounter API v2 endpoints
- `05f6fd57` **Darius Wattimena** (2026-07-01): feat(encounter): add OpenAPI schema annotations
- `03ccbf2e` **Darius Wattimena** (2026-07-01): fix(config): increase CSI REST template read timeout to 60s
- `6725918e` **Darius Wattimena** (2026-07-01): fix(config): increase Poma REST template read timeout to 60s
- `c5b3aae7` **Darius Wattimena** (2026-07-01): Adjusted output to also include port id and unlocode
- `ff113ef7` **Darius Wattimena** (2026-07-01): Added unit tests for the new encounter endpoints
- `c886a1e0` **Darius Wattimena** (2026-07-02): Added more unit tests to cover data source
- `4b60cbd5` **Michel Wilson** (2026-07-02): Merge pull request #805 from teqplay/TCC-1018-ship-role
  Add role to ShipDetails
- `2d6253e1` **Darius Wattimena** (2026-07-02): Merge pull request #807 from teqplay/TCC-1005-bunker-encounter-api
  TCC-1005 bunker encounter api
- `7cc33d60` **Darius Wattimena** (2026-07-02): Fix broken tests after merging PR in develop
- `b496e1f3` **Darius Wattimena** (2026-07-06): Merge pull request #808 from teqplay/TCC-1005-fix-tests-failing
  TCC-1005 Fix broken tests after merging PR in develop

## Reviews

### michel-teqplay — APPROVED (2026-07-07)

_No comment._

## Comments
