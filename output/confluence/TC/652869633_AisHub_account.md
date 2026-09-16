---
id: confluence:652869633
source: confluence
type: page
space: TC
title: AisHub account
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652869633
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652869633
---
# AisHub account

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652869633  

## Content

Our AIS Receiver is 'donating' data in raw AIS format:

Host: data.aishub.net (144.76.105.244)
UDP port: 2475 / 2548 / 2127 

In return we get:

1. You can receive all other AISHub feeds via TCP at:

Host: data.aishub.net
TCP ports:
- 4548 (used for ais-stream forwarded by aisforwarder.teqplay:12345)
- 4475 (used for ais-stream-dev forwarded by backenddev.teqplay.nl:12345)
- 4127 (spare, used by aisdata until it is shutdown)

Old situation to be removed:

Host: data.aishub.net
TCP port: 4475 (used for aisdatadev) / 4548 (used for aisdata)/ 4127 (spare for backenddev experiments)

2. You can use our XML/JSON webservice (<http://www.aishub.net/xml-description.html>). There are two accounts.

The webservice account used by the teqplay live platform is:

AH\_2475\_39D649E3 !!! Do not use this account for development, only for live!!!

the following account can be used for development purposes:

AH\_2548\_83A94351

And the last one for development purposes:

AH\_2127\_078D713E

3. The same account is valid for AISHub version of VT Explorer (<http://www.aishub.net/vt-explorer-download.html>) and Apple/Android VT Explorer apps.
4. Your AIS data is also displayed at <http://www.vesselfinder.com>

# Cofano AIS Account

Cofano has a number of transponders in the field, which are covering some open spots in AIS Hub. We have access to their feed via:

#!python
https://ais.watch/teqplay/

Login: teqplay

Password: oaOKMyN8JVeBAav5gkd1

These basic Auth credentials can also be used to retrieve the service information from:

#!java
https://ais.watch/teqplay/index.php?actuals

Updated 2017-03-20