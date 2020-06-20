![](https://github.com/giuliafiorucci/covid_app/workflows/integration/badge.svg)
# Covid App
Yet another interactive app on Covid, deployed to Heroku

# Installation geopandas windows
```
conda create -y -n geo_env python==3.7
conda activate geo_env
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda config --env --add channels conda-forge
conda install python==3.7 geopandas
conda install -y pyshp
conda install -y --file ./requirements.txt
```

# Build (broken)
`tox`, but tox uses `pip` so it can't install geopandas properly... need to solve this
## Build links
- https://stackoverflow.com/questions/30555943/is-it-possible-to-use-tox-with-conda-based-python-installations

# WIP Links
## Plotly and Geopandas
- https://plotly.com/python/choropleth-maps/
- https://plotly.github.io/plotly.py-docs/generated/plotly.express.choropleth.html
- https://community.plotly.com/t/choropleth-maps-with-custom-geojson/35756
- https://plotly.github.io/plotly.py-docs/generated/plotly.express.choropleth_mapbox.html
- http://vincepota.com/plotly_choropleth_map.html
- http://andrewgaidus.com/leaflet_webmaps_python/
- http://darribas.org/gds15/content/labs/lab_03.html
- https://geopandas.org/mergingdata.html
- https://geopandas.org/aggregation_with_dissolve.html
- https://stackoverflow.com/questions/40385782/make-a-union-of-polygons-in-geopandas-or-shapely-into-a-single-geometry
- https://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py
- https://gist.github.com/frankrowe/6071443
- https://towardsdatascience.com/mapping-geograph-data-in-python-610a963d2d7f
- https://gis.stackexchange.com/questions/74808/extract-a-record-by-name-in-pyshp

## GIS
- http://hub.arcgis.com/datasets/inspire-esri::municipal-boundaries-of-italy-2019?geometry=-39.614%2C28.929%2C65.767%2C51.950
- https://wiki.openstreetmap.org/wiki/ArcGIS
- https://www.openstreetmap.org/export#map=10/42.9690/11.4134
- https://download.geofabrik.de/europe/italy.html
- https://wiki.openstreetmap.org/wiki/Shapefiles
- https://www.eea.europa.eu/data-and-maps/data/eea-reference-grids-2/gis-files/italy-shapefile

## Layouts
- https://dash.plotly.com/interactive-graphing
- https://plotly.com/python/scatter-plots-on-maps/
- https://plotly.com/python/choropleth-maps/

- https://towardsdatascience.com/lets-make-a-map-using-geopandas-pandas-and-matplotlib-to-make-a-chloropleth-map-dddc31c1983d
- https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0
- https://towardsdatascience.com/mapping-geograph-data-in-python-610a963d2d7f, shape files
- https://www.naturalearthdata.com/downloads/

## Bokeh
- https://cbouy.github.io/blog/2019/06/09/interactive-map
- https://data-dive.net/cologne-bike-rentals-interactive-map-bokeh
- https://docs.bokeh.org/en/latest/docs/gallery/texas.html
- https://www.activestate.com/blog/dash-vs-bokeh/
- https://docs.bokeh.org/en/latest/docs/user_guide/server.html
