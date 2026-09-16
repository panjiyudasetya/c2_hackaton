---
id: confluence:1293910020
source: confluence
type: page
space: TC
title: Keycloak Integrations
author: Ryan Kharisma Rakhmat
date: '2026-08-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1293910020
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1293910020
---
# Keycloak Integrations

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1293910020  

## Content

### Backgrounds

Accessing the API from the Client side needs some sort of security mechanism. The Bearer token Authorizations with JWT technology are usually implemented in a lot of companies todays. Auth0 is one of the standards for ID as a services in cloud architecture. Keycloak is the one of open-source solutions for the Auth0 implementations. So we are going to secure the API with the Authorizations mechanism with Keycloak.

### Sequence Diagram

The Client will post the auth to the keycloak with the client\_id, user, and password. Then Keycloak will be return the JWT Token for authorizations that can be used to login. After that the Client will use the token to Get the API data to PostgREST. So from the that, the token will be verified by PostgREST whether or not the token are authorized to the specific API. Then PostgREST will query data from postgres datamart to get the requested KPI and also send back the data in json format into the Client.

### Local Implementations

We have 3 components here for our purposes as below:

|  |  |  |
| --- | --- | --- |
| **Component** | **Version / Image** | **Role** |
| PostgreSQL | postgres:16 | Primary data store; enforces Row Level Security (RLS) per request |
| PostgREST | postgrest/postgrest:latest (resolved 14.15) | Auto-generated REST API in front of Postgres; validates JWTs |
| Keycloak | <http://quay.io/keycloak/keycloak:26.0> | Identity provider (IdP); issues signed JWTs (RS256) via OIDC |

**Keycloak Configurations**

1. Create a Client named `postgrest` on Demo Realm

2. Create a Roles `authenticated` in the postgrest client

3. Create a users by clicking the `Add user` blue button

4. Assign postgrest `authenticated` roles to users

5. Some JWT sample exported (after the users is successfully login to keycloak)

jsonwide760true{
"exp": 1784710402,
"iat": 1784710102,
"jti": "d979f808-0826-4ac9-847d-873b007df345",
"iss": "http://localhost:8080/realms/demo",
"aud": "api",
"typ": "Bearer",
"azp": "postgrest",
"sid": "0a7d2df0-c02c-48cb-8de0-32494fa77acf",
"resource\_access": {
"postgrest": {
"roles": [
"authenticated"
]
}
},
"scope": "api"
}

**Postgrest Configurations**

To get the jwk just hit this url: <http://localhost:8080/realms/demo/protocol/openid-connect/certs>

Because the jwk.json here is the public key certificates to use by the postgrest for communicating with keycloak.

postgrest.conf

wide760truedb-uri = "postgres://authenticator:secret@postgres:5432/appdb"
db-schemas = "api"
db-anon-role = "web\_anon"
jwt-secret = "@/etc/jwk.json"
jwt-aud = "api"
jwt-role-claim-key = ".resource\_access.postgrest.roles[0]"
server-port = 3000

**Postgresql DB Preparations**

Run the query below before we are playing around with postgrest and keycloak:

init.sql

sqlwide760trueCREATE ROLE authenticator LOGIN PASSWORD 'secret';
CREATE ROLE web\_anon NOLOGIN;
CREATE ROLE authenticated NOLOGIN;
CREATE ROLE admin NOLOGIN;
GRANT web\_anon TO authenticator;
GRANT authenticated TO authenticator;
GRANT admin TO authenticator;
CREATE SCHEMA api;
GRANT USAGE ON SCHEMA api TO web\_anon;
GRANT USAGE ON SCHEMA api TO authenticated;
GRANT USAGE ON SCHEMA api TO admin;
CREATE TABLE api.todo
(
id serial PRIMARY KEY,
owner uuid NOT NULL,
task text NOT NULL
);
GRANT SELECT ON api.todo TO web\_anon;
GRANT
SELECT,
INSERT,
UPDATE,
DELETE
ON api.todo
TO authenticated;
GRANT USAGE, SELECT ON api.todo\_id\_seq TO authenticated;

seed.sql

sqlwide760trueINSERT INTO api.todo(owner, task)
VALUES
(
'11111111-1111-1111-1111-111111111111',
'Learn PostgREST'
),
(
'22222222-2222-2222-2222-222222222222',
'Learn Keycloak'
);

**Sample API Tests**

***login***

**POST** to the url: localhost:8080/realms/demo/protocol/openid-connect/token

jsonwide760true{
"access\_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI3eGJYS09rMTJTZDFicFcxOTYxNkFVblRwcjRLZERSdnFtZi11aGQzNWZRIn0.eyJleHAiOjE3ODQ4OTAxODYsImlhdCI6MTc4NDg4OTg4NiwianRpIjoiMzYyMGRhYmUtOTViZi00OWY3LTkyZWUtOGEwYzZlOTYzMTg0IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9kZW1vIiwiYXVkIjoiYXBpIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoicG9zdGdyZXN0Iiwic2lkIjoiMThkZDVlODctMDcyMy00NjJjLTkxZjAtNjdjMjEzMjkyYjM1IiwicmVzb3VyY2VfYWNjZXNzIjp7InBvc3RncmVzdCI6eyJyb2xlcyI6WyJhdXRoZW50aWNhdGVkIl19fSwic2NvcGUiOiJhcGkifQ.QWD2raWxiFG4i3TgDgGWANM4ZnitnflOlRFLX3-kpxXNUDau8LBnJp9og0i1ykz02VtsAB7MIDUdCl4jskflaXUtg\_\_XjD7iAuSkY00qJ76URhpaq8yi5rJzUmrJ5jlxwXNZ1MhHKiaf7d9LsEyJk6zzFfWMDge8aWrInV7BP2p\_nm6AN7sY\_KpoUt3qnTJiZ1YA\_HsrDw5duEl\_KJ2UQe7tBbFSvNL-Q6eQAD5LpH7cksJPgCOWkcqChhMVd5kh8\_NY-yoMp8hOdzDcqceYf6chWrZeuzV1VG21o07ewzTo6p9xPEm452i5olQZdjni71K1fv6-N8n8c4ld2GlqZw",
"expires\_in": 300,
"refresh\_expires\_in": 1800,
"refresh\_token": "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2OTE2YThhZS05MmVkLTRmNzctOWUxMS02MjJiMmE3NzkwMWMifQ.eyJleHAiOjE3ODQ4OTE2ODYsImlhdCI6MTc4NDg4OTg4NiwianRpIjoiZDA4Zjk4NzItZmJjZS00ZWJjLWI1YmItYjVmZjA3NjQzZTY4IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9kZW1vIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9kZW1vIiwidHlwIjoiUmVmcmVzaCIsImF6cCI6InBvc3RncmVzdCIsInNpZCI6IjE4ZGQ1ZTg3LTA3MjMtNDYyYy05MWYwLTY3YzIxMzI5MmIzNSIsInNjb3BlIjoiYXBpIn0.-LofLfflV2I5ivUw2KMVRsRmRirV2XQWsJP333HYm3o8mG1MJ3n-HAULe\_1xKWN5T2MX-O9bn6vpeDeBglyuzw",
"token\_type": "Bearer",
"not-before-policy": 0,
"session\_state": "18dd5e87-0723-462c-91f0-67c213292b35",
"scope": "api"
}

***get API data***

**GET** to the url localhost:3000/todo

jsonwide760true[
{
"id": 33333333,
"owner": "b3016cdf-3733-418a-828e-d4409714a3f9",
"task": "Learn postgREST"
},
{
"id": 3,
"owner": "11111111-1111-1111-1111-111111111111",
"task": "Wire up Keycloak JWT"
},
{
"id": 4,
"owner": "11111111-1111-1111-1111-111111111111",
"task": "verify postgrest client rename"
}
]

### Dev Configurations

**Keycloak**

* create a new client named `postgrest`
* create a new roles in the postgrest client named `postgrest_kpi`
* grant the `data-engineering` service account for the new `postgrest_kpi` roles.

**PostgREST**

wide760true PGRST\_DB\_POOL: '10'
PGRST\_DB\_SCHEMAS: gold,silver
PGRST\_SERVER\_HOST: 0.0.0.0
PGRST\_JWT\_SECRET: some jwt from this url-> https://keycloakdev.teqplay.nl/realms/dev/protocol/openid-connect/certs
PGRST\_JWT\_AUD: api
PGRST\_JWT\_ROLE\_CLAIM\_KEY: .resource\_access.postgrest.roles[0]

**PostgreSQL**

sqlwide760trueDO
$$
BEGIN
IF NOT EXISTS (SELECT FROM pg\_catalog.pg\_roles WHERE rolname = 'postgrest\_kpi') THEN
CREATE ROLE postgrest\_kpi NOLOGIN;
END IF;
END
$$;
GRANT postgrest\_kpi TO api\_authenticator;
GRANT USAGE ON SCHEMA gold TO postgrest\_kpi;
GRANT SELECT ON
gold.kpi\_metric\_registry,
gold.kpi\_anchorage\_duration\_monthly,
gold.kpi\_portcall\_duration\_monthly,
gold.kpi\_overall\_port\_performance\_monthly,
gold.kpi\_berth\_occupancy\_monthly,
gold.kpi\_portcall\_performance\_monthly,
gold.kpi\_berth\_stay\_duration\_monthly
TO postgrest\_kpi;

#### Test the API in Postman

At first we need to get the token first with authentication calls to the internal API url `v1/auth/token` Then we are using the generated token to be put on the Authorizations here with type Bearer Token:

If we are hit the API without the token, we will get the `Anonymous acess is disabled` messages:

### Live Configurations

Same as dev configs but with different realm and environment.

* + Realm = master
  + Environment = Live

Get the certs from this url :

wide760truehttps://keycloak.teqplay.nl/realms/prod/protocol/openid-connect/certs

And here is the sample configs of the PostgREST :

wide760trueapiVersion: v1
kind: ConfigMap
metadata:
name: postgrest-config
namespace: data-engineering
uid: 7ee8916c-8315-42bb-8c32-72bd2a1da7c6
resourceVersion: '937710667'
creationTimestamp: '2026-05-29T10:21:04Z'
labels:
k8slens-edit-resource-version: v1
annotations:
kubectl.kubernetes.io/last-applied-configuration: >
{"apiVersion":"v1","data":{"PGRST\_DB\_ANON\_ROLE":"api\_web\_anon","PGRST\_DB\_POOL":"10","PGRST\_DB\_SCHEMAS":"silver,gold","PGRST\_SERVER\_HOST":"0.0.0.0"},"kind":"ConfigMap","metadata":{"annotations":{},"name":"postgrest-config","namespace":"data-engineering"}}
selfLink: /api/v1/namespaces/data-engineering/configmaps/postgrest-config
spec: {}
data:
PGRST\_DB\_ANON\_ROLE: api\_web\_anon #this line is to enable anonymous users.
PGRST\_DB\_POOL: '10'
PGRST\_DB\_SCHEMAS: gold,silver
PGRST\_JWT\_AUD: api
PGRST\_JWT\_ROLE\_CLAIM\_KEY: .resource\_access.postgrest.roles[0]
PGRST\_JWT\_SECRET: >
some public certs paste here from the url above.
PGRST\_SERVER\_HOST: 0.0.0.0