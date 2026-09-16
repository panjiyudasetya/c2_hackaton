---
id: github:teqplay/poma-backend:pr:281
source: github
type: pull_request
repo: teqplay/poma-backend
number: 281
title: 'Release PR: remove auth0 frontend support'
author: michel-teqplay
state: closed
date: '2026-09-14'
merged_at: '2026-09-14'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/poma-backend/pull/281
labels: []
linked_issues: []
explicit_links: []
---
# PR #281: Release PR: remove auth0 frontend support

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/pull/281  
**State:** closed | **Author:** michel-teqplay  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-09-14  
**Merged:** 2026-09-14  

## Description

_No description._

## Commits

- `087860ab` **Jamie de Leest** (2026-08-18): remove-sbom-upload
- `e1aad8a3` **Joost Dambrink** (2026-08-18): Merge pull request #278 from teqplay/remove-sbom-upload
  remove-sbom-upload
- `34638b5d` **Jamie de Leest** (2026-09-02): ci: add id-token/contents permissions for reusable workflow jobs
- `52549c05` **Michel Wilson** (2026-09-09): Merge pull request #279 from teqplay/add-reusable-workflow-permissions
  ci: add id-token/contents permissions for reusable workflow jobs
- `8e4849c0` **Michel Wilson** (2026-09-07): TCC-1138 Remove Auth0 frontend support
  Drop the auth-credentials-auth-zero (user/frontend) skeleton module and
  its auth-credentials-auth0 config block. The s2s modules and
  auth-credentials-auth0-s2s config stay: the Auth0 logs show data science
  still authenticates with machine-to-machine tokens.
  
  Also drops the README instructions for hand-extending an Auth0 user
  token, which no longer apply.
  
  Co-Authored-By: Claude <noreply@anthropic.com>
- `53e14117` **Michel Wilson** (2026-09-14): Merge pull request #280 from teqplay/TCC-1138-remove-auth0-frontend
  TCC-1138 Remove Auth0 frontend support

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-14)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-14)

### 🟡 Changes recommended

Removing Dependency-Track inputs may disable dependency scanning and SBOM publication.

*Get a fresh assessment by requesting another Copilot review.*

<details>
<summary>Pull request overview</summary>

Removes frontend Auth0 support while retaining Auth0 machine-to-machine authentication.

**Changes:**
- Removes frontend Auth0 configuration and dependency.
- Updates authentication testing documentation.
- Updates CI permissions and removes Dependency-Track inputs.
</details>

<details>
<summary>File summaries</summary>

| File | Summary |
|---|---|
| `src/main/resources/application.yml` | Removes frontend Auth0 settings. |
| `README.md` | Simplifies token instructions. |
| `build.gradle` | Removes the frontend Auth0 module. |
| `.github/workflows/main.yml` | Updates permissions and CI inputs. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 3/4 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/poma-backend/new/master?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### TeqJoostD — APPROVED (2026-09-14)

_No comment._

## Review Comments

### Copilot — 2026-09-14 on `.github/workflows/main.yml`

Removing `dependency_track: true` (and the `dt_api_key` below) opts this service out of the Dependency-Track step in the reusable workflow, while `cyclonedxBom` is still configured in `build.gradle`. Unless Dependency-Track is being intentionally retired, this silently stops dependency scanning/SBOM publication on every push and is unrelated to the Auth0 frontend removal; please retain these inputs or replace the scan with the new mechanism.

## Comments
