---
id: github:teqplay/vesselvoyage-backend:issue:51
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 51
title: Spv-541 Draught Support
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/51
labels: []
explicit_links: []
---
# Issue #51: Spv-541 Draught Support

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/51  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [b62b761d0a94...29c2c5ad033c](https://github.com/teqplay/vesselvoyage-backend/compare/b62b761d0a94...29c2c5ad033c)
**Merge commit:** [29c2c5ad033c](https://github.com/teqplay/vesselvoyage-backend/commit/29c2c5ad033c)
**Author:** Darius Wattimena
**Reviewers:** Jos de Jong
**Approvers:** Jos de Jong
**Source Branch:** [SPV-541_draught-support](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-541_draught-support)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-01T13:13:34.783880+00:00
**Status:** MERGED

It was a bit more painful to finish up the database migration part as adding a field to all items of an array which is an object, is rather annoying with kmongo.  
  
I suppose I did learn that you can call `$[]` to select all available items in an array!

