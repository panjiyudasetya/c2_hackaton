---
id: github:teqplay/poma-backend:pr:201
source: github
type: pull_request
repo: teqplay/poma-backend
number: 201
title: No more reactive
author: Darius-Wattimena
state: closed
date: '2025-08-11'
merged_at: '2025-08-22'
base_branch: develop
head_branch: no-more-reactive
url: https://github.com/teqplay/poma-backend/pull/201
labels: []
linked_issues: []
explicit_links: []
---
# PR #201: No more reactive

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/201  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `no-more-reactive`  
**Created:** 2025-08-11  
**Merged:** 2025-08-22  

## Description

_No description._

## Commits

- `1c0a7bdb` **Darius Wattimena** (2025-08-08): Remove unused WOP code
- `db28137a` **Darius Wattimena** (2025-08-08): Adjusted webclients to instead make use of resttemplates and no more webflux to avoid loading netty
- `fece4ffb` **Darius Wattimena** (2025-08-08): ktlint

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-08-11)

## Pull Request Overview

This PR removes the reactive WebClient-based implementation for World of Ports (WOP) integration and replaces it with RestTemplate-based HTTP clients. The WOP feature is being deprecated and its configuration is being removed.

- Deprecates the World of Ports feature entirely with @Deprecated annotations
- Replaces WebClient with RestTemplate for HTTP communications in HBR and Slack services
- Removes WOP-specific configuration properties and web client beans

### Reviewed Changes

Copilot reviewed 8 out of 9 changed files in this pull request and generated no comments.

<details>
<summary>Show a summary per file</summary>

| File | Description |
| ---- | ----------- |
| application.yml | Removes WOP configuration properties |
| WopService.kt | Deprecates service and removes import/API call functionality |
| WopRawDatasource.kt | Adds deprecation annotation |
| WopController.kt | Adds deprecation annotation and removes commented import endpoint |
| BerthService.kt | Replaces WebClient with RestTemplate for HBR API calls |
| SlackService.kt | Replaces WebClient with RestTemplate for Slack webhook calls |
| RestTemplateConfiguration.kt | Removes WebClient beans and replaces with RestTemplate configurations |
| Config.kt | Removes WOP configuration properties class |
</details>

### TeqJoostD — APPROVED (2025-08-12)

_No comment._
