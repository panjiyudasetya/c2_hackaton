---
id: github:teqplay/dataflow_plugins:pr:31
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 31
title: Release 1.6.0 to master
author: panjiyudasetya
state: closed
date: '2026-04-21'
merged_at: '2026-04-21'
base_branch: master
head_branch: release/1.6.0
url: https://github.com/teqplay/dataflow_plugins/pull/31
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2513
- jira:PTO-2561
---
# PR #31: Release 1.6.0 to master

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/31  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `master` ← `release/1.6.0`  
**Created:** 2026-04-21  
**Merged:** 2026-04-21  

## Description


## [1.6.0] - 2026-04-21
### Added
- Add batch SOF retrieval endpoint and update API documentation (#27) 
- Add `POST` download support with DRY refactoring (#28)
- Add bulk retrieval methods to `InternalCsiAPI and PomaAPI (#29)  

## Commits

- `bf2b6245` **Panji Y. Wiwaha** (2025-12-18): Merge pull request #25 from teqplay/release/1.5.0
  Release 1.5.0 to develop
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
- `b975340d` **Panji Y. Wiwaha** (2026-02-24): Merge pull request #27 from teqplay/PTO-2513
  PTO-2513 Add batch SOF retrieval endpoint and update API documentation
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
- `ab9cfa58` **Panji Y. Wiwaha** (2026-02-24): Merge pull request #28 from teqplay/chore/add-download-options
  Feature - Add POST Download Support with DRY Refactoring
- `3508bcef` **Panji Y. Wiwaha** (2026-04-17): feat(api): add bulk retrieval methods to InternalCsiAPI
  Add two new POST methods for bulk data retrieval:
  - get_registered_ships_by_ids(): Retrieve multiple registered ships by ship IDs
  - get_ship_mappings_by_imos(): Retrieve ship mappings by IMO numbers
  
  Both methods:
  - Use POST with JSON payload for bulk operations
  - Follow existing code patterns and utilize _api_request from BaseAPI
  - Include proper type hints and docstrings with Swagger references
  - Support authentication via Bearer token
  
  Also reorganized download_ship_mappings() method position for better logical grouping.
- `b5edd59a` **Panji Y. Wiwaha** (2026-04-17): feat(api): add bulk retrieval methods to PomaAPI
  Add three new POST methods for bulk data retrieval:
  - get_ports_bulk(): Retrieve multiple ports by port IDs
  - get_terminals_bulk(): Retrieve multiple terminals by terminal IDs
  - get_berths_bulk(): Retrieve multiple berths by berth IDs
  
  All methods:
  - Use POST with JSON payload for bulk operations
  - Follow existing code patterns and utilize _api_request from BaseAPI
  - Include proper type hints and docstrings with Swagger documentation links
  - Support authentication via Bearer token
  
  Methods are organized logically with bulk variants placed after their respective single-item counterparts.
- `391fb390` **Panji Y. Wiwaha** (2026-04-17): test(api): add comprehensive tests for InternalCsiAPI bulk methods
  Add unit tests for the new bulk retrieval methods:
  - test_get_registered_ships_by_ids(): Tests bulk ship retrieval by IDs
  - test_get_ship_mappings_by_imos(): Tests ship mappings retrieval by IMOs
  
  Test features:
  - Mock _api_request to isolate method logic
  - Verify correct HTTP method (POST) and endpoint paths
  - Validate payload and token parameters are passed correctly
  - Assert response data is properly parsed from JSON
  - Use realistic mock data matching API response structure
  
  All tests pass successfully (6/6 tests in TestInternalCsiAPI).
- `2983bb99` **Panji Y. Wiwaha** (2026-04-17): test(api): add comprehensive tests for PomaAPI bulk methods
  Add unit tests for the new bulk retrieval methods:
  - test_get_ports_bulk(): Tests bulk port retrieval by IDs
  - test_get_terminals_bulk(): Tests bulk terminal retrieval by IDs
  - test_get_berths_bulk(): Tests bulk berth retrieval by IDs
  
  Test features:
  - Mock _api_request to isolate method logic
  - Verify correct HTTP method (POST) and endpoint paths
  - Validate payload and token parameters are passed correctly
  - Assert response data is properly parsed from JSON
  - Use realistic mock data matching API response structure
  - Follow existing test patterns in the codebase
  
  All tests pass successfully (9/9 tests in TestPomaAPI).
- `1277122d` **Panji Y. Wiwaha** (2026-04-17): feedback(docstring): Address PR #29 review comments
  - Add missing documentation for the requried parameters
- `00c3a168` **Panji Y. Wiwaha** (2026-04-17): Merge pull request #29 from teqplay/PTO-2561
  PTO-2561 Add Bulk Retrieval Methods to InternalCsiAPI and PomaAPI
- `8bfa5d92` **Panji Y. Wiwaha** (2026-04-21): Bump version 1.6.0

## Reviews

### ryan-kharisma — APPROVED (2026-04-21)

LGTM

### augmentcode[bot] — COMMENTED (2026-04-21)

Review completed. 2 suggestions posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_plugins%2Fpull%2F31%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

## Review Comments

## Comments
