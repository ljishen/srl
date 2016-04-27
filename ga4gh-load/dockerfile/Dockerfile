# VERSION 1.0

FROM ubuntu:latest

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Install Prerequisites
RUN apt-get update \
    && apt-get install -y \
        python-pip \ 
        python-dev \
        git \
        vim \
    && pip install --upgrade paramiko PyYAML Jinja2 httplib2 six

WORKDIR /opt

# Install Ansible From Source
RUN git clone git://github.com/ansible/ansible.git --recursive

WORKDIR /opt/ansible

# Compiling Ansible
RUN bash -c 'source ./hacking/env-setup'

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH /opt/ansible/bin:$PATH
ENV PYTHONPATH /opt/ansible/lib:$PYTHONPATH

WORKDIR /root
ADD ansible.cfg ansible.cfg
ADD entrypoint.sh entrypoint.sh
ADD hosts hosts

ENTRYPOINT ["entrypoint.sh"]
