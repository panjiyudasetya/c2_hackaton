---
id: confluence:984776705
source: confluence
type: page
space: TC
title: Creating new EC2 instance and login with AWS SSM
author: Joost Laurman
date: '2025-11-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/984776705
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/984776705
---
# Creating new EC2 instance and login with AWS SSM

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/984776705  

## Content

Written for the DEVELOP AWS account

Create a new EC2 instance.

Let the instance use the `basic-instance` IAM role

Set this as user data. This will make sure the SSM-agent is installed on the machine and the machine is accessible.

wide760Content-Type: multipart/mixed; boundary="//"
MIME-Version: 1.0
--//
Content-Type: text/cloud-config; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="cloud-config.txt"
#cloud-config
cloud\_final\_modules:
[scripts-user, always]
--//
Content-Type: text/x-shellscript; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="userdata.txt"
#!/bin/bash
sudo yum install -y python3
sudo dnf install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux\_amd64/amazon-ssm-agent.rpm
sudo systemctl status amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent
-//-

* Use AWS SSM to login into the machine:  
  `aws ssm start-session --target <<instance_id>> --profile <<amazon_profile_id>> --region eu-west-1`
* Enter the ubuntu user by doing `sudo -i -u ubuntu`