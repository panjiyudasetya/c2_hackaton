---
id: confluence:83197953
source: confluence
type: page
space: TC
title: Setting up a Kubernetes cluster in EKS
author: Minh Trang Nguyen (Unlicensed)
date: '2023-06-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/83197953
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/83197953
---
# Setting up a Kubernetes cluster in EKS

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/83197953  

## Content

This guide will be making use of `aws`, `kubectl`, `eksctl` and `helm`. Please make sure you have all those packages installed.

* AWS CLI→ <https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>
* Kubernetes CLI→ <https://kubernetes.io/docs/tasks/tools/>
* EKS CLI → <https://eksctl.io/introduction/#installation>
* Helm → <https://helm.sh/docs/intro/install/>

## Setting up a new EKS instance

Create a cluster via the AWS console interface (can be found when searching [EKS -> Clusters](https://eu-west-1.console.aws.amazon.com/eks/home?region=eu-west-1#/clusters)):

* Set as service role `eksctl-develop-cluster-ServiceRole-1GSMRHF62FN6Y` or a role with the following policies:

  + `AmazonEKSClusterPolicy`
  + `AmazonEKSVPCResourceController`
  + `cloudwatch:PutMetricData` allow for `*`
  + `ec2:DescribeAccountAttributes` allow for `*`  
    `ec2:DescribeAddresses` allow for `*`  
    `ec2:DescribeInternetGateways` allow for `*`
* For subnets set both our public and private subnets (Fargate can only run in private subnets, and the cluster also needs access to the public subnets in case we want to connect to already existing EC2 instances).
* Set as security group `eks-cluster-sg-1559690845` or a group with the following inbound rules:

  + All traffic from itself (this security group will also be attached to services and pods when not overridden, making it needed to connect to each other if needed).
* Set the cluster endpoint as followed based on the needs:

  + Set to `Private` if you want to enforce only connecting or proxying to the Kubernetes cluster with a VPN connection.
  + Set to `Public` if you want to avoid the need for a VPN connection. This is something you need on the `develop` cluster as students can’t access our VPN.

Once the cluster is created (this can take up to 10 minutes):

* Go to `Configuration -> Compute` and create a `Node Group`. The specs of the machines that are mainly used are as followed:

  + AMI type should be `Amazon Linux 2`
  + Capacity type `On-Demand`
  + The instance type we mainly use is `r5.large`
  + The disk size can be kept at 20 GiB, although, when running a lot of Pods on 1 machine then upping this to at least 40 GiB is suggested.

## Connecting to the EKS instance

To access the EKS instance you need to talk with the Kubernetes API. This can be done via `kubectl`. We need to update our Kubernetes config. This can be done by calling the `aws eks update-kubeconfig` provided also the name of the cluster you want to connect to. To call this command you need to have specified the needed access id, secret and region in your .aws configuration file. This can be configured by either calling `aws configure` or editing your existing `.aws/configuration` file.

Once `aws` is configured then the following commands can be called:

* develop → `aws eks update-kubeconfig --name develop --alias develop`
* production → `aws eks update-kubeconfig --name production --alias production`

Here `--name develop` specifies the name of our cluster that we want to connect to and `--alias develop` is the name I gave it myself so I can access it quickly. Not providing an alias will create a really long URL which is a pain to use.

Once your kubeconfig is set up we need to make sure we are using the correct context. The following commands can be used:

* Checking the current context → `kubectl config current-context`   
  This will return the alias we have specified when updating our kubeconfig.
* Switching our context to a different one → `kubectl config use-context develop`  
  This will switch our kubectl config to the develop cluster.

## Configuring the Kubernetes cluster

Before we can start using the Kubernetes cluster we have to set up quite a few services so it can easily work together with AWS. We will be setting up the following components:

* Cloudwatch logging
* AWS Load Balancer Controller
* Teqplay Namespace

From here on out it is recommended to have some sort of Kubernetes IDE to easily edit Kubernetes resources without having to write everything in command line.

Highly recommended to be using Lens for this → <https://k8slens.dev/>

note

All the following YAML content is expected to be applied to the Kubernetes cluster. This can easily be done using a Kubernetes IDE which supports a 'Create resource' functionality. If this is not possible, save this YAML to a file and call the following command `kubectl apply -f ./FILENAME_HERE.yaml`

All the following YAML content is expected to be applied to the Kubernetes cluster. This can easily be done using a Kubernetes IDE which supports a 'Create resource' functionality. If this is not possible, save this YAML to a file and call the following command `kubectl apply -f ./FILENAME_HERE.yaml`

### Cloudwatch logging

This needs to be set up via the Helm chart Fluent for AWS. The values are located in the repo `kubernetes-scripts` in the directory `fluentbit-for-aws`.

Add the Helm chart repository when it was not set up before.

helm repo add eks https://aws.github.io/eks-charts

Create the namespace and switch to the namespace.

kubectl create namespace amazon-cloudwatch
kubectl config set-context --current --namespace=amazon-cloudwatch

Create the `configmap` first. For the `fluent-bit-cluster-info` set the cluster name in “`<SET THE CLUSTERNAME>`“ e.g. develop or production.

kubectl create -f - <<EOF
apiVersion: v1
kind: ConfigMap
metadata:
name: fluent-bit-cluster-info
namespace: amazon-cloudwatch
data:
cluster.name: <SET THE CLUSTERNAME>
http.port: "2020"
http.server: "on"
logs.region: eu-west-1
read.head: "off"
read.tail: "on"
EOF

Install the Helm chart.

helm install -f values.yaml aws-for-fluent-bit eks/aws-for-fluent-bit

Result:

kubectl get pods
NAME READY STATUS RESTARTS AGE
aws-for-fluent-bit-2dn8w 1/1 Running 0 17d
aws-for-fluent-bit-46prg 1/1 Running 0 17d
aws-for-fluent-bit-4n96l 1/1 Running 0 7d16h
aws-for-fluent-bit-5824k 1/1 Running 0 7d16h
aws-for-fluent-bit-5j4r6 1/1 Running 0 17d
aws-for-fluent-bit-c6j2t 1/1 Running 0 17d
aws-for-fluent-bit-csps7 1/1 Running 0 17d
aws-for-fluent-bit-jdc9q 1/1 Running 0 17d
aws-for-fluent-bit-qfwg2 1/1 Running 0 17d
aws-for-fluent-bit-r75mg 1/1 Running 0 17d
aws-for-fluent-bit-rvzr5 1/1 Running 0 7d15h
aws-for-fluent-bit-vrgzb 1/1 Running 0 17d
aws-for-fluent-bit-zgvhs 1/1 Running 0 17d
aws-for-fluent-bit-zzwvv 1/1 Running 0 17d

Go to AWS CloudWatch and find the log groups of the cluster and check if data is being logged.

Updating Helm chart

Go to `KubeApps` to update Fluentbit.

### AWS Load Balancer Controller

This component will be added so services will automatically be added to AWS ALB’s `(Application Load Balancer)` when an ingress is registered.

All commands from here on will be using the `develop` cluster as an example, please keep in mind to change this to your cluster name when applying those commands.

The first thing that is needed is to set up the IAM service account so our Controller can communicate with AWS.

* Create an IAM OICD provider.

  eksctl utils associate-iam-oidc-provider --region eu-west-1 --cluster develop --approve
* Add a new `ServiceAccount` in the Kubernetes cluster using the below-specified YAML:

  yamlapiVersion: v1
  kind: ServiceAccount
  metadata:
  name: aws-load-balancer-controller
  namespace: kube-system
  labels:
  app.kubernetes.io/managed-by: eksctl
  annotations:
  eks.amazonaws.com/role-arn: >-
  arn:aws:iam::050356841556:role/AWS-EKSLoadBalancerController
* The next step is to allow the just created OICD provider to be used by our `AWS-EKSLoadBalancerController` role which is already created in AWS IAM. To do this we have to update the trust policy of this role. We can do this by adding the newly created OICD provider (which can be found at [AWS IAM Identity providers](https://console.aws.amazon.com/iamv2/home#/identity_providers)). An example trust policy statement can be found below. *Note that you still have to change the OICD id to the one that you just created.*

  json{
  "Effect": "Allow",
  "Principal": {
  "Federated": "arn:aws:iam::050356841556:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/5FC7B8323EF5BB6AA9FB5B0CC8D2D827"
  },
  "Action": "sts:AssumeRoleWithWebIdentity",
  "Condition": {
  "StringEquals": {
  "oidc.eks.eu-west-1.amazonaws.com/id/5FC7B8323EF5BB6AA9FB5B0CC8D2D827:sub": "system:serviceaccount:kube-system:aws-load-balancer-controller",
  "oidc.eks.eu-west-1.amazonaws.com/id/5FC7B8323EF5BB6AA9FB5B0CC8D2D827:aud": "sts.amazonaws.com"
  }
  }
  }

Once this has been done we can actually install the load balancer controller:

* Install the TargetGroupBinding custom resource definitions.

  kubectl apply -k "github.com/aws/eks-charts/stable/aws-load-balancer-controller//crds?ref=master"
* Install the aws-load-balancer-controller, make sure to change the `clusterName`.

  helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName=develop --set serviceAccount.create=false --set region=eu-west-1 --set vpcId=vpc-28ff4e4d --set serviceAccount.name=aws-load-balancer-controller --set hostNetwork=true -n kube-system

note

If helm isn’t set up then you first have to add the AWS EKS helm repo:

`helm repo add eks https://aws.github.io/eks-charts`

<https://github.com/aws/eks-charts>

If helm isn’t set up then you first have to add the AWS EKS helm repo:

`helm repo add eks https://aws.github.io/eks-charts`

<https://github.com/aws/eks-charts>

### Teqplay Namespace

To be able to use the cluster the last thing we need to do is create and configure a namespace to which we can deploy our applications. We will be doing this for our `teqplay-app` namespace.

* Create the `teqplay-app` namespace using the below-specified YAML:

  yamlapiVersion: v1
  kind: Namespace
  metadata:
  name: teqplay-app
  labels:
  name: teqplay-app
* Create the `teqapp` service account using the below-specified YAML:

  yamlapiVersion: v1
  kind: ServiceAccount
  metadata:
  name: teqapp
  namespace: teqplay-app

  This service account will later be used by all of our pods to be able to communicate with other resources in the cluster and automatically create any needed resources on the side of AWS.
* Create an admin cluster role binding for the `teqapp` service account using the below-specified YAML:

  yamlapiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRoleBinding
  metadata:
  name: teqapp-cluster-admin
  subjects:
  - kind: ServiceAccount
  name: teqapp
  namespace: teqplay-app
  roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin

  For this example, we have used the default `cluster-admin` cluster role but if more fine-grained role rules are needed then creating a custom role is suggested.