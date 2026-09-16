---
id: github:teqplay/poma-backend:issue:40
source: github
type: issue
repo: teqplay/poma-backend
number: 40
title: Pra-171 Validated/Updated Since Endpoint
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/40
labels: []
explicit_links: []
---
# Issue #40: Pra-171 Validated/Updated Since Endpoint

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/40  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [f817cf1bb437...9a21bb24bcc7](https://github.com/teqplay/poma-backend/compare/f817cf1bb437...9a21bb24bcc7)
**Merge commit:** [9a21bb24bcc7](https://github.com/teqplay/poma-backend/commit/9a21bb24bcc7)
**Author:** Former user
**Reviewers:** Michel Wilson, Wouter Naloop, Darius Wattimena
**Approvers:** Wouter Naloop, Darius Wattimena
**Source Branch:** [PRA-171-validated/updated-since-endpoint](https://github.com/teqplay/poma-backend/tree/PRA-171-validated/updated-since-endpoint)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2022-10-10T12:01:07.356444+00:00
**Status:** MERGED

* Move /bulk endpoint into InfrastructureController

    * Noticed this is used to get an endpoint in all controllers, so removed the duplicated code.
    
* Add endpoint to request all validated & updated infra since a given time

The area-monitor will use this endpoint for every area type \(ports, berths, etc.\) to request all areas that are validated and updated since a given time. That way the area-monitor can update specifically those areas that have been updated recently.

