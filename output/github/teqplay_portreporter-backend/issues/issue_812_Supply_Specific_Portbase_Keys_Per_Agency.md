---
id: github:teqplay/portreporter-backend:issue:812
source: github
type: issue
repo: teqplay/portreporter-backend
number: 812
title: Supply Specific Portbase Keys Per Agency
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/812
labels: []
explicit_links: []
---
# Issue #812: Supply Specific Portbase Keys Per Agency

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/812  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [cf6927684b84...9da7f8b64776](https://github.com/teqplay/portreporter-backend/compare/cf6927684b84...9da7f8b64776)
**Merge commit:** [9da7f8b64776](https://github.com/teqplay/portreporter-backend/commit/9da7f8b64776)
**Author:** Former user
**Reviewers:** Shravan Shetty
**Approvers:** Shravan Shetty
**Source Branch:** [portbase-token-rotation](https://github.com/teqplay/portreporter-backend/tree/portbase-token-rotation)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2020-10-16T11:11:18.049679+00:00
**Status:** MERGED

Addon features can now have extra details that are stored in a new db collection, named `addonFeatures`. For portbase orders specifically it can store the access keys per company.

And removed the settings in the config for the Portbase keys.

