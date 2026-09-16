---
id: github:teqplay/vesselvoyage-backend:pr:622
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 622
title: 'fix: Sort entries before assuming the entries are sorted when merging…'
author: TeqJoostD
state: closed
date: '2025-10-03'
merged_at: '2025-10-03'
base_branch: master
head_branch: revents-merge-hotfix
url: https://github.com/teqplay/vesselvoyage-backend/pull/622
labels: []
linked_issues: []
explicit_links: []
---
# PR #622: fix: Sort entries before assuming the entries are sorted when merging…

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/622  
**State:** closed | **Author:** TeqJoostD  
**Base ← Head:** `master` ← `revents-merge-hotfix`  
**Created:** 2025-10-03  
**Merged:** 2025-10-03  

## Description

… back revents vesselvoyage changes.

## Commits

- `6c4a4d27` **TeqJoostD** (2025-10-03): fix: Sort entries before assuming the entries are sorted when merging back revents vesselvoyage changes.

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-10-03)

## Pull Request Overview

This PR fixes a bug in the entries merge service where the code was assuming entries were sorted by start time without actually ensuring they were sorted first. The fix sorts the entries at the beginning of the merge process before performing any operations that depend on chronological order.

### Key Changes
- Sort entries by start time before processing
- Replace all references to the original unsorted entries with the sorted version
