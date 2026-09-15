---
id: github:teqplay/dataflow_dag_core:pr:758
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 758
title: PTO-2990 Resolve RabbitMQ connection resets on `staging_sof` stream DAGs
author: panjiyudasetya
state: closed
date: '2026-09-04'
merged_at: '2026-09-07'
base_branch: master
head_branch: PTO-2990
url: https://github.com/teqplay/dataflow_dag_core/pull/758
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2990
---
# PR #758: PTO-2990 Resolve RabbitMQ connection resets on `staging_sof` stream DAGs

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/758  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `PTO-2990`  
**Created:** 2026-09-04  
**Merged:** 2026-09-07  

## Description

### Problem

The DAGs `staging_sof__barge_stream` and `staging_sof__sea_vessel_stream` failed 11 times on 2026-09-03 due to RabbitMQ TCP resets, producing a misleading `ChannelWrongStateError: Channel is closed` in Airflow task logs that obscured the real failure.

### Root Cause

Pika's `BlockingConnection` stops sending heartbeats while blocked in DB persistence (between `channel.consume()` exit and `basic_ack()`). With the broker's default 60s heartbeat, the broker kills any connection silent for >120s.

Three concurrent DAG instances each consuming up to 1,500 messages and simultaneously upserting into `staging_sof` caused lock contention that extended DB persistence well beyond 120s. RabbitMQ broker logs confirmed 91 `missed heartbeats from client, timeout: 60s` events on 2026-09-03, 71 of which had a connection duration of exactly 3 minutes, the precise fingerprint of: ~30s consuming + 120s broker tolerance = connection killed at ~3 minutes.

The visible `ChannelWrongStateError` was a secondary exception: `rollback()` attempted `basic_nack()` on the already-dead channel inside the `except` block, replacing the real `StreamLostError` in Airflow logs.

### Changes

#### `teqplay/services/streaming/rabbitmq/handlers.py`
- Wrapped `basic_nack()` in `try/except` inside `rollback()`, makes it best-effort so a dead channel on rollback no longer raises a secondary exception that masks the original failure. When the connection is already gone, RabbitMQ requeues unacknowledged messages automatically.

#### `teqplay/dags/streaming/staging_sof/*_stream_dag.py`
- Reduced `max_active_runs` from 3 to 2. Three concurrent instances allowed all three to finish consuming simultaneously and collide on `staging_sof` upserts. Two instances maintain the intended overlap for continuous queue draining while eliminating the worst-case three-way lock collision. Updated the docstring to match.

### Out of Scope
- **Heartbeat timeout**; A client-side `heartbeat` parameter cannot override the broker's 60s
value where RabbitMQ negotiates to `min(client, broker)`. A genuine increase requires raising `heartbeat_timeout` in the Amazon MQ broker configuration. The `max_active_runs=2` reduction and the `number_of_messages` change below are the code-level mitigations.
- `RABBITMQ_BARGE_MSG_COUNT` is set to 1,500 in the staging environment (confirmed via broker crash dumps showing `{1500}` prefetch count). Reducing it to 500 (the code default) is tracked separately and must be applied via Lens.
- Git-sync sidecars on the EKS worker, scheduler, and triggerer pods are crashing due to a GitHub port 443 connectivity issue that started 2026-08-09. This is a separate infrastructure issue but must be resolved before this branch can deploy.

### Test Plan

- [ ] Confirm `ChannelWrongStateError` no longer appears in task logs on connection reset, `StreamLostError` should be the reported failure
- [ ] Confirm no more than 2 concurrent active runs for both DAGs in the Airflow UI
- [ ] Monitor broker logs for `missed heartbeats` events after deploy; frequency should drop significantly with `max_active_runs=2`
- [ ] Verify `RABBITMQ_BARGE_MSG_COUNT` staging env var via Lens and reduce to 500 if set higher

## Commits

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

## Reviews

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F758%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### copilot-pull-request-reviewer[bot] — COMMENTED (2026-09-04)

### 🟡 Changes recommended

`rollback()` can still raise and mask the original exception if the channel closes between the `is_closed` check and `basic_nack()`, so rollback should be best-effort and not throw secondary errors.

*Once you've addressed the issues Copilot identified, you can request another Copilot review.*

<details>
<summary>Pull request overview</summary>

This PR updates the RabbitMQ streaming deferred-acknowledgement helper to prevent `DeferredAckHandler.rollback()` from raising `ChannelWrongStateError` after a broker-side connection reset, which previously masked the root `StreamLostError` in Airflow logs.

**Changes:**
- Guarded `rollback()` with a `channel.is_closed` check to avoid calling `basic_nack()` on a closed channel.
- Fixed rollback ordering by capturing `max_tag`/`count` before clearing `_pending_tags`.
- Added warning log path when rollback is skipped because the channel is already closed.
</details>

<details>
<summary>File summaries</summary>

| File | Description |
| ---- | ----------- |
| `teqplay/services/streaming/rabbitmq/handlers.py` | Makes rollback resilient to already-closed RabbitMQ channels so the original connection-reset error remains visible. |
</details>

<details>
<summary>Review details</summary>

- **Files reviewed:** 1/1 changed files
- **Comments generated:** 1
- **Review effort level:** Lite
</details>

---

💡 <a href="/teqplay/dataflow_dag_core/new/master?filename=.github/skills/code-review/SKILL.md" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Add a `code-review` agent skill</a> or configure MCP servers for context-aware, tailored reviews. <a href="https://docs.github.com/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review?tool=webui#mcp-servers-and-agent-skills" class="Link--inTextBlock" target="_blank" rel="noopener noreferrer">Learn more in the docs.</a>

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### panjiyudasetya — COMMENTED (2026-09-04)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-04)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### augmentcode[bot] — COMMENTED (2026-09-07)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F758%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-07)

_No comment._

### augmentcode[bot] — COMMENTED (2026-09-07)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F758%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-09-07)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-07)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-07)

_No comment._

### ryan-kharisma — COMMENTED (2026-09-07)

_No comment._

### ryan-kharisma — APPROVED (2026-09-07)

LGTM

### panjiyudasetya — COMMENTED (2026-09-07)

_No comment._

## Review Comments

### Copilot — 2026-09-04 on `teqplay/services/streaming/rabbitmq/handlers.py`

`rollback()` can still mask the original exception if the channel closes (or the TCP connection drops) after the `is_closed` check but before/during `basic_nack()`. Since `rollback()` is called from an `except` block, it should be best-effort and avoid raising secondary exceptions that replace the real failure in logs.

### panjiyudasetya — 2026-09-04 on `teqplay/services/streaming/rabbitmq/handlers.py`

Resolved by 9eed678

### panjiyudasetya — 2026-09-04 on `teqplay/services/streaming/rabbitmq/handlers.py`

Resolved by 9eed678

### panjiyudasetya — 2026-09-07 on `teqplay/services/streaming/rabbitmq/base.py`

Resolved by 7600a57

### panjiyudasetya — 2026-09-07 on `teqplay/dags/streaming/staging_sof/barge_stream_dag.py`

the "claimed 600-second heartbeat" doesn't exist in the code or docstrings; the residual risk is acknowledged and tracked as an infra action.

### ryan-kharisma — 2026-09-07 on `teqplay/services/streaming/rabbitmq/handlers.py`

I think this comments needs to delete too.

### ryan-kharisma — 2026-09-07 on `teqplay/services/streaming/rabbitmq/handlers.py`

line 88 and 89 I mean

### ryan-kharisma — 2026-09-07 on `teqplay/services/streaming/rabbitmq/handlers.py`

ok my bad. I thought it is deleted.

### panjiyudasetya — 2026-09-07 on `teqplay/services/streaming/rabbitmq/handlers.py`

We still enable `requeue=True`. The only difference is that we wrap the NACK process in a try-catch block, so we can get better insight into what actually happens when an error occurs.

## Comments

### panjiyudasetya — 2026-09-04

augment review

### panjiyudasetya — 2026-09-07

augment review

### panjiyudasetya — 2026-09-07

augment review
