# VERSION 1.0

FROM ubuntu:latest

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# See http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html
# Install Oracle Java 8
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:webupd8team/java \
    && apt-get update \
    && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
    && apt-get install -y \
        oracle-java8-installer \
        oracle-java8-set-default

# Install Python2, VIM, screen, Git
RUN apt-get update \
    && apt-get install -y \
        python \
        vim \
        screen \
        git

RUN rm -r /var/lib/apt/lists/*
