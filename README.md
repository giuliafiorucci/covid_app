![](https://github.com/giuliafiorucci/covid_app/workflows/integration/badge.svg)
# Covid App
Yet another interactive app on Covid, deployed to Heroku

# Installation geopandas windows
```
conda create -y -n geo_env python==3.8
conda activate geo_env
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda config --env --add channels conda-forge
conda install -y python=3 geopandas
conda install -y pyshp
conda install -y --file ./requirements.txt

conda env create -f environment.yml
```

# Build (broken)
`tox` uses `pip` so it can't install geopandas properly. Explored solutions so far 
 1. `tox-conda` to use `conda` as package manager, but it didn't work due to the 
    highly customised installation phase
 2. Using `docker` to provision the conda environment and run the tests. Did not
    work as tox always tries to build its own environments (duh!). 
    - I added `tox-current-env` to let tox use the provisioned environment to run
    the tests. It failed for some unknown reason.
