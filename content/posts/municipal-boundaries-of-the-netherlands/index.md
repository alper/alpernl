---
author: alper
categories:
  - english
  - monster-swell
  - product-/-design
  - the-city
date: "2010-09-29T02:20:14+00:00"
title: Municipal boundaries of the Netherlands
aliases:
  - /dingen/2010/03/municipal-boundaries-of-the-netherlands/

---
### Goal

I want to create a simple visualization tool for [Processing](http://processing.org) so I can input a set of values for each Dutch municipality and then color a map based on those values.

This is harder than it seems because there is no convenient source for the cartographic data for the boundaries of [the Dutch municipalities](http://en.wikipedia.org/wiki/Municipalities_in_the_Netherlands). So the first step is to acquire those boundaries.

### OSM

This [blogpost in Dutch](http://oegeo.wordpress.com/2008/11/18/gemeentegrenzen-uit-openstreetmap/) put me on track for this dataset. [OpenStreetMap](http://www.openstreetmap.org/) has a pretty complete picture of the Netherlands and they track municipal boundaries under [boundary admin\_level=8](http://wiki.openstreetmap.org/wiki/Map_features#Boundary).

The data dump contains all administrative boundaries on several levels and is something of a mess. The informationfreeway link on the blogpost which should generate an OSM file with only the relations with `admin_level=8` but that specific API seems to be down. Also the approach of importing the OSM file back into a PostGIS database before rendering anything struck me as somewhat too cumbersome. So an alternative approach was called for.

There are some readily [available dumps at CloudMade](http://downloads.cloudmade.com/europe/netherlands#breadcrumbs) both with OSM files ( [format](http://en.wikipedia.org/wiki/OpenStreetMap#Data_format)) and Shapefiles for these administrative boundaries. That seemed to be a useful starting point.

An OSM file is just an XML file with series of `nodes`, `ways` and `relations` in it. It is filterable by the generic processing tool [Osmosis](http://wiki.openstreetmap.org/wiki/Osmosis) with the options that I guessed `--way-key-value` to filter ways with the admin\_level tag and `--node-key-value` to do the same for nodes. Osmosis does not specify anything for relations which I want to preserve to be able to identify each boundary by the name of the municipality.

Having done that, the resulting OSM file needed to be drawn to the screen. I made a simple XML reader in Processing to display the resulting boundaries. The result did not seem to be completely what I wanted both with missing and unlinked geographical features and I think not everything properly labelled. For this particular application a wiki-map does not seem like the most suitable source of data.

### CBS

 [CBS](http://www.cbs.nl) (the Dutch statistics office) also [provides a dataset with administrative boundaries](http://www.cbs.nl/nl-NL/menu/themas/dossiers/nederland-regionaal/publicaties/geografische-data/archief/2007/2006-wijk-en-buurtkaart.htm) of the Netherlands. It is a bit hard to track down on the site and there's a reference to the [Kadaster](http://www.kadaster.nl/) which isn't entirely clear, but the generalized [Shapefile](http://en.wikipedia.org/wiki/Shapefile) is workable.

One problem is that Shapefiles are only understood properly by GIS people and there are hardly any libraries for web developers to work with the data format. Sunlight Labs recently released their [ClearMaps library](http://sunlightlabs.com/blog/2010/clearmaps-mapping-framework/) to aid developers wanting to work with Shapefiles, which is a big step in the right direction.

Another problem is that the file on the CBS site is from 2006 and that several municipalities have merged/split, so that adds some problems for correlating it to data. And come to think of it, this municipal rejiggering makes any historical data view of the Netherlands a daunting task. Somebody on Wikipedia has generated [a similar map of the Netherlands](http://nl.wikipedia.org/wiki/Bestand:2010-Nederlandse-Gemeenten-1790.png) for 2010 supposedly using data from the CBS, but I can't find that dataset on the site ((Nor can I find anything else there, but that is a different story.)).

Oddly enough there's also nothing readily available to draw Shapefiles in Processing. Perusing the forum yields [this post](http://processing.org/discourse/yabb2/YaBB.pl?board=LibraryProblems;action=display;num=1189739304) which points to [Geotools](http://geotools.org/) which is a massive set of Java libraries consisting mostly of [a huge dependency nightmare](http://geotools.org/quickstart.html#quickstart) mitigated somewhat by Eclipse and Maven.

### Geographical data

Viewing the Shapefile in qGIS shows that it does indeed contain the municipal boundaries with correct labeling. Having verified that, we need to extract the geographical data from the file into a format for easier reuse. Linking all the Geotools ((Another alternative would have been a Python binding to [GDAL/OGR](http://gdal.org/ogr/) which looked even less tractable.)) dependencies to my Processing sketch does not seem like an attractive proposition. Using the Geotools quickstart to setup Eclipse to pull in the libraries and run the Java code, did work pretty conveniently.

Poking around the Shapefile with Java and using the very poor javadocs (the [User Guide's](http://docs.codehaus.org/display/GEOTDOC/Home) usefulness turned out to be extremely limited) and sources posted online that are available of Geotools yielded something worthwhile after a full day's work. I also found lots of forum posts of very confused people with few replies and little insight to be gleaned from them. This really seems to be an underdeveloped field.

It turns out the Shapefile read with Geotools contains [`SimpleFeature`](http://www.geoapi.org/snapshot/pending/org/opengis/feature/simple/SimpleFeature.html) classes ( [UML](http://docs.codehaus.org/display/GEOTDOC/Feature) for those, and the [Wikipedia lemma for the OpenGIS standard](http://en.wikipedia.org/wiki/Simple_Features)) of which you can call the [`getDefaultGeometry()`](http://www.geoapi.org/snapshot/pending/org/opengis/feature/simple/SimpleFeature.html#getDefaultGeometry()) methods.

Geotools also provides a default [`Drawer.java`](http://svn.osgeo.org/geotools/branches/geocat/modules/library/render/src/main/java/org/geotools/legend/Drawer.java) which you can use to [display the features](http://www.geotools.org/examples/crslab.html#displaying-the-shapefile) (via [`LiteShapes`](http://javadoc.geotools.fr/2.6/org/geotools/geometry/jts/LiteShape.html)) in the Shapefile using Java AWT Graphics. This turned out to be useful mainly for debugging purposes and to verify that Geotools does indeed properly read in the Shapefile. Using a [`GeomCollectionIterator`](http://geosysin.iict.ch/irstv-trac/browser/platform/orbisgis-core/src/main/java/org/orbisgis/renderer/liteShape/GeomCollectionIterator.java?rev=4753) to walk through the points and extract the coordinates that way turned out to be a dead end (especially because I didn't get the role of the various [Transforms](http://geotools.org/javadocs/org/geotools/referencing/operation/transform/GeocentricTranslation.html)).

Another idea was to generate SVG from the Shapefile but the [`GenerateSVG`](http://udig.refractions.net/files/docs/api-geotools/org/geotools/svg/GenerateSVG.html) class did not seem to be included in my library checkout and fiddling with the maven file seemed risky.

Finally the following piece of code yielded for me the two pieces of data I was looking for, the names of the municipalities and the content of the SimpleFeatures as MULTIPOLYGONs.

```

  String gemShapefile = "/Users/alper/Documents/projects/muniboundaries/cbs/buurt_2008_gen2/gem_2008_gn2.shp";
  File file = new File(gemShapefile);

  FileDataStore store = FileDataStoreFinder.getDataStore(file);
  FeatureSource featureSource = store.getFeatureSource();

  FeatureCollection features = featureSource.getFeatures();
  FeatureIterator iter = features.features();

  int counter = 0;

  PrintWriter pw = new PrintWriter(new FileWriter("/tmp/geo.txt"));

  while(iter.hasNext()) {
  	SimpleFeature feature = iter.next();

  	Collection props = feature.getProperties();

  	if (counter > 0) {
  		String gemNaam = "";
  		String geoWKT = "";

    	for (Iterator it = props.iterator(); it.hasNext();) {
		Property property = it.next();

		if (property.getName().getLocalPart().equals("the_geom")) {
			geoWKT = property.getValue().toString();
		}

		if (property.getName().getLocalPart().equals("GM_NAAM")) {
			gemNaam = property.getValue().toString();
		}
	}

    	pw.println(gemNaam + "; " + geoWKT);

    	System.out.println(gemNaam);
  	}

  	counter++;
  }

  pw.close();

```

The funny thing is every feature has a property “the\_geom”which contains the geometry data and its `toString()` method yields the geometry data as [Well-known text](http://en.wikipedia.org/wiki/Well-known_text). That turned out to be all we needed.

It turns out the coordinates in the Shapefile are in [Rijksdriehoekscoördinaten](http://nl.wikipedia.org/wiki/Rijksdriehoekscoördinaten) ((Seemingly you can put anything you want in a Shapefile also given the vast diversity in geodetic datums which are in use around the globe.)) which are cartesian coordinates based on a custom projection and associated rectangular grid for the Netherlands ((This is something I couldn't figure out anywhere, what the agreement was —if any— for the contents of the coordinates in the Shapefile. My question: “How do I get GPS coordinates from a Shapefile?”did not yield any answers.)). This is easily verified using [this web form to convert a pair](http://www.rdnap.nl/cgi-bin/rdetrs.pl) back to GPS and looking that up in Google Maps ((I have the formulas in a dense PDF, but some sample Java code to do the conversion would be very nice.)).

The above code produces lines such as:
`Leek; MULTIPOLYGON ( ( (224599.999985 582499.999985, 224999.999985 581299.999985, […] 223366.621185 581866.621185, 223499.999985 581999.999985, 224440.97068499998 582470.485385, 224499.999985 582499.999985, 224599.999985 582499.999985)))`

This is a simple list of coordinates that define the boundaries of the polygons. A MULTIPOLYGON contains one or more POLYGONS. A POLYGON is one list of the boundary with zero or more lists defining any holes within that boundary. I figured that out looking at [the specification for GeoJSON](http://wiki.geojson.org/GeoJSON_draft_version_6#MultiPolygon) (same data model, different markup) which is the format I am going to republish this information in.

### Drawing

With these coordinates, it became quite easy to write a Processing sketch to draw these boundaries. I looked up a datasource for the last European elections and hooked that up for the colors.

[![Results of the 2009 elections for European Parliament](http://farm5.static.flickr.com/4047/4388299738_edc0cd2922_m.jpg)](http://www.flickr.com/photos/alper/4388299738/ "Results of the 2009 elections for European Parliament by illustir, on Flickr")

Making iterative sketches in Processing with Eclipse is somewhat cumbersome because you need to utilize quite a high level of abstraction if you don't want your classes to interfere with each other but still Eclipse allows me to work quickly and lets you write Java 1.5 level code against the Processing core.jar (that alone is worth the effort).

I'm going to release a generic Processing sketch where you only need to add a data file with colors or values for each name. Publication as these boundaries as both GeoJSON and SVG is also forthcoming. I'm also looking for the more recent 2010 Shapefile from the CBS with all the current municipal boundaries in it. If there's demand I can also extract the living quarter and neighborhood level administrative boundaries which are in the other Shapefiles.

**Update:** Some research shows there's a very promising avenue to do this stuff by converting the entire Shapefile to GeoJSON as explained in [this StackOverflow post](http://stackoverflow.com/questions/2223979/convert-a-shapefile-shp-to-xml-json) and then drawing thath using either ProcessingJS or [OpenLayers](http://openlayers.org/).

**Update:** Managed to convert the data to [GeoJSON](http://www.geojson.org/) and draw it using [ProcessingJS](http://processingjs.org/):
[![Processing the Netherlands](http://farm3.static.flickr.com/2707/4417261722_6b6f994d1e_m.jpg)](http://www.flickr.com/photos/alper/4417261722/ "Processing the Netherlands by illustir, on Flickr")

This opens up a ton of possibilities for interactive visualization and sharing. More to follow.
