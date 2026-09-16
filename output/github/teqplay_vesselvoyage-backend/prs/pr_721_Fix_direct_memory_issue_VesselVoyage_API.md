---
id: github:teqplay/vesselvoyage-backend:pr:721
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 721
title: Fix direct memory issue VesselVoyage API
author: Darius-Wattimena
state: closed
date: '2026-02-20'
merged_at: '2026-02-20'
base_branch: develop
head_branch: direct-buffer
url: https://github.com/teqplay/vesselvoyage-backend/pull/721
labels: []
linked_issues: []
explicit_links: []
---
# PR #721: Fix direct memory issue VesselVoyage API

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/721  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `direct-buffer`  
**Created:** 2026-02-20  
**Merged:** 2026-02-20  

## Description

_No description._

## Commits

- `8762a813` **Darius Wattimena** (2026-02-20): Set MaxDirectMemorySize to avoid DirectMemory buffer errors in VesselVoyage API

## Reviews

### augmentcode[bot] — COMMENTED (2026-02-20)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-02-20)

## Pull request overview

This PR updates the VesselVoyage API Helm environment-specific values to cap JVM direct (off-heap) memory via `JAVA_TOOL_OPTIONS`, addressing a direct memory issue in the API runtime configuration.

**Changes:**
- Add `JAVA_TOOL_OPTIONS=-XX:MaxDirectMemorySize=512m` to API dev Helm values.
- Add `JAVA_TOOL_OPTIONS=-XX:MaxDirectMemorySize=512m` to API prod Helm values.

### Reviewed changes

Copilot reviewed 2 out of 2 changed files in this pull request and generated no comments.

| File | Description |
| ---- | ----------- |
| helm/values.api-prod.yaml | Adds a JVM direct memory cap for the production API deployment via `JAVA_TOOL_OPTIONS`. |
| helm/values.api-dev.yaml | Adds a JVM direct memory cap for the development API deployment via `JAVA_TOOL_OPTIONS`. |

### TeqJoostD — APPROVED (2026-02-20)

_No comment._

## Comments
