---
id: confluence:397606914
source: confluence
type: page
space: TC
title: 'Managing Network Policies: Creation, Modification, and Deletion'
author: Minh Trang Nguyen (Unlicensed)
date: '2024-07-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/397606914
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/397606914
---
# Managing Network Policies: Creation, Modification, and Deletion

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/397606914  

## Content

Network policies are organized within the repository at `https://bitbucket.org/teqplay/kubernetes-scripts/src/master/cluster-network-policies/environments/` tailored for both development and production environments due to deployment name variations.

Structure of the directory:

cluster-network-policies
├── environments
│ ├── all
│ ├── develop
│ ├── production
│ ├── apply-policies-develop.sh
│ ├── apply-policies-production.sh
│ ├── remove-policies-develop.sh
│ └── remove-policies-production.sh

The `all` directory houses network policies intended for universal application across namespaces. The `develop` and `production` directories contain namespace-specific, application-related network policies.

Scripts included:

* `apply-policies-develop.sh` and `apply-policies-production.sh` automate the application of network policies across namespaces.
* `remove-policies-develop.sh` and `remove-policies-production.sh` facilitate the removal of all network policies.

## Establishing a New Namespace and Install new Applications

Initiate a new branch for the repository located at `<https://bitbucket.org/teqplay/kubernetes-scripts/`.

Upon creating a new namespace, several essential steps must be undertaken:

1. **Directory Creation**: For both the "develop" and "production" environments, generate directories named after the new namespace. This ensures organised storage and management of environment-specific configurations.
2. **Network Policies Manifest**: In the directories created for the new namespace, generate manifest files for network policies. These files define the rules governing traffic flow to and from the pods within the namespace, enhancing security and operational efficiency.
3. **Script Updates**: Amend the deployment scripts to include commands for applying the network policies in the new namespace. Similarly, update the removal scripts to ensure that these policies can be cleanly retracted when necessary. This step integrates the new namespace into the existing automation workflows, facilitating smooth operations and maintenance.

### Creating new Network Policies for Applications

For enhanced readability and management, each application requires separate templates for "ingress" and "egress" network policies. This deliberate separation facilitates easier understanding and modification of the network traffic rules specific to each application.

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
name: <name of the network policy name>-<ingress or egress>
namespace: <name of the namespace>
spec:
podSelector:
matchLabels:
app.kubernetes.io/instance: <name of the instance>
app.kubernetes.io/name: <name of the application>
policyTypes:
- Ingress
ingress:
- ports:
- protocol: TCP
port: 8080

#### Ingress

In the section "ingress" add the ports.

**Example:**

 ingress:
- ports:
- protocol: TCP
port: 8000

#### Egress

The principle stays the same, add the ports to the egress section.

**Example:**

 egress:
- ports:
- protocol: TCP
port: 8000

#### PodSelector matchlabels

Typically, selecting pods for network policy application requires matching just two labels as displayed the above example. One can test this in the terminal if the correct pods are selected by the defined labels.

Example:

kubectl get pods -l app.kubernetes.io/instance=portmatcher-dev,app.kubernetes.io/name=skeleton-mongo-app

Add the commands to apply the new namespace network policies.

**script:** apply-policies-develop.sh

...
kubectl apply -f develop/new-namespace ; kubectl apply -f all -n new-namespace

**script:** remove-policies-develop.sh

...
kubectl delete -f develop/new-namespace ; kubectl delete -f all -n new-namespace

**script:** apply-policies-production.sh

...
kubectl apply -f production/new-namespace ; kubectl apply -f all -n new-namespace

**script:** remove-policies-production.sh

...
kubectl delete -f production/new-namespace ; kubectl delete -f all -n new-namespace

#### Update documentation

Please enhance the documentation by incorporating a new table that outlines the new namespace and network policies applicable to the applications for DEVELOP and PRODUCTION. Refer to the existing documentation for guidance.

Cluster network policies details

#### Permissions

In order to apply, modify, or revoke network policies, one must possess the privileges associated with the 'devops' or 'techsupport' groups. Please consult your system administrator to acquire these permissions.