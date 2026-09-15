---
id: confluence:165675009
source: confluence
type: page
space: TC
title: Vaultwarden
author: Michel Wilson
date: '2023-09-15'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/165675009
explicit_links: []
---
# Vaultwarden

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/165675009  

## Content

Vaultwarden is the open source re-implementation of the Bitwarden server, the official homepage is [here](https://github.com/dani-garcia/vaultwarden). The official Docker image is [vaultwarden/server](https://hub.docker.com/r/vaultwarden/server), and we use a Helm chart for the installation which can be found in [this](https://github.com/guerzon/vaultwarden) repository, combined with some extra functionality (see [here](https://github.com/michelwilson/vaultwarden/tree/fix-upgrading), waiting for a PR to be merged). The chart (including extra bits) is available in Chartmuseum, as `teqplay/vaultwarden`.

## Preparation

Vaultwarden needs to persist data in a database, for this we use an AWS managed Postgres instance (RDS). Also, it needs to send e-mail for notifications, and we need to setup a hostname in the Route53 zone redirecting to either the production or develop loadbalancer.

### Database

In the Amazon RDS console, create a Postgres hosted database. At the time of installing, version 14.6 was used, with basic non-clustered settings, using a t4g.micro instance (burstable). For the disk, ensure that gp3 storage is used. 20G is the minimum disk size, this should be ample. In the connectivity settings part, assign the “postgres inbound access” security group. Public access should be disabled, and you should ensure that the instance is created in the eu-west-1c AZ, in which the cluster also lives.

Create an admin account and password, save these to the password manager. Then, using `createdb` (part of the Postgres CLI, install this on your local machine if needed), create the `vaultwarden` database:

nonecreatedb \
-h vaultwarden.cvaevgsmr2it.eu-west-1.rds.amazonaws.com \
-U teqplayadmin \
vaultwarden

Connect to the database with `psql` and execute the following commands:

sqlCREATE USER vaultwarden WITH PASSWORD 'xxxxxxxxxx';
GRANT ALL PRIVILEGES ON DATABASE vaultwarden TO vaultwarden;

Using the above, we can create the database connection string for vaultwarden:

DATABASE\_URL=postgresql://vaultwarden:xxxxxxxxxx@<rds url>/vaultwarden

The first `vaultwarden` is the user name, the trailing `vaultwarden` is the database.

### Sendgrid

We need to create a Sendgrid API key for the server to be able to send e-mail notifications (for invites):

* In the Sendgrid dashboard, under “Settings > API Keys” click “Create API Key”
* Give the key a descriptive name, select “Restricted Access”, and give full access to the “Mail Send” category.
* Save the key, and copy the value of the key

## Installation

First, we start by generating and hashing the admin token. For this, you need to have `openssl` and `argon2` installed on your machine. Generate and write down an admin token (later, this token will have to be added to the vault):

openssl rand -base64 48

Then, use `argon2` to hash the token, as follows:

echo -n "my super secret token" | argon2 \
"$(openssl rand -base64 32)" \
-e -id -k 65540 -t 3 -p 4

Finally, all the secrets we need are going to be stored in a Kubernetes secret, using the following command:

kubectl -n vaultwarden create secret generic vaultwarden \
--from-literal=adminToken=<...> \
--from-literal=databaseUrl=<...> \
--from-literal=smtpUsername=apikey \
--from-literal=smtpPassword=<...>

If you want, you can validate that the secrets are stored correctly using Lens.

Then, using the values files in the kubernetes-scripts repository, install the application:

helm install vaultwarden teqplay/vaultwarden \
--namespace vaultwarden \
--values values.yaml \
--values values.prod.yaml

Access the admin page by going to [https://vault.teqplay.nl/admin](https://vaultdev.teqplay.nl/admin) and entering the admin token you generated.

## Configuration

Enter the admin panel by going to `https://vaultdev.teqplay.nl/admin` and entering the admin token you have generated. The following settings need to be checked/changed:

* **General Settings**

  + Domain URL: `https://vault[dev].teqplay.nl`
  + Allow new signups: **false**
  + Invitation organization name: `Teqplay Vaultwarden`
* **Advanced Settings**

  + Client IP header: `X-Forwarded-For`

Here, you can also test if the SMTP configuration is correct by sending a test email.

## Upgrading

If a new server version is available (this can be see in the admin page of Vaultwarden), an update can be performed by executing the following command:

* Execute the following command:

  helm upgrade vaultwarden teqplay/vaultwarden \
  --namespace vaultwarden \
  --values values.yaml \
  --values values.prod.yaml \
  --set "image.tag=<version-number>"