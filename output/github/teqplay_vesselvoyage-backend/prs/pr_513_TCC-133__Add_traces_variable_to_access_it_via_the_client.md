---
id: github:teqplay/vesselvoyage-backend:pr:513
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 513
title: 'TCC-133: Add traces variable to access it via the client'
author: leonjoosse
state: closed
date: '2025-05-26'
merged_at: '2025-05-26'
base_branch: develop
head_branch: TCC-133-fixclient
url: https://github.com/teqplay/vesselvoyage-backend/pull/513
labels: []
linked_issues: []
explicit_links: []
---
# PR #513: TCC-133: Add traces variable to access it via the client

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/513  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `TCC-133-fixclient`  
**Created:** 2025-05-26  
**Merged:** 2025-05-26  

## Description

_No description._

## Commits

- `97233548` **leonj** (2025-05-26): Add traces variable to access it via the client

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-05-26)

## Pull Request Overview

This PR adds support to access the traces endpoint via the client by introducing a new client variable and updating the documentation.  
- Added a new Traces client instance with the endpoint "/v2/traces".  
- Updated the documentation to include reference to the traces endpoint.


<details>
<summary>Comments suppressed due to low confidence (1)</summary>

**client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt:57**
* Consider adding tests to verify that the new traces endpoint functions correctly and integrates well with the client.
```
val traces = Traces(restTemplate, "/v2/traces")
```
</details>

### Darius-Wattimena — APPROVED (2025-05-26)

_No comment._
