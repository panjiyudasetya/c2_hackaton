---
id: confluence:652050471
source: confluence
type: page
space: TC
title: Host your front-end project with AWS
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652050471
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652050471
---
# Host your front-end project with AWS

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652050471  

## Content

**Steps:** - Creating s3 bucket (hosting the code) - Create cloudfront instance (SSL secure) - Route 53 DNS entry (link the .teqplay.nl URL to the bucket)

## Login

1. Go to the AWS console: <http://console.aws.amazon.com/>
2. Account ID is `teqplay`
3. If you have an account login with the credentials
4. If you don't have an account yet, request one with Vasyl / Richard / ask if someone can help you on slack

## S3 Bucket

1. Go to *Services* at the top and search on `S3`
2. Click *Create Bucket*
3. Fill in the bucket name as followed and replace <PROJECT\_NAME> `<PROJECT_NAME>.teqplay.nl`
4. Region should be EU (Ireland)
5. Click on the *Create*
6. Select the bucket you just created in the list
7. Go to the *Properties* tab and select *Static website hosting* -> activate *Use this bucket to host a website*. Fill in `index.html` at *Index document* and also for *Error document* -> *Save*
8. Go to the *Permissions* tab and *Edit* the *Block public access* -> Disable the `all` option and save
9. Go to *Bucket Policy* and fill in the following text and replace again <PROJECT\_NAME>:`{ "Version": "2012-10-17", "Statement": [ { "Sid": "PublicReadGetObject", "Effect": "Allow", "Principal": "*", "Action": "s3:GetObject", "Resource": "arn:aws:s3:::<PROJECT_NAME>.teqplay.nl/*" } ] }`
10. Go back to the *Permissions* tab and enable 3 blocks: `new access control lists`, `any access`, `new public bucket or access point policies` -> press *save*
11. Deploy the build from the project to the bucket by using the AWS CLI: [Tutorial](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Deploy%20React%20with%20Command%20Line)

## Create Cloufront instance

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

## Route 53, Add DNS record

1. Go to *Services* at the top and search on `Route 53`
2. Go to *Hosted zones* select <http://teqplay.nl> and press *Create record* -> *Simple routing* -> *Define simple record*
3. Fill in the URL you defined for the bucket. It will find the s3 bucket, or when you select (instead of the Alias to S3… value) Alias to Cloudfront… the right bucket/cloudfront instance will appear. Than the record type will automatically be A
4. Press *Define simple record* and it is done, it should work after waiting for a bit