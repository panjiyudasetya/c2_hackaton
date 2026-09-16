---
id: confluence:966328321
source: confluence
type: page
space: TC
title: Thanos in new dev cluster
author: Joost Laurman
date: '2025-11-05'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/966328321
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/966328321
---
# Thanos in new dev cluster

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/966328321  

## Content

As of today thanos can access the S3 bucket in the production AWS by the `ThanosS3BucketAccess` policy.

There is this policy in place allowing Thanos access to the S3 bucket in the production AWS. That is currently working because it’s allowing public access.

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "ThanosCrossAccountS3Access",
"Effect": "Allow",
"Action": [
"s3:ListBucket"
],
"Resource": "arn:aws:s3:::data.thanos.teqplay"
},
{
"Sid": "ThanosCrossAccountS3ObjectAccess",
"Effect": "Allow",
"Action": [
"s3:GetObject",
"s3:PutObject",
"s3:DeleteObject"
],
"Resource": "arn:aws:s3:::data.thanos.teqplay/\*"
}
]
}