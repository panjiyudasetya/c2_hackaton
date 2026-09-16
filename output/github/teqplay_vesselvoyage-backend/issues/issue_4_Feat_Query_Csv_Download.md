---
id: github:teqplay/vesselvoyage-backend:issue:4
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 4
title: Feat/Query Csv Download
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/4
labels: []
explicit_links: []
---
# Issue #4: Feat/Query Csv Download

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/4  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [645e54750490...8324e95d2c9f](https://github.com/teqplay/vesselvoyage-backend/compare/645e54750490...8324e95d2c9f)
**Merge commit:** [8324e95d2c9f](https://github.com/teqplay/vesselvoyage-backend/commit/8324e95d2c9f)
**Author:** Jos de Jong
**Reviewers:** 
**Approvers:** Former user
**Source Branch:** [feat/query_csv_download](https://github.com/teqplay/vesselvoyage-backend/tree/feat/query_csv_download)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2021-07-14T10:06:09.055772+00:00
**Status:** MERGED

Implement endpoints to download visit/voyage query results as CSV. 

Currently the exported data does not contain _all_ the information that is available: for example every visit contains a list with anchorages and port areas each having their own start/end time, ids, etc. Currently a simple, flat export is done where every visit/voyage is one row, and multiple ports are summarized as a comma separated list in a single cell.

