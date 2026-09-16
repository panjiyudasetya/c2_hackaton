---
id: confluence:652116008
source: confluence
type: page
space: TC
title: Automatic token replacement in Postman
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652116008
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652116008
---
# Automatic token replacement in Postman

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652116008  

## Content

It is possible in Postman to let it automatically set the Authorization token for every collection you have.

To give you feeling how this works, first an overview of the concept: You have different environments. In my case this are 3:

* localhost
* dev
* live

For all three you create an environment in Postman, all with an `url` and `token` variable. The url variable is the base url for every call you make in this environment, e.g. `http://backenddev.teqplay.nl`. The token variable will contain the current authentication token for the calls.

Lets try to think through a example where you want to do a call to the live environment. You open up Postman and you select the live environment. As you do not have a authentication token you do the authentication call for the first time. This causes the `token` variable to be set for future calls to the live environment. Now you select the call you want to do and fire it. No hassle with copy/pasting tokens anymore!

## So, how to setup?

You have to do this for every environment you want to create.

1. First create a environment in Postman, in the upper right corner. Click on Manage Enviroments
2. Secondly, click on add and give a name for the environment. I called mine `localhost`, `dev` and `live`, but you can call it anything you like.
3. Create a key/value pair with the name `token`. It doesn't need a value.
4. Create a key/value pair with the name `url`. Add the base url of the environement, e.g. `http://backenddev.teqplay.nl`.
5. Go to your `auth/login` resource call (which of course you already defined in a collection).
6. Select the Tests tab
7. Add this piece of code:

   var jsonData = JSON.parse(responseBody);
   postman.setEnvironmentVariable("token", jsonData.token);

   This will set the environment variable `token` with the value of the token you just received in the response of the call.
8. Instead of copy/paste the token, you can now just use an environment variable where you normally would paste your token. Change all the Authorization Headers to {{token}}.
9. Change all the base urls to {{url}} to make the calls interchangeable.
10. Don't forget to select the environment you desire in the upper left corner.