---
id: confluence:196902913
source: confluence
type: page
space: TC
title: Configuring Kubernetes Access and Cluster Policies for Users
author: Jamie de Leest
date: '2026-03-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/196902913
explicit_links: []
---
# Configuring Kubernetes Access and Cluster Policies for Users

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/196902913  

## Content

**Status: ready**

This is a proposal how to access the EKS cluster `develop` or `production`.

All user actions within the Kubernetes clusters must be logged and traceable. Access to the clusters is granted through Keycloak as the identity provider. To obtain access, a Keycloak account is necessary. Please consult the administrator to request an account.

## Multi-factor authentication

Before accessing the Kubernetes cluster, OTP authentication must be enabled in Keycloak. The administrator can configure this on a per-user basis through the Keycloak admin control panel.

## Steps to set up access to Kubernetes cluster

A setting up guide to k8s access can be found here: <https://teqplaybv.atlassian.net/wiki/x/AoC6RQ>

## Possible issue: accidentally closing login screen

When unable to log in via the browser due to accidentally closing the login screen, a waiting period of up to 3 minutes may ensue before attempting to log in again. This delay is attributable to the authentication timeout. However, this timeout duration can be adjusted to a shorter interval. If login can be achieved within 30 seconds, consider modifying the settings as outlined below:

Example DEVELOP settings:

wide760kubectl config set-credentials keycloak-dev \
--exec-api-version=client.authentication.k8s.io/v1beta1 \
--exec-command=kubelogin \
--exec-arg=get-token \
--exec-arg=--oidc-issuer-url=https://keycloakdev.teqplay.nl/auth/realms/kubeapps \
--exec-arg=--oidc-client-id=kubeapps \
--exec-arg=--oidc-client-secret=<AVAILABLE IN BITWARDEN UNDER oidc-client-secret (DEVELOP)> \
--exec-arg=--authentication-timeout-sec=30

Alternatively, you have the option to manually edit the Kubernetes configuration file.

wide760- name: keycloak-dev
user:
exec:
apiVersion: client.authentication.k8s.io/v1beta1
args:
- oidc-login
- get-token
- --oidc-issuer-url=https://keycloakdev.teqplay.nl/auth/realms/kubeapps
- --oidc-client-id=kubeapps
- --oidc-client-secret=<AVAILABLE IN BITWARDEN UNDER oidc-client-secret (DEVELOP)>
- --authentication-timeout-sec=30
command: kubectl
env: null
interactiveMode: IfAvailable
provideClusterInfo: false

## Possible issue: 502 Bad Gateway error

When you are trying to log in, a 502 Bad Gateway error could pop up instead of the Keycloak sign-in page. It might help to delete the cookies of that webpage.

**Chrome:**

1. F12 or right-click → inspect
2. Application
3. Cookies
4. right-click https://keycloakdev.teqplay.nl/ → Clear

## Lens software

Utilizing a desktop application for accessing Kubernetes clusters may encounter issues with older versions. It is recommended to consistently use the latest version to ensure optimal compatibility and functionality.

## Switch user

When the user has access to multiple user accounts, it’s possible to switch to another user via the command. This could be the case when the user has an Keycloak and AWS account.

wide760kubectl config set-context develop --user=<USER>
# example: the keycloak user for cluster develop
kubectl config set-context develop --user=keycloak-dev

## Switch between DEVELOP and PRODUCTION cluster CLI

wide760# Go to DEVELOP cluster
kubectl config use-context develop
kubectl get po
# Go to PRODUCTION cluster
kubectl config use-context production

## Fallback Access Strategy for Clusters During Keycloak Outages

**status:** work in progress, it’s only available for users in IAM Identity Center

In the event that Keycloak becomes unavailable due to downtime, access tokens for the clusters will remain valid until their expiration. To ensure continued access to the clusters, utilizing the AWS account serves as an alternative method. This option is specifically available for the "administrators" and "tech-support" groups during Keycloak outages. To facilitate access under these circumstances, please adhere to the following steps.

**Step 1: login into AWS access portal**

Navigate to the URL <https://teqplay.awsapps.com/start> and sign in using your IAM Identity Center account credentials. Once logged in, click on the link labeled “Access keys”.

Select the "Copy" button to copy the credentials into your clipboard as environment variables.

**Step 2: open terminal and paste the credentials**

Enter the credentials into the terminal and press Enter.

**Step 3: setup Kubernetes context**

To configure access for both the `develop` and `production` environments, please adhere to the instructions provided below. Note that this setup is required only once for each environment.

Develop

wide760aws eks update-kubeconfig --name develop --region eu-west-1 --user-alias aws-account-develop

Production

wide760aws eks update-kubeconfig --name production --region eu-west-1 --user-alias aws-account-production

Once the context is established, switching to a different context can be seamlessly achieved as demonstrated below.

Develop

wide760kubectl config use-context aws-account-develop

Production

wide760kubectl config use-context aws-account-production

**Step 4: switch back to Keycloak context**

To revert to Keycloak authentication, execute the following commands:

Develop

wide760kubectl config use-context develop

Production

wide760kubectl config use-context production

## Kubernetes audit log

Owing to the utilization of Keycloak as an identity provider, all Kubernetes cluster-related actions are meticulously logged. Actions are identified by email address and stored in AWS CloudWatch. The relevant log groups include `/aws/eks/develop/cluster` and `/aws/eks/production/cluster`.

Executing sensitive actions, such as creating or deleting network policies, may prompt an alert.

## Keycloak groups

Different groups are available to access the cluster.

* developer: backend and frontend developers
* techsupport: tech support
* devops: maintenance and develop cluster applications
* students: only specific for students
* readonly: users who only needs read only access

In addition to the default groups, users can be added to extra groups that grant access to specific namespaces. These additional groups include ais-core, ais-processing, brokers, portcall, voyage, core-service, general-service, customer-apps, bunkerplanner, and teqplay-api.

### Resource permissions

The table shows the groups which are allowed to access the Kubernetes API resources.

| **Resources** | **devops** | **techsupport** | **developer** | **students** | **readonly** |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |
| **Workload** |  |  |  |  |  |
| Pod | x | x | x | x | x |
| PodTemplate | x |  | x | x | x |
| ReplicationController | x |  | x | x | x |
| ReplicaSet | x | x | x | x | x |
| Deployment | x | x | x | x | x |
| StatefulSet | x | x | x | x | x |
| ControllerRevision | x |  | x | x | x |
| DaemonSet | x | x | x | x | x |
| Job | x | x | x | x | x |
| CronJob | x | x | x | x | x |
| HorizontalPodAutoscaler | x |  | x | x | x |
| PriorityClass | x |  | x | x | x |
| Namespaces | x | x | x | x | x |
|  |  |  |  |  |  |
| **Service** |  |  |  |  |  |
| Service | x | x | x | x | x |
| Endpoints | x | x | x | x | x |
| EndpointSlice | x | x | x | x | x |
| Ingress | x | x | x | x | x |
| IngressClass | x |  | x | x | x |
|  |  |  |  |  |  |
| **Config and Storage** |  |  |  |  |  |
| ConfigMap | x | x | x | x | x |
| Secret | x | x | x | x | x |
| PersistentVolumeClaim | x |  | x | x | x |
| PersistentVolume | x | x | x | x | x |
| StorageClass | x | x | x | x | x |
| VolumeAttachment | x | x | x | x | x |
| CSIDriver |  |  |  |  |  |
| CSINode |  |  |  |  |  |
| CSIStorageCapacity |  |  |  |  |  |
|  |  |  |  |  |  |
| **Authentication** |  |  |  |  |  |
| ServiceAccount | x | x | x | x | x |
| TokenRequest | x |  |  |  | x |
| TokenReview |  |  |  |  |  |
| CertificateSigningRequest |  |  |  |  |  |
|  |  |  |  |  |  |
| **Authorization** |  |  |  |  |  |
| ClusterRole | x | x |  | x | x |
| ClusterRoleBinding | x | x |  | x | x |
| Role | x | x |  | x | x |
| RoleBinding | x | x |  | x | x |
|  |  |  |  |  |  |
| **Policy** |  |  |  |  |  |
| LimitRange | x | x | x | x | x |
| ResourceQuota | x | x | x | x | x |
| NetworkPolicy | x | x | x | x | x |
| PodDisruptionBudget | x | x | x | x | x |
|  |  |  |  |  |  |
| **Extend** |  |  |  |  |  |
| CustomResourceDefinition | x |  |  |  | x |
|  |  |  |  |  |  |

Not all actions are displayed in the table. The verbs like `impersonate` or `userextras` are not used, because only the actions which are used are displayed.

#### Actions - devops

| **Resources** | **get** | **list** | **watch** | **create** | **update** | **patch** | **delete** |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
| **Workload** |  |  |  |  |  |  |  |
| Pod | x | x | x | x | x | x | x |
| PodTemplate | x | x | x | x | x | x | x |
| ReplicationController | x | x | x | x | x | x | x |
| ReplicaSet | x | x | x | x | x | x | x |
| Deployment | x | x | x | x | x | x | x |
| StatefulSet | x | x | x | x | x | x | x |
| ControllerRevision | x | x | x | x | x | x | x |
| DaemonSet | x | x | x | x | x | x | x |
| Job | x | x | x | x | x | x | x |
| CronJob | x | x | x | x | x | x | x |
| HorizontalPodAutoscaler | x | x | x | x | x | x | x |
| PriorityClass | x | x | x | x | x | x | x |
| Namespaces | x | x | x | x | x | x | x |
|  |  |  |  |  |  |  |  |
| **Service** |  |  |  |  |  |  |  |
| Service | x | x | x | x | x | x | x |
| Endpoints | x | x | x | x | x | x | x |
| EndpointSlice | x | x | x | x | x | x | x |
| Ingress | x | x | x | x | x | x | x |
| IngressClass | x | x | x | x | x | x | x |
|  |  |  |  |  |  |  |  |
| **Config and Storage** |  |  |  |  |  |  |  |
| ConfigMap | x | x | x | x | x | x | x |
| Secret | x | x | x | x | x | x | x |
| PersistentVolumeClaim | x | x | x | x | x | x | x |
| PersistentVolume | x | x | x | x | x | x | x |
| StorageClass | x | x | x | x | x | x | x |
| VolumeAttachment | x | x | x | x | x | x | x |
| CSIDriver | x | x | x | x | x | x | x |
| CSINode | x | x | x | x | x | x | x |
| CSIStorageCapacity | x | x | x | x | x | x | x |
|  |  |  |  |  |  |  |  |
| **Authentication** |  |  |  |  |  |  |  |
| ServiceAccount | x | x | x | x | x | x | x |
| TokenRequest | x | x | x | x | x | x | x |
| TokenReview | x | x | x | x | x | x | x |
| CertificateSigningRequest | x | x | x | x | x | x | x |
|  |  |  |  |  |  |  |  |
| **Authorization** |  |  |  |  |  |  |  |
| ClusterRole | x | x | x | x | x | x | x |
| ClusterRoleBinding | x | x | x | x | x | x | x |
| Role | x | x | x | x | x | x | x |
| RoleBinding | x | x | x | x | x | x | x |
|  |  |  |  |  |  |  |  |
| **Policy** |  |  |  |  |  |  |  |
| LimitRange | x | x | x | x | x | x | x |
| ResourceQuota | x | x | x | x | x | x | x |
| NetworkPolicy | x | x | x | x | x | x | x |
| PodDisruptionBudget | x | x | x | x | x | x | x |
|  |  |  |  |  |  |  |  |
| **Extend** |  |  |  |  |  |  |  |
| CustomResourceDefinition | x | x | x | x | x | x | x |

#### Actions - **techsupport**

| **Resources** | **get** | **list** | **watch** | **create** | **update** | **patch** | **delete** |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
| **Workload** |  |  |  |  |  |  |  |
| Pod | x | x | x | x | x | x | x |
| PodTemplate |  |  |  |  |  |  |  |
| ReplicationController |  |  |  |  |  |  |  |
| ReplicaSet | x | x | x | x | x | x | x |
| Deployment | x | x | x | x | x | x | x |
| StatefulSet | x | x | x | x | x | x | x |
| ControllerRevision |  |  |  |  |  |  |  |
| DaemonSet | x | x | x | x | x | x | x |
| Job | x | x | x | x | x | x | x |
| CronJob | x | x | x | x | x | x | x |
| HorizontalPodAutoscaler |  |  |  |  |  |  |  |
| PriorityClass |  |  |  |  |  |  |  |
| Namespaces | x | x | x |  | x | x |  |
|  |  |  |  |  |  |  |  |
| **Service** |  |  |  |  |  |  |  |
| Service | x | x | x |  | x | x |  |
| Endpoints | x | x | x |  | x | x |  |
| EndpointSlice | x | x | x |  | x | x |  |
| Ingress | x | x | x |  | x | x |  |
| IngressClass | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Config and Storage** |  |  |  |  |  |  |  |
| ConfigMap | x | x | x | x | x | x | x |
| Secret | x | x | x | x | x | x | x |
| PersistentVolumeClaim | x | x | x | x | x | x | x |
| PersistentVolume | x | x | x |  |  |  |  |
| StorageClass | x | x | x |  |  |  |  |
| VolumeAttachment | x | x | x |  |  |  |  |
| CSIDriver |  |  |  |  |  |  |  |
| CSINode |  |  |  |  |  |  |  |
| CSIStorageCapacity |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authentication** |  |  |  |  |  |  |  |
| ServiceAccount | x | x | x | x | x | x | x |
| TokenRequest |  |  |  |  |  |  |  |
| TokenReview |  |  |  |  |  |  |  |
| CertificateSigningRequest |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authorization** |  |  |  |  |  |  |  |
| ClusterRole | x | x | x |  |  |  |  |
| ClusterRoleBinding | x | x | x |  |  |  |  |
| Role | x | x | x |  |  |  |  |
| RoleBinding | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Policy** |  |  |  |  |  |  |  |
| LimitRange | x | x | x | x | x | x |  |
| ResourceQuota | x | x | x | x | x | x |  |
| NetworkPolicy | x | x | x | x | x | x |  |
| PodDisruptionBudget | x | x | x | x | x | x |  |
|  |  |  |  |  |  |  |  |
| **Extend** |  |  |  |  |  |  |  |
| CustomResourceDefinition |  |  |  |  |  |  |  |

#### Actions - developer

| **Resources** | **get** | **list** | **watch** | **create** | **update** | **patch** | **delete** |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
| **Workload** |  |  |  |  |  |  |  |
| Pod | x | x | x | x | x | x | x |
| PodTemplate | x | x | x | x | x | x | x |
| ReplicationController | x | x | x | x | x | x | x |
| ReplicaSet | x | x | x | x | x | x | x |
| Deployment | x | x | x | x | x | x | x |
| StatefulSet | x | x | x | x | x | x | x |
| ControllerRevision | x | x | x | x | x | x | x |
| DaemonSet | x | x | x | x | x | x | x |
| Job | x | x | x | x | x | x | x |
| CronJob | x | x | x | x | x | x | x |
| HorizontalPodAutoscaler | x | x | x | x | x | x | x |
| PriorityClass | x | x | x | x | x | x | x |
| Namespaces | x | x | x |  | x | x |  |
|  |  |  |  |  |  |  |  |
| **Service** |  |  |  |  |  |  |  |
| Service | x | x | x | x | x | x | x |
| Endpoints | x | x | x |  |  |  |  |
| EndpointSlice | x | x | x |  |  |  |  |
| Ingress | x | x | x | x | x | x | x |
| IngressClass | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Config and Storage** |  |  |  |  |  |  |  |
| ConfigMap | x | x | x | x | x | x | x |
| Secret | x | x | x | x | x | x | x |
| PersistentVolumeClaim | x | x | x | x | x | x | x |
| PersistentVolume | x | x | x | x | x | x | x |
| StorageClass | x | x | x |  |  |  |  |
| VolumeAttachment | x | x | x |  |  |  |  |
| CSIDriver |  |  |  |  |  |  |  |
| CSINode |  |  |  |  |  |  |  |
| CSIStorageCapacity |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authentication** |  |  |  |  |  |  |  |
| ServiceAccount | x | x | x | x | x | x | x |
| TokenRequest |  |  |  |  |  |  |  |
| TokenReview |  |  |  |  |  |  |  |
| CertificateSigningRequest |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authorization** |  |  |  |  |  |  |  |
| ClusterRole |  |  |  |  |  |  |  |
| ClusterRoleBinding |  |  |  |  |  |  |  |
| Role |  |  |  |  |  |  |  |
| RoleBinding |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Policy** |  |  |  |  |  |  |  |
| LimitRange | x | x | x |  |  |  |  |
| ResourceQuota | x | x | x |  |  |  |  |
| NetworkPolicy | x | x | x |  |  |  |  |
| PodDisruptionBudget | x | x | x | x | x | x | x |
|  |  |  |  |  |  |  |  |
| **Extend** |  |  |  |  |  |  |  |
| CustomResourceDefinition |  |  |  |  |  |  |  |

#### Actions - students

| **Resources** | **get** | **list** | **watch** | **create** | **update** | **patch** | **delete** |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
| **Workload** |  |  |  |  |  |  |  |
| Pod | x | x | x | x | x | x | x |
| PodTemplate | x | x | x | x | x | x | x |
| ReplicationController | x | x | x | x | x | x | x |
| ReplicaSet | x | x | x | x | x | x | x |
| Deployment | x | x | x | x | x | x | x |
| StatefulSet | x | x | x | x | x | x | x |
| ControllerRevision | x | x | x | x | x | x | x |
| DaemonSet | x | x | x | x | x | x | x |
| Job | x | x | x | x | x | x | x |
| CronJob | x | x | x | x | x | x | x |
| HorizontalPodAutoscaler | x | x | x | x | x | x | x |
| PriorityClass |  |  |  |  |  |  |  |
| Namespaces | x | x | x |  | x | x |  |
|  |  |  |  |  |  |  |  |
| **Service** |  |  |  |  |  |  |  |
| Service | x | x | x | x | x | x | x |
| Endpoints | x | x | x |  |  |  |  |
| EndpointSlice | x | x | x |  |  |  |  |
| Ingress | x | x | x |  |  |  |  |
| IngressClass | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Config and Storage** |  |  |  |  |  |  |  |
| ConfigMap | x | x | x | x | x | x | x |
| Secret | x | x | x | x | x | x | x |
| PersistentVolumeClaim | x | x | x | x | x | x | x |
| PersistentVolume | x | x | x |  |  |  |  |
| StorageClass | x | x | x |  |  |  |  |
| VolumeAttachment | x | x | x |  |  |  |  |
| CSIDriver |  |  |  |  |  |  |  |
| CSINode |  |  |  |  |  |  |  |
| CSIStorageCapacity |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authentication** |  |  |  |  |  |  |  |
| ServiceAccount | x | x | x | x | x | x | x |
| TokenRequest |  |  |  |  |  |  |  |
| TokenReview |  |  |  |  |  |  |  |
| CertificateSigningRequest |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authorization** |  |  |  |  |  |  |  |
| ClusterRole |  |  |  |  |  |  |  |
| ClusterRoleBinding |  |  |  |  |  |  |  |
| Role |  |  |  |  |  |  |  |
| RoleBinding |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Policy** |  |  |  |  |  |  |  |
| LimitRange | x | x | x |  |  |  |  |
| ResourceQuota | x | x | x |  |  |  |  |
| NetworkPolicy | x | x | x |  |  |  |  |
| PodDisruptionBudget | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Extend** |  |  |  |  |  |  |  |
| CustomResourceDefinition |  |  |  |  |  |  |  |

#### Actions - readonly

| **Resources** | **get** | **list** | **watch** | **create** | **update** | **patch** | **delete** |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
| **Workload** |  |  |  |  |  |  |  |
| Pod | x | x | x |  |  |  |  |
| PodTemplate | x | x | x |  |  |  |  |
| ReplicationController | x | x | x |  |  |  |  |
| ReplicaSet | x | x | x |  |  |  |  |
| Deployment | x | x | x |  |  |  |  |
| StatefulSet | x | x | x |  |  |  |  |
| ControllerRevision | x | x | x |  |  |  |  |
| DaemonSet | x | x | x |  |  |  |  |
| Job | x | x | x |  |  |  |  |
| CronJob | x | x | x |  |  |  |  |
| HorizontalPodAutoscaler | x | x | x |  |  |  |  |
| PriorityClass | x | x | x |  |  |  |  |
| Namespaces | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Service** |  |  |  |  |  |  |  |
| Service | x | x | x |  |  |  |  |
| Endpoints | x | x | x |  |  |  |  |
| EndpointSlice | x | x | x |  |  |  |  |
| Ingress | x | x | x |  |  |  |  |
| IngressClass | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Config and Storage** |  |  |  |  |  |  |  |
| ConfigMap | x | x | x |  |  |  |  |
| Secret | x | x | x |  |  |  |  |
| PersistentVolumeClaim | x | x | x |  |  |  |  |
| PersistentVolume | x | x | x |  |  |  |  |
| StorageClass | x | x | x |  |  |  |  |
| VolumeAttachment | x | x | x |  |  |  |  |
| CSIDriver | x | x | x |  |  |  |  |
| CSINode | x | x | x |  |  |  |  |
| CSIStorageCapacity | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authentication** |  |  |  |  |  |  |  |
| ServiceAccount | x | x | x |  |  |  |  |
| TokenRequest | x | x | x |  |  |  |  |
| TokenReview | x | x | x |  |  |  |  |
| CertificateSigningRequest | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Authorization** |  |  |  |  |  |  |  |
| ClusterRole | x | x | x |  |  |  |  |
| ClusterRoleBinding | x | x | x |  |  |  |  |
| Role | x | x | x |  |  |  |  |
| RoleBinding | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Policy** |  |  |  |  |  |  |  |
| LimitRange | x | x | x |  |  |  |  |
| ResourceQuota | x | x | x |  |  |  |  |
| NetworkPolicy | x | x | x |  |  |  |  |
| PodDisruptionBudget | x | x | x |  |  |  |  |
|  |  |  |  |  |  |  |  |
| **Extend** |  |  |  |  |  |  |  |
| CustomResourceDefinition | x | x | x |  |  |  |  |

### Namespace access - develop

|  | **devops** | **techsupport** | **developer** | **students** | **readonly** |
| --- | --- | --- | --- | --- | --- |
| ais-core | x | x |  |  | x |
| ais-processing | x | x |  |  | x |
| amazon-cloudwatch | x | x |  |  | x |
| aws-observability | x | x |  |  | x |
| ambassador | x |  |  |  | x |
| brokers | x | x | x |  | x |
| bunkerplanner | x | x |  |  | x |
| calico-apiserver | x |  |  |  | x |
| calico-system | x |  |  |  | x |
| core-service | x | x |  |  | x |
| customer-apps | x | x |  |  | x |
| data-engineering | x | x |  |  | x |
| default | x |  |  |  | x |
| external-dns | x | x |  |  | x |
| general-service | x | x |  |  | x |
| keycloak | x | x |  |  | x |
| kube-node-lease | x |  |  |  | x |
| kube-public | x |  |  |  | x |
| kube-system | x | x |  |  | x |
| kubeapps | x | x |  |  | x |
| monitoring | x | x | x |  | x |
| portcall | x | x |  |  | x |
| pto | x | x |  |  | x |
| revents-core | x | x |  |  | x |
| students | x | x | x | x | x |
| teqplay-api | x | x |  |  | x |
| teqplay-app | x | x |  |  | x |
| teqplay-fun | x | x | x |  | x |
| testing | x | x | x |  | x |
| tigera-operator | x | x |  |  | x |
| vaultwarden | x | x |  |  | x |
| velero | x | x |  |  | x |
| voyage | x | x |  |  | x |

### Namespace access - production

|  | **devops** | **techsupport** | **developer** | **readonly** |
| --- | --- | --- | --- | --- |
| ais-core | x | x |  | x |
| ais-processing | x | x |  | x |
| amazon-cloudwatch | x | x |  | x |
| aws-observability | x | x |  | x |
| brokers | x | x | x | x |
| bunkerplanner | x | x |  | x |
| calico-apiserver | x |  |  | x |
| calico-system | x |  |  | x |
| core-service | x | x |  | x |
| customer-apps | x | x |  | x |
| data-engineering | x | x |  | x |
| default | x |  |  | x |
| external-dns | x | x |  | x |
| general-service | x | x |  | x |
| keycloak | x | x |  | x |
| kube-node-lease | x |  |  | x |
| kube-public | x |  |  | x |
| kube-system | x | x |  | x |
| kubeapps | x | x |  | x |
| monitoring | x | x | x | x |
| portcall | x | x |  | x |
| pto | x | x |  | x |
| revents-core | x | x |  | x |
| teqplay-api | x | x |  | x |
| teqplay-app | x | x |  | x |
| teqplay-fun | x | x | x | x |
| voyage | x | x |  | x |

## Access to specific namespaces

For specific namespaces it’s required to select the permission group in Keycloak to grant access for that specific namespace. This applies for the following namespaces.

wide760ais-core
ais-processing
brokers
bunkerplanner
core-service
customer-apps
data-engineering
general-service
portcall
pto
revents-core
teqplay-api
voyage

**Join the Keycloak group**

To perform the described action, administrator access to Keycloak is required. Refer to the displayed image for guidance on how to join a specific Keycloak group, which is mapped to a namespace in the cluster.

So in the keycloak admin panel:

1. Go to kubeapps realm
2. Go to users
3. Assign <user> the role or group called <group-role>

## Applying roles

Within the `kubernetes-scripts` repository, modify the roles and permissions, then apply the changes to the cluster. Navigate to the `kubeapps/rbac` directory, where groups are outlined. Each group specifies the cluster role, cluster binding, role, and role bindings. The `namespaces.txt` file enumerates the namespaces to which the group is granted access.

## Managing roles (Work in Progress)

Within the `kubernetes-scripts` repository, scripts in the `kubeapps/rbac` directory are available to manage cluster roles. Two scripts have been developed—one for removing all roles in the cluster and another for applying the roles. Ensure modifications are made only at appropriate times. Notably, roles for `devops` are exempt from automatic removal since, after removal, access to the cluster would be restricted. Therefore, roles for `devops` should be addressed manually.

### Add new group

It's crucial to discern whether a group is bound to a namespace or the entire cluster. If the group's permissions are confined to a specific namespace, there is no necessity to include cluster roles. In the example below, roles for both the namespace and the entire cluster are provided.

* Create a directory with the name of the new group.
* Copy the files of an existing group e.g. developer.
* Replace all names which has `developer` in it with the new group name.
* Change the file `namespaces.txt` by adding or removing the namespaces the group has access to.
* Apply the roles with the script `apply-roles.sh`.

wide760./apply-roles.sh

* Create the group in Keycloak for DEVELOP and PRODUCTION.
* The group is ready to be used by a specific user.
* Update the roles and permissions in this document.