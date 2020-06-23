FROM continuumio/miniconda3:latest as base
COPY . /app
WORKDIR /app
RUN conda config --prepend channels conda-forge && \
    conda config --set channel_priority strict && \
    conda install --yes geopandas && \
    conda install --yes pyshp && \
    conda install --yes --file ./requirements/common.txt && \
    conda install --yes --file ./requirements/testing.txt && \
    conda clean -afy

FROM base as test
RUN rm -fr .tox && tox -r

FROM base as runtime
ENTRYPOINT ["bash"]