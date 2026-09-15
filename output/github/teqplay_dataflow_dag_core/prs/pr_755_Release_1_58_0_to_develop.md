---
id: github:teqplay/dataflow_dag_core:pr:755
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 755
title: Release 1.58.0 to develop
author: ryan-kharisma
state: closed
date: '2026-09-04'
merged_at: '2026-09-04'
base_branch: develop
head_branch: release/1.58.0
url: https://github.com/teqplay/dataflow_dag_core/pull/755
labels: []
linked_issues: []
explicit_links: []
---
# PR #755: Release 1.58.0 to develop

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/755  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `develop` ← `release/1.58.0`  
**Created:** 2026-09-04  
**Merged:** 2026-09-04  

## Description


## [1.58.0] - 2026-09-04
### Added
- ID-token content permissions for reusable workflow jobs (#753)
- Tug Bunker Vessel Types additional support (#752)
- All Average and All StdDev value for Fact Performance Analytics (#751)

### Changed
- Eliminate deadlocks on other fact tables fia lock ordering, pool and retries (#750)
- Eliminate deadlocks on fact performance analytics (#749)


## Commits

- `5f3252bc` **ryan_at_teqplay** (2026-09-04): Bump version 1.58.0
- `610801e8` **ryan_at_teqplay** (2026-09-04): fix typo

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F755%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-04)

### 🟡 Changes recommended

The 1.58.0 changelog entry contains a verified typo (“fia” → “via”) that should be corrected before release.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

Bumps the package version to 1.58.0 and records the 1.58.0 release notes in the project changelog.

**Changes:**
- Update `teqplay.__version__` to `1.58.0`.
- Add a new `1.58.0` section to `CHANGELOG.md` summarizing included PRs/features.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `teqplay/__init__.py` | Version bump to 1.58.0. |
| `CHANGELOG.md` | Add 1.58.0 release notes entry. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 2/2 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — DISMISSED (2026-09-04)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-04)

_No comment._

### panjiyudasetya — APPROVED (2026-09-04)

_No comment._

## Review Comments

### Copilot — 2026-09-04 on `CHANGELOG.md`

Typo in changelog entry: "fia" should be "via".

### ryan-kharisma — 2026-09-04 on `CHANGELOG.md`

I'm just doing typo. please ignoreit 

## Comments
