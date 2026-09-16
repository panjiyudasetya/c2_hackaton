---
id: confluence:988479489
source: confluence
type: page
space: TC
title: Nats to Rabbitmq migration plan
author: Jamie de Leest
date: '2025-11-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/988479489
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/988479489
---
# Nats to Rabbitmq migration plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/988479489  

## Content

This document presents a migration plan for consolidating our messaging infrastructure by moving from the current setup, which uses both NATS and RabbitMQ, to a single RabbitMQ-based solution. The goal of this migration is to simplify system architecture, reduce operational complexity, and centralize message handling while ensuring reliability, scalability, and minimal disruption to existing services. This plan outlines the steps, considerations, and best practices for a controlled transition from a dual-messaging system to a unified RabbitMQ environment.

---

21falsenonelisttrue

---

# **Migration of Components**

The migration will involve transitioning each NATS feature to the most appropriate target in the new architecture:

* **NATS Streams → RabbitMQ**: All existing NATS streaming topics will be migrated to RabbitMQ queues. This will centralize message streaming and ensure durability and reliability are maintained through RabbitMQ’s persistent queues and acknowledgements.
* **NATS Key-Value (KV) → Redis**: NATS KV stores will be replaced with Redis. Redis provides a high-performance, in-memory key-value store suitable for the use cases currently served by NATS KV, including caching and state management.
* **NATS Request/Reply → RabbitMQ RPC**: Existing request/reply patterns in NATS will be migrated to RabbitMQ using RPC mechanisms. This allows synchronous communication between services while leveraging RabbitMQ’s routing and delivery guarantees.

Each migration path is chosen to align with the intended use case of the original NATS feature, while standardizing on RabbitMQ and Redis for messaging and state management.

## **Migrating NATS Streams to RabbitMQ**

The migration of NATS Streams to RabbitMQ will involve translating NATS concepts into RabbitMQ equivalents to preserve functionality while aligning with RabbitMQ’s architecture:

* **Streams → Exchanges**: Each NATS Stream will be represented as a RabbitMQ exchange. Exchanges in RabbitMQ act as the routing hub, similar to how streams in NATS distribute messages to subscribers. The type of exchange (direct, topic, or fanout) will be chosen based on the message routing pattern currently used in the stream.
* **Consumers → Queues**: NATS consumers subscribing to streams will be mapped to RabbitMQ queues. Queues will bind to the appropriate exchanges, ensuring that messages are delivered to the correct consumers. Durable queues and message acknowledgements will be configured to maintain reliability equivalent to the NATS Streams setup.
* **Message Flow**: Publishers will send messages to RabbitMQ exchanges instead of NATS Streams. Exchanges will route messages to queues according to bindings, allowing multiple consumers to process messages independently or in a load-balanced manner.

This mapping ensures that the behavior of NATS Streams is preserved, while taking advantage of RabbitMQ’s robust routing, durability, and message acknowledgment mechanisms.

---

# HA Applications NATS vs RabbitMQ

for HA applications like CSI that use NATS need special attention because with NATS they automatically create a consumer that gets assigned to them.

This is different in RabbitMQ especially because we have decided that we don't want any automatic Configuration of RabbitMQ and that we want to set everything up manually these will probably mean that we need to create a mechanism in Kubernetes (Stateful sets as an example) for the applications that are HA that for each of them points to there respective queue

of course if we forgo this decision to only do manual Configuration we can have HA applications that create there own queue’s with:

* `exclusive: true`
* `autoDelete: true`
* (optional) `durable: false`

then it will create its own queue that gets deleted if it losses connect but in this case you get data lose when the pods restarts

---

# Message Retry

## How RabbitMQ Handles Message Acknowledgements

Message acknowledgements (acks) are a core part of how RabbitMQ ensures that messages are **delivered reliably** without being **lost** or **processed more than once**. Acks give consumers control over confirming that work is done.

RabbitMQ supports three key acknowledgement modes:

1. **Automatic acknowledgement** (`auto-ack` or `noAck=true`)
2. **Manual acknowledgement**
3. **Negative acknowledgement (nack)** and **rejection**

---

### 1. Automatic Acknowledgements

With automatic ack mode, the broker marks the message as **acknowledged immediately after it is sent to the consumer**, *not* when the consumer finishes processing it.

**Pros**

* Faster, less overhead.

**Cons**

* Risky: if the consumer crashes mid-processing, the message is **lost forever**.

Use this only when message loss is acceptable.

---

### 2. Manual Acknowledgements (Recommended)

Manual acks give your consumer explicit control.

A consumer receives a message and must later send:

wide760basic.ack

This tells RabbitMQ:

> “I’m done with this message. You can delete it from the queue.”

If the consumer dies *before* sending `ack`, RabbitMQ will detect that the TCP connection (or channel) is gone and do this:

* The message is **requeued**
* RabbitMQ delivers it to another consumer (or the same consumer when it reconnects)

This ensures **at-least-once delivery**.

---

### 3. Negative Acknowledgements (Nack) & Rejections

Consumers can explicitly say:

* `basic.nack`
* `basic.reject`

These mean:

> "I cannot process this message."

Both support an option:

wide760requeue = true | false

### If requeue = true

The message is placed back into the queue for redelivery.

### If requeue = false

RabbitMQ discards the message *or* dead-letters it (if a DLX is configured).

---

## How Redelivery Works

If a message is delivered again, RabbitMQ sets the `redelivered` flag.

Consumers can check:

wide760message.properties.redelivered

Useful for avoiding infinite loops or applying fallback logic.

---

## Internals: What RabbitMQ Does With Unacked Messages

RabbitMQ stores unacked messages in a **per-channel unacked message buffer**.

* When a consumer receives a message:

  + it moves from the queue to the channel’s **Unacked** state
* When the consumer sends `ack`:

  + RabbitMQ removes it from memory/disk
* If the channel closes:

  + RabbitMQ *moves all those unacked messages back into the queue*

This is why **long-running consumers should ack messages properly**, otherwise unacked messages can accumulate.

---

## Prefetch (QoS) — Important in Manual Ack Mode

`basic.qos` lets you control how many messages a consumer can have “in flight” (unacked).

wide760prefetch = 1

Means:

> “Give me only one message at a time until I ack it.”

This prevents slow consumers from being overwhelmed—very important for fair dispatch.

---

## How This Looks in Modern RabbitMQ 4.2

RabbitMQ 4.2 improves several features that interact with acks:

### Quorum queues

Now better handle unacked messages and rebalancing.

### Flow Control Enhancements

RabbitMQ slows producers if unacked messages grow too large.

### Monitoring Improvements

The 4.x UI makes it easier to inspect:

* unacked message count
* per-consumer throughput
* redeliveries
* DLX activity

The fundamental ack behavior remains consistent with older versions.

---

# Request/reply

NATS Request/reply could be replaced with RabbitMQ RPC

RabbitMQ **RPC (Remote Procedure Call)** is a common messaging pattern described in the official RabbitMQ tutorials. It lets one application send a request message and wait for a reply—similar to calling a function on another machine.

---

## How RPC with RabbitMQ Works

RabbitMQ does **not** have built-in RPC as a protocol. Instead, it provides the tools (queues, properties, correlation IDs) so you can *implement* RPC using messaging.

The official RPC pattern uses five important parts:

1. **Client (requester)**
2. **Server (worker that does the work)**
3. **Requests queue**
4. **Reply queue**
5. **Correlation ID**

---

## Full Flow (Step-by-Step)

### 1. **Client sends a message to the "RPC queue"**

The client sends a message containing:

* The *actual request data* (ex: “calculate fib(30)”)
* A *reply\_to* property → tells the server where to send the result
* A *correlation\_id* → unique ID so the client knows which response belongs to which request

**Example (conceptual):**

wide760Message:
Body: "fib(30)"
Properties:
reply\_to: "amq.rabbitmq.reply-to"
correlation\_id: "abc123"

---

### 2. **RabbitMQ delivers the message**

RabbitMQ simply puts the message into the **RPC request queue**, e.g.:

wide760rpc\_queue

The worker/server listens on this queue.

---

### 3. **Server receives request and processes it**

The worker receives the message, reads the content, performs the requested job, and prepares a result.

---

### 4. **Server replies using** `reply_to`

The worker sends a response message to the queue specified in the message’s `reply_to` property.

It also includes the **same correlation\_id** as in the request.

wide760Message:
Body: "832040"
Properties:
correlation\_id: "abc123"

This allows the client to match responses to requests.

---

### 5. **Client waits for and receives the response**

The client listens to the reply queue (often an **auto-generated exclusive queue** or the built-in `amq.rabbitmq.reply-to` pseudo-queue).

When the response arrives, the client checks:

wide760If correlation\_id == abc123:
This is the reply to my request!

---

## Key Concepts from the RabbitMQ Documentation

### **reply\_to Property**

A header specifying which queue RabbitMQ should deliver the response to.  
Often a private, temporary queue created by the client.

### **correlation\_id Property**

A unique ID that lets the client identify which request the response belongs to.

### **Exclusive Reply Queue**

The client usually creates a queue like:

* random name
* exclusive (deleted automatically on disconnect)

Example from docs:

wide760amq.gen-JzTY20BRgKO-HjmUJj0wLg

### **Direct Reply-to Optimization**

RabbitMQ provides a special queue:

wide760amq.rabbitmq.reply-to

When used, it allows *“direct-reply-to” RPC*, which eliminates the need for a real reply queue, making RPC faster (no queue declares, bindings, etc.).

---

# Current NATS setup

this is our current NATS setup split between PROD and DEV and per context

## **PROD:**

### Context: ais-stream

* Streams: ais-stream:diff

  + Consumers: ais-stream-consume-area-monitor\_0
  + Consumers: ais-stream-consume-diff-monitor
  + Consumers: ais-stream-consume-encounter-monitor
  + Consumers: ais-stream-consume-etapredictor
  + Consumers: ais-stream-consume-stop-monitor
  + Consumers: ais-stream-consume-vesselvoyage
* Streams: ais-stream:history

  + Consumers: ais-stream-consume-ais-rabbitmq
  + Consumers: ais-stream-consume-ship-history-processor

---

### Context: csi

* Streams: csi:updates

  + Consumers: csi-query\_67d4cf4898-q2vxn
  + Consumers: csi-query\_67d4cf4898-vnwdv
  + Consumers: csi-query\_67d4cf4898-xvvnt

---

### Context: etapredictor

* Streams: KV\_etapredictor

---

### Context: events

* Streams: event-stream

  + Consumers: anchor-monitor
  + Consumers: berth-monitor
  + Consumers: event-consume-etapredictor
  + Consumers: event-consume-ship-history-processor
  + Consumers: event-converter
  + Consumers: event-history-processor
  + Consumers: port-matcher
  + Consumers: portcallplus
  + Consumers: portreporter-monitor
  + Consumers: vesselvoyage
* Streams: KV\_portreporter-monitor-encounter-concurrency
* Streams: KV\_portreporter-monitor-pilot-onboard
* Streams: KV\_portreporter-monitor-tug-standby
* Streams: KV\_portreporter-monitor-tug-waiting
* Streams: KV\_anchor-monitor
* Streams: KV\_encounter-monitor
* Streams: KV\_berth-monitor

---

### Context: service

nats-box context with no jetstream

---

### Context: ship-history

* Streams: ship-history:updates

  + Consumers: ship-history\_548fdf99d8-9cdmh
  + Consumers: ship-history\_548fdf99d8-bgsk9
  + Consumers: ship-history\_548fdf99d8-c4tqj

---

## **DEV:**

### Context: ais-stream

* Streams: ais-stream:diff

  + Consumers: ais-stream-consume-area-monitor\_0
  + Consumers: ais-stream-consume-diff-monitor
  + Consumers: ais-stream-consume-encounter-monitor
  + Consumers: ais-stream-consume-etapredictor
  + Consumers: ais-stream-consume-stop-monitor
  + Consumers: ais-stream-consume-vesselvoyage
* Streams: ais-stream:history

  + Consumers: ais-stream-consume-ais-rabbitmq
  + Consumers: ais-stream-consume-ship-history-processor

---

### Context: csi

* Streams: csi:updates

  + Consumers: csi-query\_dev-6bb556dd9d-8xdkt
  + Consumers: csi-query\_dev-6bb556dd9d-rtqvg
  + Consumers: csi-query\_dev-6bb556dd9d-tkbn8

---

### Context: etapredictor

* Streams: KV\_etapredictor

---

### Context: events

* Streams: event-stream

  + Consumers: anchor-monitor
  + Consumers: berth-monitor
  + Consumers: event-consume-etapredictor
  + Consumers:event-consume-ship-history-processor
  + Consumers:event-converter
  + Consumers:event-history-processor
  + Consumers: port-matcher
  + Consumers: portcallplus
  + Consumers: portreporter-monitor
  + Consumers: service-vessel-component
  + Consumers: vesselvoyage
* Streams: KV\_portreporter-monitor-encounter-concurrency
* Streams: KV\_portreporter-monitor-pilot-onboard
* Streams: KV\_portreporter-monitor-tug-standby
* Streams: KV\_portreporter-monitor-tug-waiting
* Streams: KV\_anchor-monitor
* Streams: KV\_encounter-monitor
* Streams: KV\_berth-monitor

---

### Context: service

nats-box context with no jetstream

---

### Context:ship-history

* Streams: ship-history:updates

  + Consumers: ship-history\_dev-79547d784b-drc6n

---

### Context:test

nats-box context with no jetstream

# Single Broker Setup with RabbitMQ and Redis

this is an example of how the new architecture could look like

## PROD:

### Virtual Host: ais-stream

* Exchange: ais.diff

  + Queue: area-monitor
  + Queue: diff-monitor
  + Queue: encounter-monitor
  + Queue: etapredictor
  + Queue: stop-monitor
  + Queue: vesselvoyage
* Exchange: ais.history

  + Queue: ais-rabbitmq
  + Queue: ship-history-processor

---

### Virtual Host: csi

* Exchange: csi:updates

  + Queue: csi-query\_67d4cf4898-q2vxn
  + Queue: csi-query\_67d4cf4898-vnwdv
  + Queue: csi-query\_67d4cf4898-xvvnt

---

### Redis: etapredictor

* Redis: KV\_etapredictor

---

### Virtual Host: events

* Exchange: event-stream

  + Queue: anchor-monitor
  + Queue: berth-monitor
  + Queue: event-consume-etapredictor
  + Queue: event-consume-ship-history-processor
  + Queue: event-converter
  + Queue: event-history-processor
  + Queue: port-matcher
  + Queue: portcallplus
  + Queue: portreporter-monitor
  + Queue: vesselvoyage
* Redis: KV\_portreporter-monitor-encounter-concurrency
* Redis: KV\_portreporter-monitor-pilot-onboard
* Redis: KV\_portreporter-monitor-tug-standby
* Redis: KV\_portreporter-monitor-tug-waiting
* Redis: KV\_anchor-monitor
* Redis: KV\_encounter-monitor
* Redis: KV\_berth-monitor

---

### Context: service

?

---

### Virtual Host: ship-history

* Exchange: ship-history:updates

  + Queue: ship-history\_1
  + Queue: ship-history\_2
  + Queue: ship-history\_3

---

## **DEV:**

### Virtual Host: ais-stream

* Exchange: ais-stream:diff

  + Queue: ais-stream-consume-area-monitor\_0
  + Queue: ais-stream-consume-diff-monitor
  + Queue: ais-stream-consume-encounter-monitor
  + Queue: ais-stream-consume-etapredictor
  + Queue: ais-stream-consume-stop-monitor
  + Queue: ais-stream-consume-vesselvoyage
* Exchange: ais-stream:history

  + Queue: ais-stream-consume-ais-rabbitmq
  + Queue: ais-stream-consume-ship-history-processor

---

### Virtual Host: csi

* Exchange: csi:updates

  + Queue: csi-query\_dev-1
  + Queue: csi-query\_dev-2
  + Queue: csi-query\_dev-3

---

### Redis: etapredictor

* Redis: KV\_etapredictor

---

### Virtual Host: events

* Exchange: event-stream

  + Queue: anchor-monitor
  + Queue: berth-monitor
  + Queue: event-consume-etapredictor
  + Queue:event-consume-ship-history-processor
  + Queue:event-converter
  + Queue:event-history-processor
  + Queue: port-matcher
  + Queue: portcallplus
  + Queue: portreporter-monitor
  + Queue: service-vessel-component
  + Queue: vesselvoyage
* redis: KV\_portreporter-monitor-encounter-concurrency
* redis: KV\_portreporter-monitor-pilot-onboard
* redis: KV\_portreporter-monitor-tug-standby
* redis: KV\_portreporter-monitor-tug-waiting
* redis: KV\_anchor-monitor
* redis: KV\_encounter-monitor
* redis: KV\_berth-monitor

---

### Context: service

?

---

### Virtual Host: ship-history

* Exchange: ship-history:updates

  + Queue: ship-history\_dev-1

---

### Context:test

?

---