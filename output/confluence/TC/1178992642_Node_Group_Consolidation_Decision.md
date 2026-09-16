---
id: confluence:1178992642
source: confluence
type: page
space: TC
title: Node Group Consolidation Decision
author: Jamie de Leest
date: '2026-04-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1178992642
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1178992642
---
# Node Group Consolidation Decision

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1178992642  

## Content

## Overview

This document outlines the decision to consolidate the existing Kubernetes node groups into a single, more efficient configuration. The change is driven by both operational improvements and better resource utilization.

---

## Previous Setup

We previously maintained two separate node groups:

* **AIS Engine node group:** 4 nodes
* **Development node group:** 10 nodes
* **Total nodes:** 14

### Infrastructure Details

| Node Type | CPU | Clock Speed | CoreMark Score | Memory (GB) | Price per Month ($) |
| --- | --- | --- | --- | --- | --- |
| r5.xlarge | 4 | 3.1 GHz | 58,306.21 | 32 | 183.96 |

**Total Resources:**

* CPU: 56
* Memory: 448 GB
* Monthly Cost: **$2,575.44**

---

## New Setup

We are migrating to a unified node group using:

| Node Type | CPU | Clock Speed | CoreMark Score | Memory (GB) | Price per Month ($) |
| --- | --- | --- | --- | --- | --- |
| r6a.x2large | 8 | 3.6 GHz | 161,567.20 | 64 | 331.13 |

**Deployment:**

* Total nodes: 5
* Total CPU: 40
* Total Memory: 320 GB
* Monthly Cost: **$1,655.64**

---

## Resource Requirements

### Actual Requested Resources

| Workload | CPU | Memory (GB) |
| --- | --- | --- |
| AIS Engine | 27.2 | 146 |
| Development | 9 | 69 |
| **Total** | **36** | **216** |

### Capacity vs Demand

* **Provisioned CPU:** 40 → sufficient for 36 requested
* **Provisioned Memory:** 320 GB → sufficient for 216 GB requested

This leaves adequate headroom for scaling and operational stability.

---

## Key Reasons for the Change

### 1. Reduced Resource Waste

Previously, separating workloads into different node groups created a **hard boundary**:

* Unused resources in one node group could not be used by the other
* This led to significant **overprovisioning and inefficiency**

By merging the node groups:

* Resources are now shared across workloads
* Overall utilization is significantly improved

---

### 2. Simplified Upgrade Strategy

The original reason for separate node groups was to simplify Kubernetes upgrades.

**Old approach:**

* Upgrade per node group

**New approach:**

* Restart workloads **per namespace**

This makes separate node groups unnecessary while still allowing controlled rollouts and minimizing downtime.

---

### 3. Improved Performance per Node

The new node type (**r6a.x2large**) provides:

* Higher CPU performance (significantly better CoreMark score)
* More memory per node
* Better cost-to-performance ratio

This allows us to run fewer nodes while maintaining (and improving) performance.

---

### 4. Cost Reduction

* **Previous cost:** $2,575.44/month
* **New cost:** $1,655.64/month

**Savings:** ~$920/month (~35% reduction)

---

## Conclusion

By consolidating node groups:

* Resource utilization is improved
* Operational complexity is reduced
* Upgrade strategy remains effective via namespace-level restarts
* Infrastructure costs are significantly lowered

This change results in a more efficient, scalable, and cost-effective Kubernetes environment.