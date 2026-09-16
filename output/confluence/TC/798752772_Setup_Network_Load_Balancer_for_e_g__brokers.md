---
id: confluence:798752772
source: confluence
type: page
space: TC
title: Setup Network Load Balancer for e.g. brokers
author: Minh Trang Nguyen (Unlicensed)
date: '2025-07-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/798752772
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/798752772
---
# Setup Network Load Balancer for e.g. brokers

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/798752772  

## Content

## Introduction

This guide describes the set up of a Network Load Balancer for connected VPCs. You can only create one Network Load Balancer using service annotations. All other apps require target group bindings after the creation of the Network Load Balancer. Be aware, that the primary app, which setup must not be removed in the future cannot be deprecated independently, as removing it will also delete the Network Load Balancer and other bindings.

## NodePorts

The default NodePort range in Kubernetes is 30000-32767. We will use this range partly for our setup, as it simplifies the configuration of Security group rules.

## Setup by example

We will demonstrate the setup using examples, with `Nginx` serving as our example application. Nginx is ideal for this purpose due to its immediate feedback. The setup for this example includes two VPCs: **VPC-A** and **VPC-B**.

In **VPC-A** and **VPC-B** pods were deployed with the tool `curl`, so we can check the connections in both VPC’s.

### Broker RabbitMq

To set up the Network Load Balancer for the environment, it’s recommended to make `RabbitMQ` the primary application. You can then add other applications to this load balancer at a later time. The example below is a fake setup of a broker and deployed in **VPC-B**.

bashwide760kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
name: some-broker-deployment
spec:
replicas: 1
selector:
matchLabels:
app: broker
template:
metadata:
labels:
app: broker
spec:
nodeSelector:
app.teqplay.nl/nodegroup: mongodb
tolerations:
- key: "nodegroup"
operator: "Equal"
value: "mongodb"
effect: "NoSchedule"
containers:
- name: broker
image: nginx:latest
ports:
- containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
name: broker-service
annotations:
service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
service.beta.kubernetes.io/aws-load-balancer-name: nlb-eks-develop
service.beta.kubernetes.io/aws-load-balancer-scheme: "internal"
service.beta.kubernetes.io/aws-load-balancer-subnets: "subnet-030ca4bb313172e24"
spec:
type: LoadBalancer
selector:
app: broker
ports:
- protocol: TCP
nodePort: 31000
port: 5001
targetPort: 80
EOF

The service annotations can be found at <https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.13/guide/service/annotations/>. The scheme must be `internal`, and the `subnets` need to be configured. In this example, the `NodePort` was explicitly set to simplify the management of inbound Security Group rules.

### Other fake broker

Deploy a new fake broker in VPC-B and add it to the Network Load Balancer.

bashwide760kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
name: app-broker2
spec:
replicas: 1
selector:
matchLabels:
app: broker2
template:
metadata:
labels:
app: broker2
spec:
nodeSelector:
app.teqplay.nl/nodegroup: mongodb
tolerations:
- key: "nodegroup"
operator: "Equal"
value: "mongodb"
effect: "NoSchedule"
containers:
- name: broker2
image: nginx:latest
ports:
- containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
name: app-broker2-service
spec:
type: NodePort
selector:
app: broker2
ports:
- protocol: TCP
nodePort: 32000
port: 5002
targetPort: 80
EOF

The service annotations were intentionally omitted. This is because AWS limits Network Load Balancer creation to a single instance.

### Create new Target Group

A new Target Group needs to be created, which can then be added to the Network Load Balancer.

The NodePort `32000`, as defined in the service, must be added to the details and protocol should be TCP.

Select the nodes and click button `Include as pending below`.

### Create TargetGroupBinding for Service

The next step is to create a TargetGroupBinding, which connects the in-cluster service to the AWS Target Group. For more information see <https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.13/guide/targetgroupbinding/targetgroupbinding/.>

The TargetGroup ARN is required. Copy it and paste it into the manifest.

bashwide760kubectl apply -f - <<EOF
apiVersion: elbv2.k8s.aws/v1beta1
kind: TargetGroupBinding
metadata:
name: brokers2-nlb-binding
spec:
serviceRef:
name: app-broker2-service
port: 5002
targetGroupARN: "arn:aws:elasticloadbalancing:eu-west-1:704630444514:targetgroup/k8s-brokers2/7c944b0260f2fe41"
EOF

Result is:

bashwide760kubectl get targetgroupbindings -o wide
NAME SERVICE-NAME SERVICE-PORT TARGET-TYPE ARN NAME AGE
brokers2-nlb-binding app-broker2-service 5002 instance arn:aws:elasticloadbalancing:eu-west-1:704630444514:targetgroup/k8s-brokers2/7c944b0260f2fe41 28m
k8s-testingt-brokerse-19d91f9b94 broker-service 5001 instance arn:aws:elasticloadbalancing:eu-west-1:704630444514:targetgroup/k8s-testingt-brokerse-19d91f9b94/03145bdfe884c5e7 61m

### Add TargetGroup to Network Load Balancer

The next step is to add the TargetGroup to the Network Load Balancer.

Select the Network Load Balancer and go to the details to add a listener.

Add the incoming port number, which is `5002` in this case. Forward it to the newly created Target Group.

### Security Groups

The Security Group Rules needs to be configured to allow traffic into the Network Load Balancer for the new service.

#### Rules managed by Load Balancer

The incoming ports must be added to the rules managed by the Load Balancer.

It's important to use a port range because adding individual rules can disrupt the Network Load Balancer's functionality. This behavior was confirmed through intensive testing.

The Port range is now `5001 - 5002`.

#### Rules EKS cluster

Next step is to add the NodePort to the Security Group associated with the EKS cluster.

## Testing

bashwide760kubectl get svc -o wide
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE SELECTOR
app-broker2-service NodePort 10.100.29.223 <none> 5002:32000/TCP 72m app=broker2
broker-service LoadBalancer 10.100.221.8 nlb-eks-develop-e91d28be4b710187.elb.eu-west-1.amazonaws.com 5001:31000/TCP 80m app=broker

From pods in both **VPC-A** and **VPC-B**, curl commands were executed to send requests to services in VPC-B. All requests were successful. We can use the `EXTERNAL-IP` to make the requests, which is also the Network Load Balancer DNS name.

Example curl commands:

bashwide760curl -v nlb-eks-develop-e91d28be4b710187.elb.eu-west-1.amazonaws.com:5001
...
\* Request completely sent off
< HTTP/1.1 200 OK
...
curl -v nlb-eks-develop-e91d28be4b710187.elb.eu-west-1.amazonaws.com:5002
...
\* Request completely sent off
< HTTP/1.1 200 OK
...