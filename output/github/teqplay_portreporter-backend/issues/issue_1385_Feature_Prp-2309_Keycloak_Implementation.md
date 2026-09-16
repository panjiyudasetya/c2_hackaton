---
id: github:teqplay/portreporter-backend:issue:1385
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1385
title: Feature/Prp-2309 Keycloak Implementation
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1385
labels: []
explicit_links: []
---
# Issue #1385: Feature/Prp-2309 Keycloak Implementation

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1385  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [244bcf8fbe1e...a6c8c8fa45eb](https://github.com/teqplay/portreporter-backend/compare/244bcf8fbe1e...a6c8c8fa45eb)
**Merge commit:** [a6c8c8fa45eb](https://github.com/teqplay/portreporter-backend/commit/a6c8c8fa45eb)
**Author:** Shan Minh Nguyen
**Reviewers:** Darius Wattimena, Joaquin Marquez Bugella
**Approvers:** Darius Wattimena
**Source Branch:** [feature/PRP-2309_login_with_keycloak](https://github.com/teqplay/portreporter-backend/tree/feature/PRP-2309_login_with_keycloak)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-09-16T07:41:26.777222+00:00
**Status:** MERGED

This is the implementation / migration code for users going from Authenticator to Keycloak and all related Authenticator code updated with KeyCloak.  
Existing users can migrate by logging in with their Authentication details so that the system can migrate them to Keycloak.  
This can also be done by an Admin after logging in for other users.  
* Updated models, config and changed login with Authenticator and sessionManager to work with Keycloak access token.
* Removed unused code and updated gradle build.
* Updated skeleton plugin version
* Added extra logging in case Keycloak fails
* Disabled and/or replaced Authenticator functions with Keycloak functions.
* disabled some classes
* Remove unused code
* Reverting and modified some changes to set cors headers
* Changed error code when trying to login through old way
* changed error code response when authenticating fails to old login to 400 bad request
* Removed unused/commented code and updated keycloak login endpoint with a fetch profile to return a more detailed response
* Updated password reset via Keycloak and changed endpoint to public so that password reset via Keycloak works.
* Updated code to allow bean overriding due to conflicts with class WebSecurityConfigurerAdapter from base skeleton plugin and updated logout through keycloak as well
* Added logging line to check if user is calling keycloak endpoint to logout
* Changed config and added custom baseService for keycloak
* Changed some names from feedback
* Removed password from requests when creating new user
* Updated data sources with latest kmongo from develop
* Fixing default permissions of new keycloak users by config

