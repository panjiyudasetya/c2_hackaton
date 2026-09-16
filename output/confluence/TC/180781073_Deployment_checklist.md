---
id: confluence:180781073
source: confluence
type: page
space: TC
title: Deployment checklist
author: Damon Asberg
date: '2023-05-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/180781073
explicit_links: []
---
# Deployment checklist

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/180781073  

## Content

## This is a guideline to prevent any mistakes from happening during live deployments.

Please add items to the list if they're missing.

### Before deployment

* Update the version in package.json
* (optional) Update the version number in `config.xml` for Cordova projects

  + Make sure the project name inside the `config.xml` is in 1 single line otherwise the app build will fail.
* Test on Chrome
* Test on Firefox
* Test on Safari
* Test on Edge (is Chromium based so should be very similar to Chrome...)
* (optional) Test on mobile device
* (optional) Check if (backend) environment is set to live
* (optional) Notify clients about update
* (optional) Update the changelog

### After deployment

* Test if application loads
* Check that it's connecting to the right backend
* Move cards to done
* Notify client that deployment is done