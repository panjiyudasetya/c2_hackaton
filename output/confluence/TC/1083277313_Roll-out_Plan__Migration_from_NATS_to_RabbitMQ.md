---
id: confluence:1083277313
source: confluence
type: page
space: TC
title: 'Roll-out Plan: Migration from NATS to RabbitMQ'
author: Joaquin Marquez Bugella
date: '2026-03-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1083277313
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1083277313
---
# Roll-out Plan: Migration from NATS to RabbitMQ

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1083277313  

## Content

none

## Goal & Scope

The goal of this plan is to migrate messaging workloads from **NATS to RabbitMQ** in a controlled, low-risk manner.  
The migration impacts multiple teams:

* **DevOps** – infrastructure, cluster setup, cleanup
* **Core Components** – shared services and internal messaging
* **Projects** – product-specific consumers and publishers

The migration will be executed **incrementally**, per NATS context, ordered by business importance

**references documents:**   
[NATS diagram](https://drive.google.com/file/d/1eMfVNG4xud4_e1QBSXDFVsi5atYizodx/view?usp=drive_link)

[Roll-out plan diagram](https://drive.google.com/file/d/1A5sq4dUmEurKXvXQ2IzB9kbDNIJh7G9o/view?usp=drive_link)

## Migration path

### Option 1 – Big bang Migration (Preferred)

**Summary:**  
Migrate tightly-coupled publishers and consumers **in one coordinated step**.

#### How it works

For a given message flow (exchange / subject):

1. Downscale or stop the publisher
2. Let existing consumers fully drain messages from NATS
3. Reconfigure publishers and consumers to use RabbitMQ
4. Scale everything back up

#### Pros

* Clean cut-over
* No dual-publishing logic

#### Cons

* Requires strong coordination
* Higher risk of downtime
* Harder rollback

### Option 2 – Gradual migration

**Summary:**  
Applications temporarily connect to **both NATS and RabbitMQ**.

#### How it works

* Publishers publish events to **both NATS and RabbitMQ**

  + Example: `ais-diff` publishes to both systems
* Consumers migrate independently:

  + `ship-history` consumes **only from RabbitMQ**
  + `event-history` continues consuming from **NATS**
* RabbitMQ bindings and queues are created **only when a consumer is ready**

  + Prevents queues from filling up unnecessarily

#### Pros

* Lowest risk
* No hard cut-over moment
* Teams can migrate independently
* Easy rollback

#### Cons

* Temporary duplicate publishing
* Slightly higher operational complexity during migration

## Preparation phase

## HA Queue Support Research and create a guide (DevOps)

**Applies to:** CSI, Ship-history, and other highly available services

**Owner:** DevOps

Before any migration work starts, DevOps will add support the core components team by researching and creating a guide for highly available applications to create their own RabbitMQ queues.

### Responsibilities

* Ensure queues are created only when a consumer is active

### Queue Configuration

Queues created by the plugin must use:

textwide760exclusive: true
autoDelete: true
durable: false (optional)

### Requirements

* One queue per application instance
* Queues are automatically removed when an instance stops
* No unused queues or bindings should remain
* Compatible with RabbitMQ-only and dual (NATS + RabbitMQ) setups

**Outcome:**  
HA services can safely scale and restart without manual queue management or message buildup.

---

## RabbitMQ infrastructure Preparation DEV/LIVE (DevOps)

**Owner:** DevOps  
**Status:** Prerequisite for all following phases

### Tasks

* Provision and configure a **clean RabbitMQ cluster**
* Configure:

  + High availability
  + Authentication & authorization
  + Monitoring & alerting
* Define:

  + Exchange naming conventions
  + Queue naming conventions
  + Bindings and routings

**Outcome:**  
A production-ready RabbitMQ cluster that teams can safely connect to.

---

## Application Changes to Support RabbitMQ Migration (Core Components & Project Teams)

**Owners:** Core Components & Project Teams  
**DevOps support**

All applications must be updated to support migration from NATS to RabbitMQ,  
support both NATS and RabbitMQ via configuration so that the applications can be reconfigured for the migration and easily rolled back if needed  
  
request - reply needs to be removed from portreporter-monitor and replaced with a http rest api call currently portreporter-monitor is not using any of the benefits from using request - reply and can therefore be replaced with http rest api call

### Replace ETA-Predictor Request/Response (Core Components)

**Owner:** Core Components  
**Timing:** Anytime can be done fully independent from the rest of the migration

Before decommissioning NATS, the Core Components team will replace the **ETA-Predictor request/response pattern** currently using NATS with a **RabbitMQ-based implementation**.

### Scope

* Implement RabbitMQ request/response directly in **eta-predictor**
* Validate functional parity, latency, and reliability
* Ensure backward compatibility where required during transition

### Migration Approach

1. Build and validate the RabbitMQ request/response implementation in **eta-predictor**
2. Use this implementation in production
3. Generalize and extract the solution into **skeleton plugins** for reuse by other services

**Outcome:**  
All ETA-Predictor communication is RabbitMQ-based, removing the final NATS dependency from core components and unblocking NATS cleanup.

### Replace NATS in Revents (Core Components)

**Owner:** Core Components  
**Timing:** Anytime can be done fully independent from the rest of the migration

All logic in Revents where it spins up a nats instance were the revents engine publishes its messages on needs te be reworked to work with RabbitMQ

## Migration phase

### Chosen Strategy: Big Bang per NATS Stream

The migration will follow the **Big Bang migration path**, executed **incrementally per NATS stream**, rather than a single platform-wide cutover.

Each NATS stream is treated as an isolated migration unit. Within a stream, all tightly coupled publishers and consumers are migrated in one coordinated step to avoid dual-publishing logic and reduce long-term complexity.

The migration order and application grouping are defined in:

* [**NATS diagram**](https://drive.google.com/file/d/1eMfVNG4xud4_e1QBSXDFVsi5atYizodx/view?usp=drive_link)
* [**Roll-out plan diagram**](https://drive.google.com/file/d/1A5sq4dUmEurKXvXQ2IzB9kbDNIJh7G9o/view?usp=drive_link)

notea70b0b8be690

Note: The Diagrams focuses primarily on ais-engine, as it is the most tightly coupled component.

Note: The Diagrams focuses primarily on ais-engine, as it is the most tightly coupled component.

---

### Migration Order (per NATS Stream)

The proposed migration order, based on business criticality and coupling, is:

1. **diff-stream + history-stream**
2. **event-stream**

Each stream is migrated independently and fully completed before moving to the next one.

---

### Standard Migration Steps (per Stream)

For every application participating in a given NATS stream, the following steps are executed **in order**:

1. **Disable NATS Publishing**

   * Temporarily downscale or stop all publishers for the stream.
   * Ensure no new messages are published to NATS.
2. **Drain Existing NATS Messages**

   * Allow all active consumers to fully process and acknowledge remaining messages.
   * Verify that the NATS stream is empty and stable.
3. **Reconfigure Consumers to RabbitMQ**

   * Update configuration to consume from RabbitMQ exchanges and queues.
   * Validate consumer readiness and correct bindings.
   * Start or scale consumers back up.
4. **Reconfigure and Re-enable Publishers**

   * Update publishers to publish exclusively to RabbitMQ.
   * Re-enable or scale publishers back up.
   * Validate end-to-end message flow.

This approach guarantees a **clean cut-over per stream**, with no overlap or duplicate publishing.

---

### Stream-Specific Scope

Detailed information on which applications belong to each stream is intentionally **not duplicated** in this document.

For the authoritative mapping of:

* Publishers
* Consumers
* Stream ownership

please refer to:

* [**NATS diagram**](https://drive.google.com/file/d/1eMfVNG4xud4_e1QBSXDFVsi5atYizodx/view?usp=drive_link)
* [**Roll-out plan diagram**](https://drive.google.com/file/d/1A5sq4dUmEurKXvXQ2IzB9kbDNIJh7G9o/view?usp=drive_link)

These diagrams define the exact migration scope per stream.

---

### Special Cases

#### CSI and Ship-History

**CSI** and **Ship-History** can be migrated **independently** from the main AIS streams.

Reasoning:

* Their NATS streams are used only for:

  + API ↔ processor synchronization (Ship-History)
  + Internal querying (CSI)
* They are not tightly coupled to the AIS engine streams.

This allows:

* Independent scheduling
* Reduced coordination requirements
* Lower migration risk

These services still follow the same **Big Bang per stream** procedure but are not blocking the main AIS stream migrations.

---

### Validation and Rollback

After each stream migration:

* Verify:

  + Message throughput
  + Consumer lag
  + Error rates
* Monitor RabbitMQ metrics and application logs closely.

Rollback strategy (if needed):

* Disable RabbitMQ publishers
* Re-enable NATS publishing
* Restore consumer configuration to NATS

Because migrations are executed **per stream**, rollback impact is limited and controlled.

## Cleanup phase

### NATS Cleanup (DevOps)

**Triggered when all contexts are migrated**

### Tasks

* Remove remaining NATS consumers
* Disable publishers
* Archive or remove NATS contexts
* Decommission NATS infrastructure

**Outcome:**  
RabbitMQ is the single messaging platform in use.

---

### Application Cleanup – NATS Removal (Core components & Projects)

After all streams are migrated and NATS is decommissioned, all applications must remove **all NATS-related code and configuration**.

* Remove NATS dependencies and configuration
* Delete NATS publishers, consumers, and dual-stack logic
* Ensure applications run **RabbitMQ-only**

**Outcome:** No NATS code remains in any project.