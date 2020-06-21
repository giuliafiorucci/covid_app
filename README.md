![](https://github.com/giuliafiorucci/covid_app/workflows/integration/badge.svg)
# Covid App
Dash App on Covid deployed to Heroku

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

# WIP Links
https://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py
https://wiki.openstreetmap.org/wiki/Shapefiles
https://gist.github.com/frankrowe/6071443
https://stackoverflow.com/questions/43119040/shapefile-into-geojson-conversion-python-3
https://towardsdatascience.com/mapping-geograph-data-in-python-610a963d2d7f

http://www.pcn.minambiente.it/mattm/servizi/
https://www.eea.europa.eu/data-and-maps/data/eea-reference-grids-2/gis-files/italy-shapefile
http://hub.arcgis.com/datasets/inspire-esri::municipal-boundaries-of-italy-2019?geometry=-39.614%2C28.929%2C65.767%2C51.950
https://wiki.openstreetmap.org/wiki/ArcGIS

# Build
`tox`