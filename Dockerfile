FROM continuumio/miniconda3:latest as base

WORKDIR /app
COPY deploy /app/deploy
COPY requirements /app/requirements
RUN sed -i 's/\r$//' ./deploy/conda_install.sh
RUN ["bash",  "./deploy/conda_install.sh"]

ADD . /app/

#FROM base as test
#RUN rm -fr .tox && tox -r

FROM base as runtime

RUN useradd -m myuser
USER myuser
ARG port=${PORT}
CMD waitress-serve --port=$port src.appdash.main:server