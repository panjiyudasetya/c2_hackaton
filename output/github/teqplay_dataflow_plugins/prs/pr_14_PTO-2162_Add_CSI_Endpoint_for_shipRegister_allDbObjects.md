---
id: github:teqplay/dataflow_plugins:pr:14
source: github
type: pull_request
repo: teqplay/dataflow_plugins
number: 14
title: PTO-2162 Add CSI Endpoint for shipRegister allDbObjects
author: ryan-kharisma
state: closed
date: '2025-09-19'
merged_at: '2025-11-04'
base_branch: develop
head_branch: PTO-2162_add_csi_endpoint_allDbObjects
url: https://github.com/teqplay/dataflow_plugins/pull/14
labels: []
linked_issues: []
explicit_links: []
---
# PR #14: PTO-2162 Add CSI Endpoint for shipRegister allDbObjects

**Repo:** teqplay/dataflow_plugins  
**URL:** https://github.com/teqplay/dataflow_plugins/pull/14  
**State:** closed | **Author:** ryan-kharisma  
**Base ← Head:** `develop` ← `PTO-2162_add_csi_endpoint_allDbObjects`  
**Created:** 2025-09-19  
**Merged:** 2025-11-04  

## Description

add new csi API shipRegister allDbObjects to get shipcat and subcat and shiprole

## Commits

- `2948689f` **ryan_at_teqplay** (2025-09-19): add new csi API shipRegister allDbObjects to get shipcat and subcat and shiprole
- `585139da` **ryan_at_teqplay** (2025-11-03): revert api version
- `b2f5ae2a` **ryan_at_teqplay** (2025-11-03): update download function download_registered_ships_all_dbo and test the api
- `6b637f78` **ryan_at_teqplay** (2025-11-03): add augment rules for SRP OOP and DRY concepts
- `5b787531` **ryan_at_teqplay** (2025-11-03): fix flake8 linter
- `b4e26212` **ryan_at_teqplay** (2025-11-03): fix imports
- `a567b14a` **ryan_at_teqplay** (2025-11-03): address Panji's Feedback
- `472e9282` **ryan_at_teqplay** (2025-11-03): fix imports
- `8e7a1238` **ryan_at_teqplay** (2025-11-04): remove DAG related in dry principle docs
- `e9176379` **ryan_at_teqplay** (2025-11-04): hide implementation details on augment rules

## Reviews

### panjiyudasetya — CHANGES_REQUESTED (2025-11-03)

_No comment._

### ryan-kharisma — COMMENTED (2025-11-03)

_No comment._

### panjiyudasetya — CHANGES_REQUESTED (2025-11-04)

_No comment._

### panjiyudasetya — APPROVED (2025-11-04)

_No comment._

## Review Comments

### panjiyudasetya — 2025-11-03 on `.augment/rules/dry_principle.md`

I think this rule should be adjusted @ryan-kharisma.

### panjiyudasetya — 2025-11-03 on `tests/dataflow_plugins/api_clients/test_download_methods_api.py`

Please remove this one, @ryan-kharisma. The `pytest` library will scan all test files (any files having `test_` prefixes) under the `tests/` directory.

### ryan-kharisma — 2025-11-03 on `tests/dataflow_plugins/api_clients/test_download_methods_api.py`

okay

### ryan-kharisma — 2025-11-03 on `.augment/rules/dry_principle.md`

okay

### panjiyudasetya — 2025-11-04 on `.augment/rules/dry_principle.md`

This one is still associated with the DAGs. Please avoid using the term DAG.

### panjiyudasetya — 2025-11-04 on `.augment/rules/dry_principle.md`

This one as well. Please avoid using the term DAG.

### panjiyudasetya — 2025-11-04 on `.augment/rules/dry_principle.md`

Aslo this one. Please avoid using the term DAG.

### panjiyudasetya — 2025-11-04 on `.augment/rules/dry_principle.md`

And this one. Please avoid using the term DAG.

### panjiyudasetya — 2025-11-04 on `.augment/rules/dry_principle.md`

And this one.

### panjiyudasetya — 2025-11-04 on `.augment/rules/dry_principle.md`

Please avoid using the term DAG.

## Comments

### ryan-kharisma — 2025-11-03

already tested in local and check the expected results as below: 

python3 tests/dataflow_plugins/api_clients/test_download_methods_api.py
🧪 CSI API Download Methods Test
Time: 2025-11-03 14:45:57
Environment: dev
🚀 Testing Download Methods - API Integration
============================================================

1️⃣  Setting up authentication...
   ✅ Client ID: data-engineering
   ✅ Client Secret: ********************************
INFO:dataflow_plugins.api_clients.teqplay_api.auth:Requesting a new keycloak token...
INFO:dataflow_plugins.api_clients.teqplay_api.auth:Keycloak token expires at 2025-11-04T14:45:57.523455 ...
   ✅ Token obtained: eyJhbGciOiJSUzI1NiIs...

2️⃣  Initializing CSI API...
   ✅ API initialized
   ✅ Base URL: https://csibackend-internal.dev.teqplay.com
   ✅ API Version: 1
   ✅ Constructed URL: https://csibackend-internal.dev.teqplay.com/v1

3️⃣  Created temp directory: /var/folders/0c/_rp987dd6qq3d83ggtgffmw80000gn/T/tmpds42m1ow

4️⃣  Testing download_registered_ships (v1 endpoint)...
   📥 Downloading to: /var/folders/0c/_rp987dd6qq3d83ggtgffmw80000gn/T/tmpds42m1ow/registered_ships_v1.json
   🌐 Expected URL: https://csibackend-internal.dev.teqplay.com/v1/shipRegister/list/cache
   ✅ File created: registered_ships_v1.json
   ✅ File size: 130,000,988 bytes
   ✅ Valid JSON array with 160,711 records
   ✅ Sample fields: ['_id', 'identifiers', 'types', 'categories', 'dimensions']...

5️⃣  Testing download_registered_ships_all_dbo (v2 endpoint)...
   📥 Downloading to: /var/folders/0c/_rp987dd6qq3d83ggtgffmw80000gn/T/tmpds42m1ow/registered_ships_all_dbo_v2.json
   🌐 Expected URL: https://csibackend-internal.dev.teqplay.com/v2/shipRegister/allDbObjects
   ✅ File created: registered_ships_all_dbo_v2.json
   ✅ File size: 207,591,726 bytes
   ✅ Valid JSON array with 160,711 records
   ✅ Sample fields: ['identifiers', 'types', 'categories', 'dimensions', 'administration']...

6️⃣  Comparing results...
   📊 V1 endpoint records: 160,711
   📊 V2 endpoint records: 160,711
   📊 V1 endpoint fields: 10 fields
   📊 V2 endpoint fields: 14 fields
   📊 Common fields: 9
   📊 V1 unique fields: ['nameUpperCase']
   📊 V2 unique fields: ['administration', 'communication', 'scores', 'syncedAt', 'ticketId']

✅ API Integration Test Completed Successfully!
   ✅ Both download methods work correctly
   ✅ V1 endpoint: download_registered_ships
   ✅ V2 endpoint: download_registered_ships_all_dbo
   ✅ DRY implementation verified

🎉 All tests passed!
