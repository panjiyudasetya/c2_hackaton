---
id: confluence:652345355
source: confluence
type: page
space: TC
title: Install SSL certificate on EC2 servers
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652345355
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652345355
---
# Install SSL certificate on EC2 servers

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652345355  

## Content

Firstly, download the SSL certificate to the filesystem.

`/usr/bin/openssl s_client -connect www.vts-scheldt.net:443`

Copy everything from -----BEGIN CERTIFICATE----- and -----END CERTIFICATE----- (Don't forget to also include the BEGIN and END part) to a file, e.g. `vts-scheldt.cer`

On a EC2 server look at `/usr/lib/jvm/java-11-openjdk-amd64/lib/security` to see which cacerts file is used.

ubuntu@backendpronto:~$ cd /usr/lib/jvm/java-11-openjdk-amd64/lib/security/
ubuntu@backendpronto:/usr/lib/jvm/java-11-openjdk-amd64/lib/security$ ls -la
total 8
drwxr-xr-x 2 root root 4096 Apr 30 2021 .
drwxr-xr-x 6 root root 4096 Apr 30 2021 ..
lrwxrwxrwx 1 root root 47 Apr 21 2021 blacklisted.certs -> /etc/java-11-openjdk/security/blacklisted.certs
lrwxrwxrwx 1 root root 27 Apr 21 2021 cacerts -> /etc/ssl/certs/java/cacerts
lrwxrwxrwx 1 root root 44 Apr 21 2021 default.policy -> /etc/java-11-openjdk/security/default.policy
lrwxrwxrwx 1 root root 52 Apr 21 2021 public\_suffix\_list.dat -> /etc/java-11-openjdk/security/public\_suffix\_list.dat

As you can see in this example, the cacerts file is located in `/etc/ssl/certs/java/cacerts`

With the keytool, import to that file.

`sudo keytool -importcert -trustcacerts -file ~/vts-scheldt.cer -alias vts-scheldt.net -keystore /etc/ssl/certs/java/cacerts`

If it's asked for a password use `changeit`, as that is the default password for this file.

Now it's imported and ready to go. Do a restart of tomcat to make sure the changes are used.