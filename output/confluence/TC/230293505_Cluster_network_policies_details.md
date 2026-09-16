---
id: confluence:230293505
source: confluence
type: page
space: TC
title: Cluster network policies details
author: Minh Trang Nguyen (Unlicensed)
date: '2024-08-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/230293505
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/230293505
---
# Cluster network policies details

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/230293505  

## Content

**Status:** ready

This document offers a comprehensive examination of the network policies implemented in both the DEVELOP and PRODUCTION clusters.

Network policies will not be integrated directly into the application, as the responsibility for managing security policies should be shared between the development and operations teams. By maintaining a separation between applications and network policies, any changes to security policies can be implemented without necessitating new deployments. This approach ensures flexibility and allows for independent management of application logic and network security configurations.

Network policies are categorised into three groups: general, develop, and production-specific policies. General network policies are enforced across all namespaces within both the develop and production clusters. These policies universally apply to all pods within a specific namespace. On the other hand, the develop and production policies are specific to their respective namespaces and are not interchangeable; they exclusively govern the behaviour of pods within their designated namespaces. This implies an increased number of files to manage, yet it ultimately provides us with greater flexibility when making adjustments to the policies.

## Network policies

Each namespace is equipped with its own set of network policies, which can be viewed by executing the following command in the terminal.

kubectl get networkpolicies
NAME POD-SELECTOR AGE
allow-egress-to-coredns <none> 3d20h
datascience-dev-egress app.kubernetes.io/instance=datascience-dev,app.kubernetes.io/name=datasciencebackend 3d20h
datascience-dev-ingress app.kubernetes.io/instance=datascience-dev,app.kubernetes.io/name=datasciencebackend 3d20h
default-deny-ingress-egress <none> 3d20h
functionalmonitoring-dev-egress app.kubernetes.io/instance=functionalmonitoring-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h
functionalmonitoring-dev-ingress app.kubernetes.io/instance=functionalmonitoring-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h
functionalmonitoring-dev-mongodb-ingress app.kubernetes.io/instance=functionalmonitoring-dev,app.kubernetes.io/name=mongodb 3d20h
pdfrenderer-dev-egress app.kubernetes.io/instance=pdfrenderer-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h
pdfrenderer-dev-ingress app.kubernetes.io/instance=pdfrenderer-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h
scrapeshark-dev-egress app.kubernetes.io/instance=scrapeshark-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h
scrapeshark-dev-ingress app.kubernetes.io/instance=scrapeshark-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h
terminallineup-dev-egress app.kubernetes.io/instance=terminallineup-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h
terminallineup-dev-ingress app.kubernetes.io/instance=terminallineup-dev,app.kubernetes.io/name=skeleton-mongo-app 3d20h

When a pod encounters issues while communicating with an external service, consider either removing the network policy `default-deny-ingress-egress` or removing all existing network policies. This issue should be reported, and it will be addressed at a later stage.

The network policies are stored in the repository `kubernetes-scripts` under directory `network-policies`.

Each deployment will be assigned both an Ingress and an Egress network policy. The Ingress policy specifies the permitted incoming connections, dictating which ports are allowed to connect. Meanwhile, the Egress policy governs outgoing connections, specifying the allowed ports for connections originating from within the cluster. Below, you'll find some illustrative examples.

Example: datascience-dev Egress

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: datascience-dev-egress
namespace: general-service
spec:
podSelector:
matchLabels:
app.kubernetes.io/instance: datascience-dev
app.kubernetes.io/name: datasciencebackend
policyTypes:
- Egress
egress:
- ports:
- protocol: TCP
port: 443
- protocol: TCP
port: 27017

Example: datascience-dev-ingress

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: datascience-dev-ingress
namespace: general-service
spec:
podSelector:
matchLabels:
app.kubernetes.io/instance: datascience-dev
app.kubernetes.io/name: datasciencebackend
policyTypes:
- Ingress
ingress:
- ports:
- protocol: TCP
port: 8000

## Ports

This table provides an overview of the ports used by the cluster pods, accompanied by their respective descriptions. It's important to note that a single port may be employed by multiple services.

| **port** | **code** | **service** | **description** |
| --- | --- | --- | --- |
| 25 | smtp | SMTP |  |
| 53 | kubedns | Kubernetes DNS service | udp / tcp |
| 80 | port80 | Default http port |  |
| 443 | https | All websites over HTTPS |  |
| 465 | smtp-implicit-tls | SMTP Implicit TLS |  |
| 587 | smtp | SMTP |  |
| 993 | imap | IMAP |  |
| 2020 | fluentbit | Metrics for Prometheus |  |
| 3000 | node-server | Node webserver | Kubeapps, Grafana |
| 3012 | vaultwarden-websocket | Vaultwarden websocket |  |
| 3333 | kubeapps-api-proxy | Kubeapps specific API plugin proxy |  |
| 4222 | nats | Nats |  |
| 5432 | postgres | Postgresql relational database |  |
| 5443 | calico-api | Calico API server | This API server facilitates communication through "kubectl" to retrieve information about the Calico network. |
| 5473 | calico-tyhpa | Calico Typha component | Calico’s datastore proxy |
| 5671 | rabbitmq-tls | RabbitMQ TLS |  |
| 5672 | rabbitmq | RabbitMQ |  |
| 6222 | nats-routing | Nats routing s a port for clustering |  |
| 7422 | nats-leafnode | Nats Lead nodes |  |
| 7522 | nats-gateways | Nats gateways |  |
| 7777 | nats-prometheus | Nats Prometheus metrics |  |
| 7800 | infinispan | High-performance, distributable in memory data grid | Used by Keycloak |
| 7979 | external-dns-metrics | external-dns metrics |  |
| 8000 | custom-web | Django or any other Python app | Custom port |
| 8080 | http | Spring Boot, Prometheus | Custom port |
| 8085 | velero-metrics | Velero Prometheus metrics |  |
| 8081 | http-custom | Amabassador Datawire Telepresence | Custom port |
| 8222 | nats-http | Nats HTTP management tool for information reporting |  |
| 8443 | https-custom | Ambassador Datawire Telepresence | Custom port |
| 9090 | prometheus | Prometheus server |  |
| 9091 | prometheus-push | Prometheus push gateway |  |
| 9093 | prometheus-alert | Prometheus alertmanager API |  |
| 9094 | calico-metrics | Calico Kube controllers metrics |  |
| 9094 | grafana-alerts | Port for Grafana alerts |  |
| 9100 | prometheus-export-metrics | Prometheus exporter metrics |  |
| 9153 | dns-metrics | Kubernetes DNS metrics |  |
| 9187 | postgres-metrics | Postgresql metrics |  |
| 9216 | mongodb-metrics | Prometheus metrics |  |
| 9443 | aws-lb-webhook | AWS Load Balancer webhook |  |
| 9808 | ebs-csi-healthz | EBS CSI health check port |  |
| 10900 | thanos-gossip | Thanos Gossip | Advertise membership data and propagate metadata |
| 10901 | prometheus-grpc | Prometheus gRPC services | gRPC = google Remote Procedure Calls, bi-directional communication |
| 10902 | prometheus-svc | Prometheus internal services |  |
| 12345 |  | Custom stream | Custom port |
| 15000 |  | Custom stream | Custom port |
| 19291 | thanos-receive | Thanos receive component |  |
| 23456 |  | Custom stream | Custom port |
| 27017 | mongodb | MongoDB |  |
| 50051 | kubeapps-api | Kubeapps API |  |
| 56784 | spire | SPIRE streamingv2.ais.spire.com |  |
| 61678 | aws-node | AWS node daemon |  |

## General network policies

These policies are applied per namespace.

| **name** | **type** | **description** |
| --- | --- | --- |
| allow-egress-to-coredns | egress | Pods are restricted to communication solely over port 53, allowing interactions exclusively with CoreDNS for domain resolution purposes. |
| default-deny-ingress-egress | ingress, egress | Restrict all incoming and outgoing traffic for pods. Exercise caution when implementing this policy, as it will block all traffic outright. |

## Network policies cluster DEVELOP

For each namespace, we will display a table detailing the services along with the permitted incoming and outgoing ports. All other ports within that namespace will be restricted.

**ais-core**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| ais-stream-dev | nats, 12345, 23456, 15000, http | nats, 12345, 23456, 15000, http, https, mongodb |
| ais-stream-dev-mongodb | mongodb |  |

**ais-processing**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| ais-diff-dev | http, nats | nats, mongodb |
| ais-engine-dev-mongodb | mongodb |  |
| ais-rabbitmq-dev | http, nats, rabbitmq-tls | nats, rabbitmq-tls, mongodb |
| ais-rabbitmq-dev-mongodb | mongodb |  |
| anchor-monitor-dev | http, nats | https, nats, mongodb |
| area-monitor-dev | http, nats | https, nats, mongodb |
| area-monitor-dev-mongodb | mongodb |  |
| berth-monitor-dev | http, nats | https, nats |
| encounter-monitor-dev | http, nats | https, http, nats |
| event-converter-dev | http, nats, rabbitmq-tls | https, nats, rabbitmq-tls |
| event-history-dev | http | https, mongodb |
| event-history-migrator | http | https, mongodb |
| event-history-processor-dev | http, nats | https, nats, mongodb |
| event-history-processor-dev-mongodb | mongodb |  |
| ship-history-dev | http, nats | https, nats, mongodb |
| ship-history-processor-dev | http, nats | https, nats, mongodb |
| ship-history-processor-dev-mongodb | mongodb |  |

**amazon-cloudwatch**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| aws-for-fluent-bit | fluentbit | https, port80 |

**brokers**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| nats | nats, nats-routing, nats-leafnode, nats-http, nats-prometheus | nats, nats-routing, nats-leafnode |
| nats-leaf-node | nats, nats-routing, nats-http, nats-prometheus | nats, nats-routing |
| nats-box | nats | nats |
| nats-leaf-node-box | nats, nats-prometheus | nats, nats-leafnode |

\*check nats-box and nats-leaf-node-box

**bunkerplanner**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| bunkerplanner-dev | http | https, mongodb |
| bunkerplanner-test | http | https, mongodb |
| fuelboss-dev | http | https, mongodb |
| fuelboss-test | http | https, mongodb |

**calico-apiserver**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| calico-apiserver (managed by Helm chart) | calico-api |  |

**calico-system**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| calico-kube-controllers | calico-metrics | https |
| calico-typha | calico-tyhpa | all |
| calico-node | all | all |
| csi-node-driver | all | all |

**core-service**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| csi-internal-dev | http, nats, rabbitmq-tls | https, nats, http, rabbitmq-tls, mongodb |
| csi-query-dev | http, nats | https, nats, http, mongodb |
| emissioncalculator-dev | http | https |
| poma-dev | http | https, mongodb |
| poma-sandbox | http | https, mongodb |
| poma-sandbox-mongodb | mongodb |  |
| portmatcher-dev | http, nats | https, nats, mongodb |
| routescout-dev | http | https, mongodb |
| routescout-graph-dev | http | https, mongodb |
| routescout-graph-dev-mongodb | mongodb |  |
| routescout-route-planning-dev | http | https, mongodb |
| poma-dev-mongodb | mongodb-metrics, mongodb | mongodb |
| poma-dev-mongodb-arbiter | mongodb | mongodb |

**customer-apps**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| datastore-dev | http | https, mongodb |
| portsupport-dev | http | https, mongodb |
| shipsparelogistics-dev | http, rabbitmq-tls | https, rabbitmq-tls, mongodb |
| terminalplanner-dev | http, rabbitmq-tls | https, rabbitmq-tls, mongodb |
| vesselcompliance-dev | http, rabbitmq-tls | https, mongodb, rabbitmq-tls |
| vesselcompliance-dev-mongodb | mongodb |  |
| vesselmatcher-dev | http | https, mongodb |

**external-dns**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| external-dns-dev | external-dns-metrics | All non-reserved ports are utilized for communication, as dynamic ports play a crucial role in facilitating the exchange of data. |

**general-service**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| datascience-dev | custom-web | https, mongodb |
| functionalmonitoring-dev | http, rabbitmq-tls | https, mongodb, rabbitmq-tls |
| functionalmonitoring-dev-mongodb | mongodb |  |
| pdfrenderer-dev | http | https, mongodb |
| scrapeshark-dev | rabbitmq-tls, http | https, rabbitmq-tls, imap, mongodb |
| terminallineup-dev | http | https, mongodb |

**keycloak**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| keycloak-dev | http, infinispan | infinispan, postgres, smtp, https |

**kube-system**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| aws-load-balancer-controller | aws-lb-webhook | https |
| aws-node | aws-node | all |
| coredns | kubedns, dns-metrics | all |
| ebs-csi-controller | ebs-csi-healthz | https, port80 |
| ebs-csi-node | ebs-csi-healthz | https |

**kubeapps**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| kubeapps-dev | node-server, http | http, https, postgres, kubeapps-api |
| kubeapps-dev-internal-dashboard | http |  |
| kubeapps-dev-internal-kubeappsapis | http, kubeapps-api | postgres, kubeapps-api-proxy |
| kubeapps-dev-postgresql | postgres |  |
| kubeapps-dev-internal-apprepository-controller |  | https |
| **sync cronjobs created by Kubeapps**  kubeapps-jobs-dev |  | **https, postgres** |

**monitoring**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| grafana-dev | node-server, grafana-alerts | all |
| prometheus-kube-state-metrics | http | https |
| prometheus-prometheus-pushgateway | prometheus-push |  |
| prometheus-server | prometheus, prometheus-grpc, prometheus | all |
| prometheus-prometheus-node-exporter | prometheus-export-metrics | all |
| thanos (sidecar), network policy inside prometheus-server | prometheus-svc, prometheus-grpc, thanos-gossip | https, prometheus-svc, prometheus-grpc, thanos-gossip |
| thanos-dev-bucketweb (managed by Helm) | http | all |
| thanos-dev-compactor (managed by Helm) | prometheus-svc, prometheus | all |
| thanos-dev-query (managed by Helm) | prometheus-grpc, prometheus-svc | prometheus-grpc, prometheus-svc |
| thanos-dev-query-frontend (managed by Helm) | prometheus | all |
| thanos-dev-receive (managed by Helm) | prometheus-svc, prometheus-grpc, thanos-receive | all |
| prometheus-alertmanager | prometheus-alert | (only set when alerts are set) |
| thanos-dev-ruler (managed by Helm) | prometheus-grpc, prometheus-svc | prometheus, prometheus-alert, prometheus-grpc, prometheus-svc |
| thanos-dev-storegateway (managed by Helm) | prometheus-grpc, prometheus-svc, prometheus | prometheus-grpc, prometheus-svc, https |
| cronjob-collect-metrics-secrets-egress |  | https, prometheus-push |

**portcall**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| portcallplus-dev | http, nats, rabbitmq-tls | https, nats, rabbitmq-tls, mongodb |
| portpublisher-dev | http, rabbitmq-tls | https, rabbitmq-tls, mongodb |
| portreporter-dev | http, rabbitmq-tls | https, rabbitmq-tls, mongodb, smtp-implicit-tls |
| portreporter-monitor-dev | http, nats, rabbitmq-tls | https, nats, rabbitmq-tls |
| portreporter-testing | http, rabbitmq-tls | https, rabbitmq-tls, mongodb, smtp-implicit-tls |
| portreporter-testing-mongodb | mongodb |  |

**pto**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| hydra-encrypted-postgresql | postgres, postgres-metrics |  |
| pto-etl-dev | http | postgres, https |

**revents-core**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| revents-engine-api | http | https, mongodb |
| revents-engine-api-mongodb | mongodb |  |
| revents-engine-orchestrator | http, nats | http, https, mongodb, nats |
| revents-vesselvoyage | http | https, mongodb |
| revents-vesselvoyage-mongodb | mongodb |  |

**students**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| pdatool-dev | http | https, mongodb |
| pdatool-dev-mongodb | mongodb |  |
| extra ports for testing an developing |  | mongodb, http, https, nats, rabbitmq-tls, 5000 |

**teqplay-api**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| external-api-dev | http | http, https |
| internal-api-dev | http | http, https |

**teqplay-fun**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| foosball-dev | http | mongodb |
| tabletennis-dev | http | mongodb |

**testing**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| portreporter-daily-testing |  | https |
| cronjobs |  | https |

**tigera-operator**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| tigera-operator |  | https |

**vaultwarden**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| vaultwarden-dev | http | postgres, smtp |

\* Vaultwarden has websockets enabled, but it’s disabled in the cluster.

**velero**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| velero | velero-metrics | https |

**voyage**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| cargooptima-dev | http | https, mongodb |
| cargooptima-dev-mongodb | mongodb |  |
| cargooptima-staging | http | https, mongodb |
| cargooptima-staging-mongodb | mongodb |  |
| smartfleet-dev | http, nats, rabbitmq-tls | https, nats, rabbitmq-tls, mongodb |
| vesselvoyage-dev | http, rabbitmq-tls | https, mongodb, rabbitmq-tls |
| vesselvoyage-dev-mongodb | mongodb |  |
| vesselvoyage-api | http | https, mongodb |

---

## Network policies cluster PRODUCTION

**ais-core**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| ais-stream | nats, 12345, 23456, 15000, http | nats, 12345, 23456, 15000, http, https, mongodb |
| ais-stream-mongodb | mongodb |  |

**ais-processing**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| ais-diff | http, nats | nats, mongodb |
| ais-engine-mongodb | mongodb |  |
| ais-rabbitmq | http, nats, rabbitmq-tls | nats, rabbitmq-tls, mongodb |
| ais-rabbitmq-mongodb | mongodb |  |
| anchor-monitor | http, nats | https, nats, mongodb |
| area-monitor | http, nats | https, nats, mongodb |
| area-monitor-mongodb | mongodb |  |
| berth-monitor | http, nats | https, nats |
| encounter-monitor | http, nats | https, http, nats |
| event-converter | http, nats, rabbitmq-tls | https, nats, rabbitmq-tls |
| event-history | http | https, mongodb |
| event-history-processor | http, nats | https, nats, mongodb |
| event-history-processor-mongodb | mongodb |  |
| ship-history | http, nats | https, nats, mongodb |
| ship-history-processor | http, nats | https, nats, mongodb |
| ship-history-processor-mongodb | mongodb |  |
| stop-monitor | http, nats | https, nats, mongodb |

**amazon-cloudwatch**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| aws-for-fluent-bit | fluentbit | https, port80 |

**brokers**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| nats | nats, nats-routing, nats-leafnode, nats-http, nats-prometheus | nats, nats-routing, nats-leafnode |
| nats-box | nats | nats |

**customer-apps**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| casey | http | https, mongodb |
| datastore | http | https, mongodb |
| pdatool | http | https, mongodb |
| pdatool-mongodb | mongodb |  |
| portsupport | http | https, mongodb |
| shipsparelogistics | http, rabbitmq-tls | https, rabbitmq-tls, mongodb |
| terminalplanner | http, rabbitmq-tls | https, rabbitmq-tls, mongodb |
| vesselcompliance | http, rabbitmq-tls | https, rabbitmq-tls, mongodb |
| vesselcompliance-mongodb | mongodb |  |
| vesselmatcher | http | https, mongodb |

**bunkerplanner**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| bunkerplanner | http | https, mongodb |
| fuelboss | http | https, mongodb |
| fuelboss-demo | http | https, mongodb |

**calico-apiserver**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| calico-apiserver (managed by Helm chart) | calico-api |  |

**calico-system**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| calico-kube-controllers | calico-metrics | https |
| calico-typha | calico-tyhpa | all |
| calico-node | all | all |
| csi-node-driver | all | all |

**core-service**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| csi-internal | http, nats, rabbitmq-tls | https, nats, http, rabbitmq-tls, mongodb |
| csi-query | http, nats | https, nats, http, mongodb |
| emissioncalculator | http | https |
| nexmoservice | http | https |
| poma | http | https, mongodb |
| portlocaltime | http | https, mongodb |
| portmatcher | http, nats | https, nats, mongodb |
| routescout | http | https, mongodb |
| routescout-graph | http | https, mongodb |
| routescout-graph-mongodb | mongodb |  |
| routescout-route-planning | http | https, mongodb |
| poma-mongodb | mongodb-metrics, mongodb | mongodb |
| poma-mongodb-arbiter | mongodb | mongodb |

**external-dns**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| external-dns | external-dns-metrics | All non-reserved ports are utilized for communication, as dynamic ports play a crucial role in facilitating the exchange of data. |

**general-service**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| datascience | custom-web | https, mongodb |
| functionalmonitoring | http, rabbitmq-tls | https, mongodb, rabbitmq-tls |
| functionalmonitoring-mongodb | mongodb |  |
| pdfrenderer | http | https, mongodb |
| scrapeshark | rabbitmq-tls, http | https, rabbitmq-tls, imap, mongodb |
| terminallineup | http | https, mongodb |
| teminallineup-mongodb | mongodb |  |

**keycloak**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| keycloak | http, infinispan | infinispan, postgres, smtp, https |

**kube-system**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| aws-load-balancer-controller | aws-lb-webhook | https |
| aws-node | aws-node | all |
| coredns | kubedns, dns-metrics | all |
| ebs-csi-controller | ebs-csi-healthz | https, port80 |
| ebs-csi-node | ebs-csi-healthz | https |

**kubeapps**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| kubeapps | node-server, http | http, https, postgres, kubeapps-api |
| kubeapps-internal-dashboard | http |  |
| kubeapps-internal-kubeappsapis | http, kubeapps-api | postgres, kubeapps-api-proxy |
| kubeapps-postgresql | postgres |  |
| kubeapps-internal-apprepository-controller |  | https |
| **sync cronjobs created by Kubeapps**  kubeapps-jobs |  | **https, postgres** |

**monitoring**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| grafana | node-server, grafana-alerts | all |
| prometheus-kube-state-metrics | http | https |
| prometheus-prometheus-pushgateway | prometheus-push |  |
| prometheus-server | prometheus, prometheus-grpc, prometheus | all |
| prometheus-prometheus-node-exporter | prometheus-export-metrics | all |
| thanos (sidecar), network policy inside prometheus-server | prometheus-svc, prometheus-grpc, thanos-gossip | https, prometheus-svc, prometheus-grpc, thanos-gossip |
| thanos-bucketweb (managed by Helm) | http | all |
| thanos-compactor (managed by Helm) | prometheus-svc, prometheus | all |
| thanos-query (managed by Helm) | prometheus-grpc, prometheus-svc | prometheus-grpc, prometheus-svc |
| thanos-query-frontend (managed by Helm) | prometheus | all |
| thanos-receive (managed by Helm) | prometheus-svc, prometheus-grpc, thanos-receive | all |
| prometheus-alertmanager | prometheus-alert | (only set when alerts are set) |
| thanos-ruler (managed by Helm) | prometheus-grpc, prometheus-svc | prometheus, prometheus-alert, prometheus-grpc, prometheus-svc |
| thanos-dev-storegateway (managed by Helm) | prometheus-grpc, prometheus-svc, prometheus | prometheus-grpc, prometheus-svc, https |
| cronjob-collect-metrics-secrets-egress |  | https, prometheus-push |

**portcall**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| portcallplus | http, nats, rabbitmq-tls | https, nats, rabbitmq-tls, mongodb |
| portpublisher | http, rabbitmq-tls | https, rabbitmq-tls, mongodb |
| portreporter | http, rabbitmq-tls | https, rabbitmq-tls, mongodb, smtp-implicit-tls |

**pto**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| hydra-encrypted-postgresql | postgres, postgres-metrics |  |
| pto-etl | http | postgres, https |

**revents-core**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| revents-engine-api | http | https, mongodb |
| revents-engine-api-mongodb | mongodb |  |
| revents-engine-orchestrator | http, nats | http, https, mongodb, nats |
| revents-vesselvoyage | http | https, mongodb |
| revents-vesselvoyage-mongodb | mongodb |  |

**teqplay-api**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| external-api | http | http, https |
| internal-api | http | http, https |

**tigera-operator**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| tigera-operator |  | https |

**vaultwarden**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| vaultwarden | http | postgres, smtp |

* Vaultwarden has websockets enabled, but it’s disabled in the cluster.

**velero**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| velero | velero-metrics | https |

**voyage**

| **service** | **ingress** | **egress** |
| --- | --- | --- |
| smartfleet | http, nats, rabbitmq-tls | https, nats, rabbitmq-tls, mongodb |
| vesselvoyage | http, rabbitmq-tls | https, mongodb, rabbitmq-tls |
| vesselvoyage-mongodb | mongodb |  |
| vesselvoyage-api | http | https, mongodb |