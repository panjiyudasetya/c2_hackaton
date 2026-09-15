---
id: confluence:88702977
source: confluence
type: page
space: TC
title: RouteScout refactor
author: Former user (Deleted)
date: '2022-04-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/88702977
explicit_links: []
---
# RouteScout refactor

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/88702977  

## Content

TLDR; use polygons for removing complex “spider” routes & for more flexible routing

Considerations:

* gradual conversion from current route/line network, to include polygons
* straight line from A to B according to polygon (shortest route approach)
* creating a more centered/averaged out line from A to B within the polygon (route in the middle approach)
* add ability to tell RouteScout to route to `SGSIN` (and passing the desired coordinates?), for Singapore the route might stop at a different points when entering from the left or right, so remove the polygon of the port to cut-off any excess route
* expose sailing direction of ship to RouteScout
* support one-way routes

Use JTS polygon triangulation? <https://www.osgeo.org/wp-content/uploads/State-of-JTS-2017.pdf>

## Polygons covering approach routes

### Rotterdam + Amsterdam

### Singapore

### Göteborg

### Haypoint

## Polygons covering different seas

### Mediterranean Sea

### Caribbean Sea

### Santos

## Routing scenarios

### Rotterdam + Amsterdam

### Göteborg

### Singapore

## Algorithm examples