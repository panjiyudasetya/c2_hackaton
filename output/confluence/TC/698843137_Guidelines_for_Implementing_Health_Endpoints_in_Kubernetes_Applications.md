---
id: confluence:698843137
source: confluence
type: page
space: TC
title: Guidelines for Implementing Health Endpoints in Kubernetes Applications
author: Michel Wilson
date: '2025-04-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/698843137
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/698843137
---
# Guidelines for Implementing Health Endpoints in Kubernetes Applications

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/698843137  

## Content

This document outlines the principles and best practices for implementing health endpoints in services running on our Kubernetes cluster.

The goal is to ensure that health endpoints work effectively with in-cluster monitoring, so applications are **not restarted unnecessarily** — helping us avoid **cascading restarts** and improve system stability.

---

### 📈 Health Status Levels

| **Status** | **Meaning** |
| --- | --- |
| `HEALTHY` | Service is fully operational; all core functionality and dependencies are working as expected. |
| `DEGRADED` | Service is partially operational; one or more non-critical dependencies are impaired. |
| `DOWN` | Service is non-functional due to a critical failure and cannot fulfill its primary responsibilities. |

---

## ⚙️ General Principles

---

### 1. Prevent Unnecessary Restarts

Kubernetes health endpoints are used for two purposes:

1. **Startup Readiness**  
   Kubernetes waits for the app to report `UP` before routing traffic. If startup takes too long, the pod is terminated.
2. **Liveness Check**  
   After startup, if the health check returns `DOWN`, Kubernetes assumes the app is broken and restarts it.

> **Key rule:** Only return `DOWN` when there is a *reasonable expectation* that a restart will resolve the issue.

#### ✅ Examples

* If `poma` is down during `areamonitor` startup → report `DOWN`.  
  *Reason:* `areamonitor` *cannot start without loading areas.*
* If `poma` goes down during normal operation → report `DEGRADED`.  
  *Reason: Service can continue with stale data.*

---

### 2. Reconnect, Don’t Restart

If a long-lived connection (e.g., to a broker or database) drops, the application should:

* Attempt to **reconnect automatically**.
* Avoid using application restarts as a recovery mechanism.

---

### 3. Report Internal State (Not External Health)

* When a **non-critical dependency** fails:

  + Handle it internally.
  + Set your service health to `DEGRADED`, not `DOWN`.
* **Do not base your status on a dependency’s health endpoint.**  
  That endpoint may reflect problems irrelevant to your service. Instead, observe the actual behavior — e.g., if repeated 503s occur when calling a non-critical service, report `DEGRADED`.

---

### 4. Avoid Restart Storms

Design health checks to **avoid cascading restarts** when shared services go down.

Example:

> If MongoDB is down, and 5 services depend on it, those services should not all restart at once.

---

### 5. Keep It Simple

* Focus on **technical health**, not business logic.

  + *Example: don’t return* `DOWN` *because a feature flag is off.*
* Health endpoints are for infrastructure tools (e.g., probes, alerts), not functional status reports.

---

## ✅ Recommended Implementation Pattern

Use a pattern similar to **PortReporter**:

* Monitor dependencies from within your service logic.
* If repeated failures occur:

  + Internally mark the dependency as **unhealthy**.
  + Optionally reduce call volume or apply retry logic.
  + Set your own health to `DEGRADED`, not `DOWN`.

> ⚠️ Do **not** base your service health solely on the dependency’s health status endpoint.