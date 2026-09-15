---
id: github:teqplay/dataflow_dag_core:pr:767
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 767
title: 'fix(sql): Remove `psycopg2` placeholders from SQL comments to prevent `KeyError`
  in streaming mode'
author: panjiyudasetya
state: closed
date: '2026-09-11'
merged_at: '2026-09-11'
base_branch: develop
head_branch: fix/tug-bunker-sof-issues
url: https://github.com/teqplay/dataflow_dag_core/pull/767
labels: []
linked_issues: []
explicit_links: []
---
# PR #767: fix(sql): Remove `psycopg2` placeholders from SQL comments to prevent `KeyError` in streaming mode

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/767  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `fix/tug-bunker-sof-issues`  
**Created:** 2026-09-11  
**Merged:** 2026-09-11  

## Description

### Problem

TUG/BUNKER streaming tasks (`tug_update.load_fact_terminal_visit.prepare_base_data` and the equivalent berth visit task) were failing with:

```
KeyError: 'start'
```

`psycopg2` performs `%(key)s` substitution on the entire SQL string — including comment lines. Two SQL templates contained `%(start)s` inside `--` comments that are rendered for TUG/BUNKER in streaming mode:

- `fact/terminal_visit/prepare_base_terminal_visit.sql`
- `fact/berth_visit/prepare_base_berth_visit.sql`

The streaming `sql_params` dict only carries `is_streaming_data`, `entry_ids`, and `prefix_temp_table` — no `start` or `end` — so psycopg2 raised `KeyError: 'start'` when it encountered the placeholder in the comment.

### Changes

- **Bug fix**: Rewrote the two offending comments to plain prose (no psycopg2-style placeholders).
- **Style cleanup**: Lowercased `ANY(...)` → `any(...)` across several SQL files to match the project SQL standard (all keywords lowercase except reserved words).
- **Comment cleanup**: Replaced `%(key)s`-style references in parameter doc-comments with plain text so they can never be misinterpreted as live placeholders.

### Files changed

| File | Change |
|---|---|
| `fact/terminal_visit/prepare_base_terminal_visit.sql` | Remove `%(start)s` from streaming-mode comment (bug fix) |
| `fact/berth_visit/prepare_base_berth_visit.sql` | Same fix |
| `vessel_operational_queue/mark_completed.sql` | `ANY` → `any`, doc-comment cleanup |
| `vessel_operational_queue/reset_to_pending.sql` | `ANY` → `any`, doc-comment cleanup |
| `vessel_operational_queue/poll_pending_vessel_operational.sql` | Doc-comment cleanup |
| `staging/sof/hard_delete_queue_aware.sql` | Doc-comment cleanup |
| `fact/pilot/proceed_delta.sql` | `ANY` → `any` |
| `fact/port_performance_analytics/update_port_visit_outlier_flags.sql` | `ANY` → `any`, doc-comment cleanup |

## Commits

- `61161adb` **Panji Y. Wiwaha** (2026-09-11): fix(sql): remove psycopg2 placeholders from comments and normalise ANY to any
  %(start)s and %(end)s inside SQL comments caused KeyError in streaming mode
  because psycopg2 substitutes %(key)s patterns even inside comment lines.
  Rewrote those comments to plain prose. Also lowercased ANY to any and
  cleaned up parameter doc-comments to plain text (not %(key)s style).

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-11)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-11)

### 🟢 Approval recommended

No unresolved review issues were identified.

<details>
<summary>Pull request overview</summary>

Fixes streaming-mode `KeyError` failures caused by psycopg2 placeholders in SQL comments and applies SQL style cleanup.

**Changes:**
- Removed placeholder syntax from affected comments.
- Lowercased selected `ANY(...)` expressions.
- Cleaned parameter documentation comments.
</details>

<details>
<summary>File summaries</summary>

| File | Summary |
|---|---|
| `teqplay/templates/sql/dml/vessel_operational_queue/reset_to_pending.sql` | Cleaned comments and normalized `any`. |
| `teqplay/templates/sql/dml/vessel_operational_queue/poll_pending_vessel_operational.sql` | Cleaned parameter documentation. |
| `teqplay/templates/sql/dml/vessel_operational_queue/mark_completed.sql` | Cleaned comments and normalized `any`. |
| `teqplay/templates/sql/dml/staging/sof/hard_delete_queue_aware.sql` | Cleaned parameter documentation. |
| `teqplay/templates/sql/dml/fact/terminal_visit/prepare_base_terminal_visit.sql` | Removed the streaming comment placeholder. |
| `teqplay/templates/sql/dml/fact/port_performance_analytics/update_port_visit_outlier_flags.sql` | Cleaned comments and normalized `any`. |
| `teqplay/templates/sql/dml/fact/pilot/proceed_delta.sql` | Normalized `any`. |
| `teqplay/templates/sql/dml/fact/berth_visit/prepare_base_berth_visit.sql` | Removed the streaming comment placeholder. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 8/8 changed files
- **Comments generated:** 0
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### ryan-kharisma — APPROVED (2026-09-11)

LGTM

## Comments
