---
id: github:teqplay/vesselvoyage-backend:pr:645
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 645
title: Release
author: TeqJoostD
state: closed
date: '2025-10-21'
merged_at: '2025-10-21'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/645
labels: []
linked_issues: []
explicit_links: []
---
# PR #645: Release

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/645  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-10-21  
**Merged:** 2025-10-21  

## Description

_No description._

## Commits

- `7f606b15` **Jamie de Leest** (2025-10-15): feat: update github actions workflow and helm values for revents migration to dev ou
- `9dc5245b` **TeqJoostD** (2025-10-17): add maximum duration for resuming visit
- `e364d1f5` **jamie-teqplay** (2025-10-20): Merge pull request #638 from teqplay/DEV-1032-migrate-revents-vesselvoyage-to-dev-ou
  DEV-1032-migrate-revents-vesselvoyage-to-dev-ou
- `1f3a34a4` **Joost Dambrink** (2025-10-21): Merge pull request #641 from teqplay/master-sts-hotfix
  Master sts hotfix

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-21)

## Pull Request Overview

This PR introduces a time-based threshold for resuming port visits and restructures deployment configurations across environments. The main change adds a 7-day limit to prevent resuming old visits when vessels re-enter the same EOSP area after extended absences, ensuring more accurate voyage tracking.

**Key Changes:**
- Added 7-day threshold logic to prevent resuming stale port visits in EndOfSeaPassageStartProcessor
- Reorganized Helm configuration by moving global settings from base values.yaml to environment-specific files
- Added new AWS credentials for develop environment deployment

### Reviewed Changes

Copilot reviewed 9 out of 9 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt | Implements 7-day duration check to prevent resuming old visits when re-entering EOSP |
| helm/values.yaml | Removes global configuration settings (moved to environment-specific files) |
| helm/values.revents.yaml | Removes global namespace override and adds ingress/storage configuration |
| helm/values.processing-prod.yaml | Adds global configuration previously in base values.yaml |
| helm/values.processing-dev.yaml | Adds global configuration previously in base values.yaml |
| helm/values.processing-data.yaml | Adds global configuration previously in base values.yaml |
| helm/values.api-prod.yaml | Adds global configuration previously in base values.yaml |
| helm/values.api-dev.yaml | Adds global configuration previously in base values.yaml |
| .github/workflows/main.yml | Adds new AWS credentials for develop environment cluster |
</details>

## Review Comments

### Copilot — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

Potential null pointer issue: `visitEnd` can be null (from `previousVisit.entry.end?.time`), but `Duration.between()` requires non-null arguments. This will throw a NullPointerException if `visitEnd` is null. Add null check before calculating duration or provide a fallback value.

### Copilot — 2025-10-21 on `src/main/kotlin/nl/teqplay/vesselvoyage/service/processing/eosp/EndOfSeaPassageStartProcessor.kt`

The comment contains a logical inconsistency with the code. The comment says 'bigger than 7 days' but the condition checks for 'less than 7 days' (`voyageDuration < Duration.ofDays(7)`). The comment should read: 'If the time between entering the EOSP again is less than 7 days, resume the old visit'.
```suggestion
            // If the time between entering the EOSP again is less than 7 days, resume the old visit
```
