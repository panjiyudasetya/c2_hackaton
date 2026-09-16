---
id: github:teqplay/portreporter-backend:issue:986
source: github
type: issue
repo: teqplay/portreporter-backend
number: 986
title: Prp-189 Changelog Multipartfile Management
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/986
labels: []
explicit_links: []
---
# Issue #986: Prp-189 Changelog Multipartfile Management

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/986  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [addb4e9aaa5d...1fe573da62b9](https://github.com/teqplay/portreporter-backend/compare/addb4e9aaa5d...1fe573da62b9)
**Merge commit:** [1fe573da62b9](https://github.com/teqplay/portreporter-backend/commit/1fe573da62b9)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Wouter Naloop
**Approvers:** Wouter Naloop, Former user
**Source Branch:** [PRP-189_Changelog_multipartFile_management](https://github.com/teqplay/portreporter-backend/tree/PRP-189_Changelog_multipartFile_management)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2024-08-26T07:49:39.138858+00:00
**Status:** MERGED

This PR consist of the following points:
* Modification of the Create Endpoint to accept multipart files to create them in the S3 bucket.
* Delete files when a a changelogEntry is deleted.
* Cancellation of the update operation, as agreed on the task discussion.
Note that this is liable to be modified according to the FrontEnd capabilities related to the multipart form.
**Update:**
* Indeed a new modification was required as the create endpoint didn’t work properly with multipart files \(even though I followed Spring standards and guides\).
* Jackson gradle dependencies don’t depend on the S3 dependencies. 
* S3 bucket access has been polished.

