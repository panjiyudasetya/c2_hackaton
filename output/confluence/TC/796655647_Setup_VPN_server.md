---
id: confluence:796655647
source: confluence
type: page
space: TC
title: Setup VPN server
author: Joost Laurman
date: '2026-02-12'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796655647
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796655647
---
# Setup VPN server

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/796655647  

## Content

# Setup EC2 machine

* Create `t2.nano` instance with Ubuntu Server 24.04
* Select right VPC
* Select a PUBLIC subnet, private will close it down
* Create security group:  
  **Inbound**  
  *Custom UDP:* 1194 to All IPv4  
  **Outbound**  
  All traffic
* Select the `basic-instance` IAM role
* Add this as user data; this will install the SSM agent on the machine and you will be able to access the server without using SSH.

  Content-Type: multipart/mixed; boundary="//"
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

Now you are in the machine. Let’s setup the VPN!

# Setup OpenVPN and EasyRSA

Firstly, download EasyRSA-2.2.2 onto the machine (<https://github.com/OpenVPN/easy-rsa/releases/download/2.2.2/EasyRSA-2.2.2.tgz> ), and unpack.

Change to this newly created directory and edit the `vars` file.

Edit the `vars` file and change these values:

wide760export KEY\_SIZE=4096
export KEY\_COUNTRY="NL"
export KEY\_PROVINCE="RTM"
export KEY\_CITY="Rotterdam"
export KEY\_ORG="Teqplay"
export KEY\_EMAIL="developer@teqplay.nl"
export KEY\_OU="vpn"

Now do the following commands:

wide760sudo apt install openvpn -y
export KEY\_ALTNAMES="DNS:localhost"
source vars
cp openssl-1.0.0.cnf openssl.cnf
./build-ca
./build-key-server server
./build-dh
cd /etc/openvpn/
sudo cp ~/EasyRSA-2.2.2/keys/dh2048.pem dh2048.pem
sudo cp ~/EasyRSA-2.2.2/keys/ca.crt ca.crt
sudo cp ~/EasyRSA-2.2.2/keys/server.crt vpn.teqplay.nl.crt
sudo cp ~/EasyRSA-2.2.2/keys/server.key vpn.teqplay.nl.key

Now go to `/etc/openvpn/server`.

Create a new file, `teqplay.conf` and add the following contents:

wide760proto udp
dev tun
ca /etc/openvpn/ca.crt
cert /etc/openvpn/vpn.teqplay.nl.crt
key /etc/openvpn/vpn.teqplay.nl.key
dh /etc/openvpn/dh4096.pem
crl-verify /etc/openvpn/crl.pem
server 192.168.200.0 255.255.255.0
ifconfig-pool-persist ipp.txt 10
push "route 172.31.0.0 255.255.0.0"
push "route 172.30.0.0 255.255.0.0"
push "dhcp-option DNS 192.168.200.1"
client-to-client
keepalive 10 120
comp-lzo
user nobody
group nogroup
persist-key
persist-tun
verb 3

Copy [this file](https://github.com/OneSignal/openssl/blob/main/apps/dh4096.pem) to `/etc/openvpn` and copy this file to `/etc/openvpn` as well.

Now run the `openvpn-server` with the following command:

`sudo systemctl start openvpn-server@teqplay.service`

and enable it

`sudo systemctl enable openvpn-server@teqplay.service`

# Installation and configuration of DNSMasq

Now we are going to setup DNSMasq to pass all DNS queries through the EC2 machine to the VPC.

First install DNSMasq `sudo apt install dnsmasq -y`

After this, open up the `/etc/dnsmasq.conf`.

Uncomment the next lines:

wide760interface=tun0
bind-interfaces
except-interface=lo
no-hosts

Under the no-hosts, add these lines:

wide760listen-address=127.0.0.1,192.168.200.1
server=172.30.0.2

The server `172.30.0.2` could be different. This should be changed to match the VPC.

And now restart dnsmasq

`sudo systemctl restart dnsmasq.service`

Some additional settings

Some things still need some caretaking. For example, setting the ipv4 forward.

Check first which network interface the server is using

wide760ubuntu@openvpn:~$ ip route | grep default
default via 172.31.32.1 dev eth0 proto dhcp src 172.31.45.120 metric 100

This server is using `eth0` as network interface, so let’s use that in the iptables.

wide760# first set IPv4 forwarding
sudo sysctl -w net.ipv4.ip\_forward=1
# apply settings
sudo sysctl -p
# Correcting iptables
sudo iptables -t nat -D POSTROUTING 1
sudo iptables -t nat -A POSTROUTING -s 192.168.200.0/24 -o eth0 -j MASQUERADE
# and apply the settings into iptables
sudo iptables-save > /etc/iptables/rules.v4 

Now generate certificates and go go go!