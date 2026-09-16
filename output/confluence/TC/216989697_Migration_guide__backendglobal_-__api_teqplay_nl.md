---
id: confluence:216989697
source: confluence
type: page
space: TC
title: 'Migration guide: backendglobal -> api.teqplay.nl'
author: Former user (Deleted)
date: '2023-10-02'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/216989697
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/216989697
---
# Migration guide: backendglobal -> api.teqplay.nl

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/216989697  

## Content

In general the migration is as simple as changing the URL from:

`https://backendglobal.teqplay.nl` to `https://api.teqplay.nl/v0/global`

And also sending the appropriate (new) credentials.

We’ll now go over all the steps to both authenticate and use the API, highlighting the changes between the two URLs.

## 1. Authenticating

| **Old URL** | **New URL** |
| --- | --- |
| `POST https://backendglobal.teqplay.nl/auth/login` | `POST https://api.teqplay.nl/v0/global/auth/login` |

The request body stays the same, albeit with updated credentials:

json{
"username": "<username/email>",
"password": "<password>"
}

This gives the following response:

json{
"userName": "<username/email>",
"token": "<token>",
"refreshToken": "<refreshToken>",
"expiresInSeconds": 3600,
"createdAt": "<ISO 8601 date time format>"
}

The access `token` can be used to make requests and will expire after an hour, whereas the `refreshToken` can be used to refresh the `token` up to a day after logging in.

To refresh the access token:

| **Old URL** | **New URL** |
| --- | --- |
| `POST https://backendglobal.teqplay.nl/auth/loginWithRefreshToken` | `POST https://api.teqplay.nl/v0/global/auth/loginWithRefreshToken` |

The request body stays the same:

json{
"username": "<username/email>",
"refreshToken": "<refreshToken from previous /auth/login request>"
}

The response equals the response of `/auth/login`. The new `token` can then be used to make requests.

## 2. Making requests

Making a request to for example: `/ship/244060924`

| **Old URL** | **New URL** |
| --- | --- |
| `GET https://backendglobal.teqplay.nl/ship/244060924` | `GET https://api.teqplay.nl/v0/global/ship/244060924` |

Including the `Authorization` header with the content: `Bearer <token>.`

When you get a response code 401 Unauthorized, you should first try refreshing your access token using the `/auth/loginWithRefreshToken` endpoint. If that call is successful you should use your new `token` in the subsequent requests. If that call was not successful, you should login again using the `/auth/login` endpoint.