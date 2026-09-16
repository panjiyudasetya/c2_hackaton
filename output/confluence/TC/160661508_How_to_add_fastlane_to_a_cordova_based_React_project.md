---
id: confluence:160661508
source: confluence
type: page
space: TC
title: How to add fastlane to a cordova based React project
author: Damon Asberg
date: '2023-01-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160661508
explicit_links:
- github:CocoaPods/CocoaPods:issue:11402
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160661508
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160727044/Rotating+all+secrets+for+a+fastlane+project#Google-Play-Store-API-key
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160727044/Rotating+all+secrets+for+a+fastlane+project#App-Store-API-key
---
# How to add fastlane to a cordova based React project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160661508  

## Content

Woo you are allowed or want to add some automation to your app deployment! This should cover the basis of a cordova based application and get you automated in no-time.

As a basis, the <https://docs.fastlane.tools/> cover a lot of the bases and can provide a good resource in times of confusion.

A Mac OS device is required to setup or use iOS deployment scripts. Also in the CI.

## Getting started

What do you need on your machine before you get started?

* Ruby version 2.5 or newer  
  Mac OS already has this by default
* Bundler (`gem install bundler`)  
  Mac OS already has this by default

And of course fastlane!

### Mac OS

bashbrew install fastlane

That really is all that is needed!

### Windows

Not really sure, please refer to <https://docs.fastlane.tools/> and update this document!

## Setting up your repository

Your repository will require quite some settings and new files to be added. It is **highly** recommended to go to a separate branch for your project while you are tweaking settings.

### Fastlane files

#### Gemfile

If you have not already, inside the project root there should be a file indicating the dependency on fastlane.

Setting up a Gemfile

1. Inside the repository root, create a `Gemfile`
2. Add the following to its content:

   rubysource "https://rubygems.org"
   gem "fastlane"
3. Run the following command:

   bundle update

   This will generate a `Gemfile.lock`. Both Gemfiles should both be committed to the repository.

#### Appfile

While on your separate branch inside your project repo root, you can run:

bashfastlane init

This will ask you some questions and create an `./fastlane/Appfile`. It might actually be empty! This is good because you will have to replace it with some new information.

We will need the following:

* Android package name
* iOS App Bundle identifier

These are nearly **always** the same, so if you have one you have both. But it is worth it to double check anyway.

Android package name

##### Android

1. Go to the <https://play.google.com/console>
2. Navigate to `All apps`
3. Inside this list, find your app and note down the package id below the App name on the left  
   For example: `nl.teqplay.portreporter`
iOS app bundle identifier

##### iOS

1. Go to App Store Connect <https://appstoreconnect.apple.com/apps>
2. Click on the app of your choice
3. Click on the left side on the `App information` tab
4. Find the `Bundle ID` and note this down  
   For example: `nl.teqplay.portreporter`

Now that we have the information, we will need to replace the items in `{}`

rubyapp\_identifier "{APPLE\_BUNDLE\_ID}"
apple\_id "info@teqplay.nl"
team\_id "77UMYV878T"
json\_key\_file "./fastlane/android-api.json"
package\_name "{GOOGLE\_PACKAGE\_ID}"

And replace the `./fastlane/Appfile` contents with it.

## Code signing and setting up Fastfile

Our applications will require to be signed using the correct certificates and keystores. Setting up this process is a bit different for each platform, so we have separate guides for both Android and iOS.high

### Android

For Android we only need a couple of things, but these are key.

* Keystore file
* Google Cloud / Google Play API key JSON file

#### Keystore

Do not commit the `.keystore` file to Git, it will be inside the CI as an environment variable. For setup and local usage only, it should be placed inside the local directory.

All Android apps are signed using a keystore file. This file should be accessible inside the project directory. This keystore file should be quite familiar to you, it is the same as it is being done the manual way.

Add the following to your `.gitignore`:

/fastlane/\*.keystore
/fastlane/android-api.json

This ensures we don’t commit secrets to Git by accident.

Adding the keystore for local use

1. For your local environment only, copy the `.keystore` file to the `fastlane` folder in the project repository.
2. Rename the file to `prod.keystore`
3. Add the following line to your `.gitignore`

   /fastlane/\*.keystore

We used to use this keystore for multiple projects. Therefore we do not have to do anything as it is supplied by `android-context` inside the CI.

#### Google Cloud / Google Play API key

This key can only be generated by the Account holder of the Teqplay company in Google Play. This is Richard. Let him follow: <https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160727044/Rotating+all+secrets+for+a+fastlane+project#Google-Play-Store-API-key> in case a new key is required.

In order to communicate with Google Play, we need to get an API key which needs to be in the project directory.

1. Go to Google Drive: <https://drive.google.com/drive/u/1/folders/16tO0HrWtyIgRqQv31gys1IpKF5OhRj2n>
2. Grab the latest edited key (as of writing: `fastlane-rotate1`
3. Download the `.json` file
4. Rename the file to `android-api.json`
5. Move the file so it is located at `/fastlane/android-api.json`

That is literally all there is to it… compared to iOS this is peanuts. The Android guide continues after the long iOS segment.

### iOS

As pretty much always, Apple likes to make things complex and App code signing is no different. We will be making sure the project has access to the following:

* An Apple App Store API key
* Production / App Store certificate
* Development certificate
* Provisioning profile

#### Apple App Store API key

We will need an API key in order to communicate with the App Store to create new certificates automatically using fastlane. These keys are company bound, so they can already be found inside Google Drive. But if you want to create a new one, that is also possible.

Retrieving existing API key from Google Drive

1. Go to Google Drive: <https://drive.google.com/drive/folders/1BB6btKK5HqXWAzZRzfNBRQDYRNzKgPUw?usp=share_link>
2. Download the `iOS-API-key.p8` file
3. Put the file inside the `fastlane` folder inside your project
4. Add the following line to your `.gitignore` file:  
   We will generate the first items later, but the last line is important

   \*\*/fastlane/report.xml
   \*\*/fastlane/Preview.html
   \*\*/fastlane/screenshots
   \*\*/fastlane/test\_output
   fastlane/metadata/\*
   /fastlane/iOS-API-key.p8
Generating a new API key

I have described this process inside a separate article, since if you are generating a new API key - we probably lost the last one.

<https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/160727044/Rotating+all+secrets+for+a+fastlane+project#App-Store-API-key>

#### Matchfile

<https://docs.fastlane.tools/actions/match/> is the fastlane action we use to code sign our apps for iOS. It ensures proper storage and handles everything, from creating, applying, saving the relevant certificates and provisioning profiles required for the app.

##### Creating Matchfile

In order to create a Matchfile, we can let ourselves be guided by the command line by running the following in the repository root:

bashfastlane match init

This will give use the option to choose between several storage modes. At Teqplay we use AWS S3 for storing loads of data, so this is the best option for us right now. Select the `s3` option.

The Matchfile is created! But we actually need to replace its contents with something else:

rubys3\_bucket("teqplay-app-certificates")
s3\_region("eu-west-1")
storage\_mode("s3")

This will guide Match to the proper [S3 bucket](https://s3.console.aws.amazon.com/s3/buckets/teqplay-app-certificates), and the right region. We also remove the default type, as we will run it for both the `development` and `appstore` types later.

## Fastfile

This Fastfile will contain the actual scripts (fastlane calls them lanes) which will be executed in order to actually sign, build and deploy our app.

### Android

##### Preparation

To sign the app, we use the `/fastlane/prod.keystore` file. This file has 2 secrets:

* `FASTLANE_ANDROID_KEYSTORE_ALIAS`
* `FASTLANE_ANDROID_KEYSTORE_PASSWORD`

This might change from project to project, but as of today  it is the same for all projects. Both of these can be found in LastPass as “alias” and “password”.

##### Version sync step

As a first step, create the `/fastlane/Fastfile` if you have not already.

As a first lane, we are going to add a script / lane which will synchronise and set the proper version for us.

This will use a temporary file, which we need to add to `.gitignore`:

/scripts/.ANDROID\_VERSIONCODE

In this file we will set the version code of our application, which we can later use throughout the build process.

We will need several Fastlane plugins during the Android build. Add them one by one with the following commands:

bashfastlane add\_plugin load\_json

Next we are going to add to the actual Fastfile:

Sync version code Androidyamlplatform :android do
# Run before cordova build
desc "Sync the Android versionCode with the proper value from package.json"
lane :bump do
package = load\_json(json\_path: "./package.json")
# RiverGuide on Android has an odd versioning system
# The versionName stays intact, however the versionCode is multiplied by the underlying values
versions = package['version'].split(".")
major = Integer(versions[0]) \* 10000
minor = Integer(versions[1]) \* 100
bugfix = Integer(versions[2]) \* 1
newVersionCode = major + minor + bugfix
# Retrieve the current versionCodes in use on production
codesInUse = google\_play\_track\_version\_codes(
track: 'production'
)
# Get the code with the greatest value
highestVersionCode = codesInUse.max()
# In case the code is already in use, or if the highestVersionCode is greater than the current versionCode
if codesInUse.include?(newVersionCode) or highestVersionCode>=newVersionCode
# Bump the version code to the highest + 1
newVersionCode = highestVersionCode + 1
end
# Version code is unique and can be used
sh('echo "\n\next.cdvVersionCode = ' + newVersionCode.to\_s + '" >> ../res/android/build-extras.gradle')
# Export for use in other places
sh('touch ../scripts/.ANDROID\_VERSIONCODE')
sh('echo "' + newVersionCode.to\_s + '" > ../scripts/.ANDROID\_VERSIONCODE')
end
end

This script does the following:

* Retrieve the current package.json version
* Split the version into several parts, multiplying the major by 10000, minor by 100 and bugfix by 1.
* Concatenate these numbers into a single versionCode string
* Retrieve existing versions already in use from Google Play (uses API key)
* Check if the current versionCode that would be uploaded is higher than the one currently in place

  + If this is not the case, make sure the new versionCode is 1 higher than the existing highest versionCode
* Append this versionCode to the `./res/android/build-extras.gradle` file, to force its usage
* Export the versionCode to the `./scripts/.ANDROID_VERSIONCODE` file to be used elsewhere

The piece of code ensures we are always uploading and automatically incrementing versions, even if the settings might be off by a bit.

Make sure that inside the `./res/android/build-extras.gradle` the following exists, replacing `{I FORGOT TO REPLACE THIS}` with your project name:

/res/android/build-extras.gradlegroovydependencies {
implementation 'com.android.support:multidex:1.0.3'
}
android {
defaultConfig {
multiDexEnabled true
versionName privateHelpers.extractStringFromManifest("versionName")
applicationId "{I FORGOT TO REPLACE THIS}"
setProperty("archivesBaseName", applicationId + " v" + versionName)
}
}

##### Building the application

This guide assumes you already have the Android SDK installed

We use the cordova fastlane plugin to build our project. To add it run the following command inside the project directory:

bashfastlane add\_plugin cordova

We will need the `FASTLANE_ANDROID_KEYSTORE_ALIAS`, `FASTLANE_ANDROID_KEYSTORE_PASSWORD` environment variables in the next step.

Lets add the build step to Fastfile:

Fastlane Android build stepdesc "Build Android app using cordova"
lane :build do
cordova(
platform: 'android',
# The keystore and environment variables are injected via the CI
# via the "android-context".
keystore\_path: './fastlane/prod.keystore',
keystore\_alias: ENV['FASTLANE\_ANDROID\_KEYSTORE\_ALIAS'],
keystore\_password: ENV['FASTLANE\_ANDROID\_KEYSTORE\_PASSWORD'],
package\_type: 'bundle',
)
end

This will call the cordova plugin and build our app for us using the Android SDK.

###### FAQ - Frequent build errors

* Have you tried turning on Android Studio and see if it builds in there?  
  If it does not build in there, it is probably unrelated to whatever you just added through Fastlane.
* Wrong JDK / Gradle version  
  I used OpenJDK version `17.0.5`.
* Cordova plugin update required  
  Some plugins required updating because the `cordova-android` version required is now `11.0.0`.  
  As an example commit to see everything that had to be changed: <https://bitbucket.org/teqplay/portreporter-frontend/commits/fc383cdce71d1572895f74e289f603e4bf094dd6>   
  Some of these plugins might need an update:

  + `cordova-plugin-firebasex`  
     This might also require a config.xml change, icon changes
  + `cordova-plugin-local-notification-12`
  + `cordova-plugin-splashscreen`
* Outdated icons / splash screens  
  Android’s new API level target deprecated support for some icon types / splash screens. Therefore you have to add these new icon types.  
  <https://icon.kitchen/> is a good website to use for the icons. Background images have to be very large now so previously used small images might not be usable anymore or they will be ugly and cropped.

  + Notification icons also changed

##### Deploy time

Alright so assuming your build succeeds, we can start uploading and deploying it to the Google Play Store! You should have everything setup already considering we needed the API JSON key before.

Lets add the deploy and post\_slack lanes to the Fastfile:  
Don’t forget to replace `{PROJECT_NAME}` and `{I FORGOT TO REPLACE THIS}` in the snippet.

Fastlane Android deploy and post\_slack stepsdesc "Upload Android app to Google Play to a new draft production release"
lane :deploy do
package = load\_json(json\_path: "./package.json")
supply(
aab: './platforms/android/app/build/outputs/bundle/release/{PROJECT\_NAME} v' + package['version'] + '-release.aab',
track: 'production',
release\_status: 'draft', # !!! IMPORTANT, when release\_status is set to "completed" it will directly send it for review !!!
changes\_not\_sent\_for\_review: true,
skip\_upload\_metadata: true,
skip\_upload\_images: true,
skip\_upload\_screenshots: true,
skip\_upload\_apk: true,
skip\_upload\_changelogs: true
)
# Only post a Slack message if the SLACK\_URL variable is defined
if !ENV['SLACK\_URL'].nil? || is\_ci
post\_slack
end
end
lane :post\_slack do
package = load\_json(json\_path: "./package.json")
versionCode = File.read('../scripts/.ANDROID\_VERSIONCODE')
slack(
success: true,
payload: {
"App upload successful": '{I FORGOT TO REPLACE THIS} has been uploaded to Google Play',
"Platform": "Android",
"Version number": package['version'],
"Version code": versionCode
},
default\_payloads: ["git\_branch", "git\_author", "last\_git\_commit"]
)
end

In this snippet the following happens:

* Prepare your app `.aab` file for uploading
* Upload the file as a new draft release to Google Play, skipping any metadata changes (you can change this if you want to supply screenshots and other stuff from here)
* If you are inside a CI environment, post a slack message saying upload has succeeded.

##### Wrapping up the Fastfile

We have now gone through all the steps so lets make sure the Fastfile has some shortcuts added to automate the full process.

Fastlane Android complete Fastfile platform :android do
lane :deploy\_build do
build
deploy
end
lane :deploy\_nobuild do
deploy
end
# Run before cordova build
desc "Sync the Android versionCode with the proper value from package.json"
lane :bump do
package = load\_json(json\_path: "./package.json")
# RiverGuide on Android has an odd versioning system
# The versionName stays intact, however the versionCode is multiplied by the underlying values
versions = package['version'].split(".")
major = Integer(versions[0]) \* 10000
minor = Integer(versions[1]) \* 100
bugfix = Integer(versions[2]) \* 1
newVersionCode = major + minor + bugfix
# Retrieve the current versionCodes in use on production
codesInUse = google\_play\_track\_version\_codes(
track: 'production'
)
# Get the code with the greatest value
highestVersionCode = codesInUse.max()
# In case the code is already in use, or if the highestVersionCode is greater than the current versionCode
if codesInUse.include?(newVersionCode) or highestVersionCode>=newVersionCode
# Bump the version code to the highest + 1
newVersionCode = highestVersionCode + 1
end
# Version code is unique and can be used
sh('echo "\n\next.cdvVersionCode = ' + newVersionCode.to\_s + '" >> ../res/android/build-extras.gradle')
# Export for use in other places
sh('touch ../scripts/.ANDROID\_VERSIONCODE')
sh('echo "' + newVersionCode.to\_s + '" > ../scripts/.ANDROID\_VERSIONCODE')
end
desc "Build Android app using cordova"
lane :build do
cordova(
platform: 'android',
# The keystore and environment variables are injected via the CI
# via the "android-context".
keystore\_path: './fastlane/prod.keystore',
keystore\_alias: ENV['FASTLANE\_ANDROID\_KEYSTORE\_ALIAS'],
keystore\_password: ENV['FASTLANE\_ANDROID\_KEYSTORE\_PASSWORD'],
package\_type: 'bundle',
)
end
desc "Upload Android app to Google Play to a new draft production release"
lane :deploy do
package = load\_json(json\_path: "./package.json")
supply(
aab: './platforms/android/app/build/outputs/bundle/release/{PROJECT\_NAME} v' + package['version'] + '-release.aab',
track: 'production',
release\_status: 'draft', # !!! IMPORTANT, when release\_status is set to "completed" it will directly send it for review !!!
changes\_not\_sent\_for\_review: true,
skip\_upload\_metadata: true,
skip\_upload\_images: true,
skip\_upload\_screenshots: true,
skip\_upload\_apk: true,
skip\_upload\_changelogs: true
)
# Only post a Slack message if the SLACK\_URL variable is defined
if !ENV['SLACK\_URL'].nil? || is\_ci
post\_slack
end
end
lane :post\_slack do
package = load\_json(json\_path: "./package.json")
versionCode = File.read('../scripts/.ANDROID\_VERSIONCODE')
slack(
success: true,
payload: {
"App upload successful": '{PROJECT\_NAME} has been uploaded to Google Play',
"Platform": "Android",
"Version number": package['version'],
"Version code": versionCode
},
default\_payloads: ["git\_branch", "git\_author", "last\_git\_commit"]
)
end
end

### iOS

##### Adding API connection

In the previous step we made sure the `iOS-API-key.p8` file is present in our local directory. Now we can start adding a lane inside the Fastfile called `retrieve_certificates`.

For this step we need to have 2 environment variables set:

* `FASTLANE_IOS_CERT_KEY_ID`

  + This ID can be found here, corresponding to your API key which you downloaded before <https://appstoreconnect.apple.com/access/api>
* `FASTLANE_IOS_CERT_ISSUER_ID`

  + This ID can also be found here: <https://appstoreconnect.apple.com/access/api>

This key will not change until we rotate the key, so its a good practice to add these to your `~./bashrc` or `~./zshrc`

*Since this part is the main part of Fastlane, I covered this in a bit more detail.*

Fastlane iOS retrieve API key

This is not the final version of the iOS `retrieve_certificates` lane, it will be extended throughout the tutorial.

For the final iOS version, please skip to the end of the Fastfile (iOS) tutorial

rubyplatform :ios do
desc "Connect to App Store Connect and retrieve certificates from S3"
lane :retrieve\_certificates do
app\_store\_connect\_api\_key(
# The environment variables are injected via the CI via the "ios-context".
# The key\_id, issuer\_id and key\_content are all available through https://appstoreconnect.apple.com/access/api
key\_id: ENV['FASTLANE\_IOS\_CERT\_KEY\_ID'],
issuer\_id: ENV['FASTLANE\_IOS\_CERT\_ISSUER\_ID'],
# The API key content is encoded in Base 64 via the CI to fix any issues related to it being in multi-line.
# This is then decoded and saved unencoded to the fastlane directory.
key\_filepath: "./fastlane/iOS-API-key.p8",
duration: 1200,
in\_house: false
)
end
end

When running `fastlane ios retrieve_certificates` in your command line, it should return you with something like this:

+------+---------------------------+-------------+
| fastlane summary |
+------+---------------------------+-------------+
| Step | Action | Time (in s) |
+------+---------------------------+-------------+
| 1 | app\_store\_connect\_api\_key | 0 |
+------+---------------------------+-------------+
fastlane.tools finished successfully 🎉

This means it successfully connected to the App Store using the API key.

##### Generating certificates

You will need a Mac OS device for this step

Now that we have the API connection, we can extend the lane with several `match` commands. We will add the Developer and Distribution certificate steps now.

If you are logged into AWS via the command line aws tool, you will not need these environment variables. These will be added to the CI via the `common-build-context`, so you can generate one yourself on AWS through your work account. Otherwise, add these variables to either `~/.zshrc` or `~/.bashrc`:

* `AWS_ACCESS_KEY`
* `AWS_SECRET_KEY`

Extend the lane `retrieve_certificates` inside the `Fastfile` to make it become the following:

Fastfile with completed ios retrieve\_certificates lanerubyplatform :ios do
desc "Connect to App Store Connect and retrieve certificates from S3"
lane :retrieve\_certificates do
app\_store\_connect\_api\_key(
# The environment variables are injected via the CI via the "ios-context".
# The key\_id, issuer\_id and key\_content are all available through https://appstoreconnect.apple.com/access/api
key\_id: ENV['FASTLANE\_IOS\_CERT\_KEY\_ID'],
issuer\_id: ENV['FASTLANE\_IOS\_CERT\_ISSUER\_ID'],
# The API key content is encoded in Base 64 via the CI to fix any issues related to it being in multi-line.
# This is then decoded and saved unencoded to the fastlane directory.
key\_filepath: "./fastlane/iOS-API-key.p8",
duration: 1200,
in\_house: false
)
# All certificates are stored inside S3 using match
# First, retrieve the signing certificate for the App Store
match(
type: "appstore",
# The environment variables are injected via the CI via the "common-builds-context".
s3\_access\_key: ENV['AWS\_ACCESS\_KEY'],
s3\_secret\_access\_key: ENV['AWS\_SECRET\_KEY'],
readonly: is\_ci
)
# Because some libraries are not signed (CocoaPods & XCode 14 error),
# https://github.com/CocoaPods/CocoaPods/issues/11402
# We need our own development certificate to sign these as well.
# This will retrieve the development certificate stored in S3
match(
type: "development",
# The environment variables are injected via the CI via the "common-builds-context".
s3\_access\_key: ENV['AWS\_ACCESS\_KEY'],
s3\_secret\_access\_key: ENV['AWS\_SECRET\_KEY'],
readonly: is\_ci
)
end
end

What this lane now does is:

* Connect to Apple App Store via the supplied API key
* Retrieve (or generate) the App Store signing certificate
* Retrieve (or generate) the Development signing certificate
* Install any relevant provisioning profiles
* Upload these to the S3 bucket

In order to generate new certificates and provisioning profiles, we can just run the lane using:

bashfastlane ios retrieve\_certificates

This will ask for a `MATCH_PASSWORD`. This password can be found in Lastpass underneath `Fastlane MATCH_PASSWORD`.

It will generate the certificates if they do not exist, and will install them on your device so next time they do not have to be retrieved again.

When you have ran the command it should end with something along these lines:

bashAll required keys, certificates and provisioning profiles are installed 🙌
Setting Provisioning Profile type to 'development'
+------+---------------------------+-------------+
| fastlane summary |
+------+---------------------------+-------------+
| Step | Action | Time (in s) |
+------+---------------------------+-------------+
| 1 | app\_store\_connect\_api\_key | 0 |
| 2 | is\_ci | 0 |
| 3 | match | 4 |
| 4 | is\_ci | 0 |
| 5 | match | 3 |
+------+---------------------------+-------------+
fastlane.tools finished successfully 🎉

This means we have the code signing step completed!

##### Aligning version numbers

We want to make sure the version number and build code used to upload the package to the App Store is correct. You will need to change some variables in this code snippet, but it can be inserted inside the `platform :ios do` code block.

The variables you will need:

* Name of the `.xcodeproj` file of your project
* Name of the target of your project, usually matches the project filename

Fastlane iOS version bump coderubydesc 'Bump build numbers, and set the version to match the package.json version.'
lane :bump do
# Load the correct version directly from the package.json
package = load\_json(json\_path: "./package.json")
increment\_version\_number\_in\_xcodeproj(
xcodeproj: './platforms/ios/{PROJECT\_NAME}.xcodeproj',
version\_number: package['version'],
target: 'Port Reporter'
)
increment\_build\_number(
build\_number: is\_ci ? ci\_build\_number : 1,
xcodeproj: './platforms/ios/{PROJECT\_NAME}.xcodeproj',
)
end

This does the following:

* Look up the version number inside the `package.json` file
* Apply this to the xcodeproj
* Check the `ci_build_number` (will fallback to 1 if not found)
* Apply this to the xcodeproj

We need several fastlane plugins for this step. Add them one by one by running:

bashfastlane add\_plugin load\_json
fastlane add\_plugin versioning

Should it ask for you to modify the Gemfile, say **y**es. This will have created a Pluginfile and appended the plugins inside of it.

This bump step should be run every time you build your code. Speaking of which…

##### Add building step

You need a Mac OS device for this step

**Prerequisites**

You will need the XCode command line tools for this. To install on your Mac OS device:

xcode-select --install

We are actually going to use the `fastlane-plugin-cordova` plugin for this build step. It simplifies the whole cordova build step to just a single command in Fastlane.

To add the plugin to the project, run the following command inside the project directory:

bashfastlane add\_plugin cordova

**The actual building step**

Next step is to add the actual building step inside the `platform :ios do` block.

Fastlane iOS building steprubydesc "Build the iOS app using cordova"
lane :build do
cordova(
platform: 'ios',
release: true,
cordova\_prepare: true,
build\_number: ci\_build\_number # defaults back to 1 if run outside the CI
)
end

While this is the only edit to the Fastfile, we need to add some other things since there can be quite some bugs in the building process.

###### FAQ - Frequent building errors

Sadly there are quite a few errors you can run into, some might be your fault and others are definitely not.

Have you tried re-adding the project?bashcordova platform rm ios
cordova platform add ios
npm run build && cordova prepareCouldn't find info plist file at path ./platforms/ios/Port Reporterbashfastlane finished with errors
[!] Couldn't find info plist file at path './platforms/ios/
Port Reporter
.xcodeproj/../
Port Reporter
/
Port Reporter
-Info.plist'

Inside the `config.xml` file of the root of the project, the `<name>Port Reporter</name>` all has to be on a single line:

WRONG:

xml<?xml version="1.0" encoding="utf-8"?>
<widget id="nl.teqplay.portreporter" ios-CFBundleVersion="1" version="3.10.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
<name>
Port Reporter
</name>
<description>
Port Reporter
</description>

CORRECT:

xml<?xml version="1.0" encoding="utf-8"?>
<widget id="nl.teqplay.portreporter" ios-CFBundleVersion="1" version="3.10.0" xmlns="http://www.w3.org/ns/widgets" xmlns:cdv="http://cordova.apache.org/ns/1.0">
<name>Port Reporter</name>
<description>
Port Reporter
</description>The version of the CoreSimulator framework installed on this Mac is out-of-date and not supported by this version of Xcode.bash2023-01-17 16:08:32.375 xcodebuild[68252:3225582] DVTErrorPresenter: Unable to load simulator devices.
Domain: DVTCoreSimulatorAdditionsErrorDomain
Code: 3
Failure Reason: The version of the CoreSimulator framework installed on this Mac is out-of-date and not supported by this version of Xcode.
Recovery Suggestion: Please ensure that you have installed all available updates to your Mac's software, and that you are running the most recent version of Xcode supported by macOS.
--
CoreSimulator is out of date. Current version (857.13.0) is older than build version (857.14.0).

This means that your simulator files are out of date. Solution is to open XCode on your machine and install the simulators from the prompt.

Doesn't include signing certificate Apple Development: Created via APIerror: Provisioning profile "match AppStore nl.teqplay.portreporter" doesn't include signing certificate "Apple Development: Created via API (XXXX)". (in target 'Port Reporter' from project 'Port Reporter')

This means the provisioning profile has been created using a certificate than is available.

* Go to the S3 bucket `teqplay-app-certificates`
* Remove the provisioning profiles in both the `profiles/appstore` and `profiles/development` folders
* Go to <https://developer.apple.com/account/resources/profiles/list> and remove the matching profiles:

  + `match Development nl.teqplay.xxx`
  + `match AppStore nl.teqplay.xxx`
* Rerun the `fastlane ios retrieve_certificates` lane to generate new provisioning profiles matching the certificate you have on your machine
Signing for "<POD NAME>" requires a development teamerror: Signing for "FirebaseInAppMessaging-InAppMessagingDisplayResources" requires a development team. Select a development team in the Signing & Capabilities editor. (in target 'FirebaseInAppMessaging-InAppMessagingDisplayResources' from project 'Pods')
error: Signing for "GoogleTagManager-TagManagerResources" requires a development team. Select a development team in the Signing & Capabilities editor. (in target 'GoogleTagManager-TagManagerResources' from project 'Pods')

This one is quite annoying and is not really your fault. The affected libraries actually need to have a development team set, but they don’t have one set. We are going to set it to ourselves using a Podfile extension script. This is available inside the `/res/ios/Podfile`.

Straight from the `config.yml` these are the steps that have to be taken:

bashcat ./res/ios/Podfile >> ./platforms/ios/Podfile
cd ./platforms/ios
pod install
cd ../../

##### Add the uploading step

Finally, we are going to upload the build!

This is a 2 lane process, one for the actual uploading and the other for posting a nice Slack message to the channel of your choice.

First we are going to add the uploading step to the Fastfile. As in a previous step, make sure the `{PROJECT_NAME}` is replaced properly.

Fastfile iOS uploading steprubydesc "Upload the app to the App Store"
lane :deploy do
# Load the correct version directly from the package.json
package = load\_json(json\_path: "./package.json")
appstore(
# Using a direct link to the file as this is the default path
ipa: './platforms/ios/build/device/{PROJECT\_NAME}.ipa',
app\_version: package['version'],
precheck\_include\_in\_app\_purchases: false,
skip\_screenshots: true,
force: true
)
# Only post a Slack message if the SLACK\_URL variable is defined
if !ENV['SLACK\_URL'].nil?
post\_slack
end
end

You can already see the `post_slack` action at the end, we are getting to it quickly!

Then we will add the Slack message step to the Fastfile. This will require a `SLACK_URL` environment variable, which you can either set locally inside your exports or not set at all. If it is not set it will not be called.

You will need to replace `YOU_FORGOT_TO_REPLACE_THIS` with your desired name of the project.

Fastlane post-upload Slack messagerubylane :post\_slack do
package = load\_json(json\_path: "./package.json")
# Uses the SLACK\_URL environment variable
# Set inside the CI repo specific environment variables
slack(
success: true,
payload: {
"App upload successful": '{YOU\_FORGOT\_TO\_REPLACE\_THIS} has been uploaded to Apple App Store',
"Platform": "iOS",
"Version number": package['version'],
"Build number": is\_ci ? ci\_build\_number : 1
},
default\_payloads: ["git\_branch", "git\_author", "last\_git\_commit"]
)
end

##### Complete Fastfile (click here to quickly copy-paste the full file)

You can call lanes from other lanes, which can be quite handy if you want to skip a certain step.

These are:

* `deploy_build`
* `deploy_no_build`

Your Fastfile should look a lot like this now:

Completed iOS Fastfilerubyplatform :ios do
desc "Build iOS application and upload to the App Store"
lane :deploy\_build do
retrieve\_certificates
build
bump
deploy
end
desc "Upload an already built app to the App Store"
lane :deploy\_no\_build do
retrieve\_certificates
bump
deploy
end
desc "Connect to App Store Connect and retrieve certificates from S3"
lane :retrieve\_certificates do
app\_store\_connect\_api\_key(
# The environment variables are injected via the CI via the "ios-context".
# The key\_id, issuer\_id and key\_content are all available through https://appstoreconnect.apple.com/access/api
key\_id: ENV['FASTLANE\_IOS\_CERT\_KEY\_ID'],
issuer\_id: ENV['FASTLANE\_IOS\_CERT\_ISSUER\_ID'],
# The API key content is encoded in Base 64 via the CI to fix any issues related to it being in multi-line.
# This is then decoded and saved unencoded to the fastlane directory.
key\_filepath: "./fastlane/iOS-API-key.p8",
duration: 1200,
in\_house: false
)
# All certificates are stored inside S3 using match
# First, retrieve the signing certificate for the App Store
match(
type: "appstore",
# The environment variables are injected via the CI via the "common-builds-context".
s3\_access\_key: ENV['AWS\_ACCESS\_KEY'],
s3\_secret\_access\_key: ENV['AWS\_SECRET\_KEY'],
readonly: is\_ci
)
# Because some libraries are not signed (CocoaPods & XCode 14 error),
# https://github.com/CocoaPods/CocoaPods/issues/11402
# We need our own development certificate to sign these as well.
# This will retrieve the development certificate stored in S3
match(
type: "development",
# The environment variables are injected via the CI via the "common-builds-context".
s3\_access\_key: ENV['AWS\_ACCESS\_KEY'],
s3\_secret\_access\_key: ENV['AWS\_SECRET\_KEY'],
readonly: is\_ci
)
end
desc 'Bump build numbers, and set the version to match the package.json version.'
lane :bump do
# Load the correct version directly from the package.json
package = load\_json(json\_path: "./package.json")
increment\_version\_number\_in\_xcodeproj(
xcodeproj: './platforms/ios/{REPLACE\_WITH\_PROJECT\_NAME}.xcodeproj',
version\_number: package['version'],
target: {REPLACE\_WITH\_PROJECT\_NAME}
)
increment\_build\_number(
build\_number: is\_ci ? ci\_build\_number : 1,
xcodeproj: './platforms/ios/{REPLACE\_WITH\_PROJECT\_NAME}.xcodeproj',
)
end
desc "Build the iOS app using cordova"
lane :build do
cordova(
platform: 'ios',
release: true,
cordova\_prepare: true,
build\_number: is\_ci ? ci\_build\_number : 1 # defaults back to 1 if run outside the CI
)
end
desc "Upload the app to the App Store"
lane :deploy do
# Load the correct version directly from the package.json
package = load\_json(json\_path: "./package.json")
appstore(
# Using a direct link to the file as this is the default path
ipa: './platforms/ios/build/device/{REPLACE\_WITH\_PROJECT\_NAME}.ipa',
app\_version: package['version'],
precheck\_include\_in\_app\_purchases: false,
skip\_screenshots: true,
force: true
)
# Only post a Slack message if the SLACK\_URL variable is defined
if !ENV['SLACK\_URL'].nil?
post\_slack
end
end
lane :post\_slack do
package = load\_json(json\_path: "./package.json")
# Uses the SLACK\_URL environment variable
# Set inside the CI repo specific environment variables
slack(
success: true,
payload: {
"App upload successful": '{REPLACE\_WITH\_PROJECT\_NAME} has been uploaded to Apple App Store',
"Platform": "iOS",
"Version number": package['version'],
"Build number": is\_ci ? ci\_build\_number : 1
},
default\_payloads: ["git\_branch", "git\_author", "last\_git\_commit"]
)
end
end

You can now run `fastlane ios deploy_build` and it should just workTM!

## Preparing CI automatisation

Now that we can run the script locally, we need to make sure we can be completely lazy and run it anywhere!

This guide assumes we are using CircleCI

### Android

#### config.yml

No additions needed anymore to the Fastfile, we are going straight into the `config.yml`.

We need to add a few orbs to the project (this is duplicated from the iOS guide):

yamlorbs:
ruby: circleci/ruby@2.0.0
macos: circleci/macos@2.3.4
android: circleci/android@2.1.2
node: circleci/node@5.0.3

Now for the build step. You can execute this build step on any platform (Windows, Linux, Mac OS), assuming you have a working Android SDK setup.

The raw steps for the config.yml are as follows:

1. `checkout`  
   Checkout the latest project code
2. `bundle install`  
   Installs Fastlane and other dependencies
3. `sdkmanager "build-tools;32.0.0"`  
   Installs the relevant SDK build tools, in this case version `32.0.0`
4. `node/install`  
   The Android docker image does not contain NodeJS, so we have to install it
5. `node --version`  
   Check if the node version command executes, and Node is successfully installed
6. Set the npm token for `npm install` later
7. Writing the `FASTLANE_ANDROID_KEYSTORE` environment variable to a `keystore.b64` file, which is then decrypted and written to `./fastlane/prod.keystore`  
   Then the `ANDROID_API_JSON` API key is written to `./fastlane/android-api.json`
8. `npm install --location=global cordova`  
   Cordova is not present on this image
9. `npm install`
10. `npm run predeploy`
11. `bundle exec fastlane android bump`  
    Make sure the version numbers inside the `package.json` are synced with the Android app
12. `npx cordova platform add android@11.0.0`  
    Installs `cordova-android` and specifically the `11.0.0` version as this or a higher version is required by Google Play
13. `bundle exec fastlane android deploy_build`  
    Executes the `deploy_build` lane in your Fastfile

Full Android addition to Fastfileyamlbuild-android:
docker:
# from https://circleci.com/developer/images/image/cimg/android
- image: cimg/android:2022.09.2
steps:
- checkout
- run:
name: "Install dependencies from Gemfile"
command: |
bundle install
- run :
name: "Install Android SDK Build tools"
command: |
sdkmanager "build-tools;32.0.0"
- node/install:
node-version: '16.16'
- run: node --version
- run:
name: "Setting NPM token"
command: |
echo "//registry.npmjs.org/:\_authToken=$NPM\_TOKEN" >> ~/.npmrc
- run:
name: "Write required signing files to file"
command: |
echo $FASTLANE\_ANDROID\_KEYSTORE > keystore.b64
base64 -d -i "./keystore.b64" > ./fastlane/prod.keystore
echo "$ANDROID\_API\_JSON" > ./fastlane/android-api.json
- run: npm install --location=global cordova
- run: npm install
- run: npm run predeploy
- run:
name: "Fastlane correct versionCode in build-extras.gradle"
command: |
bundle exec fastlane android bump
- run:
name: "Add cordova Android platform to project"
command: |
npx cordova platform add android@11.0.0
- run:
name: fastlane
command: bundle exec fastlane android deploy\_build
workflows:
build-approve-deploy:
jobs:
- Execute Android build and upload:
type: approval
- build-android:
requires:
- Execute Android build and upload
context:
- common-builds-context
- android-context

Before you commit the file, be sure to set `SLACK_URL` as an environment variable inside the project settings inside CircleCI.

### iOS

We just need to add one thing to the `Fastfile`! At the top of the file, add the following:

rubyplatform :ios do
before\_all do
setup\_circle\_ci
end

#### config.yml

Now comes the real work, setting up the `config.yml`.

We start by adding a few orbs at the top (this is duplicated from the Android guide):

orbs:
ruby: circleci/ruby@2.0.0
macos: circleci/macos@2.3.4
android: circleci/android@2.1.2
node: circleci/node@5.0.3

Now comes the actual build step. For iOS we have to use a Mac OS CI machine, with the latest XCode installed. If you ever have to update the XCode version this is where you do it.

The raw steps are as follows:

1. `checkout`  
   Checkout the latest project code
2. `macos/preboot-simulator`  
   XCode requires a simulator to be active as XCode will build the app against the simulator as a target. It is recommended practice to boot the simulator as early as possible.
3. Set the npm token for `npm install` later
4. Write the App Store API key to file  
   This key is Base64 encoded and saved inside the `ios-context`, saved locally, then decoded to a regular file and saved inside the fastlane directory.
5. `npm install`
6. `npm run predeploy` (regular Cordova app build step)
7. `ruby/install-deps`  
   Install some ruby related dependencies
8. `bundle install`  
   Installs fastlane and other dependencies
9. `npx cordova platform add ios`  
   Adds the iOS cordova platform to the project structure. Uses `npx` to not have to install cordova globally.
10. Add post\_install to Podfile and re-install Pods  
    Fixes the `Signing for "<POD NAME>" requires a development team` error which might pop up during the build
11. `bundle exec fastlane ios bump`  
    Bumps the version number inside XCode to the latest before it starts building
12. `bundle exec fastlane ios deploy_build`  
    Executes the `deploy_build` step from the Fastfile.

Full addition to config.yml (iOS)yamlbuild-ios:
macos:
xcode: 14.2.0
resource\_class: medium
environment:
FL\_OUTPUT\_DIR: output
shell: /bin/bash --login -o pipefail
steps:
- checkout
- macos/preboot-simulator:
version: "16.2"
platform: "iOS"
device: "iPhone 14 Pro Max"
- run:
name: "Setting NPM token"
command: |
echo "//registry.npmjs.org/:\_authToken=$NPM\_TOKEN" >> ~/.npmrc
- run:
name: "Write App Store API key to file"
command: |
echo $FASTLANE\_IOS\_CERT\_PKEY > iospkey.b64
base64 -d -i "./iospkey.b64" > ./fastlane/iOS-API-key.p8
- run: npm install
- run: npm run predeploy
- ruby/install-deps
- run:
name: "Install dependencies from Gemfile"
command: |
bundle install
- run:
name: "Add cordova iOS platform to project"
command: |
npx cordova platform add ios
- run:
name: "Add post\_install to Podfile and re-install Pods"
command: |
cat ./res/ios/Podfile >> ./platforms/ios/Podfile
cd ./platforms/ios
pod install
cd ../../
- run:
name: "Sync version of package.json with XCode project"
command: |
bundle exec fastlane ios bump
- run:
name: fastlane
command: bundle exec fastlane ios deploy\_build
workflows:
version: 2
build-approve-deploy:
jobs:
- Execute iOS build and upload:
type: approval
- build-ios:
requires:
- Execute iOS build and upload
context:
- common-builds-context
- ios-context

Before you commit the file, be sure to set `SLACK_URL` as an environment variable inside the project settings inside CircleCI.