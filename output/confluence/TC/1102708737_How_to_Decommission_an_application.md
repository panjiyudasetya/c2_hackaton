---
id: confluence:1102708737
source: confluence
type: page
space: TC
title: How to Decommission an application
author: Joost Laurman
date: '2026-01-30'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1102708737
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1102708737
---
# How to Decommission an application

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1102708737  

## Content

To delete / decommission an application completely, exectute the following steps:

1. In AWS:

   1. **Cloudfront**

      1. Disable Cloudfront distributions related to this
      2. Delete the Cloudfront distributions that you disabled in previous step
   2. **S3**

      1. Empty buckets from the front-end applications or related to saving data from the application
      2. Delete the buckets that you emptied in the previous step
   3. **ECR**

      1. Delete the private repository that is storing images for this application
   4. **Databases**

      1. Remove any RDS that is related to this application
   5. **Route53**

      1. For production, remove URL’s related to this application
      2. For develop, this is managed by `external-dns`
2. In Kubernetes:

   1. Uninstall **helm release** from production cluster
   2. Uninstall **helm release** from develop cluster
   3. Remove any left-over **ConfigMaps**
   4. Remove any left-over **Secrets**
   5. Remove any left-over **Network Policies**
   6. Remove any left-over **Persistent Volume Claims (PVC)**
   7. Remove any left-over **Persistent Volumes (PV)**
   8. If any PVC/PV has been deleted, delete those **Volumes** as well from AWS EC2 → EBS → Volumes section
3. In NoSQLBooster (or any other mongodb client)

   1. If application was inside a shared database, removed the database from there
4. In Keycloak

   1. From the DEV or PROD realm remove any **Clients** related to this application
5. In GitHub

   1. Archive the repositories (front- and backend) so it’s clear it’s no longer active