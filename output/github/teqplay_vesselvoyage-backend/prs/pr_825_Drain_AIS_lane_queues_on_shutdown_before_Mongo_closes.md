---
id: github:teqplay/vesselvoyage-backend:pr:825
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 825
title: Drain AIS lane queues on shutdown before Mongo closes
author: Darius-Wattimena
state: closed
date: '2026-07-21'
merged_at: '2026-07-23'
base_branch: develop
head_branch: fix/shutdown-drain-ais-lanes
url: https://github.com/teqplay/vesselvoyage-backend/pull/825
labels: []
linked_issues: []
explicit_links: []
---
# PR #825: Drain AIS lane queues on shutdown before Mongo closes

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/825  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `fix/shutdown-drain-ais-lanes`  
**Created:** 2026-07-21  
**Merged:** 2026-07-23  

## Description

## Problem
On shutdown, `RabbitMqConsumersService.shutdown()` only closed the RabbitMQ channels. `RabbitMqAisConsumerService` acks each AIS message as soon as it is routed into a lane queue (fire-and-forget, up to 1000 in flight), and the lane workers kept flushing those already-acked items to Mongo while Spring destroyed the Mongo client bean — failing with `MongoServerUnavailableException` and silently losing the items, since RabbitMQ won't redeliver acked messages.

## Fix
`ProcessingService.onClose()` runs on `ContextClosedEvent`, which fires **before** bean destruction, so Mongo is still available at that point. `RabbitMqConsumersService.shutdown()` now:
1. Closes the channels first (no new deliveries)
2. Then calls the new `RabbitMqAisConsumerService.shutdown()`, which drains the remaining lane items to Mongo, bounded by a 30s timeout before forcing termination

The drain loop uses a timed `poll` instead of a blocking `take` so lane workers exit once shutdown starts and their lane is empty. Late deliveries arriving mid-shutdown are dropped instead of blocking on lanes no longer being drained — they are unacked (the channel is closing), so RabbitMQ redelivers them on restart.

## Not fixed here
The `AlreadyClosedException` on `basicAck` during shutdown comes from skeleton's `RabbitMqEventHandler`: `closeChannel()` doesn't cancel the consumer or wait for in-flight `handleDelivery` calls. Harmless (unacked messages are redelivered), but silencing it needs a graceful cancel in the skeleton library.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Commits

- `74c51741` **Darius Wattimena** (2026-07-21): Drain AIS lane queues on shutdown before Mongo closes
  Messages routed to a lane are acked immediately, but on shutdown the
  lane workers kept flushing to Mongo while Spring destroyed the Mongo
  client, failing with MongoServerUnavailableException and losing the
  already-acked in-flight items (up to 1000).
  
  RabbitMqConsumersService.shutdown() now closes the channels first (no
  new deliveries) and then drains the lane queues while Mongo is still
  open, bounded by a 30s timeout. Late deliveries during shutdown are
  dropped instead of blocking on lanes no longer being drained.
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
- `d6dc5bab` **Darius Wattimena** (2026-07-21): Address review feedback on shutdown drain
  - Split drainLane into awaitNextBatch and flushBatchLogged to reduce
    cognitive complexity
  - Propagate InterruptedException out of the flush catch blocks so a
    forced shutdown (shutdownNow) can stop lane workers promptly
  - Handle InterruptedException from awaitTermination so the forced-stop
    path still runs
  - Run the lane drain in a finally block so a failure while closing a
    consumer can't skip it
  
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-21)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F825%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### TeqJoostD — APPROVED (2026-07-22)

_No comment._

## Review Comments

## Comments
