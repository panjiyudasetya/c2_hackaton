---
id: github:teqplay/portreporter-backend:issue:982
source: github
type: issue
repo: teqplay/portreporter-backend
number: 982
title: 'Prp-299 : Changeloginfo''S Backend Enhancements'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/982
labels: []
explicit_links: []
---
# Issue #982: Prp-299 : Changeloginfo'S Backend Enhancements

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/982  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b4cb8862d23b...4c4fc9cb892d](https://github.com/teqplay/portreporter-backend/compare/b4cb8862d23b...4c4fc9cb892d)
**Merge commit:** [4c4fc9cb892d](https://github.com/teqplay/portreporter-backend/commit/4c4fc9cb892d)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Former user
**Source Branch:** [PRP-299_Changeloginfo_backend_enhancements](https://github.com/teqplay/portreporter-backend/tree/PRP-299_Changeloginfo_backend_enhancements)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-11-08T15:20:01.830152+00:00
**Status:** MERGED

* Get endpoints filter the content based on the currently logged in user's roles. Impersonation is being taken into account by the parameter email.
* Addition of batch control parameters for the GET's batch entrypoints
* Adding an optional parameter for the endpoint /v1/changelog/all to retrieve entries above a given version


