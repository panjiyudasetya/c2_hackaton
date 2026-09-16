---
id: confluence:1277100033
source: confluence
type: page
space: TC
title: Spring Boot 4 Upgrade Guide
author: Darius Wattimena
date: '2026-07-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1277100033
explicit_links:
- jira:UTF-8
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1277100033
---
# Spring Boot 4 Upgrade Guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1277100033  

## Content

This guide describes how to migrate a Teqplay service from Spring Boot 3.x to Spring Boot 4.  
It is based on the tested migrations of **csi-backend** and **skeleton-plugins** (`update-spring-boot-4`  
branches), so everything in sections 1–12 is known to work. Section 13 lists changes from the  
[official Spring Boot 4.0 Migration Guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide) that we did *not* run into in these two repos, but that you may encounter in other services.

## Before you start

* Requirements: **Java 17+**, **Kotlin 2.2+**, Jakarta EE 11 / Servlet 6.1.
* Add the properties migrator while migrating — it reports (and temporarily migrates) renamed or  
  removed configuration properties at startup, including keys coming from Kubernetes configmaps:

  kotlinruntimeOnly("org.springframework.boot:spring-boot-properties-migrator")

  Remove it again once the migration is fully rolled out.

---

## 1. Version bumps

| Dependency | Before | After |
| --- | --- | --- |
| Spring Boot | 3.x | **4.0.7** |
| Kotlin | 1.x | **2.2.20** |
| Spring Cloud (BOM) | 2024.0.x | **2025.1.2** |
| Spring Cloud Kubernetes | 3.2.1 | **5.0.2** |
| springdoc-openapi | 2.8.6 | **3.0.3** |
| MongoDB driver | 4.11.x | **5.8.0** |
| MongoJack | 5.0.2 | **6.0.0** |
| bson4jackson | 2.18.0 | **3.1.0** |
| JUnit | 5.x | **6.0.3** |
| skeleton-plugins | 2.12.x | **3.0.0** |
| KMongo | 5.2.1 | **removed** (KMongo is dead, see §11) |

Notes:

* `io.spring.dependency-management` (`spring_dependencies_version`) is no longer needed when using the Spring Boot Gradle plugin's built-in BOM support — skeleton-plugins removed it entirely.
* The ktlint Gradle plugin (`org.jlleitschuh.gradle.ktlint`) was disabled in our tests to ensure all changes were only related to the spring update and not a ktlint update.
* Add the JUnit launcher explicitly so it stays aligned with the JUnit 6 engine instead of Gradle's  
  bundled launcher:

  kotlintestRuntimeOnly("org.junit.platform:junit-platform-launcher")

### Java Upgrade

Java can be upgraded to **Java 21** without requiring any additional code or configuration changes. Java 21 is fully supported by the targeted Spring version and is the recommended Long-Term Support (LTS) release.

No application code changes are required specifically for the Java version upgrade. However, it is recommended to run the full test suite after upgrading to confirm compatibility with your project's dependencies.

## 2. Renamed and new starters

Spring Boot 4 modularized itself: many features moved out of `spring-boot`/`spring-boot-autoconfigure` into their own modules, so you must depend on them explicitly.

| Before | After |
| --- | --- |
| `spring-boot-starter-web` | `spring-boot-starter-webmvc` |
| `spring-boot-starter-aop` | `spring-boot-starter-aspectj` |
| *(part of web starter)* | `spring-boot-starter-restclient` — **new**, required for `RestTemplateBuilder` / `RestTemplate` |
| `spring-boot-starter-web-services` | `spring-boot-starter-webservices` |

For test code that builds REST clients you may also need:

kotlinwide760testImplementation("org.springframework.boot:spring-boot-starter-webmvc-test")
testImplementation("org.springframework.boot:spring-boot-restclient-test")

Every module that uses `RestTemplateBuilder` needs the restclient module on its classpath  
(`spring-boot-starter-restclient`, or `spring-boot-restclient` if you only need the classes and not the auto-configuration).

## 3. Package relocations (imports)

Mechanical find-and-replace across the codebase:

| Before | After |
| --- | --- |
| `org.springframework.boot.web.client.RestTemplateBuilder` | `org.springframework.boot.restclient.RestTemplateBuilder` |
| `org.springframework.boot.web.client.RootUriTemplateHandler` | `org.springframework.boot.restclient.RootUriTemplateHandler` |
| `org.springframework.boot.actuate.health.Health` | `org.springframework.boot.health.contributor.Health` |
| `org.springframework.boot.actuate.health.HealthIndicator` | `org.springframework.boot.health.contributor.HealthIndicator` |
| `org.springframework.boot.actuate.health.AbstractHealthIndicator` | `org.springframework.boot.health.contributor.AbstractHealthIndicator` |
| `org.springframework.boot.actuate.health.Status` | `org.springframework.boot.health.contributor.Status` |
| `org.springframework.boot.actuate.health.StatusAggregator` | `org.springframework.boot.health.actuate.endpoint.StatusAggregator` |
| `org.springframework.boot.actuate.health.SimpleStatusAggregator` | `org.springframework.boot.health.actuate.endpoint.SimpleStatusAggregator` |
| `org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration` | `org.springframework.boot.amqp.autoconfigure.RabbitAutoConfiguration` |
| `org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc` | `org.springframework.boot.webmvc.test.autoconfigure.AutoConfigureMockMvc` |
| `org.springframework.boot.test.autoconfigure.web.client.AutoConfigureWebClient` | `org.springframework.boot.restclient.test.autoconfigure.AutoConfigureRestClient` (annotation renamed too: `@AutoConfigureWebClient` → `@AutoConfigureRestClient`) |

The actuator endpoint annotations (`@Endpoint`, `@ReadOperation`, …) did **not** move.

If you reference class names as strings (e.g. `@ConditionalOnClass(name = [...])`), update those  
too — skeleton's `HEALTH_INDICATOR_CLASS` constant changed from `org.springframework.boot.actuate.health.HealthIndicator` to `org.springframework.boot.health.contributor.HealthIndicator`.

Auto-configurations also moved to their feature modules. If the module is not on your classpath,  
you can no longer exclude its auto-configuration (and don't need to):

kotlinwide760// Before
@SpringBootApplication(exclude = [MongoAutoConfiguration::class, RabbitAutoConfiguration::class])
// After: Mongo auto-config lives in spring-boot-mongodb, which is not on the classpath here
@SpringBootApplication(exclude = [RabbitAutoConfiguration::class])

## 4. Jackson 2 → Jackson 3

This is the largest part of the migration. Jackson 3 moved to the `tools.jackson` group id and  
package, **except** the annotations, which stay on `com.fasterxml.jackson.annotation` for  
compatibility.

### 4.1 Dependencies

kotlinwide760// Before
implementation("com.fasterxml.jackson.core:jackson-core")
implementation("com.fasterxml.jackson.core:jackson-databind")
implementation("com.fasterxml.jackson.core:jackson-annotations")
implementation("com.fasterxml.jackson.module:jackson-module-kotlin")
implementation("com.fasterxml.jackson.dataformat:jackson-dataformat-yaml")
// After
implementation("tools.jackson.core:jackson-core")
implementation("tools.jackson.core:jackson-databind")
implementation("com.fasterxml.jackson.core:jackson-annotations") // annotations keep the old coordinates!
implementation("tools.jackson.module:jackson-module-kotlin")
implementation("tools.jackson.dataformat:jackson-dataformat-yaml")

### 4.2 Imports

| Before | After |
| --- | --- |
| `com.fasterxml.jackson.core.*` | `tools.jackson.core.*` |
| `com.fasterxml.jackson.databind.*` | `tools.jackson.databind.*` |
| `com.fasterxml.jackson.module.kotlin.*` | `tools.jackson.module.kotlin.*` |
| `com.fasterxml.jackson.annotation.*` | **unchanged** |

### 4.3 The Kotlin `_id` pitfall (⚠ data loss risk)

**Jackson 3 no longer detects Kotlin's** `get_id()` as a getter. Any Kotlin property named `_id`  
(our MongoDB id convention) silently disappears from serialized JSON — and from MongoDB documents — unless you name the property explicitly:

kotlinwide760data class Ship(
@get:JsonProperty("\_id")
val \_id: String,
...
)

Audit **every** model with an `_id` property, including interfaces like `DbObject` ([DbObject.kt](api/src/main/kotlin/nl/teqplay/csi/model/DbObject.kt)) *and* every class that overrides it (the annotation on the interface getter is not inherited by constructor parameters of data classes — annotate both). Verify by serializing a document and checking `_id` is present before deploying anything that writes to MongoDB.

### 4.4 ObjectMapper is immutable — use the builder

`ObjectMapper` can no longer be reconfigured after construction. Replace mutate-in-place chains  
with `JsonMapper.builder()`:

kotlinwide760// Before
val mapper = ObjectMapper()
.disable(DeserializationFeature.FAIL\_ON\_UNKNOWN\_PROPERTIES)
.disable(SerializationFeature.WRITE\_DATES\_AS\_TIMESTAMPS)
.registerModule(ExtendedDateModule())
.registerModule(JavaTimeModule())
.registerKotlinModule()
// After
val mapper = JsonMapper.builder()
.disable(DeserializationFeature.FAIL\_ON\_UNKNOWN\_PROPERTIES)
.configure(DateTimeFeature.WRITE\_DATES\_AS\_TIMESTAMPS, false) // moved to tools.jackson.databind.cfg.DateTimeFeature
.addModule(ExtendedDateModule())
.addModule(kotlinModule())
.build()

* `JavaTimeModule` is built into Jackson 3 — drop the registration.
* `WRITE_DATES_AS_TIMESTAMPS` moved from `SerializationFeature` to `DateTimeFeature`.
* To tweak an injected mapper, rebuild it: `(objectMapper as JsonMapper).rebuild()....build()`.  
  `objectMapper.copy()` + mutation no longer works.
* `ObjectMapper().findAndRegisterModules()` → `JsonMapper.builder().findAndAddModules().build()`.
* Default property inclusion: `.setSerializationInclusion(NON_NULL)` → `.changeDefaultPropertyInclusion { it.withValueInclusion(NON_NULL) }`.
* MongoJack 6: `MongoJackModule.configure(mapper)` now *returns* a new mapper instead of mutating the argument. In csi this is all wrapped in `MongoDbBuilder.configureObjectMapper(objectMapper)` from skeleton — use that instead of configuring MongoJack yourself (see [MongoDbConfiguration.kt](app/base/src/main/kotlin/nl/teqplay/csi/config/MongoDbConfiguration.kt)).

### 4.5 Renamed classes and methods

| Before | After |
| --- | --- |
| `JsonSerializer<T>` | `ValueSerializer<T>` |
| `JsonDeserializer<T>` | `ValueDeserializer<T>` |
| `SerializerProvider` | `SerializationContext` |
| `TextNode` | `StringNode` |
| `deser.std.UUIDDeserializer` | `deser.jdk.UUIDDeserializer` |
| `ser.std.UUIDSerializer` | `ser.jdk.UUIDSerializer` |
| `JsonProcessingException` | `tools.jackson.core.JacksonException` |
| `gen.writeStringField(...)` | `gen.writeStringProperty(...)` |
| `gen.writeNumberField(...)` | `gen.writeNumberProperty(...)` |
| `gen.writeBinaryField(...)` | `gen.writeBinaryProperty(...)` |
| `gen.writeFieldName(...)` | `gen.writeName(...)` |
| `gen.writeObject(x)` | `gen.writePOJO(x)` |
| `node.fieldNames()` | `node.propertyNames()` |
| `node.isContainerNode` | `node.isContainer` |
| `parser.currentToken` (property) | `parser.currentToken()` (method) |
| `parser.codec.readTree(parser)` | `ctxt.readTree(parser)` (codec removed; use the `DeserializationContext`) |

### 4.6 Jackson-related property renames

propertieswide760# Before
spring.jackson.deserialization.read-unknown-enum-values-using-default-value=true
# After — the enum features moved to spring.jackson.datatype.enum
spring.jackson.datatype.enum.read-unknown-enum-values-using-default-value=true

Other `spring.jackson.read.*` / `spring.jackson.write.*` / `spring.jackson.parser.*` keys moved to `spring.jackson.json.read.*` / `spring.jackson.json.write.*` — the properties migrator (see top) flags these at startup.

## 5. RestTemplate nullability

The Kotlin extension functions `RestTemplate.getForObject<T>()` and `postForObject<T>()` now return `T?` instead of `T`. Every call site needs a null-handling decision:

kotlinwide760// Lists: fall back to empty
fun list(): List<ShipRegisterMapping> =
restTemplate.getForObject<Array<ShipRegisterMapping>>(url = "$PREFIX/list")
?.toList() ?: emptyList()
// Required values: fail explicitly
val token = restTemplate.postForObject<TokenResponse>(url)
?: throw InternalErrorException("token response was empty")

Also, reified type parameters on your own generic RestTemplate helpers may now need an upper bound: `inline fun <reified T>` → `inline fun <reified T : Any>`.

`HttpHeaders` also changed (Spring Framework 7):

* `headers.keys` → `headers.headerNames()`
* `headers.containsKey(...)` → `headers.containsHeader(...)`

## 6. Actuator / health indicators

Besides the package moves in §3:

* `Health.Builder.withDetail(key, value)` no longer accepts `null` values — guard them:

  kotlin// Before
  if (e != null) withDetail("error", e.message)
  // After (e.message can be null!)
  e?.message?.let { withDetail("error", it) }
* Actuator endpoint enablement properties were replaced by the *access* model:

  properties# Before
  management.endpoints.enabled-by-default=false
  management.endpoint.health.enabled=true
  # After
  management.endpoints.access.default=none
  management.endpoint.health.access=unrestricted
* Liveness/readiness probes are now enabled by default.
* `management.health.mongo.*` → `management.health.mongodb.*`.

## 7. Spring Security

* `AntPathRequestMatcher` is gone:

  kotlin// Before
  import org.springframework.security.web.util.matcher.AntPathRequestMatcher
  AntPathRequestMatcher(path)
  // After
  import org.springframework.security.web.servlet.util.matcher.PathPatternRequestMatcher
  PathPatternRequestMatcher.withDefaults().matcher(path)

  Note that `PathPattern` syntax is stricter than Ant patterns (`**` is only allowed at the end of a pattern) — review your matchers.
* Framework callback interfaces tightened their nullability (JSpecify). Kotlin overrides that  
  declared parameters as nullable no longer compile, e.g. `AuthenticationEntryPoint.commence(request, response, authException)` — all parameters are non-null now, and `ServerSecurityContextRepository.save(exchange, ...)` takes a non-null `ServerWebExchange`. Remove the `?` and any dead null-guards.

## 8. Testing

* `@MockBean` / `@SpyBean` were removed:

  kotlin// Before
  import org.springframework.boot.test.mock.mockito.MockBean
  @MockBean lateinit var dataSource: ShipRegisterInfoDataSource
  // After
  import org.springframework.test.context.bean.override.mockito.MockitoBean
  @MockitoBean lateinit var dataSource: ShipRegisterInfoDataSource
* `@AutoConfigureMockMvc` moved (see §3), and `@SpringBootTest` no longer auto-provides MockMvc, `WebClient`, or `TestRestTemplate` — add `@AutoConfigureMockMvc`, `@AutoConfigureRestClient`, or `@AutoConfigureTestRestTemplate` explicitly.
* JUnit 6: mostly source-compatible with JUnit 5 for our usage, but add `testRuntimeOnly("org.junit.platform:junit-platform-launcher")`.
* Test `ObjectMapper` setup follows §4.4 (`JsonMapper.builder()...build()`).
* MongoDB driver 5.8: mocks of `MongoDatabase.listCollectionNames()` must return the new  
  `com.mongodb.client.ListCollectionNamesIterable` type instead of a generic `MongoIterable<String>`.

## 9. Web MVC / servlet miscellanea

* `ContentCachingRequestWrapper(request)` single-arg constructor: use `ContentCachingRequestWrapper(request, -1)` (`-1` = unlimited cache).
* SpEL `StandardEvaluationContext.setVariables(map)` no longer accepts maps with nullable values — loop and call `setVariable(name, value)` per entry.

## 10. Skeleton-plugins 3.0.0: removed KMongo modules

Skeleton 3.0.0 **deleted all KMongo-based modules** (KMongo is unmaintained and incompatible with  
the new stack). Migrate to their MongoJack-based `*2` successors:

| Removed module | Replacement |
| --- | --- |
| `datasource` | `datasource2` |
| `datasource-builder` | `datasource-builder2` |
| `datasource-history` | `datasource-history2` |
| `auth-credentials-auth-zero-s2s-server` | `auth-credentials-auth-zero-s2s-server2` |
| `auth-credentials-keycloak-s2s-mongo` | `auth-credentials-keycloak-s2s-mongo2` |
| `auth-credentials-mongo` | **no replacement** — contact the platform team if you still use it |

## 11. Suggested upgrade order

1. Bump versions (§1) and rename starters (§2); add `spring-boot-properties-migrator`.
2. Fix imports (§3) — this is mechanical.
3. Migrate Jackson (§4). Pay special attention to the `_id` pitfall (§4.3) — this is the only  
   change in the whole migration that can silently corrupt data.
4. Fix RestTemplate nullability (§5) — the compiler finds these for you.
5. Fix tests (§8) and properties (§6).
6. Run the full test suite, then start the service locally and check the startup log for  
   properties-migrator warnings.
7. Verify MongoDB writes contain `_id` and health endpoints report correctly before deploying.

## 12. Possible issues not covered by our migration

From the official migration guide — we didn't hit these in csi-backend/skeleton-plugins, but other  
services might:

**Removed features**

* **Undertow** support removed (incompatible with Servlet 6.1) — switch to Tomcat or Jetty.
* Executable-jar launch scripts (`fully executable` jars) removed.
* Spring Session Hazelcast and MongoDB moved out of Spring Session.
* Spock test framework integration removed.
* Spring Retry dependency management removed (Spring Framework 7 has its own retry package).

**More renamed starters/modules**

* Flyway/Liquibase now need explicit starters: `spring-boot-starter-flyway` / `spring-boot-starter-liquibase`.
* OAuth2 starters renamed with a `security-` prefix.
* Spring Batch defaults to in-memory; use `spring-boot-starter-batch-jdbc` for JDBC persistence.
* WAR deployments on Tomcat: use `spring-boot-starter-tomcat-runtime`.
* As a stop-gap you can use `spring-boot-starter-classic` / `spring-boot-starter-test-classic`, which pull in the old aggregate dependency set — useful to get compiling before modularizing properly.

**More Jackson 3 changes**

* `@JsonComponent` → `@JacksonComponent`, `@JsonMixin` → `@JacksonMixin`.
* `Jackson2ObjectMapperBuilderCustomizer` → `JsonMapperBuilderCustomizer`.
* Boot's `JsonObjectSerializer`/`JsonValueDeserializer` → `ObjectValueSerializer`/`ObjectValueDeserializer`.
* If a dependency still needs Jackson 2, `spring-boot-jackson2` exists as a deprecated  
  compatibility module, and `spring.jackson.use-jackson2-defaults=true` restores Jackson 2 default behavior on the Jackson 3 mapper.
* Boot now auto-configures format-specific mappers (`JsonMapper` for JSON, `XmlMapper` for XML); custom mapper beans must match the specific type.

**More package relocations**

* `EnvironmentPostProcessor`: `org.springframework.boot.env` → `org.springframework.boot`.
* `BootstrapRegistry`: `org.springframework.boot` → `org.springframework.boot.bootstrap`.
* `@EntityScan` → `org.springframework.boot.persistence.autoconfigure`.
* `TestRestTemplate` → `org.springframework.boot.resttestclient`.

**More property renames**

* `spring.data.mongodb.*` (connection settings) → `spring.mongodb.*`; MongoDB UUID and BigDecimal representations must now be configured explicitly (`spring.mongodb.representation.uuid`, `spring.data.mongodb.representation.big-decimal`) if you use Spring Data MongoDB.
* `spring.session.redis.*` → `spring.session.data.redis.*` (same for mongodb).
* `spring.dao.exceptiontranslation.enabled` → `spring.persistence.exceptiontranslation.enabled`.

**Behavior changes**

* `org.springframework.lang.Nullable` support removed — migrate to `org.jspecify.annotations.Nullable`.
* `PropertyMapper` no longer calls adapters/predicates for null values; `alwaysApplyingWhenNonNull()` removed.
* Logback default charset is now UTF-8.
* DevTools live reload is disabled by default (`spring.devtools.livereload.enabled=true` to restore).
* `server.forward-headers-strategy` has no effect in WAR deployments — register a `ForwardedHeaderFilter` manually.
* Elasticsearch: low-level `RestClient` replaced by `Rest5Client`; `RestClientBuilderCustomizer` → `Rest5ClientBuilderCustomizer`.

# Projects

**Notes:**

Skeleton plugins is a dependency for every project that's why its excluded from the dependencies column

| full\_name | Team | status | **Dependencies** |
| --- | --- | --- | --- |
| teqplay/skeleton-plugins | Core Components | Done | None |
| teqplay/csi-backend | Core Components | Done | ais-engine |
| teqplay/ais-engine | Core Components |  | poma, vesselvoyage, smartfleet |
| teqplay/vesselvoyage-backend | Core Components |  | csi, poma, ais-engine, eta-predictor |
| teqplay/vesselvoyage-completeness-test-backend | Core Components |  | ais-engine |
| teqplay/poma-backend | Core Components |  | None |
| teqplay/eta-predictor-backend | Core Components |  | csi, routescout, portmatcher, ais-engine |
| teqplay/api | Core Components |  | csi, ais-engine |
| teqplay/csi-agentic-tickets-creator | Core Components |  | none |
| teqplay/routescout-v2-backend | Core Components |  | none |
| teqplay/driftpredictor-backend | Core Components |  | none |
| teqplay/portmatcher-backend | Core Components |  | ais-engine |
| teqplay/customereventpublisher-backend | Core Components |  | poma, ais-engine |
| teqplay/portlocaltime-backend | Core Components |  | none |
| teqplay/skeleton-backend | Core Components |  | none |
| teqplay/area-occupancy | Core Components |  | ais-engine, csi, poma |
| teqplay/service-vessel-analysis | Core Components |  | ais-engine, csi, vesselvoyage |
| teqplay/vesselcompliance-backend | Projects |  | none |
| teqplay/pdatool-backend | Projects |  | none |
| ~~teqplay/chorus-backend~~ | Projects | Gavin said no longer relevant | none |
| teqplay/terminalplanner-backend | Projects |  | none |
| teqplay/portcallplus | Projects |  | csi, ais-engine, smartfleet |
| teqplay/portreporter-backend | Projects |  | csi, smartfleet, vesselvoyage |
| teqplay/smartfleet | Projects |  | csi, vesselvoyage, terminalplanner |
| teqplay/portcallone-backend | Projects |  | ais-engine, vesselvoyage |
| teqplay/shipsparelogistics-backend | Projects |  | portcallplus, portreporter\_portcall\_library |
| teqplay/timeline-backend | Projects |  | ais-engine, vesselvoyage |
| teqplay/sednaintegration-backend | Projects |  | none |
| teqplay/vesselmatcher-backend | Projects |  | none |
| teqplay/nexmoservice-backend | Projects |  | none |
| teqplay/scrapeshark-backend | Projects |  | none |
| teqplay/terminallineup-backend | Projects |  | none |
| teqplay/reporting-jobs | Devops |  | portreporter, portcallplus, csi |