---
id: confluence:1092583425
source: confluence
type: page
space: TC
title: PortCallOne Scalable Arrival and In-Port Cache
author: Milzam Abi Karami
date: '2026-01-29'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1092583425
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1092583425
---
# PortCallOne Scalable Arrival and In-Port Cache

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1092583425  

## Content

22falsenonelisttrue

## 🎯 Executive Summary

**Goal:** Scale the `getJourneysByPortCached` caching mechanism from 3 ports to 50-100 ports without consuming excessive application memory.

**Proposed Approach:** MongoDB-backed cache storing full journey objects with 1-hour TTL.

**Key Benefits:**

* ✅ **50% memory reduction** (90MB in-memory → 45MB in MongoDB for 100 ports)
* ✅ **No new infrastructure** (uses existing MongoDB)
* ✅ **Eliminates cold start problem** (current: ~3 min for 2 ports → ~150 min for 100 ports)
* ✅ **Survives restarts** (critical for SEO - no slow responses after deployment)
* ✅ **Fast cache hits** (10-20ms vs current <1ms)
* ✅ **Scales to 100+ ports** easily
* ✅ **No dependency on external APIs** for cache hits

**Trade-offs:**

* ⚠️ Slightly slower cache hits (10-20ms vs <1ms in-memory)
* ⚠️ Data can be up to 1 hour stale (acceptable per business requirements)
* ⚠️ Larger MongoDB storage (45MB vs potential 1.5MB with IMO-only approach)

---

## 📊 Current State Analysis

### Current Implementation

**Location:** `VesselJourneyService.kt` (lines 52-311)

**Architecture:**

kotlinwide760// In-memory cache
private val journeysByPortCache = ConcurrentHashMap<JourneysByPortCacheKey, Set<FullShipJourney>>()
// Scheduled refresh every 15 minutes
@Scheduled(fixedRateString = "\${cache.journeys-by-port}")
fun refreshJourneysByPort() { ... }

**Cache Key:**

kotlinwide760data class JourneysByPortCacheKey(
val unlocode: String, // e.g., "BRSSZ"
val journeyStatus: JourneyStatus, // EN\_ROUTE or IN\_ARRIVAL\_PORT
val minimumShipLength: Int // Currently fixed at 150m
)

**Current Configuration:**

* **Cached ports:** 2 ports from `vessel-journey.cached-unlocodes`
* **Cache entries:** 2 per port (EN\_ROUTE + IN\_ARRIVAL\_PORT) = 4 total
* **Refresh interval:** 15 minutes (`cache.journeys-by-port=PT15M`)
* **Memory usage:** ~3KB per journey × ~50 vessels × 2 statuses = **~300KB** per port
* **Preload time:** **~3 minutes for 2 ports** (4 calls total)

### Scaling Calculation

**For 100 ports:**

* Cache entries: 100 ports × 2 statuses = 200 entries
* Vessels per port: ~150 average
* Memory per journey: ~3KB (FullShipJourney with nested objects)
* **Total memory:** 100 × 2 × 150 × 3KB = **90MB** 🔴

**Problem:** This doesn't fit well in a 2Gi heap, especially with other caches and operations.

---

## 🚨 Problem Statement

### Business Requirements

1. **SEO Performance:** Google crawlers need fast responses (<200ms) for all cached ports
2. **Scale Target:** Support 50-100 ports (vs current 3)
3. **Restart Resilience:** Cache must survive application restarts (no cold start penalty)
4. **Staleness Tolerance:** Up to 1 hour stale data is acceptable
5. **Infrastructure Constraint:** Use existing MongoDB (no Redis/ElastiCache)

### Technical Challenges

1. **Memory Pressure:** 90MB in-memory cache is too large for single pod
2. **Cold Start Problem:**

   * Current: ~3 minutes to preload 2 ports
   * Projected: **~75-150 minutes** to preload 100 ports 🔴
   * SEO Impact: Google crawlers see slow responses for hours after restart
3. **Not Shared:** Each pod has its own cache (if we scale horizontally later)
4. **Unbounded Growth:** No eviction policy → memory grows with port count

---

## 💡 Proposed Solution

### Core Concept: Store Full Journey Objects in MongoDB

**Key Insight:** We need to cache the complete `FullShipJourney` objects because:

1. **Upstream services don't cache** - CsiService, VesselVoyageService, and ShipHistoryService make direct HTTP calls
2. **Cache hits must be fast** - Reconstructing from IMO lists would require 500ms-2s of external API calls
3. **Business accepts staleness** - Up to 1 hour stale data is acceptable per requirements
4. **MongoDB is cheaper than heap** - 45MB in MongoDB vs 90MB in application heap

**Storage Trade-off:**

* **Before:** Store `Set<FullShipJourney>` in heap (~3KB per journey) = 90MB for 100 ports
* **After:** Store `Set<FullShipJourney>` in MongoDB (~3KB per journey) = 45MB for 100 ports
* **Benefit:** Moves data out of application heap, survives restarts, shared across pods

### Architecture Diagram

wide760┌──────────────────────────────────────────────────────────────────┐
│ API Request │
│ GET /v1/vesselJourney/port?unlocode=BRSSZ │
└──────────────────────┬───────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────────┐
│ VesselJourneyService.getJourneysByPortCached() │
│ ┌────────────────────────────────────────────────────────────┐ │
│ │ 1. Query MongoDB cache for full journey objects │ │
│ │ → journeysCacheDataSource.findByKey(...) │ │
│ └────────────────────────────────────────────────────────────┘ │
│ │ │
│ ┌──────────┴──────────┐ │
│ │ Cache Hit? │ │
│ └──────────┬──────────┘ │
│ │ │
│ ┌───────────┴───────────┐ │
│ │ YES │ NO │
│ ▼ ▼ │
│ ┌─────────────────┐ ┌──────────────────────┐ │
│ │ Get journeys │ │ getJourneysByPort │ │
│ │ from cache │ │ Direct (slow path) │ │
│ │ (10-20ms) │ │ (500ms-2s) │ │
│ └────────┬────────┘ └──────────┬───────────┘ │
│ │ │ │
│ │ │ Update cache │
│ │ │ with full journeys │
│ │ │ │
│ └────────────┬───────────┘ │
│ ▼ │
│ ┌────────────────────────┐ │
│ │ Return FullShipJourney │ │
│ │ Set to caller │ │
│ └────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘
Background Process (Every 30 minutes):
┌──────────────────────────────────────────────────────────────────┐
│ refreshJourneysByPortCache() │
│ ┌────────────────────────────────────────────────────────────┐ │
│ │ 1. Find cache entries expiring in next 15 min │ │
│ │ 2. For each entry: │ │
│ │ - Fetch fresh data via getJourneysByPortDirect() │ │
│ │ - Store full journey objects in MongoDB │ │
│ │ - Set expiresAt = now + 1 hour │ │
│ └────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────┘

---

## 🔧 Technical Design

### 1. MongoDB Collection Schema

**Collection Name:** `journeysByPortCache`

**Document Structure:**

kotlinwide760data class JourneysByPortCache(
@JsonProperty("\_id")
override val \_id: String = UUID.randomUUID().toString()
// Cache key components
val unlocode: String, // e.g., "BRSSZ"
val journeyStatus: JourneyStatus, // EN\_ROUTE or IN\_ARRIVAL\_PORT
val minimumShipLength: Int, // e.g., 150
// Cached data (FULL JOURNEY OBJECTS)
val journeys: Set<FullShipJourney>, // Complete journey objects with all nested data
// Audit fields
override val createdAt: Instant = Instant.now(),
override val createdBy: String = "system",
override val updatedAt: Instant = Instant.now(),
override val updatedBy: String = "system",
) : DbObject, ExtendedTrackable

**Indexes:**

kotlinwide760// Compound index for fast lookups
ensureIndex(
JourneysByPortCache::unlocode,
JourneysByPortCache::journeyStatus,
JourneysByPortCache::minimumShipLength
)

**Example Document:**

jsonwide760{
"\_id": "BRSSZ:EN\_ROUTE:150",
"unlocode": "BRSSZ",
"journeyStatus": "EN\_ROUTE",
"minimumShipLength": 150,
"journeys": [
{
"ship": {
"imo": "9123456",
"name": "VESSEL NAME",
"mmsi": "123456789",
"flag": "BR",
"type": "Container Ship",
"length": 200.0,
"width": 32.0
},
"currentPosition": { "latitude": -23.5, "longitude": -46.6 },
"currentVoyage": { "destination": "BRSSZ", "eta": "2026-01-28T10:00:00Z" },
"arrivalVisitInfo": { "port": {...}, "estimatedTime": "2026-01-28T10:00:00Z" }
}
],
"refreshedAt": "2026-01-27T10:00:00Z",
"expiresAt": "2026-01-27T11:00:00Z",
"createdAt": "2026-01-27T09:00:00Z",
"createdBy": "system",
"updatedAt": "2026-01-27T10:00:00Z",
"updatedBy": "system"
}

**Note:** Each `FullShipJourney` object is ~3KB, so a cache entry with 150 vessels = ~450KB per document.

---

## 💻 Code Examples

### 2. Data Access Layer (DataSource)

**New File:** `src/main/kotlin/nl/teqplay/portcallone/datasource/JourneysByPortCacheDataSource.kt`

kotlinwide760package nl.teqplay.portcallone.datasource
import com.mongodb.client.model.ReplaceOptions
import com.mongodb.kotlin.client.MongoDatabase
import nl.teqplay.portcallone.model.cache.JourneysByPortCache
import nl.teqplay.skeleton.datasource.kmongo.and
import nl.teqplay.skeleton.datasource.kmongo.ensureIndex
import nl.teqplay.skeleton.datasource.kmongo.eq
import nl.teqplay.skeleton.datasource.kmongo.findOne
import nl.teqplay.skeleton.datasource.kmongo.lte
import nl.teqplay.vesselvoyage.apiv2.model.Journey.JourneyStatus
import org.springframework.stereotype.Component
import java.time.Duration
import java.time.Instant
@Component
class JourneysByPortCacheDataSource(database: MongoDatabase) : DataSource<JourneysByPortCache>() {
private val collectionName = "journeysByPortCache"
override val collection =
database
.getCollection(collectionName, JourneysByPortCache::class.java)
.apply {
// Compound index for fast cache lookups
ensureIndex(
JourneysByPortCache::unlocode,
JourneysByPortCache::journeyStatus,
JourneysByPortCache::minimumShipLength,
)
}
override fun createWith(
item: JourneysByPortCache,
by: String,
at: Instant,
): JourneysByPortCache = item.copy(createdBy = by, createdAt = at)
override fun updateWith(
item: JourneysByPortCache,
by: String,
at: Instant,
): JourneysByPortCache = item.copy(updatedBy = by, updatedAt = at)
/\*\*
\* Find cache entry by key components.
\* Returns null if not found or expired.
\*/
fun findByKey(
unlocode: String,
journeyStatus: JourneyStatus,
minimumShipLength: Int,
): JourneysByPortCache? {
val filter =
and(
JourneysByPortCache::unlocode eq unlocode,
JourneysByPortCache::journeyStatus eq journeyStatus,
JourneysByPortCache::minimumShipLength eq minimumShipLength,
)
return collection.findOne(filter)
}
}

### 3. Model Class

**New File:** `src/main/kotlin/nl/teqplay/portcallone/model/cache/JourneysByPortCache.kt`

kotlinwide760package nl.teqplay.portcallone.model.cache
import com.fasterxml.jackson.annotation.JsonProperty
import nl.teqplay.portcallone.model.ExtendedTrackable
import nl.teqplay.portcallone.model.shipjourney.FullShipJourney
import nl.teqplay.skeleton.datasource.DbObject
import nl.teqplay.vesselvoyage.apiv2.model.Journey.JourneyStatus
import java.time.Instant
import java.util.UUID
/\*\*
\* MongoDB cache document for journeys by port.
\* Stores complete FullShipJourney objects to avoid external API calls on cache hits.
\*/
data class JourneysByPortCache(
@JsonProperty("\_id")
override val \_id: String = UUID.randomUUID().toString(),
val unlocode: String,
val journeyStatus: JourneyStatus,
val minimumShipLength: Int,
val journeys: Set<FullShipJourney>, // Complete journey objects
val refreshedAt: Instant,
val expiresAt: Instant,
override val createdAt: Instant = Instant.now(),
override val createdBy: String = "system",
override val updatedAt: Instant = Instant.now(),
override val updatedBy: String = "system",
) : DbObject, ExtendedTrackable

### 4. Service Layer Changes

**Modified File:** `src/main/kotlin/nl/teqplay/portcallone/service/VesselJourneyService.kt`

#### 4.1 Remove In-Memory Cache

**BEFORE:**

kotlinwide760@Service
class VesselJourneyService(
private val csiService: CsiService,
private val pomaService: PomaService,
private val vesselVoyageService: VesselVoyageService,
private val shipHistoryService: ShipHistoryService,
private val vesselSubscriptionDataSource: VesselSubscriptionDataSource,
private val portVisitSharingService: PortVisitSharingService,
private val portVisitNotesService: PortVisitNotesService,
private val vesselJourneyProperties: VesselJourneyProperties,
) {
private val logger = KotlinLogging.logger { }
// ❌ REMOVE THIS
private val journeysByPortCache = ConcurrentHashMap<JourneysByPortCacheKey, Set<FullShipJourney>>()
// ❌ REMOVE THIS
private val cacheInitialized = AtomicBoolean(false)
// ... rest of the class
}

**AFTER:**

kotlinwide760@Service
class VesselJourneyService(
private val csiService: CsiService,
private val pomaService: PomaService,
private val vesselVoyageService: VesselVoyageService,
private val shipHistoryService: ShipHistoryService,
private val vesselSubscriptionDataSource: VesselSubscriptionDataSource,
private val portVisitSharingService: PortVisitSharingService,
private val portVisitNotesService: PortVisitNotesService,
private val vesselJourneyProperties: VesselJourneyProperties,
private val journeysCacheDataSource: JourneysByPortCacheDataSource, // ✅ ADD THIS
) {
private val logger = KotlinLogging.logger { }
// ... rest of the class
}

#### 4.2 Update `getJourneysByPortCached` Method

**BEFORE (lines 180-215):**

kotlinwide760fun getJourneysByPortCached(
portId: String?,
unlocode: String?,
journeyStatus: JourneyStatus,
minimumShipLength: Int,
): Set<FullShipJourney> {
if (journeyStatus == JourneyStatus.IN\_DEPARTURE\_PORT) {
throw BadRequestException("IN\_DEPARTURE\_PORT is not supported")
}
val port =
pomaService.getPortByPortIdOrUnlocode(portId, unlocode)
?: throw NotFoundException("Port not found")
if (port.unlocode !in vesselJourneyProperties.cachedUnlocodes) {
throw BadRequestException("Port is not supported.")
}
val cacheKey =
JourneysByPortCacheKey(
unlocode = port.unlocode,
journeyStatus = journeyStatus,
minimumShipLength = minimumShipLength,
)
// ❌ OLD: Check in-memory cache
journeysByPortCache[cacheKey]?.let { cachedResult ->
return cachedResult
}
// Cache miss - Data is not cached, fetch directly
return getJourneysByPortDirect(portId, unlocode, journeyStatus, minimumShipLength)
}

**AFTER:**

kotlinwide760fun getJourneysByPortCached(
portId: String?,
unlocode: String?,
journeyStatus: JourneyStatus,
minimumShipLength: Int,
): Set<FullShipJourney> {
if (journeyStatus == JourneyStatus.IN\_DEPARTURE\_PORT) {
throw BadRequestException("IN\_DEPARTURE\_PORT is not supported")
}
val port =
pomaService.getPortByPortIdOrUnlocode(portId, unlocode)
?: throw NotFoundException("Port not found")
if (port.unlocode !in vesselJourneyProperties.cachedUnlocodes) {
throw BadRequestException("Port is not supported.")
}
// ✅ NEW: Check MongoDB cache
val cached = journeysCacheDataSource.findByKey(port.unlocode, journeyStatus, minimumShipLength)
// If cache hit and not expired, return cached journeys directly
if (cached != null && !cached.isExpired()) {
logger.debug { "Cache HIT for ${port.unlocode}:$journeyStatus:$minimumShipLength (${cached.journeys.size} journeys)" }
return cached.journeys // Fast: 10-20ms MongoDB query
}
// Cache miss: fetch fresh data and update cache
logger.debug { "Cache MISS for ${port.unlocode}:$journeyStatus:$minimumShipLength" }
return getJourneysByPortDirect(portId, unlocode, journeyStatus, minimumShipLength).also { journeys ->
// Store complete journey objects in cache
val cacheEntry =
JourneysByPortCache(
\_id = JourneysByPortCache.generateId(port.unlocode, journeyStatus, minimumShipLength),
unlocode = port.unlocode,
journeyStatus = journeyStatus,
minimumShipLength = minimumShipLength,
journeys = journeys, // Store full objects
refreshedAt = Instant.now(),
expiresAt = Instant.now().plus(1, ChronoUnit.HOURS),
)
journeysCacheDataSource.upsert(cacheEntry)
logger.info { "Updated cache for ${port.unlocode}:$journeyStatus with ${journeys.size} journeys" }
}
}

#### 4.3 Update `refreshJourneysByPort` Method

**BEFORE (lines 271-311):**

kotlinwide760@Scheduled(fixedRateString = "\${cache.journeys-by-port}")
fun refreshJourneysByPort() {
if (cacheInitialized.compareAndSet(false, true)) {
// initiate cache keys for cached ports
for (unlocode in vesselJourneyProperties.cachedUnlocodes) {
journeysByPortCache[
JourneysByPortCacheKey(
unlocode = unlocode,
journeyStatus = JourneyStatus.IN\_ARRIVAL\_PORT,
minimumShipLength = MINIMUM\_SHIP\_LENGTH\_FOR\_JOURNEY\_IN\_METERS,
),
] = emptySet()
journeysByPortCache[
JourneysByPortCacheKey(
unlocode = unlocode,
journeyStatus = JourneyStatus.EN\_ROUTE,
minimumShipLength = MINIMUM\_SHIP\_LENGTH\_FOR\_JOURNEY\_IN\_METERS,
),
] = emptySet()
}
}
iOScope().launch {
val cacheKeys = journeysByPortCache.keys.toList()
val time =
measureTime {
for (key in cacheKeys) {
try {
val journeys =
getJourneysByPortDirect(null, key.unlocode, key.journeyStatus, key.minimumShipLength)
journeysByPortCache[key] = journeys
} catch (e: Exception) {
logger.warn(e) {
"Failed to refresh journeys for $key"
}
}
}
}
logger.info { "JourneyByPort cache is refreshed in $time" }
}
}

**AFTER:**

kotlinwide760@Scheduled(fixedRateString = "\${cache.journeys-by-port}") // Keep same schedule (PT15M or PT30M)
fun refreshJourneysByPort() {
iOScope().launch {
val time =
measureTime {
// Find cache entries that will expire in the next 15 minutes
val entriesToRefresh = journeysCacheDataSource.findExpiringWithin(Duration.ofMinutes(15))
logger.info { "Refreshing ${entriesToRefresh.size} cache entries" }
entriesToRefresh.forEach { entry ->
try {
// Fetch fresh data
val freshJourneys =
getJourneysByPortDirect(
null,
entry.unlocode,
entry.journeyStatus,
entry.minimumShipLength,
)
// Update cache with complete journey objects
val updatedEntry =
entry.copy(
journeys = freshJourneys, // Store full objects
refreshedAt = Instant.now(),
expiresAt = Instant.now().plus(1, ChronoUnit.HOURS),
)
journeysCacheDataSource.upsert(updatedEntry)
logger.debug { "Refreshed cache for ${entry.unlocode}:${entry.journeyStatus} with ${freshJourneys.size} journeys" }
} catch (e: Exception) {
logger.warn(e) {
"Failed to refresh cache for ${entry.unlocode}:${entry.journeyStatus}"
}
}
}
}
logger.info { "JourneyByPort cache refresh completed in $time" }
}
}

---

## ❓ Some Questions

1. Should we keep the `cached-unlocodes` whitelist, or open it up to any port?
2. Is 1 hour TTL appropriate, or should it be configurable? Or should we not add TTL?
3. Should we keep 15-minute refresh, or change to 30 minutes?
4. Should mongodb be populated and updated on startup?