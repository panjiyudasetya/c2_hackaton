---
id: confluence:807370765
source: confluence
type: page
space: TC
title: Tomcat10 migration (draft)
author: Pim van den Toorn (Unlicensed)
date: '2025-12-08'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/807370765
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/807370765
---
# Tomcat10 migration (draft)

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/807370765  

## Content

# Management

## Reverting

After all the migration is done, it can always be reverted simply by doing:

wide760sudo systemctl stop tomcat10wide760sudo systemctl start tomcat8

## Logs

Move to the log directories using:

wide760cd /var/log/tomcat8wide760cd /var/log/tomcat10 

In these, there is the **catalina.out**, which has the logs with the http request (it’s the main tomcat log file), and the **platform.log** without them.

To see the live logs, use:

wide760tail -n 100 -f /var/log/tomcat10/catalina.out

**tail** shows the end of the file  
**-n 100** shows the last 100 lines (default is 10)  
**-f** follows the file, so it keeps printing new lines that are added to it

## Deployment

Move to the directory with the deployment or restart scripts using:

wide760cd /home/ubuntu/platform-scripts

In here you have a deploy.py and a restart.py (and possibly already the tomcat10 versions)

You can run these by doing

wide760./deploy-tomcat10.py

## Managing the tomcat process

To start or stop the tomcat:

wide760sudo systemctl stop tomcat10

Replace **stop** with **start** or **restart**, this also works for tomcat 8

To check the status of tomcat:

wide760systemctl status tomcat10

To get more system logs for debugging:

wide760journalctl -xe

where **x** gives a more detailed output, and **e** puts you at the end of the file. Move up or down through the file using the arrow keys.

# Setting up Tomcat10

544
273fdbbb-abe5-4d67-809e-62efa41d62c9
incomplete
Download java 17

545
c46a90d4-635a-4c24-812c-846611451620
incomplete
Download Tomcat 10

546
5d7bba5a-08ff-4f85-a51d-ecc84dde0934
incomplete
Create the tomcat user

547
3a484327-3e2e-4d01-837e-1bc8c09db5c4
incomplete
Create the directories

548
b621d971-5fef-4dce-a203-c4a9d091610d
incomplete
Link the logs

549
f3800220-df13-4130-9819-34666558e692
incomplete
Create the settings

550
1435a62a-0466-4cd9-80a9-adbfa74e5137
incomplete
Update Tomcat Native

551
578749a0-3527-4673-bb60-ddc84bf9cde6
incomplete
Create Tomcat 10 versions of deploy.py and restart.py

552
313d0cc0-9da7-4ee9-a88f-969b6b0a984b
incomplete
Get the new authenticator

553
202eee0e-5943-49df-bc22-153a163259ba
incomplete
Stop Tomcat 8 and start Tomcat 10

### Download java 17:

wide760sudo apt update
sudo apt install openjdk-17-jdk

Should now be in /usr/lib/jvm/

### Download Tomcat 10:

Tomcat 10 is not available with the server’s Ubuntu version, so it must be installed manually. First download it from Apache:

wide1011cd /opt
sudo wget https://downloads.apache.org/tomcat/tomcat-10/v10.1.24/bin/apache-tomcat-10.1.24.tar.gz

Changed to 10.1.49 on live, as the .24 was not available anymore

Extract:

wide760sudo tar -xzf apache-tomcat-10.1.24.tar.gz

Rename:

wide760sudo mv apache-tomcat-10.1.24 tomcat10

Make the scripts executable:

wide760sudo chmod +x /opt/tomcat10/bin/\*.sh

**chmod** → Change mode: changes the file permissions

**+x** → makes files executable

**\*.sh** → all files ending with .sh

### Create the tomcat user:

wide760sudo useradd -r -m -U -d /opt/tomcat10 -s /bin/false tomcat

**-r** → create a system account

**-m** → create the home directory if it doesn’t exist

**-U** → create a group with the same name as the user

**-d /opt/tomcat10** → set the home directory

**-s /bin/false** → user can’t log in

Then set the ownership of that directory to tomcat:

wide760sudo chown -R tomcat:tomcat /opt/tomcat10

**-R** → recursively set it for all files and directories within the given directory

### Creating directories

Create the directories:

wide760mkdir /var/lib/tomcat10
mkdir /var/log/tomcat10

Set the ownership of these directories to tomcat:

wide760sudo chown -R tomcat:tomcat /var/lib/tomcat10
sudo chown -R tomcat:tomcat /var/log/tomcat10

Maybe necessary?:

wide760sudo cp -r /opt/tomcat10/{bin,conf,lib,temp,work} /var/lib/tomcat10/

### Linking the logs

Create a link:

wide760sudo ln -s /var/log/tomcat10 /var/lib/tomcat10/logs

Any interaction with /var/lib/tomcat10/logs will now be redirected.

### Tomcat settings

Create the /etc/systemd/system/tomcat10.service file:

wide760sudo nano /etc/systemd/system/tomcat10.service

Paste in it:

bashwide760[Unit]
Description=Apache Tomcat 10 Web Application Container
After=network.target
[Service]
Type=forking
User=tomcat
Group=tomcat
Environment="JAVA\_HOME=/usr/lib/jvm/java-17-openjdk-amd64"
Environment="CATALINA\_PID=/opt/tomcat10/temp/tomcat.pid"
Environment="CATALINA\_HOME=/opt/tomcat10"
Environment="CATALINA\_BASE=/var/lib/tomcat10"
Environment="CATALINA\_OUT=/var/log/tomcat10/catalina.out"
Environment="CATALINA\_OPTS=-server"
Environment="JAVA\_OPTS=--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED"
ExecStart=/opt/tomcat10/bin/catalina.sh start
ExecStop=/opt/tomcat10/bin/shutdown.sh
SuccessExitStatus=143
Restart=on-failure
[Install]
WantedBy=multi-user.target

Save with **Ctrl+o**  then  **Enter**

When changing settings, run:

nonewide760sudo systemctl daemon-reexec
sudo systemctl daemon-reload

And if tomcat10 was already running:

wide760sudo systemctl restart tomcat10

### Update the Tomcat Native library

The necessary version isn’t available with the Ubuntu version the server is running, so it has to be manually installed:

wide1011sudo apt install build-essential libssl-dev libapr1-dev libaprutil1-dev wget
cd ~
wget https://downloads.apache.org/tomcat/tomcat-connectors/native/1.3.1/source/tomcat-native-1.3.1-src.tar.gz
tar -xzf tomcat-native-1.3.1-src.tar.gz
cd tomcat-native-1.3.1-src/native
./configure --with-apr=/usr/bin/apr-1-config --with-java-home=/usr/lib/jvm/java-17-openjdk-amd64
make
sudo make install

### Creating tomcat10 versions of deploy.py and restart.py

Cd to the /home/ubuntu/platform-scripts folder and copy the files using:

wide760cp deploy.py deploy-tomcat10.py

Then edit the files using

wide760nano deploy-tomcat10.py

For the deploy.py, there are, at the end of the file in the def main() function, a few references to tomcat8, change those to tomcat10. Same for the restart.py.

### Get the new authenticator

Copy the updated Authentication.war to the new tomcat, possibly from your own computer using WinSCP or something similar.  
Change ownership to tomcat

### Stop Tomcat 8 and start Tomcat 10

To turn off the old platform version and start the new one:

`sudo systemctl stop tomcat8`  
`sudo systemctl start tomcat10`

### Add log rotation

in /etc/logrotate.d, add the catalina.out, platform.log and /var/log/teqplay/reportinglog.txt

### Have both tomcat8 and the new tomcat user get access to the /var/lib/teqplay directory

`sudo groupadd tomcat_shared`

`sudo usermod -aG tomcat_shared tomcat8`

`sudo usermod -aG tomcat_shared tomcat`

Add group to the directory:

`sudo chown -R :tomcat_shared /var/lib/teqplay`

Have any new files in the directory be group owned:

`sudo chmod g+s`

Give the group write access on all files in the directory:

`chmod -R g+w /var/lib/teqplay`

memory limits?/garbage collector?