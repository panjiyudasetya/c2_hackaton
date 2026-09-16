---
id: confluence:651886595
source: confluence
type: page
space: TC
title: Security Standards
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651886595
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651886595
---
# Security Standards

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651886595  

## Content

This document describes what are the preferred ways to handle security related subjects

| Situation | Local | in Dev | in Live | What is the preferred way |
| --- | --- | --- | --- | --- |
| Storing passwords in a config file |  |  |  | Store these variables in a file on the server that overrides the config or use environment variables |
| Use 2FA whenever possible |  |  |  |  |
| Use ssh keys to login to servers |  |  |  | Highly preferred to put a password on that key |
| Logging passwords |  |  |  | This is a high security risk due to the logs staying available |
| Committing passwords to git |  |  |  | When doing this consider changing the password that is committed |
| Use of basic auth to login |  |  |  | This is an option but it is preferred to use the authenticator or a m2m solution |
| Put databases behind a vpn |  |  |  | Databases should only be reachable internally and should not need an external connection |
| Enforce https |  |  |  | http only for develop purposes but not in production |