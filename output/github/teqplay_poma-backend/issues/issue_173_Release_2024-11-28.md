---
id: github:teqplay/poma-backend:issue:173
source: github
type: issue
repo: teqplay/poma-backend
number: 173
title: Release 2024-11-28
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/173
labels: []
explicit_links: []
---
# Issue #173: Release 2024-11-28

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/173  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [ad2f72e9e12b...308c188184fc](https://github.com/teqplay/poma-backend/compare/ad2f72e9e12b...308c188184fc)
**Merge commit:** [308c188184fc](https://github.com/teqplay/poma-backend/commit/308c188184fc)
**Author:** Darius Wattimena
**Reviewers:** 
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2024-11-28T10:01:05.792987+00:00
**Status:** MERGED

* Port search bounding box uses eos bound when available
* Port search added eosAreaFilter flag
* Added EosAreaService, EOS area and its bounding box are now updated whenever an anchorage, pilot boarding, approach area or break water area gets created or updated, added a fixEosAreas endpoint to update all ports,
* Added forceUpdate to updateEosArea to fix the ports with an existing EOS area
* When constructing a port, take the boundingBox if there's no eos area
* Added EosInfrastructureService and moved the duplicate create and update functions into that
* Added EosAreaServiceTest
* Added liveSyncRestTemplate, added synchronize to the InfrastructureService and -controller, added scheduled to all infrastructures
* Added mock for RestTemplate in tests
* Moved the liveSyncRestTemplate to the body of InfrastructureService
* Only gets and syncs the Teqplay db, then call mergeDatabases to update the merged db,
* Added mergeWOPCron to live sync and removed merge after sync from terminal and berth, due to incompatibility, also added replaceCollection to DataSource for a safe and total replacement
* Modified the eosAreaFilter check
* Re-added checking if live sync is enabled, defaulted live sync to false
* Live-sync enabled now for the complete ability to synchronize, this also prevents an exception when no keycloak credentials are given
* Added the saving of one "\_old" database when replacing a collecting, in case of some accidental sync on prod. If the synchronize endpoint is called twice it's still lost
* Added SyncService and -Controller with ability to synchronize from prod, dev or sandbox and the option to sync everything or a single infrastructure type
* Added synchronizePort\(s\), added PortInfraDataSource and -service as support,
* Added scheduled autoSync to SyncService and removed the scheduled syncing from all infra services
* Restored resolveTimeZone for Port
* Replaced autoMerge bool from InfrastructureService and replaced with try catch in SyncService, removed missed scheduled merge
* Added enum for source, included enum for infrastructure type and added a comment about merging
* Berth and custom area now search for equal to uniqueId instead of regex
* ktlint
* Insert and insertMany are now insert if not exists
* Removed secured from whitelist getAll
* Added synchronizeWhitelist
* Added logging of syncs
* Added a try/catch for a forbidden exception in the synchronizeWhitelist
* Merged in feat/CO-365/add\_displayName\_to\_terminal\_and\_berths \(pull request #145\)
    CO-365 : Set displayName to Terminals and Berths. Also, created 3 endpoints for capitalizing Ports, Terminals and Berths's displayNames.

    * CO-365 : Set displayName to Terminals and Berths. Also, created 3 endpoints for capitalizing Ports, Terminals and Berths's displayNames.
    * Merged develop into feat/CO-365/add\_displayName\_to\_terminal\_and\_berths
    * CO-365 : launch IOScope coroutines with the correct SecurityCoroutineContext.
    * CO-365 : forgot to import SecurityCoroutineContext.
    * CO-365 : Adding start and ending logs.
    * CO-365 : setting empty displayNames for terminals, ports and berths.
    * CO-365 : CapitalizeAllWords should lowercase each individual word and Uppercase only the first character.
    * ktlint
    * CO-365 : rename method names and endpoints.
    * Merged in feat/CO-365/add\_displayName\_to\_terminal\_and\_berths\_with\_security\_context \(pull request #150\)
    
    Feat/CO-365/add displayName to terminal and berths with security context

    Approved-by: Maryam Tavakoli

    Approved-by: Pim van den Toorn

* Sync config to kebab-case, renamed SyncSourceEnum and added documentation
* New package
* Added PortInfraController, so all the port infrastructures have the getByPort\(s\) endpoints for syncing
* Fixed synchronizePorts to request all models for a port instead of updating the known models
* Removed nullability from the prod, dev and sandbox properties/templates
* Moved synchronize whitelist to a separate endpoint
* Added PomaConnection with enabled boolean
* Better naming and documentation
* Moved SyncLogEntry to the models folder
* Renamed whatIsSynced to description
* Added security to the whitelist getAll endpoint
* ktlint
* ktlint
* PortInfraController fix
* Added RestTemplate.get and .post functions
* feat: added support for whitelist field in Port Model
* fix: merge conflicts
* fix
* Added endpoint to check the differences with another database
* feat: add endpoint that support returning whole port model for whitelisted ports
* fix: remove unused services
* fix: merge conflict
* Merged in hotfix/allow\_terminal\_and\_berth\_api\_models\_displayName\_to\_be\_nullable\_clean\_up \(pull request #155\)
    hotfix clean after FE adapt.

    * hotfix clean after FE adapt.
    
    Approved-by: Joost Dambrink

* feat: change source to POMA when importing fix: remove the WOP source from PoMa
* feat: add separate controller for whitelist operations
* Changed: when updating a model, also update source and sourceType instead of ignoring the new version
* Default to only show the difference when syncing, split the difference into port- and portInfraDifferences, added differences for not in local or not in other database
* Prints the source if it's an illegal source
* getAll in the differences now has validated = null to actually get all
* Removed the whitelist syncing, as the whitelist is being integrated into port
* Added comments and changed the boolean onlyDifference to synchronize in the SyncController
* Now deletes local entries on sync if they're not in the response, added name to InfrastructureModel
* ApproachRoute name non-nullable, collection will now be replaced even if the external collection is empty, added uniqueId to ModelDifference
* RequestParam synchronize now non-nullable with default false, fixed difference when local is empty
* Combined differences and sync to not request the models twice from the external source
* Added getByPort functions to DataSource so Ports can be handled the same as the other infrastructure, removing many lines from SyncService
* ktlint
* Fixed logger showing updated and deleted for models that were only deleted
* Added ApiPorts to get ports in ModelDifference
* Merged in DEV-Upgrading-Spring \(pull request #161\)
    DEV Upgrading Spring

    * Upgrading spring
    * editing CI config
    * editing CI config
    * fixed: logback and spring
    * fixed: change skeleton version
    * fixed: update spring security filter
    * fix: moved security chain changes to skeleton plugins
    * chore: ktlint format
    * fix: auth controller autoconfig
    * chore: change version
    * chore: separate spring cloud version from the implementation
    
    Approved-by: Gavin den Hollander

* Berth unknown source string now defaults to Source.UNKNOWN
* Merged in feat/SEC-67/removing\_sensitive\_auth\_information\_from\_logs \(pull request #163\)
    SEC-67 : Upgrading skeleton plug-ins so not to log auth credentials.

    * SEC-67 : Upgrading skeleton plug-ins so not to log auth credentials.
    
* Removed timezone search when converting an api port to a dbmodel port
* Added clarification to the model differences, like when the model is not in the local database
* Added port displayName to ModelDifference
* Changed resetDisplayNames to setEmptyDisplayNames, now only setting names which are empty
* Added \_id to ModelDifference
* Changed getAllPath to controllerPath
* Added getAllDbObjects endpoint to InfrastructureController
* Added ports option to getAllDbObjects
* Changed responseType from ApiModel to Model, changed response to external
* Added syncedAt to all InfrastructureModels
* Changed ApiModel to Model in ModelDifference
* Null to isNullOrEmpty
* Added test getTemplate
* Added test infrastructure- modelDifferences
* Added test synchronizeAll - test all the replaceCollection, the merge and the log
* Added test synchronizeInfrastructure
* Added test synchronizePorts
* Merge fix and changed Port to apiPort and .../basemodel/Port to Port
* Merge fix and changed Port to apiPort and .../basemodel/Port to Port
* Format fix
* modelDifference minor rewrite for clarity \+ some small things
* Clarified the getPortNameAndCode
* syncedAt comment correct format
* Added acceptance as a sync source
* Sync tests fix
* Per model difference checking to a separate function
* Changed acceptance to data
* Filter syncedAt and updatedAt from modelDifferences
* Added \_id filter to modelDifference
* Performance improvements: search model in map instead from list, create list of properties once and pass to function
* Performance improvement: instant return if updatedAt times are same
* Ktlint
* Got rid of an unnecessary warning
* Also changed acceptance to data in the tests
* Made CircleCI changes to include a new environment

