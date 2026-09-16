---
id: confluence:652115990
source: confluence
type: page
space: TC
title: CloudWatch EC2
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652115990
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652115990
---
# CloudWatch EC2

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652115990  

## Content

1. Ensure your instance has a role with the `CloudWatchAgentServerPolicy` policy
2. Download the package

   wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
3. Install it

   sudo dpkg -i amazon-cloudwatch-agent.deb
4. Configure the metrics that should be collected

   sudo bash -c 'cat > /opt/aws/amazon-cloudwatch-agent/bin/config.json' <<EOT
   {
   "agent": {
   "metrics\_collection\_interval": 60,
   "run\_as\_user": "root"
   },
   "metrics": {
   "append\_dimensions": {
   "AutoScalingGroupName": "\${aws:AutoScalingGroupName}",
   "ImageId": "\${aws:ImageId}",
   "InstanceId": "\${aws:InstanceId}",
   "InstanceType": "\${aws:InstanceType}"
   },
   "metrics\_collected": {
   "disk": {
   "measurement": [
   "used\_percent"
   ],
   "metrics\_collection\_interval": 60,
   "ignore\_file\_system\_types":[
   "devtmpfs",
   "overlay",
   "squashfs",
   "tmpfs",
   "nfs4"
   ],
   "resources": [
   "\*"
   ]
   },
   "mem": {
   "measurement": [
   "mem\_used\_percent"
   ],
   "metrics\_collection\_interval": 60
   }
   }
   }
   }
   EOT
5. Load the new configuration file

   sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
6. Remove the package

   rm amazon-cloudwatch-agent.deb
7. Check that cloudwatch agent is running

   amazon-cloudwatch-agent-ctl -a status

   and start if it's not

   amazon-cloudwatch-agent-ctl -a start
8. Check in CloudWatch that metrics are indeed sent (this may take a few minutes)