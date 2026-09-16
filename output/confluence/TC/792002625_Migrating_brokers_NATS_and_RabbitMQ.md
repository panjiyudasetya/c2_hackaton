---
id: confluence:792002625
source: confluence
type: page
space: TC
title: Migrating brokers NATS and RabbitMQ
author: Minh Trang Nguyen (Unlicensed)
date: '2025-07-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792002625
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792002625
---
# Migrating brokers NATS and RabbitMQ

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/792002625  

## Content

Status: work in progress

## Definitions

VPC-A: old develop VPC

VPC-B: new develop OU VPC

## Introduction

This document describes the process for migrating the NATS cluster and RabbitMQ to a Virtual Private Cloud (VPC) within a separate Organizational Unit (OU), aiming to simplify the overall transition.

## NATS via Network Load Balancer

The RabbitMQ cluster resides within a private subnet and is accessible through a Network Load Balancer. The plan is to implement the NATS cluster with an identical deployment strategy, ensuring it's also in a private subnet and behind a Network Load Balancer, while using separate node groups.

Add the following annotations to the NATS service of the Helm chart values:

wide760 annotations:
service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
service.beta.kubernetes.io/aws-load-balancer-name: nlb-eks-develop
service.beta.kubernetes.io/aws-load-balancer-scheme: "internal"
service.beta.kubernetes.io/aws-load-balancer-subnets: "subnet-0751f28b388902f9e"

The NATS cluster should be set up similarly to the old develop cluster.

## RabbitMq via Network Load Balancer

Follow the instruction of document to setup RabbitMq: RabbitMq cluster

## Route 53

For seamless migration to the new Develop OU, the new `NATS cluster` needs to be resolvable through Route 53's `dev.teqplay.com` hosted zone. This will involve creating a CNAME DNS record within the existing `dev.teqplay.com` hosted zone in the old cluster. It's imperative that this new domain name is discoverable from both VPC-A and VPC-B (in the new Develop OU) to prevent migration difficulties.

### Creating CNAME record

Navigate to the Route 53 **private** hosted zone `dev.teqplay.com` and create a `CNAME` record named `nats.dev.teqplay.com` or any good subdomain address, pointing it to the Network Load Balancer's address. To get the value, find the Network Load Balancer address:

wide760kubectl get services -n brokers
NAME TYPE CLUSTER-IP EXTERNAL-IP
nats-service LoadBalancer 10.100.19.91 nlb-teqplay-develop-74f5367adfda55ff.elb.eu-west-1.amazonaws.com

Use the value under `EXTERNAL-IP`: [nlb-teqplay-develop-74f5367adfda55ff.elb.eu-west-1.amazonaws.com](http://nlb-teqplay-develop-74f5367adfda55ff.elb.eu-west-1.amazonaws.com)

Exampe:

To confirm http://test-develop-ou.dev.teqplay.com is available in both VPCs, use a test pod within the test namespace.

bashwide760kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
name: curl
spec:
replicas: 1
selector:
matchLabels:
app: curl
template:
metadata:
labels:
app: curl
spec:
containers:
- name: curl
image: alpine/curl:latest
command:
- sleep
args:
- infinity
EOF

Enter the pod (example):

wide760kubectl exec -it curl-78b4fbd7dc-qgxtc -- /bin/sh

Check

wide760curl -v test-develop-ou.dev.teqplay.com

This action should fail because VPC-B currently lacks access to the private Route 53 Hosted Zone `dev.teqplay.com`. To grant VPC-B the necessary access, execute the following commands:

## Associate Private Hosted Zone with VPC

It’s important to run the commands based on the location of the hosted zone. If the hosted zone is in VPC-B, you should associate it with the VPC from which you want to resolve DNS queries, in this case, VPC-A.

Example hosted zone located in VPC-A:

wide760aws route53 create-vpc-association-authorization \
--hosted-zone-id <HOSTED ZONE IN VPC-A> \
--vpc VPCRegion=eu-west-1,VPCId=<VPC-B>

Example hosted zone located in VPC-B:

wide760aws route53 create-vpc-association-authorization \
--hosted-zone-id <HOSTED ZONE IN VPC-B> \
--vpc VPCRegion=eu-west-1,VPCId=<VPC-A>

### Step 1: login VPC-A

Use the administrator credentials to authenticate via the CLI.

Route 53 hosted zone `dev.teqplay.com` = Z060232111LJCUDJX7KZT

VPC Id VPC-B = Z060232111LJCUDJX7KZT

bashwide760aws route53 create-vpc-association-authorization \
--hosted-zone-id Z060232111LJCUDJX7KZT \
--vpc VPCRegion=eu-west-1,VPCId=vpc-050e91e66325f632c

This command grants permission for the Route 53 hosted zone to be used by VPC-B.

The example below is the case of hosted zone in VPC-A.

### Step 2: login VPC-B

This step primarily functions as a validation of Step 1. Please ensure you are logged in via the CLI before proceeding.

bashwide760aws route53 associate-vpc-with-hosted-zone \
--hosted-zone-id Z060232111LJCUDJX7KZT \
--vpc VPCRegion=eu-west-1,VPCId=vpc-050e91e66325f632c

You should see a message like this:

bashwide760{
"ChangeInfo": {
"Id": "/change/C04571073O6NIRNLZI95",
"Status": "PENDING",
"SubmittedAt": "2025-07-07T06:03:32.239000+00:00",
"Comment": ""
}
}

Don’t apply again, because you’ll receive an error message.

bashwide760An error occurred (ConflictingDomainExists) when calling the AssociateVPCWithHostedZone operation: The VPC vpc-050e91e66325f632c in region eu-west-1 has already been associated with the hosted zone Z060232111LJCUDJX7KZT with the same domain name.

These steps have successfully made the Route 53 Private Hosted Zone accessible from VPC-B. However, communication will not yet work, as the next step involves configuring Security Groups and Route Tables.

## Security Groups

For communication to happen, VPC-A and VPC-B must be configured to mutually recognize and allow traffic to their respective CIDR address ranges.

### VPC-A Security Group

Go to security group in. cluster develop of VPC-A.

Add a new inbound security group rule. Set the source to the CIDR block `172.30.0.0/16` (representing VPC-B) to allow all incoming traffic.

### VPC-B Security Group

Add a new inbound security group rule. Set the source to the CIDR block `172.31.0.0/16` (representing VPC-A) to allow all incoming traffic.

## Route Table

To enable inter-VPC communication, the next step involves configuring routes to both VPCs through their peering connection.

### VPC-A Main route table

Navigate to the main route table. Add a new route where the destination is `172.30.0.0/16` and the target is the `Peering Connection` `pcx-0e519e6413c9fb182`.

Since most applications in VPC-A run in public subnets, these route table routes will be sufficient.

### VPC-B Main route table

In VPC-B, locate the main route table, as shown in the image below.

Add a new route where the destination is `172.31.0.0/16` and the target is the Peering Connection `pcx-0e519e6413c9fb182`.

### VPC-B Private subnet eu-west-1a

### VPC-B Private subnet eu-west-1b

Replicate this for subnet `eu-west-1b`, even though it's not currently active.

## Public Subnets

Similarly, to facilitate communication between pods in VPC-B's public subnets and VPC-A, a route is required in VPC-B's Route Table. The configuration process is identical to that used for private subnets.

## Cross-VPC Communication Enabled and Tested

Communication was verified by deploying an `Nginx` instance in VPC-B, exposed via a Network Load Balancer. Test pods, equipped with `curl` for HTTP requests, were then deployed in both a public subnet of VPC-A and a private subnet of VPC-B. Successful requests to the `Nginx` deployment from both VPCs confirmed the established communication.

## Update configmaps apps with NATS urls

Modify all applications currently configured with NATS to use the new Route 53 NATS address.

## Migration steps NATS

1. After NATS was moved to the new Develop cluster (VPC-B), stop all producers. Ensure consumers have fully drained their messages before taking further steps.
2. Run the NATS key-value copy Python script (**todo!**).
3. Producers may be scaled up, and they will subsequently begin producing messages to the NATS cluster located in VPC-B.
4. Consumers may be scaled up, and they will subsequently begin consuming from the NATS cluster located in VPC-B.

## Migration steps RabbitMQ

1. Reduce TTL (seconds) to 1 minute.

2. After RabbitMq was moved to the new Develop cluster (VPC-B), stop all producers. Ensure consumers have fully drained their messages before taking further steps.
3. Reconfigure the `rabbitmq.dev.teqplay.com` DNS record. Convert its type from `Address` to **CNAME**, then specify the Network Load Balancer's address (located within the VPC-B service) as its new value.

4. Producers may be scaled up, and they will subsequently begin producing messages to the RabbitMQ cluster located in VPC-B.
5. Consumers may be scaled up, and they will subsequently begin consuming from the RabbitMQ cluster located in VPC-B.

## Copy key-value store

A simple Python script will be used to copy the key-value stores. This script is designed to be idempotent, ensuring consistent results even when run multiple times. Apply the script in the old develop cluster.

yamlwide760kubectl apply -n brokers -f - <<EOF
apiVersion: v1
data:
copy\_kv\_store.py: |
import asyncio
import logging
import os
from nats.aio.client import Client as NATS
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(\_\_name\_\_)
async def copy\_all\_kv\_buckets(src\_url, dst\_url, user, password):
nc\_src = NATS()
await nc\_src.connect(servers=[src\_url], user=user, password=password)
js\_src = nc\_src.jetstream()
nc\_dst = NATS()
await nc\_dst.connect(servers=[dst\_url], user=user, password=password)
js\_dst = nc\_dst.jetstream()
streams = await js\_src.streams\_info()
kv\_buckets = [s.config.name[3:] for s in streams if s.config.name.startswith("KV\_")]
for bucket in kv\_buckets:
kv\_src = await js\_src.key\_value(bucket)
kv\_dst = await js\_dst.key\_value(bucket)
keys = await kv\_src.keys()
for key in keys:
entry = await kv\_src.get(key)
await kv\_dst.put(key, entry.value)
logger.info(f"Copied bucket: {bucket}")
await nc\_src.close()
await nc\_dst.close()
if \_\_name\_\_ == "\_\_main\_\_":
nats\_src\_url = os.environ.get("NATS\_SRC\_URL")
nats\_dst\_url = os.environ.get("NATS\_DST\_URL")
nats\_user = os.environ.get("NATS\_USER")
nats\_password = os.environ.get("NATS\_PASSWORD")
asyncio.run(copy\_all\_kv\_buckets(
nats\_src\_url,
nats\_dst\_url,
user=nats\_user,
password=nats\_password
))
kind: ConfigMap
metadata:
creationTimestamp: null
name: copykvstore
EOF

The key-value stores from the existing development cluster must be precisely mirrored in the new NATS cluster.

bashwide760nats --user <USERNAME> --password <PASSWORD> kv add portreporter-monitor-encounter-concurrency --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add portreporter-monitor-pilot-onboard --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add portreporter-monitor-tug-standby --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add portreporter-monitor-tug-waiting --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add encounter-monitor --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add anchor-monitor --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add berth-monitor --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add stop-monitor-trace --replicas=3
nats --user <USERNAME> --password <PASSWORD> kv add stop-monitor --replicas=3

Run the job:

bashwide760kubectl apply -n brokers -f - <<EOF
apiVersion: batch/v1
kind: Job
metadata:
name: job-copy-nats-key-values
spec:
template:
spec:
containers:
- name: copying-key-values
image: python:3.12-bookworm
env:
- name: NATS\_SRC\_URL
value: "nats://<NATS SOURCE URL>:4222"
- name: NATS\_DST\_URL
value: "nats://<NATS DESTINATION URL>:4222"
- name: NATS\_USER
value: "<USER>"
- name: NATS\_PASSWORD
value: "<PASSWORD>"
command: ["/bin/sh", "-c"]
args:
- pip install nats-py && python /app/copy\_kv\_store.py
volumeMounts:
- name: script-volume
mountPath: /app/copy\_kv\_store.py
subPath: copy\_kv\_store.py
volumes:
- name: script-volume
configMap:
name: copykvstore
restartPolicy: Never
EOF

Results:

wide760INFO:\_\_main\_\_:Copied bucket: anchor-monitor
INFO:\_\_main\_\_:Copied bucket: berth-monitor
INFO:\_\_main\_\_:Copied bucket: encounter-monitor
INFO:\_\_main\_\_:Copied bucket: portreporter-monitor-encounter-concurrency
INFO:\_\_main\_\_:Copied bucket: portreporter-monitor-pilot-onboard
INFO:\_\_main\_\_:Copied bucket: portreporter-monitor-tug-standby
INFO:\_\_main\_\_:Copied bucket: portreporter-monitor-tug-waiting
INFO:\_\_main\_\_:Copied bucket: stop-monitor
INFO:\_\_main\_\_:Copied bucket: stop-monitor-trace

When the job finished, remove the job:

bashwide760kubectl delete job job-copy-nats-key-values