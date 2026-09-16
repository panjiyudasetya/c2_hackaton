---
id: confluence:524550152
source: confluence
type: page
space: TC
title: Velero encrypted backups
author: Minh Trang Nguyen (Unlicensed)
date: '2024-11-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/524550152
explicit_links:
- github:teqplay/velero-plugin-for-aws:pr:1
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/524550152
---
# Velero encrypted backups

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/524550152  

## Content

At the time of this writing, Velero backup snapshots were not encrypted, which is an expectation of customers. To avoid enabling encryption by default, it is preferable to enable encryption solely for the snapshots. It is not possible to instruct Velero to encrypt the snapshots directly, as the AWS API does not support this functionality. The only method to encrypt snapshots is by customizing the Velero AWS plugin to perform the encryption. The solution below should only be used until encryption is enabled by default in the clusters. The diagram below illustrates the process by which the snapshots are encrypted.

Figure 1: process to encrypt snapshots

The blue-colored boxes illustrate the default behavior of the Velero plugin. The plugin invariably creates unencrypted snapshots as an initial step. This is a mandatory process, as the creation of an unencrypted snapshot must be completed before encryption can be applied. Consequently, it is necessary to wait for the unencrypted snapshot creation process to finish before proceeding with the encryption.

In addition to the Velero backup jobs, a CronJob is executed every 30 minutes to identify and delete any unencrypted snapshots created by Velero.

## Custom code

The following custom adjustments have been made to the AWS plugin version v1.5.3. The details of these adjustments are provided below. The steps outlined below demonstrate how to implement these adjustments. As this version of the plugin is no longer supported, it is not necessary to keep up with changes to the AWS plugin.

The custom changes are located in repository https://github.com/teqplay/velero-plugin-for-aws/pull/1

Load your temporary AWS environment variables, which can be found in the AWS access portal. See picture below.

aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin 050356841556.dkr.ecr.eu-west-1.amazonaws.com
IMAGE\_VERSION=4
docker build --platform=linux/amd64 -t teqplay/custom-velero-plugin-for-aws .
docker tag teqplay/custom-velero-plugin-for-aws:latest 050356841556.dkr.ecr.eu-west-1.amazonaws.com/teqplay/custom-velero-plugin-for-aws:${IMAGE\_VERSION}
docker push 050356841556.dkr.ecr.eu-west-1.amazonaws.com/teqplay/custom-velero-plugin-for-aws:${IMAGE\_VERSION}

## Changes to Velero deployment

In the deployment of Velero, it is necessary to set the environment variable `KMS_KEY_ID`. AWS requires this key to encrypt the snapshots.

kubectl get deploy
NAME READY UP-TO-DATE AVAILABLE AGE
velero 1/1 1 1 2y14dkubectl edit deploy velero

Paste the environment variable into the deployment.

**Develop cluster**

 - name: KMS\_KEY\_ID
value: arn:aws:kms:eu-west-1:050356841556:key/00934cd1-fde9-418d-8144-f7265259be14

**Production cluster**

 - name: KMS\_KEY\_ID
value: arn:aws:kms:eu-west-1:050356841556:key/283b9db4-b661-4a31-b63a-99e7f710c551

Change the image with the value build in the previous step:

050356841556.dkr.ecr.eu-west-1.amazonaws.com/teqplay/custom-velero-plugin-for-aws:4

Save the changes!

## Test run

Run a test by running the following command.

velero backup create --from-schedule daily-schedule

## Cronjob

Every 30 minutes, a job will run to remove unencrypted snapshots created by Velero. The code is located in the `kubernetes-scripts` repository.