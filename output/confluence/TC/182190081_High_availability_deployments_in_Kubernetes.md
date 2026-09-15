---
id: confluence:182190081
source: confluence
type: page
space: TC
title: High availability deployments in Kubernetes
author: Minh Trang Nguyen (Unlicensed)
date: '2023-05-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/182190081
explicit_links: []
---
# High availability deployments in Kubernetes

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/182190081  

## Content

Making an application high available means that with each new deployment http requests should not throw any error 5xx status codes. The process of not receiving 5xx status is not the responsibility only of Kubernetes, but also the application itself.

A Kubernetes termination lifecycle has a couple of important phases, which needs to be considered. This document won’t go into details, but only the most important steps in the termination lifecycle are explained.

1. The termination of the Pod
2. Prestop hook is called. This hook runs concurrent with the Kubernetes termination grace period. Usually used to do some cleanups. The duration of the hook should not be longer than the terminationGracePeriodSeconds value.
3. SIGTERM signal sent to Pod.
4. Kubernetes wait for a grace period. In the “skeleton-mongo-app“ Helm chart the default value is 30 seconds (terminationGracePeriodSeconds).
5. SIGKILL signal sent to Pod and Pod will be removed.

**Adjustment 1**

The first adjustment is that the application needs to have support for graceful shutdown. When the application is being told to shutdown, it must stop accepting new connections and graceful handle existing connections. For Spring Boot application this must be set in the application.properties (<https://docs.spring.io/spring-boot/docs/2.3.0.RELEASE/reference/html/spring-boot-features.html#boot-features-graceful-shutdown> ).

`server.shutdown=graceful`

When requests longer than a specific time exist in the application, use the “spring.lifecycle.timeout-per-shutdown-phase“ property.

`spring.lifecycle.timeout-per-shutdown-phase=60s`

Keep in mind that “terminationGracePeriodSeconds“ also depends on the value above.

**Adjustment 2**

In the deployment file of the Helm chart a lifecycle “prestop” hook needs to be added. See the example as below. The sleep time needs to be less or equal the time of the “terminationGracePeriodSeconds“. In this case Kubernetes is being told to wait for 30 seconds before terminating the Pod. Without this waiting time it’s possible that requests are not processed correctly.

spec:
containers:
image: 050356841556.dkr.ecr.eu-west-1.amazonaws.com/routescout:develop-b330
imagePullPolicy: IfNotPresent
lifecycle:
preStop:
exec:
command: ["sh", "-c", "sleep 30"]

Sources:

<https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-terminating-with-grace>

<https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/web/server/Shutdown.html>

<https://docs.spring.io/spring-boot/docs/2.3.0.RELEASE/reference/html/spring-boot-features.html#boot-features-graceful-shutdown>