---
id: confluence:527728643
source: confluence
type: page
space: TC
title: Increasing data quality for ports with low AIS coverage
author: Richard van Klaveren
date: '2024-11-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/527728643
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/527728643
---
# Increasing data quality for ports with low AIS coverage

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/527728643  

## Content

Within Teqplay timestamps on relevant moments are being detected, for example arrival in a port, dropping the anchor or detecting a tug alongside of a sea-vessel. Timestamps are derived based on AIS data, using the different monitors in the AisEngine.

## The challenge

Accuracy of these timestamps normally is quite accurate, compared to what is happening in real-life. Normally an accuracy of having the detected timestamp not deviate more than **6 minutes** of the actual events in real-life is considered accurate.

In most cases this accuracy and timeliness is achievable, when the data is accurate enough, e.g. based on a terrestrial data-source. However, when data is being received via satellite or floating/dynamic AIS timeliness (and thus consequentially usable accuracy in real-time) differs quite a lot since these sources provide:

* Lower amount of updates: Since data is going via satellite with limited bandwidth less messages are passing through
* Messages arriving out of order: Satellites are programmed to dump newest data first when they have connection, resulting in many older messages arriving out of order. These messages arriving out of order are ignored during real-time processing.

The challenge is to have as often as possible the detection in AisEngine accurate enough to still comply to the 6 minutes accuracy. Updating the real-time SOF is not required and extremely complex. The requirement would be to have afterwards the SOF as accurate as possible.

## The solution direction

The solution direction discussed allows taking 3 steps. All steps trust on the (r)events mechanism, which allows to regenerate the events based on the AIS Historical data stored for a certain situation. The idea would be to set a trigger X hours after a vessel left the EOS passage of a port, and then trigger a recalculation of the full visit based on (r)events. However, this is only necessary for ports where we know we have a low AIS coverage. We discussed 2 possibilities to not have to run (r)events for all ports, but only the ones where data quality is at stake:

1. Store with each port in POMA an extra parameter like ‘lowCoverage’ to reflect that visits in that port will need to be recalculated.
2. Extend AreaMonitor to detect when vessels have sparse updates in the port area, share this on the events and mark that for that specific call in Vesselvoyage. This mechanism is a lot more flexible and could also deal with temporary low coverage ports (since the terrestrial source is temporarily disrupted).

Since option 1 is the easiest solution to start with, this was decided to start with at first.

The following steps from easy to complex can be used in this regeneration of VesselVoyage visits:

### Step 1: Take into account also the data that originally arrived out of sequence

The data that arrived out-of-sequence is timestamped at the source and still stored within the Ship-History, and since the data is fed to (r)events afterwards, can be first put in the right order before feeding it to the (r)events engine. Therefore it can be considered properly in the afterwards scenario, providing more data-points and thus increasing data quality. (r)events already has an option to do so, therefore this option could be used out-of-the box.

### Step 2: Download or Buy Data

In order to upgrade the data quality for a port in a certain time-period, we can also buy more accurate data and load this in the ShipHistory before executing the (r)events. Some research has indicated that the [Made Smart Group has the largest and most accurate AIS data store](https://www.madesmart.nl/worlds-largest-ais-data-store/), and allows automated interfacing via an API using the Prospector solution. Basically, you buy a bundle of X Gb (yearly subscription incl 5 Gb costs 13.350 euro, extensions with 10 Gb cost about 9.000 euro, 100 Gb costs 45.250 euro) and can download information per ship or per area whatever you prefer. Indicative, a year of data for a ship will cost about 80 Mb of data. For this step an interface need to be built to connect to the MSG Prospector, to import the data into the ShipHistory. Data can be downloaded in Excel format (holding all AIS fields) or in flat text format holding all AIS fields interpreted:

For US related ports, a lot of historical information is available and exposed by US government via the NOAA initiative. More information and the way to download such data can be found here: <https://hub.marinecadastre.gov/pages/vesseltraffic>

The technical implementation direction discussed and agreed here is to inject data (read from file, uploaded via CSV or read via e.g. a REST interface) directly into the Ais Stream component where also the other data feeds (more real-time) are being processed. This is not expected to result into any issues in detection of events or so, since all data will be classified anyhow as arriving ‘out-of-synch’. This will guarantee that all data is taken into account for the ShipHistory component in just the same fashion as Satellite data arriving 2 days late would be taken into account.

In order to take advantage of this data, (r)events will need to be run, allowing to process data arriving out of sync (see also step 1).

### Step 3: Interpolate data

Independent from whether step 2 (buying data) is executed and not leading to the right quality of data, or not executed, we can enhance the data more based on a smart interpolation mechanism. Basically the idea here would be to use the ETA predictor to generate a specific ETA prediction based on the past few (or 1) data points, where the path is used based on Routescout (preventing the assumption to sail over land). Such solution could be used in 2 different ways:

1. Integrated in the area monitor, and triggering when it is detected that data points inside the port area have very limited updates. The advantage of this approach is that it does not depend on any configuration per port, and can even handle visits ports facing with temporary low coverage.
2. Based on an option per port, where the ETA prediction trace is always generated into the port, and covering also the crossing of other areas (anchor, pilot area, etc).

It has been agreed that all data-points generated by such an interpolation mechanism need to hold a clear indicator that shows they are based on interpolation, and thus cannot be trusted at the same level as an actual measurement.

*Please note that interpolation of data for the purpose of filling-in-the-gaps for statistical analysis as done in PTO has significant risks. It builds on the ‘ceteris paribus’ condition, and therefore this condition needs to be cross-checked before using this method. The proposed method of validation here would be:*

1. *Make a prediction using **extrapolation** of the last (few) point(s) of the vessel. So, taking into account the last speed of the vessel, forecast the path to e.g. the pilot boarding place and calculate when the vessel would arrive over there.*
2. *Make a prediction using **interpolation** of the last point before the AIS was lost until the first point where the AIS was picked-up again, using the predicted path and the time-difference between those 2 points as the reference to calculate the relevant crossing point.*
3. *Compare the results of the extrapolation and the interpolation method. If the 2 methods differ more than 10% (of the interpolated timeframe), the ceteris paribus condition is not applicable since the vessel did not sail with a similar speed. In this case the prediction is unreliable and should be thrown away.*

*Using this method to only calculate the situations where the ceteris paribus condition applied introduces a clear **bias** into the data-set excluding situations where things were deviating from the normal. The risk is this results in highlighting only the happy flow to the PTO customer since all other information cannot be reproduced.*

Step 1 is expected to provide a more or less okay solution for geo-bounding boxes but not for encounter based scenarios, where 2 vessels will need to be close together time-synced. Vesselvoyage does provide fallbacks for e.g. the pilot encounters, when other details are required, buying data seems to be the only option for now.

Scenario 3 most probably will be quite a high investment for limited added value (especially in a statistics case like PTO), and therefore most likely not selected on the short term for implementation. When scenario 3 is used all data-points should be explicitly marked, and no data points should be included anywhere for scenarios where extrapolation and interpolation do not match.