---
id: confluence:426672141
source: confluence
type: page
space: TC
title: Prometheus Push Gateway metrics
author: Minh Trang Nguyen (Unlicensed)
date: '2024-08-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/426672141
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/426672141
---
# Prometheus Push Gateway metrics

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/426672141  

## Content

## Kubernetes secrets

It's not always possible to have a continuous stream of metrics gathered by Prometheus. Metrics collected ad-hoc need to be sent to the Prometheus Push Gateway. To obtain metrics about the usage of Kubernetes secrets, a script was created to gather these metrics. The Kubernetes cluster logs are located in the CloudWatch log groups `/aws/eks/develop/cluster` and `/aws/eks/production/cluster`. The script processes the data from the logs and sends metrics to the Prometheus Push Gateway.

### Solution

The figure below illustrates the solution as a process. This solution does not require a CI/CD pipeline to build a Docker image, which would need to be stored in the Elastic Container Registry. It is easily managed and maintained. The cronjob depends on a secret, configmap, and network policy. It runs every hour to obtain log data from CloudWatch, filtering the data based on the Kubernetes actions GET, LIST, CREATE, DELETE, and PATCH. The job will then push these actions to the Prometheus Push Gateway, and the metrics will be displayed in Grafana.

### Grafana

The metrics are displayed in Grafana, as shown in the figure below.

The dashboard shows who accessed which secrets in which namespace. If a line is red, it indicates that the secrets were accessed more than usual.

### Code

The implementation is located in the Git repository `kubernetes-scripts` in the directory `prometheus-push-gateway`.