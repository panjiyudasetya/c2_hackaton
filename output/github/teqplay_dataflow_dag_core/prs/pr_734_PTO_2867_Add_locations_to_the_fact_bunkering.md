---
id: github:teqplay/dataflow_dag_core:pr:734
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 734
title: PTO 2867 Add locations to the fact bunkering
author: ryan-kharisma
state: closed
date: '2026-08-05'
merged_at: '2026-08-07'
base_branch: develop
head_branch: PTO-2867_Add_Location_In_Fact_Bunkering
url: https://github.com/teqplay/dataflow_dag_core/pull/734
labels: []
linked_issues: []
explicit_links: []
---
# PR #734: PTO 2867 Add locations to the fact bunkering

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/734  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `develop` ← `PTO-2867_Add_Location_In_Fact_Bunkering`  
**Created:** 2026-08-05  
**Merged:** 2026-08-07  

## Description

**Add locations to the fact bunkering**

Introduce new fields for location latitude and longitude in the `fact_bunkering` table:
- start_location_lat
- start_location_lon
- end_location_lat
- end_location_lon

source table from `ods_encounter`.

## Commits

- `4e209051` **ryan_at_teqplay** (2026-08-05): add locations to the fact bunkering
- `18388938` **ryan_at_teqplay** (2026-08-07): add new location columns to merge delta to fact sql
- `b4be18b8` **ryan_at_teqplay** (2026-08-07): add location to fdw proceed sql

## Reviews

### augmentcode[bot] — COMMENTED (2026-08-05)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_dag_core%2Fpull%2F734%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-08-06)

_No comment._

### ryan-kharisma — COMMENTED (2026-08-07)

_No comment._

### ryan-kharisma — COMMENTED (2026-08-07)

_No comment._

### panjiyudasetya — APPROVED (2026-08-07)

LGTM 👍

## Review Comments

### panjiyudasetya — 2026-08-06 on `teqplay/templates/sql/dml/fact/bunkering/proceed_delta.sql`

I think this feedback is valid. Please consider to address this, @ryan-kharisma 

### ryan-kharisma — 2026-08-07 on `teqplay/templates/sql/dml/fact/bunkering/proceed_delta.sql`

okay sure, Already addressed on this commit : 18388938f4b6536d356bbaa86ba97dd95381784d

### ryan-kharisma — 2026-08-07 on `teqplay/templates/sql/dml/fact/bunkering/proceed.sql`

okay already addressed on this commit : b4be18b8f1a3181bc6f34b2833f336e9cd4cd0d7

## Comments
