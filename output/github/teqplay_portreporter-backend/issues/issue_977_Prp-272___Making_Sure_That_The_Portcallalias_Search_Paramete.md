---
id: github:teqplay/portreporter-backend:issue:977
source: github
type: issue
repo: teqplay/portreporter-backend
number: 977
title: 'Prp-272 : Making Sure That The Portcallalias Search Parameter Is Safe-Checked
  For Regex'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/977
labels: []
explicit_links: []
---
# Issue #977: Prp-272 : Making Sure That The Portcallalias Search Parameter Is Safe-Checked For Regex

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/977  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [de8a1c454e4a...dd2eeb047825](https://github.com/teqplay/portreporter-backend/compare/de8a1c454e4a...dd2eeb047825)
**Merge commit:** [dd2eeb047825](https://github.com/teqplay/portreporter-backend/commit/dd2eeb047825)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Former user
**Source Branch:** [PRP-272_Safe-check_PortcallAliases_search](https://github.com/teqplay/portreporter-backend/tree/PRP-272_Safe-check_PortcallAliases_search)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-11-02T10:20:01.224116+00:00
**Status:** MERGED

Just making sure that the search for PortCallAliases safely uses the searchPattern in the context of regex.

Also, correcting the treatment of the char ‘\\', which was just removed instead of quoted '\\\\’

