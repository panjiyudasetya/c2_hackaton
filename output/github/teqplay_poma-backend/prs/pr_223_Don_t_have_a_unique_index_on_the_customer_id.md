---
id: github:teqplay/poma-backend:pr:223
source: github
type: pull_request
repo: teqplay/poma-backend
number: 223
title: Don't have a unique index on the customer id
author: michel-teqplay
state: closed
date: '2026-01-07'
merged_at: '2026-01-07'
base_branch: develop
head_branch: TCC-577_multiple-areas-per-customer
url: https://github.com/teqplay/poma-backend/pull/223
labels: []
linked_issues: []
explicit_links: []
---
# PR #223: Don't have a unique index on the customer id

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/223  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-577_multiple-areas-per-customer`  
**Created:** 2026-01-07  
**Merged:** 2026-01-07  

## Description

_No description._

## Commits

- `49a8a79d` **Michel Wilson** (2026-01-07): Don't have a unique index on the customer id

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-01-07)

## Pull request overview

This PR removes the unique index constraint on the `customerId` field in the CustomerArea collection, replacing it with a regular index. This change allows multiple customer areas to be associated with the same customer ID.

- Converts `customerId` from a unique index to a regular index
- Maintains query performance through indexing while allowing duplicate customer IDs





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### github-actions[bot] — COMMENTED (2026-01-07)

The code change correctly removes the unique constraint on `customerId` to support multiple areas per customer. However, MongoDB's `ensureIndex` won't automatically drop an existing unique index, which may require manual database migration.

---
*🤖 Automated review complete. Please react with 👍 or 👎 on the individual review comments to provide feedback on their usefulness.*

### Darius-Wattimena — APPROVED (2026-01-07)

_No comment._

## Review Comments
