---
id: github:teqplay/portreporter-backend:issue:1098
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1098
title: 'Prp-1002 : Improve Vessel Identification For Incoming Scraped Nominations.'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1098
labels: []
explicit_links:
- jira:PRP-1002
---
# Issue #1098: Prp-1002 : Improve Vessel Identification For Incoming Scraped Nominations.

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1098  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [b1749b7f2224...3e5b770cd7b7](https://github.com/teqplay/portreporter-backend/compare/b1749b7f2224...3e5b770cd7b7)
**Merge commit:** [3e5b770cd7b7](https://github.com/teqplay/portreporter-backend/commit/3e5b770cd7b7)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Joost Laurman
**Source Branch:** [PRP-1002/improve_vessel_identification_for_incoming_scraped_nominations](https://github.com/teqplay/portreporter-backend/tree/PRP-1002/improve_vessel_identification_for_incoming_scraped_nominations)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-05-25T10:27:40.149047+00:00
**Status:** MERGED

After Richard’s feedback and some live experiences, I have include:

* Better identification of company by using a regex \(case insensitive\).
* If the scraped nomination does not provide the imo, but ship name is included, try to locate the vessel in the shippingCompany’s fleet.
* Check that IMO is always present in the identified ship.
* Add test cases to unit tests.


