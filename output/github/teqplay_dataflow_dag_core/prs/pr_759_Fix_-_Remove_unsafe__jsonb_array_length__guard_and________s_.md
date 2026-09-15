---
id: github:teqplay/dataflow_dag_core:pr:759
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 759
title: Fix - Remove unsafe `jsonb_array_length` guard and `%(...)s` patterns from
  SQL comments
author: panjiyudasetya
state: closed
date: '2026-09-04'
merged_at: '2026-09-04'
base_branch: develop
head_branch: fix/streaming-transformation-issues
url: https://github.com/teqplay/dataflow_dag_core/pull/759
labels: []
linked_issues: []
explicit_links: []
---
# PR #759: Fix - Remove unsafe `jsonb_array_length` guard and `%(...)s` patterns from SQL comments

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/759  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `fix/streaming-transformation-issues`  
**Created:** 2026-09-04  
**Merged:** 2026-09-04  

## Description

### Summary

Two production bugs found in the ODS SOF stream pipeline:

- **`ods_sof__stream` task failures** (`ingest_ods_slow_moving_periods` and other ODS loaders):
  `InvalidParameterValue: cannot get array length of a non-array` — PostgreSQL's query planner does not guarantee predicate evaluation order in a WHERE clause, so `jsonb_array_length(col)` was being called on non-array JSONB values before the `jsonb_typeof(col) = 'array'` guard filtered them out.

- **Rollback failure** after any task failure (`Rollback failed for SEA_VESSEL: syntax error`):
  psycopg2 scans the entire SQL string for `%(key)s` placeholders, including inside `--` comment blocks. When the key was absent from the params dict, psycopg2 raised `KeyError`, masking the real failure cause and corrupting the rollback note passed to `sof_update_state`.

### Changes

#### Fix 1 — Remove redundant `jsonb_array_length` guards (10 ODS DML files)

`jsonb_typeof(col) = 'array'` is sufficient. An empty JSON array already produces zero rows through `jsonb_array_elements`, making the `AND jsonb_array_length(col) > 0` check both redundant and unsafe. Removed from all ODS `stg_to_ods.sql` loaders: `slow_moving_period`, `tug_event`, `terminal_visit`, `berth_visit`, `unclassified_stop`, `encounter`, `anchor_stop`, `lock_stop`, `visited_approach_area`, `ship_to_ship_transfers`.

#### Fix 2 — Remove `%(key)s` from SQL comment blocks (10 processing_queue templates)

Replaced `%(key)s` parameter doc notation in comment blocks with plain `key:` text across all processing_queue SQL files. The actual SQL bodies are unchanged — only the comment header docs are affected.

### Test plan

- [ ] Redeploy `ods_sof__stream` and confirm `ingest_ods_slow_moving_periods` no longer
  fails with `InvalidParameterValue`
- [ ] Trigger a deliberate ODS task failure and confirm rollback succeeds without secondary
  `syntax error` log entry
- [ ] Verify all other ODS stream tasks (`berth_visit`, `terminal_visit`, `tug_event`, etc.)
  continue to process correctly

## Commits

- `c9bfdb18` **Panji Y. Wiwaha** (2026-09-04): fix(ods-dml): remove redundant jsonb_array_length guard from all ODS stg_to_ods loaders
  jsonb_typeof(col) = 'array' is sufficient to ensure col is a JSON array.
  The additional AND jsonb_array_length(col) > 0 is redundant — an empty
  array produces zero rows through jsonb_array_elements regardless — and
  unsafe because PostgreSQL's planner does not guarantee predicate evaluation
  order, so jsonb_array_length can be invoked on a non-array value before
  the jsonb_typeof guard filters it out.
  
  This caused InvalidParameterValue: cannot get array length of a non-array
  on the ingest_ods_slow_moving_periods task in the ods_sof__stream DAG.
  The same pattern was present in 9 other ODS loaders and is fixed here too.
- `1c626760` **Panji Y. Wiwaha** (2026-09-04): fix(sql): remove %(...)s placeholders from SQL comment blocks in processing_queue templates
  psycopg2 scans the entire SQL string for %(key)s placeholders, including
  inside -- comments. When the substitution key is present in the params dict,
  psycopg2 embeds the quoted value into the comment, which is harmless but
  unintended. When the key is absent, psycopg2 raises KeyError, masking the
  real cause of the failure and corrupting the rollback note.
  
  Removed %(key)s from all comment-block parameter docs in processing_queue
  SQL files. The actual SQL bodies retain %(key)s for correct psycopg2
  parameterisation.
  
  sof_update_state.sql also fixed to prevent the secondary rollback failure
  seen when note values contain psycopg2-sensitive characters.
- `e498d6ee` **Panji Y. Wiwaha** (2026-09-04): fix(sql): correct slow_moving_periods jsonb_typeof guard and update vessel_type docs
  - slow_moving_period/stg_to_ods.sql: change jsonb_typeof guard from 'array'
    to 'object' — slow_moving_periods is a JSON object (Dict) keyed by
    arrival/inPort/departure, not a JSON array. The 'array' check was
    incorrectly filtering every valid payload.
  
  - processing_queue SQL files: update vessel_type parameter documentation
    from 'SEA_VESSEL' or 'BARGE' to include 'TUG' and 'BUNKER', which are
    now valid callers of the SOF processing queue workflow.
    Affected: sof_update_state, sof_fetch_ods_completed,
    sof_fetch_pending_delete, sof_fetch_pending_update,
    sof_mark_stale_deletes, sof_mark_stale_updates.

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F759%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-04)

### 🟡 Changes recommended

One of the updated ODS loaders (`slow_moving_period/stg_to_ods.sql`) has a JSON type guard that appears inconsistent with how the JSON is subsequently accessed, risking silently dropping data after removing the failing predicate.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

This PR addresses two production failure modes in the SOF ODS stream pipeline by (1) removing unsafe `jsonb_array_length(...)` predicates that can be evaluated before their type guards, and (2) removing `%(...)s` placeholder-like patterns from SQL comment blocks to prevent psycopg2 placeholder parsing from breaking rollbacks.

**Changes:**
- Removed redundant/unsafe `jsonb_array_length(...) > 0` checks from ODS `stg_to_ods.sql` loaders that expand JSON arrays.
- Updated `processing_queue` SQL template header comments to document parameters without `%(key)s` patterns (avoids psycopg2 scanning comment blocks as placeholders).
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| teqplay/templates/sql/dml/processing_queue/sof_validate_metadata.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_update_state.sql | Removes `%(...)s` patterns from parameter doc comments (rollback-safety). |
| teqplay/templates/sql/dml/processing_queue/sof_mark_stale_updates.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_mark_stale_deletes.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_increment_recovery_attempts.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_fetch_pending_update.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_fetch_pending_delete.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_fetch_ods_completed.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_fetch_deferred.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/processing_queue/sof_extract_missing_metadata.sql | Removes `%(...)s` patterns from parameter doc comments. |
| teqplay/templates/sql/dml/ods/visited_approach_area/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
| teqplay/templates/sql/dml/ods/unclassified_stop/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
| teqplay/templates/sql/dml/ods/tug_event/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guards on berth visits + tug arrays. |
| teqplay/templates/sql/dml/ods/terminal_visit/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
| teqplay/templates/sql/dml/ods/slow_moving_period/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check (needs follow-up; see comment). |
| teqplay/templates/sql/dml/ods/ship_to_ship_transfers/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
| teqplay/templates/sql/dml/ods/lock_stop/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
| teqplay/templates/sql/dml/ods/encounter/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
| teqplay/templates/sql/dml/ods/berth_visit/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
| teqplay/templates/sql/dml/ods/anchor_stop/stg_to_ods.sql | Removes unsafe `jsonb_array_length` guard while keeping type check. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 20/20 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-09-04)

LGTM

## Review Comments

### Copilot — 2026-09-04 on `teqplay/templates/sql/dml/ods/slow_moving_period/stg_to_ods.sql`

`sof.slow_moving_periods` is subsequently treated like a JSON object (extracted via `-> 'arrival'`, `-> 'inPort'`, `-> 'departure'`). Filtering it to `jsonb_typeof(...) = 'array'` will exclude the object-shaped payload that this query appears to expect (and will also yield NULL for those extracted fields if an array slips through), potentially resulting in silently missing ODS rows after this change stops raising an exception. Consider aligning the type guard with the object-shaped access pattern here (or normalizing both shapes explicitly).

### panjiyudasetya — 2026-09-04 on `teqplay/templates/sql/dml/ods/slow_moving_period/stg_to_ods.sql`

Resolved by e498d6e

### panjiyudasetya — 2026-09-04 on `teqplay/templates/sql/dml/ods/slow_moving_period/stg_to_ods.sql`

Resolved e498d6e

## Comments

### panjiyudasetya — 2026-09-04

augment review

### panjiyudasetya — 2026-09-04

All green now on my local
<img width="2672" height="1459" alt="image" src="https://github.com/user-attachments/assets/fb0c8d75-f839-44de-b6a5-d041ebe301db" />
