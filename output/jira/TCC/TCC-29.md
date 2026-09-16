---
id: jira:TCC-29
source: jira
type: issue
key: TCC-29
project: TCC
board: TCC board
issuetype: Bug
priority: Medium
assignee: Pim van den Toorn
labels: []
components: []
title: POMA returning berths outside the port I am looking for
author: Richard van Klaveren
status: Done
date: '2025-03-25'
url: https://teqplaybv.atlassian.net/browse/TCC-29
explicit_links:
- jira:TCC-152
---
# [TCC-29] POMA returning berths outside the port I am looking for

**URL:** https://teqplaybv.atlassian.net/browse/TCC-29  
**Type:** Bug | **Status:** Done | **Priority:** Medium  
**Reporter:** Richard van Klaveren | **Assignee:** Pim van den Toorn  
**Created:** 2025-03-25 | **Updated:** 2025-06-06  
**Board:** TCC board  
**Parent:** [TCC-152] Production Issues  

## Description

I'm having an issue in PortcallPlus when searching for berths in the new CorpusChristiService.
The results of searching for {{BUCKEYE #1}} is the following berth list:
{{BUCKEYE BERTH (PERTH AMBOY), BUCKEYE #1, BUCKEYE #3, NORTH P READING, BERTH 3 - SOUTH (BARGE), DOCK NO. 1 (BARGES), BUCKEYE #2, BUCKEYE #5, HESS BERTH 1 (BAYONNE), ROSETON BERTH, SOUTH TEXAS #1, SOUTH TEXAS #2, BUCKEYE #4, BERTH 1, OIL SOUTH PORTLAND, OIL DELAIR NORTH, OIL DELAIR SOUTH, BUCKEYE(EX OIL HEWITT), BUCKEYE CINCINNATI DOCK, OIL BUCKEYE BERTH, CURTIS BAY, OIL BARGE BERTH, BERTH NO. 1, FREEPORT BUNKERING (BUCKEYE/BORCO), HESS ROSETON DOCK, OIL DOCK, HESS OIL (EX OIL HESS CHESAPEAKE), BUCKEYE MONEY POINT BARGE DOCK, BUCKEYE DOCK 1, MAIN DOCK (EX - BUCKEYE CARIBBEAN), SMALL TANKER DOCK}}
Whereas I was expecting a nice match, as I searched by the exact name, it didn't.


Let’s make sure the search will:

# only provide results in the requested port
# Include a queryParam ‘onlyExactMatches’, returning only 1 value iff it can be found

## Comments

### Pim van den Toorn — 2025-05-06

POMA seems to work as intended, when searching for “BUCKEYE #1” in USCRP, I’m only getting the exact berth. Also the CorpusChristiService in portcallplus has been updated by Joaquin in the meantime, and it should just return 1 berth, in the correct port.

Let me know if you still see the issue [~accountid:557058:0ffdaf08-199c-4b89-afe7-ac0306e26b29]

### Richard van Klaveren — 2025-05-06

[~accountid:60dd67bcad9bba006a9b4d74] Could you please share with Pim which call you did on Poma that did not work? If I remember well, you made the ‘quick-fix on portcall+ side’, right?

### Joaquin Marquez Bugella — 2025-05-08

Yes, with pleasure!
[~accountid:63e224de8978d7a4353c94ca] , I had to do do this _not-so-nice_ method to find a berth by its exact name:
[https://github.com/teqplay/portcallplus/blob/e3db4da9d9e747842f6d8f743db3c75c51fe3e0a/src/main/kotlin/nl/teqplay/portcallplus/service/external/CorpusChristiService.kt#L285|https://github.com/teqplay/portcallplus/blob/e3db4da9d9e747842f6d8f743db3c75c51fe3e0a/src/main/kotlin/nl/teqplay/portcallplus/service/external/CorpusChristiService.kt#L285] 

{noformat}...
  private fun String.findPomaBerth(): Berth? {
      return pomaService
          .getBerths(this, IDPREFIX_USCRP)
          .also {
              log.debug { "Returned ${it.size} berths when searching for $this." }
              log.debug { "Names: ${it.joinToString(", ") { it.name }}" }
          }.firstOrNull { it.name.equals(this, true) }
  }
...{noformat}

Point is that {{pomaService.getBerths("BUCKEYE #1", "USCRP")}}, got the berth list (in that order) in the description (listing only the names):

# BUCKEYE BERTH (PERTH AMBOY),
# *BUCKEYE #1     <----- I aimed for this!*
# BUCKEYE #3
# NORTH P READING
# BERTH 3 - SOUTH (BARGE)
# DOCK NO. 1 (BARGES)
# BUCKEYE #2
# BUCKEYE #5
# HESS BERTH 1 (BAYONNE)
# ROSETON BERTH
# SOUTH TEXAS #1
# SOUTH TEXAS #2
# BUCKEYE #4
# BERTH 1
# OIL SOUTH PORTLAND
# OIL DELAIR NORTH
# OIL DELAIR SOUTH
# BUCKEYE(EX OIL HEWITT)
# BUCKEYE CINCINNATI DOCK
# OIL BUCKEYE BERTH
# CURTIS BAY
# OIL BARGE BERTH
# BERTH NO. 1
# FREEPORT BUNKERING (BUCKEYE/BORCO)
# HESS ROSETON DOCK
# OIL DOCK
# HESS OIL (EX OIL HESS CHESAPEAKE)
# BUCKEYE MONEY POINT BARGE DOCK
# BUCKEYE DOCK 1
# MAIN DOCK (EX - BUCKEYE CARIBBEAN)
# SMALL TANKER DOCK

Whereas the result is in the list, it’s in the second place…. 🤷‍♂️.

Additionally, there are many results that I don’t know why they are included, i.e. _NORTH P READING_, _BERTH 3 - SOUTH (BARGE)_ and quite some more.

### Pim van den Toorn — 2025-05-27

This issue is due to the '#' being a fragment character in a url, referring to an element in a page. With our current setup of the RestTemplate in skeleton, when it does url encoding, it does not encode the # to %23, but it leaves it in. See the chatgpt answer:

{quote}This issue is due to how URLs are defined: the # character starts a fragment identifier, and anything after it is not sent to the server. This is a browser and HTTP standard behavior, not something you can change on the server side (Spring Boot or any backend).

Solution:
Clients must URL-encode the # character as %23 in query parameters. The server cannot receive anything after a # in the URL, as it is never transmitted.

Summary:

The server cannot fix or read # as a regular character if it is not encoded.
The client must encode # as %23 in the request.{quote}



I made a quick fix for PortcallPlus that replaces the # with %23 after the other encoding is done, but this should just be fixed in Skeleton, see [Github fix # branch|https://github.com/teqplay/portcallplus/tree/fix/fix-%23-not-getting-encoded-for-poma-searches]:


{noformat}    @PostConstruct
    fun encapsulateRestTemplateUriHandler() {
        try {
            // Get the RestTemplate from the client via reflection
            val field = pomaClient.javaClass.getDeclaredField("restTemplate")
            field.isAccessible = true
            val restTemplate = field.get(pomaClient) as RestTemplate

            // Get the original handler
            val originalHandler = restTemplate.uriTemplateHandler

            // Create a proxy UriTemplateHandler that wraps the original one and replaces # with %23
            val proxyHandler = object : org.springframework.web.util.UriTemplateHandler {
                override fun expand(uriTemplate: String, uriVariables: Map<String, *>): URI {
                    return originalHandler
                        .expand(uriTemplate, uriVariables)
                        .toString()
                        .replace("#", "%23")
                        .let {
                            URI(it)
                        }
                }

                override fun expand(uriTemplate: String, vararg uriVariables: Any): URI {
                    return originalHandler
                        .expand(uriTemplate, uriVariables)
                        .toString()
                        .replace("#", "%23")
                        .let {
                            URI(it)
                        }
                }
            }

            // Replace the URI handler with our proxy
            restTemplate.uriTemplateHandler = proxyHandler

            log.info("Successfully replaced URL handling to properly encode # characters")
        } catch (e: Exception) {
            log.error(e, "Failed to replace URL handling: ${e.message}")
        }
    }{noformat}
