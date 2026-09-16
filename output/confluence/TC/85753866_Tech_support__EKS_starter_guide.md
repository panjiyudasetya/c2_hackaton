---
id: confluence:85753866
source: confluence
type: page
space: TC
title: 'Tech support: EKS starter guide'
author: Jamie de Leest
date: '2026-03-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/85753866
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/85753866
---
# Tech support: EKS starter guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/85753866  

## Content

This guide will explain everything you need to know to be doing tech support duties on our EKS clusters. It is expected to have some knowledge about Docker containers, Kubernetes and Kubernetes resources.

## Useful resources

* <https://kubernetes.io/docs/reference/kubectl/cheatsheet/>
* <https://docs.aws.amazon.com/eks/latest/userguide/eks-networking.html>

## Prepare your machine for EKS and Kubernetes

Install the following packages on your machine:

* AWS CLI → <https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>

  + Alternative: <https://pypi.org/project/awscliv2/>:  
    `pip install awscliv2` to install the wrapper tool, then `awscliv2 -i` to download the official cli in a docker image, and then use your favourite Linux way to ensure `aws` is an alias for `awsv2`
* Kubernetes CLI → <https://kubernetes.io/docs/tasks/tools/> (only `kubectl`)
* Helm → <https://helm.sh/docs/intro/install/>

While entirely optional, I also suggest installing <https://k8slens.dev/>. This program can do all the commands in this guide without filling them in yourself. The program also shows real-time metrics of the `Nodes` and `Pods`.

[This Guide](https://teqplaybv.atlassian.net/wiki/x/AoC6RQ) will help you to now connect with your local tools to the Teqplay cluster, using Keycloak for authentication and setting-up the AWS CLI to connect to our AWS environment.

## General knowledge needed about Kubernetes

Our Kubernetes resources are specified in so-called `Namespaces`. This can be seen as an enclosed environment inside Kubernetes. Because this is enclosed, it means that the applications are not allowed to access any Namespaces outside of this when not given access. It is generally good to have your Kubernetes-specific resources separated from your applications. Almost all example commands in this starter guide are followed by `-n teqplay-app`. Here `-n` refers to the Namespace you want to do something in. Without specifying this, you will do something in the `default` Namespace, which is currently not used.

* All our applications and related resources can be found in the Namespace `teqplay-app`.
* All the student applications can be found in the Namespace `students` (Only for the develop cluster).
* All the Kubernetes system-specific applications can be found in the Namespace `kube-system`.
* A KeyCloak instance runs on its own Namespace called `keycloak`.
* All our Zabbix agents run on the `monitoring` Namespace.

## Where to find EKS?

EKS can be found in the AWS console interface. Here you can view all our currently created clusters. When a cluster is selected, we can see all the `Nodes` that have been created. Here `Nodes` can be seen as all the machines we are running for the EKS cluster. This can be Fargate instances but also EC2 machines.

Each `Node` can run multiple `Pods`. A `Pod` can be seen as one instance of an application. Although with Fargate, we always have 1 `Node` per `Pod`. Each `Pod` can also be found on the `Workloads` page, which specifies all the `Services` we are running. Here `csi-dev` can be seen as a good example, which is one application. This `Service` can have one or more `Pods` scattered around over multiple `Nodes`.

In the last tab, we can find the `Configuration` of our EKS cluster. Here only the `Compute` sub-menu is important. This sub-menu is used to specify how many `EC2` machines are booted up to deploy pods on. For `Fargate` profiles, we can specify which namespace(s) and what matching tags a `Fargate` instance should be spun up.

## Where to find the Kubernetes cluster?

On the EKS view in the AWS console interface, we can’t do much besides looking at our running `Nodes`, `Services` and `Pods`. To edit our resources, view our logs, and see the application load, we have to access it via the Kubernetes API. We need to update our `kubeconfig` to get access. Creating or updating the config can be done by running the following commands:

* For develop → `aws eks update-kubeconfig --name develop --alias develop --role-arn arn:aws:iam::050356841556:role/Developer-EKS-Role`
* For production → `aws eks update-kubeconfig --name production --alias production --role-arn arn:aws:iam::050356841556:role/Developer-EKS-Role`

To check if you did everything correctly, run the following commands:

* Checking the current context → `kubectl config current-context`   
  This will return the alias we have specified when updating our kubeconfig.
* Switching our context to a different one → `kubectl config use-context develop`  
  This will change our kubectl config to the develop cluster.

## How to make config changes to an Application?

Our applications in EKS make use of a so-called `ConfigMap`. This is where all the configuration fields are specified. This can be seen as the equivalent of changing the configuration of an Elastic Beanstalk instance.

Editing a `ConfigMap` is as easy as calling:

wide760kubectl edit configmap/csi-dev -n teqplay-app

## How to restart an Application?

Restarting can be done on multiple levels:

* `Deployment` level, you want to recreate all the `Pods` of an Application.
* `Pod` level, you only want to restart one particular instance.

### Restarting on `Deployment` level

To restart all `Pods`, we have to roll out a restart on the `Deployment`. How it does the rollout depends on what is specified in the strategy type of the deployment. The strategy can be either `Recreate` or `RollingUpdate`.

* `Recreate` it will first shut down the already existing pods, then boot up new ones.
* `RollingUpdate` will boot up new `Pods`, then shut down the old ones (this is the default behaviour).

Executing the restart on the deployment level can be done by running the following command:

wide760kubectl rollout restart deployment/csi-dev -n teqplay-appnote3549f61a6339

Optionally you can monitor the rollout after initiating the restart by running the following command:

`kubectl rollout status -w deployment/csi-dev -n teqplay-app`

This will follow the rollout status until the deployment is marked as completed.

Optionally you can monitor the rollout after initiating the restart by running the following command:

`kubectl rollout status -w deployment/csi-dev -n teqplay-app`

This will follow the rollout status until the deployment is marked as completed.

### Restarting on `Pod` level

Delete the Pod you want to restart. Doing so will spin up a new Pod automatically.

wide760kubectl delete csi-dev-5c9f48dcc7-wtkz6 -n teqplay-app

### Verifying if the `Pods` are correctly restarted

Once this step is done, it should handle everything automatically, and once the pod is declared as healthy, it will automatically be registered to the target group of the load balancer.

If this does not happen, then you should verify this yourself in EC2, which can be found at [EC2 -> Load Balancers](https://eu-west-1.console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LoadBalancers:sort=loadBalancerName).

* Click the EKS ALB for prod or dev.
* Go to the `listeners` tab and `view/edit rules` of the `HTTPS : 443` listeners.
* Click on the `Forward to` entry of the application that you want to check if it is registered.
* Go to the `Targets` tab, here the private IP address of our new target should be located.

## Where to find logs?

Logs can be accessed by looking at the logs directly on the `Pod` or via Cloudwatch if, for example, the `Pod` killed itself and already restarted.

### Via a `Pod` directly:

First, we need to find out the name of the `Pod` that we want to monitor. The name of a `Pod` is always generated using the name of the `Service` appended with some random characters to make them unique.

To find all the pods of a specific application, search the following:

wide760kubectl get pods -l app.kubernetes.io/instance=csi-dev -n teqplay-app

Once you have found the name of the Pod that you are interested in, call the following command to view the current logs of the machine:

wide760kubectl logs csi-dev-5c9f48dcc7-wtkz6 -n teqplay-app

* You can add `-f` after `logs` to follow.
* You can add `--tail n` to download `n` lines of log lines.

### Via Cloudwatch:

On the CloudWatch page, go to `Log Groups`. In here the log files are stored in the following groups:

`/eks/<cluster>/<namespace>/<application>`

So we could have the following for the backend of Poma:

* `/eks/develop/teqplay-app/poma-dev` for develop
* `/eks/production/teqplay-app/poma` for production

In the log group, you can find a log stream for each pod. This means in the case of Poma that, we have two log streams that might be interesting for us as it is running two replicas.

## How does Zabbix currently monitor our Kubernetes instances?

We are currently running Zabbix agents on each Kubernetes node. They are automatically added and will be automatically registered to our list of hosts. Monitoring the nodes is only to track the Linux/system related issues (e.g. CPU usage, memory usage, disk utilization and more).

Monitoring the pods is done through the Kubernetes API. We’ve extended the `Kubernetes nodes by HTTP` template for each cluster, called `Kubernetes develop nodes` and `Kubernetes production nodes`. The develop and production template contain both the needed macros, which override the `{$KUBE.API.ENDPOINT}` and `{$KUBE.API.TOKEN}` to be able to access the Kubernetes API.

note47b09a5a9a4c

Monitoring of the Pods is limited. Currently we have triggers to detect the following:

* Fire a trigger when a pod is reporting as unhealthy.
* Fire a trigger when a pod is stuck in boot-loop.

Monitoring of the Pods is limited. Currently we have triggers to detect the following:

* Fire a trigger when a pod is reporting as unhealthy.
* Fire a trigger when a pod is stuck in boot-loop.

## Setup metrics in Lens

To setup metrics in Lens go to settings and enter the Prometheus service address `monitoring/prometheus-server:80`. Change the address for clusters develop and production.