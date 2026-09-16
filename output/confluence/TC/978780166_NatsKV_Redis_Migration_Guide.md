---
id: confluence:978780166
source: confluence
type: page
space: TC
title: NatsKV Redis Migration Guide
author: Jamie de Leest
date: '2025-11-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/978780166
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/978780166
---
# NatsKV Redis Migration Guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/978780166  

## Content

This guide describes how to migrate from **NATS Key-Value storage** to **Spring Data Redis** using Redis Sentinel for high availability.

---

## 1️⃣ Redis Connection Configuration

Replace your NATS KV configuration with a Redis Sentinel setup in `application.yml`:

yamlwide760spring:
application:
name: stop-monitor
data:
redis:
password:
sentinel:
master: mymaster
nodes:
- redis-0.redis-sentinel-external.dev.teqplay.dev:26379
- redis-1.redis-sentinel-external.dev.teqplay.dev:26379
- redis-2.redis-sentinel-external.dev.teqplay.dev:26379
password:

Spring Boot will automatically configure a `RedisConnectionFactory` and `RedisTemplate` for you.

---

## 2️⃣ Replace KV Store Operations

Example form encounter-monitor `KvBucketConfiguration.kt`  
  
Previously, data was persisted and removed through NATS KV operations:

**Before (NATS KV):**

kotlinwide760override fun persist(encounter: EncounterState) {
store(encounter)
kvBucket.put(encounter.key(), encounter)
}
override fun remove(encounter: EncounterState) {
ongoing[encounter.mmsi1]?.remove(encounter.mmsi2)
ongoing[encounter.mmsi2]?.remove(encounter.mmsi1)
kvBucket.delete(encounter.key())
}

**After (Spring Data Redis):**

kotlinwide760override fun persist(encounter: EncounterState) {
store(encounter)
repository.save(encounter)
}
override fun remove(encounter: EncounterState) {
ongoing[encounter.mmsi1]?.remove(encounter.mmsi2)
ongoing[encounter.mmsi2]?.remove(encounter.mmsi1)
repository.delete(encounter)
}

All interactions with Redis should go through your Spring Data repository.

---

## 3️⃣ Define the Redis Repository

Create a Spring Data Redis repository to handle persistence:

kotlinwide760import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository
@Repository
interface EncounterRepository : CrudRepository<EncounterState, String>

Spring will automatically generate implementations for standard CRUD operations like `save()`, `findById()`, `delete()`, etc.

for more CRUD operations like an find by mmsi function you can create this function in the repository like so:

kotlinwide760import org.springframework.data.repository.CrudRepository
import org.springframework.stereotype.Repository
@Repository
interface EncounterRepository : CrudRepository<EncounterState, String> {
fun findByMmsi(mmsi1: Long): List<EncounterState>
}

then spring data will generate these functions for you, for more information about all the possibilities with Query Methods in spring data i would recommend referencing the spring data documentation   
<https://docs.spring.io/spring-data/commons/reference/repositories/query-methods-details.html>

<https://docs.spring.io/spring-data/commons/reference/repositories/query-keywords-reference.html>

---

## 4️⃣ Annotate Your Entity

Annotate your entity with `@RedisHash` to map it to a Redis hash, and mark your lookup fields with `@Indexed` if you need to query by them.

kotlinwide760import org.springframework.data.annotation.Id
import org.springframework.data.redis.core.RedisHash
import org.springframework.data.redis.core.index.Indexed
@RedisHash("encounter-monitor:encounter")
data class EncounterState(
@Id val key: String,
@Indexed
val mmsi1: Long,
@Indexed
val mmsi2: Long,
val state: String
)

### 🔍 About `@Indexed`

* The `@Indexed` annotation tells Spring Data Redis to **automatically maintain secondary indexes** for those fields.
* This allows you to query the repository by non-ID fields.

For example:

kotlinwide760interface EncounterRepository : CrudRepository<EncounterState, String> {
fun findByMmsi1(mmsi1: Long): List<EncounterState>
fun findByMmsi2(mmsi2: Long): List<EncounterState>
}

Spring Data Redis will automatically use the Redis secondary index to resolve these queries efficiently.

---

## 5️⃣ Key Naming Convention

We use the following key pattern for all Redis hashes to ensure consistency across applications:

wide760<app-name>:<store>:<rest-of-key>

**Example:**

wide760encounter-monitor:encounter:12345-67890

This helps separate data per application and per domain object.