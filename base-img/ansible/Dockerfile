# VERSION 1.1

FROM ubuntu:latest

MAINTAINER Jianshen Liu <jliu120@ucsc.edu>

# Install Prerequisites
# Note: libffi-dev is required for paramiko
RUN apt-get update \
    && apt-get install -y \
        python-pip \
        python-dev \
        libffi-dev \
        libssl-dev \
        sshpass \
        git \
    && pip install --upgrade pycrypto paramiko PyYAML Jinja2 httplib2 six

WORKDIR /opt

# Install Ansible From Source
RUN git clone git://github.com/ansible/ansible.git --recursive --branch v2.0.2.0-1

WORKDIR /opt/ansible

# Compiling Ansible
RUN bash -c 'source ./hacking/env-setup'

# Clean Up
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH /opt/ansible/bin:$PATH
ENV PYTHONPATH /opt/ansible/lib:$PYTHONPATH

ENTRYPOINT ["ansible-playbook"]
CMD ["--version"]
