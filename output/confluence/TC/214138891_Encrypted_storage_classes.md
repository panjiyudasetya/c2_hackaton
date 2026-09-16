---
id: confluence:214138891
source: confluence
type: page
space: TC
title: Encrypted storage classes
author: Minh Trang Nguyen (Unlicensed)
date: '2023-09-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214138891
explicit_links: []
---
# Encrypted storage classes

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214138891  

## Content

In the clusters storage classes are available to create encrypted EBS volumes. Use these classes when high security is required. The storage classes are:

* **gp3-encrypt:** This storage class will create encrypted EBS volumes with the encryption key of the  
  cluster (develop or production). Volumes are not retained.
* **gp3-retain-encrypt:** the volumes are retained.

## Policy

The encryption key for clusters `develop` and `production` are managed in AWS Key Management Service (KMS). It’s not possible to remove the encryption keys.

The EBS CSI driver inherit the role `NodeInstanceRoleInfo` and at that location the policy was created to allow the cluster to create encrypted volumes. See below the pictures of the EBS driver and the role nodes and how to make adjustments to the policy.

Changes regarding the policy needs to be done in `EBSKMSCreateandAttach`. The resources are the encryption keys for cluster `develop` and `production`.

{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "EBSKMSCreateandAttach",
"Effect": "Allow",
"Action": [
"kms:Decrypt",
"kms:GenerateDataKeyWithoutPlaintext",
"kms:CreateGrant"
],
"Resource": [
"arn:aws:kms:eu-west-1:050356841556:key/00934cd1-fde9-418d-8144-f7265259be14",
"arn:aws:kms:eu-west-1:050356841556:key/283b9db4-b661-4a31-b63a-99e7f710c551"
]
}
]
}