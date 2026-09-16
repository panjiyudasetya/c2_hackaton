---
id: confluence:1279721474
source: confluence
type: page
space: TC
title: Resources for Terraform Conversion
author: Jamie de Leest
date: '2026-07-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1279721474
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1279721474
---
# Resources for Terraform Conversion

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1279721474  

## Content

Resources that should be converted to terrafrom

* EKS Cluster

  + Node Groups
  + Addons
  + Pod Identity associations
  + Fargate Profiles
  + OIDC Provider
  + Access Entries
  + Access Policy Associations
* ECR
* EC2

  + Instances

    - AIS-Forwarder
    - PowerBI Gateway
    - OpenVPN
    - VesselMatcherMail
    - IHS ports
  + Volumes

    - AIS-Forwarder
    - PowerBI Gateway
    - OpenVPN
    - VesselMatcherMail
    - IHS ports
  + Launch Templates
  + Security Groups
  + Elastic IPs
* Route 53

  + Hosted zones
* VPC

  + Subnets
  + Route tables
  + Internet gateways
  + NAT gateway
  + Peering connectinos
  + Network ACL
* RDS
* AWS Backup
* IAM

  + Roles
  + Policies
  + Users
  + Identity Providers
* IAM Identity Center
* Certificate Manager
* CloudWatch

  + Alarms
* Application S3 Buckets

  + Ship-history
  + Event-history
  + Navista/VesselCompliance
  + Bunkerplanner
  + Portreporter
* CloudFront

  + S3 buckets related to CloudFront
* Lambda
* SES
* MTurk
* Secret Manager
* KMS
* GuardDuty

Excluded

* Load balancers (Managed by AWS load balancer)
* EKS Volumes (Managed by EBS CSI)
* Route53 Routes (Managed by external DNS)
* CloudWatch Logs (Managed by Fluent-bit)