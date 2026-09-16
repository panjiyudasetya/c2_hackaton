---
id: confluence:397672498
source: confluence
type: page
space: TC
title: Making a new live release
author: Shan Minh Nguyen (Unlicensed)
date: '2024-11-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/397672498
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/397672498
---
# Making a new live release

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/397672498  

## Content

Currently there are two ways to make a release:

* One is by merging develop into master where you would also need to do the following:

  + Make a new branche from master to update project version by updating two files and commit with removing the -SNAPSHOT line
  + src/main/resources/application.properties - info.project.version
  + build.gradle - base\_version
  + (Optional to check) Make sure the CHANGELOG.md is updated with the latest changes under the new version
* The second option is by making a branch from develop with the updated release versioning and make a pull request to master whilst still following the substeps above

In CI, once the above steps has been done and CI has build successfully, we can deploy to live by approving the hold-production step

Once the deployment is build successfully by seeing a green check mark in deploy-production, we need to update the develop branch versioning by updating the 2 files again by 1 minor version, e.g. from 5.31.0-SNAPSHOT -> 5.32.0-SNAPSHOT

Before deploying to live these steps can also be taken as an additional step in case it’s needed (this is depending on the changes):

* (1) Backup the current config by creating a new configmap resource as a fallback