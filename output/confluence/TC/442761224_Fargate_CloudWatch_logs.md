---
id: confluence:442761224
source: confluence
type: page
space: TC
title: Fargate CloudWatch logs
author: Minh Trang Nguyen (Unlicensed)
date: '2024-08-22'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/442761224
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/442761224
---
# Fargate CloudWatch logs

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/442761224  

## Content

The log data from Fargate instances are transmitted to CloudWatch through AWS Fluentbit. The log groups associated with this process are `eks/develop/fluent-bit-cloudwatch` and `eks/production/fluent-bit-cloudwatch`. The configuration for this operation is defined in the "aws-logging" ConfigMap.