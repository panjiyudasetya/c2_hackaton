---
id: confluence:806027268
source: confluence
type: page
space: TC
title: Plan migrating Internal and External API
author: Minh Trang Nguyen (Unlicensed)
date: '2025-07-21'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/806027268
explicit_links:
- jira:FS-1
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/806027268
---
# Plan migrating Internal and External API

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/806027268  

## Content

## Introduction

The current architecture for internal-api routes leverages Kubernetes DNS addresses. This approach presents substantial challenges when attempting to make these addresses resolvable from a separate EKS cluster, particularly given the identical domain addresses. A better strategy would be to expose these services via an existing private load balancer. By creating corresponding Route 53 records in the "teqplay.dev" Hosted Zone that point to the load balancer, we can significantly streamline the process of migrating to a new hosted zone, such as "dev.teqplay.dev," in the future.

## Migration strategy

For services configured in both the internal and external APIs, an Ingress is created. This process registers a new entry in the Application Load Balancer `k8s-eksdevinternal-58b13eb317`. To ensure proper routing, a corresponding Route 53 CNAME record is then required for each host within the private hosted zone, pointing to the load balancer's DNS endpoint `k8s-eksdevinternal-58b13eb317-994558034.eu-west-1.elb.amazonaws.com`.

Template creating Ingress resource:

bashwide760kubectl apply -n <NAMESPACE> -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-<SERVICE NAME>
spec:
ingressClassName: alb
rules:
- host: internal-api-<SERVICE NAME>.teqplay.dev
http:
paths:
- backend:
service:
name: <SERVICE NAME>
port:
number: 8080
pathType: ImplementationSpecific
EOF

Ingresses have been created based on the routes.

---

### routes-csi

bashwide760kubectl apply -n core-service -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-csi-query-dev
spec:
ingressClassName: alb
rules:
- host: internal-api-csi-query-dev.teqplay.dev
http:
paths:
- backend:
service:
name: csi-query-dev
port:
number: 8080
pathType: ImplementationSpecific
EOF

### routes-event-history, routes-event-history-platform

bashwide760kubectl apply -n ais-processing -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-event-history-dev
spec:
ingressClassName: alb
rules:
- host: internal-api-event-history-dev.teqplay.dev
http:
paths:
- backend:
service:
name: event-history-dev
port:
number: 8080
pathType: ImplementationSpecific
EOF

### routes-internal-ais-stream

bashwide760kubectl apply -n ais-core -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-ais-stream-dev
spec:
ingressClassName: alb
rules:
- host: internal-api-ais-stream-dev.teqplay.dev
http:
paths:
- backend:
service:
name: ais-stream-dev
port:
number: 8080
pathType: ImplementationSpecific
EOF

### routes-platform

Nothing to apply.

### routes-poma

bashwide760kubectl apply -n core-service -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-poma-dev
spec:
ingressClassName: alb
rules:
- host: internal-api-poma-dev.teqplay.dev
http:
paths:
- backend:
service:
name: poma-dev
port:
number: 8080
pathType: ImplementationSpecific
EOF

### routes-portcallplus

bashwide760kubectl apply -n portcall -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-portcallplus-dev
spec:
ingressClassName: alb
rules:
- host: internal-api-portcallplus-dev.teqplay.dev
http:
paths:
- backend:
service:
name: portcallplus-dev
port:
number: 8080
pathType: ImplementationSpecific
EOF

### routes-ship-history, routes-ship-history-platform, external-api-dev, internal-api-dev

bashwide760kubectl apply -n ais-processing -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-ship-history-dev
spec:
ingressClassName: alb
rules:
- host: internal-api-ship-history-dev.teqplay.dev
http:
paths:
- backend:
service:
name: ship-history-dev
port:
number: 8080
pathType: ImplementationSpecific
EOF

### routes-vesselvoyage, routes-vesselvoyage-v2

bashwide760kubectl apply -n voyage -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
annotations:
alb.ingress.kubernetes.io/group.name: eks-dev-internal
alb.ingress.kubernetes.io/healthcheck-interval-seconds: "30"
alb.ingress.kubernetes.io/healthcheck-path: /actuator/health
alb.ingress.kubernetes.io/healthcheck-port: traffic-port
alb.ingress.kubernetes.io/healthcheck-protocol: HTTP
alb.ingress.kubernetes.io/healthcheck-timeout-seconds: "20"
alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS":443}]'
alb.ingress.kubernetes.io/load-balancer-attributes: idle\_timeout.timeout\_seconds=300
alb.ingress.kubernetes.io/security-groups: sg-03116540549b32d34
alb.ingress.kubernetes.io/ssl-policy: ELBSecurityPolicy-FS-1-2-2019-08
alb.ingress.kubernetes.io/ssl-redirect: "443"
alb.ingress.kubernetes.io/subnets: subnet-419d3218,subnet-9f1578fa,subnet-6f2da718
alb.ingress.kubernetes.io/target-type: ip
name: internal-api-vesselvoyage-api-dev
spec:
ingressClassName: alb
rules:
- host: internal-api-vesselvoyage-api-dev.teqplay.dev
http:
paths:
- backend:
service:
name: vesselvoyage-api-dev
port:
number: 8080
pathType: ImplementationSpecific
EOF

## Route 53

Create the CNAME records for the following addresses and point to DNS name:

`k8s-eksdevinternal-58b13eb317-994558034.eu-west-1.elb.amazonaws.com`

wide760internal-api-csi-query-dev.teqplay.dev
internal-api-event-history-dev.teqplay.dev
internal-api-ais-stream-dev.teqplay.dev
internal-api-poma-dev.teqplay.dev
internal-api-portcallplus-dev.teqplay.dev
internal-api-ship-history-dev.teqplay.dev
internal-api-vesselvoyage-api-dev.teqplay.dev

## Backup configmaps teqplay-api

It is advisable to create a backup of the configmap routes for future reference or recovery.

wide760kubectl get configmap external-api-dev -o yaml -n teqplay-api > bac.external-api-dev.yaml
kubectl get configmap internal-api-dev -o yaml -n teqplay-api > bac.internal-api-dev.yaml
kubectl get configmap routes-csi -o yaml -n teqplay-api > bac.routes-csi.yaml
kubectl get configmap routes-event-history -o yaml -n teqplay-api > bac.routes-event-history.yaml
kubectl get configmap routes-event-history-platform -o yaml -n teqplay-api > bac.routes-event-history-platform.yaml
kubectl get configmap routes-internal-ais-stream -o yaml -n teqplay-api > bac.routes-internal-ais-stream.yaml
kubectl get configmap routes-platform -o yaml -n teqplay-api > bac.routes-platform.yaml
kubectl get configmap routes-poma -o yaml -n teqplay-api > bac.routes-poma.yaml
kubectl get configmap routes-portcallplus -o yaml -n teqplay-api > bac.routes-portcallplus.yaml
kubectl get configmap routes-ship-history -o yaml -n teqplay-api > bac.routes-ship-history.yaml
kubectl get configmap routes-ship-history-platform -o yaml -n teqplay-api > bac.routes-ship-history-platform.yaml
kubectl get configmap routes-vesselvoyage -o yaml -n teqplay-api > bac.routes-vesselvoyage.yaml
kubectl get configmap routes-vesselvoyage-v2 -o yaml -n teqplay-api > bac.routes-vesselvoyage-v2.yaml

## Update configmaps teqplay-api

Kubernetes DNS records are being replaced with the new Ingress addresses in ConfigMaps via the provided terminal commands. It is recommended to verify the output prior to applying the modifications.

You need to have `yq` installed on your computer.

wide760brew install yq

Run the commands to update the configmaps with the new Ingress address.

### Configmap external-api-dev

bashwide1158kubectl get configmap external-api-dev -o yaml -n teqplay-api | \
sed 's|http://ship-history-dev.ais-processing:8080|https://internal-api-ship-history-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > external-api-dev.yaml
...
kubectl apply -f external-api-dev.yaml -n teqplay-api

### Configmap internal-api-dev

bashwide1176kubectl get configmap internal-api-dev -o yaml -n teqplay-api | \
sed 's|http://ship-history-dev.ais-processing:8080|https://internal-api-ship-history-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > internal-api-dev.yaml
...
kubectl apply -f internal-api-dev.yaml -n teqplay-api

### Configmap routes-csi

bashwide1182kubectl get configmap routes-csi -o yaml -n teqplay-api | \
sed 's|http://csi-query-dev.core-service:8080|https://internal-api-csi-query-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > csi-query-dev.yaml
...
kubectl apply -f csi-query-dev.yaml -n teqplay-api

### Configmap routes-event-history

bashwide1194kubectl get configmap routes-event-history -o yaml -n teqplay-api | \
sed 's|http://event-history-dev.ais-processing:8080|https://internal-api-event-history-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-event-history.yaml
...
kubectl apply -f routes-event-history.yaml -n teqplay-api

### Configmap routes-event-history-platform

bashwide1238kubectl get configmap routes-event-history-platform -o yaml -n teqplay-api | \
sed 's|http://event-history-dev.ais-processing:8080|https://internal-api-event-history-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-event-history-platform.yaml
...
kubectl apply -f routes-event-history-platform.yaml -n teqplay-api

### Configmap routes-internal-ais-stream

bashwide1230kubectl get configmap routes-internal-ais-stream -o yaml -n teqplay-api | \
sed 's|http://ais-stream-dev.ais-core:8080|https://internal-api-ais-stream-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-internal-ais-stream.yaml
...
kubectl apply -f routes-internal-ais-stream.yaml -n teqplay-api

### Configmap routes-poma

bashwide1226kubectl get configmap routes-poma -o yaml -n teqplay-api | \
sed 's|http://poma-dev.core-service:8080|https://internal-api-poma-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-poma.yaml
...
kubectl apply -f routes-poma.yaml -n teqplay-api

### Configmap routes-portcallplus

bashwide1218kubectl get configmap routes-portcallplus -o yaml -n teqplay-api | \
sed 's|http://portcallplus-dev.portcall:8080|https://internal-api-portcallplus-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-portcallplus.yaml
...
kubectl apply -f routes-portcallplus.yaml -n teqplay-api

### Configmap routes-ship-history

bashwide1194kubectl get configmap routes-ship-history -o yaml -n teqplay-api | \
sed 's|http://ship-history-dev.ais-processing:8080|https://internal-api-ship-history-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-ship-history.yaml
...
kubectl apply -f routes-ship-history.yaml -n teqplay-api

### Configmap routes-ship-history-platform

bashwide1176kubectl get configmap routes-ship-history-platform -o yaml -n teqplay-api | \
sed 's|http://ship-history-dev.ais-processing:8080|https://internal-api-ship-history-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-ship-history-platform.yaml
...
kubectl apply -f routes-ship-history-platform.yaml -n teqplay-api

### Configmap routes-vesselvoyage

bashwide1180kubectl get configmap routes-vesselvoyage -o yaml -n teqplay-api | \
sed 's|http://vesselvoyage-api-dev.voyage:8080|https://internal-api-vesselvoyage-api-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-vesselvoyage.yaml
...
kubectl apply -f routes-vesselvoyage.yaml -n teqplay-api

### Configmap routes-vesselvoyage-v2

bashwide1180kubectl get configmap routes-vesselvoyage-v2 -o yaml -n teqplay-api | \
sed 's|http://vesselvoyage-api-dev.voyage:8080|https://internal-api-vesselvoyage-api-dev.teqplay.dev|g' > temp.yaml && \
yq 'del(.metadata.annotations."kubectl.kubernetes.io/last-applied-configuration")' temp.yaml > routes-vesselvoyage-v2.yaml
...
kubectl apply -f routes-vesselvoyage-v2.yaml -n teqplay-api

## Application moved to new OU

If `internal-api-csi-query-dev.teqplay.dev` is moved, its new address would be `internal-api-csi-query-dev.dev.teqplay.dev` (Route 53 Hosted Zone dev.teqplay.dev). In this scenario, the CNAME value must be updated to reflect the Application Load Balancer DNS name of the new Development OU. Also the configmaps should be updated with the new address.