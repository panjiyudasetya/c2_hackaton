---
id: confluence:176259073
source: confluence
type: page
space: TC
title: Splitting Chorus and Fuelboss back-end
author: Leon Joosse (Unlicensed)
date: '2023-04-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/176259073
explicit_links:
- jira:CHOR-123
- jira:FLB-123
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/176259073
---
# Splitting Chorus and Fuelboss back-end

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/176259073  

## Content

We decided to split the Chorus / Fuelboss back-end into two separate projects, with a shared module. The shared module contains, for example, the LNG composition calculations.

This document outlines which steps we need to take. An hourly estimation is included at the end.

# Project and Git repository separation

There are 2 options: separate repositories (chorus, fuelboss, shared) or a mono-repo with 3 modules (chorus, fuelboss, shared).

## Separate repositories

The current bunkerplanner repo is copied to the chorus and fuelboss projects, a third shared project is created. Every project has its own git repository. Chorus and Fuelboss depend on the shared project using a regular Gradle dependency.

Code from the shared project is build into an artifact where chorus and fuelboss repos depend on. Using snapshot builds with a local maven repository allows for local development.

Tests are run separately in each project. The shared project tests run before it’s build into an artifact.

Building artifacts for a release is straightforward. The code from the shared project is included using a dependency. Once the to-be-released branch is pushed to Bitbucket, we use the regular hold-deploy steps to deploy to the relevant server.

All projects have their own version numbering.

**Pros**:

1. There is full separation of code, git branches, tests, build artifacts and version numbering.

**Cons**:

1. Developing in the shared project is slow: every change results in a new build artifact before it can be used in the chorus/fuelboss project. Building the artifact and refreshing the chorus/fuelboss project takes easily 1 minute per change.
2. If something changes in the shared project for Chorus, and there is no Fuelboss test covering it, you won’t know if it breaks Fuelboss project. You’d have to execute the tests in the Fuelboss project separately. This loose coupling is not ideal, you’re not easily aware if the other project breaks.

## Mono-repo

The current bunkerplanner repo is changed to have modules for chorus, fuelboss and ‘shared’. The Chorus/Fuelboss projects include the shared module via Gradle directly (no intermediate build artifact needed).

Chorus and Fuelboss modules depend on the shared code via a Gradle module. The code is included without intermediate artifact (as with fully separate repos). A change in the shared module makes Gradle/IntelliJ compile both Chorus and Fuelboss modules, you’ll know immediately if it breaks something.

Tests can run independent for Chorus and Fuelboss, but both should also execute the shared module tests.

Branches master and develop will be shared. That should not bite between Chorus and Fuelboss modules, because both projects do not depend on each other. It does require the code of all modules to compile without errors (one never should push non-compiling code to bitbucket anyway, so that’s no problem).   
When Chorus, for example, wants to have a release, the develop branch is merged to master. The Chorus build artifact can then be created. This also means that code from the Fuelboss module is merged to master, that code may not be ready yet to release. The release is intended for Chorus, so only the Chorus artifact should be created. As the Fuelboss artifact is not created, it cannot be released.  
Branch names can collide, but we’re using prefixes from the Jira board (CHOR-123, FLB-123), so that should not be a problem.

Version numbering is shared between Chorus and Fuelboss, as it is now.

**Pros**:

1. Any code breaking change (method removal, signature change) in the shared module reflects immediately in the Chorus/Fuelboss module. You’ll be aware immediately, because the project won’t compile anymore
2. When developing in the shared module, code is immediately available in the Chorus/Fuelboss modules: there’s no need to build an artifact of the shared module first

**Cons**:

1. One project merging to master may pull non-production ready code of the other project to master. This is not an issue if we only create an artifact for the project that intends to release, but we need to pay attention to it

## Conclusion

The mono-repo gives the advantage of knowing immediately when you break something for the other project. And gives the option to easily share security updates / patches.

There is no consensus on how to do branching yet, but that can be taken as a separate step.

# Splitting the project

1. Get Chorus up-to-date with Fuelboss code + testing [40]

   1. Merge branch ‘develop-shell’ into ‘develop’ (watch out for breaking changes)
   2. Test develop branch on Chorus (possibly copy production data to dev, then test it with notifications turned off)
2. Make a ‘mono-repo’ of the current project, set-up the modules [8]

   1. ‘chorus’                             copy from module main
   2. ‘chorus-test’                      copy from module test
   3. ‘chorus-intest’                   copy from module intest
   4. ‘fuelboss’                           copy from module main
   5. ‘fuelboss-test’                   copy from module test
   6. ‘fuelboss-intest’                copy from module intest
3. Set-up the shared module [4]

   1. Create module ‘shared’, ‘shared-test’ and ‘shared-intest’
   2. Code will find its way into these modules once we move it from chorus or fuelboss to shared
4. Change remaining gradle tasks, clean up root build.gradle [4]
5. Change CircleCI scripts to facilitate deployments [8]
6. Deploy Chorus and Fuelboss and do a quick test (negotiation, emails, signing) [8]

# Candidates for the shared library

Candidates for full sharing, requiring no abstraction. These can be copy/pasted without change, to the shared module. [8]

1. LNGComputationService + util classes
2. Locations (controller, service, data source, model)
3. LogoDatasource
4. SettingsService + SettingsDatasource + UserSettingsDatasource
5. SignRequestForm

Candidates for full sharing, requiring a bit of abstraction. These contain a lot of shareable code, but need a bit of abstraction to make it work [80] (incl testing)

1. Bunker ship (controller, service, data source, model) [16]
2. Company (service, data source, model) [16]  
   (methods handling permission knowledge should be kept in project-specific module)
3. Documents (controller, service, data source, model) [16]
4. NotificationService (depends a bit on refactor) [16]
5. Receiving ship (controller, service, data source, model) [16]

# Clean-up [24]

Removing Chorus specific stuff from Fuelboss and vice-versa. Some classes need to be removed (listed below), as well as permission specifics.

## Remove from Chorus [12]

1. BIExport
2. BunkerDeliveryData (controller + data source)
3. Charter / owner functions
4. DnvIntegrationController
5. EbdnImportService
6. EmailLogController
7. Permission specifics
8. Pipeline (controller, data source, model)
9. SpotEnquiry (controller, service, data source, model)
10. TokenController
11. ZipConversionService

## Remove from Fuelboss [12]

1. Actions (controller, data source, model)
2. Auth0 service
3. Comments (controller, data source, model)
4. DeliveryPlan (controller, service, data source, model)
5. ExportController + ExcelExportService
6. IAPHController (was replaced by SafetyChecklistController)
7. LoadingFacility (controller, data source, model)
8. MRF (controller, service, data source, model)
9. NOR (controller, service, data source, model)
10. PositionReport (controller, service, data source, model)
11. Permission specifics
12. QualityReport (controller, service, data source, model)
13. Sandbox (controller, data source, from /v1/prompt/\* urls)
14. Tasks (controller, data source, model)
15. VoyageOrders (controller, service, data source, model)

# Estimation

| **Task** | **Estimated hours** |
| --- | --- |
| Splitting the project into mono-repo \* | 72 |
| Move code to shared module (no modifications to code needed) | 8 |
| Move code to shared library (slight modifications needed) | 80 |
| Clean-up (remove Chorus specifics from Fuelboss, vice-versa) | 24 |

\* Another option is 3 separate repositories. This requires the same amount of hours.