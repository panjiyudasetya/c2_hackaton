---
id: confluence:1169850370
source: confluence
type: page
space: TC
title: Kubernetes Access Guide
author: Jamie de Leest
date: '2026-03-27'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1169850370
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1169850370
---
# Kubernetes Access Guide

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1169850370  

## Content

this is a Guide for setting up access to our Kubernetes clusters

## Prepare your machine for EKS and Kubernetes

Install the following packages on your machine:

* AWS CLI → <https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>
* Kubernetes CLI → <https://kubernetes.io/docs/tasks/tools/> (only `kubectl`)
* Helm → <https://helm.sh/docs/intro/install/>

While entirely optional, I also suggest installing <https://k8slens.dev/>. This program can do all the commands in this guide without filling them in yourself. The program also shows real-time metrics of the `Nodes` and `Pods`.

---

## Setup AWS CLI

To configure access to our EKS Cluster you need to setup your AWS CLI

### Get SSO details from your admin

You’ll need:

* SSO start URL (`https://teqplay.awsapps.com/start/#`)
* AWS region (`eu-west-1`)
* Account ID
* Role name

### Run SSO configuration

Run:

wide760aws configure sso

You’ll be prompted for:

* **SSO session name** → e.g. `my-sso`
* **SSO start URL**
* **SSO region**
* It will open a browser to log in
* Then select:

  + Account
  + Role

Finally:

* **CLI profile name** → e.g. `dev` or `prod`

### Login with SSO

Before using AWS commands:

wide760aws sso login --profile dev

This opens your browser and authenticates you.

### Use the profile

Example:

wide760aws s3 ls --profile dev

### Where config is stored

AWS stores config in:

wide760~/.aws/config

Example:

wide760[profile dev]
sso\_session = my-sso
sso\_account\_id = 123456789012
sso\_role\_name = Developer
region = eu-west-1

### Re-authentication

SSO sessions expire (usually after a few hours).  
Just run again:

wide760aws sso login --profile dev

---

## Steps to set up access to Kubernetes cluster

<https://github.com/int128/kubelogin>

### Step 1: install kubelogin

macOS

wide760brew install int128/kubelogin/kubelogin

Linux

wide760# Check the version first and replace it in de url
# See releases
# https://github.com/int128/kubelogin/releases
curl -vL https://github.com/int128/kubelogin/releases/download/v1.xx.x/kubelogin\_linux\_amd64.zip -o kubelogin.zip
# Example:
# curl -vL https://github.com/int128/kubelogin/releases/download/v1.28.0/kubelogin\_linux\_amd64.zip -o kubelogin.zip
unzip kubelogin.zip
mv kubelogin /usr/local/bin/kubectl-oidc\_login

Windows

wide760choco install kubelogin

### Step 2: add the cluster to the “kubeconfig” file

**Develop**

wide760aws eks update-kubeconfig --region eu-west-1 --name develop --alias develop
kubectl config use-context develop

**Production**

wide760aws eks update-kubeconfig --region eu-west-1 --name production --alias production
kubectl config use-context production

### Step 3: connect Keycloak with Kubectl

The OIDC client secret can be found in Bitwarden. If the secret is not visible, kindly request access to the client secret from the responsible administrator.

The configuration may differ based on your operating system. The subsequent section is segregated into a Linux/Mac section and a Windows section. Please select the one that corresponds to your situation.

**Linux and MacOS users**

**Develop**

wide760kubectl config set-credentials keycloak-dev \
--exec-api-version=client.authentication.k8s.io/v1beta1 \
--exec-command=kubectl \
--exec-arg=oidc-login \
--exec-arg=get-token \
--exec-arg=--oidc-issuer-url=https://keycloakdev.teqplay.nl/auth/realms/kubeapps \
--exec-arg=--oidc-client-id=kubeapps \
--exec-arg=--oidc-client-secret=<AVAILABLE IN BITWARDEN UNDER oidc-client-secret (DEVELOP)>
wide760kubectl config set-context develop --user=keycloak-dev

**Production**

wide760kubectl config set-credentials keycloak-prod \
--exec-api-version=client.authentication.k8s.io/v1beta1 \
--exec-command=kubectl \
--exec-arg=oidc-login \
--exec-arg=get-token \
--exec-arg=--oidc-issuer-url=https://keycloak.teqplay.nl/auth/realms/kubeapps \
--exec-arg=--oidc-client-id=kubeapps \
--exec-arg=--oidc-client-secret=<AVAILABLE IN BITWARDEN UNDER oidc-client-secret (PRODUCTION)>
wide760kubectl config set-context production --user=keycloak-prod

**Windows users**

**Develop**

wide760kubectl config set-credentials keycloak-dev \
--exec-api-version=client.authentication.k8s.io/v1beta1 \
--exec-command=kubelogin \
--exec-arg=get-token \
--exec-arg=--oidc-issuer-url=https://keycloakdev.teqplay.nl/auth/realms/kubeapps \
--exec-arg=--oidc-client-id=kubeapps \
--exec-arg=--oidc-client-secret=<AVAILABLE IN BITWARDEN UNDER oidc-client-secret (DEVELOP)>
wide760kubectl config set-context develop --user=keycloak-dev

**Production**

wide760kubectl config set-credentials keycloak-prod \
--exec-api-version=client.authentication.k8s.io/v1beta1 \
--exec-command=kubelogin \
--exec-arg=get-token \
--exec-arg=--oidc-issuer-url=https://keycloak.teqplay.nl/auth/realms/kubeapps \
--exec-arg=--oidc-client-id=kubeapps \
--exec-arg=--oidc-client-secret=<AVAILABLE IN BITWARDEN UNDER oidc-client-secret (PRODUCTION)>
wide760kubectl config set-context production --user=keycloak-prod

Find the oidc-client-secret in Bitwarden under `oidc-client-secret (DEVELOP)` or `oidc-client-secret (PRODUCTION).`

### Step 4: sign into with Keycloak

Open a terminal and run a “kubectl” command.

wide760# DEVELOP
kubectl config use-context develop
kubectl get pods
# PRODUCTION
kubectl config use-context production
kubectl get pods

Upon initiating the kubectl command in the terminal, the Kubelogin utility will automatically open the Keycloak sign-in page in your browser. However, running the command in the terminal is not mandatory; opening Lens achieves the same result. Proceed to sign in with your credentials.

Upon successful sign-in, the "Authenticated" message will be displayed, indicating the ability to execute "kubectl" commands in the terminal or use "Lens."

#### Access tokens

Tokens are stored in the directory `~/.kube/cache/oidc-login`. If you remove the tokens from that directory, the Kubelogin utility will attempt to refresh the token. Deleting the session in Keycloak will trigger a new sign-in session.