---
id: github:teqplay/vesselvoyage-backend:pr:506
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 506
title: Automatic recalculation more stats
author: Darius-Wattimena
state: closed
date: '2025-05-19'
merged_at: '2025-05-20'
base_branch: develop
head_branch: explain-recalc-ship-types
url: https://github.com/teqplay/vesselvoyage-backend/pull/506
labels: []
linked_issues: []
explicit_links: []
---
# PR #506: Automatic recalculation more stats

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/506  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `explain-recalc-ship-types`  
**Created:** 2025-05-19  
**Merged:** 2025-05-20  

## Description

Adds the possibility to show the amount of ships that still need to be recalculated and also per category. I needed this today so I could make a better assessment on what ships were failing. But given that the code was quite okay, I thought it wouldn't hurt to add this endpoint to the available ones.

Example result from the current PROD automatic recalculations data:
```json
{
	"status": {
		"NOT_READY": 80509,
		"FINISHED": 43526,
		"ERROR": 11213,
		"READY": 86
	},
	"byCategory": {
		"FISHING": {
			"NOT_READY": 11378,
			"FINISHED": 2338,
			"ERROR": 624,
			"READY": 2
		},
		"TUG": {
			"FINISHED": 2804,
			"NOT_READY": 15456,
			"ERROR": 864,
			"READY": 5
		},
		"BULK_CARRIER": {
			"FINISHED": 6917,
			"NOT_READY": 2846,
			"ERROR": 1638
		},
		"TANKER": {
			"FINISHED": 9227,
			"ERROR": 2249,
			"NOT_READY": 9101
		},
		"GENERAL_CARGO": {
			"NOT_READY": 15414,
			"FINISHED": 10471,
			"ERROR": 2521,
			"READY": 2
		},
		"OFFSHORE": {
			"NOT_READY": 2935,
			"FINISHED": 1498,
			"ERROR": 395
		},
		"PASSENGER": {
			"NOT_READY": 5558,
			"FINISHED": 1299,
			"READY": 68,
			"ERROR": 498
		},
		"CONTAINER": {
			"FINISHED": 3795,
			"NOT_READY": 1214,
			"ERROR": 907
		},
		"PLEASURE_CRAFT": {
			"NOT_READY": 2380,
			"FINISHED": 630,
			"ERROR": 240
		}
	}
}
```

## Commits

- `6b431f79` **Darius Wattimena** (2025-05-19): Added an endpoint to see the automatic recalculation status per ship category
- `5a67fed2` **Darius Wattimena** (2025-05-19): Code cleanup

## Reviews

### leonjoosse — APPROVED (2025-05-19)

_No comment._
