# VERSION 1.0

FROM krallin/ubuntu-tini:trusty

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Install basic pre-requisite packages
RUN apt-get update \
    && apt-get install -y \
        wget \
        libffi-dev \
        zlib1g-dev \
        libxslt1-dev \
        libcurl4-openssl-dev \
        python-virtualenv

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Miniconda
RUN wget -q https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
    && /bin/bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/miniconda2 \
    && rm Miniconda2-latest-Linux-x86_64.sh

ENV PATH /opt/miniconda2/bin:$PATH

# Install jupyter kernel gateway
RUN conda install --quiet --yes \
    jupyter \
    && conda clean -ay

# Create a directory to hold the GA4GH server code
RUN mkdir /srv/ga4gh
WORKDIR /srv/ga4gh

# Make a virtualenv, and install the ga4gh package
RUN virtualenv ga4gh-server-env \
    && /bin/bash -c "source ga4gh-server-env/bin/activate" \
    && pip install ga4gh

# Configure container startup
WORKDIR /home
EXPOSE 8888
ENTRYPOINT ["tini", "--", "jupyter", "notebook"]

# Add local files as late as possible to avoid cache busting
COPY jupyter_notebook_config.py /root/.jupyter/
