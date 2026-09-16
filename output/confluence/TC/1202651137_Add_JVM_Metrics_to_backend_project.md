---
id: confluence:1202651137
source: confluence
type: page
space: TC
title: Add JVM Metrics to backend project
author: Joost Laurman
date: '2026-05-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1202651137
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1202651137
---
# Add JVM Metrics to backend project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1202651137  

## Content

Add into `build.gradle`

groovywide760// Prometheus metrics
implementation "io.micrometer:micrometer-registry-prometheus"

Add to your projects helm `values.yaml`

yamlwide760podAnnotations:
prometheus.io/scrape: "true"
prometheus.io/path: /actuator/prometheus
prometheus.io/port: "8080"

Whitelist endpoints, if authentication is enabled, e.g.

kotlinwide760fun authorizationConfigurer(): AuthorizationConfigurer =
AuthorizationConfigurer(
AUTH\_PATHS + SWAGGER\_PATHS + listOf(
"/actuator/health"
"/actuator/health",
"/actuator/prometheus"
)
)

Add these values to your `application.yml`

yamlwide760management.metrics.enable.jvm: true
management.endpoints.web.exposure.include: health,prometheus