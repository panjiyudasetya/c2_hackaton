---
id: confluence:1236631554
source: confluence
type: page
space: TC
title: API Testing Tools
author: Joost Laurman
date: '2026-06-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236631554
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236631554
---
# API Testing Tools

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1236631554  

## Content

Two tests have been conducted, with similar tools. The first one is Burp Suite Professional and the second one OWASP ZAP.

| **Feature** | **Burp Suite Professional** | **OWASP ZAP** |
| --- | --- | --- |
| Cost | Paid license ($500) | Free |

**Requirements:**

* Endpoints known in swagger docs
* Pen tests with no auth
* Test without VPN access

**Later steps:**

* Pen tests with with auth / roles
* Test with VPN access

Both tools have a big default test suite. In Burp Suite the default test executed 47006 requests, while ZAP executed 97188 requests.

**Burp Suite Professional** performs active and passive DAST (Dynamic Application Security Testing) testing, combining payload-based vulnerability exploitation attempts with response analysis to identify server-side, client-side, authentication, authorization, configuration, and business-logic security weaknesses.

**ZAP** actively tests a web application for vulnerabilities such as SQL Injection, Cross-Site Scripting (XSS), Remote Code Execution, Command Injection, Path Traversal, Server-Side Template Injection, XXE, and information disclosure by injecting attack payloads into application inputs and evaluating the responses.

| Tool | Scan Coverage |
| --- | --- |
| **OWASP ZAP** | Focuses primarily on automated active scanning for common web application vulnerabilities such as SQLi, XSS, XXE, SSRF, RCE, SSTI, and information disclosure. |
| **Burp Suite Professional** | Provides a broader DAST platform with active and passive scanning, including advanced checks for access control, JWT security, HTTP smuggling, cache poisoning, client-side vulnerabilities, CSP weaknesses, GraphQL issues, deserialization flaws, and modern web framework vulnerabilities. |

Both tools perform DAST, but Burp Suite offers a larger and more frequently updated vulnerability rule set, deeper client-side analysis, and more advanced testing for modern web technologies, while ZAP focuses on comprehensive coverage of the most common web application vulnerabilities.

At our current mindset I think ZAP should be enough. It’s open source, community supported and can also be integrated into our CI/CD tools.