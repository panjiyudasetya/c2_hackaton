---
id: confluence:986120193
source: confluence
type: page
space: TC
title: AIS Forwarder setup dev
author: Jamie de Leest
date: '2025-11-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/986120193
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/986120193
---
# AIS Forwarder setup dev

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/986120193  

## Content

This setup provides two lightweight TCP forwarder services using `socat`. Each service listens on a local port and forwards all incoming TCP traffic to an external AIS data provider. The services are managed using **systemd**, ensuring they automatically start on boot and restart on failure.

## Overview

The system runs two forwarders:

1. **AISHub Forwarder**

   * Listens locally on port **12345**
   * Forwards traffic to **144.76.105.244:4475**
2. **FleetMon Forwarder**

   * Listens locally on port **23456**
   * Forwards traffic to **148.251.80.108:32002**

Both services use `socat` to create simple TCP relay endpoints.

---

## AWS Setup

in AWS we are running a EC2 t3.nano `AIS-FORWARDER-DEV` machine with the elastic IP `52.18.232.42` this is one of the we have registered with `fleetmon` and `aishub` and is allowed to call there services

---

## AISHub Forwarder Service

**File:** `/etc/systemd/system/aishub-forwarder.service`

This service listens on port **12345** and forwards connections to the AISHub server at port **4475**.

### Service Definition

nonewide760[Unit]
Description=service to start a socat from 12345 to aishub port 4475
[Service]
Type=simple
StandardOutput=syslog
StandardError=syslog
ExecStart=/usr/bin/socat TCP-LISTEN:12345,fork TCP:144.76.105.244:4475
Restart=on-failure
RestartSec=5s
[Install]
WantedBy=multi-user.target

## FleetMon Forwarder Service

**File:** `/etc/systemd/system/fleetmon-forwarder.service`

This service listens on port **23456** and forwards connections to the FleetMon server on port **32002**.

### Service Definition

wide760[Unit]
Description=service to start a socat from 23456 to fleetmon port 32002
[Service]
Type=simple
StandardOutput=syslog
StandardError=syslog
ExecStart=/usr/bin/socat TCP-LISTEN:23456,fork,reuseaddr TCP:148.251.80.108:32002
Restart=always
[Install]
WantedBy=multi-user.target

---

## Enabling and Starting the Services

After creating the service files, run:

wide760sudo systemctl daemon-reload
sudo systemctl enable aishub-forwarder.service
sudo systemctl enable fleetmon-forwarder.service
sudo systemctl start aishub-forwarder.service
sudo systemctl start fleetmon-forwarder.service

Check status:

wide760sudo systemctl status aishub-forwarder.service
sudo systemctl status fleetmon-forwarder.service