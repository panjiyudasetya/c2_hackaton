---
id: github:teqplay/vesselvoyage-backend:pr:642
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 642
title: fix parameter naming
author: TeqJoostD
state: closed
date: '2025-10-20'
merged_at: '2025-10-20'
base_branch: master
head_branch: client-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/642
labels: []
linked_issues: []
explicit_links: []
---
# PR #642: fix parameter naming

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/642  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `client-hotfix`  
**Created:** 2025-10-20  
**Merged:** 2025-10-20  

## Description

_No description._

## Commits

- `c5155f09` **TeqJoostD** (2025-10-20): fix parameter naming

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-20)

## Pull Request Overview

This PR fixes a parameter naming inconsistency in the VesselVoyageClient by correcting the key name from "destinationPortAreaIds" to "destinationAreaIds" while keeping the actual variable reference unchanged.

- Corrected parameter key name for destination area IDs to match expected API contract
