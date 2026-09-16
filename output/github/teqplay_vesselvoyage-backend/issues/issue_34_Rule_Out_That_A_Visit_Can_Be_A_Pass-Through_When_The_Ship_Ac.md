---
id: github:teqplay/vesselvoyage-backend:issue:34
source: github
type: issue
repo: teqplay/vesselvoyage-backend
number: 34
title: Rule Out That A Visit Can Be A Pass-Through When The Ship Actually Stopped
author: jbugella
state: closed
date: '2024-12-20'
url: https://github.com/teqplay/vesselvoyage-backend/issues/34
labels: []
explicit_links: []
---
# Issue #34: Rule Out That A Visit Can Be A Pass-Through When The Ship Actually Stopped

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/issues/34  
**State:** closed | **Author:** jbugella  
**Created:** 2024-12-20  
**Closed:** 2024-12-20  

## Description

**Full diff:** [601f98f28fc5...ad0e6c32526b](https://github.com/teqplay/vesselvoyage-backend/compare/601f98f28fc5...ad0e6c32526b)
**Merge commit:** [ad0e6c32526b](https://github.com/teqplay/vesselvoyage-backend/commit/ad0e6c32526b)
**Author:** Jos de Jong
**Reviewers:** Darius Wattimena
**Approvers:** Darius Wattimena
**Source Branch:** [feat/SPV-409_utilize_e-sof_stops_to_determine_pass-through](https://github.com/teqplay/vesselvoyage-backend/tree/feat/SPV-409_utilize_e-sof_stops_to_determine_pass-through)
**Destination Branch:** [develop](https://github.com/teqplay/vesselvoyage-backend/tree/develop)
**Closed On:** 2022-01-03T12:33:09.809758+00:00
**Status:** MERGED

Before, it sometimes happened that a visit was marked as a pass-through, and therefore removed, because the average speed of the ship was too high. For example in Singapore which has a very large port area: if a ship stops for a short period of say 7 hours, and travels on normal speed for 6 hours though the port area, the average speed is too high during this 13 hours and the visit is marked as a pass through and removed.

This PR solves this by ruling out that a visit can be a pass-through when the ship actually stopped.

