---
id: github:teqplay/vesselvoyage-backend:issue:53
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 53
title: Smartly Regenerate Traces Only When They Are Outdated
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/53
labels: []
explicit_links: []
---
# Issue #53: Smartly Regenerate Traces Only When They Are Outdated

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/53  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [3c5945bf38a4...97461b2a13fb](https://github.com/teqplay/vesselvoyage-backend/compare/3c5945bf38a4...97461b2a13fb)
**Merge commit:** [97461b2a13fb](https://github.com/teqplay/vesselvoyage-backend/commit/97461b2a13fb)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/keep_unchanged_traces](https://github.com/teqplay/vesselvoyage-backend/tree/feat/keep_unchanged_traces)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-02-07T10:48:51.444138+00:00
**Status:** MERGED

* Smartly regenerate traces only when they are outdated when recalculating a ship’s story. A trace is outdated when:
    * no matching trace for an entry
    * the matching trace has differing startTime or endTime
    * the version number of the trace is outdated
    * parameter `forceRegenerateTraces=true`
    
* Enable recalculating multiple ships in parallel in the RecalculationService \(`@Async`\)
The new `HistoricTrace.version` property is a breaking change, but it turns out Jackson automatically fills in `0` when this field is missing in Mongo. That saves us a migration of all traces \(35 GB\) :sweat_smile: .


