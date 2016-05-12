# VERSION 1.0

FROM ubuntu:latest 

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Install basic pre-requisite packages & enable mod_wsgi 
RUN apt-get update \
    && apt-get install -y \
        python-dev \
        python-pip \
        python-virtualenv \
        zlib1g-dev \
        libxslt1-dev \
        libffi-dev \
        libssl-dev \
        libcurl4-openssl-dev \
        apache2 \
        libapache2-mod-wsgi

# Create the Python egg cache directory,
# and make it writable by the www-data user
RUN mkdir /var/cache/apache2/python-egg-cache \
    && chown www-data:www-data /var/cache/apache2/python-egg-cache/

# Create a directory to hold the GA4GH server code,
# configuration and data
RUN mkdir /srv/ga4gh
WORKDIR /srv/ga4gh

# Make a virtualenv, and install the ga4gh package
RUN virtualenv ga4gh-server-env \
    && /bin/bash -c "source ga4gh-server-env/bin/activate" \
    && pip install ga4gh

# Create configuration files
COPY application.wsgi /srv/ga4gh/application.wsgi
COPY config.py /srv/ga4gh/config.py
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80

# Start server when container starts
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
