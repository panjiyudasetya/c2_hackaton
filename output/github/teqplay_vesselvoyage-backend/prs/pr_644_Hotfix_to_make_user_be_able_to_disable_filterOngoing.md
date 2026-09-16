---
id: github:teqplay/vesselvoyage-backend:pr:644
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 644
title: Hotfix to make user be able to disable filterOngoing
author: TeqJoostD
state: closed
date: '2025-10-21'
merged_at: '2025-10-21'
base_branch: master
head_branch: vesselvoyage-client-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/644
labels: []
linked_issues: []
explicit_links: []
---
# PR #644: Hotfix to make user be able to disable filterOngoing

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/644  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `vesselvoyage-client-hotfix`  
**Created:** 2025-10-21  
**Merged:** 2025-10-21  

## Description

_No description._

## Commits

- `37e60289` **TeqJoostD** (2025-10-21): Hotfix to make user be able to disable filterOngoing

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-21)

## Pull Request Overview

This PR introduces a configurable `filterMultipleOngoing` parameter to allow users to control filtering behavior for ongoing voyage entries. Previously hardcoded to `true`, this parameter is now exposed through the API endpoint and client with a default value of `true` to maintain backward compatibility.

- Added `filterMultipleOngoing` parameter with a default value of `true` to the API endpoint
- Updated all three request model implementations to include the new parameter
- Modified the client to support passing this parameter through to the API

### Reviewed Changes

Copilot reviewed 3 out of 3 changed files in this pull request and generated 2 comments.

| File | Description |
| ---- | ----------- |
| `ApiVoyageV2Controller.kt` | Added `filterMultipleOngoing` parameter to the endpoint and passed it through to request models and response mapping |
| `VesselVoyageClient.kt` | Added `filterMultipleOngoing` parameter to the client method with default value and documentation |
| `VoyagesByPortRequest.kt` | Added `filterMultipleOngoing` property to the interface and all three implementing data classes |

## Review Comments

### Copilot — 2025-10-21 on `api/src/main/kotlin/nl/teqplay/vesselvoyage/apiv2/model/requestresponse/VoyagesByPortRequest.kt`

The documentation states 'not sure what this does since no documentation' which provides no useful information about the parameter's purpose. Based on the code context, this parameter controls whether to filter out all ongoing voyage entries except the last one. Update the documentation to clearly explain this behavior.

### Copilot — 2025-10-21 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

The documentation comment 'filter out all ongoing entries but the last' lacks clarity about what constitutes an 'ongoing entry' and what 'the last' refers to (most recent? final in list?). Provide more specific documentation about what entries are filtered and the criteria used for filtering.
