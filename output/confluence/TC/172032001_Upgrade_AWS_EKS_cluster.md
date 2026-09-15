---
id: confluence:172032001
source: confluence
type: page
space: TC
title: Upgrade AWS EKS cluster
author: Jamie de Leest
date: '2026-03-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/172032001
explicit_links: []
---
# Upgrade AWS EKS cluster

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/172032001  

## Content

This document describes the steps to upgrade the Kubernetes cluster.

# Preparations UPGRADE

## Announcement preparations for upgrading Kubernetes cluster

Alert via Slack that preparations are on the way to upgrade the Kubernetes cluster.

DEVELOP

> Today, I will be starting the preparatory steps for upgrading the DEVELOP cluster. There's a possibility of encountering some issues, so I would appreciate it if you could inform me of any issues that occur.

PRODUCTION

> Today, I will be starting the preparatory steps for upgrading the PRODUCTION cluster. There's a possibility of encountering some issues, so I would appreciate it if you could inform me of any issues that occur.

## **1. Upgrade EKS Add-ons**

* The add-ons are managed by AWS and an upgrade button is available for each add-on.
* If the upgrade introduces new default configuration values, ensure to override the existing ones.

The version updates in the DEVELOP cluster should be documented, as these versions are slated for future upgrades in the PRODUCTION cluster. Here is a sample representation of how we document the process during the upgrade of EKS Add-ons.

* VPC CNI: v1.18.1-eksbuild.3
* Kubeproxy: v1.27.12-eksbuild.2
* CoreDNS: v1.10.1-eksbuild.11
* EBS: v1.31.0-eksbuild.1

## 2. Upgrade Helm charts via Kubeapps

* The Helm charts are managed with Kubeapps via [https://kubeappsdev.teqplay.dev](https://kubeappsdev.teqplay.dev/) for the DEVELOP cluster and <https://kubeapps.teqplay.dev> for the PRODUCTION cluster..
* Applications are located across different namespaces. Switch to each namespace and upgrade the application via the upgrade button.

For every cluster upgrade, it is essential to document the Helm chart version and the corresponding application version to which the Helm chart is being updated. These recorded versions will serve as a reference during the upgrade process of the PRODUCTION cluster. We aim to avoid introducing an additional version into the Production environment. Here is a sample representation of how we document the process during the upgrade of Helm charts.

Helm chart: Kubeapps

Namespace: kubeapps

Chart version: 15.1.1

App version: 2.10.0

Note: the upgrade to version 15.1.1 was executed seamlessly, with no issues identified.

Helm chart: Keycloak

Namespace: keycloak

Chart version: 21.3.1

App version: 24.0.4

Note: the upgrade could not be completed as it involved a transition from application version 23 to 24. This change is significant as the Infinispan cache does not permit the introduction of another major version. Consequently, we are required to forcibly remove the pods.

Helm chart: prometheus

Namespace: monitoring

Chart version: 25.21.0

App version: v2.52.0

Note: an affinity rule was necessary to implement because the Daemonset attempted to deploy a pod on a Fargate node, an action that is unfeasible due to the existing taints. The YAML configuration can be incorporated into the Helm chart values within Kubeapps.

wide760prometheus-node-exporter:
affinity:
nodeAffinity:
requiredDuringSchedulingIgnoredDuringExecution:
nodeSelectorTerms:
- matchExpressions:
- key: "eks.amazonaws.com/compute-type"
operator: "NotIn"
values:
- "fargate"

Helm chart: thanos

Namespace: monitoring

Chart version: 15.6.0

App version: 0.35.1

Note: the upgrade was executed seamlessly, with no issues identified.

Helm chart: aws-for-fluent-bit

Namespace: amazon-cloudwatch

Chart version: 0.1.33

App version: 2.32.2.20240425

Note: an affinity rule was necessary to implement because the Daemonset attempted to deploy a pod on a Fargate node, an action that is unfeasible due to the existing taints. The YAML configuration can be incorporated into the Helm chart values within Kubeapps.

wide760tolerations:
[
{
effect: "NoSchedule",
key: "node-role.kubernetes.io/master",
operator: "Exists"
},
{ effect: "NoExecute", operator: "Exists" },
{ effect: "NoSchedule", operator: "Exists" },
{
effect: "NoSchedule",
key: "eks.amazonaws.com/compute-type",
operator: "Equal",
value: "fargate"
}
]
affinity:
nodeAffinity:
requiredDuringSchedulingIgnoredDuringExecution:
nodeSelectorTerms:
- matchExpressions:
- key: "eks.amazonaws.com/compute-type"
operator: "NotIn"
values:
- "fargate"

**After the upgrade, verify that Fluent Bit is still running and sending logs to AWS. Additionally, ensure that Fluent Bit is checked regularly.**

Helm chart: tigera-operator

Namespace: tigera-operator

Chart version: v3.28.0

App version: v3.28.0

Note: a patch was required for the Daemonset 'csi-node-driver' to prohibit the deployment of a pod on a Fargate node. This action was required to be executed in the terminal.

wide1011kubectl patch -n tigera-operator installations.operator.tigera.io default --type='merge' -p '{
"spec": {
"csiNodeDriverDaemonSet": {
"spec": {
"template": {
"spec": {
"affinity": {
"nodeAffinity": {
"requiredDuringSchedulingIgnoredDuringExecution": {
"nodeSelectorTerms": [
{
"matchExpressions": [
{
"key": "eks.amazonaws.com/compute-type",
"operator": "NotIn",
"values": [
"fargate"
]
}
]
}
]
}
}
}
}
}
}
}
}
}'

Helm chart: aws-load-balancer-controller

Namespace: kube-system

Chart version: 1.8.1

App version: v2.8.1

Note: the upgrade was executed seamlessly, with no issues identified.

Helm chart: external-dns

Namespace: external-dns

Chart version: 7.5.2

App version: 0.14.2

Note: the setting for "pdb" was adjusted to false in the Helm chart values, as it was deemed unnecessary.

Not all applications are available to upgrade with Kubeapps. The following applications needs to be upgraded manually.

* Velero (<https://velero.io/> )

## 3. Check if applications are running feature branches

Using one of the scripts in <https://github.com/teqplay/kubernetes-scripts/tree/master/get-images-script>

to get a list of all images used in a cluster verify if any applications are running feature branches to then check if these feature branch image still exists in ECR if it does not exits Kubernetes won’t be able to pull the image

## 4. Upgrade EKS cluster

# Final UPGRADE

## Announcement upgrading Kubernetes cluster

Alert individuals via Slack regarding the upcoming Kubernetes cluster upgrade. Anticipate downtime during this process. Copy and paste the following text in Slack:

DEVELOP

> Today, we are initiating the upgrade of the Kubernetes cluster DEVELOP to version x.xx (please replace with the actual version). Please be aware that downtime is expected throughout this process.

PRODUCTION

> Today, we are initiating the upgrade of the Kubernetes cluster PRODUCTION to version x.xx (please replace with the actual version). Please be aware that downtime is expected throughout this process.

Following the upgrade of the EKS Add-ons and Helm charts in the PRODUCTION cluster, it's necessary to alert the DevOps team via email that we're ready for the upgrade. Below is a sample email to notify the team. Please adjust the version and upgrade time as needed. A confirmation is required before proceeding with the final upgrade.

wide760Dear Team,
I hope this message finds you well. I am writing to inform you that the
necessary preparations for upgrading our Kubernetes cluster to
version 1.28 have been successfully completed.
We are now ready to proceed with the actual upgrade
process. The proposed schedule for this upgrade is Thursday, June 20th, 2024,
between 14:00 and 16:00. This time slot has been chosen with the aim of
minimizing any potential disruption to our services.
The applications may be down for a couple of minutes.
Please let us know if this proposed time slot aligns with the schedule
or if there are any concerns that need to be addressed. Thank you for
your attention to this matter.
Best Regards,

Upon availability of a new Kubernetes version, you'll notice an "update now" button on the EKS dashboard. Click the button to initiate the cluster upgrade, bearing in mind that this process may take approximately 10-15 minutes, as of the current writing.

## 5. Upgrade MongoDB cluster

The first step is to create a new nodegroup for mongodb-arbiters. Remove the old nodegroup when the new one was created.

1. mongodb-arbiters-<DATE>

**mongodb-arbiters-<DATE>**

Add the taint:

key: nodegroup

value: mongo-arbiters

effect: NoSchedule

Add label:

key: [app.teqplay.nl/nodegroup](http://app.teqplay.nl/nodegroup)

value: mongo-arbiters

Add subnet:

Subnet: subnet-6f2da718

Some node groups are not allowed to be upgraded automatically. The node groups with MongoDB replicas clusters needs to be upgraded manually, because the MongoDB replicas hosts are DNS records in Route 53 and are created dynamically. It takes some time before the new DNS records are propagated and for that reason it’s impossible to upgrade the node groups automatically, which goes to fast. The application won’t be able to resolve the new DNS hostnames fast enough.

For the following node groups use the “add new node group” option.

1. mongodb-replicas-<DATE>

The new node group needs to be created first.

**mongodb-replicas-<DATE>**

Add the taint:

key: nodegroup

value: mongo-replicas

effect: NoSchedule

Add label:

key: [app.teqplay.nl/nodegroup](http://app.teqplay.nl/nodegroup)

value: mongo-replicas

Add subnet:

Subnet: subnet-6f2da718

### Steps to move from the old to the new node group

First get the nodes of the old node group. These can be retrieved via the MongoDB pods. Try to follow the examples below. The ID’s in the cluster differs from the examples here below, so don’t copy and paste the values used in the examples!

wide760kubectl describe pod mongodb-pomadev-0
Name: mongodb-pomadev-0
Namespace: teqplay-app
Priority: 0
Service Account: mongodb-pomadev
Node: ip-172-31-28-246.eu-west-1.compute.internal/172.31.28.246
Start Time: Thu, 27 Jul 2023 13:33:33 +0200
Labels: app.kubernetes.io/component=mongodb
app.kubernetes.io/instance=mongodb-pomadev
app.kubernetes.io/managed-by=Helm
app.kubernetes.io/name=mongodb
controller-revision-hash=mongodb-pomadev-69dfbcf79d
helm.sh/chart=mongodb-13.15.1
statefulset.kubernetes.io/pod-name=mongodb-pomadev-0

The node ID for `mongodb-pomadev-0`` is `ip-172-31-28-246.eu-west-1.compute.internal` and for the second one is `ip-172-31-17-42.eu-west-1.compute.internal`.

Check the installed pods of the replicas in the node.

wide760kubectl describe node ip-172-31-28-246.eu-west-1.compute.internal
......
Non-terminated Pods: (10 in total)
Namespace Name CPU Requests CPU Limits Memory Requests Memory Limits Age
--------- ---- ------------ ---------- --------------- ------------- ---
amazon-cloudwatch aws-for-fluent-bit-gb7q2 50m (2%) 0 (0%) 50Mi (1%) 250Mi (7%) 73m
calico-system calico-node-jzg5s 0 (0%) 0 (0%) 0 (0%) 0 (0%) 73m
calico-system csi-node-driver-8kj88 0 (0%) 0 (0%) 0 (0%) 0 (0%) 73m
kube-system aws-node-7fp5t 25m (1%) 0 (0%) 0 (0%) 0 (0%) 73m
kube-system ebs-csi-node-r5bsj 30m (1%) 0 (0%) 120Mi (3%) 768Mi (23%) 73m
kube-system kube-proxy-tpjkn 100m (5%) 0 (0%) 0 (0%) 0 (0%) 73m
lens-metrics node-exporter-mmgmg 10m (0%) 200m (10%) 24Mi (0%) 100Mi (3%) 73m
monitoring prometheus-prometheus-node-exporter-k5xks 0 (0%) 0 (0%) 0 (0%) 0 (0%) 73m
monitoring zabbix-agent-xb2p6 100m (5%) 100m (5%) 54Mi (1%) 54Mi (1%) 73m
teqplay-app mongodb-pomadev-0 100m (5%) 0 (0%) 500Mi (15%) 500Mi (15%) 56m
Allocated resources:
(Total limits may be over 100 percent, i.e., overcommitted.)

In the above example the pod `mongodb-pomadev-0` is installed on the node. The next step is to cordon the nodes to prevent the Kubernetes scheduler to schedule any new resources on it.

wide760kubectl cordon ip-172-31-28-246.eu-west-1.compute.internal
>> node/ip-172-31-28-246.eu-west-1.compute.internal cordoned
kubectl cordon ip-172-31-17-42.eu-west-1.compute.internal
>> node/ip-172-31-17-42.eu-west-1.compute.internal cordoned

The next step is to drain one node only and wait around 10-15 minutes to drain the next node.

wide760kubectl drain --ignore-daemonsets ip-172-31-28-246.eu-west-1.compute.internal
>> evicting pod calico-system/calico-typha-5bf5c8b799-5dhlw
>> evicting pod teqplay-app/mongodb-pomadev-0
>> pod/mongodb-pomadev-0 evicted
>> pod/calico-typha-5bf5c8b799-5dhlw evicted
>> node/ip-172-31-31-234.eu-west-1.compute.internal drained

Inspect the DNS host of the evicted MongoDB pod. Typically, wait for a duration of 6-10 minutes to ensure a 100% confirmation before proceeding to drain the next node.. Also check if the POMA application is working properly (<https://pomadev.teqplay.nl> for DEVELOP).

Try to connect to the Poma on address `poma-dev-mongodb-0.eks-dev.teqplay`.

When all is still good, continue to drain the next node.

wide760kubectl drain --ignore-daemonsets ip-172-31-17-42.eu-west-1.compute.internal

Check if de pods are all up and running, before removing the old node groups in AWS.

wide760kubectl get pods -n core-service | grep poma-dev-mongodb
mongodb-pomadev-0 2/2 Running 0 71m
mongodb-pomadev-1 2/2 Running 0 61m
mongodb-pomadev-arbiter-0 1/1 Running 0 47h

## 6. Upgrade node groups automatically

Before creating new nodes, check the other cluster node configurations.

Every node group has a “update now“ button, **after the upgrade of Kubernetes**. To upgrade a node group there are two options.

Not all node groups are allowed to be upgraded automatically. Some node groups needs to be upgraded manually. See chapter 5 Upgrade node groups manually.

For the following node groups use the “add new node group” option.

1. ais-engine-<DATE>
2. ship-history-mongo-<DATE>
3. develop-nodes-<DATE> or production-nodes-<DATE>

Create a new node-group with a unique name. For example develop-nodes-<today>. After the creation of the node-group, remove the old one. AWS will redeploy pods from the old node to the new node. This is the most efficient way to upgrade the node. Using the “upgrade button“ for these node groups will result into a longer downtime of various applications.

**ais-engine-<DATE>**

Add the taint:

key: nodegroup

value: ais-engine

effect: NoSchedule

Add label:

key: app.teqplay.nl/nodegroup

value: ais-engine

Add subnet:

Subnet: subnet-6f2da718

**!ATTENTION**

Prior to upgrading the nodes, reduce the scale of the specified deployments. After completing the nodegroup upgrade to the new Kubernetes version, resume the deployments by scaling them back up.

* ais-rabbitmq (ais-processing)
* ais-stream (ais-core)
* event-history-processor (ais-processing**)**

Scale down!

**DEVELOP cluster**

wide760kubectl scale --replicas=0 deploy/ais-stream-dev -n ais-core
kubectl scale --replicas=0 deploy/ais-rabbitmq-dev -n ais-processing
kubectl scale --replicas=0 deploy/event-history-processor-dev -n ais-processing

**PRODUCTION cluster**

wide760kubectl scale --replicas=0 deploy/ais-stream -n ais-core
kubectl scale --replicas=0 deploy/ais-rabbitmq -n ais-processing
kubectl scale --replicas=0 deploy/event-history-processor -n ais-processing

Scale up!

**DEVELOP cluster**

wide760kubectl scale --replicas=1 deploy/ais-stream-dev -n ais-core
kubectl scale --replicas=1 deploy/ais-rabbitmq-dev -n ais-processing
kubectl scale --replicas=1 deploy/event-history-processor-dev -n ais-processing

**PRODUCTION cluster**

wide760kubectl scale --replicas=1 deploy/ais-stream -n ais-core
kubectl scale --replicas=1 deploy/ais-rabbitmq -n ais-processing
kubectl scale --replicas=1 deploy/event-history-processor -n ais-processing

**ship-history-mongo-<DATE>**

Add the taint:

key: nodegroup

value: ship-history-mongo

effect: NoSchedule

Add label:

key: app.teqplay.nl/nodegroup

value: ship-history-mongo

Add subnet:

Subnet: subnet-6f2da718

**!ATTENTION**

Prior to upgrading the nodes, reduce the scale of the specified deployments. After completing the nodegroup upgrade to the new Kubernetes version, resume the deployments by scaling them back up.

* ship-history-processor (ais-processing)

Scale down!

**DEVELOP cluster**

wide760kubectl scale --replicas=0 deploy/ship-history-processor-dev -n ais-processing

**PRODUCTION cluster**

wide760kubectl scale --replicas=0 deploy/ship-history-processor -n ais-processing

Scale up!

**DEVELOP cluster**

wide760kubectl scale --replicas=1 deploy/ship-history-processor-dev -n ais-processing

**PRODUCTION cluster**

wide760kubectl scale --replicas=1 deploy/ship-history-processor -n ais-processing

**develop-nodes-<DATE> or production-nodes-<DATE>**

This nodegroup currently lacks any labels or taints.

**!ATTENTION**

Prior to upgrading the nodes, reduce the scale of the specified deployments. After completing the nodegroup upgrade to the new Kubernetes version, resume the deployments by scaling them back up.

* terminallineup
* vesselcompliance
* vesselvoyage

Scale down!

**DEVELOP cluster**

wide760kubectl scale --replicas=0 deploy/terminallineup-dev -n general-service
kubectl scale --replicas=0 deploy/vesselcompliance-dev -n customer-apps
kubectl scale --replicas=0 deploy/vesselcompliance-staging -n customer-apps
kubectl scale --replicas=0 deploy/vesselvoyage-dev -n voyage

**PRODUCTION cluster**

wide760kubectl scale --replicas=0 deploy/terminallineup -n general-service
kubectl scale --replicas=0 deploy/vesselcompliance -n customer-apps
kubectl scale --replicas=0 deploy/vesselvoyage -n voyage

Scale up!

**DEVELOP cluster**

wide760kubectl scale --replicas=1 deploy/terminallineup-dev -n general-service
kubectl scale --replicas=1 deploy/vesselcompliance-dev -n customer-apps
kubectl scale --replicas=1 deploy/vesselcompliance-staging -n customer-apps
kubectl scale --replicas=1 deploy/vesselvoyage-dev -n voyage

**PRODUCTION cluster**

wide760kubectl scale --replicas=1 deploy/terminallineup -n general-service
kubectl scale --replicas=1 deploy/vesselcompliance -n customer-apps
kubectl scale --replicas=1 deploy/vesselvoyage -n voyage

### Node group compute, nats, rabbitmq and others

Only for the node group “compute“ use the “upgrade now“ button. Choose “Rolling update“ option. Only after ais-engine is online.

## 7. Check workings applications and database

Verify the operational status of all Teqplay applications and databases to ensure their continued functionality.

## 8. Check Grafana & Revents

We need to verify the monitoring system to ensure that data processing is occurring as expected.

Also check if Revents-engine is working correctly by checking the `revents-engine-orchestrator` and`revents-engine-orchestrator-data` log files and see there are no errors

## 9. Create alarms

Don’t forget to remove the alarms for the old auto scaling groups in Cloudwatch Alarms! Missing data is treated as an alarm.

Use the script `check_asg_cpu_alarms.sh` in the `kubernetes-scripts` to create new alarms for the new auto scaling groups.

## 10. Inform in Slack once the upgrade has been successfully completed

Choose between DEVELOP or PRODUCTION cluster.

> The Kubernetes DEVELOP cluster upgrade has been successfully completed.

> The Kubernetes PRODUCTION cluster upgrade has been successfully completed.