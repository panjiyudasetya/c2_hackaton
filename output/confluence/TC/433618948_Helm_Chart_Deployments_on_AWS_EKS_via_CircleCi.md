---
id: confluence:433618948
source: confluence
type: page
space: TC
title: Helm Chart Deployments on AWS EKS via CircleCi
author: Minh Trang Nguyen (Unlicensed)
date: '2024-08-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/433618948
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/433618948
---
# Helm Chart Deployments on AWS EKS via CircleCi

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/433618948  

## Content

status: proposal

The previous method of deploying applications to AWS EKS clusters involved the use of a long-lived Access Token. This token, equipped with credentials, carried permissions granting full access to the AWS EKS clusters. However, the updated deployment approach outlined in this document promises enhanced security compared to the former method.

Figure: process deployment via CircleCi

The diagram provides a clear depiction of the deployment process for a Helm chart application within the AWS EKS cluster, applicable to both Develop and Production environments. The process begins with a manual deployment, where the developer sets up the AWS CLI to retrieve the AWS STS token. This token is crucial for assuming the IAM role 'CircleCiAssumeRoleEks'.

The 'CircleCiAssumeRoleEks' IAM role is not all-encompassing, as it does not provide full access to the EKS cluster. However, it does grant enough permissions to install a Helm chart. For security reasons, the lifespan of the token is kept short.

Once AWS successfully delivers the token, CircleCi proceeds to configure the Kube config file. This step establishes a communication line with the Kubernetes cluster. Subsequently, Helm is installed, paving the way for the Helm chart to be deployed into the cluster.

The EKS cluster then cross-verifies the permissions of the IAM role 'CircleCiAssumeRoleEks' against the Cluster role 'teqplay:deploy:installation' to which it is mapped. The installation of the Helm chart is executed based on these verified permissions.

## IAM role CircleCiAssumeRoleEks

In order to establish communication between CircleCi and AWS STS, an Identity Provider is required. This can be created by using the following URL: '<https://oidc.circleci.com/org/02225313-c824-414e-b600-48219d7c438e>', when creating a new Identity Provider. The identifier ID for this can be found in the CircleCi console under the Organization Settings.

The role associated with this process is designed to have minimal permissions. While the diagram does not detail all permissions, it is important to note that they should be kept to a minimum. To link the role to the Identity Provider, the Trust relationships must be configured as depicted in the diagram.

AWS verifies the 'audience' key field in the JWT token, and for CircleCi, the audience is the organization ID '02225313-c824-414e-b600-48219d7c438e'.

Figure: create identity provider

Figure: set permissions IAM role

Figure: connect IAM role to CircleCi

## Allow access to IAM role

An access entry must be created to grant the IAM role permission to access the EKS cluster. This involves adding the cluster role "teqplay:deploy:installation" to the Group names.

The permissions for the Cluster role can be found in the 'cluster-permissions' directory of the 'kubernetes-scripts' repository.

Figure: EKS cluster access

Example CircleCD config

version: '2.1'
orbs:
aws-cli: circleci/aws-cli@4.0
jobs:
aws-cli-example:
executor: aws-cli/default
steps:
- checkout
- aws-cli/setup:
profile\_name: WEB IDENTITY PROFILE
role\_arn: arn:aws:iam::050356841556:role/CircleCiAssumeRoleEks
role\_session\_name: example-session
- run:
name: Install kubectl
command: |
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
- run:
name: Setup kubeconfig
command: |
aws eks update-kubeconfig --region eu-west-1 --name develop
- run:
name: Run kubectl get ns
command: |
kubectl get ns
- run:
name: Install Helm
command: |
curl -fsSL -o get\_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get\_helm.sh
./get\_helm.sh
- run:
name: Show all Helm charts
command: |
helm list -A
workflows:
aws-cli:
jobs:
- aws-cli-example:
context: aws