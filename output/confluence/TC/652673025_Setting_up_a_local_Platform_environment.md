---
id: confluence:652673025
source: confluence
type: page
space: TC
title: Setting up a local Platform environment
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652673025
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652673025
---
# Setting up a local Platform environment

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652673025  

## Content

# Windows

### NOTE: If problems persist in any file, try changing the line endings to UNIX within IntelliJ. (probably communication.conf)

1. Download and install Java JDK 1.8 <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>
2. Download Maven 3 from <https://maven.apache.org/download.cgi>
3. Add `M2_HOME` and `MAVEN_HOME` to your system variables, pointing towards `C:\Program Files\Apache\Maven` or wherever you installed Maven.
4. Download Mongo Community Server from <https://www.mongodb.com/download-center#community>
5. Open the enivorment variables again and open Path variable. Add `C:\Program Fies\MongoDB\Server\4.0\bin\` as a new entry to the path. (Please make sure the version matches the path)
6. Create a keystore for the platform by running the command `keytool -genkey -alias tomcat -keyalg RSA` (if this doesn't work, add a new system variable JAVA\_HOME, pointing to your Java JDK and add to the system variable Path the following: `%JAVA_HOME%\bin`). Make sure the password is set to `playtech`.
7. Checkout the authenticator. <https://bitbucket.org/teqplay/authenticator>
8. Inside the authenticator folder, build the project with the command `mvn clean install`.
9. Checkout the platform. <https://bitbucket.org/teqplay/platform>
10. Inside the platform folder (not platform/platform), build the project with the command `mvn clean install`.
11. After this finished (it could take up to 15 minutes) create or open the file `C:\Users\<username>\.m2\settings.xml`. In this file add the code found in appendix #1 `settings.xml`. This should enable you to run the platform without getting the error tomcat7 plugin could not be found.
12. Open up a command prompt and go to the platform folder. Make sure the file is executable and do `init_admin_account.bat` to create the default admin account for the platform (username: admin, password: bootstrap).
13. Now open up IntelljIDEA. Do import project and select the platform folder. Select `import project from external model` and choose `Maven`. Click next. To the default settings on this screen add a check to `Search for projects recursively` and `Import Maven projects automatically`. Click next. Make sure all the projects are checked and click on next. Now you have to select the project SDK. Click on the + icon. A popup opens. It should automatically found the JDK to use, click on open. It has now added 1.8 as a folder, click next and Finish. Now wait for a few minutes as it is now resolving all the dependencies. After a few minutes the `api`, `communication` and `platform` project should appear.
14. Add configurations. To run the project you should have 3 configurations. One to only run what is already build, one to build and run without testing and one to build and run with all tests. In the top menu bar go to `Run -> Edit Configurations`. Click on the `+` icon and select Maven.

* Name the first `clean install`.
* Working directory -> click on the folder icon and select master.
* Command line -> `clean install tomcat7:run`
* Click apply
* Name the second `skip tests`.
* Working directory -> click on the folder icon and select master.
* Command line -> `clean install -Dmaven.test.skip=true tomcat7:run`
* Click apply
* Name the third `run`.
* Working directory -> click on the folder icon and select master.
* Command line -> `tomcat7:run`
* Click apply

You are now ready to develop the platform!

# Mac OSX

1. Download and install Java JDK 1.8 <http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html>
2. Set the $JAVA\_HOME environment variable. Open `~/.bash_profile` or create it when it does not exist yet. Add `export JAVA_HOME=$(/usr/libexec/java_home)` in this file and save it. Do the command `source ~/.bash_profile` to reinitialise.
3. Replace the policies with these two in the folder `/Library/Java/JavaVirtualMachines/jdk1.8.0_112.jdk/Contents/Home/jre/lib/security/`. <https://bitbucket.org/teqplay/teqplay-wiki/downloads/jce.zip>
4. Install maven. If you've not have installed homebrew yet, run the command `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`. Afterwards do `brew install maven` to install maven.
5. Install mongo. Run the command `brew install mongodb`
6. Create a keystore for the platform by running the command `$JAVA_HOME/bin/keytool -genkey -alias tomcat -keyalg RSA`
7. Checkout the authenticator. <https://bitbucket.org/teqplay/authenticator>
8. Inside the authenticator folder, build the project with the command `mvn clean install`.
9. Checkout the platform. <https://bitbucket.org/teqplay/platform>
10. Inside the platform folder (not platform/platform), build the project with the command `mvn clean install`.
11. After this finished (it could take up to 15 minutes) create or open the file `~/.m2/settings.xml`. In this file add the code found in appendix #1 `settings.xml`. This should enable you to run the platform without getting the error tomcat7 plugin could not be found.
12. Run the authenticator by doing `mvn tomcat7:run` inside the authenticator folder.
13. Run MongoDB by using the command `sudo mongod` inside a terminal screen.
14. Open up another terminal screen and go to the platform folder. First do the command `chmod 755 init_admin_account.sh` to make this file executable. Now execute the `init_admin_account.sh` script inside the platform folder to create the default admin account for the platform (username: admin, password: bootstrap).
15. Now open up IntelljIDEA. Do import project and select the platform folder. Select `import project from external model` and choose `Maven`. Click next. To the default settings on this screen add a check to `Search for projects recursively` and `Import Maven projects automatically`. Click next. Make sure all the projects are checked and click on next. Now you have to select the project SDK. Click on the + icon. A popup opens. It should automatically found the JDK to use, click on open. It has now added 1.8 as a folder, click next and Finish. Now wait for a few minutes as it is now resolving all the dependencies. After a few minutes the `api` and `platform` project should appear.
16. Add configurations. To run the project you should have 3 configurations. One to only run what is already build, one to build and run without testing and one to build and run with all tests. In the top menu bar go to `Run -> Edit Configurations`. Click on the `+` icon and select Maven.

* Name the first `clean install`.
* Working directory -> click on the folder icon and select master.
* Command line -> `clean install tomcat7:run`
* Click apply
* Name the second `skip tests`.
* Working directory -> click on the folder icon and select master.
* Command line -> `clean install -Dmaven.test.skip=true tomcat7:run`
* Click apply
* Name the third `run`.
* Working directory -> click on the folder icon and select master.
* Command line -> `tomcat7:run`
* Click apply

You are now ready to develop the platform!

# Linux (Ubuntu)

# Appendix

## 1. settings.xml

#!xml
<settings>
<pluginGroups>
<pluginGroup>org.apache.tomcat.maven</pluginGroup>
</pluginGroups>
</settings>