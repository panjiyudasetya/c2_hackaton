---
id: confluence:900366338
source: confluence
type: page
space: TC
title: Recreate Prometheus ALB
author: Joost Laurman
date: '2025-11-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/900366338
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/900366338
---
# Recreate Prometheus ALB

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/900366338  

## Content

Problem will look like this:

`prometheus-dev` in the old cluster can no longer come up. It will always stay unhealthy/unready.

This is caused by a race condition between the creation of two Service

* prometheus-server
* prometheus-server-test

Prometheus-server is the regular Service. It is used to expose the data from prometheus to port `80`.

Prometheus-server-test is the ALB to let the new DEV cluster access the old one.

When things blow you need to remove:

* Service - prometheus-server-test
* Endpoint - prometheus-server-test

Make sure `prometheus` gets up again.

As soon as it's up, you can re-create the Service again.

yamlwide760apiVersion: v1
kind: Service
metadata:
name: prometheus-server-test
namespace: monitoring
spec:
ports:
- name: http
protocol: TCP
port: 3222
targetPort: 9090
selector:
app.kubernetes.io/component: server
app.kubernetes.io/instance: prometheus
app.kubernetes.io/name: prometheus

Prometheus-server service for reference

yamlwide760apiVersion: v1
kind: Service
metadata:
name: prometheus-server
namespace: monitoring
spec:
ports:
- name: http
protocol: TCP
port: 80
targetPort: 9090
selector:
app.kubernetes.io/component: server
app.kubernetes.io/instance: prometheus
app.kubernetes.io/name: prometheus

This will register the application to the load balancer. Now it should be working again.