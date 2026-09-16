---
id: confluence:1179680769
source: confluence
type: page
space: TC
title: 'Guide: Migrating from AWS Access Keys → EKS Pod Identity'
author: Jamie de Leest
date: '2026-06-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1179680769
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1179680769
---
# Guide: Migrating from AWS Access Keys → EKS Pod Identity

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1179680769  

## Content

# 1. Developer Changes

## 🔴 What needs to change?

**Remove all explicit credential providers from AWS clients.**

The AWS SDK will automatically use the Pod Identity credentials.

---

## Example 1 (❌ Old → ✅ New)

### ❌ Before (using static credentials)

wide760@Configuration
class S3Configuration(private val properties: S3Properties) {
@Bean
fun s3Client(): S3Client {
val credentials = AwsBasicCredentials.create(properties.keyId, properties.secretKey)
return S3Client.builder()
.region(Region.of(properties.region))
.credentialsProvider(StaticCredentialsProvider.create(credentials))
.build()
}
}

### ✅ After (using Pod Identity)

wide760@Configuration
class S3Configuration(private val properties: S3Properties) {
@Bean
fun s3Client(): S3Client {
return S3Client.builder()
.region(Region.of(properties.region))
.build()
}
}

👉 **Key change:**  
Remove `.credentialsProvider(...)` entirely.

---

## Example 2 (Already compatible ✅)

wide760val s3Client =
S3Client {
region = archive.region.replace('\_', '-')
if (archiveGlobal.credentials != null) {
credentialsProvider =
StaticCredentialsProvider {
accessKeyId = archiveGlobal.credentials.accessKeyId
secretAccessKey = archiveGlobal.credentials.secretKey
}
}
httpClient(CrtHttpEngine)
}

### Why this works

* If no credentials are provided → SDK falls back to **default provider chain**
* This includes **EKS Pod Identity automatically**

👉 No changes needed **as long as credentials are not passed**

---

# 2. DevOps Changes (AWS / EKS)

There are **two scenarios**:

---

# Scenario A: Same AWS Account

## Steps

1. **Create IAM Role**

   * Copy permissions from existing IAM user
2. **Set trust policy for EKS Pod Identity**

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Service": "pods.eks.amazonaws.com"
},
"Action": [
"sts:AssumeRole",
"sts:TagSession"
]
}
]
}

3. **Attach permissions**

   * Example: S3 access policy
4. **Attach role to Kubernetes Service Account**

   * In the AWS EKS Console under access Via **EKS Pod Identity association** add a new entry for a EKS Pod Identity

---

# Scenario B: Cross-Account Access

When:

* EKS cluster is in **Account DEV**
* Resource (e.g. S3) is in **Account PROD**

---

## Step 1 — Role in Resource Account (Account PROD)

### Trust policy

Allow the STS role from Account DEV:

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"AWS": "arn:aws:iam::<DEV\_ACCOUNT\_ID>:role/<DEV\_ROLE\_NAME>"
},
"Action": [
"sts:AssumeRole",
"sts:TagSession"
]
}
]
}

### Permissions (example S3)

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "ListObjectsInBucket",
"Effect": "Allow",
"Action": "s3:ListBucket",
"Resource": "arn:aws:s3:::<S3\_BUCKET\_NAME>"
},
{
"Sid": "GetAllObjectActions",
"Effect": "Allow",
"Action": "s3:GetObject\*",
"Resource": "arn:aws:s3:::<S3\_BUCKET\_NAME>/\*"
}
]
}

---

## Step 2 — Role in EKS Account (Account DEV)

### Trust policy (Pod Identity)

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Service": "pods.eks.amazonaws.com"
},
"Action": [
"sts:AssumeRole",
"sts:TagSession"
]
}
]
}

### Permissions (Assume target role)

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "AssumeTargetRole",
"Effect": "Allow",
"Action": [
"sts:AssumeRole",
"sts:TagSession"
],
"Resource": "arn:aws:iam::<PROD\_ACCOUNT\_ID>:role/<PROD\_ROLE\_NAME>"
}
]
}

---

## Step 3 — EKS Pod Identity Association

| Field | Value |
| --- | --- |
| IAM Role | `arn:aws:iam::<DEV_ACCOUNT_ID>:role/<DEV_ROLE_NAME>` |
| Target IAM Role | `arn:aws:iam::<PROD_ACCOUNT_ID>:role/<PROD_ROLE_NAME>` |
| Namespace | `<K8S_NAMESPACE>` |
| Service Account | `<K8S_SERVICE_ACCOUNT>` |
| Session Tags | Enabled |

---

# 3. How It Works (Flow)

1. Pod starts
2. Pod Identity injects credentials
3. AWS SDK uses default credential chain
4. SDK assumes IAM role automatically
5. (Optional) STS assumes cross-account role
6. App accesses AWS resources