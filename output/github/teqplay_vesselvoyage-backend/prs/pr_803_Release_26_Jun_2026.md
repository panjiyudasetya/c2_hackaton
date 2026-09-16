---
id: github:teqplay/vesselvoyage-backend:pr:803
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 803
title: Release 26 Jun 2026
author: Darius-Wattimena
state: closed
date: '2026-06-26'
merged_at: '2026-06-26'
base_branch: master
head_branch: develop
url: https://github.com/teqplay/vesselvoyage-backend/pull/803
labels: []
linked_issues: []
explicit_links: []
---
# PR #803: Release 26 Jun 2026

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/803  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `master` ← `develop`  
**Created:** 2026-06-26  
**Merged:** 2026-06-26  

## Description

_No description._

## Commits

- `af1abaee` **Darius Wattimena** (2026-06-23): Extend portreporter sof with lock stops
- `2a47fe56` **Darius Wattimena** (2026-06-23): Added tests to match new lock stops in portreporter sof
- `786476a6` **Darius Wattimena** (2026-06-23): Add dedicated test to reflect broken behaviour
- `4c2aed67` **Darius Wattimena** (2026-06-23): Fix the issue where inconsitent metadata is returned when we found the ship in CSI
- `e043a29d` **Darius Wattimena** (2026-06-23): Also add the MMSI for completeness
- `4ab36013` **Darius Wattimena** (2026-06-23): Adjust imo resolving to take the csi data as leading
- `65b69850` **Michel Wilson** (2026-06-23): Add ship name to encounter metadata in PortReporter SOF view
- `beceb7f1` **Darius Wattimena** (2026-06-23): Merge pull request #798 from teqplay/TCC-1038-lock-stops-portreporter-sof
  TCC-1038 lock stops portreporter sof
- `28b41732` **Darius Wattimena** (2026-06-23): Merge pull request #799 from teqplay/TCC-1038-inconsistent-ship-information
  TCC-1038 inconsistent ship information
- `09b88e40` **Darius Wattimena** (2026-06-23): Merge branch 'develop' into TCC-1030-add-ship-to-prp-encounter
- `22d73e12` **Darius Wattimena** (2026-06-23): Adjust name adding to be using the mappers still so we avoid auto wiring and extended pilots as well for consistency
- `9df454ba` **Darius Wattimena** (2026-06-23): Make portreporter sof be consistent as well with how it exposes the encounter info like we do for the PTO sof
- `a1f491e0` **Darius Wattimena** (2026-06-23): Added unit testing for the PortReporter SOF mapper
- `0d271d12` **Darius Wattimena** (2026-06-24): Merge pull request #800 from teqplay/TCC-1030-add-ship-to-prp-encounter
  Add ship name to encounter metadata in PortReporter SOF view
- `00b5b415` **Darius Wattimena** (2026-06-24): Fix an issue where the unlocode isn't taken into account to match the port area
- `041777de` **Darius Wattimena** (2026-06-24): Added some tests to represent the new logic which also allows port area resolving based on unlocode
- `a0910fa1` **Darius Wattimena** (2026-06-26): Merge pull request #802 from teqplay/TCC-1038-lock-stop-fix
  TCC-1038 lock and anchor stop port reference fix

## Reviews

### TeqJoostD — APPROVED (2026-06-26)

_No comment._

### augmentcode[bot] — COMMENTED (2026-06-26)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fvesselvoyage-backend%2Fpull%2F803%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments
