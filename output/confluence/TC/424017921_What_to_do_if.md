---
id: confluence:424017921
source: confluence
type: page
space: TC
title: What to do if...
author: Richard van Klaveren
date: '2026-08-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/424017921
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/424017921
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/424017921/What+to+do+if...#ALERT%3A-DOWN-PRIO2-PORTCALL%2B
---
# What to do if...

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/424017921  

## Content

This section captures a couple of thoughts on what a specific message received as a devops person could mean, and how the cause could be verified.

61falsedecimallisttrue

# Updown related messages

## [updown alert][DOWN] AIS-Hub Office

This message means that <http://Updown.io> did detect that one of the AIS receivers is not sending data to AisHub anymore, or that the page at AISHub where the data reception can be verified is not working properly anymore. [There are 2 AIS receivers 2475, located at Richards home, and 2548 located at the office and using the backenddev to share its AIS information to AISHub](https://bitbucket.org/teqplay/teqplay-wiki/wiki/AISHub%20account). When the AIS receiver at Richards home is down 24 hours our AIS feed from AIS Hub will be disconnected, which means a major issue for Teqplay! Steps to be taken:

1. Check which receiver is in error: [www.aishub.net](http://www.aishub.net/stations?Station%5BSID%5D=&Station%5Bstatus%5D=0&Station%5Buptime%5D=&Station%5BCOUNTRY%5D=&Station%5BLOCATION%5D=Poortugaal&Station%5BCOUNT%5D=&Station%5BDISTINCT%5D=). Instead of using the overview, the updown alert also includes which receiver is down.
2. If the overview is not working, nothing can be done, send an E-mail to AisHub [aishub@astrapaging.com](mailto:aishub@astrapaging.com)
3. If the AIS Received at Richards' home is down, contact Richard
4. If the received at the office is down: check on backenddev whether the process is still running (you should see AIS messages scrolling by) by reopening the TO\_AISHUB screen
5. If no messages scroll by, stop the dispatcher with a ctrl-c. The screen should exit, if it doesn't, exit the shell with a ctrl-d. Re-start the dispatcher by executing `~/apps/platform/scripts/startAisForwarding.sh`. Messages should start scrolling by after a few seconds.
6. If still no messages are received, restart the AIS received in the office by unplugging the black box and plugging in again, it will connect itself to the backenddev.

## [updown alert][DOWN] BACKENDDEV

<http://Updown.io> detected that the backenddev is not responding anymore to requests on the HTTPS interface. There can be multiple reasons, with related fixes:

1. Check whether the link from a browser is really not responsive: <https://backenddev.teqplay.nl,> normally it should return a 404. If not responsive, check the http version (<http://backenddev.teqplay.nl),> and the http version without port forwarding (<http://backenddev.teqplay.nl:9090).>
2. If the latter does work, but the former don't, the portforwarder is down, forwarding all traffic from normal HTTP / HTTPS ports to specific ports used by the platform (9090 and 9091). SSH to the relevant system, and restart the port forwarding via `/home/ubuntu/apps/platform/scripts/startPortforwarding.sh`. This Typically should start the portforwarders that were crashed. If this does not work, identify the portforwarding process (`ps -ef | grep socat` ) and manually remove all portforwarding processes (`kill -9 [processId]`) before executing the startPortforwarding script again.
3. If all three checks fail, the platform either crashed or is to busy to answer. Login in the relevant environment via SSH, and restart the platform via: `/home/ubuntu/apps/platform/scripts/startBackend.sh`. This will stop and remove the old platform before actually starting a new one again. Afterwards check whether the platform is available both via port 9090 and via https to make sure the portforwarder did not crash as well.
4. If the server is completely unresponsive, forcibly stop and start it again through the AWS console. You need to stop twice to force it, and it takes about a minute. Then start the instance again.

## [updown alert][DOWN] PRIO3 <http://TEQPLAY.COM>

This message means updown detected that <http://www.teqplay.com> is down. Restart of the server of Digital Ocean should be enough.

Note: is the website blocked from your IP only? Then you (or someone) did too many wrong login attempts via your IP. The block should be gone after 2 or 3 hours. Or, check the `fail2ban` plugin on the server, to remove the IP from the blacklist. Also, our office network provider (NetworX) does not block on request type, so if a PING works, then a GET must work as well.

* Go to <https://cloud.digitalocean.com> and login as [developer@teqplay.nl](mailto:developer@teqplay.nl)
* Click on Droplets
* Click on teqplay-live-website
* Go to the power page and do a power cycle
* The virtual server the website is on will restart now

Digital Ocean has a new layout:

* In the drawer on the left side under projects → Teqplay-website
* Under droplets select the active teqplay-website
* Click on Settings
* Click on Restart
* Enter the droplet name and restart

## ALERT: DOWN PRIO2 PORTCALL+

Portcall+ is responsible for collecting portcall information from different sources, formatting them in the same way and sharing updates on those portcalls with other components. For every port authority a separate connection is made. This message means that any of the tasks running to fetch and process portcall details might be down. Due to the low update rates of portcalls, typically there is no major issue if any of these connections is down for say an hour, but if it starts taking longer than a couple of hours things might start to impact operations. It is logged in slack which adapter is degraded or down, but an overview can be retrieved by

* Go to [portcall+ status link](https://portcallplus.teqplay.nl/actuator/health)
* This will indicate which task failed to run as scheduled in the `detailedStatus` field

Adapters are:

* **DIGITRAFFIC** - Connection to the Finnish port authorities, retrieving the portcalls as described in [this page](https://www.digitraffic.fi/en/marine-traffic/). Currently(11-2024) no operational systems are depending on portcall data from Finland coast. no direct POC is known. Status page can be found [here](https://status.digitraffic.fi/), and there is no support mail address, the support channel for Digitraffic Maritime is Google Group <https://groups.google.com/g/meridigitrafficfi>
* **ENIGMA\_SCRAPER\_INCOMING** - Scraping the website of all expected incoming vessels for Northseaports in [this page](https://en.northseaport.com/enigma/detail/19/expected-arrivals). Data is used operationally for reporting in Terneuzen, Flushing and Ghent. We do not have a POC to be contacted.
* **ENIGMA\_SCRAPER\_OUTGOING** - Scraping the website of all expected departing vessels for Northseaports in [this page](https://en.northseaport.com/enigma/detail/21/expected-sailings). Data is used operationally for reporting in Terneuzen, Flushing and Ghent. We do not have a POC to be contacted.
* **LIS\_SCRAPPER** - Scraping the information from the pilots for NorthSeaPorts to augment information from Antwerp and Northseaports. Page being scraped is located [here](https://lis.loodswezen.be/Lis/VerwachteReizen.aspx). No POC available.
* **PORTCALL\_SYNC** - A sync to the portcalls in another version of portcall+, e.g. the dev version connecting to the live version.
* **SG\_MDH\_DUE\_TO\_ARRIVE** - Retrieval of portcalls for vessels due to arrive from the API at [Singapore Maritime Datahub](https://sg-mdh.mpa.gov.sg/), holding data from Singapore. Helpdesk can be reached via ‘[digitalport@mpa.gov.sg](mailto:digitalport@mpa.gov.sg)’
* **SG\_MDH\_DUE\_TO\_DEPART** - Retrieval of portcalls for vessels due to arrive from the API at [Singapore Maritime Datahub](https://sg-mdh.mpa.gov.sg/), holding data from Singapore. Helpdesk can be reached via ‘[digitalport@mpa.gov.sg](mailto:digitalport@mpa.gov.sg)’
* **SG\_MDH\_VISIT\_ARRIVAL\_DECLARATION** - Retrieval of portcalls for vessels due to arrive from the API at [Singapore Maritime Datahub](https://sg-mdh.mpa.gov.sg/), holding data from Singapore. Helpdesk can be reached via ‘[digitalport@mpa.gov.sg](mailto:digitalport@mpa.gov.sg)’.
* **VOPAK\_NOMINATION** - Connection to the VOPAK Myservice, sharing the terminal planning of multiple terminals (Houston, and 4 at Singapore) of Vopak, by sharing nominations. Direct contact is ‘[myvopak@vopak.com](mailto:myvopak@vopak.com)’ for the service itself and alternatively ‘[cs.dp@vopak.com](mailto:cs.dp@vopak.com)’ should help (on giving access to the right resources). Source has been added for an experiment, and kept up-to-date after, but currently (11-2024) no operational systems are dependent upon it.
* **NXTPORT\_V2** - Connection to Antwerp Port Authority providing updates on portcalls. The source can be updated every 15 minutes (without requesting to much data) on live and every 30 minutes on dev. More details on the API can be found [here](https://console.nxtport.com/). This one is used in operational context. Support tickets can be created [here](https://nxtport.atlassian.net/servicedesk/customer/portal/1).
* **MARITEAM\_PORTBASE** - Connection to PortBase, authorizing using the Mariteam access token, and thus only retrieving Mariteam portcall information in PortBase for Rotterdam and Amsterdam portcalls. Data overlaps with the data retrieved via Hamis / IRIS and thus is not used in operations, except for the invoice reference. So, when down no major issue. Support Mail address: [CustomerService@portbase.com](mailto:CustomerService@portbase.com)
* **OUDKERK\_PORTBASE** - Connection to PortBase, authorizing using the Oudkerk access token, and thus only retrieving Oudkerk portcall information in PortBase for Rotterdam and Amsterdam portcalls. Data overlaps with the data retrieved via Hamis / IRIS and thus is not used in operations, except for the invoice reference. So, when down no major issue. Support Mail address: [CustomerService@portbase.com](mailto:CustomerService@portbase.com)
* **S5\_PORTBASE** - Connection to PortBase, authorizing using the S5 access token, and thus only retrieving S5 portcall information in PortBase for Rotterdam and Amsterdam portcalls. Data overlaps with the data retrieved via Hamis / IRIS and thus is not used in operations, except for the invoice reference. So, when down no major issue. Support Mail address: [CustomerService@portbase.com](mailto:CustomerService@portbase.com)
* **VOPAK\_PORTBASE** - Not valid or used anymore, has been migrated to IAMCONNECTED\_PORTBASE.
* **IAMCONNECTED\_PORTBASE** - Connection to Portbase retrieving portcalls for all users providing us access via the authorization portal. It is a follow-up for above mentioned single authentication connections, but also this one is a paid one. In order to retrieve details, please login on <https://www.iamconnected.eu/>. At the moment of writing, this only is used to retrieve portcalls for Vertom and Wilhelmsen Rotterdam and Amsterdam. Data overlaps with the data retrieved via Hamis / IRIS and thus is not used in operations, except for the invoice reference. So, when down no major issue. Support Mail address: [CustomerService@portbase.com](mailto:CustomerService@portbase.com)
* **CORPUS\_CHRISTI** -

  1
  1
  incomplete
   to complete!

If it is not an external system, we could kick a task into force execution by using a POST to the `start` or `stop` endpoints:

## PORTCALL+ NXTPORT\_V2 agents can’t be retrieved from Port Of Antwerp Bruges (POAB) - automated solution

Currently (2025-04-01) the POAB site has an IP-location filter to obtain stays info (i.e. <https://www.portofantwerpbruges.com/api/cpoint/getByNumber?shipType=seaship&number=9523548>).  
For this, we’ve set temporary a microservice (Springbased) application in DigitalOcean, located in Rotterdam to act as a bypass (<http://104.248.91.46:8080/v1/antwerp/stay?shipType=seaship&number=9523548>).

### These are relevant info to know:

* The DigitalOcean POAB bypass runs on [104.248.91.46](http://104.248.91.46:8080/v1/antwerp/stay?shipType=seaship&number=9523548). It’s needed to get an ssh key (similar/not necessarily the same to accessing to Platform). Ask  to set it up or look at “Antwerp Proxy” or “Digital Ocean” entries in Bitwarden.
* Portcall+ pods (live and dev) require allowing outgoing calls to the port the Digital Ocean service, by the port 8080.
* If a fix is needed

  + Use the repository <https://github.com/teqplay/antwerpportproxy-backend> . There’s only a master branch, as it’s a simple and short-term solution.
  + SSH in the machine, check the *screens* opened with :

    screen -ls
  + Enter the screen where the pod is running with:

    screen -r <antwerportproxy-app-screen-entry-in-list>
  + Stop the service with CRTL+C
  + Change directory to `antwerpportproxy-backend`

    cd antwerpportproxy-backend
  + Pull changes

    git pull
  + Change directory back and invoke the script `./mainBoot.sh` or run the application with gradlew or :

    cd ..
    ./mainBoot.sh

    or

    ./gradlew bootRun
  + Closing the terminal doesn’t terminate the spring app, but worth to double check with a call to <http://104.248.91.46:8080/v1/antwerp/stay?shipType=seaship&number=9523548> in the browser (use a recent Antwerp portcall’s IMO).  
     If you closed the Screen itself, recreate it so to be able to exit your terminal without terminating the spring app.
* **Bitwarden** relevant entries summary:

  + Antwerp Proxy → Linux credentials to access to the machine or invoke sudo.
  + DigitalOcean.com → Digital Ocean credentials in case of needing to reconfigure the machine.
  + Antwerp port proxy app (library fetching for building) → S3 credentials to fetch libraries to build.

## PORTCALL+ NXTPORT\_V2 agents can’t be retrieved from Port Of Antwerp Bruges (POAB) - Manual solution

Sometimes it is not only the endpoint to retrieve agents but also the NxtPort endpoint being limited to locations in Belgium / The Netherlands. So, in that case the manual approach to address this temporary is to execute the following about 3 times spread over the day:

* We manually call the NxtPort service (<https://api.nxtport.com/portstays/v1/stays?date=2025-11-08T00:00:00Z>) polling for updates, and post the results on the newly added endpoint (<https://portcallplus.teqplay.nl/v1/fix/nxtport/processVesselStayData?date=2025-11-08T00:00:00.000Z>) to inject them into PortCall+
* We check in the database which portcalls in Antwerp do not yet have an agent assigned, and manually collect the agent from the website (<https://www.portofantwerpbruges.com/api/cpoint/getByNumber?shipType=seaship&number=9848479>). When updating the PortCall+ database, make sure you add the field ‘VesselAgent’ and updated the ‘updateTimestamp’.
* Then we update the agent in the portcall+ database and send out an event to PortReporter that the agent has changed  (<https://portcallplus.teqplay.nl/v1/fix/fireMissedAgentChangedEvents>) where you post in the body a list of portcallIds of the updated portcalls.

## [updown alert][DOWN] PORTCALL+ because SSL certificate issue external server

How to temporary accept a certificate that might be outdated or corrupted in EBS:

* login into the relevant EBS instance
* Create a file (sudo) in `/etc/pki/ca-trust/source/anchors/` with the content of the base-64 export
* run `sudo update-ca-trust extract` to update the certificate trust store with the new certificate
* restart tomcat: 'sudo service restart tomcat.service' to run the service accepting the newly added certificate

## ALERT: AIS FEED 2475 DOWN!

Same issue as '[updown alert][DOWN] AIS-Hub Office' but now detected by an internal monitor in the platform. Steps to repair are the same

# Platform related messages

## ALARM: "TEQPLAY-DEV-High-CPU-Credit-Usage" in EU (Ireland)

This alarm happens if one of the machines uses for some time more CPU power than expected.

* It regularly occurs on a restart of the machine, so first check whether anyone was giving the system a restart
* If this is on the backenddev once in a while the TO\_AISHUB feed taking the AIS from the office AIS instance and bringing it to AisHub is taking all CPU power available. Login to the screen TO\_AISHUB and restart the process running there.
* Login to the system via SSH and check whether the high cpu use is a continuous one via the `htop` command. It can als be determined from whether it is a certain thread taking all cpu power or not.
* Try to identify which process is causing the high CPU power use by watching the screen BACKEND on one terminal, and watching the performance (htop) on another terminal, is any correlation visible?
* Try to trace down the relevant thread via the `/home/ubuntu/busyThread.sh` which writes to the console all threads in a java process and what they are doing. Please note: The ids of the java threads resulting from the busythread.sh are hexadecimal coded, the ones in htop are decimal coded.

## HamisPortcallAdapter is down!

wide760

This is now running on backend instead of pronto

If Hamis is down for more than 1 hour (or preferrably even within half an hour), all PortReporter users in Rotterdam need to be informed. How to do this is described here: <https://docs.google.com/document/d/1x6j0mjaPH1HBuIFDAWPKobInsaFRI_sJcf0gVMEz2mM/edit> ("Hamis or IRIS down").

This monitor receives portcall updates from Hamis via a REST endpoint and expects a JSON response. To check if it is a problem with Hamis itself, do the following query on POSTMAN (or equivalent):

GET [https://api.portofrotterdam.com/v1/events?from={communicationId}](https://api.portofrotterdam.com/v1/events?from=%7BcommunicationId%7D) E.g. 13539353.

Headers: apikey <key as listed in LastPass note (search for Hamis)>

The latest communicationId processed by the respective platform can be seen in the `cache_keyBased` collection with \_id: "CACHE\_HAMIS\_MESSAGE" under `lastId`.

In case of problems with Hamis REST endpoint contact information could be found [here](https://drive.google.com/file/d/1D7OLJ3HJms-rxWCqdSuzIhfgroIVwNuc/view?ths=true)

If IrisPortcallNLRTMAdapter is not down, it's possible to switch to that service to still have the portcall information available. You can do this by using the portcall monitor switch endpoint.

wide760curl --request POST \\
--url <https://backend.teqplay.nl/portcall/monitor/configure> \\
--header 'authorization: ' \\
--header 'content-type: application/json' \\
--data '[
{
"name":"HamisPortcallAdapter",
"enabled": true,
"allowedEvents": [],
"disallowedEvents": ["ALL\_EVENTS"]
},
{
"name":"IrisPortcallNLRTMAdapter",
"enabled": true,
"allowedEvents": ["ALL\_EVENTS"],
"disallowedEvents": []
}
]'

Don't forgot to turn it back to the default config after Hamis is back online again.

wide760curl --request POST \\
--url <https://backend.teqplay.nl/portcall/monitor/configure> \\
--header 'authorization: ' \\
--header 'content-type: application/json' \\
--data '[
{
"name":"HamisPortcallAdapter",
"enabled": true,
"allowedEvents": ["ALL\_EVENTS"],
"disallowedEvents": []
},
{
"name":"IrisPortcallNLRTMAdapter",
"enabled": true,
"allowedEvents": ["ETAREQUEST", "ETA", "HAMISETA"],
"disallowedEvents": []
}
]'

## BICS connection issues

When you get messages like this on backend, it's probably means BICS is requiring a restart:

`something went wrong when creating voyage: java.net.SocketTimeoutException: connect timed out`

Go to EC2 and restart the machine `BICS live`

# RabbitMQ is down!

To investigate what is wrong:

* Check if <https://rabbitmq.teqplay.nl:15671/> is up
* Check the memory and diskspace usage on the management panel

When the server is not accessible :

* Connect to the EC2 server with SSH
* Try to restart the rabbitmq-server with `sudo service rabbitmq-server restart`
* While restarting check `sudo service rabbitmq-server status` and when its done check the management panel
* If it did not work, reboot the EC2 instance and check if the management panel is accessible again (This may take up to 5 mins)

All the queues should automatically reconnect again in ~2 minutes and read/write again from their respective queues.

If restarting didn't work, last resort is to create a new EC2 + RabbitMQ instance:

* Find the latest snapshot of RABBITMQ
* Create an image
* Launch instance with image (Do not forget to set the security group to RabbitMQ and set the KEY\_PAIR\_NAME to DEV\_KEY)
* Login on the server with ssh and set the hostname with `sudo hostnamectl set-hostname rabbitmq-live`
* Restart rabbitmq-service `sudo service rabbitmq-server restart`
* Reconfigure all the applications that used the RabbitMQ LIVE

## RabbitMQ can’t bind a PVC because it’s already bound to another node

**Problem**  
RabbitMQ pods fail to start and show errors indicating that the PersistentVolumeClaim (PVC) cannot be mounted because it is already bound to a different node.  
This commonly happens with StatefulSets when a pod was previously scheduled on another node and Kubernetes cannot reattach the volume automatically (for example after a node issue or reschedule).

**Symptoms**

* RabbitMQ pod stuck in `Pending` or `ContainerCreating`
* Events show volume attach/mount errors
* Error mentions PVC already bound or attached to another node

**Solution**  
Force a clean re-creation of the RabbitMQ pods so Kubernetes can safely reattach the PVC.

**Steps**

1. Scale the RabbitMQ StatefulSet down to zero replicas:

   bashkubectl scale statefulset -n brokers rabbitmq-cluster --replicas=0
2. Wait until **all RabbitMQ pods are fully terminated**:

   bashkubectl get -n brokers pods

   Ensure no RabbitMQ pods remain.
3. Scale the StatefulSet back up to the desired number of replicas:

   bashkubectl scale statefulset -n brokers rabbitmq-cluster --replicas=1

   (Adjust the replica count if needed.)
4. Verify that the pod starts successfully and the PVC is mounted:

   bashkubectl get -n brokers pods
   kubectl describe pod rabbitmq-cluster-0

**Result**  
The PVC is detached from the old node and correctly reattached, allowing RabbitMQ to start normally.

## You need to change RabbitMQ’s configuration

RabbitMQ is no longer installed via a helm chart and now uses the RabbitMQ Cluster Operator

When using the RabbitMQ Kubernetes Operator, you do not edit the resources directly. Instead, you modify the Custom Resource (CR), and the operator reconciles the changes automatically.

RabbitMQ clusters are defined using a `RabbitmqCluster` resource.

Example:

wide760apiVersion: rabbitmq.com/v1beta1
kind: RabbitmqCluster
metadata:
name: my-rabbit
spec:
replicas: 3

The operator watches this resource and ensures the actual cluster matches the spec.

in lens this can be found under:

wide760Custom Resources:
rabbitmq.com
Rabbitmq Cluster:

# Alongside monitor ssl-dev-queue queue is DOWN

Example message:

wide760Alongside monitor
ssl-dev-queue queue is DOWN
No messages received for 60 minutes (limit 60)

To check whether we indeed don't receive messages anymore, look into the RabbitMQ user interface of <https://www.cloudamqp.com/.> Credentials and url can be found in LastPass.

If we indeed do not receive messages anymore, we have to let the guys from SSL know. This can be preferrably done via E-mail via [ict@ssl.nl](mailto:ict@ssl.nl). Alternatively this can be done via the Slack channel "alongsidemonitor" in the "Teqplay Projects" Slack (not really monitored anymore). Addresses are listed in Google Drive "Teqplay OPS/DevOps/Support/POC\_SSL\_ALONGSIDEMONITOR".

# Vesselmatcher

The system can report down if

* no email was received in the last 8 hours (or otherwise configured with `health.emailimport.other.idletime`)
* no ship visit planning was received for some time
* or other components, like RouteScout

## Detailed down/degraded info

The `/actuator/health` endpoint gives very brief information by default. The detailed response tells you exactly which component is down. To get the detailed response:

* Use the `/actuator/health` endpoint to retrieve the info
* Search in Lastpass for the token (should never expire, dev and live have a different token): 'VesselMatcher health token'
* Use the retrieved token in the `M2M-Authorization` header (no further 'Authorization' header needed)
* Execute a GET request:

wide760# LIVE
curl --request GET --url <https://backendvesselmatcher.teqplay.nl/actuator/health> --header 'M2M-Authorization: PASTE\_TOKEN\_HERE'
# DEV
curl --request GET --url <https://backendvesselmatcherdev.teqplay.nl/actuator/health> --header 'M2M-Authorization: PASTE\_TOKEN\_HERE'

Log file:

* `/var/log/tomcat/vesselmatcher.log` or
* Cloud Watch -> Log Groups -> `vesselmatcher-prod-1-end` or `vesselmatcher-dev-1` -> vesselmatcher.log

## emailImport reports DOWN

* Check when the last email was received, search in the log for `EmailController: Imported email`
* If that is long ago (like an hour during working hours, or 8 hours outside working hours), do the following:
* Send an email to [incoming@vesselmatchermail.teqplay.nl](mailto:incoming@vesselmatchermail.teqplay.nl). The datetime and subject are logged, so use something you will recognize.
* Check the log file if your email arrived
* If the email did not arrive, then the incoming mailserver [vesselmatchermail.teqplay.nl](http://vesselmatchermail.teqplay.nl) (or a process there) might be down. See the architecture document how this is configured: <https://docs.google.com/document/d/1YnXwbIL0BnOZc8763AoxQt_pcj_ZtxeZ8TvSiKiRJHg>

### planningImport reports DOWN

* Vertom sends their ship planning to us every 30 minutes, between 7:00 and 18:00 (NL time).
* Check when the last planning was sent to our back-end, search the log file for `VisitImportService: Imported`
* If the ship planning is not received within the stated hours, we should contact Vertom why they are not sending it. There is a WhatsApp group where contact takes place. Leon, Richard and Joaquin are in that group. An example message to be sent “We have not received any planning updates in Vesselmatcher in the last X hours, could you please check your systems are still sending?”
* The system will still function without new ship planning

### diskSpace reports DOWN

* Disk space of our incoming mail server, [vesselmatchermail.teqplay.nl](http://vesselmatchermail.teqplay.nl), is running out. When the disk is full, incoming emails cannot be processed
* See the architecture document on how the server is set-up: <https://docs.google.com/document/d/1YnXwbIL0BnOZc8763AoxQt_pcj_ZtxeZ8TvSiKiRJHg>

## Adapter StreamingLiveInstanceAisMonitorAdapter is down! / Adapter StreamingAreaMonitor is down!

This means that the backend isn't receiving updates anymore. Go to the RabbitMQ management page to checkout the queue for this backend.   
[RabbitMQ Live Management](https://rabbitmq.teqplay.nl:15671/#/queues)   
[RabbitMQ Dev Management](https://rabbitmqdev.teqplay.nl:15671/#/queues)

* If the total amount of messages for this backend is rising and it isn't decreasing, it means the backend isn't consuming the messages anymore. It also didn't reconnect automatically (hence getting the down message), so a manual platform restart is required.
* If the total amount of messages is zero and it isn't rising, it means the producer isn't sending updates anymore. Either AISDATA or AISDATADEV stopped sending updates and couldn't reconnect automatically, so a manual platform restart is required.

If these steps didn't resolve the issue it means it's a RabbitMQ issue, and you need to resolve it there.

## Adapter frieslandBridges.watchdogMonitor - Failed running

A watchdog runs to safeguard the connection between Friesland Swettehuus and teqplay. This connection goes over many hops (for safety) and firewalls. The first one is 'Enable U' converting our API request into an internal event on their bus. The watchdog reports down when no watchdog was successfully returned for 5 minutes. Therefore, things will need to be escalated. Formal escalation procedures are not yet fully ready, but it is clear that 2 parties will need to be contacted:

1. Enable U: Send them a mail [support@enable-u.com](mailto:support@enable-u.com) or call them on 085-8881133
2. cc in the mail the province Fryslan (for coordination purposes) via mail on swettehus-td-ruimte@fryslan.frl or call them on 058-2928272

Please note that support is only required between 9:00 and 21:00 including weekends.

# EKS related messages

## EKS Node is crashing

When a node is crashing/stuck, you most likely will not see any condition when going to the Nodes tab in Lens. This means we can skip any attempts to restart the node and do a hard restart.

Prep: Copy the `InternalIP` of the crashing node. This will be needed to easily find the node in step 2.

1. Drain the node that is crashing. This can be done inside Lens once the node has been selected, as seen in the screenshot below. This will unregister all pods stuck on the node, making them try to relocate if possible.

2. Terminate the node in EC2.
3. Wait for a new node should be registered in around 2 minutes. The applications should all automatically start up.
4. If this doesn't happen, up the number of nodes in the AWS console, at the EKS section. *EKS -> Cluster name -> Compute -> Node groups.* Select and edit the node group the node was part of. Set the desired count to 1 higher.

**Only do the next step on production if the volume is stuck on the old machine, and the crashing node is stuck on terminating state!**

5. In EC2, EBS, lookup the stuck volume and *Force detach volume*.
6. Delete the Pod that can't be spinned up, this way a new pod will be created and the disk will be attached to the new node.

## EKS Node is running out of storage space

When Zabbix reports that more than 80% of storage has been used, then you need to check where and what you can delete on the machine to free some space.

* SSH into the node (This can be done in Lens by clicking the "Node shell" button in the top right)
* Check what folders are currently using the most space (for example, by executing `du -sh -- *`)

The easiest way of clearing space would be by removing unused Docker images (as currently, all of them are being cached on the machine itself). The images can be found in `/var/lib/docker/overlay2`. If this folder is big, use the following docker command to prune the images `docker image prune -a`.

A different option where you can clean up

If you find that one of the mounts is taking too much storage space, they can be ignored as they are attached to the system and shouldn't interfere with the node's storage. (They are located in `/var/lib/kubelet/plugins/kubernetes.io/aws-ebs/mounts/...`)

## EKS MongoDB is crashing/continuously restarted

If the mongodb pod in EKS is continuously being restarted due to being killed too early, you could relax the `startupProbe` to have a longer timeout.

Going into the `deployment` of that mongodb pod you should see `startupProbe` being set. If not, you should copy the content of the `livenessProbe` into a new section. The `startupProbe.failureThreshold` determines how many times the probe is retried until it fails. This value can be increased to a higher value to allow for more failures before restarting. The time it takes for the pod to be restarted also depends on the `startupProbe.periodSeconds`. `startupProbe.periodSeconds * startupProbe.failureThreshold` is the maximum amount of time it takes before the pod is restarted. A `startupProbe.periodSeconds = 10` with a `startupProbe.failureThreshold = 30` allows for 5 minutes before being restarted.

You could also consider migrating the disk to `gp3`, if it uses `gp2`. But this could take a very long time depending on the disk size, so should not necessarily change that now.

## EKS cluster backup is (partially) failing

Install the Velero CLI. See here

Follow the troubleshooting steps on What to do when a backup fails

# NATS node complaining after a restart

see: <https://github.com/teqplay/kubernetes-scripts/blob/master/nats/docs/troubleshooting.md>

# (r)events scenario crashing or nodes not being cleaned

In case revents is having an issue, see the troubleshooting section here: <https://bitbucket.org/teqplay/ais-engine/src/master/app/revents-engine-api/>

# Switch AIS Forwarder AISHub feed to backup ip address

Connect to the AIS Forwarder machine via SSH

Turn off the main feed  
`sudo systemctl stop aishub-forwarder.service`

Wait for half a minute to make sure socat is killed

Turn on the backup feed  
`sudo systemctl start aishub-forwarder-backup.service`

Check with `sudo systemctl status aishub-forwarder-backup.service` if everything is running active and running.

On restart of the machine, the main feed is used again.

# Switch Encounter Events back to Platform Encounter Monitor

Platform rebuild - tech support info

# Vessel Compliance (Navista)

Has a separate what-to-do-if page: Tech support / What to do if...

# KV\_something: NATS left-over KV consumer

We're currently being affected by what seems to be a NATS bug where KV consumers are not being cleared up properly. You can delete such a consumer by opening a shell on the `nats-box`. First, select the correct context using `nats context select` (most (all?) kv stores are in the `events` context). Then, inspect the consumer you want to remove by doing `nats consumer info -a`. Select the `KV_something` stream as shown in the alert, and you should see the consumer that is stuck being listed. Select the consumer, and ensure that the info shown shows "No interest" at the bottom. This means that no-one is using that consumer. Then, using `nats consumer rm -a`, select the same consumer again to delete it.

# Alert: Disk is filling-up data-rabbitmq-cluster-X

This alert indicates that the disks under one (or multiple) of the nodes under the rabbitMQ cluster is filling-up. Multiple reasons have been noticed in the past:

* One of the consumers stopped consuming messages, so the queue is filling-up, which is stored on the disk. Possible solution directions:

  + Find the queue that is not consumed anymore and make sure the consumer will consume again
  + Empty the queue (NOTE: this means loosing data, so make an assessment if this is the best solution). When the disk is filled-up to 100% and one of the nodes under the cluster is down, purging of the data does not work anymore in all cases, in that case, first increase the disk-size
  + Increase the disk-size to buy some time: in LENS, navigate to the involved Pod (e.g. rabbitmq-clute-2), open the info panel in scroll down to ‘volumes’. Click on the volume name being mentioned in the alert, and edit it by clicking the pencil in the top-bar. Scroll down to the ‘Spec’ section and update the `spec.resources.requests.storage` and increase the size. Restart the relevant pods via `deployments`.
* AWS-fluent-bit running on the node not able to upload log-data to AWS anymore and therefore putting all on the disk. Solution (if in time): restart the AWS-Fluent-bit pod running on this node

# Disk full under Kubernetes Node

There are multiple ways to recover from a situation where a disk is full and will not start-up anymore for that reason:

1. **A clean way**: create a new node-group and move the nodes in the old node-group to the new node group, described in this article here (at the bottom).
2. **A quick-fix:** Increase the size of the disk and remove the underlying cause of continuous growth. For that login into AWS console in the EC2 Service and execute the following steps (light blue is optional):

   1. Resize disk on in EC2 directly on the volume *(EC2 > instances)*

      1. Look up EC2 machine via private ip address.
      2. Go to storage, and open the volume mounted on `/dev/xvda` which should be the node disk.
      3. Press `Modify` and change `Size (GiB)` to new value.
   2. Go to the Auto Scaling Group of the node. *(EC2 > Auto Scaling Groups)*

      1. Can be found at the detail mentioning `Auto Scaling Group name` .
   3. Adjust launch template setting desired disk size to new value. *(EC2 > Launch Templates)*

      1. Press the `View details in the launch template console` in the Auto Scaling Group.
      2. Top right, Actions -> `Modify template (Create new version)`.
      3. Under `Storage (volumes)` set the disk size to what it needs to be.
   4. Restart EC2 node where this change needs to happen. *(EC2 > Instances)*

      1. Right click the node in EC2 -> `Reboot instance`.
   5. Fix the underlying cause for filling-up the node (e.g. restart the aws-fluent-bit pod that was crashed from Lens)

# Platform error message - "PKIX path building failed" and "unable to find valid certification path to requested target"

This can occur if the target’s self signed certificate has not been whitelisted by us in the JVM and thus we’re unable to scrape contents from the target.  
The solution is to download the certificate (let’s call it exampleCert.crt) from the website ([example.org](http://example.org)) onto your computer from the webbrowser or command line, upload to the server and add the certificate.

## Download certificate from command line on OSX / Linux:

`echo -n | openssl s_client -connect example.org:443 | \ sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > exampleCert.crt`

## Upload the certificate file to the server by SCP

`scp exampleCert.crt user@backendserver.nl:/EXAMPLE_FOLDER_LOCATION`

## Add certificate to the JVM (the location of the folder is depending on the jdk version used on the server, this may need to be looked up first and changed accordingly if the following command doesn’t work):

`sudo keytool -import -trustcacerts -keystore /usr/lib/jvm/java-11-openjdk-amd64/lib/security/cacerts \`  
 `-storepass changeit -noprompt -alias exampleCert -file /EXAMPLE_FOLDER_LOCATION/exampleCert.crt`

## Timeout or no response waiting for NATS JetStream server

When getting this error message in one of our apps it could mean that there is too much strain on the server which is the leader of the stream we try to publish to (e.g. event-stream for any event published).

note607650d7-a380-464b-b9f7-915722b3f493

Make sure you are on the correct NATS context to see the stream that you think is having the issue.

wide760

Make sure you are on the correct NATS context to see the stream that you think is having the issue.

To find out which server the stream leader is:

wide760nats stream report

To scale down to a different server:

wide760nats stream cluster step-down

If that still isn’t enough, you can also move the server of a consumer:

wide760nats consumer cluster step-down

# ship-history-processor failing to start/not consuming

Currently, `ship-history-processor` has an issue where it sometimes can fail to start/consume properly if there is a large backlog of data. If you encounter this issue, the hacky fix is to delete the buffer collections in the underlying Mongo database. You can connect via the VPN to the Mongo instance, and you will see two collections, `shipHistoryByArea_buffer` and `shipHistoryByMmsi_buffer`. Drop these two collections and restart `ship-history-processor`, and it should recover.

# VesselVoyage Processing direct memory buffer errors

Issue: You will see a bunch of exceptions complaining about OOM issues.

nonewide760java.lang.OutOfMemoryError: Cannot reserve 4903399 bytes of direct buffer memory

or even exceptions about:

wide760i.n.u.ResourceLeakDetector: LEAK: ByteBuf.release() was not called before it's garbage-collected.

Fix: Change the existing memory buffer to a bigger size.

1. Adjust the helm release values the `-XX:MaxDirectMemorySize=...` JVM variable should be changed to the size that you want. For example something like this would make the direct memory buffer 250m:

   yamlenv:
   - name: JAVA\_TOOL\_OPTIONS
   value: -XX:MaxDirectMemorySize=250m
2. If the old pod doesn’t shut down, force delete it. This does mean that the shutdown hook won’t be executed correctly.

   1. `kubectl config use-context production`
   2. `kubectl delete pod <NAME OF POD> --namespace voyage --grace-period=0 --force`

# VesselVoyage not processing fast enough (NATS Slow Consumer)

To improve processing performance when **vesselvoyage** is not consuming queues fast enough, the amount of threads that are consuming messages can be increased with the following values in the **ConfigMap**:

#### ConfigMap Keys to Adjust

* `event-processing.total-threads:`  
  *Use if* `vesselvoyage` *is lagging on the **event-stream** queue.*
* `trace.total-threads:`  
  *Use if* `vesselvoyage` *is lagging on **ais-stream:diff** (AIS diff messages).*

#### Consumer Names

* `ais-stream-consume-vesselvoyage` → (**ais-stream:diff**) → *trace threads*
* `vesselvoyage` → (**event-stream**) → *event-processing threads*

---

### Resource Considerations

Increasing thread counts **may require scaling**:

* **vesselvoyage memory/CPU**
* **Database resources**

Always check usage before and after the change.

---

### Restarting vesselvoyage

* Restart **if** :

  + `vesselvoyage` has **stopped consuming**
  + It's **persistently slow** despite increased threads

> Note: Restarting triggers state reloading and ships lazy loading. It may take time for consumption to ramp up. Avoid restarting every few minutes hoping for immediate improvement.

# A Revents job has been ongoing for more than 24 hours

A revents job is probably stuck. Contact the vesselvoyage team to check if this is right. Is not an very important issue, more for insights.

# AIS-Stream

## **PROD SINGAPORE alert: No AIS data Singapore**

SG-MDH Not delivering any AIS-data. See the [Portcall+](https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/424017921/What+to+do+if...#ALERT%3A-DOWN-PRIO2-PORTCALL%2B) section to see when and how to contact SG-MDH.

## PROD KPLER alert: No Ais data from Kpler

**Standard Requests:** Please continue to email [**cs@kpler.com**](mailto:cs@kpler.com)or [**customersupport@marinetraffic.com**](mailto:customersupport@marinetraffic.com). For password resets, account queries, or general navigation help, please use our email to ensure the emergency line remains open for critical system issues.

**Urgent technical outages:** We have launched a dedicated Emergency Report Line. This number is strictly for reporting critical system outages or total loss of service that cannot wait until the next business day.

**EUROPE: +32 2315 0223 / +44 131 392 9565**

**APAC: +65 3138 2094**  
**AMERICA: +1 626 380 0410**  
Please note: you will be asked to leave a voicemail with your name, contact details, and a description of the issue.

# Redis

**Setup context:**

* 1 Redis **master**, 2 **replicas**,
* Each Redis pod runs its own **Sentinel** sidecar
* **AOF (Append Only File)** enabled for data persistence
* Automatic failover handled by **Sentinel**

---

## Sentinels can’t elect a new master

**Symptoms:**

* No pod has the role `master`
* `redis-cli INFO replication` shows all as replicas
* `redis-cli sentinel masters` shows that master is down
* Sentinel logs contain “Could not find a suitable master” or “failover state: waiting for votes”

**Actions:**

1. Try resetting Sentinel:

   bashredis-cli sentinel reset mymaster
2. If still stuck:

   * Restart all redis pods at once  
     (in Kubernetes):

     bashkubectl scale statefulset redis --replicas=0 -n brokers
     kubectl scale statefulset redis --replicas=3 -n brokers

     *(Adjust StatefulSet name if different)*
3. If failover still doesn’t complete:

   * Manually promote a node:

     bashredis-cli -h <replica-host> -p <replica-port> slaveof no one
   * Then make other replicas follow it:

     bashredis-cli -h <replica-host> -p <replica-port> slaveof <new-master-host> <new-master-port>
   * Finally reset Sentinels again:

     bashredis-cli sentinel reset mymaster

---

## AOF file corruption

**Symptoms:**

* Redis fails to start: “AOF read error” or “Bad file format”
* Pod in CrashLoopBackOff

**Actions:**

1. Run repair manually:

   bashkubectl exec -it <redis-pod> -- redis-check-aof --fix /data/appendonly.aof
2. Restart pod afterward:

   bashkubectl delete pod <redis-pod>
3. Validate Redis is up and role assigned.

**Redis AOF documentation:**

<https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/>

---

## Cluster shows inconsistent roles (multiple masters)

**Symptoms:**

* Two nodes both show `role:master`
* Sentinel logs show conflicting failovers

**Actions:**

1. Pick the correct master (based on latest data / AOF timestamp)
2. For others:

   bashredis-cli -h <wrong-master> slaveof <correct-master-host> <port>
3. Reset Sentinels:

   bashredis-cli sentinel reset mymaster

---

## How to verify Redis cluster health

Quick checklist:

| Check | Command | Healthy Output |
| --- | --- | --- |
| Master present | `redis-cli info replication` | One `role:master` |
| Replicas connected | `redis-cli info replication` | `connected_slaves:2` |
| Sentinel view | `redis-cli sentinel masters` | Correct IP/port for master |
| Sentinels Status | `redis-cli sentinel sentinels mymaster` | Correct IP/port for sentinel instances |
| AOF status | `redis-cli info persistence` | `aof_enabled:1` & no errors |
| Connectivity | `redis-cli ping` | `PONG` |

# The VPN is unavailable and you cant access the k8s cluster

## Re-enable Public Access via AWS Console

1. Go to **AWS Console → EKS → Clusters**
2. Select your cluster.
3. Go to the **Networking** tab.
4. Under **Manage**, click Endpoint Access.
5. Change the settings to:

   * ☑ **Public and Private**
   * (Optional) Add **Public access CIDR** in **Advanced settings** → `0.0.0.0/0`  
     → or better: your office IP or your home IP for safety.
6. Click **Save**.

The API endpoint will become reachable publicly again within ~30 seconds.

you can view the status in **Cluster Info** if its still updating.