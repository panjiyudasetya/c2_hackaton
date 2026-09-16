---
id: github:teqplay/poma-backend:pr:219
source: github
type: pull_request
repo: teqplay/poma-backend
number: 219
title: Increase CPU requests to reflect actual usage
author: michel-teqplay
state: closed
date: '2025-12-10'
merged_at: '2025-12-10'
base_branch: develop
head_branch: increase-requests
url: https://github.com/teqplay/poma-backend/pull/219
labels: []
linked_issues: []
explicit_links: []
---
# PR #219: Increase CPU requests to reflect actual usage

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/219  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `increase-requests`  
**Created:** 2025-12-10  
**Merged:** 2025-12-10  

## Description

_No description._

## Commits

- `69ca1dec` **Michel Wilson** (2025-12-10): Increase CPU requests to reflect actual usage

## Reviews

### github-actions[bot] — COMMENTED (2025-12-10)

Review completed. The CPU request increase appears reasonable given the 10x jump from 0.01 to 0.1 cores, though documentation of the actual usage metrics that justified this change would be valuable for future reference.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-10)

## Pull request overview

This PR increases the CPU request allocation for the application from 0.01 to 0.1 (a 10x increase) to better align with actual usage patterns. This change should help prevent CPU throttling and improve application performance by ensuring adequate CPU resources are reserved.

- CPU request increased from 0.01 to 0.1 cores





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### Darius-Wattimena — APPROVED (2025-12-10)

_No comment._
