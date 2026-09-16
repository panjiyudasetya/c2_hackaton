---
id: confluence:651001876
source: confluence
type: page
space: TC
title: BerthExposer
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651001876
explicit_links:
- jira:KDD-96
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651001876
---
# BerthExposer

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/651001876  

## Content

*Developer:* Chiel Broere  
*Gebruikte talen:* R, Java

## Inhoud

* [Berth Exposer](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-berth-exposer)

  + [Inhoud](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-inhoud)
  + [Inleiding](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-inleiding)
  + [Doel](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-doel)
  + [Specificaties](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-specificaties)
  + [Onderzoeks fase](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-onderzoeks-fase)

    - [dbscanalgorithm.R](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-dbscanalgorithmr)
    - [clusterlengthscript.R](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-clusterlengthscriptr)
  + [Develop fase](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-develop-fase)

    - [Tussenresultaten](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-tussenresultaten)
    - [Eindresultaat](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-eindresultaat)
  + [Project Port Mapper](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-project-port-mapper)

    - [Build .jar](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-build-jar)
  + [Restart the cluster](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-restart-the-cluster)

    - [Create DataBricks job](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-create-databricks-job)
    - [Run DataBricks job](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-run-databricks-job)
    - [Update existing jar](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-update-existing-jar)
  + [Bevindingen](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-bevindingen)

    - [Cluster algoritmes](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-cluster-algoritmes)
    - [Sub-cluster algoritmes](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-sub-cluster-algoritmes)
    - [Java 8 Stream API](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-java-8-stream-api)
    - [EPS & MinPts values in DBSCAN](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-eps-minpts-values-in-dbscan)

## Inleiding

Een schip vaart vaak van haven naar haven. Een schip komt naar een haven toe om te laden en/of te lossen. De acties die het schip uitvoert verschilt per haven, schip en opdracht. Deze ligplaatsen zijn van belang in het bestaande platform van Teqplay. Zo kan er dus herkend worden dat schepen van ligplaats naar ligplaats varen en niet zomaar op een willekeurige plaats stoppen. Ook het type ligplaats kan gevalideerd worden. Zo is het dus mogelijk om wereldwijd ligplaatsen te markeren. Dit geeft meer duidelijkheid in de data die later gebruikt kan worden in andere analyses of voorspellingen.

Teqplay verzamelt AIS-data door middel van een eigen antenne op kantoor. De data heeft een bereik over alle waterwegen in Nederland. Tijdens mijn stageperiode heb ik de toegang tot het platform van Teqplay waar ik al mijn benodigde data kan halen. In dit platform kan ik historische gegevens opvragen van alle schepen in een bepaald gebied. Tijdens de realisatie van mijn product zal ik eerst focussen op de Maasvlakte in Rotterdam. Hier is veel activiteit door schepen en dus ook veel ligplaatsen. Dit is een goede plek om te beginnen met data analyses. Het is de bedoeling om de applicatie te automatiseren zodat het zelfstandig te werk kan gaan over alle grote havens in de wereld.

Bijkomende uitdaging is om de applicatie uit te breiden om ankerplaatsen en wachtplaatsen voor bruggen en sluizen te herkennen. Deze plekken zijn geen vaste plekken voor schepen die komen laden en lossen. Als het mogelijk is om de patronen in de datasets te herkennen, dan kan ik dit uitbreiden naar wachtplaatsen en ankerplaatsen.

Het visualiseren van deze data gaat door naar bestaande applicaties van Teqplay. Teqplay heeft namelijk al verschillende applicaties zelf ontwikkeld om mijn data te laten visualiseren. Het is aan Teqplay de keuze voor welke applicatie ze gaan kiezen voor mijn data. Het is dus belangrijk dat de data die ik genereer platform onafhankelijk is.

## Doel

Berth Exposer is een hulpmiddel om infrastructuur in kaart te brengen door o.a. ligplaatsen en ankerplaatsen af te leiden van historische AIS data. Dit is gedaan met behulp van slimme algoritmes en tools.

## Specificaties

Er zijn een aantal requirements gesteld aan het programma:

* Mijn ontwikkelde programma is niet afhankelijk van platform van Teqplay
* Het programma moet zonder user input kunnen starten en resultaten uitgeven
* Het programma moet ongeacht de locatie op de wereld kunnen clusteren
* Het programma moet ligplaatsen, wachtplaatsen en ankerplaatsen detecteren
* Het programma moet op basis van de beschikbare data ligplaats dimensies berekenen
* Het programma moet berekende resultaten opslaan in een database
* Het programma moet zelfstandig werken op een Databricks instantie
* Het programma moet berekende resultaten opslaan als GeoJSON in Databricks

## Onderzoeks fase

Git: <https://bitbucket.org/teqplay/berthexposer>

---

### dbscanalgorithm.R

Voor het toepassen van het DBSCAN algoritme op de dataset is het `dbscanalgorithm.R` script geschreven. Dit script maakt gebruik van de data uit de backenddev API van Teqplay.

json.history.input <- jsonlite::fromJSON(request.content.history)
# filter the data for accurate results
json.history.input <- json.history.input[json.history.input$speedOverGround < 3, ]
json.history.filtered <- cbind.data.frame(json.history.input$mmsi,
json.history.input$location$latitude,
json.history.input$location$longitude)
colnames(json.history.filtered) <- c("mmsi", "latitude", "longitude")

De resultaten van de call zijn geformatteerd als JSON. In R is er een package beschikbaar om JSON om te zetten naar een dataframe. Het resultaat van het omzetten naar een dataframe is `json.history.filtered`.

Voor het clusteralgoritme is er gekozen voor het [DBSCAN](https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf) algoritme uit de [fpc: Flexible Procedures for Clustering package](https://cran.r-project.org/web/packages/fpc/index.html). Dit algoritme is in staat om clusters te detecteren in datasets waar de dichtheid van 2 dimensionale punten hoog is. Dit sluit aan aan de eisen van het programma.

set.seed(123)
dbscan.output <- fpc::dbscan(subset(input.filtered,
select = c("latitude",
"longitude")),
eps = 0.00030, # EPS value has to be set by the user
MinPts = 60 # MinPts value has to be set by the user

De `fpc::dbscsan(...)` functie is het DBSCAN algorithme. Het neemt als input de gegeven dataset `input.filtered`, de `eps.value` en `minpts.value`. De waarde van eps kan worden bepaald door de dataset te plotten op een [k-Nearest Neighbor Distance Plot](https://rdrr.io/cran/dbscan/man/kNNdist.html). Voor de minpts value is `sqrt(n)`, waarbij "n" het aantal datapunten zijn, een handige vuistregel.

current.time <- format(Sys.time(), "%Y\_%m\_%d\_%H\_%M")
csv.output <- cbind.data.frame(dbscan.output$cluster,
input.filtered$latitude,
input.filtered$longitude,
input.filtered$mmsi)
colnames(csv.output) <- c("cluster", "latitude", "longitude", "mmsi")
csv.ordered <- csv.output[with(csv.output, order(cluster, mmsi)), ]
write.csv(csv.ordered, file = paste(current.time, "csv", sep = "."), row.names = FALSE)

Het resultaat van het algoritme is in dezelfde volgorde als de input, dus het resultaat zal worden teruggekoppeld om te zien welk punt in welk cluster ligt. Dit wordt weggeschreven als .csv bestand voor verdere analyse.

| "cluster" | "latitude" | "longitude" | "mmsi" |
| --- | --- | --- | --- |
| 0 | 51.896045 | 4.36617 | "[211469960](https://bitbucket.org/teqplay/teqplay-wiki/commits/211469960)" |
| 0 | 51.898445 | 4.364865 | "[215825000](https://bitbucket.org/teqplay/teqplay-wiki/commits/215825000)" |
| ... | ... | ... | ... |
| 1 | 51.89485 | 4.3665 | "[241231000](https://bitbucket.org/teqplay/teqplay-wiki/commits/241231000)" |
| 1 | 51.89481 | 4. [3661433](https://bitbucket.org/teqplay/teqplay-wiki/commits/3661433) | "[565026000](https://bitbucket.org/teqplay/teqplay-wiki/commits/565026000)" |
| ... | ... | ... | ... |
| 2 | 51.89441 | 4.381385 | "[244100055](https://bitbucket.org/teqplay/teqplay-wiki/commits/244100055)" |

### clusterlengthscript.R

Voor het analyseren van de resulterende clusters is een apart script geschreven, namelijk `clusterlengthscript.R`. Het analyseer script neemt de output van het algoritme, geformatteerd in csv. Het doel hiervan is om inzicht te krijgen wat voor schepen actief zijn op gevonden clusters. De resultaten van het analyseer script heeft geen invloed op het resultaat van het algoritme.

csv.splitted <- split(csv.input, cut2(csv.input$cluster))
csv.filtered <- list()
for (i in 1:length(csv.splitted[])){
csv.filtered[[i]] <- aggregate(csv.splitted[[i]]$cluster,
by = list(mmsi = csv.splitted[[i]]$mmsi, cluster = csv.splitted[[i]]$cluster),
FUN = length) %>%
mutate(per = paste0(round(x / sum(x) \* 100, 3), "%")) %>%
ungroup
csv.filtered[[i]] <- csv.filtered[[i]][with(csv.filtered[[i]],
order(as.numeric(sub("%", "", per)) / 100,
decreasing = TRUE)), ]
}

Input `csv.splitted` wordt per cluster ingedeeld in dataframe `csv.filtered`. Voor ieder uniek ship in een cluster wordt bekerend hoevaak het schip voorkomt in het gegeven cluster. Dit is in zowel aantal hits als procentueel. Deze data kan worden gebruikt om per cluster data op te halen van elk ship dat in een cluster ligt. Zo zijn `c(request.parsed$positionOfTransponder$distanceToBow + request.parsed$positionOfTransponder$distanceToStern)` van belang om de lengte van een schip te berekenen, `request.parsed$name` om het schipnaam te bepalen, `request.parsed$role` en `request.parsed$shipType` van belang om het type schip te bepalen.

output.reduced <- do.call(rbind.fill,
lapply(csv.filtered,
data.frame,
stringsAsFactors = FALSE))
request.output <- cbind.data.frame(as.numeric(as.character(request.parsed$mmsi)),
request.parsed$name,
c(request.parsed$positionOfTransponder$distanceToBow +
request.parsed$positionOfTransponder$distanceToStern),
request.parsed$role,
request.parsed$shipType)
colnames(request.output) <- c("mmsi", "name", "length", "role", "type")
# filter out all ships with length 0 or NA
request.filternull <- request.output[request.output$length != 0
& request.output$length < 400, ]
request.filterna <- request.filternull[!is.na(request.filternull$length), ]
request.ordered <- request.filterna[with(request.filterna, order(length)), ]
merge.request <- left\_join(x = output.reduced, y = request.output, by = c("mmsi"))
merge.total <- semi\_join(x = merge.request, y = request.ordered, by = c("mmsi"))

In de laastse stap wordt er een request gedaan naar de backend van Teqplay. In `request.output` staat per schip beschreven wat de lengte is, het type schip en wat voor rol het schip heeft. Niet elk schip heeft een correcte lengte ingevuld. Dit wordt in `request.ordered` gefiltered. In de laatste stap is er een join tussen `output.reduced` en `request.ordered`. Dit resulteert in het volgende:

| "mmsi" | "cluster" | "hits" | "per" | "name" | "length" | "role" | "type" |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [245907000](https://bitbucket.org/teqplay/teqplay-wiki/commits/245907000) | 0 | 127 | "4.749%" | "TEXELBANK" | 28 | "TUG" | "TOWING" |
| [211594440](https://bitbucket.org/teqplay/teqplay-wiki/commits/211594440) | 9 | 21 | "5.983%" | "FREYJA" | 85 | "TANKERBARGE" | "TANKER" |
| [244010030](https://bitbucket.org/teqplay/teqplay-wiki/commits/244010030) | 4 | 1 | "0.243%" | "DESPERADO" | 110 | "TANKERBARGE" | "TANKER" |
| [244750137](https://bitbucket.org/teqplay/teqplay-wiki/commits/244750137) | 18 | 44 | "32.836%" | "ESCAPE" | 125 | "TANKERBARGE" | "TANKER" |
| [244130941](https://bitbucket.org/teqplay/teqplay-wiki/commits/244130941) | 0 | 8 | "0.299%" | "NAUTICTRANS" | 110 | "CARGOBARGE" | "CARGO" |

De behaalde resultaten uit deze twee scripts waren een aanleiding om de logica direct te integreren in het [platform van Teqplay](https://bitbucket.org/teqplay/platform). Door direct in verbinding te staan met het platform scheelt het een tussenstap om gegevens te verwerken naar dataframes in R. Het programma is dan afhankelijk van het platform, maar het platform is niet afhankelijk van Berth Exposer. Het is dus de bedoeling dat Berth Exposer op de achtergrond rustig aan het werk kan gaan. Dit staat beschreven in "Develop fase".

## Develop fase

*Git:* <https://bitbucket.org/teqplay/platform/branch/berthExposer>

---

De keuze om de onderzoeksfase te realiseren in het platform is een grote stap geweest. Zo is de logica van R niet 1 op 1 overplaatsbaar naar Java. Een voordeel van Java is dat er veel library's beschikbaar zijn gesteld voor diverse problemen. Het programma kan live gedeployed worden, op de achtergrond naast de live producten. Zo is het platform niet afhankelijk van Berth Exposer.

Het clusteren is in twee stappen verdeeld, namelijk: pre-clustering en clustering. Voor het pre-clusteren is er gebruik gemaakt van het k-Means algoritme. Dit algoritme zorgt ervoor dat een twee dimensionale dataset wordt veldeeld in gelijkmatige clusters. Aan de hand van het gegeven gebied en gewenste cluster grootte kan het algoritme dit verdelen in clusters. Dit staat ook in [bevindingen](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-bevindingen) beschreven.

De realisatie van de [DBSCAN algoritme](http://commons.apache.org/proper/commons-math/javadocs/api-3.6.1/index.html) is mogelijk gemaakt door de [Apache Commons Mathematics Library](http://commons.apache.org/proper/commons-math/). De implementatie van het DBSCAN algoritme sluit goed aan op de beschikbare data die uit het platform te verkrijgen is. Ook voor het k-Means algoritme is gebruik gemaakt van Commons Math.

---

Het programma maakt gebruik van een eigen configuratie. In deze configuratie kan het gedrag van de algoritmes worden ingesteld. Zo kan je dus handmatig instellen welk gebied je wil analyseren en hoe de algoritmes dit moeten aanpakken. Dit stel je in in de `berthexposer.conf`.

berthExposerConfig {
# setters for both deriveHarbourBerths & deriveIteratedHarbourBerths
# timestamp in ms
from = 1512082800000
# timestamp in ms
to = 1512601200000
# speed in km/h
speedOverGround = 2.0
# DBSCAN eps value, usually set to (meters / 10 0000)
eps = 0.00020
# Mininal Points multiplier value, set this value to detect more or less clusters
minPtsMultiplier = 1.0
# Maximum Area value for K-Means algorithm, usually set to (km^2 / 1000)
maxArea = 0.0008
# setters only for deriveIteratedHarbourBerths
iterations = 1
daysPerIteration = 1
# kml output path
kmlOutputPath = "/Users/chielbroere/Documents/teqplay/portmapper/"
# shiptraces for each calculated harbour
shiptraces = false
backendUrl = "http://backenddev.teqplay.nl"
username = ""
password = ""
}
enabledPorts = [
"Port of Rotterdam"
]

De timestamps `from` en `to` gegeven aan wat de periode moet zijn om te laten clusteren.  
Voor het filteren van schepen die onder een bepaalde snelheid varen wordt er gebruik gemaakt van de `speedOverGround` waarde.  
Het gegrag van het DBSCAN algoritme is ook aan te passen (zie ook [bevindingen](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-bevindingen)) met `eps` en `minPtsMultiplier`.  
De `maxArea` waarde is verbonden aan het k-means algoritme (zie ook [bevindingen](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-bevindingen)).  
Om meerdere keren over een bepaald gebied te itereren kan je gebruik maken van `daysPerIteration`. Hierin geef je aan in aantal dagen hoevaak je wil itereren over een gebied.  
Voor het wegschrijven van de resultaten (in KML of JSON) maak je gebruik van de `kmlOutputPath` die aangeeft wat het pad is waar het programma naartoe moet schrijven.  
De `shiptraces` kan worden gebruikt om voor kleine gebieden per schip te zien wat de shiptrace was in de timewindow `from` naar `to`.  
Voor het verkrijgen van de data maakt het programma gebruik van de Teqplay backenddev API. Hierin moet je inloggen met je eigen credentials.  
Als laatst kan je het programma de `enabledPort` meegeven om aan te geven dat je meer gebieden wil clusteren dan een.

private void setup() {
from = berthExposerConf.getLong(ConfigSettings.BERTHEXPOSER\_FROM);
to = berthExposerConf.getLong(ConfigSettings.BERTHEXPOSER\_TO);
timeWindow = new TimeWindow(from, to);
speedOverGround = berthExposerConf.getNumber(ConfigSettings.BERTHEXPOSER\_SPEEDOVERGROUND).floatValue();
eps = berthExposerConf.getDouble(ConfigSettings.BERTHEXPOSER\_EPS);
minPtsMultiplier = berthExposerConf.getDouble(ConfigSettings.BERTHEXPOSER\_MINPTSMULTIPLIER);
maxArea = berthExposerConf.getDouble(ConfigSettings.BERTHEXPOSER\_MAXAREA);
iterations = berthExposerConf.getInt(ConfigSettings.BERTHEXPOSER\_ITERATIONS);
daysPerIteration = berthExposerConf.getInt(ConfigSettings.BERTHEXPOSER\_DAYSPERITERATION);
kmlOutputPath = berthExposerConf.getString(ConfigSettings.BERTHEXPOSER\_KMLOUTPUTPATH);
shiptraces = berthExposerConf.getBoolean(ConfigSettings.BERTHEXPOSER\_SHIPTRACES);
if (!berthExposerConf.getStringList("enabledPorts").isEmpty()) {
enabledPorts.addAll(berthExposerConf.getStringList("enabledPorts"));
}
backendUrl = berthExposerConf.getString(ConfigSettings.BERTHEXPOSER\_BACKENDURL);
service = ServiceGenerator.createService(backendUrl, null, BerthExposerService.class, null,
new BerthExposerInterceptor());
}

In de functie `setup()` leest het programma de `berthexposer.conf` waaruit de gewenste instellingen worden gehaald. Alle functies die gebruikt worden maken gebruik van de waardes die zijn ingesteld door de gebruiker. Als dit niet is gedaan dan kan het programma ook niet starten.

---

Na het instellen van alle variabelen kan je kiezen uit twee functies de het programma start, namelijk `deriveHarbourBerths()` en `deriveIteratedHarbourBerths()`. Het verschil hier is dat de `Iterated` deel meerdere keren herhaalt over een bepaald gebied. In dit voorbeeld neem ik `deriveHarbourBerths()`.

/\*\*
\* Public method to retrieve clusters in a area where there is an high amount of moored ships activities
\*/
public static List<List<CalculatedBerth>> deriveHarbourBerths() {
LOG.log(Level.INFO, "Starting BerthExposer on {0} ports", enabledPorts.size());
return areaList.stream()
.map(port -> BerthExposerUtil.getHistory(service, timeWindow, port, speedOverGround)) // retrieve history for entire input polygon
.peek(log -> LOG.log(Level.INFO, "Amount of points confirming the filter: {0}", log.size()))
.map(BerthExposer::getKmeansClusterResults) // divide the input polygon into sub polygons with K-means algorithm
.peek(log -> LOG.log(Level.INFO, "Pre-clustering divided area in {0} subclusters", log.getCalculatedBasin().size()))
.map(BerthExposer::getDbscanClusters) // analyse all sub polygons for clusters with DBSCAN algorithm
.map(dbscanClusters -> convertClustersToPolygons(dbscanClusters, timeWindow)) // convert all clusters to calculated berths
.collect(toList());
}

`deriveHarbourBerths()` is de methode die alle functies aanroept om in een keer te clusteren.  
Per gebied wordt er eerst historische data opgehaald met de functie `getHistory()`.  
Na het ophalen van de data wordt de data bewerkt in de `getKmeansClusterResults()` en de `getDbscanClusters()` functies.  
Als laatst worden de clusters geanalyseerd en per cluster de dimensies berekend.

De keuze om gebruik te maken van Java 8 Stream API staat beschreven in [bevindingen](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-bevindingen).

De eerste stap die wordt gedaan is het ophalen van de data in het vooringesteld gebied:

/\*\*
\* Method to retrieve all history points in a given area
\* @param berthExposerService the BerthExposerService
\* @param timeWindow the given timewindow in ms
\* @param polygon the given area selected by user
\* @param speedOverGround the speed condition
\*/
public static Set<HistoricShipInfo> getHistory(BerthExposerService berthExposerService, TimeWindow timeWindow, nl.teqplay.platform.model.Location[] polygon, Float speedOverGround) {
// Stream platform data to a List<Location>. This step includes filter all ships with a specific speed.
Set<HistoricShipInfo> historicShipInfoSet = berthExposerService.getHistoricalVesselsInPolygon(timeWindow.getFrom(), timeWindow.getTo(), polygon, 2000L, null, 10000000L).stream()
.filter(l -> l.getSpeedOverGround() != null && l.getSpeedOverGround() < speedOverGround)
.collect(Collectors.toSet());
checkForCorrectReturn(historicShipInfoSet, timeWindow.getFrom(), timeWindow.getTo());
return historicShipInfoSet;
}

Hier wordt aangegeven door de `berthExposerService` waar de data vandaan komt, de `timeWindow` geeft de tijdsperiode aan, `polygon` is het gebied waar de analyse wordt toegepast en `speedOverGround` is de filter voor schepen die langzamer voeren dan een bepaalde snelheid.

private static void checkForCorrectReturn(Set<HistoricShipInfo> historicShipInfo, Long from, Long to) {
Long minTimestamp = historicShipInfo.stream()
.map(HistoricShipInfo::getTimeLastUpdate)
.collect(toSet()).stream().min(Long::compare).get();
Long maxTimestamp = historicShipInfo.stream()
.map(HistoricShipInfo::getTimeLastUpdate)
.collect(toSet()).stream().max(Long::compare).get();
Long minDiff = (from - minTimestamp) / -1;
Long maxDiff = to- maxTimestamp;
if (minDiff > 86400000L || maxDiff > 86400000L) {
LOG.log(Level.SEVERE, "The API request does not return the same timewindow, @limit too low? ");
System.exit(1);
}
}

Ook wordt de data gechecked door de functie `checkForCorrectReturn()`. Deze functie vergelijkt de timestamp `from` en `to` met de timestamps van de dataset. Als de timestamps niet met elkaar overeen komen wordt het programma afgesloten met een error.

---

/\*\*
\* Method to calculate sub-clusters with K-means algorithm
\*
\* @param portHistory the input polygon covering the whole area
\*/
protected static CalculatedBasin getKmeansClusterResults(Set<HistoricShipInfo> portHistory) {
Set<Location> locationsFromHistory = BerthExposerUtil.getLocationsFromHistory(portHistory);
Geometry polygon = LocationConversionUtils.createConvexHull(locationsFromHistory);
assert polygon != null;
Double area = polygon.getArea();
Double k = area / maxArea;
Set<DoublePoint> collect = locationsFromHistory.stream()
.map(location -> new DoublePoint(new double[]{location.getLatitude(), location.getLongitude()}))
.collect(toSet());
// Check if the area is bigger or smaller then the max area.
if (k < 1.0D) {
Set<CentroidCluster<DoublePoint>> centroidClusters = new HashSet<>();
CentroidCluster<DoublePoint> centroidCluster = new CentroidCluster<>(collect.iterator().next());
collect.forEach(centroidCluster::addPoint);
centroidClusters.add(centroidCluster);
return new CalculatedBasin(portHistory, null, centroidClusters);
} else {
KMeansPlusPlusClusterer<DoublePoint> kMeansClusterer = new KMeansPlusPlusClusterer<>((int) Math.ceil(k), 100, new EuclideanDistance(), new MersenneTwister());
return new CalculatedBasin(portHistory, null, new HashSet<>(kMeansClusterer.cluster(collect)));
}
}

`getKmeansClusterResults(...)` is het k-means algoritme die in staat is om grote gebieden te verkleinen in gebieden van `maxArea` km^2. Het resultaat hiervan wordt geplaatst in de `CalculatedBasin` model. Dit model bevat de mogelijkheid om de verdeelde gebieden apart van elkaar op te slaan.

Het voordeel van het sub-clusteren staat beschreven in [bevindingen](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-bevindingen)

---

/\*\*
\* DBSCAN algorithm clustering points with high density.
\*
\* @param kMeansClusters input list of location history
\*/
protected static CalculatedSubBerth getDbscanClusters(CalculatedBasin kMeansClusters) {
// This method will take the most time because this is the actual clustering algorithm
Set<List<Location[]>> dbscanResult = new HashSet<>();
int i = 1;
// Calculate the minimal points value based on the time
for (CentroidCluster<DoublePoint> cluster : kMeansClusters.getCalculatedBasin()) {
int size = cluster.getPoints().size();
int minPtsValue = (int) Math.ceil(Math.sqrt(size) \* minPtsMultiplier);
LOG.log(Level.INFO, "Clustering basin {0} out of {1} basins", new Object[]{i, kMeansClusters.getCalculatedBasin().size()});
i++;
DBSCANClusterer<DoublePoint> dbscanAlgorithm = new DBSCANClusterer<>(eps, minPtsValue);
Set<Cluster<DoublePoint>> dbscanCluster = dbscanAlgorithm.cluster(cluster.getPoints()).stream()
.filter(a -> a.getPoints().size() > minPtsValue)
.collect(toSet());
List<Location[]> locations = BerthExposerUtil.clusterToLocationArray(dbscanCluster);
dbscanResult.add(locations);
}
return new CalculatedSubBerth(kMeansClusters, dbscanResult, timeWindow);
}

`getDbscanClusters(...)` is de kern van Berth Exposer. De DBSCAN algoritme is gebaseerd op de [paper](http://www.dbs.ifi.lmu.de/Publikationen/Papers/KDD-96.final.frame.pdf) die DBSCAN beschrijft. Het neemt als input `history` de clusters die uit `getKmeansClusterResults(...)` komen. De parameter `eps` is de maximale radius van de nabije omgeving. Het kiezen en vaststellen van deze value staat beschreven in [bevindingen](https://bitbucket.org/teqplay/teqplay-wiki/wiki/Berth%20Exposer#markdown-header-bevindingen). Ook staat er beschreven wat de doorslag was voor het nemen van de `minPtsValue` value. De output van het algoritme geeft per sub-cluster aan hoeveel en welke punten een cluster vormen.  
De resultaten worden opgeslagen in het `CalculatedSubBerth` model. In dit model worden de k-means cluster gebieden, de berekende DBSCAN clusters en de timewindow opgeslagen.

---

/\*\*
\* Method to convert a list of cluster with DoublePoint to resulting Polygon combining multiple methods
\*
\* @param inputClusters the input clusters with DoublePoint positions with all speed < x
\* @param timeWindows the defined timewindow for calculating heading for each berth
\*/
protected static List<CalculatedBerth> convertClustersToPolygons(CalculatedSubBerth inputClusters, TimeWindow timeWindows) {
Set<List<Location[]>> clusters2 = inputClusters.getCalculatedSubBerth();
Set<HistoricShipInfo> locationsInBasin = inputClusters.getCalculatedBasins().getLocationsInBasin();
// List of the resulting polygons in each cluster
List<CalculatedBerth> calculatedBerths = new ArrayList<>();
Location[] harbourArea = areaList.get(0);
Map<String, Location> mmsiMapHarbour = BerthExposerUtil.getMmsiMapForHarbour(service, timeWindows, harbourArea, speedOverGround);
Set<ShipInfo> shipInfoSetHarbour = BerthExposerUtil.readMultipleShipInfoForSinglePolygon(service, mmsiMapHarbour);
if (shiptraces) {
Map<String, List<HistoricShipInfo>> mmsiSet = BerthExposerUtil.getMmsiSet(service, timeWindows, harbourArea, speedOverGround);
BerthExposerUtil.writeShipTraceToKml(mmsiSet, kmlOutputPath, enabledPorts.get(0));
}
for (List<Location[]> aClusters2 : clusters2) {
LOG.log(Level.INFO, "I start now!! -----------------------");
Set<CalculatedBerth> calculatedBerthList = new HashSet<>();
for (Location[] polygon : aClusters2) {
if (polygon != null && timeWindows.getFrom() != null && timeWindows.getTo() != null && speedOverGround != null) {
List<Integer> polygonHeadings = BerthExposerUtil.getHeadings(locationsInBasin, polygon);
if (!polygonHeadings.isEmpty()) {
Map<String, Location> mmsiMap = BerthExposerUtil.getMmsiMap(locationsInBasin, polygon);
Set<ShipInfo> shipInfoSet = shipInfoSetHarbour.stream().filter(a -> mmsiMap.containsKey(a.getMmsi())).collect(toSet());
calculatedBerthList.add(getCalculatedBerth(shipInfoSet, mmsiMap, polygonHeadings, inputClusters, timeWindows));
} else {
calculatedBerthList.add(new CalculatedBerth(inputClusters, timeWindows, BerthExposerUtil.getConvexHull(Arrays.asList(polygon)), null, null, null, null, null));
}
} else {
LOG.log(Level.SEVERE, "Location to berth calculation failed");
}
}
LOG.log(Level.INFO, "I'm finished!! -----------------------");
Set<Geometry> polygonList = new HashSet<>();
for (CalculatedBerth calculatedBerth : calculatedBerthList) {
if (calculatedBerth != null && calculatedBerth.getPolygon() != null) {
polygonList.add(calculatedBerth.getPolygon());
}
}
Set<Geometry> filteredPolygons = BerthExposerUtil.filterCrossingPolygonsSet(polygonList);
for (Geometry polygon : filteredPolygons) {
calculatedBerths.add(new CalculatedBerth(inputClusters, timeWindows, polygon, null, null, null, null, null));
}
}
return calculatedBerths;
}

In `convertClustersToPolygons(CalculatedSubBerth inputClusters, TimeWindow timeWindows)` berekent het programma de clusters die zijn gedetecteerd in stap 3. Per cluster wordt er berekend welk schip in de ingestelde tijd `timeWindows` zijn geweest. Als elk schip is verzameld kan ik met de historische data de dimensies berekenen van het cluster:

/\*\*
\* Method to convert a location point to ship location dimensions
\*
\* @param shipInfoInput containing all ships in input polygon
\* @param historicShipInfoSet containing mmsi and location
\* @param headingList the list of all fetched headings in a cluster area
\* @param calculatedSubBerth the calculated sub berths from the algorithm
\* @param timeWindow the input timewindow, the same as the algorithm timewindow
\*/
public static CalculatedBerth getCalculatedBerth(Set<ShipInfo> shipInfoInput, Map<String, Location> historicShipInfoSet, List<Integer> headingList, CalculatedSubBerth calculatedSubBerth, TimeWindow timeWindow) {
Map<String, ShipInfo> shipInfoMap = BerthExposerUtil.getIdenticalShipsInSet(shipInfoInput, historicShipInfoSet);
double[] mostOccurringHeadings;
Geometry polygon;
if (headingList != null) {
mostOccurringHeadings = BerthExposerUtil.getMostOccurringHeadings(headingList);
List<Map<String, List<Integer>>> sortedHeadings = BerthExposerUtil.getHeadingDistribution(headingList);
List<List<Double>> sortedHeadingsAsList = BerthExposerUtil.getHeadingsAsList(headingList, sortedHeadings);
Double heading1 = mostOccurringHeadings[0];
List<Location> clusterDimensions;
if (heading1 == 0.0D) {
return null;
}
clusterDimensions = BerthExposerUtil.getClusterDimensions(historicShipInfoSet, shipInfoMap, mostOccurringHeadings[0], null);
if (clusterDimensions.size() < 6) {
return null;
}
polygon = BerthExposerUtil.getConvexHull(clusterDimensions);
if (polygon == null) {
return null;
}
} else {
List<Location> locationSet = historicShipInfoSet.entrySet().stream().map(Map.Entry::getValue).collect(toList());
polygon = BerthExposerUtil.getConvexHull(locationSet);
mostOccurringHeadings = new double[]{511D};
}
Set<Map<ShipInfo.ShipType, SubBerthSpecifications>> perShipDetails = BerthExposerUtil.getPerTypeDetails(shipInfoMap);
Double averageLength = shipInfoMap.entrySet().stream().map(Map.Entry::getValue)
.filter(ship -> ship.getLength() != 0)
.collect(Collectors.averagingDouble(ShipInfo::getLength));
Double averageWidth = shipInfoMap.entrySet().stream().map(Map.Entry::getValue)
.filter(ship -> ship.getWidth() != 0)
.collect(Collectors.averagingDouble(ShipInfo::getWidth));
Integer totalAmountOfShips = historicShipInfoSet.size();
return new CalculatedBerth(calculatedSubBerth, timeWindow, polygon, averageLength, averageWidth, mostOccurringHeadings, perShipDetails, totalAmountOfShips);
}

De functie `getCalculatedBerth(...)` is de functie die meerdere methodes aanroept om per cluster te kunnen berkenen wat de dimensies zijn van het gevonden cluster. Ook wordt er extra informatie gegenereerd zoals gemiddelde lengte + breedte en totaal aantal schepen in het cluster. De berekende ligplaatsen worden opgeslagen in het `CalculatedBerth` model. Dit model bevat zowel de polygoon als details van de ligplaats die berekend is.

/\*\*
\* Method to calculate the ship lengths in the given cluster
\*
\* @param historicShipInfoSet Set containing all retrieved HistoricShipInfo in a cluster
\* @param shipInfoMap Map containing all individual ships in the input cluster
\* @param heading1 The most occurring heading for all ships in a cluster
\* @param heading2 The most occurring heading 180 degrees turned
\*/
public static List<nl.teqplay.platform.model.Location> getClusterDimensions(Map<String, nl.teqplay.platform.model.Location> historicShipInfoSet, Map<String, ShipInfo> shipInfoMap, Double heading1, Double heading2) {
List<nl.teqplay.platform.model.Location> clusterDimensions = new ArrayList<>();
if (heading2 == null) {
for (Map.Entry<String, nl.teqplay.platform.model.Location> shipInfo : historicShipInfoSet.entrySet()) {
clusterDimensions.add(ShipLocationUtils.getBowLocation(shipInfoMap.get(shipInfo.getKey()), shipInfo.getValue(), heading1));
clusterDimensions.add(ShipLocationUtils.getSternLocation(shipInfoMap.get(shipInfo.getKey()), shipInfo.getValue(), heading1));
}
} else {
for (Map.Entry<String, nl.teqplay.platform.model.Location> shipInfo : historicShipInfoSet.entrySet()) {
clusterDimensions.add(ShipLocationUtils.getBowLocation(shipInfoMap.get(shipInfo.getKey()), shipInfo.getValue(), heading1));
clusterDimensions.add(ShipLocationUtils.getBowLocation(shipInfoMap.get(shipInfo.getKey()), shipInfo.getValue(), heading2));
clusterDimensions.add(ShipLocationUtils.getSternLocation(shipInfoMap.get(shipInfo.getKey()), shipInfo.getValue(), heading1));
clusterDimensions.add(ShipLocationUtils.getSternLocation(shipInfoMap.get(shipInfo.getKey()), shipInfo.getValue(), heading2));
}
}
return clusterDimensions;
}

Voor het berkenen van de lengte en breedte van een ligplaats berekend de functie `getClusterDimensions(...)` per schip de locatie van de stevens (voor- en achterkant van de scheepsromp). Omdat het programma aanneemt dat elk schip dat in het cluster voorkomt ook daadwerkelijk heeft stilgelegen op de gevonden locatie, kan het programma voor elk schip de locatie van het schip berekenen op het cluster. Het resultaat is dat er per cluster een realistisch beeld wordt weergeven over hoe de schepen in het cluster langs een ligplaats stil hebben gelegen.

/\*\*
\* Method to convert a list of list with Location to Polygon
\*
\* @param input the input Location from clusterToLocationArray method
\*/
public static Geometry getConvexHull(List<nl.teqplay.platform.model.Location> input) {
// First this will calculate the convex hull of each cluster, and calculate the smallest surrounding rectangle
// and at last filter all duplicate values
if (input.size() > 2) {
Geometry convexHull = LocationConversionUtils.createConvexHull(input);
Polygon smallestSurroundingRectangle = getSmallestSurroundingRectangle(convexHull);
if (smallestSurroundingRectangle != null) {
return smallestSurroundingRectangle;
}
}
return null;
}

`getConvexHull()` is een methode om van een lijst met locaties de omtrek te berekenen. De uitkomst van de functie is een polygoon die alle locaties in de lijst vertegenwoordigd. De omtrek van de polygoon is namelijk gelijk aan de lengtes van de schepen die in het cluster voorkomen.  
Omdat ligplaatsen (bijna) altijd als een vierhoek worden weergeven, wordt in de functie `getSmallestSurroundingRectangle()` van elke polygoon de vierhoekige omtrek berekend.

### Tussenresultaten

Als voorbeeld is een stuk van de botlek gekozen om te clusteren.

Als eerst is er geprobeerd om te kijken of het mogelijk is om per cluster de dimensies van de schepen te tekenen. Hierbij was er nog geen juiste methode gevonden om de richting van de schepen te berekenen. Je kan zien dat als je de clusters zou draaien dat de lengtes zouden kloppen met de werkelijkheid.

Hierna is geprobeerd om per cluster te richting van de schepen te berkenen. Hierbij wordt er per cluster berekend wat de meest voorkomende richting is. Deze richting wordt gebruikt voor elk schip dat in het cluster voorkomt, zodat er geen schepen op een verkeerde richting uitsteken.

De clusters hadden wel een correcte richting mee, maar voor het oog waren dit nog geen mooie ligplaatsen op de kaart. Per cluster werd er bereken wat de omtrek moest zijn. De vierhoek die wordt getekend is nog niet gematched met de richting van het cluster.

Als laatst werd er rekening gehouden met de omtrek van de ligplaatsen met een juiste richting. Hier kan je goed zien dat de ligplaatsen nu beter geplaats zijn op de kaart. Deze ligplaatsen worden dan ook gebruikt voor het eindresultaat die de gebruiker kan zien.

### Eindresultaat

De haven van Rotterdam is de grootste van Europa. In 2017 zijn er [meer dan 29 duizend schepen in Rotterdam geweest](http://bit.ly/2mtl4Ru). Door de diversiteit van zeeschepen en binnenvaartschepen is deze haven een bijzondere haven. Dit zorgt ervoor dat niet alle ligplaatsen in de havens gelijk zijn. Voor dit project bleek dit ook een lastige uitdaging. Het resultaat hiervan is wel naar wens. De grotere havens waar voornamelijk zeeschepen komen zijn makkelijk te detecteren, mede dankzij de accurate AIS data van deze schepen. Voor de kleinere havens blijkt dit wat moeilijker. Voor binnenvaartschepen geldt dat de AIS transponder niet van gelijke specificaties moet als dat van zeeschepen. Zo zijn er veel binnenvaartschepen zonder elektrisch kompas. Dit vormt voor dit project wel een probleem, want het project is afhankelijk van de data die schepen leveren. Als er geen data beschikbaar is over de richting van een schip dan kan er geen richting worden bepaald voor het cluster. Door heel veel data te gebruiken is dit probleem minder zichtbaar.

De haven van Antwerpen is na Rotterdam de grootste van Europa. Deze haven heeft net als Rotterdam een grote diversiteit van zeeschepen en binnenvaartschepen. Er zijn een paar dokken in Antwerpen waarbij heel veel schepen op een dag komen. Deze dokken zijn heel goed te zien op de resultaten van het clusteren. De problemen die in Rotterdam voordoen zijn ook zichtbaar in Antwerpen. Ook in Antwerpen is het op sommige dokken lastig om juiste resultaten te verkrijgen. Door veel data en vaak te clusteren is dit probleem een stuk minder.

De haven van Singapore is na Shanghai de groote haven ter wereld. In deze haven komen vooral zeeschepen in en uit. Veel schepen liggen voor anker voor de kust van Singapore. Dit soort activiteiten zijn anders dan stil liggende schepen langs een kade. Als een schip voor anker ligt dan is het schip altijd in beweging. Dit is goed te zien op de resultaten van het programma. Er is namelijk veel anker activiteit te zien voor de kust van Singapore. Deze plaatsen worden wel apart van elkaar berekend als ligplaatsen, omdat het programma niet kan bepalen of het schip langs kade ligt of voor anker.

## Project Port Mapper

Aan het begin van 2018 heeft Teqplay in samen werking met Havenbedrijf Rotterdam een nieuw project opgestart. Het team van Teqplay heeft besloten om mijn project te gebruiken als start voor “Port Mapper”. Het was aan mij de taak om het gerealiseerd deel los te koppelen van het Teqplay platform en dit als nieuw project te starten op Port Mapper. Het losstaande project kan worden gebruikt om in de online tool Databricks te laten draaien. Samen met Jos heb ik er voor gezorgd dat mijn project online staat in Databricks en ten alle tijden gebruikt kan worden om grote hoeveelheden data te clusteren.

De resultaten van het clusteren wordt getoond op de applicatie Port Mapper. Het team van Teqplay heeft een applicatie gerealiseerd dat bouwt op de resultaten van Databricks. Zo kan je elk resultaat individueel inzien en aanpassen indien gewenst.

Voor dit project heb is er ook een `README.md` geschreven specifiek gericht op het gebruik van dit programma in Databricks:

### Build .jar

To build this project with dependecies included, use `build_jar.sh` script.

sh ./build\_jar.sh
> IMPORTANT: The result of this script should always start the .jar file with --help. If this is not the case, manually check if the .jar file is build correctly and manually start the script with `java -cp target/berthexposer-1.0.jar nl.teqplay.datascience.berthexposer.BerthExposer -h`

usage: BerthExposer [-d <arg>] [-e <arg>] [-f <arg>] [-h] [-i <arg>] [-ma <arg>]
[-mp <arg>] [-o <arg>] [-p <arg>] [-s <arg>] [-t <arg>] [-v]
-d,--days-per-iteration <arg> Amount of days per iteration if iterated
-e,--eps <arg> The EPS value for DBSCAN algorithm
-f,--from <arg> First timestamp to cluster from in ms
-h,--help Help interface
-i,--iterations <arg> Amount of iterations if iterated
-ma,--max-area <arg> The maximum pre-cluster area
-mp,--multp <arg> Multiplier for pre-clustering sensitivity
-o,--output-path <arg> The path to write output file to
-p,--port <arg> The port to cluster
-s,--speed-over-ground <arg> The speed over ground filter value
-t,--to <arg> Last timestamp to cluster to in ms
-v,--version Print the current version of BerthExposer
```
### Upload .jar
To upload the compiled .jar file, the `upload\_jar.sh` script will handle this automatically
```bash
sh ./upload\_jar.sh username key
e.g. -> sh /upload\_jar.sh user@mail.com 12345
> Important: `key` must be the api key, not the encoded base64 key

Depending on your uploadspeed, the response should be:

{}

## Restart the cluster

After uploading a new jar, it is necessary to restart the cluster(s) before the new version of the jar is applied.

Restarting the cluster can be done via the DataBricks GUI, or using the REST API:

POST {{url}}/api/2.0/clusters/restart
{
"cluster\_id": "0116-105435-gelid3"
}

Where `{{url}}` is your databricks url, for example `https://dbc-a9cf60ca-e5a5.cloud.databricks.com`

You will have to pass an Authorization header containing a base-64 encoded auth with your username and databricks token.

To check the status of a cluster (restarting), check the "state" field in the following response (for example `"RESTARTING"` or `"RUNNING"`):

GET {{url}}/api/2.0/clusters/get?cluster\_id=0116-105435-gelid3

### Create DataBricks job

A DataBrick job allows (amongst others) to run a `main` function from a jar.

> The job for one specific jar has to be created only once, no changes are needed after the jar is replaced with a newer version.

POST {{url}}/api/2.0/jobs/create
{
"name": "berthexposer rotterdam",
"existing\_cluster\_id": "0116-105435-gelid3",
"libraries": [
{
"jar": "dbfs:/FileStore/job-jars/berthexposer.jar"
}
],
"timeout\_seconds": 3600,
"max\_retries": 1,
"spark\_jar\_task": {
"main\_class\_name": "nl.teqplay.datascience.berthexposer.BerthExposer",
"parameters": [
"-o", "/dbfs/mnt/portmapper/berthexposer/rotterdam/",
"--from", "1509490800000",
"--to", "1510009200000",
"--port", "Port of Rotterdam"
]
}
}

This request returns a job id like:

{
"job\_id": 5
}
> Note that you can find the id of a cluster (or job) easily via the DataBricks UI: view the cluster in Databricks, then you can see the id in the url.

### Run DataBricks job

Now, the job can be executed immediately (it can also be scheduled), via the DataBricks GUI or using the REST API.

POST {{url}}/api/2.0/jobs/run-now
{
"job\_id": 5,
"jar\_params": []
}
> A job can only run when the configured cluster is actually running. So make sure the cluster is up and running before starting a job.

### Update existing jar

In short, the following steps (explained before) need to be repeated:

* Build jar
* Upload jar to DBFS
* Restart cluster
* Run (existing) job

## Bevindingen

Tijdens de onderzoeksfase heb ik verschillende onderwerpen onderzocht:

### Cluster algoritmes

* [DBSCAN](http://www.dbs.ifi.lmu.de/Publikationen/Papers/KDD-96.final.frame.pdf)
* [OPTICS](http://www.dbs.ifi.lmu.de/Publikationen/Papers/OPTICS.pdf)

DBSCAN staat voor Density-Based Spatial Clustering of Applications with Noise. Dit algoritme is in staat clusters met hoge dichtheid te detecteren. Een voordeel van dit algoritme is dat als de dataset en input values gelijk blijven, dat de resultaten altijd hetzelfde zijn. Dit algoritme is dus zeer consistent.

OPTICS staat voor Ordering Points To Identify the Clustering Structure. Dit algoritme is op de basis van DBSCAN gebaseerd. Het verschil met DBSCAN is dat EPS niet meer handmatig bepaald wordt, maar automatisch op basis van een reachability-plot. Per cluster wordt bepaald wat de optimale EPS value moet zijn. Een nadeel van deze techniek is dat het algoritme zelf bepaald wat een value moet zijn, en kan dus mogelijk te veel noise oppakken. Dit maakt het algoritme niet consistent en dus minder betrouwbaar.

### Sub-cluster algoritmes

* [K-means](http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf)
* [Neural Network - Self-Organizing Maps](http://www.shy.am/wp-content/uploads/2009/01/kohonen-self-organizing-maps-shyam-guthikonda.pdf)

K-means algoritme verdeelt een dataset in meerdere clusters door de afstand van elk punt in een cluster zo laag mogelijk te houden vanaf een random center punt.

Self-Organizing Maps is een vorm van een Neuraal Netwerk, gebaseerd op de [Kohonen Map](http://ieeexplore.ieee.org/document/58325/). Het netwerk is in staat om een dataset te verdelen in gelijkmatige stukken. Het opzetten en trainen van een Neuraal Netwerk kost veel tijd, en is daarom niet de beste oplossing om snel een dataset te verdelen in sub-clusters.

### Java 8 Stream API

Java 8 bevat een `stream()` [functie](http://www.oracle.com/technetwork/articles/java/ma14-java-se-8-streams-2177646.html). Deze functie zorgt ervoor om snel en effecties queries uit te voeren op datasets. Omdat Berth Exposer veel data moet verwerken, is het gebruik van queries een stuk overzichtelijker in gebruik. Voor het mappen, fliteren en collecten van data is het goed te gebruiken voor conversies. Een `List<Location>` kan dan eenvoudig gemapped worden naar `Location[]` en andersom.

### EPS & MinPts values in DBSCAN

Het DBSCAN algoritme neemt twee values als input, namelijk `EPS` en `MinPts`. Voor beide geldt dat als een van de values van waarde veranderd, dat de uitkomst ook anders kan zijn voor de gehele dataset.

De `EPS` value kan zowel vast als dynamisch worden gebruikt. In het geval van Berth Exposer is er gekozen voor een vaste EPS value. Dit heeft te maken met de consistentie van de uitkomsten. Doordat de coordinaten van transponderlocaties worden gebruikt om te clusteren, krijg je op deze plekken een hoge dichtheid van punten, waardoor het voor het algoritme niet nodig is om een groot bereik te nemen, maar een dynamisch `MinPts` value op basis van de beschikbare data.

`MinPts` heeft net als `EPS` veel effect op het resultaat van het DBSCAN algoritme. Door te kiezen voor een lage waarde, is het mogelijk dat het cluster algoritme te veel "noise" oppakt. Door te kiezen voor een variabele `MinPts` waarde, is het algoritme flexibeler op plaatsen waar er heel veel activiteit is en waar weinig activiteit is. Door veel te proberen en te valideren is de `MinPts` waarde te berekenen door de simpele formule: `sqrt(n) * minPtsMultiplier`. Een multiplier van 1.0 heeft vaak goede resultaten, maar kan ten alle tijden gevoeliger of minder gevoelig worden ingesteld.