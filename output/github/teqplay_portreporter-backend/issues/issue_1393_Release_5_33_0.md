---
id: github:teqplay/portreporter-backend:issue:1393
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1393
title: Release 5.33.0
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1393
labels: []
explicit_links: []
---
# Issue #1393: Release 5.33.0

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1393  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [2c71a78ae89a...a3518942b177](https://github.com/teqplay/portreporter-backend/compare/2c71a78ae89a...a3518942b177)
**Merge commit:** [a3518942b177](https://github.com/teqplay/portreporter-backend/commit/a3518942b177)
**Author:** Shan Minh Nguyen
**Reviewers:** Joaquin Marquez Bugella
**Approvers:** Joaquin Marquez Bugella
**Source Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/portreporter-backend/tree/master)
**Closed On:** 2024-09-23T08:38:32.251905+00:00
**Status:** MERGED

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
* Merged master and updated base version to new snapshot version
* Removed password from requests when creating new user
* Merged in feat/PRP-2413/PRP-2432/create\_admin\_patch\_portcall\_endpoint \(pull request #760\)
    Create admin patch portcall endpoint

    * PRP-2413, PRP-2432 : Enabling portcall patch endpoint for admins to update agent, startTime, endTime and portATA.
    * PRP-2413, PRP-2432 : Setting only PATCH as a valid endpoint's method.
    * PRP-2413, PRP-2432 : send slack message when new agent is not a valid one.
    * PRP-2413, PRP-2432 : logging full change for traceability.
    * PRP-2413, PRP-2432 : change endpoint kdoc description.
    
    Approved-by: Gavin den Hollander

* Merged in feat/PRP-2433/remove\_vopak\_queue\_consumption \(pull request #759\)
    Feat/PRP-2433/remove vopak queue consumption

    * PRP-2433 : Removing Vopak ShippingLine queue consumption.
    * PRP-2433 : remove unused classes and resources.
    * Merged develop into feat/PRP-2433/remove\_vopak\_queue\_consumption
    * PRP-2433 : just correcting changelog.md
    * PRP-2433 : Adding a timeouts to wanted notifySubscribers in RestructureTest cases.
    
    Approved-by: Shan Minh Nguyen

* Merged in feat/sec-35/remove\_authenticator\_credentials\_from\_properties \(pull request #761\)
    SEC-35 : Removing authenticator credentials and url for security reasons.

    * SEC-35 : Removing authenticator credentials and url for security reasons.
    
    Approved-by: Joost Laurman

* CO-2398 : Create a common PrometheusService class to share standarize usage. Detect each metric and send them.
* CO-2398 : \[Format\] incrementMetricsBy calls inline.
* CO-2398 : formatting and adding some kdocs
* PRP-2398 : Renaming prometheus type tag enum values for notification for standardzation purposes.
* PRP-2398 : adding logs when sending metrics.
* PRP-2398 : rename enums and remove unnecessary log.
* PRP-2398 : some code styling in a better shape.
* PRP-2398 : Not using PrometheusService, but directly the metricRegistry.
* PRP-2398 : forgotten comment in changelog.md.
* Allow processing a list of incoming events
* Merged in feature/PRP\_2383\_new\_simple\_health\_client\_implementation\_from\_skeleton \(pull request #762\)
    PRP-2379 Adding the skeleton health actuator, extending it with custom smartfleet & platform implementation and removing the old actuator code

    * removed health actuator in preparation for the skeleton implementation.
    * Emptied authenticator url
    * Updating version number
    * Merged latest develop onto branch
    * Copied and made small tweaks from skeleton health actuator client for PRP clients
    * Reworked timeout check and renamed property of HealthTrackingConnection
    * Removed unused code related to old health actuator implementation and properties removed
    * Reworked property names for clearer understanding
    * Merged feature/PRP\_2383\_new\_simple\_health\_client\_implementation\_from\_skeleton into feature/smartfleet\_temp\_health\_actuator
    * Updated skeleton version with latest bugfix
    * Merged in feature/smartfleet\_temp\_health\_actuator \(pull request #766\)
    
    Copied and made small tweaks from skeleton health actuator client for PRP clients

    Approved-by: Joaquin Marquez Bugella

    Approved-by: Joaquin Marquez Bugella

* Address review feedback
* Updated data sources with latest kmongo from develop
* Fixing default permissions of new keycloak users by config
* Better exception error message
* Fixed a bug where users that already got added to keycloak but not migrated would result in a bad request when requesting anonymously thus exposing sensitive data in the public endpoint
* Added comment for method parameter usage and KTLint
* Added frontend client properties for logout function in case of different client usages with the FE
* Removed keycloak token interceptor
* Updated the Basic Auth to track the health when configured
* Revert "Updated the Basic Auth to track the health when configured \(pull request #768\)"
* Reworked logout do delete all user sessions instead of just per client, removed keycloak service
* Changed warning to info when sending reset password by keycloak
* Merged in feat/PRP-2446/expose\_when\_a\_portcall\_gets\_its\_agent\_set\_from\_null\_to\_a\_non\_null\_value \(pull request #770\)
    Feat/PRP-2446/expose when a portcall gets its agent set from null to a non null value

    * CO-2446 : fix notification metric not being sent.
    * PRP-2446 : report to prometheus when a portcall's agent is set when it was null before.
    * Merge branch 'develop' into feat/PRP-2446/expose\_when\_a\_portcall\_gets\_its\_agent\_set\_from\_null\_to\_a\_non\_null\_value
    * Adding some logs.
    * Revert "Adding some logs."
    
    This reverts commit 9a094ba83c84de1211f427ee0e6f2b02ec0979b0.

    Approved-by: Joost Laurman

* Catching 5xx status codes since it got ignored due to the exception only sending 4xx status codes
* Updated skeleton version and updated SmartFleetEventLogic due to PoMa model update
* Updated unit test due to poma model update
* Added a public endpoint to check user migration status
* Reworked keycloak lazy function
* cors added to security

