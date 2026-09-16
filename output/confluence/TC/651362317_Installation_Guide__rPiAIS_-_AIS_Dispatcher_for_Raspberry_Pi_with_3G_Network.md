---
id: confluence:651362317
source: confluence
type: page
space: TC
title: 'Installation Guide: rPiAIS - AIS Dispatcher for Raspberry Pi with 3G Network'
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651362317
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651362317
---
# Installation Guide: rPiAIS - AIS Dispatcher for Raspberry Pi with 3G Network

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651362317  

## Content

## Necessities

* Raspberry Pi
* Power Supply
* microSD Card
* 3G network dongle (in this guide: Huawei e3531)
* AIS antenna
* AIS receiver (in this guide: with cable to connect to Raspberry Pi via USB)
* Monitor and keyboard

## AIS Receiver

### Setup

**NOTE:** If DNS resolving does not work: use the IPs for those addresses in `/home/pi/restart_ais_dispatcher`, `/home/pi/restart_ais_dispatcher_no_monitor` and `/home/pi/AisMonitor/aisLiveMonitor-0.0.1-SNAPSHOT.jar`, but check if those IPs are static

**NOTE:** You'll have to check the AisMonitor project if the IP and scraping for AISHub work correctly! (If not, you'll need to build the jar with the correct code and replace this file `/home/pi/AisMonitor/aisLiveMonitor-0.0.1-SNAPSHOT.jar`)

1. Download the SD Card Image on <http://www.aishub.net/rpiais> and format and flash the SD Card.

2. Setup WiFi

* open your SD card
* open wifi folder
* rename the file wlan0.txt.example to wlan0.
* open wlan0.txt with text editor (e.g. notepad) and configure your SSID and WiFi password:

SSID myssid
PASS mypassphrase
COUNTRY NL

**NOTE: You should edit the country code to conform to your country legislation regarding WiFi frequencies and Tx power. Save changes.**

3. After putting in the SD Card into the Raspberry Pi, plugin the monitor, keyboard and finally the power source.

4. Change your password for the Raspberry Pi.

5. Use `sudo raspi-config` to setup necessary options, like localisation and boot options. If you are not automatically logged in use the boot options to setup Console Autologin. Save changes and reboot. You should now be automatically logged in.

6. Replace the home folder with the following

7. Run the following commands:

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install screen
sudo apt-get install openjdk-8-jre

8. Make sure all scripts in the following folders are executable:

/home/pi/
/home/pi/aisdispatcher/aisdispatcher\_arm\_glibc
/home/pi/aisdispatcher/tcpdispatcher
/home/pi/AisMonitor
/home/pi/tcpdispatcher

Do so with `sudo chmod +x [filename]`

9. Change startup script (`/etc/rc.local`) so it runs `sudo /home/pi/restart_ais_dispatcher` on startup

10. In `/home/pi/restart_ais_dispatcher` and `/home/pi/restart_ais_dispatcher_no_monitor` change where the AIS data is sent to (which port).

11. Manually run `/home/pi/restart_ais_dispatcher` with sudo so the screens are started.

12. Check if both `AIS` and `MONITOR` exist with `sudo screen -ls`

13. Check for AIS messages with `sudo screen -r AIS`, exit with `ctrl+a` `d`

14. Check if the monitor is working with `sudo screen -r MONITOR`, exit with `ctrl+a` `d`

### Test

**NOTE:** You need to be able to check the AIS and Monitor messages both internally and externally.

**NOTE:** You might have to wait for a few minutes to see if the setup is working when checking externally.

Here are some test cases to check if the Raspberry Pi is fully working:

1. Manually test the scripts if they are working correctly and don't give any errors

2. Restart the Raspberry Pi (and/or manually restart with `/home/pi/restart_ais_dispatcher`)

* Both screens should be started automatically
* Working connection via internet dongle
* Internal

  + AIS screen receives messages
  + MONITOR says it's online
* External

  + AISHub or another server receives messages from the Raspberry Pi

3. Shutdown the AIS screen with `sudo screen -X -S AIS quit`

* Only screen for MONITOR should exist
* Internal

  + Monitor should restart AIS screen after it is displayed as offline externally
* External

  + AISHub or another server does not receive messages and displays it's offline

4. Disable WiFi (and/or unplug internet dongle)

* MONITOR screen should reboot Raspberry Pi after down counter reaches threshold

5. Unplug power source from Raspberry Pi and plug in again after a while

* Raspberry Pi and screens should start automatically and work correctly

6. Disconnect the monitor and keyboard, change location of the Raspberry Pi and plug in the power source

* Raspberry Pi should start and you should receive messages externally

## 3G Network

1. Put a simcard in the usb internet dongle.

2. If the simcard has a pincode follow the next steps, if not skip to step 7

3. Connect the internet dongle to you computer of laptop. (With the sim in it)

4. Go to the website <http://192.168.8.1>, here you need to fill in your pincode. Make sure that you check the box that says disable pincode.

5. Check on the website (<http://192.168.8.1>) if you have a signal. (the lamp on the usb should turn green if connected to 2G and blue/cyan if connected to a 3G network)

6. Connect the internet dongle to the Raspberry Pi

7. Run the following commands to disable WiFi:

sudo apt-get install network-manager
nmcli radio wifi off

8. Check if the internet connection works :

networkctl -a
networkctl status