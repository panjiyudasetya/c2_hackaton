---
id: confluence:374210563
source: confluence
type: page
space: TC
title: Tigera Operator Calico
author: Minh Trang Nguyen (Unlicensed)
date: '2024-06-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/374210563
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/374210563
---
# Tigera Operator Calico

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/374210563  

## Content

In a Kubernetes cluster, daemonsets are responsible for installing pods on all nodes. However, this cluster also utilizes Fargate nodes, which possess taints that prohibit pod installation. To circumvent this, it's necessary to instruct the Tigera operator to prevent the CSI Node Driver from being installed on the Fargate node. Detailed instructions on how to implement these changes can be found in the installation reference section of the Calico Documentation.

<https://docs.tigera.io/calico/latest/reference/installation/api#operator.tigera.io/v1.CSINodeDriverDaemonSet>

The following code snippet instructs the Tigera Operator to avoid scheduling on Fargate nodes by patching the installation. Simply copy and paste it into your terminal to execute.

widekubectl patch -n tigera-operator installations.operator.tigera.io default --type='merge' -p '{
"spec": {
"csiNodeDriverDaemonSet": {
"spec": {
"template": {
"spec": {
"affinity": {
"nodeAffinity": {
"requiredDuringSchedulingIgnoredDuringExecution": {
"nodeSelectorTerms": [
{
"matchExpressions": [
{
"key": "eks.amazonaws.com/compute-type",
"operator": "NotIn",
"values": [
"fargate"
]
}
]
}
]
}
}
}
}
}
}
}
}
}'