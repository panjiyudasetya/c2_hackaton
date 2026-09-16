---
id: jira:TCC-24
source: jira
type: issue
key: TCC-24
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Pim van den Toorn
labels: []
components: []
title: Address issues with API-Dev not being available after spring boot update
author: Richard van Klaveren
status: Done
date: '2025-05-12'
url: https://teqplaybv.atlassian.net/browse/TCC-24
explicit_links:
- jira:TCC-152
---
# [TCC-24] Address issues with API-Dev not being available after spring boot update

**URL:** https://teqplaybv.atlassian.net/browse/TCC-24  
**Type:** Bug | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Pim van den Toorn  
**Created:** 2025-05-12 | **Updated:** 2025-06-02  
**Board:** TCC board  
**Parent:** [TCC-152] Production Issues  

## Description

_No description._

## Comments

### Pim van den Toorn — 2025-05-12

Swagger already working; RestTemplate.getForObject is now blocking, which is prohibited in webflux threads, this might also be the issue with other things.

### Pim van den Toorn — 2025-05-22

API uses the Skeleton PomaInfrastructureClient, which is RestTemplate based. I’m writing a webclient version, which first needs a webclient version of the keycloak client

### Pim van den Toorn — 2025-05-26

Nevermind on the webclient version, in the controller in api, I’ve encapsulated the calls to the area service in Monos:


{noformat}@GetMapping("/area/polygon")
fun areasByPolygon(
    @RequestParam type: String,
): Mono<Map<String, List<List<Double>>>> =
    Mono.fromCallable {
        areaService.getAreas(type)
    }.subscribeOn(Schedulers.boundedElastic()){noformat}

The boundedElastic scheduler makes it so the {{areaService.getAreas}} can do blocking calls.

### Pim van den Toorn — 2025-05-27

Currently merged with dev and deployed. Tested myself and merged as it’s a small fix

### Pim van den Toorn — 2025-05-28

You can test it by calling the endpoints in {{PlatformUnsupportedEndpointController}}, like:
[{color:#ffffff}https://internalapidev.teqplay.dev/v0/area/polygon?type=TERMINAL{color}|https://internalapidev.teqplay.dev/v0/area/polygon?type=TERMINAL] or

[{color:#ffffff}https://internalapidev.teqplay.dev/v0/area/nlrtm{color}|https://internalapidev.teqplay.dev/v0/area/nlrtm]

### Darius Wattimena — 2025-05-28

Seem to work nicely, can be deployed to prod
