---
id: github:teqplay/vesselvoyage-backend:pr:697
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 697
title: TCC-636 support event processing dry run by Ship ID
author: Darius-Wattimena
state: closed
date: '2026-01-16'
merged_at: '2026-01-19'
base_branch: develop
head_branch: TCC-636-event-dry-run
url: https://github.com/teqplay/vesselvoyage-backend/pull/697
labels: []
linked_issues: []
explicit_links: []
---
# PR #697: TCC-636 support event processing dry run by Ship ID

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/697  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `TCC-636-event-dry-run`  
**Created:** 2026-01-16  
**Merged:** 2026-01-19  

## Description

_No description._

## Commits

- `2341a32d` **Darius Wattimena** (2026-01-16): Adjusted event processing endpoint to work with both IMOs and Ship IDs
- `ed8ee08e` **Darius Wattimena** (2026-01-16): ktlint

## Reviews

### github-actions[bot] — COMMENTED (2026-01-16)

Review completed. Found one potential bug related to error handling when an IMO cannot be resolved to a shipId.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### github-actions[bot] — COMMENTED (2026-01-16)

The endpoint now supports both IMO and shipId parameters, which improves flexibility. However, there's a potential logic issue with how invalid IMOs are handled.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### michel-teqplay — DISMISSED (2026-01-19)

_No comment._

### michel-teqplay — APPROVED (2026-01-19)

_No comment._

## Review Comments
