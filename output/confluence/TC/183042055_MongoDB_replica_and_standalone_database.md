---
id: confluence:183042055
source: confluence
type: page
space: TC
title: MongoDB replica and standalone database
author: Minh Trang Nguyen (Unlicensed)
date: '2023-09-16'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/183042055
explicit_links: []
---
# MongoDB replica and standalone database

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/183042055  

## Content

## Bitnami MongoDB Helm chart

<https://github.com/bitnami/charts/tree/main/bitnami/mongodb>

The `Bitnami MongoDB Helm chart` is well maintained and is used for creating single and replica databases. The MongoDB won't be packaged together with an application, but exist separately.

* The standalone database needs to use the `values-standalone.yaml` file.
* The replica database needs to use the `values-replica.yaml` file.

## MongoDB replica initialisation script

External access in the MongoDB replica architecture was intended for service type `LoadBalancer`, which means for each replica pod a new AWS loadbalancer was created. This is not an ideal solution, so in the Helm Chart values file a custom piece of code was added. The code will set the external DNS domain names in the replica, which is required to be able to make a connection with MongoDB replica cluster via the DNS domains.

In the values file an environment variable of the domain needs to be set, see the snippet below.

extraEnvVars:
- name: DNS\_DOMAIN
value: eks-dev.teqplay

The script is located in the `initdbScripts` section.

initdbScripts:
mongo\_replica\_eks\_script.sh: |
#!/bin/bash

* The algorithm checks if the cluster is online, before doing any further actions. It will retry after 30 seconds after each check.
* With the help of the headless service, the algorithm try to find the primary node.
* When the replica cluster has the status `ok` the algorithm needs to have a list of MongoDB hosts. The list of hosts names are replaced with the `Route53` domain names e.g. `mongodb-rep-0.eks-dev.teqplay` and the cluster is reconfigured with the new `External-DNS` domains.

## Resource policy

All MongoDB instances uses the storage class `gp3-retained``, to retain the data after removal of the deployment.

## MongoDB secrets

The Helm chart requires an existing secret, so for each new MongoDB replica database a new secret needs to be generated. Replace the “SECRET\_NAME“ with the name of the secret e.g. mongodb-replica-secret.

Linux and Windows (via Git bash or WSL)

kubectl create secret generic <SECRET\_NAME> \
--from-literal=mongodb-root-password="$(openssl rand -base64 32)" \
--from-literal=mongodb-passwords="$(openssl rand -base64 32)" \
--from-literal=mongodb-replica-set-key="$(openssl rand -base64 32)"

Example

kubectl create secret generic mongodb-replica-secret \
--from-literal=mongodb-root-password="$(openssl rand -base64 32)" \
--from-literal=mongodb-passwords="$(openssl rand -base64 32)" \
--from-literal=mongodb-replica-set-key="$(openssl rand -base64 32)"

Paste the secret name in the `values.yaml` file.

auth:
existingSecret: mongodb-replica-secret

The secret has 3 fields:

* **mongodb-root-password**: root password.
* **mongodb-passwords**: password for users.
* **mongodb-replica-set-key**: key to authenticate each member of the same deployment.

## Replica Set Arbiter

MongoDB replica arbiters are located in a separate node group named “mongodb-replica-<DATE>”. The arbiter needs to be in a separated node group, because a cluster can be corrupted when the arbiter and primary/secondary are on the same node. See a snippet of the MongoDB documentation below.

Figure 1: don’t run arbiter on the same host as the primary / secondary

**EKS cluster**

In the EKS cluster two node groups exists specific for MongoDB replicas. The node groups are:

* mongodb-arbiters-<DATE CREATED>
* mongodb-replicas-<DATE CREATED>

Arbiters are not allowed to mix with MongoDB replicas. Only one arbiter is allowed per replica set, because the amount of replicas isn’t allowed to be set in the Helm chart.

**Updating Kubernetes cluster**

After upgrading the Kubernetes cluster to a new version, upgrade the node group with the MongoDB arbiters first. An arbiter is within a minute transferred to the new node group.

**Helm chart upgrading via KubeApps**

Upgrades needs to be done in little steps via the upgrade button of `KubeApps`. The maintainer `Bitnami` are doing a good job to make it simple and easy to upgrade to a higher versions. There was no problem to upgrade from MongoDB 5 to 6 in the tests.

Also a test was done by manually setting the Docker image tag of MongoDB and try to upgrade. This process failed, the cluster got corrupted and the replica needed to be fixed.

## Database export and import

The process of exporting data from the old MongoDB database and importing into the new MongoDB database is done via a `Job`. The template is available in the repo `` kubernetes-scripts` `` directory `mongodb-export-import`. The template needs to filled with the correct values to be of use. Follow the instructions in the `README.md` document.

The job will export data from the old database and import into the new database. After the importing it will compare the old data with the data imported into the new database. This will guarantee that the data has been transferred correctly.

**Helm install**

<https://github.com/bitnami/charts/tree/main/bitnami/mongodb>

Example:

helm upgrade --install testmongo oci://registry-1.docker.io/bitnamicharts/mongodb -f values-dev.yaml