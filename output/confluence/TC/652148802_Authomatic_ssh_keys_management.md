---
id: confluence:652148802
source: confluence
type: page
space: TC
title: Authomatic ssh keys management
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148802
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148802
---
# Authomatic ssh keys management

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652148802  

## Content

# Generic info

Users that belong to **developer** and **administrators** groups could upload their ssh keys and access the instances running in AWS. To do so

1. Go to [IAM / Users](https://console.aws.amazon.com/iam/home?region=eu-west-1#/users)
2. Locate your user
3. Switch to **Security credentials** tab
4. Scroll to **SSH keys for AWS CodeCommit** section
5. Press **Upload SSH public key**

# Beanstalk project setup

0. Beanstalk environment should use **aws-elasticbeanstalk-ec2-role** role or a role that is specified in the s3 bucket **teqplay-scripts** to have access to the authorized\_keys file, if it does not - update the **teqplay-scripts** bucket permission statement **GetAuthorizedKeysStatement** to also contain the role arn which is specified on the instance.
1. Copy [04-users-ssh-keys.config](https://bitbucket.org/teqplay/shipsparelogistics-backend/src/develop/.ebextensions/04-users-ssh-keys.config) to your project .ebextensions folder
2. Deploy as usual

# EC2 instance setup

0. EC2 instance should use **platform-instance** role or a role that is specified in the s3 bucket **teqplay-scripts** to have access to the authorized\_keys file, if it does not - update the **teqplay-scripts** bucket permission statement **GetAuthorizedKeysStatement** to also contain the role arn which is specified on the instance.
1. Install `boto3` python library using `apt-get` or `pip` or `easy_install`: eg `sudo apt-get install python-boto3`

   note the script uses python3, you need to install boto3 for python3: `sudo apt install python3-pip && pip3 install boto3`
2. Checkout the `platform-scripts` repository

   #!cmd
   cd ~/
   git clone https://bitbucket.org/teqplay/aws-scripts.git
3. In the config file `/etc/ssh/sshd_config`, change the following line:

   #PermitUserEnvironment no

   Into:

   PermitUserEnvironment yes

   Then run the following to apply the config change:

   sudo systemctl restart sshd

   After logging in again, running `echo $TEQPLAY_AWS_USERNAME` should print your username.

   (if this is not changed, the scripts will not be able to set the username of the currently logged in user in the environment variable `TEQPLAY_AWS_USERNAME`, which is used when sending notifications about restarting the platform).
4. Run `manage-keys.sh` located in `platform-scripts`.
5. Set up a cron job to regularly refresh the SSH keys. Run `crontab -l` on an existing server for inspiration. Example of cron job:

   \*/5 \* \* \* \* /home/ubuntu/aws-scripts/get-authorized-keys.py > /dev/null 2>&1

   Editing the cron jobs of the machine by writing

   crontab -e

# The generic idea of automatic ssh keys management

AWS allows storing public ssh keys for AWS CodeCommit service. The script uses those keys to generate **~/.ssh/authorized\_keys** file. Script uses **boto3** python library and requires permission to read public keys defined in [get-user-public-ssh-keys](https://console.aws.amazon.com/iam/home?region=eu-west-1#/policies/arn:aws:iam::050356841556:policy/get-user-public-ssh-keys$jsonEditor) policy Another script sets up a cron job to periodically run the keys update script. All files could be found at [s3 repo.teqplay.nl/scripts/user-ssh](https://s3.console.aws.amazon.com/s3/buckets/repo.teqplay.nl/scripts/user-ssh/?region=eu-west-1&tab=overview)

# Emergency SSH Key Recovery

If, for some reason, a Linux machine is no longer accessible using your SSH keypair and no-one else has a working keypair, Léon and Richard have the secret key of the emergency SSH keypair in their possession, as a printed QR code. To be able to use this key, it needs to be scanned, preferably using the camera of the device on which you're going to use it, to minimize the number of machines that "know" about this key.

Suitable tools for Linux machines:

* `zbarcam`, a very basic tool. Run it from the CLI, it pops up a window to scan the code, and any codes that are recognized are printed to the console
* `QtQR`. Did not work so well for me, ymmv. You need to click to activate recognition.

Suitable tools for Windows machines (I haven't tried any of these):

* <https://www.codetwo.com/freeware/qr-code-desktop-reader/>

Online:

* <https://webqr.com/>

When you've recovered the key text, store it in a file, and use it with `ssh -i keyfile <user@host>`.