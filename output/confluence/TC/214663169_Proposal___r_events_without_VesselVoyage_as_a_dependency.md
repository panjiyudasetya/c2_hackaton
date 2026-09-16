---
id: confluence:214663169
source: confluence
type: page
space: TC
title: 'Proposal: (r)events without VesselVoyage as a dependency'
author: Former user (Deleted)
date: '2023-09-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214663169
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214663169
---
# Proposal: (r)events without VesselVoyage as a dependency

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214663169  

## Content

(R)events uses VesselVoyage as a dependency to be able to answer:

> *Which ships were in this area/port/terminal/etc.?*

This is important for performance. A scenario to generate (r)events for Rotterdam only needs those ships that have visited the port, all other ships moving about on the world don’t need to be included that way.

However, VesselVoyage has outdated/incomplete information for some reasons:

* ports we haven’t mapped before in POMA are not queriable in VesselVoyage
* ports that have been updated since their original area wasn’t correct

To fix this, (r)events need to be generated to retroactively make these changes to the visits and voyages in VesselVoyage.

So, (r)events needs a way to be independent of VesselVoyage, to solve for these changes to data in POMA.

# A possible direction

Ship history is stored by MMSI and by area. To know which ships have been in an area, we need to use the history by area.

We can answer the following question:

> *Which ships were in the Maasvlakte area?*

Just looking at the history by area, we can convert a bounding box to the concrete buckets that contain the history for the Maasvlakte area:

This turns out to be performant enough, considering of course that these buckets also have all the ship history in there. So, definitely not as fast as VesselVoyage can answer a similar question. But using these buckets you’ll always get the most accurate answer, and it works anywhere in the world with any POMA data you want to throw at it.

To answer the question of which ships were in this area from 01-08-2023 to 01-09-2023 it took about a minute (running locally) and there were 3.181 ships. It sounds like this is pretty slow, but the (r)events process itself is way slower than just a minute to generate all events for a month of history for the whole of the Maasvlakte. And while (r)events is generating events for day 1, it is already preparing the required data for day 2 to be able to immediately continue when day 1 is finished. Then continuing to preload the data for day 3, etc. So having these area requests in there will definitely work and not impact the overall (r)events process or speed.

# Converting area buckets to usable interests

(R)events thinks about interests; a ship (MMSI) that is relevant and to generate events for within a specific `TimeWindow`.

Using area buckets we can also construct these interests, although they are not as granular as a specific port ATA (but they don’t need to be, since we’ll generate the more accurate ATA in the events).

By looking if MMSI A is in the first bucket of 01-08-2023, and also in the second bucket of 02-08-2023. We now can infer that this ship has been in the Maasvlakte between 01-08-2023 and 03-08-2023.

Do this for all ships for the whole month, and then you know that those 3.181 ships had a combined 6.390 entrances/exists in the area.

# Conclusion

The area buckets can be used to convert into interests. These interests can then be used by (r)events to not depend on VesselVoyage.

This could even fix an issue where ships anchor in front of a port for a very long time, since then you could use the full EOS area, and take a two-week margin around entering/exiting the EOS instead of the port.

Optionally, we could take this a step further to remove the VesselVoyage dependency fully. This means there can be no doubt about if the events are complete, if a ship was in a specific area there are events for it as well. Also the added benefit of not needing to feed the output of this initial (r)events run into VesselVoyage, to then run another (r)events process again based on this new info in VesselVoyage. This data can just be fed into VesselVoyage based on the initial run, and there is no need for a circular dependency.