---
id: github:teqplay/poma-backend:pr:216
source: github
type: pull_request
repo: teqplay/poma-backend
number: 216
title: Added Slack deployment notifications
author: PimTeqplay
state: closed
date: '2025-11-18'
merged_at: '2025-11-20'
base_branch: develop
head_branch: slack-deploy-notification
url: https://github.com/teqplay/poma-backend/pull/216
labels: []
linked_issues: []
explicit_links: []
---
# PR #216: Added Slack deployment notifications

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/216  
**State:** closed | **Author:** PimTeqplay  
**Base ← Head:** `develop` ← `slack-deploy-notification`  
**Created:** 2025-11-18  
**Merged:** 2025-11-20  

## Description

_No description._

## Commits

- `dc602b8e` **Pim van den Toorn** (2025-11-03): Added Slack deployment notifications

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2025-11-18)

## Pull Request Overview

This PR adds Slack deployment notifications to the GitHub Actions workflow by configuring Slack channel IDs, environment-specific success URLs, and authentication credentials for the reusable backend workflow.

- Adds Slack channel configuration for development and production notifications
- Configures success URLs for all four deployment environments (production, data, develop, sandbox)
- Adds Slack bot token secret for authentication





---

💡 <a href="/teqplay/poma-backend/new/develop/.github/instructions?filename=*.instructions.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add Copilot custom instructions</a> for smarter, more guided reviews. <a href="https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn how to get started</a>.

### Jamie-de-Leest — APPROVED (2025-11-19)

_No comment._
