---
id: confluence:652640275
source: confluence
type: page
space: TC
title: Cordova setup new project
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652640275
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652640275
---
# Cordova setup new project

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652640275  

## Content

1. Create cordova app besides original folder `$ cordova create <projectFolder> nl.teqplay.<project> <ProjectName>`
2. Copy the folders/files to your own project (platforms, plugins, res, config)
3. Copy the relevant parts of the .npmignore file into the original files from the project.
4. Make sure that the homepage is set correctly: `homepage: ‘./‘`
5. Update the relevant fields in the config.xml
6. Add to the index file the deviceready function. See riverguide-recreant project (src/index.js)
7. Add cordova import script to the `public/index.html`. See also riverguide-recreant.
8. Change in package.json file the build script to make sure the build is made in `/www`: `npm run build-css && react-scripts build && rm -rf www && mkdir www && mv -v build/* www/ && rm -rf build/`
9. Build the app `npm run build`
10. Add Android to platform `cordova platform add android@6.4.0`. Maybe remove the version, but had issues with the firebase with newer versions.
11. Add iOS to platform `cordova platform add ios`
12. Generate an icon.png (1000×1000) and splash.png (2208×2208) in the root folder off the project
13. Use [Abiro PhoneGap Image Generator](https://pgicons.abiro.com/) to generate all icons and splash screens. Add the /icon and /screen folders to the /res folder in the project.
14. Update the config.xml with the icon and splash sources for both iOS and Android: <https://pgicons.abiro.com/config.xml>
15. Make sure Android Studio and/or Xcode is installed
16. Set ANDROID\_HOME parameter
17. Build the project for one off the platforms: `cordova build android`
18. Install default plugins suggested: cordova-plugin-whitelist, cordova-plugin-splashscreen, cordova-plugin-inappbrowser