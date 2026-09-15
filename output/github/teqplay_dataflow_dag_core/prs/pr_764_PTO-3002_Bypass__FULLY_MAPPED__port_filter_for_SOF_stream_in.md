---
id: github:teqplay/dataflow_dag_core:pr:764
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 764
title: PTO-3002 Bypass `FULLY_MAPPED` port filter for SOF stream in CM environment
author: panjiyudasetya
state: closed
date: '2026-09-07'
merged_at: '2026-09-08'
base_branch: master
head_branch: PTO-3002
url: https://github.com/teqplay/dataflow_dag_core/pull/764
labels: []
linked_issues: []
explicit_links: []
---
# PR #764: PTO-3002 Bypass `FULLY_MAPPED` port filter for SOF stream in CM environment

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/764  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `PTO-3002`  
**Created:** 2026-09-07  
**Merged:** 2026-09-08  

## Description

### Description

- SOF stream UPDATE messages are currently dropped at the RabbitMQ consumer stage for ports whose `expected_mapping_status` is not `FULLY_MAPPED`. This is intentional for production to avoid ingesting incomplete data.
- In the CM (Airflow data) environment, operators need to observe SOF data even for ports that are not yet fully mapped. The filter was preventing this.
- Added an early return in `_filter_by_fully_mapped_status` that skips the filter entirely when `ETL_ENV=CM`, allowing all `UPDATE` messages through to staging and the full ODS → fact pipeline.

### Behaviour

| Environment | Ports not FULLY_MAPPED |
|---|---|
| `LIVE` | Dropped (unchanged) |
| `DEV` | Dropped (unchanged) |
| `LOCAL` | Dropped (unchanged) |
| `CM` | **Persisted** (new) |

`ETL_ENV` is already case-insensitive via `get_env()` (calls `.upper()`), so `cm`, `CM`, and `Cm` all resolve correctly.

### Notes

- DELETE messages are unaffected — they always pass through in all environments.
- No schema or DAG changes; the downstream ODS and fact stream pipelines handle the records normally.

## Commits

- `a6268046` **Panji Y. Wiwaha** (2026-09-07): feat: allow SOF stream to persist data for unmapped ports in CM environment
  In the CM (Airflow data) environment, bypass the FULLY_MAPPED port filter
  so that SOF UPDATE messages are persisted to staging regardless of port
  mapping status. All other environments (LIVE, DEV, LOCAL) continue to
  enforce the filter as before.
  
  ETL_ENV is already case-insensitive via get_env() .upper().

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-07)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-07)

### 🟢 Approval recommended

The behavior change is narrowly scoped to CM via an explicit environment check and preserves existing filtering in other environments.

<details>
<summary>Pull request overview</summary>

Updates the SOF RabbitMQ consumer’s port-mapping filter behavior so the CM environment can ingest SOF UPDATE traffic even when a port is not `FULLY_MAPPED`, while preserving the existing “drop if not fully mapped” behavior for LIVE/DEV/LOCAL.

**Changes:**
- Add a CM-specific early return in `_filter_by_fully_mapped_status()` to bypass the `FULLY_MAPPED` UNLOCODE filter.
- Move `PortMappingStatusCache` / `find_unlocode_in_message` imports to module scope and add `teqplay.settings.base` import for environment detection.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| teqplay/services/streaming/rabbitmq/sof/base.py | Skips the FULLY_MAPPED port filter when `ETL_ENV` resolves to `CM`, allowing CM to ingest all UPDATE-like SOF messages. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/master?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — COMMENTED (2026-09-08)

_No comment._

### ryan-kharisma — APPROVED (2026-09-08)

LGTM

## Review Comments

### Copilot — 2026-09-07 on `teqplay/services/streaming/rabbitmq/sof/base.py`

Log message says "UPDATE" messages, but this path can also include CREATE actions (see _separate_by_action docstring: barge treats CREATE as UPDATE). Adjust wording to avoid misleading ops/debugging in CM.

### panjiyudasetya — 2026-09-08 on `teqplay/services/streaming/rabbitmq/sof/base.py`

Not really. We only have a concern to the update message.

## Comments
