---
id: confluence:1166114817
source: confluence
type: page
space: TC
title: RabbitMQ Management Conventions
author: Joost Laurman
date: '2026-03-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1166114817
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1166114817
---
# RabbitMQ Management Conventions

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1166114817  

## Content

## 1. Purpose

This document defines the conventions and architectural decisions for managing RabbitMQ within Teqplay. The goal is to ensure consistency, scalability, and maintainability across all services using messaging.

---

## 2. Message Separation Strategy

### 2.1 Virtual Hosts (VHosts)

* VHosts are the primary mechanism for functional separation.
* Prefer fewer, larger VHosts rather than many small ones.

#### Example VHosts:

* AisUpdates
* TeqplayEvents
* PortCall (formerly PortReporter)
* Synchronization updates (e.g., CSI processing)

### 2.2 Exchanges

* Each exchange represents a single message superclass.
* Exchanges act as the input layer.

### 2.3 Queues

* Queues act as the output layer.
* Each queue must only contain messages from a single superclass.

### 2.4 Routing Keys

* Used for filtering messages within an exchange.
* Enables fine-grained control without introducing additional exchanges.

---

## 3. Topology Management

### 3.1 Manual Configuration

* RabbitMQ structure is managed manually.
* Avoid automatic creation via application code.

Ensures:

* Consistent naming
* Full operational control
* Predictability across environments

---

## 4. Naming Conventions

### 4.1 Exchanges

* Format: `superclass`
* example: a exchange called `event` for the `Event` class in `ais-engine`
* Represents the type of messages entering the system

### 4.2 Queues

* Format: `consumer_superclass`
* example: `berth-monitor_event` for a queue where the `berth-monitor` consumes `Events` from
* Represents the consumer and the message type

### 4.3 Rules

* Exchanges are inputs
* Queues are outputs
* One exchange can connect to zero or many queues
* Exchanges should NOT be chained to other exchanges

---

## 5. Authorization Model

### 5.1 User Accounts

* Use personal accounts for authentication when connection to as an example a testing queue via local machine

### 5.2 Access Control

* Permissions are assigned per VHost:

  + Read
  + Write
  + Configure

### 5.3 Management

* Credentials are managed by the DEVOPS team and are stored in Vaultwarden in the Dev or Live system\brokers collection

---

## 6. Observability

### 6.1 Metrics

* RabbitMQ metrics should be exposed to Prometheus

### 6.2 Goals

* Monitor:

  + Queue sizes
  + Message rates
  + Broker health