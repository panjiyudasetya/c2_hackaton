---
id: confluence:542572550
source: confluence
type: page
space: TC
title: Managing secrets MongoDB, PostgreSql and RabbitMQ
author: Minh Trang Nguyen (Unlicensed)
date: '2025-09-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/542572550
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/542572550
---
# Managing secrets MongoDB, PostgreSql and RabbitMQ

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/542572550  

## Content

status: concept

This document focuses on the process for MongoDB, while PostgreSQL and RabbitMQ follow a similar workflow.

## Introduction

Kubernetes Secrets are, by design, namespace-scoped and decentralized, which complicates their management. This decentralized nature means that credentials and sensitive data are often scattered across various namespaces, making it difficult to enforce a consistent security policy, audit access, and rotate keys at scale.

To address these challenges, we've established the following requirements for a centralized secret management solution:

* More centralized management
* More automatically managed
* Rotating of passwords
* MongoDB password management, cronjob + AWS secret manager
* For rotating passwords use two accounts, one account which is updated at a different time, than for second account. This is based on an article of AWS <https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/rotate-database-credentials-without-restarting-containers.html>.

## MongoDB password rotation

Managing secrets becomes increasingly complex in a microservice architecture as the number of applications grows. Currently, all secrets are managed on a per-installation basis, which complicates routine tasks like password rotation. For example, changing a MongoDB password requires a synchronized update in both the database itself and the application's configuration, a process that is difficult and prone to error.

### Moving root passwords to AWS secret manager

MongoDB root account passwords are currently stored in secrets within the clusters and are only used by developers for direct database access. A more secure approach is to migrate these passwords to AWS Secrets Manager, restricting developer access to the development environment only. For production, root passwords should be accessible only to administrators.

### A Two-Account Strategy for Seamless Password Rotation

When you rotate passwords for a single account, any active connections will fail until they are updated with the new password. This often results in a disruption of service.

A more effective approach is to use two separate accounts. This allows you to rotate the password for one account while the other remains active, ensuring a smooth transition without downtime.

Here's how the process works:

**Initial Setup**  
You begin with two accounts, `user-a` and `user-b`. Your application is configured to use `user-a` to connect to the MongoDB database.

**Rotation Trigger**  
When it's time to rotate passwords (either automatically or manually), a script is triggered.

**Password Change**  
The script changes the password for `user-b`, which is currently not in use. It then updates your application's configuration with `user-b` new credentials.

**Application Restart**  
After the application restarts, it will use the newly configured `user-b` account to connect to the database. The application does not currently support live password reloading, a feature that `Kubernetes` supports by default.

**Clean Up**  
Now that `user-a` is no longer active, its password can be safely changed without affecting the application.

For the next rotation, the process simply reverses, with `user-a` becoming the active account.

## Current configuration

The table below shows the current password configuration. The table shows where the usernames and passwords need to be changed. The MongoDB username is set in the environment variables of the deployments, while the MongoDB password is in the secret.

Also, note that multiple applications are using a shared MongoDB database, which is displayed in separate tables.

The proposal is an enhancement to the Helm chart by introducing a new switch. This feature will allow the use of External Secrets as an alternative to the conventional secret management method. More about this later in this document.

**DEVELOP CLUSTER**

table: default application + MongoDb setup

| **namespace** | **application** | **location** |
| --- | --- | --- |
| ais-core | ais-stream-dev | env vars + secret **ais-stream-dev-mongodb** |
| ais-processing | ais-rabbitmq-dev | env vars + secret **ais-rabbitmq-dev-mongodb** |
| ais-processing | event-history-processor-dev | env vars + secret **event-history-processor-dev-mongodb** |
| ais-processing | ship-history-processor-dev | env vars + secret **ship-history-processor-dev-mongodb** |
| bunkerplanner | bunkerplanner-dev | env vars + secret **bunkerplanner-dev-mongodb** |
| bunkerplanner | bunkerplanner-test | env vars + secret **bunkerplanner-test-mongodb** |
| bunkerplanner | fuelboss-dev | env vars + secret **fuelboss-dev-mongodb** |
| bunkerplanner | fuelboss-test | env vars + secret **fuelboss-test-mongodb** |
| core-service | poma-sandbox | env vars + secret **poma-sandbox-mongodb** |
| core-service | routescout-graph-dev | env vars + secret **routescout-graph-dev-mongodb** |
| customer-apps | mongodb-customer-apps-dev | env vars + secret **mongodb-customer-apps-dev** |
| customer-apps | sednaintegration-dev | env vars + secret **sednaintegration-dev-mongodb** |
| customer-apps | vesselcompliance-demo-charterer | env vars + secret **vesselcompliance-demo-charterer-mongodb** |
| customer-apps | vesselcompliance-dev | env vars + secret **vesselcompliance-dev-mongodb** |
| customer-apps | vesselcompliance-poc | env vars + secret **vesselcompliance-poc-mongodb** |
| customer-apps | vesselcompliance-staging | env vars + secret **vesselcompliance-staging-mongodb** |
| customer-apps | vesselmatcher-dev | env vars + secret **vesselmatcher-dev-mongodb** |
| general-service | functionalmonitoring-dev | env vars + secret **functionalmonitoring-dev-mongodb** |
| portcall | portreporter-testing | env vars + secret **portreporter-testing-mongodb** |
| revents-core | revents-engine-api | env vars + secret **revents-engine-api-mongodb** |
| revents-core | revents-vesselvoyage | env vars + secret **revents-vesselvoyage-mongodb** |
| students | atlas-dev | env vars + secret **atlas-dev-mongodb** |
| students | pdatool-dev | env vars + secret **pdatool-dev-mongodb** |
| voyage | cargooptima-dev | env vars + secret **cargooptima-dev-mongodb** |
| voyage | cargooptima-staging | env vars + secret **cargooptima-staging-mongod** |
| voyage | service-vessel-analysis-dev | env vars + secret **service-vessel-analysis-dev-mongodb** |
| voyage | smartfleet-dev | env vars + secret **smartfleet-dev-mongodb** |
| voyage | vesselvoyage-dev | env vars + secret **vesselvoyage-dev-mongodb** |

A shared MongoDB instance is available for applications within the `customer-apps`, `general-service`, `core-service`, and `portcall` namespaces. See tables below.

**mongodb-customer-apps-dev**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| customer-apps | datastore-dev | configmap: datastore-dev |
| customer-apps | portsupport-dev | configmap: portsupport-dev |
| customer-apps | shipsparelogistics-dev | configmap: shipsparelogistics-dev |
| customer-apps | terminalplanner-dev | configmap: terminalplanner-dev |

**mongodb-general-service-dev**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| general-service | datascience-dev | configmap: datascience-dev |
| general-service | terminallineup-dev | configmap: terminallineup-dev |
| general-service | pdfrenderer-dev | configmap: pdfrenderer-dev |
| general-service | scrapeshark-dev | configmap: scrapeshark-dev |
| general-service | timeline-dev | configmap: timeline-dev |

**mongodb-core-service-dev**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| core-service | csi-internal-dev | configmap: csi-internal-dev |
| core-service | csi-query-dev | configmap: csi-query-dev |
| core-service | portmatcher-dev | configmap: portmatcher-dev |
| core-service | routescout-dev | configmap: routescout-dev |
| core-service | routescout-route-planning-dev | configmap: routescout-route-planning-dev |

**mongodb-portcall-dev**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| portcall | portcallplus-dev | configmap: portcallplus-dev |
| portcall | portreporter-dev | configmap: portreporter-dev |
| portcall | portpublisher-dev | configmap: portpublisher-dev |

**PRODUCTION CLUSTER**

table: default application + MongoDb setup

| **namespace** | **application** | **location** |
| --- | --- | --- |
| ais-core | ais-stream | env vars + secret **ais-stream-mongodb** |
| ais-processing | ais-rabbitmq | env vars + secret **ais-rabbitmq-mongodb** |
| ais-processing | event-history-processor | env vars + secret **event-history-processor-mongodb** |
| ais-processing | ship-history-processor | env vars + secret **ship-history-processor-mongodb** |
| bunkerplanner | bunkerplanner | env vars + secret **bunkerplanner-mongodb** |
| bunkerplanner | fuelboss | env vars + secret **fuelboss-dev-mongodb** |
| bunkerplanner | fuelboss-demo | env vars + secret **fuelboss-demo-mongodb** |
| core-service | poma-data | env vars + secret **poma-sandbox-mongodb** |
| core-service | routescout-graph | env vars + secret **routescout-graph-mongodb** |
| customer-apps | vesselcompliance | env vars + secret **vesselcompliance-mongodb** |
| customer-apps | vesselmatcher | env vars + secret **vesselmatcher-mongodb** |
| general-service | functionalmonitoring | env vars + secret **functionalmonitoring-mongodb** |
| revents-core | revents-engine-api | env vars + secret **revents-engine-api-mongodb** |
| revents-core | revents-engine-api-data | env vars + secret **revents-engine-api-data-mongodb** |
| revents-core | revents-vesselvoyage | env vars + secret **revents-vesselvoyage-mongodb** |
| voyage | smartfleet | env vars + secret **smartfleet-mongodb** |
| voyage | vesselvoyage | env vars + secret **vesselvoyage-mongodb** |
| voyage | vesselvoyage-data | env vars + secret **vesselvoyage-data-mongodb** |

**mongodb-customer-apps**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| customer-apps | datastore | configmap: datastore |
| customer-apps | portsupport | configmap: portsupport |
| customer-apps | shipsparelogistics | configmap: shipsparelogistics |
| customer-apps | terminalplanner | configmap: terminalplanner |
| customer-apps | casey | configmap: casey |

**mongodb-general-service**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| general-service | datascience | configmap: datascience |
| general-service | datascience-moves | configmap: datascience-moves |
| general-service | terminallineup | configmap: terminallineup |
| general-service | pdfrenderer | configmap: pdfrenderer |
| general-service | scrapeshark | configmap: scrapeshark |
| general-service | timeline | configmap: timeline |

**mongodb-core-service**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| core-service | csi-internal | configmap: csi-internal |
| core-service | csi-query | configmap: csi-query |
| core-service | portmatcher | configmap: portmatcher |
| core-service | routescout | configmap: routescout |
| core-service | routescout-route-planning | configmap: routescout-route-planning |

**mongodb-portcall-dev**

| **namespace** | **application** | **location** |
| --- | --- | --- |
| portcall | portcallplus | configmap: portcallplus |
| portcall | portreporter | configmap: portreporter |
| portcall | portpublisher | configmap: portpublisher |

## Using Helm Charts as a source of truth with backwards compatibility secrets

The cluster supports two patterns for providing applications with MongoDB access:

**Dedicated Instance**

Each Helm chart can be configured to deploy its own dedicated MongoDB instance, running alongside the application.

**Shared Instance**

A single, shared MongoDB instance can be provisioned per namespace, which multiple applications can then connect to and use.

Our strategy is to maintain backwards compatibility by continuing to support the dedicated and shared instance model.

To centralize database credential management, an automated process is being established. A cronjob will identify applications configured with a dedicated and shared MongoDB's. For each instance, the script will query AWS Secrets Manager to verify the existence of managed credentials. If none are present, it will provision a new user in the database and populate AWS Secrets Manager with the generated credentials.

This automation supports a required change in the application's Helm chart, which will be modified to include an optional flag. When enabled, this flag will configure the application to authenticate using credentials from an external secret, which is populated from the values stored in AWS Secret Manager. This enables a easier migration to a centralized system for managing MongoDB credentials.

## Install External Secret Operator

The documentation for installing the Operator can be found here:

<https://external-secrets.io/latest/introduction/getting-started/>

### Alternatives

I’ve tested other alternatives like Secrets Store CSI driver (<https://github.com/aws/secrets-store-csi-driver-provider-aws>). It was much more complex to manage than using External Secret Operator.

First, create an AWS IAM user (e.g., external-operator) and generate a corresponding Access Key. The resulting credentials, the Access Key ID and Secret Access Key, must then be stored in a Kubernetes secret. The steps below detail how to create this secret.

wide760echo -n '<ACCESS KEY ID>' > ./access-key
echo -n '<ACCESS KEY SECRET>' > ./secret-access-key
kubectl create secret generic awssm-secret \
-n external-secrets --from-file=./access-key --from-file=./secret-access-key
# This AWS Access Key secret is also required by other namespaces
# to access AWS Secrets Manager.
kubectl create secret generic awssm-secret \
-n <NAMESPACE NAME> --from-file=./access-key --from-file=./secret-access-key
# Clean up
rm -f ./access-key && \
rm -f ./secret-access-key

Create an IAM policy:

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": [
"secretsmanager:GetSecretValue",
"secretsmanager:DescribeSecret",
],
"Resource": "\*"
}
]
}

Add the Helm repo of the external-secret operator.

wide760helm repo add external-secrets https://charts.external-secrets.io

Install the Helm chart.

wide760helm install external-secrets \
external-secrets/external-secrets \
-n external-secrets \
--create-namespace \
--set installCRDs=true

## Creating Rotation Passwords

Create IAM user with name like `rotation.mongodb.passwords` in AWS IAM.

Create the IAM policy with name `TeqplaySecretsManager`. Add the following policy.

jsonwide760{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": [
"secretsmanager:GetRandomPassword",
"secretsmanager:GetSecretValue",
"secretsmanager:DescribeSecret",
"secretsmanager:PutSecretValue",
"secretsmanager:CreateSecret",
"secretsmanager:ListSecretVersionIds",
"secretsmanager:ListSecrets",
"secretsmanager:UpdateSecret"
],
"Resource": "\*"
}
]
}

Attach this policy to the access token.

### Script: synchronize MongoDB passwords

This script automates the creation of MongoDB credentials in AWS Secrets Manager. It works by scanning for all application deployments connected to a MongoDB database, handling both dedicated and shared instances and then provisions the necessary secrets. These secrets are subsequently used by the External-Secrets operator to securely manage database access.

This script is designed to run on a schedule via a cronjob, allowing it to automatically handle any new deployments created in the cluster.

pywide760import os
import secrets
import logging
import json
import base64
import string
from typing import Dict, Any, Optional, List, Tuple
from kubernetes import client, config
import boto3
from botocore.exceptions import ClientError
logging.basicConfig(
level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
def main():
try:
logging.info("Loading in-cluster Kubernetes configuration...")
config.load\_incluster\_config()
except config.ConfigException:
logging.warning(
"Could not load in-cluster config. Falling back to kube-config."
)
config.load\_kube\_config()
aws\_access\_key\_id = os.environ.get('AWS\_ACCESS\_KEY\_ID')
aws\_secret\_access\_key = os.environ.get('AWS\_SECRET\_ACCESS\_KEY')
aws\_region = os.environ.get('AWS\_REGION', 'eu-west-1')
secrets\_manager\_client = boto3.client(
'secretsmanager',
aws\_access\_key\_id=aws\_access\_key\_id,
aws\_secret\_access\_key=aws\_secret\_access\_key,
region\_name=aws\_region
)
apps\_v1 = client.AppsV1Api()
core\_v1 = client.CoreV1Api()
process\_deployments(
apps\_v1=apps\_v1,
core\_v1=core\_v1,
secrets\_manager\_client=secrets\_manager\_client,
label\_selector="app.kubernetes.io/name=skeleton-mongo-app,app.teqplay.nl/type=skeleton-backend",
processor\_func=process\_skeleton\_app\_container,
)
process\_deployments(
apps\_v1=apps\_v1,
core\_v1=core\_v1,
secrets\_manager\_client=secrets\_manager\_client,
label\_selector="app.kubernetes.io/name=mongodb",
processor\_func=process\_mongodb\_container,
)
def process\_deployments(apps\_v1, core\_v1, secrets\_manager\_client, label\_selector: str, processor\_func) -> None:
logging.info(f"Searching for deployments with label selector: '{label\_selector}'")
try:
deployments = apps\_v1.list\_deployment\_for\_all\_namespaces(label\_selector=label\_selector)
except client.ApiException as e:
logging.error(f"Error listing deployments: {e}")
return
for deployment in deployments.items:
if not (deployment.status.replicas and deployment.status.replicas > 0):
continue
namespace = deployment.metadata.namespace
deployment\_name = deployment.metadata.name
logging.info(f"Processing active deployment '{deployment\_name}' in namespace '{namespace}'")
for container in deployment.spec.template.spec.containers:
processor\_func(
core\_v1=core\_v1,
secrets\_manager\_client=secrets\_manager\_client,
deployment=deployment,
container=container,
)
def process\_skeleton\_app\_container(core\_v1, secrets\_manager\_client, deployment, container) -> None:
env\_parser = EnvParser(container.env)
secret\_ref = env\_parser.get\_secret\_ref("MONGODB\_PASSWORD")
if not secret\_ref:
return
k8s\_secret\_name, k8s\_secret\_key = secret\_ref
namespace = deployment.metadata.namespace
logging.info(
f"Found MONGODB\_PASSWORD reference to secret '{k8s\_secret\_name}' in deployment '{deployment.metadata.name}'")
mongodb\_username = env\_parser.get\_value("MONGODB\_USERNAME")
mongodb\_host = env\_parser.get\_value("MONGODB\_HOST")
mongodb\_db = env\_parser.get\_value("MONGODB\_DB")
if not all([mongodb\_username, mongodb\_host, mongodb\_db]):
logging.warning(f"Missing required MONGODB env vars in '{deployment.metadata.name}'. Skipping.")
return
root\_password = get\_password\_from\_k8s\_secret(
core\_v1, namespace, k8s\_secret\_name, "mongodb-root-password"
)
if not root\_password:
logging.warning(f"Could not find 'mongodb-root-password' in secret '{k8s\_secret\_name}'. Skipping.")
return
aws\_secret\_name = f'mongodb-pwd-rotate-{k8s\_secret\_name}'
if secret\_exists(secrets\_manager\_client, aws\_secret\_name):
logging.info(f"AWS Secret '{aws\_secret\_name}' already exists. No action needed.")
return
payload = build\_rotation\_secret\_payload(
base\_username=mongodb\_username,
root\_password=root\_password,
host=mongodb\_host,
db\_name=mongodb\_db
)
create\_or\_update\_secret(secrets\_manager\_client, aws\_secret\_name, json.dumps(payload))
def process\_mongodb\_container(core\_v1, secrets\_manager\_client, deployment, container) -> None:
env\_parser = EnvParser(container.env)
namespace = deployment.metadata.namespace
extra\_usernames\_str = env\_parser.get\_value("MONGODB\_EXTRA\_USERNAMES")
if not extra\_usernames\_str:
return
secret\_ref = env\_parser.get\_secret\_ref("MONGODB\_EXTRA\_PASSWORDS")
if not secret\_ref:
logging.warning(
f"Found MONGODB\_EXTRA\_USERNAMES but no MONGODB\_EXTRA\_PASSWORDS secret ref in '{deployment.metadata.name}'. Skipping.")
return
k8s\_secret\_name, \_ = secret\_ref
root\_password = get\_password\_from\_k8s\_secret(
core\_v1, namespace, k8s\_secret\_name, "mongodb-root-password"
)
if not root\_password:
logging.warning(f"Could not find 'mongodb-root-password' in secret '{k8s\_secret\_name}'. Skipping.")
return
mongodb\_host = find\_mongodb\_service\_host(core\_v1, deployment)
if not mongodb\_host:
logging.warning(
f"Could not determine service host for MongoDB deployment '{deployment.metadata.name}'. Skipping.")
return
usernames = [u.strip() for u in extra\_usernames\_str.split(',') if u.strip()]
logging.info(f"Found MONGODB\_EXTRA\_USERNAMES: {usernames} in '{deployment.metadata.name}'")
for username in usernames:
aws\_secret\_name = f'mongodb-pwd-extra-rotate-{username}'
if secret\_exists(secrets\_manager\_client, aws\_secret\_name):
logging.info(f"AWS Secret '{aws\_secret\_name}' for user '{username}' already exists. No action needed.")
continue
payload = build\_rotation\_secret\_payload(
base\_username=username,
root\_password=root\_password,
host=mongodb\_host
)
create\_or\_update\_secret(secrets\_manager\_client, aws\_secret\_name, json.dumps(payload))
class EnvParser:
def \_\_init\_\_(self, env\_vars: List[client.V1EnvVar]):
self.\_values = {}
self.\_secret\_refs = {}
if env\_vars:
for env in env\_vars:
if env.value:
self.\_values[env.name] = env.value
elif env.value\_from and env.value\_from.secret\_key\_ref:
self.\_secret\_refs[env.name] = (
env.value\_from.secret\_key\_ref.name,
env.value\_from.secret\_key\_ref.key,
)
def get\_value(self, name: str) -> Optional[str]:
return self.\_values.get(name)
def get\_secret\_ref(self, name: str) -> Optional[Tuple[str, str]]:
return self.\_secret\_refs.get(name)
def generate\_password(length = 32):
characters = string.ascii\_letters + string.digits
return ''.join(secrets.choice(characters) for \_ in range(length))
def get\_password\_from\_k8s\_secret(core\_v1, namespace: str, secret\_name: str, key: str) -> Optional[str]:
try:
secret = core\_v1.read\_namespaced\_secret(secret\_name, namespace)
encoded\_value = secret.data.get(key)
if encoded\_value:
return base64.b64decode(encoded\_value).decode("utf-8")
except client.ApiException as e:
logging.error(f"Error reading k8s secret '{secret\_name}' in namespace '{namespace}': {e}")
return None
def find\_mongodb\_service\_host(core\_v1, deployment) -> Optional[str]:
instance\_label = deployment.metadata.labels.get("app.kubernetes.io/instance")
if not instance\_label:
return None
label\_selector = f"app.kubernetes.io/instance={instance\_label}"
try:
services = core\_v1.list\_service\_for\_all\_namespaces(label\_selector=label\_selector)
if services.items:
service = services.items[0]
service\_name = service.metadata.name
namespace = service.metadata.namespace
logging.info(
f"Found service '{service\_name}' in namespace '{namespace}' for deployment '{deployment.metadata.name}'")
return f"{service\_name}.{namespace}.svc.cluster.local"
except client.ApiException as e:
logging.error(f"Error finding service with label '{label\_selector}': {e}")
return None
def build\_rotation\_secret\_payload(base\_username: str, root\_password: str, host: str, db\_name: Optional[str] = None) -> \
Dict[str, Any]:
payload = {
"mongodb-username": f"{base\_username}-rotate1",
"mongodb-password": generate\_password(),
"mongodb-root-password": root\_password,
"mongodb-host": host,
"mongodb-username-rotate1": f"{base\_username}-rotate1",
"mongodb-password-rotate1": generate\_password(),
"mongodb-username-rotate2": f"{base\_username}-rotate2",
"mongodb-password-rotate2": generate\_password(),
}
if db\_name:
payload["mongodb-db"] = db\_name
return payload
def secret\_exists(client, secret\_name: str) -> bool:
try:
client.describe\_secret(SecretId=secret\_name)
return True
except ClientError as e:
if e.response["Error"]["Code"] == "ResourceNotFoundException":
return False
else:
logging.error(f"Error describing AWS secret '{secret\_name}': {e}")
raise
def create\_or\_update\_secret(client, secret\_name: str, secret\_value: str) -> None:
try:
client.create\_secret(Name=secret\_name, SecretString=secret\_value)
logging.info(f"Secret '{secret\_name}' created successfully in AWS Secrets Manager.")
except ClientError as e:
if e.response["Error"]["Code"] == "ResourceAlreadyExistsException":
logging.info(f"Secret '{secret\_name}' exist, so no action required!")
else:
logging.error(f"Failed to create secret '{secret\_name}': {e}")
if \_\_name\_\_ == "\_\_main\_\_":
main()

Put the code in file `sync_mongodb_passwords.py`.

Add this script to a ConfigMap:

wide760kubectl create configmap syncmongodbpasswords -n external-secrets \
--from-file=sync\_mongodb\_passwords.py=./sync\_mongodb\_passwords.py \
--dry-run=client -o yaml | kubectl apply -f -

Add service account:

wide760kubectl -n external-secrets apply -f - <<EOF
apiVersion: v1
kind: ServiceAccount
metadata:
annotations:
eks.amazonaws.com/role-arn: arn:aws:iam::050356841556:role/TeqplaySecretsManagement
name: password-rotater
namespace: external-secrets
EOF

The IAM role has the following configuration:

Trust relationships:

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Principal": {
"Federated": "arn:aws:iam::050356841556:oidc-provider/oidc.eks.eu-west-1.amazonaws.com/id/5FC7B8323EF5BB6AA9FB5B0CC8D2D827"
},
"Action": "sts:AssumeRoleWithWebIdentity",
"Condition": {
"StringEquals": {
"oidc.eks.eu-west-1.amazonaws.com/id/5FC7B8323EF5BB6AA9FB5B0CC8D2D827:aud": "sts.amazonaws.com"
}
}
}
]
}

IAM Policy TeqplaySecretsManager:

wide760{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "VisualEditor0",
"Effect": "Allow",
"Action": [
"secretsmanager:GetRandomPassword",
"secretsmanager:GetSecretValue",
"secretsmanager:DescribeSecret",
"secretsmanager:PutSecretValue",
"secretsmanager:CreateSecret",
"secretsmanager:ListSecretVersionIds",
"secretsmanager:ListSecrets",
"secretsmanager:UpdateSecret"
],
"Resource": "\*"
}
]
}

A ClusterRole is required for scripts to execute tasks in the cluster.

Add RBAC:

wide760kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
name: teqplay:password:rotater:role
rules:
- apiGroups: ["external-secrets.io"]
resources: ["secretstores", "externalsecrets", "clustersecretstores", "clusterexternalsecrets"]
verbs: ["get", "list", "watch", "create", "update", "patch"]
- apiGroups: ["apps"]
resources: ["deployments"]
verbs: ["get", "list", "watch", "update", "patch"]
- apiGroups: [""]
resources: ["secrets"]
verbs: ["get", "list", "create", "delete", "update", "patch"]
- apiGroups: [""]
resources: ["services"]
verbs: ["get", "list"]
- apiGroups: [""]
resources: ["configmaps"]
verbs: ["get", "list", "create", "update", "patch"]
EOFwide760kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
name: teqplay:password:rotater:role:binding
roleRef:
apiGroup: rbac.authorization.k8s.io
kind: ClusterRole
name: teqplay:password:rotater:role
subjects:
- kind: ServiceAccount
name: password-rotater
namespace: ais-processing
- kind: ServiceAccount
name: password-rotater
namespace: bunkerplanner
- kind: ServiceAccount
name: password-rotater
namespace: core-service
- kind: ServiceAccount
name: password-rotater
namespace: customer-apps
- kind: ServiceAccount
name: password-rotater
namespace: general-service
- kind: ServiceAccount
name: password-rotater
namespace: portcall
- kind: ServiceAccount
name: password-rotater
namespace: revents-core
- kind: ServiceAccount
name: password-rotater
namespace: voyage
- kind: ServiceAccount
name: password-rotater
namespace: external-secrets
- kind: ServiceAccount
name: password-rotater
namespace: testing2
EOF

The CronJob is suspended, so it will not run on its schedule. Jobs must be triggered manually.

Create the cronjob:

wide760kubectl -n external-secrets apply -f - <<EOF
apiVersion: batch/v1
kind: CronJob
metadata:
name: sync-mongodb-passwords-with-aws-sm
labels:
app: mongodb-aws-sm
spec:
schedule: "0 \* \* \* \*"
suspend: true
jobTemplate:
spec:
template:
spec:
serviceAccountName: password-rotater
containers:
- name: sync-mongodb-passwords
image: python:3.12-bookworm
volumeMounts:
- name: volume-sync-mongodb-passwords
mountPath: /app/sync\_mongodb\_passwords.py
subPath: sync\_mongodb\_passwords.py
imagePullPolicy: IfNotPresent
command: ["/bin/sh", "-c"]
args:
- pip install kubernetes && pip install boto3 && python /app/sync\_mongodb\_passwords.py
env:
- name: AWS\_REGION
value: "eu-west-1"
- name: AWS\_ACCESS\_KEY\_ID
valueFrom:
secretKeyRef:
name: awssm-secret
key: access-key
- name: AWS\_SECRET\_ACCESS\_KEY
valueFrom:
secretKeyRef:
name: awssm-secret
key: secret-access-key
restartPolicy: OnFailure
volumes:
- name: volume-sync-mongodb-passwords
configMap:
name: syncmongodbpasswords
EOF

After triggering the cronjob, a job will create the secrets in AWS Secret Manager. See screenshot below for an example.

Example logs:

wide7602025-09-13 16:59:12,697 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-vesselvoyage' for user 'vesselvoyage' already exists. No action needed.
2025-09-13 16:59:12,697 - INFO - Processing active deployment 'atlas-dev-mongodb' in namespace 'students'
2025-09-13 16:59:12,709 - INFO - Found service 'atlas-dev' in namespace 'students' for deployment 'atlas-dev-mongodb'
2025-09-13 16:59:12,709 - INFO - Found MONGODB\_EXTRA\_USERNAMES: ['atlas'] in 'atlas-dev-mongodb'
2025-09-13 16:59:12,716 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-atlas' for user 'atlas' already exists. No action needed.
2025-09-13 16:59:12,716 - INFO - Processing active deployment 'pdatool-dev-mongodb' in namespace 'students'
2025-09-13 16:59:12,727 - INFO - Found service 'pdatool-dev' in namespace 'students' for deployment 'pdatool-dev-mongodb'
2025-09-13 16:59:12,727 - INFO - Found MONGODB\_EXTRA\_USERNAMES: ['pdatool'] in 'pdatool-dev-mongodb'
2025-09-13 16:59:12,734 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-pdatool' for user 'pdatool' already exists. No action needed.
2025-09-13 16:59:12,734 - INFO - Processing active deployment 'cargooptima-dev-mongodb' in namespace 'voyage'
2025-09-13 16:59:12,752 - INFO - Found service 'cargooptima-dev' in namespace 'voyage' for deployment 'cargooptima-dev-mongodb'
2025-09-13 16:59:12,752 - INFO - Found MONGODB\_EXTRA\_USERNAMES: ['cargo-optima'] in 'cargooptima-dev-mongodb'
2025-09-13 16:59:12,761 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-cargo-optima' for user 'cargo-optima' already exists. No action needed.
2025-09-13 16:59:12,762 - INFO - Processing active deployment 'cargooptima-staging-mongodb' in namespace 'voyage'
2025-09-13 16:59:12,783 - INFO - Found service 'cargooptima-staging' in namespace 'voyage' for deployment 'cargooptima-staging-mongodb'
2025-09-13 16:59:12,783 - INFO - Found MONGODB\_EXTRA\_USERNAMES: ['cargo-optima'] in 'cargooptima-staging-mongodb'
2025-09-13 16:59:12,787 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-cargo-optima' for user 'cargo-optima' already exists. No action needed.
2025-09-13 16:59:12,787 - INFO - Processing active deployment 'service-vessel-analysis-dev-mongodb' in namespace 'voyage'
2025-09-13 16:59:12,800 - INFO - Found service 'service-vessel-analysis-dev' in namespace 'voyage' for deployment 'service-vessel-analysis-dev-mongodb'
2025-09-13 16:59:12,800 - INFO - Found MONGODB\_EXTRA\_USERNAMES: ['servicevessel'] in 'service-vessel-analysis-dev-mongodb'
2025-09-13 16:59:12,809 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-servicevessel' for user 'servicevessel' already exists. No action needed.
2025-09-13 16:59:12,809 - INFO - Processing active deployment 'smartfleet-dev-mongodb' in namespace 'voyage'
2025-09-13 16:59:12,822 - INFO - Found service 'smartfleet-dev' in namespace 'voyage' for deployment 'smartfleet-dev-mongodb'
2025-09-13 16:59:12,822 - INFO - Found MONGODB\_EXTRA\_USERNAMES: ['smartfleet'] in 'smartfleet-dev-mongodb'
2025-09-13 16:59:12,830 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-smartfleet' for user 'smartfleet' already exists. No action needed.
2025-09-13 16:59:12,830 - INFO - Processing active deployment 'vesselvoyage-dev-mongodb' in namespace 'voyage'
2025-09-13 16:59:12,844 - INFO - Found service 'vesselvoyage-dev' in namespace 'voyage' for deployment 'vesselvoyage-dev-mongodb'
2025-09-13 16:59:12,853 - INFO - Found MONGODB\_EXTRA\_USERNAMES: ['vesselvoyage'] in 'vesselvoyage-dev-mongodb'
2025-09-13 16:59:12,859 - INFO - AWS Secret 'mongodb-pwd-extra-rotate-vesselvoyage' for user 'vesselvoyage' already exists. No action needed.

### Script: sync external secrets

This section describes how AWS Secret Manager secrets are synchronized with the Kubernetes cluster. First a section how to manually create an external secret.

### Manually add an external secret (Only for testing purpose)

Below is an example how to create an external secret manually. The preferred alternative, a `ClusterSecretStore`, couldn't be tested, so its implementation is a task for the future.

wide760kubectl apply -n <NAMESPACE NAME> -f - <<EOF
apiVersion: external-secrets.io/v1
kind: SecretStore
metadata:
name: external-secret-store
spec:
provider:
aws:
service: SecretsManager
region: eu-west-1
auth:
secretRef:
accessKeyIDSecretRef:
name: awssm-secret
key: access-key
secretAccessKeySecretRef:
name: awssm-secret
key: secret-access-key
EOF

Below is an example of the content of the secret in AWS Secrets Manager:

jsonwide760{
"mongodb-username": "vesselvoyage-rotate1",
"mongodb-password": "<PASSWORD USER A>",
"mongodb-root-password": "<PASSWORD USER A>",
"mongodb-host": "vesselvoyage-dev-mongodb.voyage.svc.cluster.local",
"mongodb-username-rotate1": "vesselvoyage-rotate1",
"mongodb-password-rotate1": "<PASSWORD USER A>",
"mongodb-username-rotate2": "vesselvoyage-rotate2",
"mongodb-password-rotate2": "<PASSWORD USER B>",
"mongodb-db": "vesselvoyage"
}

Create the external secret (example).

wide760kubectl apply -n testing2 -f - <<EOF
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
name: external-test-secret
spec:
refreshInterval: "15s"
secretStoreRef:
name: external-secret-store
kind: SecretStore
target:
name: target-secret
data:
- secretKey: mongodb-username
remoteRef:
key: trangtestsecret
property: mongodb-username
- secretKey: mongodb-password
remoteRef:
key: trangtestsecret
property: mongodb-password
- secretKey: mongodb-host
remoteRef:
key: trangtestsecret
property: mongodb-host
- secretKey: mongodb-root-password
remoteRef:
key: trangtestsecret
property: mongodb-root-password
EOF

List the secrets and see if the secret was created by the External-Secrets operator.

wide760kubectl get secrets
NAME TYPE DATA AGE
awssm-secret Opaque 2 24m
target-secret Opaque 2 16m

### Automatically synchronize secrets

This script fetches all secrets from AWS Secrets Manager and creates the necessary ExternalSecret resources. It also creates a SecretStore, which configures the External Secrets Operator to authenticate with and communicate with AWS Secrets Manager. Once configured, the operator will automatically synchronize the secrets in the cluster with AWS Secrets Manager every 15 seconds.

pywide760import base64
import json
import logging
import os
import boto3
from botocore.exceptions import ClientError
from kubernetes import client, config
AWS\_SECRET\_NAME\_PREFIX = "ext-"
K8S\_SECRET\_NAME = "awssm-secret"
SECRET\_STORE\_NAME = "external-secret-store"
DEFAULT\_AWS\_REGION = "eu-west-1"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def validate\_env\_vars(\*vars):
for var in vars:
if not os.environ.get(var):
raise ValueError(f"Environment variable '{var}' is not set.")
def load\_k8s\_config():
try:
logging.info("Loading in-cluster Kubernetes configuration...")
config.load\_incluster\_config()
except config.ConfigException:
logging.warning("Could not load in-cluster config. Falling back to kube-config.")
config.load\_kube\_config()
def list\_all\_secrets(secret\_manager):
try:
secrets = []
paginator = secret\_manager.get\_paginator('list\_secrets')
for page in paginator.paginate():
secrets.extend(page.get('SecretList', []))
logging.info(f"Retrieved {len(secrets)} secrets from AWS Secrets Manager.")
return secrets
except ClientError as e:
logging.error(f"Error retrieving secrets: {e}")
return []
def create\_k8s\_secret(k8s\_core\_v1, namespace, aws\_access\_key\_id, aws\_secret\_access\_key):
try:
k8s\_core\_v1.read\_namespaced\_secret(name=K8S\_SECRET\_NAME, namespace=namespace)
logging.info(f"Secret '{K8S\_SECRET\_NAME}' already exists in namespace '{namespace}'.")
except client.exceptions.ApiException as e:
if e.status == 404:
secret\_data = {
"access-key": base64.b64encode(aws\_access\_key\_id.encode()).decode(),
"secret-access-key": base64.b64encode(aws\_secret\_access\_key.encode()).decode(),
}
secret\_manifest = {
"apiVersion": "v1",
"kind": "Secret",
"metadata": {"name": K8S\_SECRET\_NAME, "namespace": namespace},
"data": secret\_data,
}
k8s\_core\_v1.create\_namespaced\_secret(namespace=namespace, body=secret\_manifest)
logging.info(f"Secret '{K8S\_SECRET\_NAME}' created successfully in namespace '{namespace}'.")
else:
logging.error(f"Error checking or creating secret '{K8S\_SECRET\_NAME}': {e}")
def create\_secret\_store(namespace, region):
secret\_store\_manifest = {
"apiVersion": "external-secrets.io/v1",
"kind": "SecretStore",
"metadata": {"name": SECRET\_STORE\_NAME, "namespace": namespace},
"spec": {
"provider": {
"aws": {
"service": "SecretsManager",
"region": region,
"auth": {
"secretRef": {
"accessKeyIDSecretRef": {"name": K8S\_SECRET\_NAME, "key": "access-key"},
"secretAccessKeySecretRef": {"name": K8S\_SECRET\_NAME, "key": "secret-access-key"},
}
},
}
},
},
}
try:
api = client.CustomObjectsApi()
api.create\_namespaced\_custom\_object(
group="external-secrets.io",
version="v1",
namespace=namespace,
plural="secretstores",
body=secret\_store\_manifest,
)
logging.info(f"SecretStore '{SECRET\_STORE\_NAME}' created successfully in namespace '{namespace}'.")
except client.exceptions.ApiException as e:
if e.status == 409:
logging.info(f"SecretStore '{SECRET\_STORE\_NAME}' already exists in namespace '{namespace}'.")
else:
logging.error(f"Error creating SecretStore in namespace '{namespace}': {e}")
def create\_external\_secret(namespace, secret\_name):
external\_secret\_manifest = {
"apiVersion": "external-secrets.io/v1",
"kind": "ExternalSecret",
"metadata": {"name": f"{AWS\_SECRET\_NAME\_PREFIX}{secret\_name}", "namespace": namespace},
"spec": {
"refreshInterval": "15s",
"secretStoreRef": {"name": SECRET\_STORE\_NAME, "kind": "SecretStore"},
"target": {"name": secret\_name},
"data": [
{"secretKey": "mongodb-username", "remoteRef": {"key": secret\_name, "property": "mongodb-username"}},
{"secretKey": "mongodb-password", "remoteRef": {"key": secret\_name, "property": "mongodb-password"}},
{"secretKey": "mongodb-host", "remoteRef": {"key": secret\_name, "property": "mongodb-host"}},
{"secretKey": "mongodb-root-password", "remoteRef": {"key": secret\_name, "property": "mongodb-root-password"}},
],
},
}
try:
api = client.CustomObjectsApi()
api.create\_namespaced\_custom\_object(
group="external-secrets.io",
version="v1",
namespace=namespace,
plural="externalsecrets",
body=external\_secret\_manifest,
)
logging.info(f"ExternalSecret '{AWS\_SECRET\_NAME\_PREFIX}{secret\_name}' created successfully in namespace '{namespace}'.")
except client.exceptions.ApiException as e:
if e.status == 409:
logging.info(f"ExternalSecret '{AWS\_SECRET\_NAME\_PREFIX}{secret\_name}' already exists in namespace '{namespace}'.")
else:
logging.error(f"Error creating ExternalSecret in namespace '{namespace}': {e}")
def process\_secret(secret, secrets\_manager\_client, core\_v1, aws\_access\_key\_id, aws\_secret\_access\_key, aws\_region):
secret\_name = secret.get('Name')
try:
secret\_value\_response = secrets\_manager\_client.get\_secret\_value(SecretId=secret\_name)
secret\_value = secret\_value\_response.get('SecretString') or base64.b64decode(
secret\_value\_response.get('SecretBinary')).decode('utf-8')
secret\_json = json.loads(secret\_value)
mongodb\_host = secret\_json.get('mongodb-host')
if not mongodb\_host:
logging.warning(f"'mongodb-host' not found in secret '{secret\_name}'. Skipping.")
return
namespace = mongodb\_host.split('.')[1]
logging.info(f"Processing secret '{secret\_name}' for namespace '{namespace}'.")
create\_k8s\_secret(core\_v1, namespace, aws\_access\_key\_id, aws\_secret\_access\_key)
create\_secret\_store(namespace, aws\_region)
create\_external\_secret(namespace, secret\_name)
except ClientError as e:
logging.error(f"Error retrieving content for secret '{secret\_name}': {e}")
def main():
validate\_env\_vars('AWS\_ACCESS\_KEY\_ID', 'AWS\_SECRET\_ACCESS\_KEY')
aws\_access\_key\_id = os.environ['AWS\_ACCESS\_KEY\_ID']
aws\_secret\_access\_key = os.environ['AWS\_SECRET\_ACCESS\_KEY']
aws\_region = os.environ.get('AWS\_REGION', DEFAULT\_AWS\_REGION)
load\_k8s\_config()
secrets\_manager\_client = boto3.client(
'secretsmanager',
aws\_access\_key\_id=aws\_access\_key\_id,
aws\_secret\_access\_key=aws\_secret\_access\_key,
region\_name=aws\_region,
)
core\_v1 = client.CoreV1Api()
secrets = list\_all\_secrets(secrets\_manager\_client)
for secret in secrets:
process\_secret(secret, secrets\_manager\_client, core\_v1, aws\_access\_key\_id, aws\_secret\_access\_key, aws\_region)
if \_\_name\_\_ == "\_\_main\_\_":
main()

Put the code in file `sync_external_secrets.py`.

Add this script to a ConfigMap:

wide760kubectl create configmap syncexternalsecretsaws -n external-secrets \
--from-file=sync\_external\_secrets.py=./sync\_external\_secrets.py \
--dry-run=client -o yaml | kubectl apply -f -

The CronJob is suspended, so it will not run on its schedule. Jobs must be triggered manually.

Create the cronjob:

wide760kubectl -n external-secrets apply -f - <<EOF
apiVersion: batch/v1
kind: CronJob
metadata:
name: sync-external-secrets-with-aws-sm
labels:
app: external-secrets-aws-sm
spec:
schedule: "0 \* \* \* \*"
suspend: true
jobTemplate:
spec:
template:
spec:
serviceAccountName: password-rotater
containers:
- name: sync-external-secrets-with-aws-sm
image: python:3.12-bookworm
volumeMounts:
- name: volume-sync-external-secrets-aws
mountPath: /app/sync\_external\_secrets.py
subPath: sync\_external\_secrets.py
imagePullPolicy: IfNotPresent
command: ["/bin/sh", "-c"]
args:
- pip install kubernetes && pip install boto3 && python /app/sync\_external\_secrets.py
env:
- name: AWS\_REGION
value: "eu-west-1"
- name: AWS\_ACCESS\_KEY\_ID
valueFrom:
secretKeyRef:
name: awssm-secret
key: access-key
- name: AWS\_SECRET\_ACCESS\_KEY
valueFrom:
secretKeyRef:
name: awssm-secret
key: secret-access-key
restartPolicy: OnFailure
volumes:
- name: volume-sync-external-secrets-aws
configMap:
name: syncexternalsecretsaws
EOF

### Results

After triggering the cronjob, a job will create the secrets in the Cluster.

Example external secrets resources:

wide760kubectl get externalsecrets -A | grep mongodb-pwd
ais-core ext-mongodb-pwd-extra-rotate-aisstream SecretStore external-secret-store 15s SecretSynced True
ais-core ext-mongodb-pwd-rotate-ais-stream-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-extra-rotate-aisengine SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-extra-rotate-aisrabbitmq SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-extra-rotate-area-monitor SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-extra-rotate-event-history SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-extra-rotate-ship-history SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-rotate-ais-rabbitmq-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-rotate-event-history-processor-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
ais-processing ext-mongodb-pwd-rotate-ship-history-processor-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
bunkerplanner ext-mongodb-pwd-extra-rotate-bunkerplanner SecretStore external-secret-store 15s SecretSynced True
bunkerplanner ext-mongodb-pwd-extra-rotate-fuelboss SecretStore external-secret-store 15s SecretSynced True
bunkerplanner ext-mongodb-pwd-rotate-bunkerplanner-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
bunkerplanner ext-mongodb-pwd-rotate-bunkerplanner-test-mongodb SecretStore external-secret-store 15s SecretSynced True
bunkerplanner ext-mongodb-pwd-rotate-fuelboss-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
bunkerplanner ext-mongodb-pwd-rotate-fuelboss-test-mongodb SecretStore external-secret-store 15s SecretSynced True
core-service ext-mongodb-pwd-extra-rotate-csi SecretStore external-secret-store 15s SecretSynced True
core-service ext-mongodb-pwd-extra-rotate-etapredictor SecretStore external-secret-store 15s SecretSynced True
core-service ext-mongodb-pwd-extra-rotate-poma SecretStore external-secret-store 15s SecretSynced True
core-service ext-mongodb-pwd-extra-rotate-portmatcher SecretStore external-secret-store 15s SecretSynced True
core-service ext-mongodb-pwd-extra-rotate-routescout SecretStore external-secret-store 15s SecretSynced True
core-service ext-mongodb-pwd-rotate-poma-sandbox-mongodb SecretStore external-secret-store 15s SecretSynced True
core-service ext-mongodb-pwd-rotate-routescout-graph-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-casey SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-datastore SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-portsupport SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-sednaintegration SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-shipsparelogistics SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-terminalplanner SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-vesselcompliance SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-extra-rotate-vesselmatcher SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-rotate-sednaintegration-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-rotate-vesselcompliance-demo-charterer-mongodb SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-rotate-vesselcompliance-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-rotate-vesselcompliance-poc-mongodb SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-rotate-vesselcompliance-staging-mongodb SecretStore external-secret-store 15s SecretSynced True
customer-apps ext-mongodb-pwd-rotate-vesselmatcher-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
general-service ext-mongodb-pwd-extra-rotate-datascience SecretStore external-secret-store 15s SecretSynced True
general-service ext-mongodb-pwd-extra-rotate-functionalmonitoring SecretStore external-secret-store 15s SecretSynced True
general-service ext-mongodb-pwd-extra-rotate-pdfrenderer SecretStore external-secret-store 15s SecretSynced True
general-service ext-mongodb-pwd-extra-rotate-scrapeshark SecretStore external-secret-store 15s SecretSynced True
general-service ext-mongodb-pwd-extra-rotate-terminallineup SecretStore external-secret-store 15s SecretSynced True
general-service ext-mongodb-pwd-rotate-functionalmonitoring-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
portcall ext-mongodb-pwd-extra-rotate-portcall-plus SecretStore external-secret-store 15s SecretSynced True
portcall ext-mongodb-pwd-extra-rotate-portpublisher SecretStore external-secret-store 15s SecretSynced True
portcall ext-mongodb-pwd-extra-rotate-portreporter SecretStore external-secret-store 15s SecretSynced True
portcall ext-mongodb-pwd-rotate-portreporter-testing-mongodb SecretStore external-secret-store 15s SecretSynced True
revents-core ext-mongodb-pwd-extra-rotate-reventsengine SecretStore external-secret-store 15s SecretSynced True
revents-core ext-mongodb-pwd-extra-rotate-vesselvoyage SecretStore external-secret-store 15s SecretSynced True
revents-core ext-mongodb-pwd-rotate-revents-engine-api-mongodb SecretStore external-secret-store 15s SecretSynced True
revents-core ext-mongodb-pwd-rotate-revents-vesselvoyage-mongodb SecretStore external-secret-store 15s SecretSynced True
students ext-mongodb-pwd-extra-rotate-atlas SecretStore external-secret-store 15s SecretSynced True
students ext-mongodb-pwd-extra-rotate-pdatool SecretStore external-secret-store 15s SecretSynced True
students ext-mongodb-pwd-rotate-atlas-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
students ext-mongodb-pwd-rotate-pdatool-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
testing2 ext-mongodb-pwd-rotate-functionalmonitoring-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-extra-rotate-cargo-optima SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-extra-rotate-servicevessel SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-extra-rotate-smartfleet SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-rotate-cargooptima-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-rotate-cargooptima-staging-mongodb SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-rotate-service-vessel-analysis-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-rotate-smartfleet-dev-mongodb SecretStore external-secret-store 15s SecretSynced True
voyage ext-mongodb-pwd-rotate-vesselvoyage-dev-mongodb SecretStore external-secret-store 15s SecretSynced True

Example secrets resources:

wide760kubectl get secrets -A | grep mongodb-pwd
ais-core mongodb-pwd-extra-rotate-aisstream Opaque 4 32m
ais-core mongodb-pwd-rotate-ais-stream-dev-mongodb Opaque 4 32m
ais-processing mongodb-pwd-extra-rotate-aisengine Opaque 4 32m
ais-processing mongodb-pwd-extra-rotate-aisrabbitmq Opaque 4 32m
ais-processing mongodb-pwd-extra-rotate-area-monitor Opaque 4 32m
ais-processing mongodb-pwd-extra-rotate-event-history Opaque 4 32m
ais-processing mongodb-pwd-extra-rotate-ship-history Opaque 4 32m
ais-processing mongodb-pwd-rotate-ais-rabbitmq-dev-mongodb Opaque 4 32m
ais-processing mongodb-pwd-rotate-event-history-processor-dev-mongodb Opaque 4 32m
ais-processing mongodb-pwd-rotate-ship-history-processor-dev-mongodb Opaque 4 32m
...

## Trigger rotating MongoDB passwords

***This script is a work in progress. While it doesn't currently restart deployments, find deployments by a secret name or updating the user’s passwords in the MongoDB databases, it effectively demonstrates the workflow.***

Script: rotating passwords

pywide760import base64
import secrets
import json
import logging
import os
import string
import boto3
from botocore.exceptions import ClientError
from kubernetes import client, config
DEFAULT\_AWS\_REGION = "eu-west-1"
def generate\_password(length=32):
characters = string.ascii\_letters + string.digits
return ''.join(secrets.choice(characters) for \_ in range(length))
def validate\_env\_vars(\*vars):
for var in vars:
if not os.environ.get(var):
raise ValueError(f"Environment variable '{var}' is not set.")
def load\_k8s\_config():
try:
logging.info("Loading in-cluster Kubernetes configuration...")
config.load\_incluster\_config()
except config.ConfigException:
logging.warning("Could not load in-cluster config. Falling back to kube-config.")
config.load\_kube\_config()
def list\_all\_secrets(secret\_manager):
try:
local\_secrets = []
paginator = secret\_manager.get\_paginator('list\_secrets')
for page in paginator.paginate():
local\_secrets.extend(page.get('SecretList', []))
logging.info(f"Retrieved {len(local\_secrets)} secrets from AWS Secrets Manager.")
return local\_secrets
except ClientError as e:
logging.error(f"Error retrieving secrets: {e}")
return []
def rotate\_passwords(secret, secrets\_manager\_client):
secret\_name = secret.get('Name')
logging.info(f'secret\_name: {secret\_name}')
try:
secret\_value\_response = secrets\_manager\_client.get\_secret\_value(SecretId=secret\_name)
secret\_value = secret\_value\_response.get('SecretString') or base64.b64decode(
secret\_value\_response.get('SecretBinary')).decode('utf-8')
secret\_json = json.loads(secret\_value)
mongodb\_host = secret\_json.get('mongodb-host')
if not mongodb\_host:
logging.warning(f"'mongodb-host' not found in secret '{secret\_name}'. Skipping.")
return
namespace = mongodb\_host.split('.')[1]
logging.info(f"Processing secret '{secret\_name}' for namespace '{namespace}'.")
# Change the password for the user which not active.
new\_password = generate\_password()
current\_user = secret\_json.get('mongodb-username')
logging.info(f'Current user: {current\_user}')
if secret\_json.get("mongodb-username-rotate1") == current\_user:
# Rotate to mongodb-username-rotate2
secret\_json["mongodb-password-rotate2"] = new\_password
user2 = secret\_json["mongodb-username-rotate2"]
# todo: We need to change the password for MongoDB user 'user 2'. As this user account is inactive,
# there will be no impact on the application.
# todo: The MongoDB root password is available in the secret as 'mongodb-root-password'.
logging.info(f"Changing password for user '{user2}' in MongoDB.")
secrets\_manager\_client.update\_secret(
SecretId=secret\_name,
SecretString=json.dumps(secret\_json)
)
logging.info(f"Secret '{secret\_name}' updated successfully for user 2.")
# Change the active user to rotate2.
secret\_json["mongodb-username"] = user2
secret\_json["mongodb-password"] = new\_password
secrets\_manager\_client.update\_secret(
SecretId=secret\_name,
SecretString=json.dumps(secret\_json)
)
logging.info(f"Main user and password of secret '{secret\_name}' updated successfully.")
# todo: We need to verify that the External Secrets Operator has successfully synced the secret in the namespace.
# todo: We need to find the deployment that is using this secret and the secret name is known.
# todo: When changed restart the deployment.
# Rotate the password for user 1
secret\_json["mongodb-password-rotate1"] = generate\_password()
secrets\_manager\_client.update\_secret(
SecretId=secret\_name,
SecretString=json.dumps(secret\_json)
)
logging.info(f"Secret '{secret\_name}' updated successfully for user 1.")
else:
# Rotate to mongodb-username-rotate1
secret\_json["mongodb-password-rotate1"] = new\_password
user1 = secret\_json["mongodb-username-rotate1"]
# todo: We need to change the password for MongoDB user 'user 1'. As this user account is inactive,
# there will be no impact on the application.
# todo: The MongoDB root password is available in the secret as 'mongodb-root-password'.
logging.info(f"Changing password for user '{user1}' in MongoDB.")
secrets\_manager\_client.update\_secret(
SecretId=secret\_name,
SecretString=json.dumps(secret\_json)
)
logging.info(f"Secret '{secret\_name}' updated successfully for user 2.")
# Change the active user to rotate2.
secret\_json["mongodb-username"] = user1
secret\_json["mongodb-password"] = new\_password
secrets\_manager\_client.update\_secret(
SecretId=secret\_name,
SecretString=json.dumps(secret\_json)
)
logging.info(f"Main user and password of secret '{secret\_name}' updated successfully.")
# todo: We need to verify that the External Secrets Operator has successfully synced the secret in the namespace.
# todo: We need to find the deployment that is using this secret and the secret name is known.
# todo: When changed restart the deployment.
# Rotate the password for user 2
secret\_json["mongodb-password-rotate2"] = generate\_password()
secrets\_manager\_client.update\_secret(
SecretId=secret\_name,
SecretString=json.dumps(secret\_json)
)
logging.info(f"Secret '{secret\_name}' updated successfully for user 2.")
except ClientError as e:
logging.warning(f"Error retrieving content for secret '{secret\_name}': {e}")
def main():
validate\_env\_vars('AWS\_ACCESS\_KEY\_ID', 'AWS\_SECRET\_ACCESS\_KEY')
aws\_access\_key\_id = os.environ['AWS\_ACCESS\_KEY\_ID']
aws\_secret\_access\_key = os.environ['AWS\_SECRET\_ACCESS\_KEY']
aws\_region = os.environ.get('AWS\_REGION', DEFAULT\_AWS\_REGION)
load\_k8s\_config()
secrets\_manager\_client = boto3.client(
'secretsmanager',
aws\_access\_key\_id=aws\_access\_key\_id,
aws\_secret\_access\_key=aws\_secret\_access\_key,
region\_name=aws\_region,
)
secrets = list\_all\_secrets(secrets\_manager\_client)
for secret in secrets:
rotate\_passwords(secret, secrets\_manager\_client)
if \_\_name\_\_ == "\_\_main\_\_":
main()

Put the code in file `rotate_passwords.py`.

Add this script to a ConfigMap:

wide760kubectl create configmap rotatepasswords -n external-secrets \
--from-file=rotate\_passwords.py=./rotate\_passwords.py \
--dry-run=client -o yaml | kubectl apply -f -

The CronJob is suspended, so it will not run on its schedule. Jobs must be triggered manually.

Create the cronjob:

wide760kubectl -n external-secrets apply -f - <<EOF
apiVersion: batch/v1
kind: CronJob
metadata:
name: rotate-mongodb-passwords-with-aws-sm
labels:
app: rotate-mongodb-passwords-with-aws-sm
spec:
schedule: "0 \* \* \* \*"
suspend: true
jobTemplate:
spec:
template:
spec:
serviceAccountName: password-rotater
containers:
- name: rotate-mongodb-passwords-with-aws-sm
image: python:3.12-bookworm
volumeMounts:
- name: volume-sync-rotate-passwords-aws
mountPath: /app/rotate\_passwords.py
subPath: rotate\_passwords.py
imagePullPolicy: IfNotPresent
command: ["/bin/sh", "-c"]
args:
- pip install kubernetes && pip install boto3 && python /app/rotate\_passwords.py
env:
- name: AWS\_REGION
value: "eu-west-1"
- name: AWS\_ACCESS\_KEY\_ID
valueFrom:
secretKeyRef:
name: awssm-secret
key: access-key
- name: AWS\_SECRET\_ACCESS\_KEY
valueFrom:
secretKeyRef:
name: awssm-secret
key: secret-access-key
restartPolicy: OnFailure
volumes:
- name: volume-sync-rotate-passwords-aws
configMap:
name: rotatepasswords
EOF

### Results:

The screenshot shows the situation before the password rotation.

The screenshot shows the situation after.

The screenshot below shows that the Kubernetes secret has been successfully synchronized as well.

## Helm charts update

The password rotation works independently from the application. We must adjust the Helm chart to use external secrets.

In `skeleton-mongo-app` add a switch in the values.yaml file. Below an example.

**values.yaml**

yamlwide760mongodb:
enabled: true
setEnv: true
.....
externalSecret: true
externalSecretName: mongodb-pwd-extra-rotate-smartfleet
....
host: ""
hostedzone: eks-dev.teqplay
persistence: {}
auth: {}
resources:
requests:
cpu: 100m
memory: 512Mi
limits:
memory: 512Mi

The changes could be similar to what's shown below.

**deployment.yaml**

wide760apiVersion: apps/v1
kind: Deployment
metadata:
name: {{ .Release.Name }}
...
{{- if .Values.mongodb.externalSecret }}
- name: "MONGODB\_USERNAME"
valueFrom:
secretKeyRef:
name: {{ .Values.mongodb.externalSecretName }}
key: "mongodb-username"
- name: "MONGODB\_PASSWORD"
valueFrom:
secretKeyRef:
name: {{ .Values.mongodb.externalSecretName }}
key: "mongodb-password"
{{ else }}
- name: "MONGODB\_USERNAME"
value: {{ .Values.mongodb.auth.username }}
- name: "MONGODB\_PASSWORD"
valueFrom:
secretKeyRef:
name: {{ print .Release.Name "-mongodb" }}
key: "mongodb-password"
{{- end }}