---
id: confluence:984055809
source: confluence
type: page
space: TC
title: Setup simultaneous VPN connections
author: Joost Laurman
date: '2025-11-13'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/984055809
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/984055809
---
# Setup simultaneous VPN connections

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/984055809  

## Content

16falsedefaultlisttrue

# Windows setup

## Clients

The OpenVPN Connect client does not support simultaneous connections if you are using this client you will need switch OpenVPN GUI client  
  
**Resources:**   
<https://openvpn.net/community/>

<https://openvpn.net/as-docs/faq-simultaneous-openvpn-server-connections.html>

## Configuration

To be able to use two VPN simultaneously you will need to change your config files `.ovpn`

Your config files should look this but then with the added certificates

wide760proto udp
dev tun
client
remote vpn.teqplay.nl 1194
resolv-retry infinite
keepalive 10 120
comp-lzo
persist-key
persist-tun
verb 3

under the `dev tun` you need to add a new line to specify which TAP adapter this VPN is allowed to use.

for this example the TAP adapters are called `teqplay-prod` and `teqplay-dev`

**PROD:**

wide760dev-node "teqplay-prod"

**DEV:**

wide760dev-node "teqplay-dev"

## Creating TAP adapters

Now that we specified which TAP adapters the VPNs are allowed to use we need to create them for this you can use this `bat` script. it uses the `tapctl` included in OpenVPN GUI to create two TAP adapters `teqplay-prod` and `teqplay-dev`

powershellwide760@echo off
REM ============================================
REM Create and rename OpenVPN TAP adapters
REM Requires: OpenVPN installed (with tapctl.exe)
REM ============================================
echo.
echo Creating TAP adapters for teqplay-prod and teqplay-dev...
echo.
REM Locate OpenVPN installation directory
set "OPENVPN\_DIR=%ProgramFiles%\OpenVPN\bin"
if not exist "%OPENVPN\_DIR%\tapctl.exe" (
echo ERROR: tapctl.exe not found!
echo Please make sure OpenVPN GUI is installed.
pause
exit /b 1
)
REM Create two TAP adapters
echo Creating first TAP adapter...
"%OPENVPN\_DIR%\tapctl.exe" create --name "teqplay-prod"
if %errorlevel% neq 0 (
echo Failed to create teqplay-prod adapter
)
echo Creating second TAP adapter...
"%OPENVPN\_DIR%\tapctl.exe" create --name "teqplay-dev"
if %errorlevel% neq 0 (
echo Failed to create teqplay-dev adapter
)
echo.
echo Listing all TAP adapters:
"%OPENVPN\_DIR%\tapctl.exe" list
echo.
echo Done! You should now see "teqplay-prod" and "teqplay-dev" in your Network Connections.
echo Use them by adding to your .ovpn files
echo under "dev tun" add the line:
echo dev-node "teqplay-prod" --> for the production vpn config
echo dev-node "teqplay-dev" --> for the development vpn config
echo.
pause

To check if the TAP adapters where successfully created you can see them by going to

**control panel** -> **view network status and tasks** -> **change adapter settings**

If you want to do this manually you can create a TAP Adapter via this command

powershellwide760PATH\_TO\_TAPCTL/tapctl.exe create --name "NAME\_OF\_TAP\_ADAPTOR"

Make sure to add the `dev-node "NAME_OF_TAP_ADAPTOR"` to your `.ovpn` config

# MacOS setup

Have your dev ovpn and production ovpn file ready.

Go to releases of [TeqplayVPNClient](https://github.com/teqplay/teqplay-vpn-client/releases) and download the latest release.

Unzip and put the contents in /Applications

Open up a terminal, go to `/Applications` and do this command:

`xattr -cr TeqplayVPNClient.app`

Now you can start the application.

Import both profiles.

As soon as you connect to the first profile it will ask you to install a helper. This will allow to open up vpn connections.

Now you can connect to both develop and production cluster.