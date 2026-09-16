---
id: github:teqplay/poma-backend:issue:62
source: github
type: issue
repo: teqplay/poma-backend
number: 62
title: Feat/Spv-1520/Mainport
author: jbugella
state: closed
date: '2025-01-13'
url: https://github.com/teqplay/poma-backend/issues/62
labels: []
explicit_links: []
---
# Issue #62: Feat/Spv-1520/Mainport

**Repo:** teqplay/poma-backend  
**URL:** https://github.com/teqplay/poma-backend/issues/62  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-13  
**Closed:** 2025-01-13  

## Description

**Full diff:** [a74d8d1529ea...38b033cd81e4](https://github.com/teqplay/poma-backend/compare/a74d8d1529ea...38b033cd81e4)
**Merge commit:** [38b033cd81e4](https://github.com/teqplay/poma-backend/commit/38b033cd81e4)
**Author:** Wouter Naloop
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/SPV-1520/mainport](https://github.com/teqplay/poma-backend/tree/feat/SPV-1520/mainport)
**Destination Branch:** [develop](https://github.com/teqplay/poma-backend/tree/develop)
**Closed On:** 2023-06-05T05:30:48.219166+00:00
**Status:** MERGED

* SPV-1520: Add mainPort to Port model
* SPV-1520: Remove todo that was already done
* SPV-1520: remove defaulting that isn't supposed to be there, but was there for local testing
* SPV-1520: reverse search for biggest ports as this makes sure the biggest port is always the main port, renamed percentage to blowUpFactor and changed its scaling to allow for more than 100% blowup area size and the option to scale down, use the kotlin IllegalArgument instead of the java one
* SPV-1520: ktlint

