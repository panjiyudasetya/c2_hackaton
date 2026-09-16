---
id: confluence:729284611
source: confluence
type: page
space: TC
title: Disk exhaustion recovery procedure (e.g. RabbitMQ)
author: Minh Trang Nguyen (Unlicensed)
date: '2025-05-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/729284611
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/729284611
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/465895425/RabbitMq+cluster#SSL-certificates
---
# Disk exhaustion recovery procedure (e.g. RabbitMQ)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/729284611  

## Content

Despite the implementation of preventative measures, the possibility remains that a node within a node group may experience disk space exhaustion. Should such an eventuality arise, this document details the procedures to resolve this. A test environment with a RabbitMQ cluster will serve as the subject of this experiment. In operational deployments, disk space depletion in a RabbitMQ cluster is generally mitigated by a pre-configured threshold, which prevents message producers from publishing beyond the defined limit. To simulate a node's unresponsiveness resulting from disk space unavailability, we will intentionally induce a full disk condition within the test setup.

## Setup test

The experiment may be executed within the designated namespace, `testing2`. This namespace provides direct access to two secrets, specifically `rabbitmq-password-test` and `rabbitmq-tls-dev`, which are intended for use in this evaluation. The test setup will be performed via the Command Line Interface (CLI), and the subsequent commands are compatible with both Linux and macOS operating systems.

Initiate the development cluster and proceed to the `testing2` namespace.

**Initiate cluster**

kubectl config use-context develop

**Switch to namespace testing2**

kubectl config set-context --current --namespace=testing2

**Secrets**

The secret `rabbitmq-password-test` already exists, however, it can be generated using the following command:

PASSWORD=$(openssl rand -base64 24)
kubectl create secret generic rabbitmq-password-test --from-literal=rabbitmq-password=${PASSWORD}

To create the `rabbitmq-tls-dev` secret, additional prerequisites must be satisfied. See document <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/465895425/RabbitMq+cluster#SSL-certificates> .

### Create AWS node groups

To begin, provision a new node group with the subsequent specifications:

#### Node group 1

##### Step 1

Name: rabbitmq-test-1

Iam role: NodeInstanceRole

Kubernetes labels: app.teqplay.nl/nodegroup=rabbitmqbigdisk

Kubernetes taints: key=nodegroup, value=rabbitmqbigdisk, effect=NoSchedule

**figure 1: step 1** **creating a node group**

##### Step 2

Ami type: Amazon Linux 2 (AL2\_x86\_64)

Instance type: t3.medium

Disk size: 5GiB

Desired size: 3

Minimum size: 1

Maximum size: 3

**figure 2: step 2** **creating a node group**

##### Step 3

Subnet: eks-private-1c

**figure 3: step 3** **creating a node group**

### Install RabbitMq cluster

bashcat <<EOF > values.yaml
auth:
existingPasswordSecret: rabbitmq-password-test
tls:
enabled: true
existingSecret: rabbitmq-tls-dev
failIfNoPeerCert: false
sslOptionsVerify: verify\_none
username: admin
clustering:
name: RabbitMQ TESTING
rebalance: true
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
auth\_oauth2.issuer = https://keycloakdev.teqplay.nl/realms/kubeapps
auth\_oauth2.https.peer\_verification = verify\_none
quorum\_queue.continuous\_membership\_reconciliation.enabled = true
quorum\_queue.continuous\_membership\_reconciliation.target\_group\_size = 3
num\_acceptors.tcp = 40
num\_acceptors.ssl = 40
disk\_free\_limit.absolute = 1GB
ingress:
enabled: false
metrics:
enabled: true
nodeSelector:
app.teqplay.nl/nodegroup: rabbitmqbigdisk
pdb:
minAvailable: 1
persistence:
size: 4Gi
plugins: rabbitmq\_auth\_backend\_oauth2 rabbitmq\_management rabbitmq\_peer\_discovery\_k8s
replicaCount: 3
resources:
limits:
memory: 1025Mi
requests:
memory: 512Mi
service:
annotations:
service.beta.kubernetes.io/aws-load-balancer-name: nlb-eks-testing
service.beta.kubernetes.io/aws-load-balancer-scheme: internal
service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:acm:eu-west-1:050356841556:certificate/48eb53ad-fcbf-4fd9-8077-c6f0a1074f71
service.beta.kubernetes.io/aws-load-balancer-ssl-ports: "443"
service.beta.kubernetes.io/aws-load-balancer-subnets: subnet-01d04cd4e4cd1553d
service.beta.kubernetes.io/aws-load-balancer-type: nlb
ports:
manager: 443
type: LoadBalancer
tolerations:
- effect: NoSchedule
key: nodegroup
operator: Equal
value: rabbitmqbigdisk
EOF

If not already included, the repository should be added (optional)

helm repo add bitnami https://charts.bitnami.com/bitnami

Install the RabbitMq Helm chart

helm install rabbitmqtesting \
oci://registry-1.docker.io/bitnamicharts/rabbitmq \
-f values.yaml \
--version 15.0.3

### Route 53

Create a DNS record within the `private` hosted zone designated as `teqplay.dev`.

**figure 4: create DNS record**

Create a DNS record to point to the Network Load Balancer. For the purposes of this test, a new Network Load Balancer has been automatically created, and the aforementioned DNS record must be configured to resolve to this newly created instance.

### Kecyloak

1. Access Keycloak `DEVELOP` (https://keycloakdev.teqplay.nl).
2. Within the realm `kubeapps`, find the client configuration for `rabbitmq` belonging to the `kubeapps` realm.
3. Add the redirect URL `https://rabbitmqtesting.teqplay.dev/js/oidc-oauth/login-callback.html` to the settings of this rabbitmq client.

**figure 5: add redirect uri to Keycloak**

### VPN

Turn on the VPN to access the RabbitMQ console at address:

https://rabbitmqtesting.teqplay.dev

**figure 6: login screen RabbitMq console**

List the pods of the RabbitMq cluster:

teqplay@dev77 test % kubectl get pods
NAME READY STATUS RESTARTS AGE
rabbitmqtesting-0 1/1 Running 0 1d
rabbitmqtesting-1 1/1 Running 0 1d
rabbitmqtesting-2 1/1 Running 0 1d

The RabbitMQ cluster setup is successful when the pods are visible and the RabbitMQ console is accessible.

**figure 7: RabbitMq healthy nodes**

## Testing

The test to be conducted involves filling up the disk of a single node, which will consequently lead to the loss of a replica within the RabbitMQ cluster. Several critical considerations must be addressed. Notably, the Persistent Volume Claims (PVCs) must not be removed, as the underlying disks contain essential cluster state information.

Go into one Pod, choose a random numer.

kubectl exec -it rabbitmqtesting-2 -c rabbitmq -- /bin/sh

Display the filesystem and usage

df -h
Filesystem Size Used Avail Use% Mounted on
overlay 20G 4.8G 16G 24% /
tmpfs 64M 0 64M 0% /dev
tmpfs 1.9G 0 1.9G 0% /sys/fs/cgroup
/dev/nvme0n1p1 20G 4.8G 16G 24% /tmp
shm 64M 0 64M 0% /dev/shm
tmpfs 3.3G 4.0K 3.3G 1% /bitnami/rabbitmq/conf
tmpfs 3.3G 16K 3.3G 1% /opt/bitnami/rabbitmq/certs
/dev/nvme1n1 40G 1.6G 38G 5% /opt/bitnami/rabbitmq/.rabbitmq/mnesia
tmpfs 3.3G 12K 3.3G 1% /run/secrets/kubernetes.io/serviceaccount
tmpfs 1.9G 0 1.9G 0% /proc/acpi
tmpfs 1.9G 0 1.9G 0% /sys/firmware

The file will be created in the `/tmp` directory, which will also cause the node to fail. Enter the command below:

dd if=/dev/zero of=/tmp/fillfile bs=1M

This command directs an infinite stream of null bytes from the `/dev/zero` device to be written to the file `/tmp/fillfile` in `1MB` block increments.

Once the node has become unavailable and this status is reflected in the RabbitMQ console, proceed to scale down the number of replicas to two.

kubectl scale --replicas=2 statefulsets/rabbitmqtesting

## Resolve

Establish a new node group that mirrors the existing specifications in most aspects, with the distinct characteristic being its unique name.

### Create AWS node groups

#### Node group 2

##### Step 1

Name: rabbitmq-test-2

Iam role: NodeInstanceRole

Kubernetes labels: app.teqplay.nl/nodegroup=rabbitmqbigdisk

Kubernetes taints: key=nodegroup, value=rabbitmqbigdisk, effect=NoSchedule

##### Step 2

Ami type: Amazon Linux 2 (AL2\_x86\_64)

Instance type: t3.medium

Disk size: 5GiB

Desired size: 3

Minimum size: 1

Maximum size: 3

##### Step 3

Subnet: eks-private-1c

Await the complete initialization of the node groups.

kubectl get nodes
NAME STATUS ROLES AGE VERSION
ip-172-31-87-8.eu-west-1.compute.internal Ready <none> 3d4h v1.30.11-eks-473151a
ip-172-31-89-115.eu-west-1.compute.internal Ready <none> 3d4h v1.30.11-eks-473151a
ip-172-31-95-45.eu-west-1.compute.internal Ready <none> 3d4h v1.30.11-eks-473151a

**figure 8: removing node group**

Kubernetes will migrate the RabbitMQ cluster to the newly provisioned node group, a process that may require some time. Once all replicas have been successfully transferred to the new group and the RabbitMQ status indicates that all replicas are healthy, the RabbitMQ cluster can be scaled back to three replicas.

kubectl scale --replicas=3 statefulsets/rabbitmqtesting