---
id: confluence:872316930
source: confluence
type: page
space: TC
title: Migration Guide to migrate applications to new dev cluster
author: Joost Laurman
date: '2025-10-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/872316930
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/872316930
---
# Migration Guide to migrate applications to new dev cluster

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/872316930  

## Content

Only for small applications, not for the big ones where hours of migration of database is needed. (Estimated Time for Synchronization)

1. Talk to the product owner to make sure this is a good time to migrate this application
2. Announce in **#backend** that we are migrating this application
3. Get everything from the old cluster

   1. configmap -> copy from the old cluster and update values from mongodb
4. Turn off application in old cluster
5. Do an export of the database in the old cluster  
   -> A port forward can only handle tiny databases, connect directly, e.g. mongodb://username:password@mongodb-customer-apps-dev.eks-dev.teqplay:27017/
6. Make a commit in the repository of the application and change the GitHub actions workflow (often found in `.github/main.yml`) to:

   name: Teqplay Standard Workflow
   run-name : ${{ github.event.head\_commit.message }}
   on: [push]
   jobs:
   external-main:
   name: Teqplay standard workflow
   uses: teqplay/actions/.github/workflows/backend-standard.yml@new-cluster
   with:
   dependency\_track: true
   enable\_develop: false
   enable\_new\_develop: true
   secrets:
   aws\_access\_key\_id: ${{ secrets.AWS\_ACCESS\_KEY\_ID }}
   aws\_secret\_access\_key: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY }}
   aws\_access\_key\_id\_develop: ${{ secrets.AWS\_ACCESS\_KEY\_ID\_NEW\_CLUSTER }}
   aws\_secret\_access\_key\_develop: ${{ secrets.AWS\_SECRET\_ACCESS\_KEY\_NEW\_CLUSTER }}
   cm\_username: ${{ secrets.CM\_USERNAME }}
   cm\_password: ${{ secrets.CM\_PASSWORD }}
   dt\_api\_key: ${{ secrets.DT\_API\_KEY }}

Make sure to keep the existing `with` parameters e.g. `java_version` or `override_gradle_properties`

In the `helm/values.yml`, move the global items to the `values.prod.yml`:

wide760global:
storageClass: "gp2"
namespaceOverride: "teqplay-app"

In the `values.dev.yml`, add these MongoDB and ingress items:

wide760mongodb:
persistence:
storageClass: gp3-retained
hostedzone: dev.teqplay.dev
ingress:
certificateArn: arn:aws:acm:eu-west-1:704630444514:certificate/715d1cb6-0c1a-4717-8cf1-38afb68b9fd6
group: eks-dev
scheme: internet-facing
securityGroups: sg-0d26e09d2ee59f8c6,sg-09a7040413dd11218
subnets: subnet-030ca4bb313172e24,subnet-0a8c44f920ea72840

Skip the MongoDB part if the app doesn’t have its own MongoDB.

7. Now install the application in the new cluster. Especially important when the application is using it’s own separate database instance. We do this initial installation via helm charts. Open up the skeleton-mongo-app and click on install.

   Copy the existing helm chart for the application from the old dev cluster. Also make sure to use the ***version*** of the new ***build*** you created in the previous step. You can find the release version in the publish docker image step.

   Here the release version is *new-cluster-2025-09-18-b85.3*

   When installing, set these values for the ingress:

wide760ingress:
certificateArn: arn:aws:acm:eu-west-1:704630444514:certificate/715d1cb6-0c1a-4717-8cf1-38afb68b9fd6
group: eks-dev
scheme: internet-facing
securityGroups: sg-0d26e09d2ee59f8c6,sg-09a7040413dd11218
subnets: subnet-030ca4bb313172e24,subnet-0a8c44f920ea72840

If any `storageClass` is set, make sure it’s using `gp3-retained`

Don’t forget to select the right **namespace** and to give the proper **name**.

8. The next time you can also deploy it via GitHub actions.

   There is now an extra branch, Deploying on Develop OU
9. Make sure it’s running and working fine by looking at the pod logs.
10. Now scale down the deployment so we can finish up the database migration
11. Import the database in the new cluster
12. In Route 53 (AWS Console) in the old cluster, find the record. Then delete the helm release from the old cluster, this will automatically delete the record as well. Create the record again, now with CNAME record type and value:

    k8s-eksdev-bb7a781d42-1455069575.eu-west-1.elb.amazonaws.com
13. Also create the same record in the **PRIVATE** `dev.teqplay.com` domain. This is used when using the VPN and for internal networks.
14. If this application is inside on of those routes of external-api:

     - routes-platform
    - routes-csi
    - routes-ship-history
    - routes-ship-history-platform
    - routes-event-history
    - routes-event-history-platform
    - routes-vesselvoyage
    - routes-vesselvoyage-v2
    - routes-poma

    If this is the case, edit the specific route. This is a `configMap` inside the `teqplay-api` namespace. Update urls like:  
    `http://poma-dev.core-service:8080`   
    to   
    `https://backendpoma.dev.teqplay.com`
15. Scale up the deployment again
16. Check everything is working correctly
17. Do another restart and check everything is coming up as expected
18. Announce in **#backend** that the migration of this application has been completed and from now on people should use the new cluster to manage the application
19. Create a PR for the workflow file change
20. Make a note in the agenda to undeploy everything for this application in a week time