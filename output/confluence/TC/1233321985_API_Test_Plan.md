---
id: confluence:1233321985
source: confluence
type: page
space: TC
title: API Test Plan
author: Joost Laurman
date: '2026-06-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1233321985
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1233321985
---
# API Test Plan

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1233321985  

## Content

## 1. Authentication

### Endpoints

wide760POST /v1/auth/token
POST /v1/auth/token/refresh

### Tests

* Invalid `client_id` / `client_secret`
* Missing fields
* Empty strings
* Reused refresh token
* Expired refresh token
* Token replay after refresh
* Brute force / rate limit
* Response leaks: `refresh_token`, scopes, roles, expiry, internal errors

Use:

* **JWT Editor**
* **Logger++**
* **Turbo Intruder**

---

## 2. Authorization Coverage

Test every endpoint with:

wide760No Authorization header
Invalid bearer token
Expired token
Token from another client/app
Token with reduced scope

Priority groups:

wide760/v1/event/history/\*
/v1/ship/\*
/v1/infra/\*
/v1/predict/request
/v2/voyage/\*

Expected:

* `401` for unauthenticated
* `403` for authenticated but unauthorized
* No partial data leaks

---

## 3. Event History Abuse

### Endpoints

wide760POST /v1/event/history/boundingBox
POST /v1/event/history/circle
GET /v1/event/history/imo/{imo}
POST /v1/event/history/imolist
POST /v1/event/history/mmsilist
POST /v1/event/history/polygon
POST /v1/event/history/query
GET /v1/event/history/{mmsi}

### Key Tests

#### Time-window abuse

wide760maxDays=999999
from=1900-01-01T00:00:00Z
to=2100-01-01T00:00:00Z

#### Area abuse

wide760{
"bottomLeft": [-180, -90],
"topRight": [180, 90]
}

#### Circle abuse

wide760radiusInKm=0
radiusInKm=-1
radiusInKm=999999

#### Polygon abuse

* Unclosed polygon
* Self-intersecting polygon
* Huge polygon
* Thousands of coordinates
* Reversed latitude/longitude
* `NaN`, `Infinity`, strings instead of numbers

---

## 4. Query Logic Validation

Endpoint:

wide760POST /v1/event/history/query

It supports only one query mode at a time: polygon, circle, MMSI list, or IMO list. Test mixed modes.

wide760{
"polygon": {},
"circle": {},
"mmsis": [244660338],
"imos": [9270635]
}

Expected:

* Clean `400`
* No stack trace
* No partial query execution

---

## 5. Ship Data Enumeration

### Endpoints

wide760GET /v1/ship/current/mmsi/{mmsi}
GET /v1/ship/current/imo/{imo}
POST /v1/ship/current/mmsi
POST /v1/ship/current/imo
GET /v1/ship/characteristics/imo/{imo}

### Tests

* Enumerate MMSI / IMO ranges
* Compare valid vs invalid response timing
* Batch request with 1, 100, 10k IDs
* Duplicate IDs
* Negative IDs
* Very large integers
* Strings in numeric fields

Look for:

* Unrestricted data harvesting
* Missing rate limits
* Different errors revealing valid vessels

---

## 6. Infra Object Enumeration

### Pattern

wide760GET /v1/infra/{type}
GET /v1/infra/{type}/{id}
POST /v1/infra/{type}/bulk
GET /v1/infra/{type}/port/{port}

### Tests

* IDOR-style object access by ID
* Bulk endpoint with many IDs
* Port code enumeration
* Invalid port values
* Case sensitivity: `NLRTM`, `nlrtm`, `../NLRTM`
* Injection in `{id}` and `{port}`

Payloads:

wide760' -> used to test SQL injection
" -> tests parsers, JSON handling and other query construction.
../ -> tests path traversal handling
%2e%2e%2f -> test block raw traversal but accidentally allow encoded versions.
{{7\*7}} -> tests for Server-Side Template Injection (SSTI).
${7\*7} -> Similar to SSTI, but for different template engines

---

## 7. Voyage Endpoints

### Endpoints

wide760/v2/voyage/entry/\*
/v2/voyage/sof/\*

### Tests

* Access by `entryId`, `visitId`, IMO
* Cross-client data exposure
* Batch lookup authorization
* Lookaround abuse
* Date range abuse on port queries
* Large POST bodies

Key risk:

* Voyage and SOF data may be commercially sensitive.

---

## 8. Prediction Endpoint

wide760POST /v1/predict/request

### Tests

* Malformed ship identifiers
* Impossible coordinates
* Very long route
* Empty route
* Duplicate waypoints
* Extreme timestamps
* Replay same prediction request many times

Look for:

* Expensive computation DoS
* Internal model/service errors
* Unbounded request processing

---

## 9. NDJSON Response Handling

Several event endpoints return:

wide760application/x-ndjson

Test:

* Burp active scan still parses responses
* Large stream interruption
* Response truncation
* Invalid `Accept` headers

Headers to try:

wide760Accept: application/json
Accept: application/x-ndjson
Accept: \*/\*
Accept: text/html

---

## 10. Rate Limiting

Use Turbo Intruder on:

wide760POST /v1/auth/token
POST /v1/auth/token/refresh
POST /v1/event/history/query
POST /v1/ship/current/mmsi
POST /v1/predict/request

Check for:

wide760429 Too Many Requests
Retry-After

---

## 11. Burp Scan Priority

### Critical

wide760/v1/auth/\*
/v2/voyage/\*
/v1/predict/request

### High

wide760/v1/event/history/\*
/v1/ship/current/\*

### Medium

wide760/v1/infra/\*
/v1/ship/characteristics/\*

---

## Likely High-Risk Findings

1. Token refresh misuse
2. Excessive data access through ship/event batch endpoints
3. Missing authorization boundaries on voyage data
4. Geospatial/time-window DoS
5. Enumeration of MMSI, IMO, infra IDs, visit IDs
6. Large NDJSON response abuse
7. Prediction endpoint computational abuse