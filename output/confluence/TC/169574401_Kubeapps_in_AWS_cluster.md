---
id: confluence:169574401
source: confluence
type: page
space: TC
title: Kubeapps in AWS cluster
author: Minh Trang Nguyen (Unlicensed)
date: '2023-03-01'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/169574401
explicit_links: []
---
# Kubeapps in AWS cluster

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/169574401  

## Content

Kubeapps is a web based UI application for managing applications on Kubernetes clusters.

**EKS cluster**

It’s mandatory to associate an OIDC identity provider. In the case of Teqplay the provider Keycloak is being used. By associating with Keycloak, Kubernetes can map the access token to the Kubernetes authorisation (RBAC) system. See picture 1 for an example for how to create the association.

**picture 1**: associate OIDC identity provider

**Permissions**

For the cluster two roles are used, these are “Administrators” and “Developers“. The first role is based on the cluster level and the second one is only for a single namespace.

* kubeapps:cluster:role:admin
* kubeapps:role:admin

**kubeapps:cluster:role:admin**

These are the permissions the Kubeapps application is allowed to use on a cluster level. Users with this role can create, update and remove applications.

**kubeapps:role:admin**

For a single namespace, this role tells the cluster if the user is allowed to access and can make changes to applications:

For Kubeapps two role bindings are created per namespace.

**kubeapps:rolebinding:admin**

This role binding has access to the following namespaces.

* brokers
* kubeapps
* monitoring
* students
* teqplay-app
* vaultwarden
* velero
* keycloak

**kubeapps:rolebinding:developer**

This role binding has access to the following namespaces.

* brokers
* teqplay-app

**Keycloak groups**

In Keycloak create users and add them to a group. Two groups are available “kubeapps-support” and “kubeapps-developer”. See picture 2 how the user can join a group.

**Picture 2:** join a group in Keycloak