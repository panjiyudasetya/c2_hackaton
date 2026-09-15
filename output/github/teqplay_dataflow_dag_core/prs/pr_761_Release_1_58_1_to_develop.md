---
id: github:teqplay/dataflow_dag_core:pr:761
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 761
title: Release 1.58.1 to develop
author: panjiyudasetya
state: closed
date: '2026-09-07'
merged_at: '2026-09-07'
base_branch: develop
head_branch: hotfix/1.58.1
url: https://github.com/teqplay/dataflow_dag_core/pull/761
labels: []
linked_issues: []
explicit_links: []
---
# PR #761: Release 1.58.1 to develop

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/761  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `hotfix/1.58.1`  
**Created:** 2026-09-07  
**Merged:** 2026-09-07  

## Description


## [1.58.1] - 2026-09-07
### Fixed
- Fix RabbitMQ connection resets on `staging_sof` stream DAGs (#758)

## Commits

- `40343ec3` **Panji Y. Wiwaha** (2026-08-03): Merge pull request #732 from teqplay/hotfix/1.54.1
  Release 1.54.1 to master
- `b78340c2` **Ryan Kharisma Rakhmat** (2026-08-10): Merge pull request #737 from teqplay/release/1.55.0
  Release 1.55.0 to master
- `e0ae1c6e` **Panji Y. Wiwaha** (2026-08-21): Merge pull request #744 from teqplay/release/1.56.0
  Release 1.56.0 to master
- `fdf1e2f8` **Panji Y. Wiwaha** (2026-08-27): Merge pull request #748 from teqplay/release/1.57.0
  Release 1.57.0 to master
- `cbcbad49` **Ryan Kharisma Rakhmat** (2026-09-04): Merge pull request #756 from teqplay/release/1.58.0
  Release 1.58.0 to master
- `ffd77860` **Panji Y. Wiwaha** (2026-09-04): fix: guard rollback() against closed channel on connection reset
  When the RabbitMQ broker resets the TCP connection mid-commit, the
  channel is already closed by the time the except block calls
  ack_handler.rollback(). The subsequent basic_nack() raises
  ChannelWrongStateError, masking the real StreamLostError and making
  the failure harder to diagnose.
  
  Guard rollback() with channel.is_closed — when the connection is
  already gone, RabbitMQ automatically requeues unacknowledged messages,
  so no explicit NACK is needed.
- `9eed678d` **Panji Y. Wiwaha** (2026-09-04): fix: guard rollback() against closed channel on connection reset
  When the RabbitMQ broker resets the TCP connection mid-commit, the
  channel is already closed by the time the except block calls
  ack_handler.rollback(). The subsequent basic_nack() raises
  ChannelWrongStateError, masking the real StreamLostError and making
  the failure harder to diagnose.
  
  Make rollback() best-effort: wrap basic_nack() in a try/except and log
  any pika error without re-raising. This covers both the CLOSED and
  CLOSING channel states, and eliminates the TOCTOU race between an
  is_closed check and the nack call. When the connection is already gone,
  RabbitMQ automatically requeues unacknowledged messages on disconnect,
  so no messages are lost.
- `1a736ac6` **Panji Y. Wiwaha** (2026-09-07): fix: set heartbeat=300s on RabbitMQ connections to prevent broker timeout
  Pika's BlockingConnection stops processing events (including sending
  heartbeats) while the code is blocked in DB persistence after consuming
  messages. With the broker's default 60s heartbeat, any persistence run
  exceeding 120s causes a TCP reset from the broker side.
  
  Set heartbeat=300s on all pika ConnectionParameters so the broker allows
  up to 600s of silence before closing the connection. This covers worst-case
  lock contention during concurrent staging_sof upserts.
- `289da008` **Panji Y. Wiwaha** (2026-09-07): fix: reduce max_active_runs from 3 to 2 for staging_sof stream DAGs
  Three concurrent instances allow all three to finish consuming at the
  same time and simultaneously upsert into staging_sof, causing lock
  contention that extends DB persistence well beyond the heartbeat timeout.
  
  Two concurrent instances maintain the intended overlap (second instance
  starts before the first finishes) while eliminating the worst-case
  three-way lock collision. Updated the docstring to match the actual value.
- `b99170b5` **Panji Y. Wiwaha** (2026-09-07): revert: remove ineffective heartbeat=300 from pika ConnectionParameters
  RabbitMQ negotiates heartbeat to min(client, broker). With the broker's
  60s default, requesting 300 still produces a 60s heartbeat — the change
  provided no additional tolerance window.
  
  A true heartbeat increase requires raising heartbeat_timeout in the
  Amazon MQ broker configuration. The primary mitigations for the DB
  persistence timeout are the max_active_runs=2 reduction (eliminates
  3-way upsert lock collision) and reducing RABBITMQ_BARGE_MSG_COUNT to
  500 via Lens (reduces transaction hold time).
- `457635df` **Panji Y. Wiwaha** (2026-09-07): Merge pull request #758 from teqplay/PTO-2990
  PTO-2990 Resolve RabbitMQ connection resets on `staging_sof` stream DAGs
- `bba36fd8` **Panji Y. Wiwaha** (2026-09-07): Bump version 1.58.1

## Reviews

### ryan-kharisma — APPROVED (2026-09-07)

LGTM

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-07)

### 🟢 Approval recommended

The changes are small, targeted, and align with the stated root cause/mitigation, with only a minor docstring accuracy nit to address.

<details>
<summary>Pull request overview</summary>

This PR prepares the `develop` branch for release **1.58.1**, incorporating the fix from #758 to reduce RabbitMQ stream DAG failures caused by broker-side connection resets and to ensure the original exception is not masked during rollback.

**Changes:**
- Make `DeferredAckHandler.rollback()` best-effort by suppressing NACK failures so rollback exceptions don’t mask the original error.
- Reduce concurrency for `staging_sof` stream DAGs by setting `max_active_runs=2` (down from 3) for both barge and sea vessel consumers.
- Bump package version to `1.58.1` and add the corresponding changelog entry.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `teqplay/services/streaming/rabbitmq/handlers.py` | Makes rollback NACK best-effort to avoid secondary exceptions masking the root failure. |
| `teqplay/dags/streaming/staging_sof/sea_vessel_stream_dag.py` | Lowers stream DAG concurrency via `max_active_runs=2` and updates the docstring accordingly. |
| `teqplay/dags/streaming/staging_sof/barge_stream_dag.py` | Lowers stream DAG concurrency via `max_active_runs=2` and updates the docstring accordingly. |
| `teqplay/__init__.py` | Bumps `__version__` to `1.58.1`. |
| `CHANGELOG.md` | Adds the `1.58.1` release notes entry describing the fix. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 5/5 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/develop?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### augmentcode[bot] — COMMENTED (2026-09-07)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

### Copilot — 2026-09-07 on `teqplay/services/streaming/rabbitmq/handlers.py`

Docstring says only pika errors are suppressed, but the implementation catches any Exception. Either narrow the except clause to pika-specific exceptions, or update the docstring to match the actual behavior.

## Comments
