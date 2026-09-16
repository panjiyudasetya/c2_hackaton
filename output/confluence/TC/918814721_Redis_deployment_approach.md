---
id: confluence:918814721
source: confluence
type: page
space: TC
title: Redis deployment approach
author: Jamie de Leest
date: '2025-11-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/918814721
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/918814721
---
# Redis deployment approach

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/918814721  

## Content

## Context & Goals

We need a scalable, highly available, and maintainable Redis setup for use across multiple Teqplay applications. Redis will be deployed in our Kubernetes (K8s) cluster and serve as a durable key-value store for both caching and transient state.

**Key goals:**

* Provide **high availability** and **durability**.
* Ensure **data separation** between applications.
* Enable **uniform key naming and management**.
* Design for **future scalability** toward Redis Cluster mode without re-architecting applications.

## Decision Summary

We will start with a **single HA Redis deployment in the broker namespace**, using Redis Sentinel for automatic failover and PVC-backed storage for durability.

Applications will use a shared wrapper library that enforces a consistent key-naming convention and prepares us for seamless migration to Redis Cluster in the future.

## Architecture Overview

| Aspect | Design |
| --- | --- |
| **Deployment model** | One HA Redis (primary + 2 replicas) |
| **Failover** | Managed by Redis Sentinel |
| **K8s primitives** | StatefulSet, Headless Service, ClusterIP Service, PVCs, PodDisruptionBudget, anti-affinity |
| **Durability** | Persistent volumes, AOF enabled (`appendonly yes`, `appendfsync everysec`) |
| **Monitoring** | Redis exporter integrated with Prometheus and Grafana dashboards |
| **Configuration backup** | Via Velero (cluster-wide) |
| **Data backup** | Not required (data is ephemeral/stale at restore time) |
| **Security** | Kubernetes Secrets for credentials; NetworkPolicies for access control |

## Helm Deployment (DevOps)

The DevOps team will select and configure an appropriate Helm chart—**CloudPirates** `redis` (standalone + Sentinel) is recommended.

### Key configuration parameters

yamlwide760architecture: replication
podAnnotations:
prometheus.io/port: "9121"
prometheus.io/scrape: "true"
auth:
enabled: true
sentinel: true
config:
content: |-
# Redis configuration
bind \* -::\*
port 6379
# Enable AOF https://redis.io/topics/persistence#append-only-file
appendonly yes
# Disable RDB persistence, AOF persistence already enabled.
save ""
metrics:
enabled: true
replicaCount: 3
sentinel:
enabled: true
quorum: 2
extraObjects:
- apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: "{{ include \"redis.fullname\" . }}-network-policy"
namespace: "{{ .Release.Namespace }}"
spec:
podSelector:
matchLabels:
app.kubernetes.io/instance: "{{ .Release.Name }}"
app.kubernetes.io/name: "{{ .Release.Name }}"
ingress:
- ports:
- protocol: TCP
port: 6379
- protocol: TCP
port: 26379
- protocol: TCP
port: 9121
egress:
- {}
policyTypes:
- Ingress
- Egress
- apiVersion: v1
kind: Service
metadata:
name: "{{ include \"redis.fullname\" . }}-sentinel-external"
namespace: "{{ .Release.Namespace }}"
annotations:
external-dns.alpha.kubernetes.io/access: private
external-dns.alpha.kubernetes.io/hostname: "{{ include \"redis.fullname\" . }}-sentinel-external.dev.teqplay.dev"
spec:
ports:
- name: redis
protocol: TCP
port: 26379
targetPort: sentinel
clusterIP: None
selector:
app.kubernetes.io/instance: "{{ .Release.Name }}"
app.kubernetes.io/name: "{{ .Release.Name }}"

A **baseline** `values.yaml` will be stored in the same repository as our Kubernetes deployment scripts.  
This baseline defines shared defaults (persistence, replicas, metrics, PDBs) and can be reused across environments (`dev` and `prod`) with minimal overrides.

## Key Naming Standard (Core Components)

### Structure

Redis keys must follow a strict, uniform convention to ensure clear ownership and future cluster compatibility.

wide760<app>:<store>:<rest-of-key>

### Slot-pinning Strategy

Redis Cluster distributes keys across 16,384 hash slots. Using a **hash-tag** (`{}`) allows us to pin related keys to the same slot.

#### **Chosen strategy: Per-entity pinning by MMSI**

All keys associated with a single MMSI (ship) will share the same hash-tag to co-locate on one shard.

**Example keys:**

wide760stop-monitor:{123456789}:stop-state
stop-monitor:{123456789}:trace-state

**Benefits:**

* All data for one MMSI co-located → efficient transactions and Lua scripts.
* Natural horizontal distribution across shards.
* Easy migration to Redis Cluster.

**Limitations:**

* Transactions cannot span multiple MMSIs (acceptable for our use case).
* Requires consistent application of hash-tag syntax.

## Wrapper Library (Spring Data Redis)

The Core Components team will build a lightweight wrapper library around Spring Data Redis to:

* Enforce consistent key naming and tagging.
* Abstract connection setup for standalone and future cluster modes.
* Simplify serialization/deserialization and configuration.

**Planned features:**

* `KeyBuilder` API, e.g.:

* redisKeys.forStore("stop-state").forEntity(mmsi).build("current");
  // becomes stop-monitor:{123456789}:stop-state:current
* Automatic prefix insertion using the Spring `application.name` property.
* Validation of key format and hash-tag usage.
* Cluster-aware configuration path (Lettuce client).
* Optional helpers for Spring’s `@Cacheable`.

TTL/type suffixes are **not used**.

---

## Migration Plan (Stop Monitor App)

To validate Redis integration, the stop monitor app will initially connect to the new HA Redis deployment.

Migration code will rename old keys to follow the new scheme:

* Use `SCAN` → batched `RENAME` (500–1000 keys per batch).
* Implement via a Spring profile (`migration`).
* Handle potential key collisions gracefully.
* Log progress for observability.
* Keep it lightweight unless data volume demands tooling like `redis-shake`.

## Observability & Operations

* **Metrics:**

  + Ops per sec, memory usage/fragmentation, replication lag, evictions, latency, AOF/RDB status.
* **Alerting thresholds:**

  + Memory > 85 %, evictions > 0, replication down, latency p99 > 3 ms, AOF rewrite failures.
* **Prometheus integration:**

  + Enabled via Helm `metrics.enabled: true`.
* **Grafana dashboards:**

  + Include latency, ops per sec, replication health.
* **Synthetic canary:**

  + Optional lightweight job performing `PING/SET/GET` for end-to-end verification.
* **Backups:**

  + Configuration and PVCs captured by Velero; data backups not required.

## Security

* **Authentication:** Redis AUTH with per-application Kubernetes Secret.
* **Authorization:** Redis ACLs may be introduced later if multiple users per namespace arise.
* **Network:** NetworkPolicies restrict access to in-namespace applications and monitoring.

## Scalability & Future Evolution (single instance → cluster)

### Migration trigger

When:

* Memory utilization exceeds ~70 %,
* Write latency increases significantly, or
* Single-node throughput becomes a bottleneck.

### Path forward

1. Deploy a **Redis Cluster** in parallel.
2. Use `redis-shake` or `redis-migrate-tool` to live-copy data.
3. Switch clients to cluster endpoint.
4. Decommission Sentinel setup.

Because the client library and key schema are already cluster-compatible, this transition will be straightforward.