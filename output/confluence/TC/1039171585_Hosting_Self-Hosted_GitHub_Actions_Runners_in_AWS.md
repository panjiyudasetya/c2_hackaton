---
id: confluence:1039171585
source: confluence
type: page
space: TC
title: Hosting Self-Hosted GitHub Actions Runners in AWS
author: Jamie de Leest
date: '2025-12-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1039171585
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1039171585
---
# Hosting Self-Hosted GitHub Actions Runners in AWS

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1039171585  

## Content

This document outlines the plan to migrate to self-hosted GitHub Actions runners in Q1 2026 to address the issue of our publicly accessible EKS cluster endpoint.

Currently, we cannot disable public access to the cluster because GitHub Actions requires network access to deploy our application. If we disable the public endpoint, GitHub’s hosted runners would no longer be able to reach the cluster.

To solve this, we intend to deploy GitHub Actions self-hosted runners inside our VPC. This will allow GitHub Actions to interact with the private EKS cluster endpoint without exposing it to the internet.

Enabling the public endpoint on an EKS cluster means that the Kubernetes API server can be reached from outside our VPC. Although Kubernetes still enforces authentication and authorization, restricting access to only within the VPC provides an additional security layer. Moving to private-only access will improve our overall security posture by eliminating external exposure of the control plane.

Two possible approaches to hosting GitHub Actions runners within our AWS infrastructure. Both solutions allow us to execute CI/CD workloads on our own compute instead of using GitHub’s hosted runners. and this allows us to disable the public endpoint for our EKS cluster.

---

# Option A — EC2-Based Self-Hosted Runners

### Summary

Deploy one or more EC2 instances that run the GitHub Actions runner service directly.

### Steps

1. **Create an IAM Role for the Runner**

   * Permissions for SSM (for maintenance)
   * ECR pull permissions (if needed)
   * CloudWatch logging/metrics
2. **Launch EC2 Instances**

   * Choose an instance type based on expected workload
   * Use an Auto Scaling Group (optional)
3. **Install Runner Software**

   * Download and extract the GitHub Actions runner package
   * Register runner with repo/org using GitHub-provided token
   * Install runner as a systemd service for auto-restart
4. **Enable Scaling (Optional)**

   * Add multiple EC2 runners behind an Auto Scaling Group
   * Trigger scale-out based on CPU, queue length, or GitHub Webhook events
   * Scale-in when idle

# Option B — Kubernetes-Based Self-Hosted Runners

### Summary

Run ephemeral or persistent GitHub runners inside our Kubernetes cluster using the **Actions Runner Controller (ARC)**.

### Steps

1. **Install Prerequisites**

   * Ensure cluster has enough resources
   * Ensure cluster has access to GitHub (for registration)
2. **Deploy the Actions Runner Controller**

   * Install via Helm chart
   * Configure GitHub App authentication
   * Configure permissions (repo or organization scope)
3. **Create Runner Deployments**  
   Options:

   * **Ephemeral runners** (one runner per job, auto-destroyed)
   * **Persistent runners** (always available)
4. **Configure Scaling**

   * ARC supports auto-scaling based on queued workflow jobs
   * Runners spin up only when needed → cost efficient
   * Each job runs in its own Pod → high isolation
5. **Integrate with Kubernetes Tooling**

   * Monitoring via Prometheus/Grafana
   * Logging via CloudWatch Container Insights
   * Deploy resource limits and node selectors
6. **Security**

   * Let runners run in isolated Pods
   * Use Pod Security Policies or namespaced isolation
   * No direct machine access needed (ARC manages everything)

---

# Conclusion

Both approaches work well in AWS:

* **EC2 Runners** are simple and easy to maintain, good for small teams or consistent workloads.
* **Kubernetes Runners** give the best scalability, isolation, and cost efficiency — ideal if we want CI/CD that adapts to demand.

We can choose based on:

* Our expected workload
* How much Kubernetes we want to maintain
* Cost considerations