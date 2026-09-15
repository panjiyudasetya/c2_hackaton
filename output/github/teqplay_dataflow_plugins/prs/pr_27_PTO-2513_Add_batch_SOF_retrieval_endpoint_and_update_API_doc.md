---
id: github:teqplay/dataflow_plugins:pr:27
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 27
title: PTO-2513 Add batch SOF retrieval endpoint and update API documentation
author: panjiyudasetya
state: closed
date: '2026-02-20'
merged_at: '2026-02-24'
base_branch: develop
head_branch: PTO-2513
url: https://github.com/teqplay/dataflow_plugins/pull/27
labels: []
linked_issues: []
explicit_links: []
---
# PR #27: PTO-2513 Add batch SOF retrieval endpoint and update API documentation

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/27  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2513`  
**Created:** 2026-02-20  
**Merged:** 2026-02-24  

## Description

### Description

This PR adds support for retrieving Statement of Facts (SOF) data from multiple ports in a single API call via the new `get_sof_by_ports()` method. Additionally, updates all Swagger documentation URLs to reflect the new endpoint naming convention.

**Changes:**
- New `get_sof_by_ports()` method for batch SOF retrieval
- Updated Swagger URLs to new format
- Added example payload documentation


## Commits

- `fc4bccd3` **Panji Y. Wiwaha** (2026-02-20): feat(vessel-voyage-api): add batch SOF retrieval and update swagger URLs
  - Add get_sof_by_ports() method for retrieving SOF data from multiple ports in a single request
  - Update Swagger documentation URLs to use new endpoint naming format
  - Improve API documentation with example payload for batch requests
- `e82dd1aa` **Panji Y. Wiwaha** (2026-02-24): docs(vessel-voyage-api): update get_sof_by_ports example payload
  - Change view parameter to lowercase 'pto' for consistency
  - Add 'finished' parameter to example payload
- `afb7c277` **Panji Y. Wiwaha** (2026-02-24): test(vessel-voyage-api): add unit test for get_sof_by_ports method
  - Add test_get_sof_by_ports to verify POST request to /sof/byPort endpoint
  - Assert correct method, path, payload, and token are passed to _api_request
  - Verify response is correctly returned from the method
  - Prevent regressions in batch SOF retrieval functionality

## Reviews

### augmentcode[bot] — COMMENTED (2026-02-20)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_plugins%2Fpull%2F27%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-02-24)

_No comment._

### panjiyudasetya — COMMENTED (2026-02-24)

_No comment._

### ryan-kharisma — APPROVED (2026-02-24)

LGTM

## Review Comments

### panjiyudasetya — 2026-02-24 on `dataflow_plugins/api_clients/teqplay_api/vessel_voyage.py`

No, that's already correct.

### panjiyudasetya — 2026-02-24 on `dataflow_plugins/api_clients/teqplay_api/vessel_voyage.py`

Addressed by afb7c27.

## Comments

### panjiyudasetya — 2026-02-24

Here is the test script to check the new API:
```python

# Create test file on: /dataflow_plugins/test.py


from dotenv import load_dotenv
from dataflow_plugins.api_clients.teqplay_api.vessel_voyage import VesselVoyageAPI

load_dotenv()


if __name__ == "__main__":
    token = "<put-your-api-token>"

    api = VesselVoyageAPI()
    result = api.get_sof_by_ports(token=token, payload=[
        {
            "view": "pto",
            "unlocode": "NLRTM",
            "start": "2026-01-01T00:00:00Z",
            "end": "2026-01-07T00:00:00Z",
            "vesselType": ["SEA_VESSEL"],
            "finished": True,
            "limit": 10
        },
        {
            "view": "pto",
            "unlocode": "NLRTM",
            "start": "2026-01-01T00:00:00Z",
            "end": "2026-01-07T00:00:00Z",
            "vesselType": ["BARGE"],
            "finished": True,
            "limit": 10
        },
        {
            "view": "pto",
            "unlocode": "NLAMS",
            "start": "2026-01-01T00:00:00Z",
            "end": "2026-01-07T00:00:00Z",
            "vesselType": ["SEA_VESSEL"],
            "finished": True,
            "limit": 10
        }
    ])

    print(result)
```
Run it using this command `$ python test.py`
