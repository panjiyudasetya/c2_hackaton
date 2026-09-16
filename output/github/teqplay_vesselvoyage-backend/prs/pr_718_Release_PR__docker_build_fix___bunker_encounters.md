---
id: github:teqplay/vesselvoyage-backend:pr:718
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 718
title: 'Release PR: docker build fix + bunker encounters'
author: michel-teqplay
state: closed
date: '2026-02-18'
merged_at: '2026-02-18'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/718
labels: []
linked_issues: []
explicit_links: []
---
# PR #718: Release PR: docker build fix + bunker encounters

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/718  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-02-18  
**Merged:** 2026-02-18  

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
- `6fe2b18a` **Darius Wattimena** (2026-02-18): Revert "Fix negative PTO SOF terminal times by preventing inverted stops"
- `9e851daf` **Darius Wattimena** (2026-02-18): Merge pull request #716 from teqplay/revert-714-fix-negative-pto-sof-times
  Revert "Fix negative PTO SOF terminal times by preventing inverted stops"

## Reviews

### github-actions[bot] — COMMENTED (2026-02-18)

Reviewed the Spring Boot version upgrade from 3.4.4 to 3.4.12. The changes are consistent across all three build files.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — APPROVED (2026-02-18)

_No comment._

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-18)

## Pull request overview

Updates Spring Boot plugin/BOM version used across the multi-module Gradle build.

**Changes:**
- Bump `spring_boot_version` from `3.4.4` to `3.4.12` in root build.
- Bump `spring_boot_version` from `3.4.4` to `3.4.12` in `api` module.
- Bump `spring_boot_version` from `3.4.4` to `3.4.12` in `client` module.

### Reviewed changes

Copilot reviewed 2 out of 3 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| `build.gradle` | Updates shared Spring Boot version used by the root project plugins. |
| `api/build.gradle` | Aligns `api` module Spring Boot version with the release bump. |
| `client/build.gradle` | Aligns `client` module Spring Boot version with the release bump. |

## Review Comments
