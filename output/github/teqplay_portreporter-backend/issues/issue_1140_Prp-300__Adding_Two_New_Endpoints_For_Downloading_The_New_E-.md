---
id: github:teqplay/portreporter-backend:issue:1140
source: github
type: issue
repo: teqplay/portreporter-backend
number: 1140
title: 'Prp-300: Adding Two New Endpoints For Downloading The New E-Sof In Pdf And
  Json Format (First Version).'
author: jbugella
state: closed
date: '2025-02-11'
url: https://github.com/teqplay/portreporter-backend/issues/1140
labels: []
explicit_links: []
---
# Issue #1140: Prp-300: Adding Two New Endpoints For Downloading The New E-Sof In Pdf And Json Format (First Version).

**Repo:** teqplay/portreporter-backend  
**URL:** https://github.com/teqplay/portreporter-backend/issues/1140  
**State:** closed | **Author:** jbugella  
**Created:** 2025-02-11  
**Closed:** 2025-02-11  

## Description

**Full diff:** [66b0c65c7fca...d1af386af7c1](https://github.com/teqplay/portreporter-backend/compare/66b0c65c7fca...d1af386af7c1)
**Merge commit:** [d1af386af7c1](https://github.com/teqplay/portreporter-backend/commit/d1af386af7c1)
**Author:** Joaquin Marquez Bugella
**Reviewers:** Joost Laurman, Damon Asberg, Wouter Naloop
**Approvers:** Joost Laurman
**Source Branch:** [feat/PRP-300/new_esof_pdf_export](https://github.com/teqplay/portreporter-backend/tree/feat/PRP-300/new_esof_pdf_export)
**Destination Branch:** [develop](https://github.com/teqplay/portreporter-backend/tree/develop)
**Closed On:** 2022-09-08T08:51:49.005221+00:00
**Status:** MERGED

Added two new endpoints to PortReporter backend, both for downloading the new E-SoF from PortReporter, in pdf \(/v2/portcalls/esof/pdf\)and json \(/v2/portcalls/esof/json\) formats.

**Please, consider that this is a first working prototype based on the old visual format and the frontend ESOF’s portcall tab \(data logic behind\).**

The new look&feel should be applied yet in another Jira card.

I add @{557058:63a9abe4-1e1f-4d11-868f-93ad9505f219} to the card just in case he wants to point out any difference from the front-end.

