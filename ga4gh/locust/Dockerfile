# VERSION 1.0

FROM ubuntu:latest 

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Install Locust
RUN apt-get update \
    && apt-get install -y \
        python-pip \ 
        python-dev \
    && pip install --upgrade locustio pyzmq 

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# May need to increase the maximum number of open files

WORKDIR /root
