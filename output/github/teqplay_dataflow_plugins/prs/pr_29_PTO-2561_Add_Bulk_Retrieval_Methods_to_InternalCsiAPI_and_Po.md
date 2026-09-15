---
id: github:teqplay/dataflow_plugins:pr:29
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 29
title: PTO-2561 Add Bulk Retrieval Methods to InternalCsiAPI and PomaAPI
author: panjiyudasetya
state: closed
date: '2026-04-17'
merged_at: '2026-04-17'
base_branch: develop
head_branch: PTO-2561
url: https://github.com/teqplay/dataflow_plugins/pull/29
labels: []
linked_issues: []
explicit_links:
- jira:PTO-2561
---
# PR #29: PTO-2561 Add Bulk Retrieval Methods to InternalCsiAPI and PomaAPI

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/29  
**State:** closed | **Author:** panjiyudasetya  
**Base ← Head:** `develop` ← `PTO-2561`  
**Created:** 2026-04-17  
**Merged:** 2026-04-17  

## Description

## Description

This PR introduces new bulk data retrieval methods to `InternalCsiAPI` and `PomaAPI` classes, enabling efficient retrieval of multiple resources in a single API call. These methods utilize POST requests with JSON payloads to fetch data for multiple IDs at once.

## Motivation

- **Performance**: Reduce API calls by fetching multiple resources in a single request
- **Efficiency**: Avoid N+1 query problems when working with multiple related entities
- **API Coverage**: Implement missing bulk endpoints from the Teqplay API

## Changes

### InternalCsiAPI (`internal.py`)

Added two new bulk retrieval methods:

1. **`get_registered_ships_by_ids(token: str, ship_ids: List[str]) -> List[Dict]`**
   - Retrieve multiple registered ships by ship IDs in a single request
   - Endpoint: `POST /shipRegister/id`
   - Accepts a list of ship IDs as payload

2. **`get_ship_mappings_by_imos(token: str, imos: List[str]) -> List[Dict]`**
   - Retrieve ship-mapping data for multiple IMO numbers
   - Endpoint: `POST /shipMapping/imo`
   - Accepts a list of IMO numbers as payload

### PomaAPI (`poma.py`)

Added three new bulk retrieval methods:

1. **`get_ports_bulk(token: str, port_ids: List[str]) -> List[Dict]`**
   - Retrieve multiple ports by port IDs
   - Endpoint: `POST /port/bulk`
   - [Swagger docs](https://backendpoma.dev.teqplay.com/swagger-ui/index.html#/Ports/getByIds_2)

2. **`get_terminals_bulk(token: str, terminal_ids: List[str]) -> List[Dict]`**
   - Retrieve multiple terminals by terminal IDs
   - Endpoint: `POST /terminal/bulk`
   - [Swagger docs](https://backendpoma.dev.teqplay.com/swagger-ui/index.html#/Terminals/getByIds)

3. **`get_berths_bulk(token: str, berth_ids: List[str]) -> List[Dict]`**
   - Retrieve multiple berths by berth IDs
   - Endpoint: `POST /berth/bulk`
   - [Swagger docs](https://backendpoma.dev.teqplay.com/swagger-ui/index.html#/Berths/getByIds_8)

## Testing

Comprehensive unit tests have been added for all new methods:

### InternalCsiAPI Tests
- `test_get_registered_ships_by_ids` - Validates bulk ship retrieval
- `test_get_ship_mappings_by_imos` - Validates IMO mapping retrieval

### PomaAPI Tests
- `test_get_ports_bulk` - Validates bulk port retrieval
- `test_get_terminals_bulk` - Validates bulk terminal retrieval
- `test_get_berths_bulk` - Validates bulk berth retrieval

**Test Coverage:**
- All tests use mocked `_api_request` to isolate method logic
- Verify correct HTTP method (POST), endpoint paths, and payloads
- Assert proper parameter passing (payload, token)
- Validate JSON response parsing
- All existing tests continue to pass (no regressions)

**Test Results:**
```
InternalCsiAPI: 6/6 tests passing
PomaAPI: 9/9 tests passing
```

## Technical Details

### Implementation Approach
- All methods follow existing code patterns in the codebase
- Utilize `_api_request` method from `BaseAPI` class
- POST requests with JSON payloads for bulk operations
- Consistent error handling and authentication via Bearer tokens
- Proper type hints (`List[str]`, `List[Dict]`) for better code quality

### Code Quality
- Follows DRY principles (no code duplication)
- Consistent with existing API method patterns
- Comprehensive docstrings with parameter descriptions
- Swagger documentation references included
- Type hints for all parameters and return values
- No linting or diagnostic issues

### Method Organization
- Bulk methods are logically grouped near their single-item counterparts
- `InternalCsiAPI`: Reorganized `download_ship_mappings()` for better structure
- `PomaAPI`: Bulk variants placed after their respective GET methods

## Impact

**Files Modified:** 4
- `dataflow_plugins/api_clients/teqplay_api/internal.py` (+55, -15)
- `dataflow_plugins/api_clients/teqplay_api/poma.py` (+67, -7)
- `tests/dataflow_plugins/api_clients/teqplay_api/test_internal.py` (+139)
- `tests/dataflow_plugins/api_clients/teqplay_api/test_poma.py` (+182)

**Total Changes:** +443 lines, -22 lines

## Usage Example

```python
# Create test file on: /dataflow_plugins/test.py
import os

from dotenv import load_dotenv
from dataflow_plugins.api_clients.teqplay_api import InternalCsiAPI, PomaAPI

# InternalCsiAPI - Bulk ship retrieval
csi_api = InternalCsiAPI()
ship_ids = ["04f7572c-0f57-4ae1-aa24-5a1a3e0fde15", "1a2b3c4d-5e6f-7g8h-9i0j-k1l2m3n4o5p6"]
ships = csi_api.get_registered_ships_by_ids(token="your-token", ship_ids=ship_ids)

# InternalCsiAPI - Bulk IMO mapping retrieval
imos = ["9257606", "8014382"]
mappings = csi_api.get_ship_mappings_by_imos(token="your-token", imos=imos)

# PomaAPI - Bulk port retrieval
poma_api = PomaAPI()
port_ids = ["A4616C682643AD7869EEF307DEF7013DCBD252B4", "B5727D793754BE8970FFF418EFG8124EDCE363C5"]
ports = poma_api.get_ports_bulk(token="your-token", port_ids=port_ids)

# PomaAPI - Bulk terminal retrieval
terminal_ids = ["A95DE56801663AB86C95F23B31C4357DA892D171", "B06EF67902774BC97DA6G34C42D5468EB903E282"]
terminals = poma_api.get_terminals_bulk(token="your-token", terminal_ids=terminal_ids)

# PomaAPI - Bulk berth retrieval
berth_ids = ["6B2EBF4E4F1C85290DE7DF646D60260E92FA46B9", "7C3FCG5F5G2D96391EF8EG757E71371F03GB57C0"]
berths = poma_api.get_berths_bulk(token="your-token", berth_ids=berth_ids)
```

## Checklist

- [x] Code follows existing patterns and style guidelines
- [x] All new methods have comprehensive unit tests
- [x] All tests pass successfully (no regressions)
- [x] Type hints added for all parameters and return values
- [x] Docstrings include parameter descriptions and Swagger references
- [x] No linting or diagnostic issues
- [x] Follows DRY principles from `.augment/rules/dry_principle.md`
- [x] Follows Single Responsibility Principle from `.augment/rules/single_responsibility_principle.md`
- [x] No breaking changes to existing functionality

## Deployment Notes

No special deployment steps required. These are new methods that don't affect existing functionality.

## Commits

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

## Reviews

### augmentcode[bot] — COMMENTED (2026-04-17)

Review completed. 1 suggestion posted.

[![Fix All in Augment](https://public.augment-assets.com/code-review/fix-all-in-augment.svg "Fix All in Augment")](https://app.augmentcode.com/open-chat?mode=agent&prompt=%23%23%20Review%20Comment%20Analysis%0A%0APlease%20help%20me%20address%20all%20the%20review%20comments%20from%20this%20PR%3A%20https%3A%2F%2Fgithub.com%2Fteqplay%2Fdataflow_plugins%2Fpull%2F29%0A%0A%23%23%23%20Steps%20to%20Follow%3A%0A%0A1.%20%2A%2ADetermine%20Github%20Branch%2A%2A%3A%20Use%20%60git%20branch%20--show-current%60%20to%20get%20the%20current%20branch%2C%20then%20fetch%20PR%20details%20from%20the%20Github%20API%20to%20determine%20the%20correct%20branch%20for%20this%20PR%0A2.%20%2A%2ABranch%20Verification%2A%2A%3A%20Ask%20the%20user%20to%20switch%20branches%20if%20they%20are%20not%20on%20the%20correct%20branch%0A3.%20%2A%2AReview%20Comments%2A%2A%3A%20List%20all%20review%20comments%20from%20the%20PR%20and%20ask%20me%20which%20ones%20I%20want%20to%20fix%0A%0APlease%20start%20by%20checking%20the%20current%20branch%20and%20PR%20details.)


<h2></h2>

Comment `augment review` to trigger a new review at any time.

### panjiyudasetya — COMMENTED (2026-04-17)

_No comment._

### ryan-kharisma — APPROVED (2026-04-17)

LGTM

## Review Comments

### panjiyudasetya — 2026-04-17 on `dataflow_plugins/api_clients/teqplay_api/internal.py`

Resolved by 1277122.

## Comments
