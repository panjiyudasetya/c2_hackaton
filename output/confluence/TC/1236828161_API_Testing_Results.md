---
id: confluence:1236828161
source: confluence
type: page
space: TC
title: API Testing Results
author: Joost Laurman
date: '2026-06-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236828161
explicit_links:
- jira:CVE-2012
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236828161
---
# API Testing Results

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236828161  

## Content

Out of 97188 requests, 3 of the requests triggered an alert. Currently none of the tests have been executed with Authorization.

**Alerts**

* Application Error Disclosure

  + GET:https://api.dev.teqplay.com/v3/api-docs/api
  + Information Disclosure - Debug Error Messages

    - This page contains an error/warning message that may disclose sensitive information like the location of the file that produced the unhandled exception. This information can be used to launch further attacks against the web application. The alert could be a false positive if the error message is found inside a documentation page.
* GET:https://api.dev.teqplay.com/v3/api-docs/api

  + User Agent Fuzzer

    - The response appeared to contain common error messages returned by platforms such as <http://ASP.NET> , and Web-servers such as IIS and Apache. You can configure the list of common debug messages.
* POST:https://api.dev.teqplay.com/v1/uab ()({authentication:{apiKey},requests})

  + Attack: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)

    - Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

|  | **Strength** | **Elapsed** | **Reqs** | **Alerts** | **Status** |
| --- | --- | --- | --- | --- | --- |
| Analyser |  | 00:01.122 | 40 |  |  |
|  |  |  |  |  |  |
| **Plugin** |  |  |  |  |  |
| Path Traversal | Medium | 00:16.145 | 8010 | 0 | Completed |
| Remote File Inclusion | Medium | 00:09.168 | 4450 | 0 | Completed |
| Source Code Disclosure - /WEB-INF Folder | Medium | 00:00.054 | 2 | 0 | Completed |
| Remote Code Execution - Shell Shock | Medium | 00:02.692 | 890 | 0 | Completed |
| Heartbleed OpenSSL Vulnerability | Medium | 00:03.239 | 4 | 0 | Completed |
| Source Code Disclosure - CVE-2012-1823 | Medium | 00:03.239 | 0 | 0 | Completed |
| Remote Code Execution - CVE-2012-1823 | Medium | 00:01.754 | 314 | 0 | Completed |
| External Redirect | Medium | 00:08.035 | 4005 | 0 | Completed |
| Server Side Include | Medium | 00:04.103 | 1780 | 0 | Completed |
| Cross Site Scripting (Reflected) | Medium | 00:04.391 | 2225 | 0 | Completed |
| Cross Site Scripting (Persistent) - Prime | Medium | 00:01.993 | 445 | 0 | Completed |
| Cross Site Scripting (Persistent) - Spider | Medium | 00:01.607 | 157 | 0 | Completed |
| Cross Site Scripting (Persistent) | Medium | 00:01.156 | 0 | 0 | Completed |
| SQL Injection | Medium | 00:19.018 | 10131 | 0 | Completed |
| SQL Injection - MySQL (Time Based) | Medium | 00:07.779 | 4450 | 0 | Completed |
| SQL Injection - Hypersonic SQL (Time Based) | Medium | 00:08.395 | 4450 | 0 | Completed |
| SQL Injection - Oracle (Time Based) | Medium | 00:04.009 | 2225 | 0 | Completed |
| SQL Injection - PostgreSQL (Time Based) | Medium | 00:04.113 | 2225 | 0 | Completed |
| SQL Injection - SQLite (Time Based) | Medium | 00:07.697 | 4087 | 0 | Completed |
| Cross Site Scripting (DOM Based) | Medium | 01:48.803 | 0 | 0 | Completed |
| SQL Injection - MsSQL (Time Based) | Medium | 00:08.276 | 4450 | 0 | Completed |
| Log4Shell | Medium | 00:00.002 | 0 | 0 | Skipped, no Active Scan OAST service is selected. |
| Spring4Shell | Medium | 00:02.768 | 312 | 0 | Completed |
| Remote Code Execution (React2Shell) | Medium | 00:00.051 | 1 | 0 | Completed |
| Server Side Code Injection | Medium | 00:12.499 | 3560 | 0 | Completed |
| Remote OS Command Injection | Medium | 00:28.308 | 8455 | 0 | Completed |
| XPath Injection | Medium | 00:06.144 | 1335 | 0 | Completed |
| XML External Entity Attack | Medium | 00:02.133 | 0 | 0 | Completed |
| Generic Padding Oracle | Medium | 00:02.263 | 5 | 0 | Completed |
| Cloud Metadata Potentially Exposed | Medium | 00:00.548 | 9 | 0 | Completed |
| Server Side Template Injection | Medium | 00:23.759 | 6229 | 0 | Completed |
| Server Side Template Injection (Blind) | Medium | 00:25.149 | 5340 | 0 | Completed |
| Remote OS Command Injection (Time Based) | Medium | 00:27.255 | 7120 | 0 | Completed |
| Directory Browsing | Medium | 00:02.536 | 157 | 0 | Completed |
| HTTP Only Site | Medium | 00:00.002 | 0 | 0 | Completed |
| Buffer Overflow | Medium | 00:03.842 | 445 | 0 | Completed |
| Format String Error | Medium | 00:05.625 | 1335 | 0 | Completed |
| CRLF Injection | Medium | 00:10.409 | 3115 | 0 | Completed |
| Parameter Tampering | Medium | 00:03.549 | 445 | 0 | Completed |
| ELMAH Information Leak | Medium | 00:00.050 | 1 | 0 | Completed |
| Trace.axd Information Leak | Medium | 00:02.187 | 64 | 0 | Completed |
| .htaccess Information Leak | Medium | 00:02.250 | 64 | 0 | Completed |
| .env Information Leak | Medium | 00:02.447 | 64 | 0 | Completed |
| Spring Actuator Information Leak | Medium | 00:00.092 | 2 | 0 | Completed |
| Hidden File Finder | Medium | 00:02.581 | 52 | 0 | Completed |
| Exponential Entity Expansion (Billion Laughs Attack) | Medium | 00:02.575 | 0 | 0 | Completed |
| XSLT Injection | Medium | 00:03.906 | 1220 | 0 | Completed |
| HTTPS Content Available via HTTP | Medium | 00:02.162 | 0 | 0 | Completed |
| GET for POST | Medium | 00:02.079 | 0 | 0 | Completed |
| User Agent Fuzzer | Medium | 00:05.388 | 1884 | 185 | Completed |
| Script Active Scan Rules | Medium | 00:00.000 | 0 | 0 | Skipped, no scripts enabled. |
| SOAP Action Spoofing | Medium | 00:01.942 | 0 | 0 | Completed |
| SOAP XML Injection | Medium | 00:01.976 | 0 | 0 | Completed |
|  |  |  |  |  |  |
| **Totals** |  | 07:05.543 | 97188 | 191 |  |