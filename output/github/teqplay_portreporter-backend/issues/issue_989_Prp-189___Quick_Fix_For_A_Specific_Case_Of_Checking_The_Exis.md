---
id: github:teqplay/portreporter-backend:issue:989
source: github
type: issue
repo: teqplay/portreporter-backend
number: 989
title: 'Prp-189 : Quick Fix For A Specific Case Of Checking The Existence Of Files
  When Using Bucket Policies Instead Of Acls'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/989
labels: []
explicit_links: []
---
# Issue #989: Prp-189 : Quick Fix For A Specific Case Of Checking The Existence Of Files When Using Bucket Policies Instead Of Acls

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/989  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [1fe573da62b9...88ee16697ae6](https://github.com/teqplay/portreporter-backend/compare/1fe573da62b9...88ee16697ae6)
**Merge commit:** [88ee16697ae6](https://github.com/teqplay/portreporter-backend/commit/88ee16697ae6)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Michel Wilson, Wouter Naloop
**Approvers:** Michel Wilson
**Source Branch:** [PRP-189_S3_File_existence_fix_when_using_policies](https://github.com/teqplay/portreporter-backend/tree/PRP-189_S3_File_existence_fix_when_using_policies)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2021-11-19T08:30:53.127607+00:00
**Status:** MERGED

I am using Bucket policies for accessing S3 buckets, which is the right thing, instead of ACL based on personal AWS accounts. Definitely the right thing to do.  
However, checking the existence of a file throws an exception when the file doesn’t exist \(note this doesn’t happen when using ACLs, I’ve checked that\).  
My guess is that no policy can be applied to any object that doesn’t exist, throwing the exception by AWS.

So, in the case of using bucket policies, when a file doesn’t exist, the use of `s3client.doesObjectExist(bucket, key)` throws an exception instead of returning false \(weird! eh?\).


