---
id: github:teqplay/vesselvoyage-backend:pr:404
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 404
title: SPV-2499 eventbuffer remove old events
author: leonjoosse
state: closed
date: '2025-01-30'
merged_at: '2025-01-31'
base_branch: develop
head_branch: SPV-2499-eventbuffer-remove-old-events
url: https://github.com/teqplay/vesselvoyage-backend/pull/404
labels: []
linked_issues: []
explicit_links: []
---
# PR #404: SPV-2499 eventbuffer remove old events

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/404  
**State:** closed | **Author:** leonjoosse  
**Base ← Head:** `develop` ← `SPV-2499-eventbuffer-remove-old-events`  
**Created:** 2025-01-30  
**Merged:** 2025-01-31  

## Description

Remove buffered events from the shipStatus when the new event the `bufferedEvent.eventTime != newEvent.eventTime`. Before, this was removed from the resulting shipStatus of newEvent, but that caused the bufferedEvent to stay in place.



## Commits

- `e7aa62c6` **leonj** (2025-01-30): Remove buffered events from the shipStatus when the new event the bufferedEvent.eventTime != newEvent.eventTime. Before, this was removed from the resulting shipStatus of newEvent, but that caused the bufferedEvent to stay in place.

## Reviews

### Darius-Wattimena — APPROVED (2025-01-31)

_No comment._
