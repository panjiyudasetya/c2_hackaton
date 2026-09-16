---
id: confluence:426180626
source: confluence
type: page
space: TC
title: 'BICS: upgrade process'
author: Joost Laurman
date: '2024-08-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/426180626
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/426180626
---
# BICS: upgrade process

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/426180626  

## Content

Steps for upgrading BICS from 5.6.2 to 5.6.8

Upgrading BICS to newest version is not possible in one go. First you need to upgrade to 5.6.8 and from there you can upgrade to the latest version.

1. VNC into the BICS windows machine  
   (Might take SSHing into the machine, starting vncserver :1 and user TigerVNC to VNC into the machine)
2. On this machine, download BICS 5.6.8.  
   ([https://hs.bics.nl/bics2-application/5.6.8/](https://hs.bics.nl/bics2-application/5.6.8/)))
3. Install dependency needed:   
   `sudo apt install libncurses5`

3. Make BICS installer executable   
   `chmod +x BICS.bin`
4. Execute the installer (with `-DTEST=true` parameter if acceptance)
5. It will open the installer and it will tell you it has found an  
   existing installation of BICS and it will try to upgrade this one.
6. Make sure there is enough space available
7. Installer is running and will upgrade the environment to 5.6.8