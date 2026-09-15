---
id: confluence:160727044
source: confluence
type: page
space: TC
title: Rotating all secrets for a fastlane project
author: Damon Asberg
date: '2025-01-06'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160727044
explicit_links: []
---
# Rotating all secrets for a fastlane project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160727044  

## Content

Hopefully you don’t have to follow this page much, since that would mean our secrets get leaked a lot

This document will be divided into an Android section and an iOS section, and explain how to rotate/renew any secret related to the project that you might want to do.

**Table of Contents**

17

## Android

Only the Google Play Store Account Owner (Richard) has permission to perform these actions. There is no way as of today () to give these permissions to other users.

There are 2 “secrets” used for Android projects using fastlane.

* Google Play Store API key
* Android Keystore used to sign the apps

### Google Play Store API key

This key is used by fastlane to upload app binaries to Google Play Store via the command line. It can even do the full sending to Google itself, but we are limiting that to only be used manually.

For this, we need to first revoke the access to this API key. It should be targeted to all apps, so inside `android-context`, remove the `ANDROID_API_JSON` environment variable.

#### ANDROID\_API\_JSON

<https://www.youtube.com/watch?v=Ls2wkAwXftk>

##### Step 1: Revoke access of the old API key

1. Go to Google Cloud Console, the Teqplay organisation **Service Accounts**. <https://console.cloud.google.com/projectselector2/iam-admin/serviceaccounts?organizationId=641142978442>
2. This should put you inside the Service Accounts list for the Teqplay organisation.  
   There should be an account called along this lines of `fastlane@api-......iam.gserviceaccount.com`.
3. Click on the 3 vertical dots at the end and click Delete or Disable, pending on what we want to do with the old key.

##### Step 2: Generate a new service account and JSON API key

These steps are taken from the official fastlane docs and adjusted because Google Play Console has changed layout like 10 times since then: <https://docs.fastlane.tools/actions/supply/#setup>

1. Go to [https://play.google.com/console/u/0/developers/6863461032516241881/api-access](https://play.google.com/console/u/1/developers/6863461032516241881/api-access)  
   This screen shows API keys / Service accounts related to the whole organisation.
2. Click Create Service Account
3. Follow the steps inside the dialog; click the link to Google Cloud Platform

   1. Click the Create Service Account button at the top of the window.
   2. Fill in a relevant **Service account name**, something with `fastlane` preferably. Remember it for a later step to make identifying it later easy.
   3. For the Service account ID, verify that the name of the service account ends with: `6863461032516241881-{xxx}.iam-gserviceaccount.com`  
      6863461032516241881 is the Teqplay Developer Account ID, if it does not match you will need to select a different account or environment, that can be done clicking on the area looking similar to this saying “Google Play Android Developer” in the following image:
   4. Add a description to the service account, here is one you can copy and paste:

      Service account used for Automatic deployment of Android applications through CI using fastlane.
   5. Click Create and continue
   6. Select the role `Service account user` and click Continue
   7. We have tried adding developer accounts to utilise the key, but it is not required since the API key is through the organisation and not an individual account. Developers still cannot access the key through their Google Cloud Console    
        
      So we can click Done.
   8. Click on the 3 vertical dots on the right, click Manage keys, Add key → Create new key
   9. Make sure the new key is saved in **JSON** format, and click Create.
   10. Save this file on Google Drive: <https://drive.google.com/drive/folders/16tO0HrWtyIgRqQv31gys1IpKF5OhRj2n?usp=share_link>  
       The contents of this file will be added as the `ANDROID_API_JSON` environment variable in the next step, so keep it around (or pass it to a developer who will do it for you)!
4. Return to the Google Play Console tab
5. Refresh the page or click Refresh service accounts underneath **Credentials > Service accounts**
6. Confirm that the newly added service account has been added, and for this account click the corresponding Manage Play Console permissions button on the right side
7. Choose the required permissions for this service account.   
     
   It is recommended to put permissions out for the whole account, and not per app as this will reduce overhead of doing this for every app every time we add a new one for automatisation.  
   Fastlane recommends `Admin (all permissions)`, but after viewing them myself I think we only need the following:

   * `View app information`
   * `Manage store presence`
   * Everything underneath `Releases`
8. Click Invite user to finish

##### Step 3: Add the API key contents as environment variable

1. Copy the file contents of the JSON file generated at the previous step (saved in <https://drive.google.com/drive/folders/16tO0HrWtyIgRqQv31gys1IpKF5OhRj2n?usp=share_link>)
2. Add the full contents to the `android-context` as `ANDROID_API_JSON` environment variable.

That is it, now run `fastlane android deploy_build` and it should work like a charm!

### Android keystore

This can only be done once a year per Google Policy.

This has to be done per application, as the old keystore has been discontinued.

## iOS

For a simple iOS project using fastlane many different secrets are used. These are all related to the usage of certificates and the signing of an application.

This has only been done on a Mac OS device, it should be possible on a Windows machine and only step 8 will be different

### App Store API key

Inside our CI environment we use the `ios-context` to provide us with the API key used to communicate with the App Store, generate certificates and provisioning profiles used by our apps.

#### FASTLANE\_IOS\_CERT\_ISSUER\_ID

This variable cannot be changed as it is bound to our company id inside the App Store.

This variable is the `Issuer ID` that is bound to the Teqplay B.V. company inside App Store Connect. When visiting <https://appstoreconnect.apple.com/access/api>, the Issuer ID you have when generating API keys is shown at the top.

#### FASTLANE\_IOS\_CERT\_KEY\_ID and FASTLANE\_IOS\_CERT\_PKEY

The `key_id` is the unique identifier of an App Store Connect API key. This API key is used to communicate with the App Store to generate certificates and provisioning profiles.

The `FASTLANE_IOS_CERT_PKEY` is the raw content of the API key, encoded in Base64.

##### Step 1: Revoking access of the old key

1. Go to <https://appstoreconnect.apple.com/access/integrations/api>
2. Find the key used inside `ios-context` and match it with the final characters inside the `Key ID` column
3. Click edit in the top right
4. Select the key
5. Click Revoke key

##### Step 2: Generating a new key

1. Go to <https://appstoreconnect.apple.com/access/api>
2. Fill in a name so you can identify it properly, I usually named it `Fastlane iOS deployment key`
3. Set `Access` to `App Manager`
4. Click `Generate`
5. Copy the `Key ID` of your newly generated API key and paste it into the `FASTLANE_IOS_CERT_KEY_ID` environment variable inside `ios-context`
6. Click `Download API key`  
    This can only be done once, so if you lose the private key, the API key is unusable.
7. Encode the full contents of the file to Base64  
   `base64 -i AuthKey_XXXXXXXXX.p8 > encoded_key.b64`  
   This is necessary as the `.p8` file is multi-line, which if directly pasted as an environment variable will cause errors when converting the line breaks to `\n` or spaces.
8. Copy the full contents of the `encoded_key.b64` file and paste it into the `FASTLANE_IOS_CERT_PKEY` environment variable inside `ios-context`.

That should be it! This is really step 1 as it will allow you to regenerate any new certificates and profiles with this new API key. Which is in fact the next step…

### iOS certificates using match

Match is included inside fastlane and handles all the certificates and profiles that are usually manually managed. We need to revoke and change several items related to this.

#### Revoke certificates

The distribution certificate is linked to all of the provisioning profiles that are generated for each app. If you decide to revoke this certificate, you will need to regenerate **all** provisioning profiles for each individual app.

One of the most important steps is to actually revoke any of the previously used certificates. We will be regenerating certificates using match, so this will not be as impactful as it might seem.

There are 2 certificates that need to be revoked:

* Development certificate
* Distribution certificate

##### Step 3: Revoke development certificate

1. Go to <https://developer.apple.com/account/resources/certificates/list>
2. Find the `Created via API` certificate with type `Development`, created by `API Key: XXXX...`
3. Click on the certificate
4. Click revoke

##### Step 4: Revoke distribution certificate

1. Go to <https://developer.apple.com/account/resources/certificates/list>
2. Find the `Teqplay BV` certificate with type `Distribution`, created by `API Key: XXXX...`
3. Click on the certificate
4. Click revoke

#### Remove provisioning profiles

There are 2 provisioning profiles that we will need to remove and regenerate, the AppStore and the Development certificate.

##### Step 5: Remove AppStore provisioning profile

1. Go to <https://developer.apple.com/account/resources/profiles/list>
2. Find the `match AppStore nl.teqplay.[APPNAME]` profile
3. Click on the profile
4. Click remove

##### Step 6: Remove AppStore provisioning profile

1. Go to <https://developer.apple.com/account/resources/profiles/list>
2. Find the `match Development nl.teqplay.[APPNAME]` profile
3. Click on the profile
4. Click remove

#### Clear S3 bucket

All the certificates and profiles that we use with match are stored in a Amazon S3 bucket called `teqplay-app-certificates`. We will need to wipe all these certificates and provisioning profiles as we are going to regenerate them and re-upload them to S3.

##### Step 7: Delete all contents inside the S3 bucket

1. Login to Amazon AWS
2. Go to <https://s3.console.aws.amazon.com/s3/buckets>
3. Look for the `teqplay-app-certificates` bucket  
    Confirm that you are in fact inside the correct bucket before proceeding
4. Select all files inside the bucket and click delete
5. Click delete objects

#### Clear any saved certificates from your local device

This step is optional as you might not have any of these certificates on your local machine.

1. Search for the `Keychain access` app
2. Go to certificates
3. Delete any of the certificates that match steps 3, 4
4. Delete any of the provisioning profiles that match steps 5, 6

Okay now we really have wiped every single trace from the existing certificates and provisioning profiles. Up to regeneration!

#### Changing of MATCH\_PASSWORD

Match uses a variable called `MATCH_PASSWORD` to encrypt the certificates and provisioning profiles that are uploaded to the S3 bucket. This variable is then used during runtime to decrypt the certificates and profiles to apply them to the signing of the application.

As of , match does not support changing this password via its command line action `fastlane match change_password`, as it only supports git environments.

<https://github.com/fastlane/fastlane/discussions/20984>

So we will have to do this manually on the device and inside GitHub’s organisation Action secrets and variables, before we regenerate any certificates and profiles using the new password.

##### Step 8: Change MATCH\_PASSWORD on your local device

This step was written for a Mac OS device, it will be different for Linux or Windows

1. Search for the `Keychain access` application and open it
2. Go to your passwords
3. Find the `match_` internet password and open it
4. Click “Show password” at the bottom
5. Change this password to your newly desired password  
    Remember this password / write it down for the next step
6. Open the [Actions secrets and variables](https://github.com/organizations/teqplay/settings/secrets/actions) inside GitHub, change the value of `MATCH_PASSWORD` to the value of step 6.
7. (not required anymore post GitHub migration) Open the `ios-context` inside CircleCI and change the value of the `MATCH_PASSWORD` environment variable to the value of the previous step

### Regenerating certificates and profiles

The hardest part is done, we now just have to regenerate all the certificates and provisioning profiles. Luckily with match this is really easy.

This step cannot be performed on a CI machine

If the project you are working on has followed the fastlane template, it will have a lane called `ios retrieve_certificates`.

##### Step 9: Run the iOS retrieve\_certificates lane

1. Open the command line inside the repository folder
2. Run the command `fastlane ios retrieve_certificates`

This will regenerate all of the deleted certificates and provisioning profiles, as well as uploading/syncing these with the Amazon S3 bucket.

That is it!

Now all that is left to do is re-run the CI job and it should be all good to go!