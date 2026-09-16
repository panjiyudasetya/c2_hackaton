---
id: confluence:297828376
source: confluence
type: page
space: TC
title: Restoring cluster Node when it crashes
author: Minh Trang Nguyen (Unlicensed)
date: '2024-03-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/297828376
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/297828376
---
# Restoring cluster Node when it crashes

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/297828376  

## Content

This document outlines the process for resolving a MongoDB database crash, specifically for the database named "ship-history-processor-dev-mongodb". The steps provided aim to restore the database node to a functional state within approximately 5-7 minutes. All actions are performed through the terminal interface. In this document, a test node is utilized to exemplify the process.

kubectl get nodes
NAME STATUS ROLES AGE VERSION
ip-172-31-17-211.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-17-75.eu-west-1.compute.internal Ready <none> 6m39s v1.26.12-eks-5e0fdde
ip-172-31-18-173.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-18-196.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-18-204.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-18-4.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-19-155.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-20-218.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-20-51.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-21-203.eu-west-1.compute.internal Ready <none> 18d v1.26.10-eks-e71965b
ip-172-31-22-200.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-25-72.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-26-199.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-182.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-38.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-88.eu-west-1.compute.internal Ready <none> 18d v1.26.10-eks-e71965b

The test node, identified as `ip-172-31-17-75.eu-west-1.compute.internal`, will be deliberately rendered non-functional by executing a fork bomb to illustrate the steps. It's essential to note that this action is strictly for demonstration purposes and should never be performed on actual develop and production nodes.

## Node crashed!

As soon as the node crashes, it should become apparent in the monitoring system. At this point, the following steps should be undertaken:

Verify if the mounted storages are retained. In the case of `ship-history-processor-dev-mongodb`, this was confirmed. The screenshot below depicts the volume state as "In-use," indicating that everything is functioning as expected.

When a nodes crashes this is visible in the status of the node `NotReady``.

kubectl get nodes
ip-172-31-17-211.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-17-75.eu-west-1.compute.internal NotReady <none> 48m v1.26.12-eks-5e0fdde
ip-172-31-18-173.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-18-196.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-18-204.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-18-4.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-19-155.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-20-218.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-20-51.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-21-203.eu-west-1.compute.internal Ready <none> 18d v1.26.10-eks-e71965b
ip-172-31-22-200.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-25-72.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-26-199.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-182.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-38.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-88.eu-west-1.compute.internal Ready <none> 18d v1.26.10-eks-e71965b

**Step 1: cordon the node first**

kubectl cordon ip-172-31-17-75.eu-west-1.compute.internal

**Step 2: get the values for the deployment and namespace.**

kubectl get deploy -n ais-processing
NAME READY UP-TO-DATE AVAILABLE AGE
ais-diff-dev 1/1 1 1 160d
ais-engine-dev-mongodb 1/1 1 1 153d
ais-rabbitmq-dev 1/1 1 1 160d
ais-rabbitmq-dev-mongodb 1/1 1 1 160d
anchor-monitor-dev 1/1 1 1 160d
area-monitor-dev-mongodb 1/1 1 1 160d
berth-monitor-dev 1/1 1 1 160d
encounter-monitor-dev 1/1 1 1 160d
event-converter-dev 1/1 1 1 160d
event-history-dev 3/3 3 3 159d
event-history-migrator 0/0 0 0 138d
event-history-processor-dev 1/1 1 1 159d
event-history-processor-dev-mongodb 1/1 1 1 159d
ship-history-dev 3/3 3 3 160d
ship-history-processor-dev 1/1 1 1 160d
ship-history-processor-dev-mongodb 1/1 1 1 160d

**Step 3: scale down deployment**

Scale down the deployment to 0 replicas. Replace "DEPLOYMENT\_NAME" and "NAMESPACE" with the appropriate values.

kubectl scale --replicas=0 deploy/<DEPLOYMENT\_NAME> -n <NAMESPACE>

Example:

kubectl scale --replicas=0 deploy/ship-history-processor-dev-mongodb -n ais-processing

**Step 4: force remove the POD**

Force remove the pod from Kubernetes cluster.

kubectl delete pod --force <POD\_NAME>

**Step 5: scale up the node by one instance**

We need to add a new node to facilitate the deployment migration.

kubectl get nodes
ip-172-31-16-214.eu-west-1.compute.internal Ready <none> 25s v1.26.12-eks-5e0fdde
ip-172-31-17-211.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-17-75.eu-west-1.compute.internal NotReady,SchedulingDisabled <none> 51m v1.26.12-eks-5e0fdde
ip-172-31-18-173.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-18-196.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-18-204.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-18-4.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-19-155.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-20-218.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-20-51.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-21-203.eu-west-1.compute.internal Ready <none> 18d v1.26.10-eks-e71965b
ip-172-31-22-200.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-25-72.eu-west-1.compute.internal Ready <none> 62d v1.26.10-eks-e71965b
ip-172-31-26-199.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-182.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-38.eu-west-1.compute.internal Ready <none> 63d v1.26.10-eks-e71965b
ip-172-31-28-88.eu-west-1.compute.internal Ready <none> 18d v1.26.10-eks-e71965b

The new node with the hostname `ip-172-31-16-214.eu-west-1.compute.internal` has been successfully created, as shown in the terminal output.

**Step 6: reduce the node count back to one**

Resize the node count back to one and await the removal of the node.

**Step 7: check if the block storage volume is available**

**Step 8: scale deployment replicas back to one**

Once AWS removes the crashed node, scale the deployment back to one pod using the deployment configuration.

kubectl scale --replicas=1 deploy/<DEPLOYMENT\_NAME> -n <NAMESPACE>

Example:

kubectl scale --replicas=1 deploy/ship-history-processor-dev-mongodb -n ais-processing

**FAQ**

question:

The pod doesn’t get up and get stuck by showing the message “**Multi-Attach error for volume "pvc-7761b0f5-213f-43ec-b916-92d8d4e90cb8" Volume is already exclusively attached to one node and can't be attached to another**“.

answer:

It appears that AWS didn't completely remove the attachment. Scale the deployment back to zero replicas, wait for one minute, and then attempt to scale up again. During testing, this occurrence was observed only once out of six attempts.