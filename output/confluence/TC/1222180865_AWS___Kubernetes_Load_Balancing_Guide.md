---
id: confluence:1222180865
source: confluence
type: page
space: TC
title: AWS & Kubernetes Load Balancing Guide
author: Jamie de Leest
date: '2026-05-26'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1222180865
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1222180865
---
# AWS & Kubernetes Load Balancing Guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1222180865  

## Content

## Purpose

This document explains:

* The difference between **external** and **internal** AWS load balancers
* How Kubernetes load balancing and DNS work
* When to use each option
* Recommended architecture patterns for teams

---

# 1. AWS Load Balancers Overview

AWS provides managed load balancers through Amazon Web Services Elastic Load Balancing (ELB).

Main types:

| Type | Layer | Common Use |
| --- | --- | --- |
| Application Load Balancer (ALB) | Layer 7 (HTTP/HTTPS) | Web applications, APIs |
| Network Load Balancer (NLB) | Layer 4 (TCP/UDP) | High performance TCP/UDP traffic |
| Gateway Load Balancer | Layer 3/4 | Security appliances |

Most Kubernetes workloads use:

* **ALB** for HTTP applications
* **NLB** for TCP services or high-performance ingress

---

# 2. External vs Internal Load Balancers

## External Load Balancer

An **external load balancer** is publicly accessible from the internet.

### Characteristics

* Has public IPs
* Internet-facing
* Used for customer/client traffic
* Typically terminates HTTPS
* Routes traffic into Kubernetes or ECS services

### Example Use Cases

| Use Case | Recommended |
| --- | --- |
| Public website | External ALB |
| Public REST API (Vesselvoyage API) | External ALB |
| Public Rabbitmq connections | External NLB |

### Example Architecture

wide760Internet
↓
External ALB
↓
Kubernetes Ingress
↓
Services
↓
Pods

### AWS Annotation Example

wide760alb.ingress.kubernetes.io/scheme: internet-facing

### When to use

External load balancer is used when you want to expose an application to the internet that everyone can access without the teqplay vpn.

---

## Internal Load Balancer

An **internal load balancer** is only accessible inside the VPC or connected private networks.

### Characteristics

* Private IPs only
* Not accessible from the internet
* Used for internal systems
* Common for microservice communication
* Safer for admin/internal tools

### Example Use Cases

| Use Case | Recommended |
| --- | --- |
| Internal APIs | Internal ALB |
| Admin dashboards | Internal ALB |
| Private microservices | Internal NLB/ALB |
| Internal databases | Internal NLB |

### Example Architecture

wide760vpn
↓
Internal ALB
↓
Kubernetes Service
↓
Pods

### AWS Annotation Example

wide760alb.ingress.kubernetes.io/scheme: internal

### When to use

Internal load balancer is used when you want to expose an application only within our VPC this means that everyone with the teqplay vpn can access these application.

---

# 3. Kubernetes Load Balancing

Kubernetes has multiple layers of traffic routing.

---

## ClusterIP

Default Kubernetes service type.

### Characteristics

* Internal only
* Accessible within cluster
* Gets virtual IP
* Used for pod-to-pod communication

### Use Cases

| Use Case | Recommended |
| --- | --- |
| Microservice communication | ClusterIP |
| Internal APIs | ClusterIP |
| Backend services | ClusterIP |

### Example

wide760kind: Service
spec:
type: ClusterIP

---

## NodePort

Exposes a service on a port on every node.

### Characteristics

* Opens port on nodes
* Usually not used directly in production
* Often used behind AWS load balancers

### Use Cases

| Use Case | Recommended |
| --- | --- |
| Development/testing | NodePort |
| Ingress controller backend | Sometimes |

# 4. Kubernetes DNS

Kubernetes provides internal DNS through CoreDNS.

---

## Internal Service Discovery

Services automatically receive DNS names.

### Format

wide760<service>.<namespace>.svc.cluster.local

### Example

wide760users-api.backend.svc.cluster.local

### When to use

Internal Service Discovery is uses when you want a application in the cluster to connect to an other application in the cluster, by doing this all network is in the cluster and the is no usage on our loadbalancers.