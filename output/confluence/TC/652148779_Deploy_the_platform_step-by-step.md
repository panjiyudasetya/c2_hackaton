---
id: confluence:652148779
source: confluence
type: page
space: TC
title: Deploy the platform step-by-step
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148779
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148779
---
# Deploy the platform step-by-step

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148779  

## Content

Please note, if you want to run Mongo on the same machine, select a volume with XFS FileSystem.

# Create a new EC2 machine

* Setup new machine. Defaults:
* Ubuntu 18.04.3 LTS (Bionic)
* Availability zone: EU-WEST-1C (select via "Subnet")
* Set the right AWS permissions (IAM role "platform-instance" for example, but can depend on what you need)
* Check the option "Protect against accidental termination"
* When the disk needs to be able to scale beyond 2TB, make sure the disk has a GPT partition allowing for that. In case of running mongo on the same machine, set up a second disk and configure the server such that mongo writes it's data there `/var/lib/mongodb/`. The wiki page <https://bitbucket.org/teqplay/teqplay-wiki/wiki/Resizing%20Amazon%20EBS%20volumes> may be helpful.
* install ubuntu updates
* assign an elastic IP address to the server
* initially, use for example the `DEV_KEY` certificate to login the server for the first time (only if you do have this certificate!). Afterwards, we'll replace access with automatically synchronized ssh keys of all developers.

# Configure ubuntu server

* set timezone of the server to Amsterdam

  cmdsudo dpkg-reconfigure tzdata
* set the hostname for the server to something we can recognize:

  cmdsudo hostnamectl set-hostname backendsomething

  edit the file `/etc/hosts` else Java will complain about an unknown hostname

  cmdsudo nano /etc/hosts

  in there, change the following line:

  127.0.0.1 localhost

  to:

  127.0.0.1 localhost
  X.X.X.X mybackendhostname

  Where `X.X.X.X` should be replaced with the elastic IP address of the server. Note that `127.0.0.1 localhost mybackendhostname` works for ubuntu, but doesn't work with our notification service which reports the hostname in Slack notifications.
* add the credentials for the private S3 repository to `~/.m2/settings.xml` (see LastPass under "private repository")
* Configure a DNS entry for the new backend in <https://console.aws.amazon.com/route53,> so the server can be reached via "[mybackendhostname.teqplay.nl](http://mybackendhostname.teqplay.nl)" (and/or .com).

# Set up monitoring

* Install CloudWatch Agent as described in this wiki: <https://bitbucket.org/teqplay/teqplay-wiki/wiki/CloudWatch%20EC2> (this will report memory and disk usage).
* In AWS EC2 and CloudWatch, set up monitoring of the following metrics: CPU, memory usage, disk usage.

# Install required packages

cmd# Add OpenJDK repository
add-apt-repository ppa:openjdk-r/ppa
# Update and install packages
sudo apt-get install aptitude
sudo aptitude update
sudo aptitude dist-upgrade
sudo aptitude install openjdk-11-jdk-headless maven git mongodb apache2

# Checkout platform-scripts repository

* clone the repo into /home/ubuntu/

  cmdcd ~/
  git clone https://bitbucket.org/teqplay/platform-scripts.git
* Set up automated SSH key management, see wiki <https://bitbucket.org/teqplay/teqplay-wiki/wiki/Authomatic%20ssh%20keys%20management>
* Set up cron jobs for updating SSH keys and checking for system package updates. Run `crontab -l` on an existing server for inspiration. Cron jobs can look like:

  \*/5 \* \* \* \* /home/ubuntu/platform-scripts/manage-keys.py > /dev/null 2>&1
  30 8 \* \* mon-fri /home/ubuntu/platform-scripts/check-updates-and-notify.sh

# Configure mongo

* If a local database is not needed, do `sudo systemctl disable mongodb` and go to the next step 'Configure server stuff'.
* Edit/copy configuration as to be found in the `platform-scripts/conf/mongodb.conf` file to `/etc/mongodb.conf`. If using third-party mongo this file is called `mongod.conf`
* Make sure the memory usage of mongo is limited. Determine how much memory Mongo can use, and add a line in `/etc/mongodb.conf` with that:

  wiredTigerCacheSizeGB=2.5
* Start and enable mongodb (if a local database is needed):

  cmdsudo systemctl enable mongodb
  sudo systemctl start mongodb
* Make sure that the memory usage of ubuntu + platform + mongo combined is ok depending on the amount of memory the machine has. There must be some memory left (like `1GB`) to run processes like updates and deployments.

# Configure tomcat8

* install tomcat and python-pip

  sudo aptitude install tomcat8 python-pip
* create folders
* `/etc/teqplay` for configuration files
* `/var/lib/teqplay/log` for log files
* give right permissions to these folders as well. First add ubuntu user to the tomcat8 group.

  usermod -a -G tomcat8 ubuntu
* Now chown to transfer ownership

  chown tomcat8: /mnt/log
  chown tomcat8: /etc/teqplay
  chown tomcat8: /var/lib/teqplay/log
* And make a symbolic link for log directory for clarity

  ln -s /var/lib/teqplay/log /var/log/teqplay
* Edit the tomcat8 configuration with suitable options to `JAVA_OPTS`. Open up `/etc/defaults/tomcat8` and add `-Xms1g -Xmx3g -Duser.timezone='Europe/Amsterdam'` to `JAVA_OPTS`
* Edit the tomcat8 logging properties. Open up `/etc/tomcat8/logging.properties` and add `java.util.logging.SimpleFormatter.format=%1$tY-%1$tm-%1$td %1$tH:%1$tM:%1$tS [%4$s] %2$s %5$s%6$s%n` below the two lines starting with `java.util.logging`.
* Restart tomcat `sudo systemctl restart tomcat8`

# Configure Apache httpd modules:

cmda2enmod ssl proxy proxy\_http rewrite

* Install the \*.teqplay.nl certificate (public key) to `/etc/ssl/star_teqplay_nl.crt`
* Install the \*.teqplay.nl key (private key) to `/etc/ssl/private/star_teqplay_nl.key` (do a `chown root:ssl-cert star_teqplay_nl.key; chmod 640 star_teqplay_nl.key` as well!)
* Install the \*.teqplay.nl certificate bundle to `/etc/ssl/star_teqplay_nl.ca-bundle`
* Remove everything in `/etc/apache2/sites-enabled`, and add the following content to `000-backend.conf`:

  <VirtualHost \*:80>
  ServerAdmin developer@teqplay.nl
  RewriteEngine on
  RewriteCond %{HTTPS} !=on
  RewriteRule ^ https://%{SERVER\_NAME}%{REQUEST\_URI} [END,NE,R=permanent]
  </VirtualHost>
  <VirtualHost \*:443>
  ServerAdmin developer@teqplay.nl
  ProxyRequests Off
  ProxyPass / http://localhost:8080/
  ProxyPassReverse / http://localhost:8080/
  <Location "/">
  Order allow,deny
  Allow from all
  </Location>
  SSLCertificateFile /etc/ssl/star\_teqplay\_nl.crt
  SSLCertificateKeyFile /etc/ssl/private/star\_teqplay\_nl.key
  SSLCertificateChainFile /etc/ssl/star\_teqplay\_nl.ca-bundle
  SSLEngine on
  </VirtualHost>
* Restart apache: `sudo systemctl restart apache2`

# Setup authenticator

* Only do this when local authenticator is required!
* Checkout authenticator on your local system and do a `mvn clean install` on the master branch without any changes to the code. In the `target` folder there is a `Authenticator.war` file. Copy this to `/var/lib/tomcat8/webapps` and rename `Authenicator.war` to `authenicator.war` without the capital `A`.

# Setup platform deployment

* From the `platform-scripts/conf` copy the `default-system.conf` to `/etc/teqplay/system.conf` and alter the `system.conf` to the needs of the server. For example:
* Configure the area you want to monitor
* Configure either a HTTP connection to AISDATA/AISDATADEV polling once a minute, or configure streaming AIS via a rabbitmq queue.
* Enable the history sweeper to clean up AIS history older than x days
* configure areas if needed
* turn on certain monitors if needed
* Now we are ready for the actual work, running the platform! Install some python dependencies that we use for the deploy script, as ubuntu run

  pip install --user pytz pyparsing pyhocon s3fs
* Now from the `platform-scripts` folder run the deploy script `python deploy.py` and select a suitable version. This version will now run on the tomcat server.
* Now you should be able to access the platform by doing some call to it. You will be unauthorized of course. Therefor we need to create an admin account.
* Open up the `platform-scripts/mongo-scripts` folder. Give the right permissions to the script, `chmod 755 init_admin_account.sh`
* Create an initial admin account by executing the script, `sh init_admin_account.sh` (the password that it has can be found in LastPass, search for "Platform bootstrap account")
* Then, login via gatekeeper to change the admin password to something new and secure <https://gatekeeper.teqplay.nl/#/.>
* To automatically start the platform and authenticator on boot, enable it in `systemctl` by running `sudo systemctl enable tomcat8`.

# Setup backups if needed

When you're setting up a production server (not development), it is a good idea to set up creating backups of the disks: create snapshots of every volume. This can be configured in a Python script that is running as AWS Lambda:

<https://eu-west-1.console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/snapshotter?tab=configuration>

This script contains a list with the names of all backends that need snapshots. It will create daily snapshots and remove snapshots older than a week.

# Update the wiki

* If the wiki was outdated or unclear at some points, please up date it for the next time :)