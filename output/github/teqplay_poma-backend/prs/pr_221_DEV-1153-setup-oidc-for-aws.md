---
id: github:teqplay/poma-backend:pr:221
source: github
type: pull_request
repo: teqplay/poma-backend
number: 221
title: DEV-1153-setup-oidc-for-aws
author: Jamie-de-Leest
state: closed
date: '2025-12-18'
merged_at: '2025-12-22'
base_branch: develop
head_branch: DEV-1153-setup-oidc-for-aws
url: https://github.com/teqplay/poma-backend/pull/221
labels: []
linked_issues: []
explicit_links: []
---
# PR #221: DEV-1153-setup-oidc-for-aws

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/221  
**State:** closed | **Author:** Jamie-de-Leest  
**Base ← Head:** `develop` ← `DEV-1153-setup-oidc-for-aws`  
**Created:** 2025-12-18  
**Merged:** 2025-12-22  

## Description

_No description._

## Commits

- `452b801a` **Jamie de Leest** (2025-12-18): DEV-1153-setup-oidc-for-aws

## Reviews

### github-actions[bot] — COMMENTED (2025-12-18)

Review completed. The migration from AWS access keys to OIDC authentication is a security improvement. No suggestions at this time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-12-18)

## Pull request overview

This PR transitions AWS authentication from static access keys to OIDC (OpenID Connect) authentication for GitHub Actions workflows. This is a security improvement that eliminates the need to store long-lived AWS credentials as GitHub secrets.

- Removes AWS access key and secret key authentication
- Introduces AWS account ID-based authentication for OIDC
- Maintains separate configurations for production and development environments





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### Joost1991 — APPROVED (2025-12-22)

_No comment._
