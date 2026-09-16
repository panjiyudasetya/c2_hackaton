---
id: jira:TCC-82
source: jira
type: issue
key: TCC-82
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Unassigned
labels: []
components: []
title: Bucketing in AisEngine doesn't close streams correctly
author: Darius Wattimena
status: To Do
date: '2024-08-19'
url: https://teqplaybv.atlassian.net/browse/TCC-82
explicit_links: []
---
# [TCC-82] Bucketing in AisEngine doesn't close streams correctly

**URL:** https://teqplaybv.atlassian.net/browse/TCC-82  
**Type:** Bug | **Status:** To Do | **Priority:** Medium  
**Reporter:** Darius Wattimena | **Assignee:** Unassigned  
**Created:** 2024-08-19 | **Updated:** 2025-05-22  
**Board:** TCC board  

## Description

Currently streams are closed only in the happy flow. If for instance an input or output stream is used but an exception is thrown, then it will result in the stream to be never closed.

Adding a simple try-finally patterning for every place where we use streams should fix this issues.

There are two options to do this:

{noformat}val inputStream = bytes.inputStream()
try {
  // The things we currently do with the stream
} finally {
  inputStream.close()
}{noformat}

or use the Kotlin helper functionality, which I find rather confusing to use:

{noformat}val inputStream = bytes.inputStream()
inputStream.use {
  // The things we currently do with the stream
}{noformat}

NOTE: with the last approach you don’t have to call close.
