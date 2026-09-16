---
id: github:teqplay/vesselvoyage-backend:pr:646
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 646
title: Hotfix to make user be able to disable filterOngoing
author: TeqJoostD
state: closed
date: '2025-10-21'
merged_at: '2025-10-21'
base_branch: master
head_branch: vesselvoyage-client-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/646
labels: []
linked_issues: []
explicit_links: []
---
# PR #646: Hotfix to make user be able to disable filterOngoing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/646  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `vesselvoyage-client-hotfix`  
**Created:** 2025-10-21  
**Merged:** 2025-10-21  

## Description

_No description._

## Commits

- `5f038c19` **TeqJoostD** (2025-10-21): Hotfix to make user be able to disable filterOngoing

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-21)

## Pull Request Overview

This PR adds a configurable `filterMultipleOngoing` parameter to the `findByPort` API endpoint, allowing users to control whether multiple ongoing visits are filtered. Previously, this value was hardcoded to `true`.

**Key Changes:**
- Added `filterMultipleOngoing` boolean parameter with default value `true` to maintain backward compatibility
- Updated the controller to pass the parameter through to the filtering logic
- Modified the client to support the new parameter

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| ApiVisitV2Controller.kt | Added `filterMultipleOngoing` parameter to endpoint and passed it to the mapping function instead of hardcoded `true` |
| VesselVoyageClient.kt | Added `filterMultipleOngoing` parameter to client method with default value `true` |
| VisitByPortRequest.kt | Added `filterMultipleOngoing` field to request model with default value `true` |

## Review Comments

### Copilot — 2025-10-21 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

The documentation for `filterMultipleOngoing` only contains a TODO note. Add a proper description explaining what this parameter does (e.g., 'When true, filters out multiple ongoing visits for the same vessel').
```suggestion
         * @param filterMultipleOngoing When true, filters out multiple ongoing visits for the same vessel.
```

### Copilot — 2025-10-21 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VisitByPortRequest.kt`

The documentation for `filterMultipleOngoing` only contains a TODO note. Add a proper description explaining the purpose of this field, similar to the other documented fields in this class.
```suggestion
     * If true, filters out ships with multiple ongoing visits to the same port, returning only one ongoing visit per ship.
     * If false, allows multiple ongoing visits per ship to be included in the results.
     * Default is true.
```
