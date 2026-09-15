---
id: github:teqplay/dataflow_dag_core:pr:770
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 770
title: 'fix(dag): Move `PUSHBARGE` fact load after BARGE branch in `fact_transformation_dag`'
author: panjiyudasetya
state: open
date: '2026-09-15'
merged_at: null
base_branch: develop
head_branch: fix/fact-trans-flow
url: https://github.com/teqplay/dataflow_dag_core/pull/770
labels: []
linked_issues: []
explicit_links: []
---
# PR #770: fix(dag): Move `PUSHBARGE` fact load after BARGE branch in `fact_transformation_dag`

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/770  
**State:** open | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `fix/fact-trans-flow`  
**Created:** 2026-09-15  

## Description

### Description

`PUSHBARGE` records can bleed through the BARGE ingestion path via `ship.role` override in both batch (`_resolve_vessel_type`) and streaming (`resolve_vessel_type`). Running `call_fact_sof_pushbarge` before the BARGE branch meant BARGE-sourced PUSHBARGE records were not yet in ODS when the fact load ran.


### Solution
Move `call_fact_sof_pushbarge` to run sequentially after `barge_done`, before `call_fact_sof_bunker`, so all PUSHBARGE-stamped ODS data is guaranteed present.

## Commits

- `3540fd42` **Panji Y. Wiwaha** (2026-09-15): fix(dag): move PUSHBARGE fact load after BARGE branch in fact_transformation_dag
  PUSHBARGE records can bleed through the BARGE ingestion path via ship.role
  override in both batch (_resolve_vessel_type) and streaming (resolve_vessel_type).
  Running call_fact_sof_pushbarge before the BARGE branch meant BARGE-sourced
  PUSHBARGE records were not yet in ODS when the fact load ran.
  
  Move call_fact_sof_pushbarge to run sequentially after barge_done, before
  call_fact_sof_bunker, so all PUSHBARGE-stamped ODS data is guaranteed present.

## Reviews

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-15)

### 🟢 Approval recommended

The only finding is a minor documentation nit with no approval-blocking issues.

<details>
<summary>Pull request overview</summary>

Moves `PUSHBARGE` fact loading after the BARGE branch completes.

**Changes:**
- Reorders `PUSHBARGE` after `barge_done`.
- Runs BUNKER after PUSHBARGE.
- Updates orchestration comments.
</details>

<details>
<summary>File summaries</summary>

| File | Summary |
|---|---|
| `teqplay/dags/pipeline/fact_transformation_dag.py` | Adjusts DAG dependencies and documentation. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### augmentcode[bot] — COMMENTED (2026-09-15)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F770%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

### Copilot — 2026-09-15 on `teqplay/dags/pipeline/fact_transformation_dag.py`

This comment now contradicts the dependency below: `call_fact_sof_bunker` is downstream of `call_fact_sof_pushbarge` at line 195, so these tasks do not run in parallel and BUNKER waits for PUSHBARGE to complete. Please update the comment to describe the sequential ordering so the DAG's execution contract is not misread.

## Comments
