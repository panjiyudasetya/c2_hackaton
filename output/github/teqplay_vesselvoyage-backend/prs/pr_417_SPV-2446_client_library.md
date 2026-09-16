---
id: github:teqplay/vesselvoyage-backend:pr:417
source: github
type: pull_request
repo: teqplay/vesselvoyage-backend
number: 417
title: SPV-2446 client library
author: Darius-Wattimena
state: closed
date: '2025-02-13'
merged_at: '2025-02-18'
base_branch: develop
head_branch: SPV-2446-client-library
url: https://github.com/teqplay/vesselvoyage-backend/pull/417
labels: []
linked_issues: []
explicit_links: []
---
# PR #417: SPV-2446 client library

**Repo:** teqplay/vesselvoyage-backend  
**URL:** https://github.com/teqplay/vesselvoyage-backend/pull/417  
**State:** closed | **Author:** Darius-Wattimena  
**Base ← Head:** `develop` ← `SPV-2446-client-library`  
**Created:** 2025-02-13  
**Merged:** 2025-02-18  

## Description

Client is available already as a snapshot version.
You can load in the client with the following:
```
implementation "nl.teqplay.vesselvoyage:client:20250213-SNAPSHOT"
```

## Commits

- `a669f5c5` **Darius Wattimena** (2025-02-05): Cleanup main gradle script
- `63ac5dcb` **Darius Wattimena** (2025-02-05): Align api versions of package with the ones used in main
- `5ee9e066` **Darius Wattimena** (2025-02-05): Add client module
- `9cb0816d` **Darius Wattimena** (2025-02-10): Added basic VesselVoyage client to retrieve visits and voyages
- `04c1d997` **Darius Wattimena** (2025-02-10): Added support for getting the SOF by visit id
- `5fa243d1` **Darius Wattimena** (2025-02-10): Code cleanup
- `1a2d111c` **Darius Wattimena** (2025-02-12): Adjusted build.gradle so we don't apply the spring boot tasks that are not needed for a library
- `27ce6832` **Darius Wattimena** (2025-02-12): Added missing V1 client to auto configured beans
- `81f20863` **Darius Wattimena** (2025-02-17): Clean up client code and added type aliases to make calls more explicit

## Reviews

### Darius-Wattimena — COMMENTED (2025-02-17)

_No comment._

### Darius-Wattimena — COMMENTED (2025-02-17)

_No comment._

### leonjoosse — CHANGES_REQUESTED (2025-02-17)

As discussed offline

### Darius-Wattimena — COMMENTED (2025-02-17)

_No comment._

### TeqJoostD — APPROVED (2025-02-18)

_No comment._

### leonjoosse — APPROVED (2025-02-18)

_No comment._

## Review Comments

### leonjoosse — 2025-02-17 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

This response type is quite ugly... I believe I implemented this when starting on the PTO SOF... Should we maybe have a look if we can improve this by reducing the amount of generics? Maybe have some other data classes?

### Darius-Wattimena — 2025-02-17 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

this is wrong

### Darius-Wattimena — 2025-02-17 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

here as well, return type wrong

### Darius-Wattimena — 2025-02-17 on `client/src/main/kotlin/nl/teqplay/vesselvoyage/client/VesselVoyageClient.kt`

Ended up going for the type alias route on the side of the client only, to keep the impact minimal for now. Lets see what others think when they start consuming and use the client.
