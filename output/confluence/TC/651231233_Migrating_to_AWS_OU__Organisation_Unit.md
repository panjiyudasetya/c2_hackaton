---
id: confluence:651231233
source: confluence
type: page
space: TC
title: Migrating to AWS OU (Organisation Unit)
author: Minh Trang Nguyen (Unlicensed)
date: '2025-07-17'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651231233
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651231233
---
# Migrating to AWS OU (Organisation Unit)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651231233  

## Content

**Status: concept**

This document outlines the steps to set up a new environment and migrate existing resources to it.

## Prerequisites

* AWS CLI
* kubectl
* eksctl (<https://eksctl.io/installation/>)
* An AWS account with the necessary permissions

## Create OU

Begin by creating a new OU in the AWS Organizations console.

1. Select the unit `Development` and click `Add an AWS account`.

2. Assign the name `Develop OU` or a suitable alternative.
3. Enter an existing email address. This address can be used to reset the root password for this OU. This step is optional.

4. Allow time for the AWS account creation to complete. The newly created account will be visible in the root list (see image below).

5. Select the newly created AWS account and move it to the Development OU or another appropriate OU.

6. Following the account's move to the new OU, create the IAM identity groups as outlined in the document below. For testing and user assignment, create at least the `administrators-develop` group. Finally, assign the created groups to the new OU.

Plan for Restructuring AWS Permissions

7. Click 'Next' and select permission sets. This grants the group access to the new OU.

## Create Symmetric key

AWS KMS (Key Management Service) is a managed service that makes it easy to create and control the encryption keys used to encrypt your data. Navigate to the AWS Key Management Service (KMS) and create a symmetric key.

1. Select `Symmetric` and `Encrypt and decrypt`.

2. Assign the alias `eks-develop-cluster` or another appropriate name for this OU.

3. Grant administrators API permissions to manage this key.

4. The key should be displayed in the list.

## EC2 enable default encryption

Begin by enabling default EBS encryption for this OU.

1. Go to EC2 Dashboard
2. Go to Data protection and security

3. Click button manage

4. Enable encryption and use default encryption key

## IAM roles

To create an EKS cluster, you need to create an IAM role with the necessary permissions. The following roles are required.

* TeqplayNodeInstanceRole
* TeqplayServiceRoleForAmazonEKS
* AmazonEKSFargatePodExecutionRole

### TeqplayNodeInstanceRole

This IAM role enables the EKS cluster to perform essential functions, including EC2 instance management, AWS Load Balancer integration, and external-dns updates to Route 53.

Create custom policies if they do not already exist.

#### Custom AWS Policies

* AllowExternalDNSUpdates

jsonwide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"route53:ChangeResourceRecordSets"
],
"Resource": [
"arn:aws:route53:::hostedzone/\*"
]
},
{
"Effect": "Allow",
"Action": [
"route53:ListHostedZones",
"route53:ListResourceRecordSets"
],
"Resource": [
"\*"
]
}
]
}

* EBSKMSCreateandAttach

jsonwide760{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "EBSKMSCreateandAttach",
"Effect": "Allow",
"Action": [
"kms:Decrypt",
"kms:GenerateDataKeyWithoutPlaintext",
"kms:CreateGrant",
"kms:Encrypt",
"kms:RevokeGrant",
"kms:GenerateDataKey",
"kms:ReEncryptTo",
"kms:DescribeKey",
"kms:CreateGrant",
"kms:ListGrants"
],
"Resource": [
"<Put here the KMS Keys ARN>"
]
}
]
}

In the resource section, enter the ARN retrieved from KMS. See the example image below.

### Create the IAM role

1. Select button `Create role`.

2. Select trusted entity type `ec2`.

3. Attach the following policies to the IAM role.

#### Managed AWS Policies

* AmazonEBSCSIDriverPolicy
* AmazonEC2ContainerRegistryReadOnly
* AmazonEKS\_CNI\_Policy
* AmazonEKSWorkerNodePolicy
* CloudWatchAgentServerPolicy
* CloudWatchLogsFullAccess

4. Set the role name `TeqplayNodeInstanceRole`.
5. Set the description `Amazon EKS - Node Group Role`.
6. The final step is to click `Create role`.

### TeqplayServiceRoleForAmazonEKS

This role grants the EKS cluster permissions to manage AWS resources.

1. Create the role.

2. Set the role name `TeqplayServiceRoleForAmazonEKS`.

### AmazonEKSFargatePodExecutionRole

Fargate requires this IAM role to access other services running on Fargate.

1. Create a new policy `eks-fargate-logging-policy` first.

jsonwide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"logs:CreateLogStream",
"logs:CreateLogGroup",
"logs:DescribeLogStreams",
"logs:PutLogEvents"
],
"Resource": "\*"
}
]
}

2. Create IAM role `AmazonEKSFargatePodExecutionRole`.
3. Choose `Custom trust policy`.

jsonwide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Service": "eks-fargate-pods.amazonaws.com"
},
"Action": "sts:AssumeRole"
}
]
}

4. Add permissions

* eks-fargate-logging-policy
* AmazonEKSFargatePodExecutionRolePolicy

5. Save the role and add it to the EKS cluster.

## Github

To configure GitHub to connect to AWS, create an identity provider. The screenshots below illustrate the steps,  
which are detailed at [GitHub Documentation](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services).

The audience (`aud`) in the JWT token identifies the intended recipients. In the context of configuring  
GitHub to connect to AWS, the audience is the value of the `aud` key in the JWT token.

## VPC

An Amazon Virtual Private Cloud (VPC) is a service that allows you to launch AWS resources in a logically  
isolated virtual network that you define. Here are some key features of an AWS VPC:

* Isolation: Provides a secure and isolated environment for your AWS resources.
* Subnets: Allows you to create subnets within your VPC to segment your network.
* Routing: Enables you to define custom route tables to control the traffic flow within your VPC.
* Security: Supports security groups and network ACLs to control inbound and outbound traffic at the instance and subnet levels.
* Internet Gateway: Allows your VPC to connect to the internet.
* VPN Connection: Supports VPN connections to your on-premises network.

To create an EKS cluster, you must first create a VPC. Follow these steps to create a VPC:

## VPC in different availability zone

Deploying Organizational Units (OUs) across multiple availability zones (AZs), i.e., different data centers, is recommended. In eu-west-1, this means utilizing zones a, b, and c. Separating clusters across these zones is preferable, provided it doesn't incur significant cost increases.

## VPC CIDR Allocation Strategy

A CIDR block must be assigned to the VPC. The PRODUCTION environment currently uses `172.31.0.0/16`, providing 65.536 IP addresses, which are divided between public and private subnets. Based on the current setup, this allocation should be sufficient for a new AWS Organizational Unit (OU).

The key consideration is that the new CIDR block must not overlap with an existing one, as conflicting address spaces would prevent connectivity between VPCs.

The IPv4 CIDR block determines the number of available IP addresses in the VPC. An IP address is 32 bits in length. To calculate the number of IP addresses, use the formula `(2^{(32 - n)}`, where `(n)` is the number of bits in the CIDR block. Keep in mind that AWS also reserves some IP addresses for its own use.

Examples:

wide76010.0.0.0/32 = 2^(32-32) = 2^0 = 1 IP address
10.0.0.0/20 = 2^(32-20) = 2^12 = 4.096 IP addresses
10.0.0.0/18 = 2^(32-18) = 2^14 = 16.384 IP addresses

**RFC 1918 Private IP Address Ranges**  
According to RFC 1918 (Address Allocation for Private Internets), the following private IP ranges are available:

10.0.0.0/8 → 16.777.216 addresses (Best for large-scale networks)  
172.16.0.0/12 → 1.048.576 addresses (Flexible and avoids common conflicts)  
192.168.0.0/16 → 65.536 addresses (Common in home and corporate LANs)

For AWS VPCs, we avoid using 192.168.0.0/16 as it is frequently used in home and corporate networks, leading to potential conflicts.

**Choosing Between 10.0.0.0/16 and 172.16.0.0/16**  
The choice between 10.x.x.x/16 and 172.16.x.x/16 depends on future VPC expansion plans:

Use 10.0.0.0/16 if more than 1.048.576 IPs are required across multiple VPCs.

**Example:**  
10.0.0.0/16 → Production VPC  
10.1.0.0/16 → Development VPC  
10.2.0.0/16 → Staging/Testing VPC  
10.3.0.0/16 → Pre-production VPC

Use 172.16.0.0/16 for moderate-scale environments that need easier integration with hybrid networks.

**Recommended Next CIDR for This Setup**

Since `172.31.0.0/16` is the default AWS VPC CIDR, the next best choice within the `172.16.0.0/12` range is:

`172.30.0.0/16`

This ensures non-overlapping address space while keeping the structure within the RFC 1918 private range.

## Create a VPC

When an application requires high availability, it is recommended to use three availability zones. However,  
three availability zones can be expensive. For a cost-effective solution, use two availability zones, which is the minimum for an EKS cluster.

Every new AWS Organizational Unit (OU) comes with a default VPC using the CIDR block `172.31.0.0/16`. Before creating a new VPC, we must first delete the default VPC to be able to create a new VPC.

**Step 1: create VPC**

* Select VPC and more
* Generate name as “teqplaydev“.
* IPv4 CIDR block: `172.30.0.0/16`
* Disable IPv6 CIDR block

* Choose 2 availability zones. Given that the production cluster resides in eu-west-1c, the VPC should be deployed in `eu-west-1a` and `eu-west-1b`.
* Choose 2 public subnets: A public subnet is a VPC subnet that has direct access to the internet through an Internet Gateway (IG).
* Choose 2 private subnets: A private subnet doesn’t have access to the internet.
* Select 1 NAT gateway: A NAT Gateway (Network Address Translation Gateway) is an AWS managed service that allows instances in a private subnet to access the internet or other AWS services without exposing them to inbound internet traffic.
* Create S3 Gateway endpoint: an S3 Gateway Endpoint is a VPC endpoint that allows instances in your VPC to privately connect to Amazon S3 without using the internet, NAT gateway, or public IP addresses.

**Step 2 enable DNS resolution and hostnames**

DNS resolution and hostname enablement are required for EKS node joining. Refer to the red circles in the screenshot for visual clarification.

## NAT gateway

A NAT (Network Address Translation) gateway in AWS is a service that enables instances in a  
private subnet to connect to the internet or other AWS services, but prevents the internet from  
initiating a connection with those instances. Here are some key features:

* Outbound Traffic: Allows instances in a private subnet to initiate outbound traffic to the internet.
* High Availability: Can be deployed in multiple Availability Zones for redundancy.
* Scalability: Automatically scales up to accommodate the bandwidth requirements.
* Managed Service: AWS manages the NAT gateway, reducing the operational overhead.

For AWS services like S3 or ECR, we avoid routing traffic through the NAT gateway to prevent additional costs. Instead, we use VPC endpoints for direct access.

## EKS Cluster

An AWS EKS (Elastic Kubernetes Service) cluster is a managed Kubernetes service provided by Amazon Web Services (AWS). It allows you to run Kubernetes applications on AWS without needing to install and operate your own Kubernetes control plane or nodes. Here are some key features:

* Managed Control Plane: AWS manages the Kubernetes control plane, including the API servers and the etcd database.
* Scalability: EKS can automatically scale your Kubernetes clusters based on demand.
* Security: Integrates with AWS Identity and Access Management (IAM) for authentication and supports network policies for pod security.
* Integration: Seamlessly integrates with other AWS services such as IAM, VPC, and CloudWatch for monitoring and logging.
* High Availability: EKS runs the Kubernetes control plane across multiple Availability Zones to ensure high availability.

### Create cluster

1. Create the cluster named `develop` or use a name specific to the OU.
2. Select `Custom configuration`. EKS Auto Mode is more expensive and manages node creation automatically.
3. Select IAM role `TeqplayServiceRoleForAmazonEKS`.
4. Select the latest Kubernetes version of the current cluster.

5. Select `EKS API` for cluster access.
6. Go to the next step.
7. Select the VPC.
8. Select all subnets.
9. Select the default security groups.
10. Choose `Public and private` option for cluster endpoint access.

11. Enable control plane logs for `API server`, `Audit` and `Authenticator`.

12. Use the default add-ons and select extra `Amazon EBS CSI Driver`.
13. Create the cluster.

## Endpoints

Endpoints in a VPC (Virtual Private Cloud) are used to privately connect your VPC to supported AWS  
services and VPC endpoint services powered by AWS PrivateLink without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. There are two types of VPC endpoints:

1. Interface Endpoints: These are elastic network interfaces (ENIs) with private IP addresses that serve as entry points for traffic destined to a supported service.
2. Gateway Endpoints: These are gateway-type endpoints that you specify as a route target in your route table for traffic destined to a supported AWS service.

Key features of VPC endpoints:

* Private Connectivity: Allows you to connect to AWS services without exposing your traffic to the public internet.
* Security: Enhances security by keeping traffic within the AWS network.
* Cost-Effective: Reduces the need for NAT gateways and other internet-facing resources.

Enable the services:

1. ecr-api: Amazon Elastic Container Registry (ECR) API
2. ecr-dkr: Amazon ECR Docker Registry
3. ec2: Amazon Elastic Compute Cloud (EC2)
4. eks: Amazon Elastic Kubernetes Service (EKS)

After creating the endpoints, the Kubernetes cluster can be created. After creating the cluster the endpoints needs to be updated in the security group.

### ecr-api

1. Assign the name `eks-private-ecr-api-interface`.
2. Select type `AWS services`.
3. Find service `ecr.api`.
4. Select the service.
5. Choose the VPC.
6. Select subnet `eu-west-1c` and `private subnet`.
7. Security groups can be added later, but select all if possible.
8. Create the endpoint.

### ecr-dkr

1. Assign the name `eks-private-ecr-dkr-interface`.
2. Select type `AWS services`.
3. Find service `ecr-dkr`.
4. Select the service.
5. Choose the VPC.
6. Select subnet `eu-west-1c` and `private subnet`.
7. Security groups can be added later, but select all if possible.
8. Create the endpoint.

### ec2

1. Assign the name `eks-private-ec2-interface`.
2. Select type `AWS services`.
3. Find service `ec2`.
4. Select the service.
5. Choose the VPC.
6. Select subnet `eu-west-1c` and `private subnet`.
7. Security groups can be added later, but select all if possible.
8. Create the endpoint.

### eks

1. Assign the name `eks-private-eks-interface`.
2. Select type `AWS services`.
3. Find service `eks`.
4. Select the service.
5. Choose the VPC.
6. Select subnet `eu-west-1c` and `private subnet`.
7. Security groups can be added later, but select all if possible.
8. Create the endpoint.

### eks-auth

1. Assign the name `eks-private-eks-auth-interface`.
2. Select type `AWS services`.
3. Find service `eks-auth`.
4. Select the service.
5. Choose the VPC.
6. Select subnet `eu-west-1c` and `private subnet`.
7. Security groups can be added later, but select all if possible.
8. Create the endpoint.

The `eks-auth` endpoint is required to enable the Kubernetes control plane to provision nodes within the cluster's private subnets.

## Subnets

Applications are segmented into public and private subnets. Public subnets provide internet connectivity, whereas private subnets are isolated, restricting outbound internet access and limiting inbound access for enhanced security. In this section the various applications are

### Auto assign public IPv4

Enable automatic assignment of public IPv4 addresses to the public subnets, as this is necessary for Kubernetes to allocate IP addresses to node instances.

### Public subnets

| **namespace** | **name** | **load balancer type** |
| --- | --- | --- |
| external-dns | external-dns-dev | none |
| external-dns | external-dns-public | none |
| external-dns | external-dns-private | none |
| kubeapps | kubeapps | application |

### Private subnets

| **namespace** | **name** | **load balancer type** |
| --- | --- | --- |
| kube-system | aws-load-balancer-controller | none |
| brokers | rabbitmq-cluster | network |
|  |  |  |
|  |  |  |
|  |  |  |

## Add permissions to EKS cluster

Provide the administrators group with the necessary access permissions to the cluster.

1. Administrators

Locate the 'Administrators' group within the IAM principal section and select the `Standard` option.

Add the `AmazonEKSClusterAdminPolicy` and click the `Add policy` button.

2. NodeInstanceRole

Add an access entry for the `NodeInstanceRole` IAM role so it can access `EC2` to create nodes. The type need to be EC2 Linux.

## Login EKS as Administrator

We can authenticate with the EKS cluster before connecting it to Keycloak, bypassing the need for initial Keycloak setup. More details can be found at Configuring Kubernetes Access and Cluster Policies for Users.

### First time access

For the first cluster access, retrieve the configuration first.

wide760aws eks update-kubeconfig --name develop --region eu-west-1 --user-alias develop-ou

## Storageclasses

We need to configure storage classes for the cluster, ensuring they match those in the old cluster.

wide760kubectl get storageclass
NAME PROVISIONER RECLAIMPOLICY VOLUMEBINDINGMODE ALLOWVOLUMEEXPANSION AGE
gp2 kubernetes.io/aws-ebs Delete WaitForFirstConsumer false 3y147d
gp2-retained kubernetes.io/aws-ebs Retain WaitForFirstConsumer true 3y29d
gp3 (default) ebs.csi.aws.com Delete WaitForFirstConsumer true 2y123d
gp3-encrypt ebs.csi.aws.com Delete WaitForFirstConsumer true 549d
gp3-retain-encrypt ebs.csi.aws.com Retain WaitForFirstConsumer true 549d
gp3-retained ebs.csi.aws.com Retain WaitForFirstConsumer true 2y178d
io2-retained ebs.csi.aws.com Retain WaitForFirstConsumer true 2y158d

### gp3

bashwide760kubectl apply -f - <<EOF
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: gp3
parameters:
type: gp3
provisioner: ebs.csi.aws.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
EOF

### gp3-retained

bashwide760kubectl apply -f - <<EOF
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: gp3-retained
parameters:
type: gp3
provisioner: ebs.csi.aws.com
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
EOF

To configure the encrypted storage class, the ARN of the AWS KMS key is necessary.

### gp3-encrypt

bashwide760kubectl apply -f - <<EOF
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: gp3-encrypt
parameters:
encrypted: "true"
kmsKeyId: <PUT ARN KEY HERE>
type: gp3
provisioner: ebs.csi.aws.com
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
EOF

### gp3-retain-encrypt

bashwide760kubectl apply -f - <<EOF
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: gp3-retain-encrypt
parameters:
encrypted: "true"
kmsKeyId: <PUT ARN KEY HERE>
type: gp3
provisioner: ebs.csi.aws.com
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
EOF

### io2-retained

bashwide760kubectl apply -f - <<EOF
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: io2-retained
parameters:
iopsPerGb: "100"
type: io2
provisioner: ebs.csi.aws.com
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
EOF

### Default storageclass

To avoid specifying a storage class every time you create a new PVC, set a default StorageClass. Run the following command:

bashwide760kubectl patch storageclass gp3 \
-p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

Result:

wide760kubectl get storageclass
NAME PROVISIONER RECLAIMPOLICY VOLUMEBINDINGMODE ALLOWVOLUMEEXPANSION AGE
gp2 kubernetes.io/aws-ebs Delete WaitForFirstConsumer false 43d
gp3 (default) ebs.csi.aws.com Delete WaitForFirstConsumer true 42d
gp3-encrypt ebs.csi.aws.com Delete WaitForFirstConsumer true 42d
gp3-retain-encrypt ebs.csi.aws.com Retain WaitForFirstConsumer true 42d
gp3-retained ebs.csi.aws.com Retain WaitForFirstConsumer true 42d
io2-retained ebs.csi.aws.com Retain WaitForFirstConsumer true 42d

## Install AWS load balancer controller

The AWS Load Balancer Controller manages Application Load Balancers (ALB) for Kubernetes clusters. It is deployed as a Kubernetes deployment in the `kube-system` namespace and uses AWS Identity and Access Management (IAM) roles to manage the load balancers in EC2. Domains specified in the Ingress resources are used to create the Application Load Balancers and Route 53 DNS records in the Hosted Zones. The synchronization of Route 53 records is handled by another application, `external-dns`, which is described later and some information is located here.

The documentation for the installation can be found at <https://kubernetes-sigs.github.io/aws-load-balancer-controller/latest/deploy/installation/> .

### Helm installation

1. Add Helm Repository

bashwide760helm repo add eks https://aws.github.io/eks-charts

2. Associate IAM OIDC Provider

We need to associate the cluster with an OIDC (OpenID Connect) provider. This association is  
necessary to enable IAM roles for service accounts in Kubernetes. It allows Kubernetes  
workloads to securely access AWS services using IAM roles. By associating the OIDC provider,  
you can create IAM roles that Kubernetes service accounts can assume, providing fine-grained  
access control to AWS resources. This is a crucial step for setting up the AWS Load Balancer  
Controller and other AWS-integrated services in your Kubernetes cluster.

bashwide760eksctl utils associate-iam-oidc-provider \
--region eu-west-1 \
--cluster develop \
--profile <AWS Profile> \
--approve

The AWS profile can be located as seen below:

In the AWS console, the OIDC provider can be found in the IAM section.

3. Create IAM Policy for AWS Load Balancer Controller

Create a new IAM policy named "AWSLoadBalancerControllerIAMPolicy" if it does not already exist. The policy should look like the JSON below.

jsonwide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"iam:CreateServiceLinkedRole"
],
"Resource": "\*",
"Condition": {
"StringEquals": {
"iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
}
}
},
{
"Effect": "Allow",
"Action": [
"ec2:DescribeSubnets",
"ec2:DescribeVpcs",
"ec2:DescribeSecurityGroups",
"ec2:DescribeInstances",
"ec2:DescribeNetworkInterfaces",
"ec2:DescribeAccountAttributes",
"ec2:DescribeAddresses",
"ec2:DescribeAvailabilityZones",
"ec2:DescribeInternetGateways",
"ec2:DescribeVpcs",
"ec2:DescribeVpcPeeringConnections",
"ec2:DescribeSubnets",
"ec2:DescribeSecurityGroups",
"ec2:DescribeInstances",
"ec2:DescribeNetworkInterfaces",
"ec2:DescribeTags",
"ec2:GetCoipPoolUsage",
"ec2:DescribeCoipPools",
"ec2:GetSecurityGroupsForVpc",
"elasticloadbalancing:DescribeLoadBalancers",
"elasticloadbalancing:DescribeLoadBalancerAttributes",
"elasticloadbalancing:DescribeListeners",
"elasticloadbalancing:DescribeListenerCertificates",
"elasticloadbalancing:DescribeSSLPolicies",
"elasticloadbalancing:DescribeRules",
"elasticloadbalancing:DescribeTargetGroups",
"elasticloadbalancing:DescribeTargetGroupAttributes",
"elasticloadbalancing:DescribeTargetHealth",
"elasticloadbalancing:DescribeTags",
"elasticloadbalancing:DescribeTrustStores",
"elasticloadbalancing:DescribeListenerAttributes",
"elasticloadbalancing:DescribeCapacityReservation"
],
"Resource": "\*"
},
{
"Effect": "Allow",
"Action": [
"cognito-idp:DescribeUserPoolClient",
"acm:ListCertificates",
"acm:DescribeCertificate",
"iam:ListServerCertificates",
"iam:GetServerCertificate",
"waf-regional:GetWebACL",
"waf-regional:GetWebACLForResource",
"waf-regional:AssociateWebACL",
"waf-regional:DisassociateWebACL",
"wafv2:GetWebACL",
"wafv2:GetWebACLForResource",
"wafv2:AssociateWebACL",
"wafv2:DisassociateWebACL",
"shield:GetSubscriptionState",
"shield:DescribeProtection",
"shield:CreateProtection",
"shield:DeleteProtection"
],
"Resource": "\*"
},
{
"Effect": "Allow",
"Action": [
"ec2:AuthorizeSecurityGroupIngress",
"ec2:RevokeSecurityGroupIngress"
],
"Resource": "\*"
},
{
"Effect": "Allow",
"Action": [
"ec2:CreateSecurityGroup"
],
"Resource": "\*"
},
{
"Effect": "Allow",
"Action": [
"ec2:CreateTags"
],
"Resource": "arn:aws:ec2:\*:\*:security-group/\*",
"Condition": {
"StringEquals": {
"ec2:CreateAction": "CreateSecurityGroup"
},
"Null": {
"aws:RequestTag/elbv2.k8s.aws/cluster": "false"
}
}
},
{
"Effect": "Allow",
"Action": [
"ec2:CreateTags",
"ec2:DeleteTags"
],
"Resource": "arn:aws:ec2:\*:\*:security-group/\*",
"Condition": {
"Null": {
"aws:RequestTag/elbv2.k8s.aws/cluster": "true",
"aws:ResourceTag/elbv2.k8s.aws/cluster": "false"
}
}
},
{
"Effect": "Allow",
"Action": [
"ec2:AuthorizeSecurityGroupIngress",
"ec2:RevokeSecurityGroupIngress",
"ec2:DeleteSecurityGroup"
],
"Resource": "\*",
"Condition": {
"Null": {
"aws:ResourceTag/elbv2.k8s.aws/cluster": "false"
}
}
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:CreateLoadBalancer",
"elasticloadbalancing:CreateTargetGroup"
],
"Resource": "\*",
"Condition": {
"Null": {
"aws:RequestTag/elbv2.k8s.aws/cluster": "false"
}
}
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:CreateListener",
"elasticloadbalancing:DeleteListener",
"elasticloadbalancing:CreateRule",
"elasticloadbalancing:DeleteRule"
],
"Resource": "\*"
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:AddTags",
"elasticloadbalancing:RemoveTags"
],
"Resource": [
"arn:aws:elasticloadbalancing:\*:\*:targetgroup/\*/\*",
"arn:aws:elasticloadbalancing:\*:\*:loadbalancer/net/\*/\*",
"arn:aws:elasticloadbalancing:\*:\*:loadbalancer/app/\*/\*"
],
"Condition": {
"Null": {
"aws:RequestTag/elbv2.k8s.aws/cluster": "true",
"aws:ResourceTag/elbv2.k8s.aws/cluster": "false"
}
}
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:AddTags",
"elasticloadbalancing:RemoveTags"
],
"Resource": [
"arn:aws:elasticloadbalancing:\*:\*:listener/net/\*/\*/\*",
"arn:aws:elasticloadbalancing:\*:\*:listener/app/\*/\*/\*",
"arn:aws:elasticloadbalancing:\*:\*:listener-rule/net/\*/\*/\*",
"arn:aws:elasticloadbalancing:\*:\*:listener-rule/app/\*/\*/\*"
]
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:ModifyLoadBalancerAttributes",
"elasticloadbalancing:SetIpAddressType",
"elasticloadbalancing:SetSecurityGroups",
"elasticloadbalancing:SetSubnets",
"elasticloadbalancing:DeleteLoadBalancer",
"elasticloadbalancing:ModifyTargetGroup",
"elasticloadbalancing:ModifyTargetGroupAttributes",
"elasticloadbalancing:DeleteTargetGroup",
"elasticloadbalancing:ModifyListenerAttributes",
"elasticloadbalancing:ModifyCapacityReservation"
],
"Resource": "\*",
"Condition": {
"Null": {
"aws:ResourceTag/elbv2.k8s.aws/cluster": "false"
}
}
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:AddTags"
],
"Resource": [
"arn:aws:elasticloadbalancing:\*:\*:targetgroup/\*/\*",
"arn:aws:elasticloadbalancing:\*:\*:loadbalancer/net/\*/\*",
"arn:aws:elasticloadbalancing:\*:\*:loadbalancer/app/\*/\*"
],
"Condition": {
"StringEquals": {
"elasticloadbalancing:CreateAction": [
"CreateTargetGroup",
"CreateLoadBalancer"
]
},
"Null": {
"aws:RequestTag/elbv2.k8s.aws/cluster": "false"
}
}
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:RegisterTargets",
"elasticloadbalancing:DeregisterTargets"
],
"Resource": "arn:aws:elasticloadbalancing:\*:\*:targetgroup/\*/\*"
},
{
"Effect": "Allow",
"Action": [
"elasticloadbalancing:SetWebAcl",
"elasticloadbalancing:ModifyListener",
"elasticloadbalancing:AddListenerCertificates",
"elasticloadbalancing:RemoveListenerCertificates",
"elasticloadbalancing:ModifyRule"
],
"Resource": "\*"
}
]
}

Attach the policy to the IAM role `NodeInstanceRole` if it is not already attached. See the screenshot below.

4. Create service account

The service account will be created in the EKS cluster and linked to the IAM policy `AWSLoadBalancerControllerIAMPolicy`.

bashwide760eksctl create iamserviceaccount \
--cluster=develop \
--namespace=kube-system \
--name=aws-load-balancer-controller \
--attach-policy-arn=<PUT ARN IAM POLICY> \
--override-existing-serviceaccounts \
--region eu-west-1 \
--approve

See the screenshot below where to find the ARN.

Check if the service account was created in the cluster.

bashwide760kubectl get sa aws-load-balancer-controller -o yaml

5. Install Helm chart

First install the Custom Resource Definitions (CRDs) for the AWS Load Balancer Controller:

bashwide760wget https://raw.githubusercontent.com/aws/eks-charts/master/stable/aws-load-balancer-controller/crds/crds.yaml
kubectl apply -f crds.yaml

Then install the AWS Load Balancer Controller using Helm:

bashwide760helm upgrade --install aws-load-balancer-controller eks/aws-load-balancer-controller \
-n kube-system \
--set clusterName=develop \
--set region=eu-west-1 \
--set vpcId=<PUT HERE THE VPC ID> \
--set serviceAccount.create=false \
--set serviceAccount.name=aws-load-balancer-controller

Check the deployment:

bashwide760kubectl get pods -n kube-system | grep aws-load-balancer-controller

## Migrating RDS databases

Migrate the following databases to the new OU:

wide760airflow-dev-db
keycloak-dev-v3
pto-dev
support-apps-dev
vaultwarden-dev

Step 1: create a database snapshot

Step 2: retrieve the new OU's account ID

Step 3: share an encryption with the new OU

Share the key with the new OU by adding its account ID.

Step 4: copy the snapshot and encrypt it using the shared key

Step 5: share the created snapshot with the new OU

Step 6: restore the database in the new OU using the shared snapshot

* Use the same resource configuration (CPU, memory, etc.) as the old RDS instance.
* Apply these steps to all previously mentioned databases.

## Migrating EBS snapshots to new OU

The initial step is to share the snapshot with the new Development Organizational Unit (OU). To do this, locate the `Share permissions` section and add the relevant Account ID.

Navigate to the new Development Organizational Unit (OU) and await the snapshot's availability. It may take 5-10 minutes for the private snapshot to become visible.

Next, create a new volume from the snapshot. This volume will appear under `Elastic Block Store > Volumes`. Copy the volume ID, as it will be needed later.

The simplest next step is to install the application's Helm chart, then scale down the application (and also its database if exist). The new installation will provision an empty EBS volume, which is not what we need, as we require the volume created from the snapshot. The following examples are illustrative, demonstrating the process of mapping the correct volume to the newly installed application within the new develop OU.

Scale down application:

bashwide760kubectl scale --replicas=0 deployment/<DEPLOYMENT NAME> -n <NAMESPACE>

Scale down the database:

bashwide760kubectl scale --replicas=0 deployment/<DEPLOYMENT NAME MONGODB> -n <NAMESPACE>

Get the volume ID:

bashwide760kubectl get pvc -n <NAMESPACE>
NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS VOLUMEATTRIBUTESCLASS AGE
test-storage Bound pvc-960161ea-5ede-4802-8b9b-6919d8bd87ab 4Gi RWO gp3 <unset> 10s

Get the content of the PV:

bashwide760kubectl get pv pvc-960161ea-5ede-4802-8b9b-6919d8bd87ab -o yamlbashwide760apiVersion: v1
kind: PersistentVolume
metadata:
annotations:
pv.kubernetes.io/provisioned-by: ebs.csi.aws.com
volume.kubernetes.io/provisioner-deletion-secret-name: ""
volume.kubernetes.io/provisioner-deletion-secret-namespace: ""
creationTimestamp: "2025-07-17T15:10:03Z"
finalizers:
- external-provisioner.volume.kubernetes.io/finalizer
- kubernetes.io/pv-protection
- external-attacher/ebs-csi-aws-com
name: pvc-960161ea-5ede-4802-8b9b-6919d8bd87ab
resourceVersion: "17377427"
uid: ae6972ac-123a-4101-833c-8fb81c8d4160
spec:
accessModes:
- ReadWriteOnce
capacity:
storage: 4Gi
claimRef:
apiVersion: v1
kind: PersistentVolumeClaim
name: test-storage
namespace: testing-trang
resourceVersion: "17377398"
uid: 960161ea-5ede-4802-8b9b-6919d8bd87ab
csi:
driver: ebs.csi.aws.com
fsType: ext4
volumeAttributes:
storage.kubernetes.io/csiProvisionerIdentity: 1748864879890-9184-ebs.csi.aws.com
volumeHandle: vol-009378a27ba420782
nodeAffinity:
required:
nodeSelectorTerms:
- matchExpressions:
- key: topology.kubernetes.io/zone
operator: In
values:
- eu-west-1a
persistentVolumeReclaimPolicy: Delete
storageClassName: gp3
volumeMode: Filesystem
status:
lastPhaseTransitionTime: "2025-07-17T15:10:03Z"
phase: Bound

The most crucial detail to note is the `volumeHandle: vol-009378a27ba420782`, as this identifier currently refers to the empty EBS volume. To proceed, we must first remove the PersistentVolume. This action, however, is dependent upon the removal of its `claimRef`. Copy this information, which will be used later.

Remove the PV:

wide760kubectl delete pv pvc-960161ea-5ede-4802-8b9b-6919d8bd87ab

The execution of the command will not immediately delete the PersistentVolume (PV) because finalizers are preventing its removal. Consequently, the PV's status will persist as `Terminating`. To resolve this, open a new tab or window and proceed with the finalizer removal.

Open new tab:

wide760kubectl get pv
NAME CAPACITY ACCESS MODES RECLAIM POLICY STATUS CLAIM STORAGECLASS VOLUMEATTRIBUTESCLASS REASON AGE
pvc-960161ea-5ede-4802-8b9b-6919d8bd87ab 4Gi RWO Delete Terminating testing-trang/test-storage gp3 <unset> 19m

Remove finalizers:

wide760kubectl patch pv pvc-960161ea-5ede-4802-8b9b-6919d8bd87ab -p '{"metadata":{"finalizers":null}}'

The PV should be removed now.

Remove the empty EBS volume `vol-009378a27ba420782` in AWS also.

Update the volume ID field within the definition of the old PV resource, and subsequently, apply this revised configuration.

bashwide760kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolume
metadata:
annotations:
pv.kubernetes.io/provisioned-by: ebs.csi.aws.com
volume.kubernetes.io/provisioner-deletion-secret-name: ""
volume.kubernetes.io/provisioner-deletion-secret-namespace: ""
creationTimestamp: "2025-07-17T15:10:03Z"
finalizers:
- external-provisioner.volume.kubernetes.io/finalizer
- kubernetes.io/pv-protection
- external-attacher/ebs-csi-aws-com
name: pvc-960161ea-5ede-4802-8b9b-6919d8bd87ab
spec:
accessModes:
- ReadWriteOnce
capacity:
storage: 4Gi
claimRef:
apiVersion: v1
kind: PersistentVolumeClaim
name: test-storage
namespace: testing-trang
resourceVersion: "17377398"
uid: 960161ea-5ede-4802-8b9b-6919d8bd87ab
csi:
driver: ebs.csi.aws.com
fsType: ext4
volumeAttributes:
storage.kubernetes.io/csiProvisionerIdentity: 1748864879890-9184-ebs.csi.aws.com
volumeHandle: <PUT VOLUME ID FROM SNAPSHOT HERE>
nodeAffinity:
required:
nodeSelectorTerms:
- matchExpressions:
- key: topology.kubernetes.io/zone
operator: In
values:
- eu-west-1a
persistentVolumeReclaimPolicy: Delete
storageClassName: gp3
volumeMode: Filesystem
status:
lastPhaseTransitionTime: "2025-07-17T15:10:03Z"
phase: Bound
EOF

Replace the placeholder `<PUT VOLUME ID FROM SNAPSHOT HERE>` with the actual Volume ID obtained from the snapshot. Also, remove the following information:

wide760 resourceVersion: "17377427"
uid: ae6972ac-123a-4101-833c-8fb81c8d4160

Scale up the application:

bashwide760kubectl scale --replicas=1 deployment/<DEPLOYMENT NAME> -n <NAMESPACE>

Scale up the database:

bashwide760kubectl scale --replicas=1 deployment/<DEPLOYMENT NAME MONGODB> -n <NAMESPACE>

To migrate the MongoDB databases to the new OU read the document Synchronizing MongoDB Databases During Migration.

## Create namespaces

Create the following namespaces in the new Kubernetes cluster:

wide760kubectl create ns ais-core
kubectl create ns ais-processing
kubectl create ns amazon-cloudwatch
kubectl create ns aws-observability
kubectl create ns brokers
kubectl create ns bunkerplanner
kubectl create ns cattle-system
kubectl create ns core-service
kubectl create ns customer-apps
kubectl create ns data-engineering
kubectl create ns databases
kubectl create ns doit-eks-metrics
kubectl create ns external-dns
kubectl create ns general-service
kubectl create ns keycloak
kubectl create ns kubeapps
kubectl create ns monitoring
kubectl create ns portcall
kubectl create ns pto
kubectl create ns revents-core
kubectl create ns revents-jobs
kubectl create ns students
kubectl create ns teqplay-api
kubectl create ns teqplay-fun
kubectl create ns testing
kubectl create ns vaultwarden
kubectl create ns velero
kubectl create ns voyage

## Apply RBAC permissions

Run the `apply-roles.sh` script to apply all cluster roles.

See: https://github.com/teqplay/kubernetes-scripts/tree/master/cluster-permissions/rbac

## Apply network policies

Run the `apply-policies-develop.sh` script to apply all network policies for the develop cluster.

See: https://github.com/teqplay/kubernetes-scripts/tree/master/cluster-network-policies/environments

## Route 53 - route Application to New Load Balancer

Once an application is migrated, its address must be updated to point to the new load balancer within the new Kubernetes cluster of the new OU. The time to live (TTL) needs to be reduced to 60 seconds.

The address of the load balancer can be retrieved via the terminal.

wide760kubectl get ingresswide760NAME CLASS HOSTS ADDRESS PORTS AGE
event-history-dev-ingress alb eventhistorybackend.dev.teqplay.com k8s-eksdev-bb7a781d42-120868117.eu-west-1.elb.amazonaws.com 80 555d
ship-history-dev-ingress alb shiphistorybackend.dev.teqplay.com k8s-eksdev-bb7a781d42-120868117.eu-west-1.elb.amazonaws.com 80 555d

The address is visible in the "ADDRESS" column. If the new application doesn't function as expected, rollback the changes.

## Route 53 - hosted zone dev.teqplay.com

To prepare for routing all traffic to the new cluster, we need to reduce the Time-To-Live (TTL) of the current DNS record for `dev.teqplay.com` to 60 seconds.

After all applications are migrated, switch to the new hosted zone in the new OU. Find the NS addresses within that OU and replace them with the current values as displayed in the image above.

## Installing applications in new cluster

### RabbitMq

The RabbitMQ migration document is available at this location: RabbitMq cluster

Please note that the RabbitMQ export must be retrieved from the existing cluster and then imported into the new cluster. This process should be performed only once. Repeated exports and imports may result in an unstable new cluster, as observed in previous tests.

The RabbitMQ cluster uses Let's Encrypt for its TLS certificates. To set this up, you'll need to configure cert-manager. Please note that cert-manager requires access to Route 53 within the same Organizational Unit (OU).

Cert-manager for auto creating TLS certificates

### Kubeapps

Start by migrating the Kubeapps database, used for Helm chart repository synchronization. It's not necessary for the data to be perfectly in sync with the source database, since cron jobs will update the Helm charts from the public repositories.

1. Retrieve the PostgreSQL password for the `postgres` user.

wide760export PG\_PASSWORD=$(kubectl get secret kubeapps-dev-postgres -n kubeapps -o jsonpath='{.data.postgres-password}' | base64 --decode)

2. Deploy a PostgreSQL client within a Kubernetes pod.

wide760kubectl -n kubeapps apply -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
name: postgres-client
labels:
app.kubernetes.io/component: frontend
app.kubernetes.io/instance: kubeapps-dev
app.kubernetes.io/name: kubeapps
spec:
containers:
- name: postgres-client
image: postgres
env:
- name: POSTGRES\_PASSWORD
value: test
- name: PGPASSWORD
value: ${PG\_PASSWORD}
EOF

3. Dump the Kubeapps database `assets`.

wide760kubectl exec -n kubeapps -it postgres-client -- sh -c \
'pg\_dump -U postgres --no-owner --no-privileges -h kubeapps-dev-postgresql.kubeapps.svc.cluster.local -p 5432 -d assets > /tmp/kubeapps.sql'

4. Retrieve the database dump and save it to the local disk.

wide760kubectl -n kubeapps cp postgres-client:/tmp/kubeapps.sql kubeapps.sql

The new Kubeapps database can be restored using the database dump file.

**! Need to check if it’s already possible to use RDS instead of a local PostgreSQL database.**

Install Kubeapps

See <https://github.com/vmware-tanzu/kubeapps> for the installation documentation.

See how to connect Kubeapps to Keycloak Kubeapps in AWS cluster .

## DoIT migration

The `doit-eks-metrics` namespace in the `develop` and `production` EKS clusters contains deployments that gather cluster data and send it to DoIT via S3. These metrics are required for DoIT reporting.

It's possible that copying the existing cluster deployments to the new EKS cluster would be sufficient. However, to confirm this, a request for clarification has been submitted to the DoIT support desk.

## NATS migration

You can find the relevant document for the **NATS migration** at the following location: NATS supercluster for migration to new OU and Migrating brokers NATS and RabbitMQ .