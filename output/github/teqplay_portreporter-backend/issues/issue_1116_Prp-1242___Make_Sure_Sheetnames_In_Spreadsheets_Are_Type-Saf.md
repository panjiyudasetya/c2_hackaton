---
id: github:teqplay/portreporter-backend:issue:1116
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1116
title: 'Prp-1242 : Make Sure Sheetnames In Spreadsheets Are Type-Safe (No Invalid
  Characters)'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1116
labels: []
explicit_links: []
---
# Issue #1116: Prp-1242 : Make Sure Sheetnames In Spreadsheets Are Type-Safe (No Invalid Characters)

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1116  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [ba9a21ddeeb2...bc6f334468ec](https://github.com/teqplay/portreporter-backend/compare/ba9a21ddeeb2...bc6f334468ec)
**Merge commit:** [bc6f334468ec](https://github.com/teqplay/portreporter-backend/commit/bc6f334468ec)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Darius Wattimena
**Approvers:** Joost Laurman
**Source Branch:** [fix/PRP-1242/spreadsheet_safe_sheetnames](https://github.com/teqplay/portreporter-backend/tree/fix/PRP-1242/spreadsheet_safe_sheetnames)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-06-27T11:07:21.987459+00:00
**Status:** MERGED

I just found out that POI library is not very good at sheet names: there are forbidden characters.
I’ve here made some changes, which extend also to other spreadsheet exports.

