---
id: confluence:87359493
source: confluence
type: page
space: TC
title: Configure a new user in EKS
author: Darius Wattimena
date: '2022-02-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/87359493
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/87359493
---
# Configure a new user in EKS

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/87359493  

## Content

To configure a new user in EKS, it is expected to have full access to AWS IAM, EKS and the desired cluster.

You must take the following steps to give someone access to the EKS cluster. Changes need to be made on the side of Amazon IAM and on the cluster where access is required.

## Configure IAM

The user should have access to the `EKSFullAccess` or something more tailored if this is needed. Out of the box, this should already work if the user has the `developer` role.

## Configure EKS

Update the `aws-auth` ConfigMap, which you can find in the `kube-system` namespace. Change the `mapUsers` array in the `data` object of the ConfigMap. Add a new user entry; adding a user can be done by calling `kubectl`, however, I recommend changing the ConfigMap inside of Lens.

kubectl edit configmap aws-auth -n kube-system

An example entry can look as follows:

yaml- userarn: arn:aws:iam::050356841556:user/demo.student
username: demo.student
groups:
- system:bootstrappers
- system:nodes
- eks-console-dashboard-full-access-group

Keep in mind that the `username` needs to be unique. For good practice, it is recommended to fill in the AWS IAM username. The provided `groups` array are `Cluster Roles` and not `Roles` which are only on namespace level.

Giving someone full access would look as follows:

yaml- userarn: arn:aws:iam::050356841556:user/circle-ci
username: circle-ci
groups:
- system:masters