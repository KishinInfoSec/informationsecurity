---
title: twitter-geolocation
tags: [reconnaissance, passive-recon, osint, type/cheatsheet, phase/recon]
---

# Twitter Geolocation

## Twitter Geolocation

### Filter Tweet by Geographical Metadata

```
# Search String
geocode:-23.555488,-46.600370,10km url:wa.me “Gravidez”
```

* **geocode** = geolocation
* **radius** = determine a radius based on the region
* **url** = determine possible URL’s with this limitation

### Other Options

```
    geocode:-23.555488,-46.600370,10km url:wa.me filter:media
    geocode:-23.555488,-46.600370,20km url:wa.me “Drogas”
    geocode:-23.555488,-46.600370,40km url:fb.me “Gravidez”
    geocode:-23.555488,-46.600370,50km (wa.me OR fb.me) “Hacked”
    geocode:-23.555488,-46.600370,50km (wa.me OR fb.me) “Fake news”
    geocode:-23.555488,-46.600370,50km url:wa.me until:2020–08–01
    geocode:-23.555488,-46.600370,50km filter:links
```

## Geotagging: GeoSocial Footprint

### GeoSocial Fooprint

A geosocial footprint is the combined bits of location information that a user divulges through social media, which ultimately forms the users location "footprint". For Twitter.com users, this footprint is created from GPS enabled tweets, social check-ins, natural language location searching (geocoding), and profile harvesting.

***

## REFERENCES

* 
