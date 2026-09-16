---
id: github:teqplay/dataflow_plugins:pr:28
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 28
title: Feature - Add POST Download Support with DRY Refactoring
author: panjiyudasetya
state: closed
date: '2026-02-24'
merged_at: '2026-02-24'
base_branch: develop
head_branch: chore/add-download-options
url: https://github.com/teqplay/dataflow_plugins/pull/28
labels: []
linked_issues: []
explicit_links: []
---
# PR #28: Feature - Add POST Download Support with DRY Refactoring

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/28  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `chore/add-download-options`  
**Created:** 2026-02-24  
**Merged:** 2026-02-24  

## Description

### Description
Implements download-to-file functionality for `POST` requests in the Vessel Voyage API while refactoring existing download methods to eliminate code duplication.

### Key Changes
- **New Feature**: `_download_with_post()` method for downloading large resources via POST endpoints
- **DRY Refactoring**: Extracted 3 helper methods to eliminate ~42 lines of duplicate code
  - `_validate_download_params()` - Parameter validation
  - `_construct_download_url()` - URL construction with version override
  - `_write_response_to_file()` - Streaming file writer
- **Enhanced API**: `VesselVoyage.get_sof_by_ports()` now supports optional download options
- **Test Coverage**: Added 3 comprehensive unit tests for download functionality

### Impact
- **Code Reduction**: 111 → 84 lines (24% reduction)
- **Zero Duplication**: Eliminated 100% of duplicate code between download methods
- **Backward Compatible**: All 15 existing tests pass
- **Follows Guidelines**: Adheres to DRY and SRP principles

### Testing
```bash
✅ All 15 tests passing (14 VesselVoyage + 1 Internal)
✅ No linting issues
```


## Commits

- `ca07047d` **Panji Y. Wiwaha** (2026-02-24): feat: Add POST download support with DRY refactoring
  - Add three DRY helper methods to BaseAPI:
    * _validate_download_params: Validate resource type and directory
    * _construct_download_url: Build URL with optional API version override
    * _write_response_to_file: Stream and write response data to file
  
  - Add _download_with_post method for POST requests with payload
    * Supports downloading large resources via POST endpoints
    * Reuses DRY helper methods for validation, URL construction, and file writing
    * Includes proper error handling with raise_for_status()
  
  - Refactor existing _download method to use DRY helpers
    * Reduced from 54 to 18 lines (67% reduction)
    * Eliminates ~42 lines of code duplication
    * Maintains backward compatibility
  
  - Implement download options in VesselVoyage.get_sof_by_ports
    * Add optional download_opts parameter
    * Conditional logic: download to file or return JSON
    * Returns None when downloading, List[Dict] when returning JSON
  
  - Add comprehensive unit tests for download functionality
    * test_get_sof_by_ports_with_download_opts: Valid download options
    * test_get_sof_by_ports_with_incomplete_download_opts: Incomplete options
    * test_get_sof_by_ports_with_none_download_opts: No options (default)
  
  Code metrics:
  - Total lines: 111 → 84 (24% reduction)
  - Code duplication: ~42 lines → 0 lines (100% elimination)
  - All 15 tests pas- All 15 tests pas- All 15 tests pas- All 15 tests pas- Alrinciples as per project guidelines.
- `87e21e8c` **Panji Y. Wiwaha** (2026-02-24): fix: Address PR #28 review comments
  Fix three code quality issues identified in PR review:
  
  1. Enhanced download_opts validation (Line 125)
     - Check for non-empty/non-None values, not just key presence
     - Prevent surprising behavior like writing to /<filename>
     - Added validation in _validate_download_params for all 3 params
     - Added 2 new test cases for edge cases
  
  2. Fix mutable default argument anti-pattern (Line 140)
     - Changed custom_headers: Dict = {} to Optional[Dict] = None
     - Applied fix to 3 methods: _api_request, _download, _download_with_post
     - Added conditional check before updating headers
     - Prevents cross-call state leakage
  
  3. Fix truthy check in _construct_download_url (Line 232)
     - Changed 'if api_version:' to 'if api_version is not None:'
     - Ensures api_version=0 is treated as valid version, not falsy
     - Maintains backward compatibility with existing code
  
  Additional changes:
  - Updated .gitignore to exclude tmp/ directory
  
  Test results:
  - All 16 VesselVoyage tests passing
  - All Internal CSI API tests p- All Internal CSI API tests p- All Internal CSI API ices and project guidelines.
- `f2695073` **Panji Y. Wiwaha** (2026-02-24): style: Format multi-line conditional with PEP 8 compliance
  - Move binary operators to beginning of continuation lines
  - Add noqa: W503 comments to suppress line break warnings
  - Improves code readability and follows PEP 8 style guide

## Reviews

### augmentcode[bot] — COMMENTED (2026-02-24)

Review completed. 3 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_plugins%2Fpull%2F28%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-02-24)

_No comment._

### panjiyudasetya — COMMENTED (2026-02-24)

_No comment._

### panjiyudasetya — COMMENTED (2026-02-24)

_No comment._

### ryan-kharisma — APPROVED (2026-02-24)

LGTM

## Review Comments

### panjiyudasetya — 2026-02-24 on `dataflow_plugins/api_clients/teqplay_api/vessel_voyage.py`

Addressed by 87e21e8.

### panjiyudasetya — 2026-02-24 on `dataflow_plugins/api_clients/teqplay_api/base.py`

Addressed by 87e21e8.

### panjiyudasetya — 2026-02-24 on `dataflow_plugins/api_clients/teqplay_api/base.py`

Addressed by 87e21e8.

## Comments

### panjiyudasetya — 2026-02-24

Here is the script to test the download function.

```python

# Create test file on: /dataflow_plugins/test.py

import os

from dotenv import load_dotenv
from dataflow_plugins.api_clients.teqplay_api.vessel_voyage import VesselVoyageAPI

load_dotenv()


if __name__ == "__main__":
    token = "<put-your-token-here>"
    download_opts = {
        'to_dirs': os.getcwd(),
        'as_filename': 'sof-by-ports.json',
        'resource_type': 'json'
    }

    from pdb import set_trace; set_trace()

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
    ], download_opts=download_opts)

```
