---
id: confluence:181108745
source: confluence
type: page
space: TC
title: Host frontend on AWS
author: Damon Asberg
date: '2025-10-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181108745
explicit_links: []
---
# Host frontend on AWS

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/181108745  

## Content

Last updated: 2025-10-27

**Steps**

1. Creating S3 bucket (hosting the code)
2. Create cloudfront instance (SSL secure)
3. Route 53 DNS entry (link the .teqplay.nl URL to the bucket)

## Step 0: Login to the AWS console

1. Go to the AWS console: <https://teqplay.awsapps.com/start/#/?tab=accounts>
2. If you have an account login with the credentials
3. If you don't have an account yet, request one with Richard or ask if someone can help you on Slack

## Step 1: S3 Bucket

1. Go to *Services* at the top and search on `S3`
2. Click *Create Bucket*
3. Fill in the bucket name as followed and replace <PROJECT\_NAME> `<PROJECT_NAME>.teqplay.nl`
4. Region should be EU (Ireland)
5. Click on the *Create*
6. Select the bucket you just created in the list
7. Go to the *Permissions* tab and *Ensure that in* the *Block public access* -> the `all` option is enabled
8. Deploy the build from the project to the bucket by using the AWS CLI: [Tutorial](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Deploy%20React%20with%20Command%20Line)

## Step 2: Create Cloudfront instance

1. Go to *Services* at the top and search on `cloudfront`
2. Click on *Create distribution* and select *Web*
3. *Origin Domain Name* select just created bucket `<PROJECT_NAME>.teqplay.nl`
4. *Viewer Protocol Policy* select `Redirect HTTP to HTTPS`
5. *Allowed HTTP Methods* select `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`
6. *Alternate Domain Names* fill in the URL `<PROJECT_NAME>.teqplay.nl`
7. *SSL Certificate* Select `Custom SSL Certificate (example.com)` and select the one with `*.teqplay.nl`
8. *Default Root Object* fill in `index.html`
9. That's it, click on *Create distribution*
10. Click on the distribution and go to the *Errors* tab. Click *Create Custom Error Response*. Do the following twice, once for the `403` and once for the `404`. Select the *HTTP Error Code* (403/404), *Customize Error Response*: `Yes`, *Response Page Path*: `/index.html`, *HTTP Response Code*: `200 OK`
11. Make sure when you deploy a new version for the bucket that you automatically invalidate the cashed objects. This will be done by adding this line to the deploy command (Replace the *<DISTRIBUTION\_ID>*): `&& aws cloudfront create-invalidation --distribution-id <DISTRIBUTION_ID> --paths /*`
12. Ensure that in the *Origins tab* that the S3 Origin has a OAC(**Origin access controls**) Associated with it, if not add the (cloudfront-s3-oac).
13. If there was a OAC Associated to the S3 Origin it should have created a policy in the S3 bucket ensure that policy is created, if not add the policy  
    example policy

    {
    "Version": "2012-10-17",
    "Statement": [
    {
    "Sid": "AllowCloudFrontServicePrincipalRead",
    "Effect": "Allow",
    "Principal": {
    "Service": "cloudfront.amazonaws.com"
    },
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::\_\_BUCKET\_NAME\_\_/\*",
    "Condition": {
    "StringEquals": {
    "AWS:SourceArn": "arn:aws:cloudfront::050356841556:distribution/\_\_CLOUDFRONT\_DISTROBUTION\_ID\_\_"
    }
    }
    }
    ]
    }

## Step 3: Route 53, Add DNS record

1. Go to *Services* at the top and search on `Route 53`
2. Go to *Hosted zones* select <http://teqplay.nl> and press *Create record* -> *Simple routing* -> *Define simple record*
3. Fill in the URL you defined for the bucket. It will find the s3 bucket, or when you select (instead of the Alias to S3… value) Alias to Cloudfront… the right bucket/cloudfront instance will appear. Than the record type will automatically be A
4. Press *Define simple record* and it is done, it should work after waiting for a bit