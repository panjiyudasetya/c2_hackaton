---
id: confluence:854687745
source: confluence
type: page
space: TC
title: Host frontend on AWS (Updated) - BETA
author: David Hansson
date: '2025-10-23'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/854687745
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/854687745
---
# Host frontend on AWS (Updated) - BETA

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/854687745  

## Content

**Steps**

1. Creating S3 bucket (hosting the code)
2. Create cloudfront instance (SSL secure)
3. Route 53 DNS entry (link the .teqplay.nl URL to the bucket)

## Step 0: Login to the AWS console

1. Go to the AWS console: <https://teqplay.awsapps.com/start/#/?tab=accounts>
2. If you have an account login with the credentials
3. If you don't have an account yet, request one with Richard or ask if someone can help you on Slack

## Step 1: S3 Bucket

1. Go to *Services* at the top and search for `S3`.
2. Click *Create Bucket*.
3. Enter the bucket name as `<PROJECT_NAME>.teqplay.nl`.
4. Disable ACLs (recommended).
5. Set the region to EU (Ireland) (Should be default by account check navbar).
6. Click *Create*.
7. Select the newly created bucket from the list.
8. Go to the *Properties* tab, select *Static website hosting*, and activate *Use this bucket to host a website*. Enter `index.html` for both *Index document* and *Error document*, then click *Save*.
9. Go to the *Permissions* tab, edit *Block public access*, disable the `all` option, and save.
10. In *Bucket Policy*, enter the following text, replacing `<PROJECT_NAME>`:

    json{
    "Version": "2012-10-17",
    "Statement": [
    {
    "Sid": "PublicReadGetObject",
    "Effect": "Allow",
    "Principal": "\*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::<PROJECT\_NAME>.teqplay.nl/\*"
    }
    ]
    }
11. Return to the *Permissions* tab and enable the following blocks: `new access control lists`, `any access`, `new public bucket or access point policies`, then click *Save*.
12. Deploy the project build to the bucket using the AWS CLI: [Tutorial](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Deploy%20React%20with%20Command%20Line).

## Step 2: Create Cloudfront instance

1. Go to *Services* at the top and search for `cloudfront`.
2. Click on *Create distribution* and select *Web*.
3. Enter the *Distribution name* as `<PROJECT_NAME>.teqplay.nl`.
4. Select Single website or app.
5. Press Next.
6. Set Origin type to Amazon S3.
7. For S3 Origin, click browse and search for your `<PROJECT_NAME>` (it may take time to load or require pagination).
8. *This S3 bucket has static web hosting enabled. If you plan to use this distribution as a website, we recommend using the S3 website endpoint instead of the bucket endpoint. (Press use website endpoint).*
9. Keep the settings as default & recommended.
10. Set Security WAF to Disabled.
11. Create the distribution.
12. After creation, go to General > Settings and add Alternate domain name: `<PROJECT_NAME>.teqplay.nl` (this will auto-fill the TLS/SSL).
13. Save it.
14. Go to Edit settings.
15. *Add Default Root Object*: enter `index.html` and save.
16. Click on the distribution and go to the *Errors* tab. Click *Create Custom Error Response*. Do this twice, once for `403` and once for `404`. Set the *HTTP Error Code* (403/404), *Customize Error Response*: `Yes`, *Response Page Path*: `/index.html`, and *HTTP Response Code*: `200 OK`.
17. When deploying a new version for the bucket, automatically invalidate the cached objects by adding this line to the deploy command (replace *<DISTRIBUTION\_ID>*): `&& aws cloudfront create-invalidation --distribution-id <DISTRIBUTION_ID> --paths /*`.

## Step 3: Route 53, Add DNS record

1. Go to *Services* at the top and search for `Route 53`.
2. Navigate to *Hosted zones*, select [**teqplay.nl**](http://teqplay.nl), and click *Create record* -> *Simple routing* -> *Define simple record*.
3. Enable the Alias switch.
4. Select Alias to CloudFront distribution.
5. Enter the URL for the bucket. This will locate the S3 bucket. If you choose Alias to CloudFront instead of Alias to S3, the correct bucket or CloudFront instance will appear, and the record type will automatically change to A.
6. Click *Define simple record*, and it will be set up. It should work after a brief wait.

## Step 4: Add the variables into actions

1. Add variables in your github project CI, **S3\_BUCKET** + **CLOUDFRONT\_DISTRIBUTION\_ID**

+ Add **Main.yml** file in your project:

yamlwide760name: Build and deploy
run-name: ${{ github.event.head\_commit.message }}
on:
push:
branches:
- master
- develop
pull\_request:
branches:
- master
- develop
jobs:
build-and-deploy:
name: Frontend build and deploy
uses: teqplay/actions/.github/workflows/frontend-standard.yml@master
secrets:
aws\_access\_key\_id: ${{ secrets.aws\_access\_key\_id }}
aws\_secret\_access\_key: ${{ secrets.aws\_secret\_access\_key }}
npm\_token: ${{ secrets.npm\_token }}
sentry\_auth\_token: ${{ secrets.sentry\_auth\_token }}
slack\_bot\_token: ${{ secrets.slack\_bot\_token }}
dt\_api\_key: ${{ secrets.dt\_api\_key }}
with:
environments: ${{ github.ref == 'refs/heads/master' && '["data","production","develop"]' || '["develop"]' }}
slack\_bot\_token: ${{ secrets.SLACK\_BOT\_TOKEN }}