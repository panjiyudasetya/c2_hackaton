---
id: confluence:214106132
source: confluence
type: page
space: TC
title: Spring Boot 2.6 to 3.1 Migration Plan
author: Jamie de Leest
date: '2025-01-28'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214106132
explicit_links:
- github:FasterXML/jackson-module-kotlin:issue:670
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214106132
---
# Spring Boot 2.6 to 3.1 Migration Plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214106132  

## Content

Many steps need to be taken to upgrade to the newest version of Spring Boot 3.1. This plan will highlight all changes required in our applications and libraries.

## 1. General Changes

example commit:

<https://bitbucket.org/teqplay/poma-backend/commits/143306dea080ca33c829b0c3aee674d4f0e4a350>

### 1.1 Java Version

Spring Boot 3.x requires Java 17 or later. All our applications and libraries should be compiled with at least version 17 of Java.

This can be achieved by changing the `jvmTarget` in the KotlinCompile gradle task:

tasks.withType(org.jetbrains.kotlin.gradle.tasks.KotlinCompile).all {
kotlinOptions {
jvmTarget = "17"
...
}
}

We also need to change our CircleCI script. Change the build step to something as follows:

jobs:
build:
docker:
- image: cimg/openjdk:17.0
...

Keep in mind that this might break the existing CI script. If your project used our old custom docker image, you might have to install some dependencies.

### 1.2 Default endpoint behaviour

Endpoints with trailing slashes will break for WebMVC and WebFlux. Meaning frontends could also be affected by this change in behaviour.

To get the old deprecated behaviour, the following configuration should be overridden in the `configurePathMatch`. For WebMVC, this will look as follows:

java@Configuration
public class WebConfiguration implements WebMvcConfigurer {
@Override
public void configurePathMatch(PathMatchConfigurer configurer) {
configurer.setUseTrailingSlashMatch(true);
}
}

If you’re using Spring WebFlux:

java@Configuration
public class WebConfiguration implements WebFluxConfigurer {
@Override
public void configurePathMatching(PathMatchConfigurer configurer) {
configurer.setUseTrailingSlashMatch(true);
}
}

### 1.3 ConstructingBinding in Property Classes

Some projects use property classes in favour of the Konfig library for quite some time. We only need to remove the `@ConstructingBinding` annotation as they are not required anymore for any `@ConfigurationProperties` to work. Besides this, the annotation itself has been moved to a new location, but importing that one will result in the class not compiling as it no longer targets classes.

For example, below, we have the properties class from the Teqplay API:

kotlin@ConstructorBinding <--- This should be removed
@ConfigurationProperties(prefix = "auth.keycloak")
data class KeycloakProperties(
val url: String?,
val realm: String,
val audience: String
)

### 1.4 Prometheus Micrometer Metrics Changes

The `*TagProvider` `*TagContributor` and `*Tags` classes have been deprecated. They are not used by default anymore by the observation instrumentation. The `WebMvcMetricsFilter` has been fully deleted in favour of the `ServerHttpObservationFilter`.

### 1.5 Spring Security

Spring Security will be upgraded from 5 to 6. For the detailed guide, please check out <https://docs.spring.io/spring-security/reference/migration/index.html>.

#### 1.5.1 Package changes

All `javax` import needs to be changed to `jakarta`.

#### 1.5.2 Require Explicit Saving of SecurityContextRepository

In Spring Security 5, the default behaviour is for the `SecurityContext` to automatically be saved to the `SecurityContextRepository` using the `SecurityContextPersistenceFilter`. This has all been changed in Spring Security 6.

In the new behaviour by default, the `SecurityContextHolderFilter` will only read the `SecurityContext` from `SecurityContextRepository` and populate it in the `SecurityContextHolder`. Users now must explicitly save the `SecurityContext` with the `SecurityContextRepository` if they want the `SecurityContext` to persist between requests. This removes ambiguity and improves performance by only requiring writing to the `SecurityContextRepository` (i.e. `HttpSession`) when it is necessary.

To get the old behaviour the following code needs to be added to the `filterChain` bean :

kotlin@Bean
fun filterChain(http: HttpSecurity): SecurityFilterChain {
......
http {
securityContext {
requireExplicitSave = true
}
}
return http.build()
}

### 1.6 Building a Docker image

All our applications make a docker image using the built-in `bootBuildImage`. Setting the `imageName` has been changed if you use the `build.gradle.kts` variant of gradle.

This has been changed from:

tasks.withType<BootBuildImage> {
imageName = generateImageName()
}

To the following:

tasks.withType<BootBuildImage> {
imageName.set(generateImageName())
}

### 1.7 Jackson

With Spring Boot 3.1 the Jackson version has been upgraded to 2.15.

#### 1.7.1 Kotlin Version

The support versions have been changed to 1.5 or later. This means projects with 1.4 or lower need to be upgraded.

#### 1.7.2 Default behaviour of Boolean fields

The default serialization behaviour has been changed with the newest version of Jackson.

> jackson-module-kotlin changes the serialization result of getter-like functions starting with 'is'. For example, a function defined as `fun isValid(): Boolean`, which was previously output with the name `valid`, is now output with the name `isValid` ([KOTLIN#670](https://github.com/FasterXML/jackson-module-kotlin/issues/670)).

This means you have to change all your Booleans starting with the “is“ keyword or add a `@JsonProperty` annotation provided with the expected name of the field.

### 1.8 Spring Cloud

#### 1.8.1 Common

By default, the `spring.cloud.bootstrap.enabled` is set to false. In Spring Boot 3.0 and later, we need to set the variable to `true` so a Kubernetes ConfigMap can be loaded in. Alternatively we can also set `spring.config.import` to `kubernetes:` to add support for this.

#### 1.8.1 Kubernetes

Kubernetes awareness was implemented using the `spring.cloud.kubernetes.enabled` property. This property was removed and is unsupported. Instead, it uses the Spring Boot API: [ConditionalOnCloudPlatform](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/autoconfigure/condition/ConditionalOnCloudPlatform.html). If it is needed to explicitly enable or disable this awareness, use `spring.main.cloud-platform=NONE/KUBERNETES`.

## 2. Skeleton-plugin Changes

The following changes should be done in Skeleton-plugins. However, they can apply to your application as well.

### 2.1 Spring Security

When going from Spring Boot 2.6 to 2.7, they’ve deprecated the `WebSecurityConfigurerAdapter`. We use this adapter to set our CORS, authorized endpoints, and more. However, this has been entirely removed in 3.0 in favour of the `SecurityFilterChain` bean, which needs to be created in a configuration class.

note

If you are overriding this adapter yourself, then applying this step is necessary for you to follow!

If you are overriding this adapter yourself, then applying this step is necessary for you to follow!

You will end up with something as follows:

kotlin @Bean
fun configure(http: HttpSecurity): SecurityFilterChain {
http.authorizeHttpRequests { requests ->
requests.requestMatchers(AntPathRequestMatcher("/openapi/openapi.yml"))
.permitAll()
.anyRequest()
.authenticated()
}.httpBasic()
return http.build()
}

### 2.2 Auto Configuration Classes

Spring Boot 3.x support for the `META-INF/spring.factories` file has been removed. This means all libraries that use autoconfiguration will break. This has been moved to the new `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` file.

## 3. Planning

|  | **Backend Name** | **Status** | **Notes** | **Should know something about** |
| --- | --- | --- | --- | --- |
| 1 | Api | Done |  | Darius/Michel |
| 2 | DriftingPredictor | Done |  | Rowdey/Darius |
| 3 | Poma | Done |  | JoostD |
| 4 | CSI | Running on DEV awaiting testing | is dependent the internal api rest template from ais engine  ~~so ais engine needs to be updated first~~  ~~the internal api rest template is to be moved teqplay api to resolve this dependency~~  apparently the rest template was already moved to skeleton plugins but it was package was called ais-engine what was causing confusion | Michel |
| 5 | Routescout | Running on DEV awaiting release |  | JoostD |
| 6 | VesselVoyage | wait for new year |  | Darius/LeonJ |
| 7 | SmartFleet | Running on DEV awaiting testing | used konfig  changed the auth0 configuration for vesselvoyage to keycloak | Joaquin/Darius |
| 8 | PortcallPlus | In progress/ blocked by csi & ais-engine | Used konfig is dependent on the ship registrer client from csi  is also dependent on ais engine for nats stream  so csi and ais-engine needs to be updated first | Joaquin/Shan/Darius |
| 9 | PortReporter | Running on DEV awaiting release | Used konfig,  fix with joaquin: fixed | Joaquin/Shan |
| 10 | PortPublisher | NOT MIGRATING |  | ? |
| 11 | PortSupport | NOT MIGRATING |  | ? |
| 12 | Bunkerplanner | wait for chorus phase 4 |  | LeonJ |
| 13 | Fuelboss | NOT MIGRATING |  | LeonJ/JoostD |
| 14 | CargoOptima | Running on DEV awaiting testing |  | Joaquin |
| 15 | FunctionalMonitoring | Running on DEV awaiting testing |  | Darius |
| 16 | PDA Tool | Running on DEV awaiting testing |  | Pim/Darius |
| 17 | PDF renderer | NOT MIGRATING |  | ? |
| 18 | DataStore | Running on DEV awaiting testing |  | LeonJ |
| 19 | VesselMatcher | skipped for now GraphQL would need to be removed | uses GraphQL that needs to be replaced | LeonJ/Darius |
| 20 | VesselCompliance | wait for navista phase 2 |  | LeonJ/Joaquin |
| 21 | TerminalPlanner | Running on DEV awaiting testing |  | Gavin |
| 22 | PortLocalTime | Done |  | Darius |
| 23 | ShipSpareLogistics | In progress/ blocked by Portcall+ | Used konfig is dependent on portcall client from Portcall+ | Michel |
| 24 | TerminalLineup | NOT MIGRATING |  | Darius |
| 25 | ScrapeShark | Running on DEV awaiting testing | Used konfig | Darius/Joaquin |
| 26 | AisEngine |  |  | Michel/Darius |
| 27 | PortMatcher | Running on DEV awaiting testing |  | JoostD/Darius  Not really part of AisEngine but very entangled as it is basically a Monitor. |
| 28 | AisStream | Running on DEV awaiting testing |  |  |
| 29 | AisRabbitMQ | Running on DEV awaiting testing |  |  |
| 30 | ShipHistory | Running on DEV awaiting testing |  |  |
| 31 | ShipHistoryProcessor | Running on DEV awaiting testing |  |  |
| 32 | AisDiff | Running on DEV awaiting testing |  |  |
| 33 | AreaMonitor | Running on DEV awaiting testing |  |  |
| 34 | BerthMonitor | Running on DEV awaiting testing |  |  |
| 35 | EncounterMonitor | Running on DEV awaiting testing |  |  |
| 36 | StopMonitor | Running on DEV awaiting testing |  |  |
| 37 | EventHistory | Running on DEV awaiting testing |  |  |
| 38 | EventHistoryProcessor | Running on DEV awaiting testing |  |  |
| 39 | EventConverter | Running on DEV awaiting testing |  |  |
| 40 | Revents |  |  |  |