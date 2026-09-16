---
id: confluence:566132748
source: confluence
type: page
space: TC
title: Managing Cluster configurations
author: Minh Trang Nguyen (Unlicensed)
date: '2025-06-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/566132748
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/566132748
---
# Managing Cluster configurations

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/566132748  

## Content

**Status:** work in progress

The current architectural approach across deployments involves maintaining individual ConfigMaps for each service, which store base URLs for both internal cluster applications (Develop) and external services (Production). This decentralized configuration strategy has led to a redundant pattern where identical URL configurations are replicated across multiple ConfigMaps.

This approach introduces several potential challenges:

1. Every change to the domain URL is potentially an outage risk for the PRODUCTION cluster.
2. Configuration Redundancy: The same URL values are stored multiple times, increasing the risk of inconsistent or outdated information.
3. Maintenance Complexity: When a service's base URL needs to change, administrators must update multiple ConfigMaps, creating a labor-intensive and error-prone process.
4. Lack of Single Source of Truth: Without a centralized configuration management strategy, it becomes difficult to ensure uniform and consistent URL references across the entire system.

By consolidating these configuration details into a centralized configuration service, we can achieve a more streamlined, manageable, and reliable approach to managing service endpoints within our Kubernetes environment.

## Trigger to replace URLs

Having both the Development and Production clusters within the same root environment could present significant risks to the company.

## Replacing Application URLs

Replacing existing application URLs with new ones can disrupt functionality and is therefore not recommended. A safer approach is to add a new host with the desired domain URL to the Ingress configuration. This allows the application to support both the old and new domain URLs simultaneously, ensuring a smooth transition without breaking existing functionality.

## Domain URL for Develop

The use of a single domain for both development and production environments can cause issues, particularly when updating DNS records, as changes can impact both environments. The proposal is to have a dedicated domain URL for development, which can be used for both private and public IP addresses.

* Adding a DEVELOP domain means extra maintenance, such as replacing the SSL certificate for DEVELOP in the same way as for PRODUCTION.
* The developer should see immediately that it’s about a developer’s URL.

Example:

test.dev.teqplay.com

See document Managing DNS records for more information about managing DNS records.

## Current configuration DEVELOP cluster

The table below lists the configurations for the “teqplay.nl” domain, which should be kept separate from the PRODUCTION cluster.

**An 'x' in the 'Updated' column indicates that the changes have been applied to the DEVELOP cluster.**

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-core | ais-stream-dev | hostname: backenddev.teqplay.nl | hostname: cannot change! |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | ais-rabbitmq-dev | **amqp.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/AisStreaming | **amqp.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/AisStreaming | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | anchor-monitor-dev | **poma.domain**: keycloakdev.teqplay.nl | **poma.domain**: keycloak.dev.teqplay.com |  |
| ais-processing | anchor-monitor-dev | **poma.url**: https://backendpomadev.teqplay.nl/ | **poma.url**: https://backendpoma.dev.teqplay.com/ | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | area-monitor-dev | **poma**:  **url**: https://backendpomadev.teqplay.nl | **poma**:  **url**: https://backendpoma.dev.teqplay.com | x |
| ais-processing | area-monitor-dev | **poma**:  **domain**: keycloakdev.teqplay.nl | **poma**:  **domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | berth-monitor-dev | **internal-api.domain**: keycloakdev.teqplay.nl | **internal-api.domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | encounter-monitor-dev | **csi.domain**: keycloakdev.teqplay.nl | **csi.domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | event-converter-dev | **event**:  **rabbitmq**:  **incoming**:  **uri**: amqps://<username:pass>@rabbitmqdev.teqplay.nl:5671/TeqplayEventsDev | **event**:  **rabbitmq**:  **incoming**:  **uri**: amqps://<username:pass>@rabbitmq.dev.teqplay.com:5671/TeqplayEventsDev | x |
| ais-processing | event-converter-dev | **event**:  **rabbitmq**:  **outgoing**:  **uri**: amqps://<username:pass>@rabbitmqdev.teqplay.nl:5671/TeqplayEventsDev | **event**:  **rabbitmq**:  **outgoing**:  **uri**: amqps://<username:pass>@rabbitmq.dev.teqplay.com:5671/TeqplayEventsDev | x |
| ais-processing | event-converter-dev | **poma**:  **url**: https://backendpomadev.teqplay.nl | **poma**:  **url**: https://backendpoma.dev.teqplay.com | x |
| ais-processing | event-converter-dev | **poma**:  **domain**: keycloakdev.teqplay.nl | **poma**:  **domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | event-history-dev | **poma**:  **url**: https://backendpomadev.teqplay.nl | **poma**:  **url**: https://backendpoma.dev.teqplay.com | x |
| ais-processing | event-history-dev | **poma**:  **domain**: keycloakdev.teqplay.nl | **poma**:  **domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| ais-processing | ship-history-dev | **archive**:  **platform**:  **ship**:  **mmsi**:  **name**: aisdata.teqplay.nl | **archive**:  **platform**:  **ship**:  **mmsi**:  **name**: aisdata.teqplay.nl |  |
| ais-processing | ship-history-dev | **archive**:  **platform**:  **ship**:  **mmsi**:  **name**: aisdata.teqplay.nl | **archive**:  **platform**:  **ship**:  **mmsi**:  **name**: aisdata.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| core-service | csi-internal-dev | **aisStreaming.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/AisStreaming | **aisStreaming.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/AisStreaming | x |
| core-service | csi-internal-dev | **auth-credentials-auth0.audience**: csibackend.teqplay.nl | **auth-credentials-auth0.audience**: csibackend.teqplay.nl |  |
| core-service | csi-internal-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |
| core-service | csi-internal-dev | **poma.domain**: keycloakdev.teqplay.nl | **poma.domain**: keycloak.dev.teqplay.com |  |
| core-service | csi-internal-dev | **poma.url**: https://backendpomadev.teqplay.nl/ | **poma.url**: https://backendpoma.dev.teqplay.com/ | x |
| core-service | csi-internal-dev | **sync.prod.domain**: keycloak.teqplay.nl | **sync.prod.domain**: keycloak.teqplay.nl |  |
| core-service | csi-internal-dev | **sync.prod.url**: https://csibackend-internal.teqplay.nl | **sync.prod.url**: https://csibackend-internal.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| core-service | csi-query-dev | **auth-credentials-auth0.audience**: csibackend.teqplay.nl | **auth-credentials-auth0.audience**: csibackend.teqplay.nl |  |
| core-service | csi-query-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| core-service | poma-dev | **auth-credentials-auth0-s2s.audience**: https://pomadev.teqplay.nl | **auth-credentials-auth0-s2s.audience**: https://poma.dev.teqplay.com |  |
| core-service | poma-dev | **auth-credentials-auth0.audience**: https://pomadev.teqplay.nl | **auth-credentials-auth0.audience**: https://poma.dev.teqplay.com |  |
| core-service | poma-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |
| core-service | poma-dev | **cors.allowed-origins**: https://pomadev.teqplay.nl ,http://localhost:3000,https://localhost:3000,https://timeline-publicdev.teqplay.nl | **cors.allowed-origins**: https://poma.dev.teqplay.com ,http://localhost:3000,https://localhost:3000,https://timeline-public.dev.teqplay.com | x |
| core-service | poma-dev | **sync.prod.url**: https://backendpoma.teqplay.nl | **sync.prod.url**: https://backendpoma.teqplay.nl |  |
| core-service | poma-dev | **sync.prod.domain**: keycloak.teqplay.nl | **sync.prod.domain**: keycloak.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| core-service | poma-sandbox | **auth-credentials-auth0-s2s.audience**: https://poma.teqplay.nl | **auth-credentials-auth0-s2s.audience**: https://poma.teqplay.nl |  |
| core-service | poma-sandbox | **auth-credentials-auth0.audience**: https://pomadev.teqplay.nl | **auth-credentials-auth0.audience**: https://poma.dev.teqplay.com |  |
| core-service | poma-sandbox | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.nl |  |
| core-service | poma-sandbox | **cors.allowed-origins**: https://pomasandbox.teqplay.nl ,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://pomasandbox.teqplay.nl ,http://localhost:3000,https://localhost:3000,https://pomasandbox.dev.teqplay.com | x |
| core-service | poma-sandbox | sync.dev.url: https://backendpomadev.teqplay.nl | sync.dev.url: https://backendpoma.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| core-service | portmatcher-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |
| core-service | portmatcher-dev | **cors.allowed-origins**: https://onthemapdev.teqplay.nl | **cors.allowed-origins**: https://onthemap.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** |  |
| --- | --- | --- | --- | --- |
| core-service | routescout-graph-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |
| core-service | routescout-graph-dev | **auth-credentials-keycloak.domain**: https://keycloakdev.teqplay.nl/auth | **auth-credentials-keycloak.domain**: https://keycloak.dev.teqplay.com/auth |  |
| core-service | routescout-graph-dev | **keycloak.routescout.domain**: keycloak.teqplay.nl | **keycloak.routescout.domain**: keycloak.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| core-service | routescout-route-planning-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |
| core-service | routescout-route-planning-dev | **auth-credentials-keycloak.domain**: https://keycloakdev.teqplay.nl/auth | **auth-credentials-keycloak.domain**: https://keycloak.dev.teqplay.com/auth |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | datastore-dev | **application.backendUrl**: https://datastorebackenddev.teqplay.nl | **application.backendUrl**: https://datastorebackend.dev.teqplay.com | x |
| customer-apps | datastore-dev | **application.frontendUrl**: https://datastoredev.teqplay.nl | **application.frontendUrl**: https://datastore.dev.teqplay.com |  |
| customer-apps | datastore-dev | **auth-credentials-auth0.audience**: https://datastoredev.teqplay.nl | **auth-credentials-auth0.audience**: https://datastore.dev.teqplay.com |  |
| customer-apps | datastore-dev | **cors.allowed-origins**: http://localhost:3000,https://localhost:3000,https://datastoredev.teqplay.nl,http://datastoredev.teqplay.nl | **cors.allowed-origins**: http://localhost:3000,https://localhost:3000,https://datastoredev.teqplay.nl,http://datastore.dev.teqplay.com |  |
| customer-apps | datastore-dev | **datascience.python.hostname**: https://datasciencebackenddev.teqplay.nl | **datascience.python.hostname**: https://datasciencebackend.dev.teqplay.com | x |
| customer-apps | datastore-dev | **datascience.r.hostName**: https://datasciencedev.teqplay.nl | **datascience.r.hostName**: https://datascience.dev.teqplay.com |  |
| customer-apps | datastore-dev | **platform.url**: https://backendglobaldev.teqplay.nl (NOT FOUND) | **platform.url**: https://backendglobal.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | portsupport-dev (deprecated) | **cors.allowed-origins**: https://portsupportdev.teqplay.nl ,https://portsupport.teqplay.nl ,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://portsupport.dev.teqplay.com ,https://portsupport.teqplay.nl ,http://localhost:3000,https://localhost:3000 |  |
| customer-apps | portsupport-dev (deprecated) | **vesselvoyage.audience**: https://vesselvoyagedev.teqplay.nl | **vesselvoyage.audience**: https://vesselvoyage.dev.teqplay.com |  |
| customer-apps | portsupport-dev (deprecated) | **vesselvoyage.url**: https://backendvesselvoyagedev.teqplay.nl | **vesselvoyage.url**: https://backendvesselvoyage.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | shipsparelogistics-dev | **cors.allowed-origins**: http://localhost,http://localhost:3000,http://localhost:8080,http://172.31.22.167:8080,http://alongsidemonitordev.teqplay.nl,https://alongsidemonitor.teqplay.nl,https://alongsidemonitordev.teqplay.nl ,https://portsupport.teqplay.nl ,https://backendssldev.teqplay.nl | **cors.allowed-origins**: http://localhost,http://localhost:3000,http://localhost:8080,http://172.31.22.167:8080,http://alongsidemonitor.dev.teqplay.com ,https://alongsidemonitor.teqplay.nl ,https://alongsidemonitor.dev.teqplay.com ,https://portsupport.teqplay.nl ,https://backendssl.dev.teqplay.com | x |
| customer-apps | shipsparelogistics-dev | **internal-api.domain**: keycloakdev.teqplay.nl | **internal-api.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | shipsparelogistics-dev | **portreporter.domain**: https://keycloakdev.teqplay.nl | **portreporter.domain**: https://keycloak.dev.teqplay.com |  |
| customer-apps | shipsparelogistics-dev | **portreporter.keycloak-url**: https://keycloakdev.teqplay.nl/auth | **portreporter.keycloak-url**: https://keycloak.dev.teqplay.com/auth |  |
| customer-apps | shipsparelogistics-dev | **portreporter.url**: https://backendportreporterdev.teqplay.nl | **portreporter.url**: https://backendportreporter.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | terminalplanner-dev | **amqp.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/TeqplayEventsDev | **amqp.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/TeqplayEventsDev | x |
| customer-apps | terminalplanner-dev | **platform.auth.url**: https://backenddev.teqplay.nl | **platform.auth.url**: https://backend.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | vesselcompliance-dev | **cors.allowed-origins**: https://vesselcompliancedev.teqplay.nl ,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://vesselcompliance.dev.teqplay.com ,http://localhost:3000,https://localhost:3000 |  |
| customer-apps | vesselcompliance-dev | **csi.domain**: keycloakdev.teqplay.nl | **csi.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-dev | **csi.url**: https://csibackenddev.teqplay.nl | **csi.url**: https://csibackend.dev.teqplay.com | x |
| customer-apps | vesselcompliance-dev | **poma.domain**: keycloakdev.teqplay.nl | **poma.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-dev | **poma.url**: https://backendpomadev.teqplay.nl | **poma.url**: https://backendpoma.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | vesselcompliance-poc | **application.frontendUrl**: https://navistademo.teqplay.nl | **application.frontendUrl**: https://navistademo.teqplay.nl |  |
| customer-apps | vesselcompliance-poc | **cors.allowed-origins**: https://navistademo.teqplay.nl,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://navistademo.teqplay.nl ,http://localhost:3000,https://localhost:3000 |  |
| customer-apps | vesselcompliance-poc | **csi.domain**: keycloakdev.teqplay.nl | **csi.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-poc | **csi.url**: https://csibackenddev.teqplay.nl | **csi.url**: https://csibackend.dev.teqplay.com | x |
| customer-apps | vesselcompliance-poc | **poma.url**: https://backendpomadev.teqplay.nl | **poma.url**: https://backendpoma.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | vesselcompliance-staging | **application.frontendUrl**: https://vesselcompliancestaging.teqplay.nl | **application.frontendUrl**: https://vesselcompliancestaging.dev.teqplay.com |  |
| customer-apps | vesselcompliance-staging | **cors.allowed-origins**: https://vesselcompliancestaging.teqplay.nl ,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://vesselcompliancestaging.dev.teqplay.com ,http://localhost:3000,https://localhost:3000 |  |
| customer-apps | vesselcompliance-staging | **csi.domain**: keycloakdev.teqplay.nl | **csi.domain**: keycloak.dev.teqplay.nl |  |
| customer-apps | vesselcompliance-staging | **csi.url**: https://csibackenddev.teqplay.nl | **csi.url**: https://csibackend.dev.teqplay.com | x |
| customer-apps | vesselcompliance-staging | **poma.domain**: keycloakdev.teqplay.nl | **poma.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-staging | **poma.url**: https://backendpomadev.teqplay.nl | **poma.url**: https://backendpoma.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| general-service | datascience-dev | **CSI\_AUTH\_URL**: https://keycloak.teqplay.nl | **CSI\_AUTH\_URL**: https://keycloak.teqplay.nl |  |
| general-service | datascience-dev | **CSI\_URL**: https://csibackend.teqplay.nl | **CSI\_URL**: https://csibackend.teqplay.nl |  |
| general-service | datascience-dev | **PDF\_AUTH\_URL**: https://keycloakdev.teqplay.nl | **PDF\_AUTH\_URL**: https://keycloak.dev.teqplay.com |  |
| general-service | datascience-dev | **PDF\_URL**: https://pdfrendererdev.teqplay.nl/v1 | **PDF\_URL**: https://pdfrenderer.dev.teqplay.com/v1 | x |
| general-service | datascience-dev | **POMA\_AUTH\_URL**: https://keycloak.teqplay.nl | **POMA\_AUTH\_URL**: https://keycloak.teqplay.nl |  |
| general-service | datascience-dev | **POMA\_URL**: https://backendpoma.teqplay.nl | **POMA\_URL**: https://backendpoma.teqplay.nl |  |
| general-service | datascience-dev | **PTO\_AUTH\_URL**: https://keycloakdev.teqplay.nl | **PTO\_AUTH\_URL**: https://keycloak.dev.teqplay.com |  |
| general-service | datascience-dev | **PTO\_URL**: https://pto-etldev.teqplay.nl | **PTO\_URL**: https://pto-etl.dev.teqplay.com | x |
| general-service | datascience-dev | **VESSELVOYAGE\_AUTH\_URL**: https://keycloak.teqplay.nl | **VESSELVOYAGE\_AUTH\_URL**: https://keycloak.teqplay.nl |  |
| general-service | datascience-dev | **VESSELVOYAGE\_URL**: https://backendvesselvoyage.teqplay.nl | **VESSELVOYAGE\_URL**: https://backendvesselvoyage.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| general-service | functionalmonitoring-dev | **amqp.incoming.portreporting.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/PortReporterDev | **amqp.incoming.portreporting.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/PortReporterDev | x |
| general-service | functionalmonitoring-dev | **amqp.incoming.prediction.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/TeqplayEventsDev | **amqp.incoming.prediction.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/TeqplayEventsDev | x |
| general-service | functionalmonitoring-dev | **cors.allowed-origins**: https://grafana.teqplay.nl,https://grafanadev.teqplay.nl | **cors.allowed-origins**: https://grafana.teqplay.nl,https://grafana.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| general-service | pdfrenderer-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |
| general-service | pdfrenderer-dev | **static.baseUrl**: https://pdfrendererdev.teqplay.nl | **static.baseUrl**: https://pdfrenderer.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| general-service | scrapeshark-dev | **amqp.outgoing.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/ScrapesharkDev | **amqp.outgoing.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/ScrapesharkDev | x |
| general-service | scrapeshark-dev | **keycloak.portmatcher.domain**: keycloakdev.teqplay.nl | **keycloak.portmatcher.domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| general-service | terminallineup-dev | **auth-credentials-keycloak-s2s.domain**: keycloakdev.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.dev.teqplay.com |  |
| general-service | terminallineup-dev | **platform.url**: https://backenddev.teqplay.nl | **platform.url**: https://backend.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| portcall | portcallplus-dev | **cors.allowed-origins**: https://zabbix.teqplay.nl | **cors.allowed-origins**: https://zabbix.teqplay.nl |  |
| portcall | portcallplus-dev | **internal-api.domain**: keycloakdev.teqplay.nl | **internal-api.domain**: keycloak.dev.teqplay.com |  |
| portcall | portcallplus-dev | **poma.url**: https://backendpomadev.teqplay.nl/ | **poma.url**: https://backendpoma.dev.teqplay.com/ | x |
| portcall | portcallplus-dev | **rabbitmq.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/TeqplayEventsDev | **rabbitmq.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/TeqplayEventsDev | x |
| portcall | portcallplus-dev | **smartfleet.eta.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/SmartFleetDev | **smartfleet.eta.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/SmartFleetDev | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| portcall | portpublisher-dev | **amqp.incoming.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/PortReporterDev | **amqp.incoming.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/PortReporterDev | x |
| portcall | portpublisher-dev | **auth-credentials-auth0-s2s.audience**: https://portpublisher.teqplay.nl (NOT FOUND) | **auth-credentials-auth0-s2s.audience**: https://portpublisher.teqplay.nl (NOT FOUND) |  |
| portcall | portpublisher-dev | **auth-credentials-auth0.audience**: https://portpublisher.teqplay.nl (NOT FOUND) | **auth-credentials-auth0.audience**: https://portpublisher.teqplay.nl (NOT FOUND) |  |
| portcall | portpublisher-dev | **portcall-plus.url**: https://portcallplusdev.teqplay.nl/ | **portcall-plus.url**: https://portcallplus.dev.teqplay.com/ | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| portcall | portreporter-dev | **auth-credentials-keycloak.domain**: https://keycloakdev.teqplay.nl/auth | **auth-credentials-keycloak.domain**: https://keycloak.dev.teqplay.com/auth |  |
| portcall | portreporter-dev | **authenticator.url**: https://backenddev.teqplay.nl/authenticator/ | **authenticator.url**: https://backend.dev.teqplay.com/authenticator/ |  |
| portcall | portreporter-dev | **csi.domain**: keycloakdev.teqplay.nl | **csi.domain**: keycloak.dev.teqplay.com |  |
| portcall | portreporter-dev | **csi.url**: https://csibackenddev.teqplay.nl | **csi.url**: https://csibackend.dev.teqplay.com | x |
| portcall | portreporter-dev | **externalConnection.exact.redirectUri**: https://backendportreporterdev.teqplay.nl/v1/exact/oauth | **externalConnection.exact.redirectUri**: https://backendportreporter.dev.teqplay.com/v1/exact/oauth | x |
| portcall | portreporter-dev | **externalConnection.keyCloak.portreporter.url**: https://portreporterdev.teqplay.nl/ | **externalConnection.keyCloak.portreporter.url**: https://portreporter.dev.teqplay.com/ | don’t change it, this is a frontend |
| portcall | portreporter-dev | **externalConnection.keyCloak.url**: https://keycloakdev.teqplay.nl/auth/ | **externalConnection.keyCloak.url**: https://keycloak.dev.teqplay.nl/auth/ |  |
| portcall | portreporter-dev | **externalConnection.lineUp.url**: https://backendterminallineupdev.teqplay.nl | **externalConnection.lineUp.url**: https://backendterminallineup.dev.teqplay.com | x |
| portcall | portreporter-dev | **externalConnection.lineup.url**: https://backendterminallineupdev.teqplay.nl | **externalConnection.lineup.url**: https://backendterminallineup.dev.teqplay.com | x |
| portcall | portreporter-dev | **externalConnection.portcallPlusUrl**: https://portcallplusdev.teqplay.nl | **externalConnection.portcallPlusUrl**: https://portcallplus.dev.teqplay.com | x |
| portcall | portreporter-dev | **externalConnection.smartFleetUrl**: https://backendsmartfleetdev.teqplay.nl | **externalConnection.smartFleetUrl**: https://backendsmartfleet.dev.teqplay.com | x |
| portcall | portreporter-dev | **internalConnection.backendBaseUrl**: https://backendportreporterdev.teqplay.nl | **internalConnection.backendBaseUrl**: https://backendportreporter.dev.teqplay.com | need to change with exact redirect |
| portcall | portreporter-dev | **internalConnection.baseUrl**: https://portreporterdev.teqplay.nl | **internalConnection.baseUrl**: https://portreporter.dev.teqplay.com |  |
| portcall | portreporter-dev | **poma.domain**: keycloakdev.teqplay.nl | **poma.domain**: keycloak.dev.teqplay.com |  |
| portcall | portreporter-dev | **poma.url**: https://backendpomadev.teqplay.nl | **poma.url**: https://backendpoma.dev.teqplay.com | x |
| portcall | portreporter-dev | **rabbitmq.nominationsQueue.uri**: amqps://<user:pass@rabbitmqdev.teqplay.nl:5671/ScrapesharkDev | **rabbitmq.nominationsQueue.uri**: amqps://<user:pass@rabbitmq.dev.teqplay.com:5671/ScrapesharkDev | x |
| portcall | portreporter-dev | **rabbitmq.smartFleetQueue.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/SmartFleetDev | **rabbitmq.smartFleetQueue.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/SmartFleetDev | x |
| portcall | portreporter-dev | **rabbitmq.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/PortReporterDev | **rabbitmq.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/PortReporterDev | x |
| portcall | portreporter-dev | **vesselvoyage.url**: https://backendvesselvoyagedev.teqplay.nl | **vesselvoyage.url**: https://backendvesselvoyage.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| portcall | portreporter-monitor-dev | url: https://backendpomadev.teqplay.nl | url: https://backendpoma.dev.teqplay.com | x |
| portcall | portreporter-monitor-dev | domain: keycloakdev.teqplay.nl | domain: keycloak.dev.teqplay.com |  |
| portcall | portreporter-monitor-dev | url: https://csibackenddev.teqplay.nl/ | url: https://csibackend.dev.teqplay.com/ | x |
| portcall | portreporter-monitor-dev | uri: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/PortReporterDev | uri: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/PortReporterDev | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| portcall | portreporter-testing | **authenticator.url**: https://backenddev.teqplay.nl/authenticator/ | **authenticator.url**: https://backend.dev.teqplay.com/authenticator/ |  |
| portcall | portreporter-testing | **externalConnection.keyCloak.portreporter.url**: https://portreporter-temp.teqplay.nl/ | **externalConnection.keyCloak.portreporter.url**: https://portreporter-temp.dev.teqplay.com/ |  |
| portcall | portreporter-testing | **externalConnection.keyCloak.url**: https://keycloakdev.teqplay.nl/auth/ | **externalConnection.keyCloak.url**: https://keycloak.dev.teqplay.nl/auth/ |  |
| portcall | portreporter-testing | **externalConnection.portcallPlusUrl**: https://portcallplusdev.teqplay.nl | **externalConnection.portcallPlusUrl**: https://portcallplus.dev.teqplay.com | x |
| portcall | portreporter-testing | **rabbitmq.smartFleetQueue.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/SmartFleetDev | **rabbitmq.smartFleetQueue.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/SmartFleetDev | x |
| portcall | portreporter-testing | **rabbitmq.uri**: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/PortReporterDev | **rabbitmq.uri**: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/PortReporterDev | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| pto | pto-etl-dev | **cors.allowed-origins**: https://ptodev.teqplay.nl ,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://pto.dev.teqplay.com ,http://localhost:3000,https://localhost:3000 |  |
| pto | pto-etl-dev | **csi.domain**: keycloak.teqplay.nl | **csi.domain**: keycloak.teqplay.nl |  |
| pto | pto-etl-dev | **csi.url**: https://csibackend.teqplay.nl | **csi.url**: https://csibackend.teqplay.nl |  |
| pto | pto-etl-dev | **poma.domain**: keycloak.teqplay.nl | **poma.domain**: keycloak.teqplay.nl |  |
| pto | pto-etl-dev | **poma.url**: https://backendpoma.teqplay.nl | **poma.url**: https://backendpoma.teqplay.nl |  |
| pto | pto-etl-dev | **portreporter.url**: https://backendportreporter.teqplay.nl | **portreporter.url**: https://backendportreporter.teqplay.nl |  |
| pto | pto-etl-dev | **revents.domain**: keycloakdev.teqplay.nl | **revents.domain**: keycloak.dev.teqplay.com |  |
| pto | pto-etl-dev | **revents.url**: https://reventsbackenddev.teqplay.nl | **revents.url**: https://reventsbackend.dev.teqplay.com | x |
| pto | pto-etl-dev | **vesselvoyage.domain**: keycloak.teqplay.nl | **vesselvoyage.domain**: keycloak.teqplay.nl |  |
| pto | pto-etl-dev | **vesselvoyage.url**: https://backendvesselvoyage.teqplay.nl | **vesselvoyage.url**: https://backendvesselvoyage.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| revents-core | revents-engine-api | **csi**:  **url**: https://csibackend.teqplay.nl | **csi**:  **url**: https://csibackend.teqplay.nl |  |
| revents-core | revents-engine-api | **csi**:  **domain**: keycloak.teqplay.nl | **csi**:  **domain**: keycloak.teqplay.nl |  |
| revents-core | revents-engine-api | **poma**:  **url**: https://backendpoma.teqplay.nl | **poma**:  **url**: https://backendpoma.teqplay.nl |  |
| revents-core | revents-engine-api | **poma**:  **domain**: keycloak.teqplay.nl | **poma**:  **domain**: keycloak.teqplay.nl |  |
| revents-core | revents-engine-api | **vesselvoyage**:  **url**: https://backendvesselvoyagedev-processing.teqplay.nl | **vesselvoyage**:  **url**: https://backendvesselvoyage-processing.dev.teqplay.com | x |
| revents-core | revents-engine-api | **vesselvoyage**:  **domain**: keycloakdev.teqplay.nl | **vesselvoyage**:  **domain**: keycloak.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| revents-core | revents-vesselvoyage | **auth-credentials-keycloak-s2s.domain**: keycloak.teqplay.nl | **auth-credentials-keycloak-s2s.domain**: keycloak.teqplay.nl |  |
| revents-core | revents-vesselvoyage | **internal-api.domain**: keycloak.teqplay.nl | **internal-api.domain**: keycloak.teqplay.nl |  |
| revents-core | revents-vesselvoyage | **keycloak.csi.domain**: keycloak.teqplay.nl | **keycloak.csi.domain**: keycloak.teqplay.nl |  |
| revents-core | revents-vesselvoyage | **keycloak.csi.url**: https://csibackend.teqplay.nl | **keycloak.csi.url**: https://csibackend.teqplay.nl |  |
| revents-core | revents-vesselvoyage | **keycloak.poma.domain**: keycloak.teqplay.nl | **keycloak.poma.domain**: keycloak.teqplay.nl |  |
| revents-core | revents-vesselvoyage | **keycloak.poma.url**: https://backendpoma.teqplay.nl | **keycloak.poma.url**: https://backendpoma.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| revents-jobs | revents-engine-app-configmap | **internal-api**:  **domain**: keycloak.teqplay.nl | **internal-api**:  **domain**: keycloak.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **csi**:  **url**: https://csibackend.teqplay.nl | **csi**:  **url**: https://csibackend.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **csi**:  **domain**: keycloak.teqplay.nl | **csi**:  **domain**: keycloak.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **poma**:  **url**: https://backendpoma.teqplay.nl | **poma**:  **url**: https://backendpoma.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **poma**:  **domain**: keycloak.teqplay.nl | **poma**:  **domain**: keycloak.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **keycloak**:  **csi**:  **url**: https://csibackend.teqplay.nl | **keycloak**:  **csi**:  **url**: https://csibackend.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **keycloak**:  **csi**:  **domain**: keycloak.teqplay.nl | **keycloak**:  **csi**:  **domain**: keycloak.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **keycloak**:  **poma**:  **url**: https://backendpoma.teqplay.nl | **keycloak**:  **poma**:  **url**: https://backendpoma.teqplay.nl |  |
| revents-jobs | revents-engine-app-configmap | **keycloak**:  **poma**:  **domain**: keycloak.teqplay.nl | **keycloak**:  **poma**:  **domain**: keycloak.teqplay.nl |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| students | superscraper | **portlocaltime.url**: https://localporttime.teqplay.nl/v1/time/ | **portlocaltime.url**: https://localporttime.teqplay.nl/v1/time/ |  |
| students | superscraper | **mongodb.addr**: studentsdev-db.teqplay.nl (NOT FOUND) | **mongodb.addr**: students-db.dev.teqplay.com (NOT FOUND) |  |
| students | superscraper | **portlocaltime.url**: https://localporttime.teqplay.nl/v1/time/ | **portlocaltime.url**: https://localporttime.teqplay.nl/v1/time/ |  |
| students | superscraper | **portmatcher.url**: https://portmatcher.teqplay.nl/destination/recognizeDestination | **portmatcher.url**: https://portmatcher.teqplay.nl/destination/recognizeDestination |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| teqplay-api | external-api-dev | **auth:**  **keycloak:**  **poma**:  **url**: https://backendpomadev.teqplay.nl | **auth:**  **keycloak:**  **poma**:  **url**: https://backendpoma.dev.teqplay.com | x |
| teqplay-api | external-api-dev | **auth:**  **keycloak:**  **poma**:  **domain**: keycloakdev.teqplay.nl | **auth:**  **keycloak:**  **poma**:  **domain**: keycloak.dev.teqplay.com |  |
| teqplay-api | external-api-dev | **auth:**  **keycloak:**  **ship-history**:  **domain**: keycloakdev.teqplay.nl | **auth:**  **keycloak:**  **ship-history**:  **domain**: keycloak.dev.teqplay.com |  |
| teqplay-api | external-api-dev | **globalcors.corsConfigurations**:                                                  '[/\*\*]':  **allowedOrigins**:  https://timeline.teqplay.nl  https://timelinedev.teqplay.nl  https://onthemap.teqplay.nl  https://onthemapdev.teqplay.nl  https://timeline-publicdev.teqplay.nl  http://localhost:3000  http://localhost:3001 | **globalcors.corsConfigurations**:                                                  '[/\*\*]':  **allowedOrigins**:  https://timeline.teqplay.nl  https://timeline.dev.teqplay.com  https://onthemap.teqplay.nl  https://onthemap.dev.teqplay.com  https://timeline-public.dev.teqplay.com  http://localhost:3000  http://localhost:3001 |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| teqplay-api | internal-api-dev | **auth**:  **keycloak**:  **poma**:  **url**: https://backendpomadev.teqplay.nl | **auth**:  **keycloak**:  **poma**:  **url**: https://backendpoma.dev.teqplay.com | x |
| teqplay-api | internal-api-dev | **auth**:  **keycloak**:  **poma**:  **domain**: keycloakdev.teqplay.nl | **auth**:  **keycloak**:  **poma**:  **domain**: keycloak.dev.teqplay.com |  |
| teqplay-api | internal-api-dev | **auth**:  **keycloak**:  **ship-history**:  **domain**: keycloakdev.teqplay.nl | **auth**:  **keycloak**:  **ship-history**:  **domain**: keycloak.dev.teqplay.com |  |
| teqplay-api | internal-api-dev | **spring.cloud.gateway.globalcors.corsConfigurations**:         '[/\*\*]':  **allowedOrigins**:   * https://timeline.teqplay.nl * https://timelinedev.teqplay.nl * https://onthemap.teqplay.nl * https://onthemapdev.teqplay.nl * http://localhost:3000 * http://localhost:3000 | **spring.cloud.gateway.globalcors.corsConfigurations**:         '[/\*\*]':  **allowedOrigins**:   * https://timeline.teqplay.nl * https://timeline.dev.teqplay.com * https://onthemap.teqplay.nl * https://onthemap.dev.teqplay.com * http://localhost:3000 * http://localhost:3000 |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| teqplay-api | routes-platform | **routes**:   * **id**: platform-global   **prod-uri**: https://backend.teqplay.nl  **dev-uri**: https://backenddev.teqplay.nl | **routes**:   * **id**: platform-global   **prod-uri**: https://backend.teqplay.nl  **dev-uri**: https://backend.dev.teqplay.com |  |
| teqplay-api | routes-platform | **routes**:   * **id**: platform   **prod-uri**: https://backend.teqplay.nl  **dev-uri**: https://backenddev.teqplay.nl | **routes**:   * **id**: platform   **prod-uri**: https://backend.teqplay.nl  **dev-uri**: https://backend.dev.teqplay.com |  |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| voyage | smartfleet-dev | **keycloak.vesselvoyage.url**: https://backendvesselvoyagedev.teqplay.nl | **keycloak.vesselvoyage.url**: https://backendvesselvoyage.dev.teqplay.com | x |
| voyage | smartfleet-dev | **portreporter.url**: https://backendportreporterdev.teqplay.nl | **portreporter.url**: https://backendportreporter.dev.teqplay.com | x |
| voyage | smartfleet-dev | **vesselvoyage.url**: https://backendvesselvoyagedev.teqplay.nl | **vesselvoyage.url**: https://backendvesselvoyage.dev.teqplay.com | x |
| voyage | vesselvoyage-dev | **keycloak.csi.url:** https://csibackenddev.teqplay.nl | **keycloak.csi.url:** https://csibackend.dev.teqplay.com | x |
| voyage | vesselvoyage-dev | **keycloak.poma.url**: https://backendpomadev.teqplay.nl | **keycloak.poma.url:** https://backendpoma.dev.teqplay.com | x |
| voyage | vesselvoyage-dev | **amqp.outgoing.uri:** amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/VesselVoyageDev | **amqp.outgoing.uri:** amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/VesselVoyageDev | x |
| voyage | vesselvoyage-dev | event-publishing.rabbit-mq.uri: amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/VesselVoyageDev | event-publishing.rabbit-mq.uri: amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/VesselVoyageDev | x |
| voyage | vesselvoyage-api-dev | **keycloak.csi.url:** https://csibackenddev.teqplay.nl | **keycloak.csi.url:** https://csibackend.dev.teqplay.com | x |
| voyage | vesselvoyage-api-dev | **keycloak.poma.url:** https://backendpomadev.teqplay.nl | **keycloak.poma.url:** https://backendpoma.dev.teqplay.com | x |
| voyage | cargooptima-dev | **cors.allowed-origins:** https://cargooptimadev.teqplay.com,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins:** https://cargooptimadev.teqplay.com,http://localhost:3000,https://localhost:3000,https://cargooptima.dev.teqplay.com | x |
| voyage | cargooptima-staging | **cors.allowed-origins:** https://cargooptimastaging.teqplay.com,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins:** https://cargooptimastaging.teqplay.com,http://localhost:3000,https://localhost:3000,https://cargooptimastaging.dev.teqplay.com | x |
| voyage | service-vessel-analysis-dev | **rabbitmq.uri:** amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/ServiceVesselComponentDev | **rabbitmq.uri:** amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/ServiceVesselComponentDev | x |
| voyage | smartfleet-dev | **ublishing.eta-events.uri:** amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/SmartFleetDev | **publishing.eta-events.uri:** amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/SmartFleetDev | x |
| voyage | smartfleet-dev | **publishing.smartfleet-events.uri:** amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/SmartFleetDev | **publishing.smartfleet-events.uri:** amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/SmartFleetDev | x |
| voyage | smartfleet-dev | **queue.teqplay-events.uri:** amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/TeqplayEventsDev | **queue.teqplay-events.uri:** amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/TeqplayEventsDev | x |
| voyage | smartfleet-dev | **queue.vesselvoyage.uri:** amqps://<user:pass>@rabbitmqdev.teqplay.nl:5671/VesselVoyageDev | **queue.vesselvoyage.uri:** amqps://<user:pass>@rabbitmq.dev.teqplay.com:5671/VesselVoyageDev | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | vesselcompliance-demo-charterer | **cors.allowed-origins**: Navista ,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://vesselcompliance.dev.teqplay.com ,http://localhost:3000,https://localhost:3000 |  |
| customer-apps | vesselcompliance-demo-charterer | **csi.domain**: keycloakdev.teqplay.nl | **csi.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-demo-charterer | **csi.url**: https://csibackenddev.teqplay.nl | **csi.url**: https://csibackend.dev.teqplay.com | x |
| customer-apps | vesselcompliance-demo-charterer | **poma.domain**: keycloakdev.teqplay.nl | **poma.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-demo-charterer | **poma.url**: https://backendpomadev.teqplay.nl | **poma.url**: https://backendpoma.dev.teqplay.com | x |

| **namespace** | **config** | **url** | **new url** | **updated** |
| --- | --- | --- | --- | --- |
| customer-apps | vesselcompliance-demo-terminal | **cors.allowed-origins**: Navista ,http://localhost:3000,https://localhost:3000 | **cors.allowed-origins**: https://vesselcompliance.dev.teqplay.com ,http://localhost:3000,https://localhost:3000 |  |
| customer-apps | vesselcompliance-demo-terminal | **csi.domain**: keycloakdev.teqplay.nl | **csi.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-demo-terminal | **csi.url**: https://csibackenddev.teqplay.nl | **csi.url**: https://csibackend.dev.teqplay.com | x |
| customer-apps | vesselcompliance-demo-terminal | **poma.domain**: keycloakdev.teqplay.nl | **poma.domain**: keycloak.dev.teqplay.com |  |
| customer-apps | vesselcompliance-demo-terminal | **poma.url**: https://backendpomadev.teqplay.nl | **poma.url**: https://backendpoma.dev.teqplay.com | x |

## Ingresses DEVELOP cluster

| **namespace** | **ingress** | **host** | **new host** | **migrated** |
| --- | --- | --- | --- | --- |
| ais-processing | event-history-dev-ingress | eventhistorybackenddev.teqplay.nl | eventhistorybackend.dev.teqplay.com | yes |
| ais-processing | ship-history-dev-ingress | shiphistorybackenddev.teqplay.nl | shiphistorybackend.dev.teqplay.com | yes |
| bunkerplanner | bunkerplanner-dev-ingress | backendbunkerplannerdev.teqplay.nl | backendbunkerplanner.dev.teqplay.com | yes |
| bunkerplanner | bunkerplanner-test-ingress | backendbunkerplannertest.teqplay.nl | backendbunkerplannertest.dev.teqplay.com | yes |
| bunkerplanner | fuelboss-dev-ingress | backendfuelbossdev.teqplay.nl | backendfuelboss.dev.teqplay.com | yes |
| bunkerplanner | fuelboss-test-ingress | backendfuelbosstest.teqplay.nl | backendfuelbosstest.dev.teqplay.com | yes |
| core-service | csi-internal-dev-ingress | csibackenddev-internal.teqplay.nl | csibackend-internal.dev.teqplay.com | yes |
| core-service | csi-query-dev-ingress | csibackenddev.teqplay.nl | csibackend.dev.teqplay.com | yes |
| core-service | driftpredictor-dev-ingress | driftpredictordev.teqplay.dev (NOT FOUND) | driftpredictordev.teqplay.dev (NOT FOUND) |  |
| core-service | emissioncalculator-dev-ingress | emissioncalculatorbackenddev.teqplay.nl | emissioncalculatorbackend.dev.teqplay.com | yes |
| core-service | poma-dev-ingress | backendpomadev.teqplay.nl | backendpoma.dev.teqplay.com | yes |
| core-service | poma-sandbox-ingress | backendpomasandbox.teqplay.nl | backendpomasandbox.dev.teqplay.com | yes |
| core-service | portmatcher-dev-ingress | portmatcherdev.teqplay.nl | portmatcher.dev.teqplay.com | yes |
| core-service | routescout-dev-ingress | routescoutbackenddev.teqplay.nl | routescoutbackend.dev.teqplay.com | yes |
| customer-apps | datastore-dev-ingress | datastorebackenddev.teqplay.nl | datastorebackend.dev.teqplay.com | yes |
| customer-apps | portsupport-dev-ingress | backendportsupportdev.teqplay.nl | backendportsupport.dev.teqplay.com | yes |
| customer-apps | shipsparelogistics-dev-ingress | backendssldev.teqplay.nl | backendssl.dev.teqplay.com | yes |
| customer-apps | terminalplanner-dev-ingress | backendterminalplannerdev.teqplay.nl | backendterminalplanner.dev.teqplay.com | yes |
| customer-apps | vesselcompliance-dev-ingress | vesselcompliancebackenddev.teqplay.nl | vesselcompliancebackend.dev.teqplay.com | yes |
| customer-apps | vesselcompliance-poc-ingress | vesselcompliancebackendpoc.teqplay.nl | vesselcompliancebackendpoc.dev.teqplay.com | yes |
| customer-apps | vesselcompliance-staging-ingress | vesselcompliancebackendstaging.teqplay.nl | vesselcompliancebackendstaging.dev.teqplay.com | yes |
| customer-apps | vesselmatcher-dev-ingress | backendvesselmatcherdev.teqplay.nl | backendvesselmatcher.dev.teqplay.com | yes |
| general-service | datascience-dev-ingress | datasciencebackenddev.teqplay.nl | datasciencebackend.dev.teqplay.com | yes |
| general-service | functionalmonitoring-dev-ingress | functionalmonitoringbackenddev.teqplay.nl | functionalmonitoringbackend.dev.teqplay.com | yes |
| general-service | pdfrenderer-dev-ingress | pdfrendererdev.teqplay.nl | pdfrenderer.dev.teqplay.com | yes |
| general-service | scrapeshark-dev-ingress | scrapesharkbackenddev.teqplay.nl | scrapesharkbackend.dev.teqplay.com | yes |
| general-service | terminallineup-dev-ingress | backendterminallineupdev.teqplay.nl | backendterminallineup.dev.teqplay.com | yes |
| portcall | portcallplus-dev-ingress | portcallplusdev.teqplay.nl | portcallplus.dev.teqplay.com | yes |
| portcall | portpublisher-dev-ingress | backendportpublisherdev.teqplay.nl | backendportpublisher.dev.teqplay.com | yes |
| portcall | portreporter-dev-ingress | backendportreporterdev.teqplay.nl | backendportreporter.dev.teqplay.com | yes |
| portcall | portreporter-testing-ingress | backendportreportertesting.teqplay.nl | backendportreportertesting.dev.teqplay.com | yes |
| pto | pto-etl-dev-ingress | pto-etldev.teqplay.nl | pto-etl.dev.teqplay.com | yes |
| revents-core | revents-engine-api-ingress | reventsbackenddev.teqplay.nl | reventsbackend.dev.teqplay.com | yes |
| students | co2calculations-dev-ingress | co2calculationsbackenddev.teqplay.nl (NO FOUND) | co2calculationsbackend.dev.teqplay.com (NO FOUND) | yes |
| students | congestion-predictor-dev-ingress | congestionpredictorbackenddev.teqplay.nl (NO FOUND) | congestionpredictorbackend.dev.teqplay.com (NO FOUND) | yes |
| students | pdatool-dev-ingress | pdatoolbackenddev.teqplay.nl | pdatoolbackend.dev.teqplay.com | yes |
| teqplay-api | external-api-dev-ingress | apidev.teqplay.nl | api.dev.teqplay.com | yes |
| teqplay-fun | foosball-dev-ingress | foosballbackenddev.teqplay.nl | foosballbackend.dev.teqplay.com | yes |
| teqplay-fun | tabletennis-dev-ingress | backendtabletennisdev.teqplay.nl | backendtabletennis.dev.teqplay.com | yes |
| voyage | cargooptima-dev-ingress | cargooptimabackenddev.teqplay.com | cargooptimabackend.dev.teqplay.com | yes |
| voyage | cargooptima-staging-ingress | cargooptimabackendstaging.teqplay.com | cargooptimabackendstaging.dev.teqplay.com | yes |
| voyage | smartfleet-dev-ingress | backendsmartfleetdev.teqplay.nl | backendsmartfleet.dev.teqplay.com | yes |
| voyage | vesselvoyage-api-dev-ingress | backendvesselvoyagedev.teqplay.nl | backendvesselvoyage.dev.teqplay.com | yes |
| voyage | vesselvoyage-dev-ingress | backendvesselvoyagedev-processing.teqplay.nl | backendvesselvoyage-processing.dev.teqplay.com | yes |

## Route 53 DNS records DEVELOP cluster

The list below shows the expected DNS records used in the configmaps. By comparing this list with the URLs in the configmaps, we can identify any missing entries. A (✔) next to a URL indicates that it is being used in the configmaps or ingress.

aisstreambackenddev.teqplay.nl.
alongsidemonitordev.teqplay.nl. (✔)
apidev.teqplay.nl. (✔) INGRESS
aisdata.teqplay.nl. (✔) PRODUCTION
backendbunkerplannerdev.teqplay.nl. (✔) INGRESS
backendbunkerplannertest.teqplay.nl. (✔) INGRESS
backend.teqplay.nl. (✔) PRODUCTION
backenddev.teqplay.nl. (✔)
backendfoosball.teqplay.nl.
backendfrieslanddev.teqplay.nl.
backendfuelbossdemo.teqplay.nl.
backendfuelbossdev.teqplay.nl. (✔) INGRESS
backendfuelbosstest.teqplay.nl. (✔) INGRESS
backendispsdev.teqplay.nl.
backendpoma.teqplay.nl. (✔) PRODUCTION
backendpomadev.teqplay.nl. (✔) (✔) INGRESS
backendpomasandbox.teqplay.nl. (✔) INGRESS
backendportoracledev.teqplay.nl.
backendportpublisherdev.teqplay.nl.(✔) INGRESS
backendportreporter.teqplay.nl. (✔) PRODUCTION
backendportreporterdev.teqplay.nl. (✔) CONFIGMAP, INGRESS
backendportreporterstaging.teqplay.nl.
backendportreportertesting.teqplay.nl.(✔) INGRESS
backendportsupportdev.teqplay.nl. (✔) INGRESS
backendprontodev.teqplay.nl.
backendriverguidedev.teqplay.nl.
backendsmartfleetdev.teqplay.nl. (✔) CONFIGMAP, INGRESS
backendssldev.teqplay.nl. (✔) INGRESS
backendtabletennisdev.teqplay.nl. (✔) INGRESS
backendterminallineupdev.teqplay.nl. (✔) CONFIGMAP, INGRESS
backendterminalplannerdev.teqplay.nl. (✔) INGRESS
backendvesselmatcherdev.teqplay.nl. (✔) INGRESS
backendvesselvoyage.teqplay.nl. (✔) PRODUCTION
backendvesselvoyagedev-processing.teqplay.nl. (✔) CONFIGMAP, INGRESS
backendvesselvoyagedev.teqplay.nl. (✔) CONFIGMAP, INGRESS
berthoccupancydev.teqplay.nl. (✔) CLOUDFRONT
bridgemonitordev.teqplay.nl.
bunkermonitorbackenddev.teqplay.nl.
bunkermonitordev.teqplay.nl. (✔) CLOUDFRONT
cargooptimabackenddev.teqplay.nl. (✔) INGRESS
chorusdemo-delegations.teqplay.nl.
chorusdemo.teqplay.nl. (✔) CLOUDFRONT
chorusdev.teqplay.nl. (✔) CLOUDFRONT
csibackend.teqplay.nl. (✔) PRODUCTION
csibackend-internal.teqplay.nl. (✔) PRODUCTION
csibackenddata-internal.teqplay.nl.
csibackenddev-internal.teqplay.nl. (✔) INGRESS
csibackenddev.teqplay.nl. (✔)
csidev.teqplay.nl. (✔) CLOUDFRONT
datasciencebackenddev.teqplay.nl. (✔) CONFIGMAP, INGRESS
datasciencedev.teqplay.nl. (✔)
datastorebackenddev.teqplay.nl. (✔) CONFIGMAP, INGRESS
datastoredev.teqplay.nl. (✔)
datastorestaticdev.teqplay.nl. (✔) CLOUDFRONT
emissioncalculatorbackenddev.teqplay.nl. (✔) INGRESS
etapredictordev.teqplay.nl. (✔) CLOUDFRONT
eventhistorybackenddev.teqplay.nl. (✔) INGRESS
fca.teqplay.nl.
foosball.teqplay.nl.
foosballbackenddev.teqplay.nl. (✔) INGRESS
fuelbossdev.teqplay.nl.
functionalmonitoringbackenddev.teqplay.nl. (✔) INGRESS
grafanadev.teqplay.nl. (✔)
internalapidev.teqplay.nl. (✔) CONFIGMAP, INGRESS
keycloak.teqplay.nl. (✔) PRODUCTION
keycloakdev.teqplay.nl. (✔)
keycloaktest.teqplay.nl.
kubeappsdev.teqplay.nl.
localporttime.teqplay.nl. (✔) PRODUCTION
navistademo.teqplay.nl. (✔)
nexmoservicedev.teqplay.nl.
onthemapdev.teqplay.nl. (✔)
opencpudev.teqplay.nl.
pdatoolbackenddev.teqplay.nl. (✔) INGRESS
pdatooldev.teqplay.nl.
pdfrendererdev.teqplay.nl. (✔) CONFIGMAP, INGRESS
perrybackenddev.teqplay.nl.
poma.teqplay.nl. (✔) PRODUCTION
pomadev.teqplay.nl. (✔)
pomasandbox.teqplay.nl. (✔)
portcallplusdev.teqplay.nl. (✔) CONFIGMAP, INGRESS
portmatcher.teqplay.nl. (✔)
portmatcherdev.teqplay.nl. (✔) INGRESS
portreporter-temp.teqplay.nl.
portreporterdev.teqplay.nl. (✔)
portreporterstaging.teqplay.nl.
portsupportdev.teqplay.nl. (✔)
pto-etldev.teqplay.nl. (✔) CONFIGMAP, INGRESS
ptodev.teqplay.nl.
rabbitmqdev.teqplay.nl. (✔)
reventsbackenddev.teqplay.nl. (✔) CONFIGMAP, INGRESS
riverguidedev.teqplay.nl.
rolemapperdev.teqplay.nl.
routescoutbackenddev.teqplay.nl. (✔) CONFIGMAP, INGRESS
routescoutgraphbackenddev.teqplay.nl. (✔) INGRESS
routescoutroutebackenddev.teqplay.nl. (✔) INGRESS
rwspatroldemo.teqplay.nl.
scrapesharkbackenddev.teqplay.nl. (✔) INGRESS
shiphistorybackenddev.teqplay.nl. (✔) INGRESS
terminalplannerdev.teqplay.nl.
timeline-publicdev.teqplay.nl. (✔)
timelinedev.teqplay.nl. (✔)
timelineprontodev.teqplay.nl.
timelinetest.teqplay.nl.
varenfrieslanddev.teqplay.nl.
vaultdev.teqplay.nl.
vesselcompliancebackenddev.teqplay.nl. (✔) INGRESS
vesselcompliancebackendpoc.teqplay.nl. (✔) INGRESS
vesselcompliancebackendstaging.teqplay.nl. (✔) INGRESS
vesselcompliancedev.teqplay.nl. (✔)
vesselcompliancestaging.teqplay.nl. (✔)
vesselmatcherdev.teqplay.nl.
vesselvoyagedev.teqplay.nl. (✔)
zabbix.teqplay.nl. (✔)

Below is the list of domain records that aren’t used in any ConfigMaps or Ingress resources.

aisstreambackenddev.teqplay.nl.
backendfoosball.teqplay.nl.
backendfrieslanddev.teqplay.nl.
backendfuelbossdemo.teqplay.nl.
backendispsdev.teqplay.nl.
backendportoracledev.teqplay.nl.
backendprontodev.teqplay.nl.
backendriverguidedev.teqplay.nl.
bridgemonitordev.teqplay.nl.
bunkermonitorbackenddev.teqplay.nl.
chorusdemo-delegations.teqplay.nl.
csibackenddata-internal.teqplay.nl.
fca.teqplay.nl.
foosball.teqplay.nl.
fuelbossdev.teqplay.nl.
opencpudev.teqplay.nl.
pdatooldev.teqplay.nl.
perrybackenddev.teqplay.nl.
ptodev.teqplay.nl.
riverguidedev.teqplay.nl.
rolemapperdev.teqplay.nl.
rwspatroldemo.teqplay.nl.
terminalplannerdev.teqplay.nl.
timelineprontodev.teqplay.nl.
timelinetest.teqplay.nl.
varenfrieslanddev.teqplay.nl.

## Using AWS Parameter Store

The picture below shows how to manage configurations from a central place.

* Configurations are stored in AWS Parameter Store, similar to how they are stored in ConfigMaps. The Parameter Store entries will not be visible in a ConfigMap but are stored and mounted as files in a Pod.
* Storing configurations in the AWS Parameter Store makes it easier to transfer data to other Organizational Units (OUs).
* This setup allows configurations to be reloaded manually or automatically. For automatic reloading, the application must support hot reloading. Hot reloading is beyond the scope of this plan and will not be covered.
* A cronjob will synchronize the AWS Parameter Store with the Kubernetes cluster when the configuration does not exist.
* The deployment of the Pods needs to include a mount point for the configurations defined in AWS Parameter Store.

## Updating to New Development URL

**Hard Breakup**

We are separating the DEVELOP DNS records from PRODUCTION to ensure changes only affect the DEVELOP cluster. Each URL will be manually replaced with the new URL. Consequently, the DEVELOP cluster may experience temporary disruptions, potentially causing errors and non-functional applications for developers. The advantage of this approach is its speed, and no further changes are expected in the future.