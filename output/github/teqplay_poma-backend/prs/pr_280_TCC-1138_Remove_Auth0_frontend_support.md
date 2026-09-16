---
id: github:teqplay/poma-backend:pr:280
source: github
type: pull_request
repo: teqplay/poma-backend
number: 280
title: TCC-1138 Remove Auth0 frontend support
author: michel-teqplay
state: closed
date: '2026-09-09'
merged_at: '2026-09-14'
base_branch: develop
head_branch: TCC-1138-remove-auth0-frontend
url: https://github.com/teqplay/poma-backend/pull/280
labels: []
linked_issues: []
explicit_links: []
---
# PR #280: TCC-1138 Remove Auth0 frontend support

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/280  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `develop` ← `TCC-1138-remove-auth0-frontend`  
**Created:** 2026-09-09  
**Merged:** 2026-09-14  

## Description

Drop the auth-credentials-auth-zero (user/frontend) skeleton module and its auth-credentials-auth0 config block. The s2s modules and auth-credentials-auth0-s2s config stay: the Auth0 logs show data science still authenticates with machine-to-machine tokens.

Also drops the README instructions for hand-extending an Auth0 user token, which no longer apply.

## Commits

- `8e4849c0` **Michel Wilson** (2026-09-07): TCC-1138 Remove Auth0 frontend support
  Drop the auth-credentials-auth-zero (user/frontend) skeleton module and
  its auth-credentials-auth0 config block. The s2s modules and
  auth-credentials-auth0-s2s config stay: the Auth0 logs show data science
  still authenticates with machine-to-machine tokens.
  
  Also drops the README instructions for hand-extending an Auth0 user
  token, which no longer apply.
  
  Co-Authored-By: Claude <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-09)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-09)

### 🟢 Approval recommended

The changes are consistent with the PR goal and no functional issues were identified beyond a minor README wording nit.

<details>
<summary>Pull request overview</summary>

Removes Auth0 **frontend/user-token** support from the backend by deleting the user-facing skeleton dependency and the corresponding Auth0 config/docs, while keeping the Auth0 **s2s (M2M)** path for data science.

**Changes:**
- Remove the `auth-credentials-auth-zero` (frontend/user) skeleton module dependency.
- Drop the `auth-credentials-auth0` config block from `application.yml` (retain `auth-credentials-auth0-s2s`).
- Remove README instructions for manually extending Auth0 user tokens.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `src/main/resources/application.yml` | Removes the Auth0 user config block while leaving Auth0 s2s config intact. |
| `README.md` | Removes outdated instructions for extending Auth0 user tokens. |
| `build.gradle` | Drops the Auth0 frontend/user skeleton dependency and documents why s2s remains. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 2/3 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/poma-backend/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### TeqJoostD — APPROVED (2026-09-10)

_No comment._

## Review Comments

### Copilot — 2026-09-09 on `README.md`

This sentence now introduces a list but lacks punctuation, and the bullet item is split into a hanging continuation line, which makes the README harder to scan.

## Comments
