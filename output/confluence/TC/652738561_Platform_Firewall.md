---
id: confluence:652738561
source: confluence
type: page
space: TC
title: Platform Firewall
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738561
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738561
---
# Platform Firewall

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652738561  

## Content

The platform runs in Tomcat using a non-privileged user, and listens on ports 9090 and 9091 for http and https connections, respectively. To allow normal access, port forwarding rules are configured in the Linux firewall. These rules are contained in `/etc/rc.firewall`, and executed from `/etc/rc.local`. This mechanism was chosen over `iptables-save`/`iptables-restore` as this allows documentation in the form of comments in the firewall scripts.

The `/etc/rc.firewall` script contains comments explaining the specifics of the rules. If you want to add or modify a rule, all you need to do is edit this script, and run it.

To view the current firewall rules, use `sudo iptables -vL` for the `filter` table (this one should be empty), and `sudo iptables -vL -t nat` for the `nat` table (this one contains the port forwarding rules).