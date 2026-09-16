---
id: github:teqplay/csi-backend:issue:15
source: github
type: issue
repo: teqplay/csi-backend
number: 15
title: Add Ghost Ship Metadata Support
author: jbugella
state: closed
date: '2025-01-07'
url: https://github.com/teqplay/csi-backend/issues/15
labels: []
explicit_links: []
---
# Issue #15: Add Ghost Ship Metadata Support

**Repo:** teqplay/csi-backend  
**URL:** https://github.com/teqplay/csi-backend/issues/15  
**State:** closed | **Author:** jbugella  
**Created:** 2025-01-07  
**Closed:** 2025-01-07  

## Description

**Full diff:** [0cfea63d371a...bdb1503c22c7](https://github.com/teqplay/csi-backend/compare/0cfea63d371a...bdb1503c22c7)
**Merge commit:** [bdb1503c22c7](https://github.com/teqplay/csi-backend/commit/bdb1503c22c7)
**Author:** Former user
**Reviewers:** Michel Wilson
**Approvers:** Michel Wilson
**Source Branch:** [metadata-ghost-ship](https://github.com/teqplay/csi-backend/tree/metadata-ghost-ship)
**Destination Branch:** [automatic-ticket-creation](https://github.com/teqplay/csi-backend/tree/automatic-ticket-creation)
**Closed On:** 2019-11-25T08:03:30.266224+00:00
**Status:** MERGED

Added a ghost ship flag to a ship’s metadata. Also wrote a migration script which can relocate the separate `disabled` and `disabledTime` fields into one `metadata` field which also contains the ghost ship flag.

