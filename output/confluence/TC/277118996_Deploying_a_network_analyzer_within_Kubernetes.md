---
id: confluence:277118996
source: confluence
type: page
space: TC
title: Deploying a network analyzer within Kubernetes
author: Minh Trang Nguyen (Unlicensed)
date: '2024-02-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/277118996
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/277118996
---
# Deploying a network analyzer within Kubernetes

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/277118996  

## Content

To identify the ports utilized within a Kubernetes Pod, employing a network analyzer proves invaluable. This document outlines the procedures for configuring a network analyzer to be used in the cluster.

Requirements:

* Wireshark, needs to be available in the terminal path.
* Krew
* Ksniff

**Install wireshark**

<https://www.wireshark.org/download.html>

When installing the package, opt to add Wireshark to the system path using the provided option.

**Install krew**

<https://krew.sigs.k8s.io/docs/user-guide/setup/install/>

**Install ksniff**

<https://github.com/eldadru/ksniff>

**Linux users:**

On Linux you need to have permissions to run /usr/bin/dumpcap, add your user to the “wireshark” group.

sudo usermod -aG wireshark $USER

**Run the network analyzer**

kubectl sniff -p <POD NAME>

Example:

Wireshare will start running and network

kubectl sniff -p external-dns-dev-75b998d44b-kld9z
INFO[0000] no container specified, taking first container we found in pod.
INFO[0000] selected container: 'external-dns'
INFO[0000] sniffing method: privileged pod
INFO[0000] sniffing on pod: 'external-dns-dev-75b998d44b-kld9z' [namespace: 'external-dns', container: 'external-dns', filter: '', interface: 'any']
INFO[0000] creating privileged pod on node: 'ip-172-31-28-182.eu-west-1.compute.internal'
INFO[0000] pod: 'ksniff-j7pqp' created successfully in namespace: 'external-dns'
INFO[0000] waiting for pod successful startup
INFO[0001] pod: 'ksniff-j7pqp' created successfully on node: 'ip-172-31-28-182.eu-west-1.compute.internal'
INFO[0001] spawning wireshark!
INFO[0001] starting remote sniffing using privileged pod
INFO[0001] executing command: '[/bin/sh -c
set -ex
export CONTAINERD\_SOCKET="/run/containerd/containerd.sock"
export CONTAINERD\_NAMESPACE="k8s.io"
export CONTAINER\_RUNTIME\_ENDPOINT="unix:///host${CONTAINERD\_SOCKET}"
export IMAGE\_SERVICE\_ENDPOINT=${CONTAINER\_RUNTIME\_ENDPOINT}
crictl pull docker.io/maintained/tcpdump:latest >/dev/null
netns=$(crictl inspect 77b6e7cc8109a1b0554eb128cc2e8df3c1ba6b272e6d843e151fc55c6866707a | jq '.info.runtimeSpec.linux.namespaces[] | select(.type == "network") | .path' | tr -d '"')
exec chroot /host ctr -a ${CONTAINERD\_SOCKET} run --rm --with-ns "network:${netns}" docker.io/maintained/tcpdump:latest ksniff-container-cQdiigor tcpdump -i any -U -w -
]' on container: 'ksniff-privileged', pod: 'ksniff-j7pqp', namespace: 'external-dns' 

Once the data analysis is complete, proceed to remove the sniffer pod from the cluster.

ksniff-j7pqp 1/1 Running 0 3m59s