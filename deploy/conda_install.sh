conda config --prepend channels conda-forge && \
conda config --set channel_priority strict && \
conda install --yes geopandas && \
conda install --yes pyshp && \
conda clean -afy && \
conda install --yes --file ./requirements/common.txt && \
conda install --yes --file ./requirements/testing.txt && \
conda install --yes --file ./requirements/prod.txt && \
conda clean -afy