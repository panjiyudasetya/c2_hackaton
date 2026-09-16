---
id: github:teqplay/vesselvoyage-backend:issue:227
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 227
title: 'Fix: Esof Of Visit Must Be Deleted When Resuming Voyage'
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/227
labels: []
explicit_links:
- jira:SPV-2114
---
# Issue #227: Fix: Esof Of Visit Must Be Deleted When Resuming Voyage

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/227  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [791620030290...a2953165c1d5](https://github.com/teqplay/vesselvoyage-backend/compare/791620030290...a2953165c1d5)
**Merge commit:** [a2953165c1d5](https://github.com/teqplay/vesselvoyage-backend/commit/a2953165c1d5)
**Author:** Former user
**Reviewers:** Leon Joosse, Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [SPV-2114-fix-duplicate-esof-v2-insertion](https://github.com/teqplay/vesselvoyage-backend/tree/SPV-2114-fix-duplicate-esof-v2-insertion)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2024-05-03T07:29:47.938968+00:00
**Status:** MERGED

When enabling the new V2 definitions there would be the following Mongo exception:
```
com.mongodb.MongoWriteException: Write operation error on server vesselvoyage-dev-mongodb.voyage.svc.cluster.local:27017. Write error: WriteError{code=11000, message='E11000 duplicate key error collection: vesselvoyage.esofV2 index: _id_ dup key: { _id: "761e832e-6327-4115-953e-c10da98558ba.VISIT" }', details={}}.
2024-04-24 14:11:24,457 ERROR [pool-6-thread-1] i.n.c.i.ErrorListenerLoggerImpl: exceptionOccurred, Connection: 415, Exception: com.mongodb.MongoWriteException: Write operation error on server vesselvoyage-dev-mongodb.voyage.svc.cluster.local:27017. Write error: WriteError{code=11000, message='E11000 duplicate key error collection: vesselvoyage.esofV2 index: _id_ dup key: { _id: "761e832e-6327-4115-953e-c10da98558ba.VISIT" }', details={}}.
	at com.mongodb.client.internal.MongoCollectionImpl.executeSingleWriteRequest(MongoCollectionImpl.java:1093)
	at com.mongodb.client.internal.MongoCollectionImpl.executeInsertOne(MongoCollectionImpl.java:478)
	at com.mongodb.client.internal.MongoCollectionImpl.insertOne(MongoCollectionImpl.java:461)
	at com.mongodb.kotlin.client.MongoCollection.insertOne(MongoCollection.kt:516)
	at com.mongodb.kotlin.client.MongoCollection.insertOne$default(MongoCollection.kt:515)
...
```
It had to do with a visit that was deleted due to resuming a voyage, but the ESoF of the visit not being deleted.

