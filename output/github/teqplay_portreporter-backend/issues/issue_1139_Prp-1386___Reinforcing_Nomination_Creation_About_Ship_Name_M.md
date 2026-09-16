---
id: github:teqplay/portreporter-backend:issue:1139
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1139
title: 'Prp-1386 : Reinforcing Nomination Creation About Ship Name Matching (Case
  Insensitive And Considering Prefixes).'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1139
labels: []
explicit_links: []
---
# Issue #1139: Prp-1386 : Reinforcing Nomination Creation About Ship Name Matching (Case Insensitive And Considering Prefixes).

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1139  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [cd215112359c...969aadfa2e3a](https://github.com/teqplay/portreporter-backend/compare/cd215112359c...969aadfa2e3a)
**Merge commit:** [969aadfa2e3a](https://github.com/teqplay/portreporter-backend/commit/969aadfa2e3a)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Berend
**Approvers:** Berend
**Source Branch:** [feat/PRP-1386/enhance_ship_matching_in_nomination_message_handling](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-1386/enhance_ship_matching_in_nomination_message_handling)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-08-04T13:12:40.291560+00:00
**Status:** MERGED

A bit more extended than yours, but I wanted to consider a list of prefixes \(not just one\) in preparation for future.
Additionally, I also realized that the unitTests for the nomination message handling were not mocking the config object, so I fixed that.
**Update:** I took the chance in this ticket to add a change in the slack message for timecharter’s updates.

