---
id: github:teqplay/vesselvoyage-backend:pr:606
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 606
title: Release 16 Sep 2025
author: Darius-Wattimena
state: closed
date: '2025-09-16'
merged_at: '2025-09-16'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/606
labels: []
linked_issues: []
explicit_links: []
---
# PR #606: Release 16 Sep 2025

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/606  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2025-09-16  
**Merged:** 2025-09-16  

## Description

_No description._

## Commits

- `3159dd7a` **Darius Wattimena** (2025-09-09): Add API endpoints for retrieving current journey state by IMO
- `c33f5925` **TeqJoostD** (2025-09-11): cleanup: change comments
- `7be251f7` **Darius Wattimena** (2025-09-11): Adjusted logic so we still return something even when there might be data missing in the database and add support for the arrival port when in voyage
- `a6ce0830` **Darius Wattimena** (2025-09-11): Added tests to make the journey service works as expected
- `c0aaf18a` **Darius Wattimena** (2025-09-11): Extended VesselVoyage client to include the new journey endpoints
- `ad2d6ba2` **Darius Wattimena** (2025-09-11): code cleanup
- `8c62657c` **Darius Wattimena** (2025-09-11): Corrected usecase where a unlocode would be return where a portId was expected
- `3bb39f4f` **Joost Dambrink** (2025-09-11): Merge pull request #604 from teqplay/api-model-hotfix
  cleanup: change comments
- `1e5168bb` **Darius Wattimena** (2025-09-16): Merge pull request #605 from teqplay/TCC-405
  TCC-405

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-09-16)

## Pull Request Overview

This PR introduces a new Journey API that provides real-time journey state information for vessels, including departure/arrival ports and current status. The implementation adds comprehensive functionality for tracking ship journeys based on visit and voyage statuses.

Key changes:
- New Journey API with endpoints for single and batch IMO queries
- Journey service implementing complex business logic for determining ship status and port relationships
- Client library integration for consuming the Journey API

### Reviewed Changes

Copilot reviewed 7 out of 7 changed files in this pull request and generated 2 comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| JourneyService.kt | Core business logic for determining journey status from ship data |
| ApiJourneyController.kt | REST endpoints for retrieving journey information by IMO |
| VesselVoyageClient.kt | Client library methods for consuming Journey API |
| Journey.kt | Data model definitions for journey, departure port, and arrival port |
| JourneyServiceTest.kt | Comprehensive test suite covering all journey status scenarios |
| Port.kt | Updated documentation to clarify field content |
| build.gradle | Added SpringDoc OpenAPI dependency |
</details>

## Review Comments

### Copilot — 2025-09-16 on `src/test/kotlin/nl/teqplay/vesselvoyage/service/api/JourneyServiceTest.kt`

This hardcoded port ID appears to be a placeholder value (16 'A' characters) rather than a realistic test value. Consider using a more descriptive test constant or a UUID-like format that matches the expected port ID structure.
```suggestion
        val dehamPortId = "123e4567-e89b-12d3-a456-426614174000"
```

### Copilot — 2025-09-16 on `src/main/kotlin/nl/teqplay/vesselvoyage/controller/api/ApiJourneyController.kt`

Catching all exceptions with a generic Exception type can mask important errors and make debugging difficult. Consider catching specific exception types (like BadRequestException) or at minimum log the exception before returning null.
