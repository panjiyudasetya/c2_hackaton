---
id: github:teqplay/dataflow_dag_core:pr:727
source: github
type: pull_request
repo: teqplay/dataflow_dag_core
number: 727
title: 'fix(fact-migration): Guard `between_eos_entry_and_pob_duration` backfill against
  GENERATED ALWAYS columns'
author: panjiyudasetya
state: closed
date: '2026-07-22'
merged_at: '2026-07-22'
base_branch: develop
head_branch: fix/generated-column-issue
url: https://github.com/teqplay/dataflow_dag_core/pull/727
labels: []
linked_issues: []
explicit_links: []
---
# PR #727: fix(fact-migration): Guard `between_eos_entry_and_pob_duration` backfill against GENERATED ALWAYS columns

**Repo:** teqplay/dataflow_dag_core  
**URL:** https://github.com/teqplay/dataflow_dag_core/pull/727  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `fix/generated-column-issue`  
**Created:** 2026-07-22  
**Merged:** 2026-07-22  

## Description

### Description
The plain-column UPDATE backfill fails on databases where the column is already `GENERATED ALWAYS AS STORED (attgenerated = 's')`. Wrap it in a DO $$ block that checks `pg_attribute.attgenerated = ''` before executing, so the backfill only runs on databases that still hold the column as a plain double precision.

## Commits

- `35909b8f` **Panji Y. Wiwaha** (2026-07-22): fix(fact-migration): guard between_eos_entry_and_pob_duration backfill against GENERATED ALWAYS columns
  The plain-column UPDATE backfill fails on databases where the column is
  already GENERATED ALWAYS AS STORED (attgenerated = 's'). Wrap it in a
  DO $$ block that checks pg_attribute.attgenerated = '' before executing,
  so the backfill only runs on databases that still hold the column as a
  plain double precision.

## Reviews

### augmentcode[bot] — COMMENTED (2026-07-22)

Review completed. No suggestions at this time.


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### ryan-kharisma — APPROVED (2026-07-22)

LGTM

## Comments
