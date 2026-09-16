---
id: confluence:189464585
source: confluence
type: page
space: TC
title: PortReporter monitor enriching - "Richie"
author: Former user (Deleted)
date: '2023-06-09'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/189464585
explicit_links: []
---
# PortReporter monitor enriching - "Richie"

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/189464585  

## Content

1. `portreporter-monitor` receives an event from the event-stream
2. `portreporter-monitor` converts the event into a converted event
3. `portreporter-monitor` uses NATS request/reply to request metadata information from SmartFleet & Portcall+, using the converted event:

   1. *SmartFleet:* returns fleet metadata of the ship that the event is about
   2. *Portcall+:* returns portcall identifier(s), if known
4. `portreporter-monitor` publishes the converted event + metadata (SF/PC+) into the event-stream  
   *(using a* `messageId` *for deduplication)*
5. `portreporter-monitor` acknowledges the original event  
   *(not acknowledging when not published finished event, so retries are handled by the event-stream consumer of* `portreporter-monitor`*)*