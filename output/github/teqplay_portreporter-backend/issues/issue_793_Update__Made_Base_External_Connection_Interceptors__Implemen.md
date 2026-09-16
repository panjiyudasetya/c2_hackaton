---
id: github:teqplay/portreporter-backend:issue:793
source: github
type: issue
repo: teqplay/portreporter-backend
number: 793
title: 'Update: Made Base External Connection/Interceptors. Implemented Simply5 Connection'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/793
labels: []
explicit_links: []
---
# Issue #793: Update: Made Base External Connection/Interceptors. Implemented Simply5 Connection

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/793  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [89f0c19a3f66...00b5ef15d944](https://github.com/teqplay/portreporter-backend/compare/89f0c19a3f66...00b5ef15d944)
**Merge commit:** [00b5ef15d944](https://github.com/teqplay/portreporter-backend/commit/00b5ef15d944)
**Author:** Shravan Shetty
**Reviewers:** Joost Laurman, Michel Wilson, Wouter Naloop
**Approvers:** Wouter Naloop
**Source Branch:** [feat/simply5Integration](https://github.com/teqplay/portreporter-backend/tree/feat/simply5Integration)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2020-09-08T11:50:14.480047+00:00
**Status:** MERGED

* use wsimport to generate classes for Simply5
* forward all events to simply5 if there is a nomination for it
* the use of the latest version of wsimport plugin needed jdk 11
* upped the circleci docker image


