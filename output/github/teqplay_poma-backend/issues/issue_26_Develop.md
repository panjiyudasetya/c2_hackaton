---
id: github:teqplay/poma-backend:issue:26
source: github
type: issue
repo: teqplay/poma-backend
number: 26
title: Develop
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/26
labels: []
explicit_links: []
---
# Issue #26: Develop

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/26  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [291991e7a9e5...71d0a34931d4](https://github.com/teqplay/poma-backend/compare/291991e7a9e5...71d0a34931d4)
**Merge commit:** [71d0a34931d4](https://github.com/teqplay/poma-backend/commit/71d0a34931d4)
**Author:** Wouter Naloop
**Reviewers:** Darius Wattimena
**Approvers:** 
**Source Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Destination Branch:** [master](https://github.com/teqplay/poma-backend/tree/master)
**Closed On:** 2022-02-01T14:32:22.852929+00:00
**Status:** MERGED

* rearranging into a feature based approach, generify Model, Apimodel and Service and only use those as references in the rest of the code

* README.md edited online with Bitbucket

* README.md edited online with Bitbucket

* PR feedback

* Adds support for KeyCloak authentication

* only return validated models by default

* make sure on onlyvalidated null it returns everything

* make sure on onlyvalidated null it returns everything, part 2

* Updated realm and audience of keycloak to their new defaults

* Added a count method for every model to fetch how many valided / not validated items are of each model type

* change onlyValidated to validated, PR feedback

* fix failed build

* provided an endpoint to set the validatedByUser field in objects

* reformat code

* fix weird 2 different types of filtering to be combined

* Started implementing parsing of the terminal entities from gisis

* Corrected location coordinates

* Renamed decimal degrees converter function

* Made last changes to import to be able to import the new terminals

* Removed the master/develop filter on the circleci script to allow deploying feature branches

* Moved the terminal entities to their own feature package, saving them in a seperate collection for now

* Removed unneeded import

* Split up TerminalEntityService feedback

* Added documentation on the TerminalEntity class explaining why this isn't the same as a Terminal

* tryout having the ssl certificate loaded in via s3

* Added swagger from the skeleton plugins, Added hbr import every morning at 8:55

* removed old swagger dependencies

* Pullrequest feedback

* add the validated query param for the port specific query

* fix order of the parameters in the portcount

* fix pr feedback, made sure we fetch all berths 1000 at a time, correct the names of the HbrBerth and supply their naming as alias

* fix merge conflict

* add comments, fix that the health endpoint will report up again, fix that also the last page of hbr results is parsed

* add logging to the hbr import

* put back not working version upgrades

* downgrade junit

* readd keycloak

* add the newest zabbix script

* fix logging

* use tomcat instead of tomcat8

* revert logback change and logs config change, changed tomcat8 to tomcat

* attempt 10 or so, to fix logging in poma

* stop using flux with coroutines, add query params to the hbr call the right way

* allow the sets to be null in hbr

* Make sure hbr berths have the right json alias, set the max mem for webclient

* add missing function type, make sure the bulk create or update does not contain duplicates

* make more explicit that the associateBy was to deduplicate

* disable hbr import by default

* zabbix rename env

