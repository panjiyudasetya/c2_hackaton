---
id: confluence:465895425
source: confluence
type: page
space: TC
title: RabbitMq cluster
author: Minh Trang Nguyen (Unlicensed)
date: '2025-07-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/465895425
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/465895425
---
# RabbitMq cluster

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/465895425  

## Content

Status: ready

**VPN required**

This document describes the setup of the RabbitMQ cluster and the configuration of its authentication.

## Prerequisites

### TLS certificates

Install the secret for the SSL certificate `*.teqplay.nl`. It is assumed that all files are located within a single directory.

We should migrate to Let’s Encrypt cert-manager for automatic renewal of certificates. See document Cert-manager for auto creating TLS certificates.

**DEVELOP**

wide760kubectl create secret generic rabbitmq-tls-dev \
--from-file=tls.key=tls.key \
--from-file=tls.crt=tls.crt \
--from-file=ca.crt=ca.bundle.crt \
--dry-run=client -o yaml > rabbitmq-dev-secret.yamlwide760kubectl apply -f rabbitmq-dev-secret.yaml

Check the certificate in the secret.

wide760kubectl get secret rabbitmq-tls-dev -o jsonpath="{.data.tls\.crt}" \
| base64 --decode \
| openssl x509 -noout -dates
...
notBefore=Nov 13 00:00:00 2024 GMT
notAfter=Dec 2 23:59:59 2025 GMT

Remove the secret file.

wide760rm -f rabbitmq-dev-secret.yaml

**PRODUCTION**

wide760kubectl create secret generic rabbitmq-tls \
--from-file=tls.key=tls.key \
--from-file=tls.crt=tls.crt \
--from-file=ca.crt=ca.bundle.crt \
--dry-run=client -o yaml > rabbitmq-secret.yamlwide760kubectl apply -f rabbitmq-secret.yaml

Check the certificate in the secret.

wide760kubectl get secret rabbitmq-tls -o jsonpath="{.data.tls\.crt}" \
| base64 --decode \
| openssl x509 -noout -dates
...
notBefore=Nov 13 00:00:00 2024 GMT
notAfter=Dec 2 23:59:59 2025 GMT

Remove the secret file.

wide760rm -f rabbitmq-secret.yaml

Remove all certificate files.

### Default RabbitMQ password

This step needs to be done with the installation of a new RabbitMQ cluster. Please replace <SOME RANDOM PASSWORD> with a real password.

**DEVELOP**

wide760kubectl create secret generic rabbitmq-password-dev --from-literal=rabbitmq-password=<SOME RANDOM PASSWORD>

**PRODUCTION**

wide760kubectl create secret generic rabbitmq-password --from-literal=rabbitmq-password=<SOME RANDOM PASSWORD>

## Installation

Via Helm, the cluster was set up. Below is an example of the values for the develop cluster.

**DEVELOP**

wide760replicaCount: 3
auth:
username: admin
existingPasswordSecret: rabbitmq-password-dev
tls:
enabled: true
existingSecret: rabbitmq-tls-dev
failIfNoPeerCert: false
sslOptionsVerify: verify\_none
clustering:
name: "RabbitMQ DEV"
rebalance: true
pdb:
minAvailable: 1
persistence:
size: 20Gi
metrics:
enabled: true
service:
type: LoadBalancer
annotations:
service.beta.kubernetes.io/aws-load-balancer-name: "nlb-eks-develop"
service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
service.beta.kubernetes.io/aws-load-balancer-scheme: "internal"
service.beta.kubernetes.io/aws-load-balancer-subnets: "subnet-01d04cd4e4cd1553d"
service.beta.kubernetes.io/aws-load-balancer-ssl-cert: "arn:aws:acm:eu-west-1:050356841556:certificate/48eb53ad-fcbf-4fd9-8077-c6f0a1074f71"
service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "443"
ports:
manager: 443
resources:
requests:
memory: "3072Mi"
limits:
memory: "4096Mi"
nodeSelector:
app.teqplay.nl/nodegroup: rabbitmq
tolerations:
- key: nodegroup
operator: Equal
value: rabbitmq
effect: NoSchedule
ingress:
enabled: false
plugins: "rabbitmq\_auth\_backend\_oauth2 rabbitmq\_management rabbitmq\_peer\_discovery\_k8s"
extraConfiguration: |-
auth\_backends.1 = rabbit\_auth\_backend\_internal
auth\_backends.2 = rabbit\_auth\_backend\_oauth2
log.default.level = info
management.oauth\_enabled = true
management.oauth\_client\_id = rabbitmq
management.oauth\_scopes = openid profile
auth\_oauth2.resource\_server\_id = rabbitmq
auth\_oauth2.preferred\_username\_claims.1 = preferred\_username
auth\_oauth2.additional\_scopes\_key = groups
auth\_oauth2.issuer = https://keycloakdev.teqplay.nl/auth/realms/kubeapps
auth\_oauth2.https.peer\_verification = verify\_none
quorum\_queue.continuous\_membership\_reconciliation.enabled = true
quorum\_queue.continuous\_membership\_reconciliation.target\_group\_size = 3
num\_acceptors.tcp = 40
num\_acceptors.ssl = 40
disk\_free\_limit.absolute = 10GB

**PRODUCTION**

wide760replicaCount: 3
auth:
existingPasswordSecret: rabbitmq-password
tls:
enabled: true
existingSecret: rabbitmq-tls
failIfNoPeerCert: false
sslOptionsVerify: verify\_none
username: admin
clustering:
name: RabbitMQ PRODUCTION
rebalance: true
pdb:
minAvailable: 1
persistence:
size: 20Gi
metrics:
enabled: true
service:
type: LoadBalancer
annotations:
service.beta.kubernetes.io/aws-load-balancer-name: nlb-eks-production
service.beta.kubernetes.io/aws-load-balancer-scheme: internal
service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:acm:eu-west-1:050356841556:certificate/48eb53ad-fcbf-4fd9-8077-c6f0a1074f71
service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "443"
service.beta.kubernetes.io/aws-load-balancer-subnets: subnet-01d04cd4e4cd1553d
service.beta.kubernetes.io/aws-load-balancer-type: nlb
ports:
manager: 443
resources:
limits:
memory: 4096Mi
requests:
memory: 3072Mi
nodeSelector:
app.teqplay.nl/nodegroup: rabbitmq
tolerations:
- effect: NoSchedule
key: nodegroup
operator: Equal
value: rabbitmq
extraConfiguration: |-
auth\_backends.1 = rabbit\_auth\_backend\_internal
auth\_backends.2 = rabbit\_auth\_backend\_oauth2
log.default.level = info
management.oauth\_enabled = true
management.oauth\_client\_id = rabbitmq
management.oauth\_scopes = openid profile
auth\_oauth2.resource\_server\_id = rabbitmq
auth\_oauth2.preferred\_username\_claims.1 = preferred\_username
auth\_oauth2.additional\_scopes\_key = groups
auth\_oauth2.issuer = https://keycloak.teqplay.nl/auth/realms/kubeapps
auth\_oauth2.https.peer\_verification = verify\_none
quorum\_queue.continuous\_membership\_reconciliation.enabled = true
quorum\_queue.continuous\_membership\_reconciliation.target\_group\_size = 3
num\_acceptors.tcp = 40
num\_acceptors.ssl = 40
disk\_free\_limit.absolute = 10GB
ingress:
enabled: false
plugins: rabbitmq\_auth\_backend\_oauth2 rabbitmq\_management rabbitmq\_peer\_discovery\_k8s

* This configuration doesn’t require client validation, as client verification was not possible at the time of writing.
* A network load balancer was created, which has only a private subnet.
* The OAuth2 plugin was enabled, allowing sign-in with Keycloak.
* The metrics are displayed in Grafana.
* The console manager is accessible on port 443.
* There are two backends for authentication: the internal backend (`rabbit_auth_backend_internal`) for the authentication of the liveness and readiness probes, and another backend for signing in with Keycloak.

## Export / Import

The definitions file from the old RabbitMQ instance was exported and imported into the new cluster. The classic queue types were replaced with the new quorum queue type, which is better suited for a highly available cluster.

The use of Quorum Queues is ideal for scenarios requiring high availability and data durability, even in the event of node failures. In a test with classic queues, data was lost because the messages were stored on a single node. Although mirrored queues were used, data loss still occurred.

Steps for export from old instance and import into new cluster:

**export**

wide760sudo rabbitmqctl export\_definitions /tmp/definitions.file.json

In the export file, the text "classic" was replaced with "quorum", the "auto\_delete" attribute was removed, and the operator policies were removed due to errors encountered during import.

**import**

Copy file to a RabbitMq instance

wide760kubectl cp definitions.file.json rabbitmq-cluster-0:/tmp -c rabbitmq

Import data

wide760rabbitmqctl import\_definitions /tmp/definitions.file.json

Clean up

wide760rm -f /tmp/definitions.file.json

## **Management console**

## The management console service port has been changed from 15672 to 443, making it easier to secure the connection with an SSL certificate.

In Route53, two DNS records were added: one for the management console and another for the cluster. The management console is linked to the “teqplay.dev” domain, which is connected to the private network within the VPC. The cluster is mapped to the “teqplay.nl” domain, as it uses TLS secured with the “teqplay.nl” SSL certificate bundle. The cluster is not accessible via the internet, as it resides within the private subnet “eu-west-1c”. The DNS records are managed in Amazon Route 53.

Management console addresses:

**Develop**

wide760https://rabbitmq-console-dev.teqplay.dev

**Production**

wide760https://rabbitmq-console.teqplay.dev

A node group named “rabbitmq” was created for the cluster, specifically configured to allow only RabbitMQ nodes.

The node group can be updated through a rolling update, where AWS migrates each node to a new instance, a process that may take some time. To maintain high availability, at least 2 out of 3 nodes must remain online. If more than 2 nodes go down, the cluster will lose access to its data.

## Keycloak

To allow users to access the RabbitMQ console, they must be added to the `rabbitmq.tag:administrator` group. For additional permissions to create queues, users need to be added to the `rabbitmq.configure:*/*` group.

It is required to add an extra client mapper to enable signing in with RabbitMQ. Refer to the screenshots below for detailed instructions on how to add this requirement.

## RabbitMQ restore after crash

**Status: Conceptual, requires further testing!**

Each queue must be replicated across a minimum of three nodes. If this requirement is not met, the queue must rejoin a node to restore proper replication. The illustration below depicts the expected status.

**Scenario: Disks are filling up fast**

RabbitMq write all commit logs to the directory “/opt/bitnami/rabbitmq/.rabbitmq/mnesia“. First find the Helm chart version.

wide760helm list -n brokers
NAME NAMESPACE REVISION STATUS CHART APP VERSION
nats brokers 18 deployed nats-0.19.8 2.9.12-alpine
nats-leaf-node brokers 21 deployed nats-0.19.8 2.9.12-alpine
rabbitmq-cluster brokers 3 deployed rabbitmq-15.0.3 4.0.2 

The chart version is “15.0.3“, so we are going to use this version.

wide760helm upgrade rabbitmq-cluster \
oci://registry-1.docker.io/bitnamicharts/rabbitmq \
--set persistence="50Gi" \
--version 15.0.3

Replace `50Gi` with the appropriate size

The disks should resize, providing us with some additional time. Next, attempt to rejoin the node that is not accepting connections by following the steps outlined in the scenario `Disk filling up due to one node not accepting any connections.`

**Scenario: Disk filling up due to one node not accepting any connections**

In certain cases, if all alerts are missed, a node may stop accepting connections. To address this issue, follow these steps: first, identify the node that is no longer accepting connections.

wide760kubectl get pods -n brokerswide760rabbitmq-cluster-0 1/1 Running 0 40h
rabbitmq-cluster-1 1/1 Running 0 40h
rabbitmq-cluster-2 1/1 Running 0 40h

Go into the node, which doesn’t accept connections:

Node 0

wide760kubectl exec -it rabbitmq-cluster-0 -c rabbitmq -- /bin/sh

Node 1

wide760kubectl exec -it rabbitmq-cluster-1 -c rabbitmq -- /bin/sh

Node 2

wide760kubectl exec -it rabbitmq-cluster-2 -c rabbitmq -- /bin/sh

Stop the server

wide760rabbitmqctl stop\_app

We need to open a new terminal window to access a different container and detach the node from the RabbitMQ cluster. For example, if Node 0 is not accepting connections, we will need to connect to Node 1.

wide760kubectl exec -it rabbitmq-cluster-1 -c rabbitmq -- /bin/sh
rabbitmqctl forget\_cluster\_node rabbit@rabbitmq-cluster-0.rabbitmq-cluster-headless.brokers.svc.cluster.local

Return to the node that is not accepting connections. Then, select a node in the cluster that is still accepting connections.

Node 0

wide760rabbitmqctl join\_cluster rabbit@rabbitmq-cluster-0.rabbitmq-cluster-headless.brokers.svc.cluster.local

Node 1

wide760rabbitmqctl join\_cluster rabbit@rabbitmq-cluster-1.rabbitmq-cluster-headless.brokers.svc.cluster.local

Node 2

wide760rabbitmqctl join\_cluster rabbit@rabbitmq-cluster-2.rabbitmq-cluster-headless.brokers.svc.cluster.local

Join the cluster again.

Choose Node 0 when it’s alive

wide760rabbitmqctl join\_cluster rabbit@rabbitmq-cluster-0.rabbitmq-cluster-headless.brokers.svc.cluster.local

Choose Node 1 when it’s alive

wide760rabbitmqctl join\_cluster rabbit@rabbitmq-cluster-1.rabbitmq-cluster-headless.brokers.svc.cluster.local

Choose Node 2 when it’s alive

wide760rabbitmqctl join\_cluster rabbit@rabbitmq-cluster-2.rabbitmq-cluster-headless.brokers.svc.cluster.local

**Scenario: The cluster is healthy, but the queues are not fully replicated across all nodes**

Go into one of the node, which the queues to need to be added to:

Node 0

wide760kubectl exec -it rabbitmq-cluster-0 -c rabbitmq -- /bin/sh
rabbitmq-queues grow rabbit@rabbitmq-cluster-0.rabbitmq-cluster-headless.brokers.svc.cluster.local all

Node 1

wide760kubectl exec -it rabbitmq-cluster-1 -c rabbitmq -- /bin/sh
rabbitmq-queues grow rabbit@rabbitmq-cluster-1.rabbitmq-cluster-headless.brokers.svc.cluster.local all

Node 2

wide760kubectl exec -it rabbitmq-cluster-2 -c rabbitmq -- /bin/sh
rabbitmq-queues grow rabbit@rabbitmq-cluster-2.rabbitmq-cluster-headless.brokers.svc.cluster.local all

This should ensure that all queues are replicated across all nodes.

## Migration steps PRODUCTION

Take a screenshot of the active connections visible in the RabbitMQ console.

Example: active connections

**Kubernetes**

Stop the following deployments

wide760kubectl scale --replicas 0 deploy/ais-rabbitmq -n ais-processing
kubectl scale --replicas 0 deploy/event-converter -n ais-processing

**Backend**

After all messages have been consumed in the virtual hosts 'AisStreaming' and 'TeqplayEvents,' shut down the Backend Platform (EC2).

Picture: backend EC2 instance

You need to sign in to the EC2 instance.

wide760ssh ubuntu@ip-172-31-31-155.eu-west-1.compute.internal

Stop the server.

wide760sudo systemctl stop tomcat8.service

**Kubernetes**

Scale down the next deployments.

wide760kubectl scale --replicas 0 deploy/portcallplus -n portcall
kubectl scale --replicas 0 deploy/portreporter-monitor -n portcall
kubectl scale --replicas 0 deploy/vesselvoyage -n voyage

After all messages have been consumed in the virtual hosts 'VesselVoyage' scale the next deployments.

wide760kubectl scale --replicas 0 deploy/smartfleet -n voyage

Scale down any deployments that have no dependencies.

wide760kubectl scale --replicas 0 deploy/scrapeshark -n general-service

Wait until all queues on the old machine are empty before updating the DNS record in Route 53 to point to the new RabbitMQ cluster.

Change the value of the DNS record “[rabbitmq.teqplay.nl](http://rabbitmq.teqplay.nl)“ to:

wide760nlb-eks-production-7625ae705864f2f1.elb.eu-west-1.amazonaws.com.

**EC2**

The RabbitMQ EC2 instance can now be shut down.

**Kubernetes**

Scale up the deployments as needed.

wide760kubectl scale --replicas 1 deploy/ais-rabbitmq -n ais-processing
kubectl scale --replicas 1 deploy/event-converter -n ais-processing
kubectl scale --replicas 1 deploy/portcallplus -n portcall
kubectl scale --replicas 1 deploy/portreporter-monitor -n portcall
kubectl scale --replicas 1 deploy/vesselvoyage -n voyage
kubectl scale --replicas 1 deploy/smartfleet -n voyage
kubectl scale --replicas 1 deploy/scrapeshark -n general-service

**Backend**

We need to flush the DNS cache and restart the `Platform` service.

wide760sudo systemd-resolve --flush-caches
sudo systemctl restart systemd-resolved.service
platform-scripts/restart.py

**Last check - Kubernetes**

Verify that all queues have been consumed in the RabbitMq console. If not, restart the necessary deployments.

Please check if the following applications are still working:

* Platform
* VesselVoyage
* PortReporter