---
id: confluence:821919745
source: confluence
type: page
space: TC
title: Generate APNS FCM Push certificates
author: Joost Laurman
date: '2025-08-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/821919745
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/821919745
---
# Generate APNS FCM Push certificates

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/821919745  

## Content

Every year we need to renew the FCM Firebase push certificates for our apps.

Currently this contains of:

* RiverGuide
* Port Reporter

To do so, you need a Mac.

## Generate a push certificate

You first need to create a Certificate Signing Request `.certSigningRequest` File (CSR) on macOS.

1. Open Keychain Access: **Applications > Utilities > Keychain Access**
2. Launch the Certificate Assistant

* From menu bar, click: **Keychain Access > Certificate Assistant > Request a Certificate From a Certificate Authority…**

Mac Keychain Access

3. Enter Your Information

Fill in the required fields:

* **User Email Address**: `[email protected]`
* **Common Name**: Your name or the name for the certificate
* **CA Email Address**: Leave this blank
* **Request is**: Select **Saved to disk**

Certificate Assistent Window

Certificate Assistant window

4. Click Continue

* Choose a location to save the `.certSigningRequest` file
* Click **Save** to finish

You now have your `.certSigningRequest` file ready to use!

Now go the **Apple Developer Portal → Certificates, Identifiers & Profiles → Identifiers**

Click on the app you want to generate the new push certificate for, e.g. **nl-teqplay-portreporter.**

Go all the way down, to **Push Notifications → Edit**

This opens up a small modal where you can create certificates. We are gonna create a certificate for both Development and Production. Click on **Create Certificate** under **Development SSL Certificate**

Now click **Choose File** and select the `certSigningRequest` you created in step 1. Now click **Continue**. It generated the certificate now and gives you an option to download this **.cer** file. Click on **Download** and save it somewhere you can remember.

Import the downloaded **\*.cer** file into your Keychain.

It now shows up in the Keychain. The development certificate shows up as `Apple Sandbox Push Service nl.teqplay.portreporter` and the production certificate will show up as `Apple Push Services nl.teqplay.portreporter`.

Right click on the certificate you want to generate a `p12` file for **→ export “Apple Sandbox Push Services nl.teqplay.portreporter”…**

You can give it a password, but that’s not required. Click on **Save** → **OK**.

## Uploading it in Firebase Console

Go to the [Firebase Console](https://console.firebase.google.com).

Select the app you want to update the certificate for, in our case **Port Reporter**.

Firebase App Console

Go to **Project Settings**

Go to Project Settings

Go to the **Cloud Messaging** tab

Go the Cloud Messaging tab

Here you’ll see a card with **Apple app configuration.** Under the **APNs Certificates → Development APNs certificate -> Update.** (or if you update the Production certificate do it for the Production APNs certificate)

Click on Update

Here upload the p12 certificate you just created and click on **Upload.**

Now it will show up with the updated ‘Valid Until’.

Now valid until September 6, 2026!

Repeat the process but now for **Production**!